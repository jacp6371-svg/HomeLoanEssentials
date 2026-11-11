// Analytics events, ready for GA4. Nothing is sent until GA4 (gtag) or Google Tag Manager is added
// to the site; until then events queue in window.dataLayer and do nothing else.
// Event names: phone_click, enquiry_submitted, calculator_used, booking_click.
(function () {
  window.dataLayer = window.dataLayer || [];
  window.hleTrack = function (name, params) {
    params = params || {};
    try {
      if (typeof window.gtag === 'function') window.gtag('event', name, params);
      else window.dataLayer.push(Object.assign({ event: name }, params));
    } catch (e) { /* never break the page for analytics */ }
  };
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    var where = a.closest('header') ? 'header' : a.closest('footer') ? 'footer' : (a.closest('section') || {}).id || 'page';
    if (href.indexOf('tel:') === 0) window.hleTrack('phone_click', { link_location: where, page_path: location.pathname });
    else if (a.hasAttribute('data-booking')) window.hleTrack('booking_click', { link_location: where, page_path: location.pathname });
  });
})();
