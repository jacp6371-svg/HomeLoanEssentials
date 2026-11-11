// Home Loan Essentials: small helpers shared by every calculator.
// Results are estimates and general information only.
(function () {
  var HLE = window.HLE = window.HLE || {};

  var aud0 = new Intl.NumberFormat('en-AU', { style: 'currency', currency: 'AUD', maximumFractionDigits: 0 });
  var aud2 = new Intl.NumberFormat('en-AU', { style: 'currency', currency: 'AUD', minimumFractionDigits: 2, maximumFractionDigits: 2 });
  HLE.aud = function (n, cents) { if (!isFinite(n)) return '–'; return (cents ? aud2 : aud0).format(Math.round(n * (cents ? 100 : 1)) / (cents ? 100 : 1)); };
  HLE.pct = function (n, d) { return isFinite(n) ? n.toFixed(d == null ? 1 : d) + '%' : '–'; };
  HLE.years = function (months) {
    var y = Math.floor(months / 12), m = Math.round(months % 12);
    if (m === 12) { y += 1; m = 0; }
    return y + (y === 1 ? ' year' : ' years') + (m ? ', ' + m + (m === 1 ? ' month' : ' months') : '');
  };

  // Read a number from an input: accepts "650,000", "$650k", "6.2"
  HLE.num = function (id) {
    var el = typeof id === 'string' ? document.getElementById(id) : id;
    if (!el) return 0;
    if (el.type === 'checkbox') return el.checked ? 1 : 0;
    var raw = String(el.value).trim().toLowerCase().replace(/[$,\s]/g, '');
    var mult = 1;
    if (/k$/.test(raw)) { mult = 1e3; raw = raw.slice(0, -1); }
    else if (/m$/.test(raw)) { mult = 1e6; raw = raw.slice(0, -1); }
    var n = parseFloat(raw);
    return isFinite(n) ? Math.max(0, n * mult) : 0;
  };
  HLE.val = function (id) { var el = document.getElementById(id); return el ? el.value : ''; };
  HLE.checked = function (id) { var el = document.getElementById(id); return !!(el && el.checked); };
  HLE.set = function (id, text) { var el = document.getElementById(id); if (el) el.textContent = text; };
  HLE.html = function (id, h) { var el = document.getElementById(id); if (el) el.innerHTML = h; };

  // Repayment per period for principal P, annual rate r (%), n periods, f periods per year
  HLE.payment = function (P, ratePct, nPeriods, perYear) {
    var i = ratePct / 100 / perYear;
    if (nPeriods <= 0) return 0;
    if (i === 0) return P / nPeriods;
    return P * i / (1 - Math.pow(1 + i, -nPeriods));
  };
  // Present value: how much a payment per period can service
  HLE.presentValue = function (pmt, ratePct, nPeriods, perYear) {
    var i = ratePct / 100 / perYear;
    if (pmt <= 0 || nPeriods <= 0) return 0;
    if (i === 0) return pmt * nPeriods;
    return pmt * (1 - Math.pow(1 + i, -nPeriods)) / i;
  };
  // Balance remaining after k payments
  HLE.balanceAfter = function (P, ratePct, nPeriods, perYear, k) {
    var i = ratePct / 100 / perYear, pmt = HLE.payment(P, ratePct, nPeriods, perYear);
    if (i === 0) return Math.max(0, P - pmt * k);
    return Math.max(0, P * Math.pow(1 + i, k) - pmt * (Math.pow(1 + i, k) - 1) / i);
  };

  // Australian resident income tax 2026-27 plus 2% Medicare levy (ATO, checked 11 Nov 2026).
  // Ignores offsets, the Medicare levy low-income reduction and HELP repayments.
  HLE.netIncome = function (gross) {
    var t = 0;
    if (gross > 190000) t = 51370 + (gross - 190000) * 0.45;
    else if (gross > 135000) t = 31020 + (gross - 135000) * 0.37;
    else if (gross > 45000) t = 4020 + (gross - 45000) * 0.30;
    else if (gross > 18200) t = (gross - 18200) * 0.15;
    var medicare = gross > 30000 ? gross * 0.02 : 0;
    return Math.max(0, gross - t - medicare);
  };

  // Wire up a calculator: recalculates on every input, tracks first use once per page view
  HLE.calculator = function (formId, name, fn) {
    var form = document.getElementById(formId);
    if (!form) return;
    var used = false;
    var run = function (e) {
      try { fn(); } catch (err) { if (window.console) console.error(err); }
      if (e && !used) { used = true; if (window.hleTrack) window.hleTrack('calculator_used', { calculator_name: name }); }
    };
    form.addEventListener('input', run);
    form.addEventListener('change', run);
    form.addEventListener('submit', function (e) { e.preventDefault(); run(e); });
    run();
  };

  // Simple horizontal comparison bars (no library)
  HLE.bars = function (id, rows) {
    var max = Math.max.apply(null, rows.map(function (r) { return r.value; }).concat([1]));
    HLE.html(id, rows.map(function (r) {
      var w = Math.max(2, Math.round(r.value / max * 100));
      return '<div class="bar-row"><div class="bar-label"><span>' + r.label + '</span><strong>' + HLE.aud(r.value) + '</strong></div>' +
        '<div class="bar-track"><span class="bar-fill ' + (r.cls || '') + '" style="width:' + w + '%"></span></div></div>';
    }).join(''));
  };
})();
