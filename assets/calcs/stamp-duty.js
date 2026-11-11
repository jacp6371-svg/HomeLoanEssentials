// Stamp duty: uses the rates in /assets/data/stamp-duty-rates.js
HLE.calculator('calcForm', 'stamp_duty', function () {
  var state = HLE.val('sd-state') || 'QLD', price = HLE.num('sd-price');
  var owner = ((document.querySelector('input[name="sd-use"]:checked') || {}).value || 'owner') === 'owner';
  var isNew = ((document.querySelector('input[name="sd-type"]:checked') || {}).value || 'established') === 'new';
  var fhb = HLE.checked('sd-fhb'), foreign = HLE.checked('sd-foreign');
  HLE.set('sd-checked', window.HLE_DUTY.RATES_LAST_CHECKED);
  var r = window.HLE_calcDuty(state, price, { owner: owner, firstHome: fhb, newHome: isNew, foreign: foreign });
  if (r.unsupported) {
    HLE.set('sd-total', 'Not yet available');
    HLE.html('sd-sub', 'We have not added ' + r.state.name + ' yet. Use the <a href="' + r.state.calculator + '" target="_blank" rel="noopener" style="color:#8fc9a8">official calculator</a>.');
    ['sd-base', 'sd-conc', 'sd-for'].forEach(function (id) { HLE.set(id, '–'); });
    HLE.set('sd-note', ''); HLE.set('sd-status', '');
    return;
  }
  HLE.set('sd-total', HLE.aud(r.total, true));
  HLE.set('sd-sub', r.state.name + (owner ? ', owner-occupier' : ', investor') + (fhb && owner ? ', first home buyer' : '') + '.');
  HLE.set('sd-base', HLE.aud(r.base, true));
  HLE.set('sd-conc', r.concession > 0 ? '−' + HLE.aud(r.concession, true) : '$0');
  HLE.set('sd-for', r.foreign > 0 ? HLE.aud(r.foreign, true) : '$0');
  var note = r.note || '';
  if (fhb && !owner) note = 'First home concessions apply only when you live in the home. ' + note;
  if (r.state.notes) note += (note ? ' ' : '') + r.state.notes;
  HLE.set('sd-note', note);
  HLE.html('sd-status', r.status === 'official'
    ? 'Source: <a href="' + r.state.source + '" target="_blank" rel="noopener" style="color:#8fc9a8">official revenue office</a>.'
    : 'Cross-checked against independent sources. Confirm with the <a href="' + r.state.calculator + '" target="_blank" rel="noopener" style="color:#8fc9a8">official calculator</a>.');
});
