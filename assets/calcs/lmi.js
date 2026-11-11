// Lenders Mortgage Insurance: indicative estimate from a simplified table.
// TODO (Jack): these premium rates are illustrative, not from any insurer. Compare them with a lender's LMI calculator
// and adjust the table below before relying on it.
(function () {
  // Premium as % of loan, by loan size band (rows) and LVR band (columns: 80-85, 85-90, 90-95, 95+)
  var TABLE = [
    { upTo: 500000, rates: [0.65, 1.35, 2.6, 3.4] },
    { upTo: 750000, rates: [0.85, 1.75, 3.2, 4.0] },
    { upTo: 1000000, rates: [1.05, 2.1, 3.7, 4.5] },
    { upTo: Infinity, rates: [1.3, 2.5, 4.2, 5.0] }
  ];
  HLE.calculator('calcForm', 'lmi', function () {
    var value = HLE.num('lmi-value'), loan = HLE.num('lmi-loan'), fhb = HLE.checked('lmi-fhb'), qld = HLE.checked('lmi-qld');
    var lvr = value > 0 ? loan / value * 100 : 0;
    HLE.set('lmi-lvr', HLE.pct(lvr, 1));
    HLE.set('lmi-avoid', HLE.aud(Math.max(0, value * 0.2)) + ' (20%)');
    var notes = [];
    if (lvr <= 80) {
      HLE.set('lmi-est', '$0');
      HLE.set('lmi-sub', 'At 80% LVR or less, LMI is not usually charged.');
      HLE.set('lmi-range', '–');
    } else {
      var row = TABLE.filter(function (t) { return loan <= t.upTo; })[0];
      var col = lvr <= 85 ? 0 : lvr <= 90 ? 1 : lvr <= 95 ? 2 : 3;
      var est = loan * row.rates[col] / 100;
      HLE.set('lmi-est', HLE.aud(est));
      HLE.set('lmi-sub', 'Indicative only. LMI varies by lender and insurer.');
      HLE.set('lmi-range', HLE.aud(est * 0.75) + ' to ' + HLE.aud(est * 1.25));
      if (lvr > 95) notes.push('Very few lenders go above 95% LVR, usually only with a guarantor or special program.');
    }
    if (fhb && lvr > 80) {
      var cap = qld ? 'In Queensland the price cap is $1,000,000 in the capital city and regional centres (including the Gold Coast and Sunshine Coast) and $700,000 elsewhere.' : 'Price caps vary by state and area.';
      notes.push('As a first home buyer you may be able to avoid LMI with a 5% deposit under the Australian Government 5% Deposit Scheme. ' + cap + ' Check eligibility with Jack.');
    }
    notes.push('Eligible doctors, lawyers and accountants may be able to have LMI reduced or waived.');
    HLE.set('lmi-note', notes.join(' '));
  });
})();
