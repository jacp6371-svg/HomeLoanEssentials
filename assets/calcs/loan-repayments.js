// Loan repayments: P&I or interest only, weekly/fortnightly/monthly.
HLE.calculator('calcForm', 'loan_repayments', function () {
  var P = HLE.num('lr-amount'), r = HLE.num('lr-rate'), n = HLE.num('lr-term') || 30;
  var f = parseInt((document.querySelector('input[name="lr-freq"]:checked') || {}).value || '12', 10);
  var type = (document.querySelector('input[name="lr-type"]:checked') || {}).value || 'pi';
  var io = Math.min(Math.max(HLE.num('lr-io'), 1), Math.max(n - 1, 1));
  var label = { 52: 'week', 26: 'fortnight', 12: 'month' }[f];
  var ioField = document.getElementById('lr-io');
  if (ioField) ioField.closest('.field').style.opacity = type === 'io' ? '1' : '.5';
  var pay, total, interest, after = '–';
  if (type === 'io') {
    pay = P * r / 100 / f;
    var rest = (n - io) * f;
    var piPay = HLE.payment(P, r, rest, f);
    total = pay * io * f + piPay * rest;
    after = HLE.aud(piPay, true) + ' per ' + label + ' for ' + (n - io) + ' years';
    HLE.set('lr-sub', 'Per ' + label + ' during the ' + io + '-year interest-only period.');
  } else {
    pay = HLE.payment(P, r, n * f, f);
    total = pay * n * f;
    HLE.set('lr-sub', 'Per ' + label + ' over ' + n + ' years.');
  }
  interest = total - P;
  HLE.html('lr-pay', HLE.aud(pay, true) + ' <small>/ ' + label + '</small>');
  HLE.set('lr-interest', HLE.aud(interest));
  HLE.set('lr-total', HLE.aud(total));
  HLE.set('lr-after', after);
});
