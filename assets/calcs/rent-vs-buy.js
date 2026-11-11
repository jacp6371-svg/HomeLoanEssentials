// Rent vs buy: compares wealth after X years. See the assumptions on the page.
HLE.calculator('calcForm', 'rent_vs_buy', function () {
  var price = HLE.num('rb-price'), dep = Math.min(HLE.num('rb-deposit'), price), r = HLE.num('rb-rate'), term = HLE.num('rb-term') || 30;
  var state = HLE.val('rb-state') || 'QLD', fhb = HLE.checked('rb-fhb');
  var costs = HLE.num('rb-costs'), own = HLE.num('rb-own') / 100, g = HLE.num('rb-growth') / 100, sell = HLE.num('rb-sell') / 100;
  var rent0 = HLE.num('rb-rent') * 52, rentUp = HLE.num('rb-rentup') / 100, ret = HLE.num('rb-return') / 100;
  var years = Math.max(1, Math.min(40, Math.round(HLE.num('rb-years') || 10)));
  var d = window.HLE_calcDuty(state, price, { owner: true, firstHome: fhb, newHome: false });
  var duty = d.unsupported ? 0 : d.total;
  var loan = Math.max(0, price - dep);
  var payYear = HLE.payment(loan, r, term * 12, 12) * 12;
  var upfront = dep + duty + costs;
  // Renter invests the upfront cash; each year the cheaper option invests the difference
  var renterPot = upfront, buyerPot = 0, totalRent = 0, totalOwn = 0, rent = rent0, value = price, interestPaid = 0, bal = loan;
  for (var y = 1; y <= years; y++) {
    var ownCost = value * own;
    var buyOut = (y <= term ? payYear : 0) + ownCost;
    // interest this year
    for (var m = 0; m < 12 && bal > 0; m++) { var int = bal * r / 100 / 12; interestPaid += int; bal = Math.max(0, bal - (payYear / 12 - int)); }
    totalRent += rent; totalOwn += ownCost;
    renterPot *= (1 + ret); buyerPot *= (1 + ret);
    if (buyOut > rent) renterPot += buyOut - rent; else buyerPot += rent - buyOut;
    rent *= (1 + rentUp); value *= (1 + g);
  }
  var equity = value * (1 - sell) - bal + buyerPot;
  var opp = upfront * (Math.pow(1 + ret, years) - 1);
  var diff = equity - renterPot;
  HLE.set('rb-yrs', years);
  HLE.html('rb-winner', HLE.aud(Math.abs(diff)) + ' <small>' + (diff >= 0 ? 'by buying' : 'by renting') + '</small>');
  HLE.set('rb-sub', diff >= 0 ? 'On these assumptions, buying leaves you better off after ' + years + ' years.' : 'On these assumptions, renting and investing leaves you better off after ' + years + ' years.');
  HLE.set('rb-wbuy', HLE.aud(equity));
  HLE.set('rb-wrent', HLE.aud(renterPot));
  HLE.set('rb-duty', d.unsupported ? 'Not available' : HLE.aud(duty));
  HLE.set('rb-totrent', HLE.aud(totalRent));
  HLE.set('rb-dead', HLE.aud(interestPaid + totalOwn));
  HLE.set('rb-opp', HLE.aud(opp));
  HLE.bars('rb-bars', [{ label: 'Wealth if you buy', value: Math.max(0, equity) }, { label: 'Wealth if you rent and invest', value: Math.max(0, renterPot), cls: 'alt' }]);
});
