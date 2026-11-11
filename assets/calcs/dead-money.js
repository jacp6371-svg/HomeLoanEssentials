// Dead money: payments you never get back, renting vs owning, over X years.
HLE.calculator('calcForm', 'dead_money', function () {
  var years = Math.max(1, Math.min(40, Math.round(HLE.num('dm-years') || 5)));
  var rent = HLE.num('dm-rent') * 52, up = HLE.num('dm-rentup') / 100;
  var price = HLE.num('dm-price'), loan = HLE.num('dm-loan'), r = HLE.num('dm-rate'), term = HLE.num('dm-term') || 30;
  var own = HLE.num('dm-own') / 100, upfront = HLE.num('dm-upfront');
  var totalRent = 0;
  for (var y = 0; y < years; y++) totalRent += rent * Math.pow(1 + up, y);
  var months = Math.min(years, term) * 12;
  var pay = HLE.payment(loan, r, term * 12, 12), bal = loan, interest = 0, principal = 0;
  for (var m = 0; m < months && bal > 0; m++) { var i = bal * r / 100 / 12, p = Math.min(bal, pay - i); interest += i; principal += p; bal -= p; }
  var ocost = price * own * years;
  var ownDead = interest + ocost + upfront;
  HLE.html('dm-rentdead', HLE.aud(totalRent));
  HLE.set('dm-sub', 'Over ' + years + (years === 1 ? ' year' : ' years') + ', compared with ' + HLE.aud(ownDead) + ' if you own.');
  HLE.set('dm-owndead', HLE.aud(ownDead));
  HLE.set('dm-int', HLE.aud(interest));
  HLE.set('dm-ocost', HLE.aud(ocost));
  HLE.set('dm-up', HLE.aud(upfront));
  HLE.set('dm-prin', HLE.aud(principal));
  HLE.bars('dm-bars', [
    { label: 'Renting: rent paid', value: totalRent, cls: 'alt' },
    { label: 'Owning: interest, costs and upfront', value: ownDead },
    { label: 'Owning: equity built from repayments', value: principal, cls: 'muted' }
  ]);
});
