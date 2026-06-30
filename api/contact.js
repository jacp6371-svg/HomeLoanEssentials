// Vercel Serverless Function — Contact Vault
// Required environment variables (set in Vercel project settings):
//   RESEND_API_KEY   — your Resend API key (get one free at resend.com)
//   TO_EMAIL         — email address to receive enquiries (e.g. jack@homeloanessentials.com.au)
//   FROM_EMAIL       — verified sender address in Resend (e.g. noreply@homeloanessentials.com.au)
//                      OR use 'onboarding@resend.dev' while testing before domain is verified

export default async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, phone, service, message, _honeypot } = req.body || {};

  // Spam trap — bots fill hidden fields, humans don't
  if (_honeypot) {
    console.log('[contact] Honeypot triggered — spam blocked');
    return res.status(200).json({ ok: true }); // silent accept to fool bots
  }

  // Validate required fields
  const errors = [];
  if (!name || name.trim().length < 2) errors.push('Full name is required.');
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errors.push('A valid email address is required.');
  if (!message || message.trim().length < 10) errors.push('Message must be at least 10 characters.');

  if (errors.length > 0) {
    return res.status(400).json({ error: errors.join(' ') });
  }

  const apiKey = process.env.RESEND_API_KEY;
  const toEmail = process.env.TO_EMAIL || 'jack@homeloanessentials.com.au';
  const fromEmail = process.env.FROM_EMAIL || 'onboarding@resend.dev';

  // Always log the submission so it's visible in Vercel logs (backup)
  console.log('[contact] New enquiry:', JSON.stringify({ name, email, phone, service, message, ts: new Date().toISOString() }));

  if (!apiKey) {
    console.error('[contact] RESEND_API_KEY is not set — email not sent');
    return res.status(500).json({ error: 'Email service is not configured. Please contact jack@homeloanessentials.com.au directly.' });
  }

  const emailHtml = `
    <div style="font-family:Arial,sans-serif;max-width:600px;margin:0 auto;color:#1c2b27">
      <div style="background:#1c2b27;padding:24px 32px;border-radius:8px 8px 0 0">
        <h1 style="color:#4a9a72;margin:0;font-size:20px">New Contact Vault Enquiry</h1>
        <p style="color:rgba(255,255,255,0.5);margin:4px 0 0;font-size:13px">${new Date().toLocaleString('en-AU', { timeZone: 'Australia/Brisbane' })} AEST</p>
      </div>
      <div style="background:#f0ede6;padding:32px;border-radius:0 0 8px 8px">
        <table style="width:100%;border-collapse:collapse">
          <tr><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:13px;color:#4a5e58;width:120px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em">Name</td><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:15px;color:#1c2b27">${escHtml(name)}</td></tr>
          <tr><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:13px;color:#4a5e58;font-weight:600;text-transform:uppercase;letter-spacing:0.05em">Email</td><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:15px"><a href="mailto:${escHtml(email)}" style="color:#2a5c45">${escHtml(email)}</a></td></tr>
          <tr><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:13px;color:#4a5e58;font-weight:600;text-transform:uppercase;letter-spacing:0.05em">Phone</td><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:15px;color:#1c2b27">${escHtml(phone || '—')}</td></tr>
          <tr><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:13px;color:#4a5e58;font-weight:600;text-transform:uppercase;letter-spacing:0.05em">Service</td><td style="padding:10px 0;border-bottom:1px solid #e8e3d9;font-size:15px;color:#1c2b27">${escHtml(service || '—')}</td></tr>
          <tr><td style="padding:10px 0;font-size:13px;color:#4a5e58;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;vertical-align:top">Message</td><td style="padding:10px 0;font-size:15px;color:#1c2b27;white-space:pre-wrap">${escHtml(message)}</td></tr>
        </table>
        <div style="margin-top:24px;padding:16px;background:#e8f5ee;border-radius:6px;border-left:3px solid #2a5c45">
          <p style="margin:0;font-size:13px;color:#2a5c45">Reply directly to this email to respond to ${escHtml(name)}.</p>
        </div>
      </div>
    </div>
  `;

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: `Home Loan Essentials <${fromEmail}>`,
        to: [toEmail],
        reply_to: email,
        subject: `Contact Vault: New enquiry from ${name}`,
        html: emailHtml,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('[contact] Resend error:', JSON.stringify(data));
      return res.status(500).json({ error: 'Failed to send enquiry. Please email jack@homeloanessentials.com.au directly or call 0478 938 981.' });
    }

    console.log('[contact] Email sent successfully. Resend ID:', data.id);
    return res.status(200).json({ ok: true });

  } catch (err) {
    console.error('[contact] Unexpected error:', err.message);
    return res.status(500).json({ error: 'An unexpected error occurred. Please email jack@homeloanessentials.com.au directly.' });
  }
}

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
