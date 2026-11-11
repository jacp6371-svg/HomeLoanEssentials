// Contact form on the homepage: validates, then posts to /api/contact (Vercel function).
async function submitContactForm() {
  const btn = document.getElementById('cf-submit');
  const errBox = document.getElementById('cf-error');
  const succBox = document.getElementById('cf-success');
  const name = document.getElementById('cf-name').value.trim();
  const email = document.getElementById('cf-email').value.trim();
  const phone = document.getElementById('cf-phone').value.trim();
  const service = document.getElementById('cf-service').value;
  const message = document.getElementById('cf-message').value.trim();
  const honeypot = document.getElementById('_honeypot').value;

  errBox.style.display = 'none';
  succBox.style.display = 'none';

  // Client-side validation
  const errs = [];
  if (name.length < 2) errs.push('Please enter your full name.');
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) errs.push('Please enter a valid email address.');
  if (message.length < 10) errs.push('Please enter a message (at least 10 characters).');
  if (errs.length) {
    errBox.textContent = errs.join(' ');
    errBox.style.display = 'block';
    return;
  }

  btn.disabled = true;
  btn.textContent = 'Sending...';

  try {
    const res = await fetch('/api/contact', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ name, email, phone, service, message, _honeypot: honeypot })
    });
    const data = await res.json();
    if (res.ok && data.ok) {
      succBox.style.display = 'block';
      document.getElementById('cf-name').value = '';
      document.getElementById('cf-email').value = '';
      document.getElementById('cf-phone').value = '';
      document.getElementById('cf-service').value = '';
      document.getElementById('cf-message').value = '';
    } else {
      errBox.textContent = data.error || 'Something went wrong. Please email jack@homeloanessentials.com.au directly.';
      errBox.style.display = 'block';
    }
  } catch (e) {
    errBox.textContent = 'Network error. Please check your connection or email jack@homeloanessentials.com.au directly.';
    errBox.style.display = 'block';
  } finally {
    btn.disabled = false;
    btn.textContent = 'Send Message';
  }
}
