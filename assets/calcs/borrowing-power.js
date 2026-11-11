// Borrowing power: indicative estimate. See the assumptions on the page.
HLE.calculator('calcForm', 'borrowing_power', function () {
  var inc1 = HLE.num('bp-inc1'), inc2 = HLE.num('bp-inc2'), other = HLE.num('bp-other') * 0.8;
  var exp = HLE.num('bp-exp'), debts = HLE.num('bp-debts'), cards = HLE.num('bp-cards');
  var deps = Math.round(HLE.num('bp-deps')), rate = HLE.num('bp-rate'), term = HLE.num('bp-term') || 30;
  var couple = inc2 > 0;
  // Applicant 1 carries the other income for tax purposes (simplification)
  var netYear = HLE.netIncome(inc1 + other) + (couple ? HLE.netIncome(inc2) : 0);
  var net = netYear / 12;
  // Minimum living expense benchmark (simplified stand-in for HEM, not the real table)
  var gross = inc1 + inc2 + other;
  var floor = (couple ? 2650 : 1750) + deps * 480 + Math.max(0, gross - 120000) * 0.004;
  var expUsed = Math.max(exp, floor);
  var cardCost = cards * 0.038;
  var surplus = net - expUsed - debts - cardCost;
  var arate = rate + 3;
  var top = HLE.presentValue(surplus, arate, term * 12, 12);
  var capped = false;
  var dtiCap = gross * 6;
  if (top > dtiCap) { top = Math.max(0, dtiCap); capped = true; }
  var low = top * 0.85;
  if (surplus <= 0 || top <= 0) {
    HLE.set('bp-range', '$0');
    HLE.set('bp-sub', 'Based on these figures, your expenses and debts use up your income at the assessment rate. Jack can look at options.');
  } else {
    HLE.set('bp-range', HLE.aud(Math.floor(low / 1000) * 1000) + ' to ' + HLE.aud(Math.floor(top / 1000) * 1000));
    HLE.set('bp-sub', 'An estimated range. Different lenders will land at different points, and some may be outside it.');
  }
  HLE.set('bp-arate', HLE.pct(arate, 2));
  HLE.set('bp-net', HLE.aud(net));
  HLE.set('bp-expused', HLE.aud(expUsed) + (expUsed > exp ? ' (minimum)' : ''));
  HLE.set('bp-surplus', HLE.aud(Math.max(0, surplus)));
  HLE.set('bp-pay', top > 0 ? HLE.aud(HLE.payment(top, rate, term * 12, 12)) + '/month' : '–');
  var notes = [];
  if (expUsed > exp) notes.push('Your expenses were lifted to a minimum benchmark for your household size, as lenders do.');
  if (capped) notes.push('Capped at around six times your gross income, a limit many lenders apply.');
  if (cards > 0) notes.push('Your card limits cost ' + HLE.aud(cardCost) + ' a month in the assessment, even if the balance is zero.');
  HLE.set('bp-note', notes.join(' '));
});
