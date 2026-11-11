// Home Loan Essentials: shared navigation, reveal and small interaction helpers.
(function () {
  var nav = document.querySelector('nav.site-nav');
  var toggle = document.getElementById('navToggle');
  var links = document.getElementById('navLinks');

  function setMenu(open) {
    if (!toggle || !links) return;
    links.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.classList.toggle('menu-open', open);
  }
  if (toggle && links) {
    toggle.addEventListener('click', function () { setMenu(!links.classList.contains('open')); });
    links.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && links.classList.contains('open')) { setMenu(false); toggle.focus(); } });
    window.addEventListener('resize', function () { if (window.innerWidth > 860) setMenu(false); });
  }

  // Header gains a soft shadow once the page scrolls
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mark the current page in the menu
  var page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === page || href === page.replace(/\.html$/, '')) { a.classList.add('active'); a.setAttribute('aria-current', 'page'); }
  });

  // Gentle reveal on scroll; everything shows at once without IntersectionObserver
  var reveals = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    reveals.forEach(function (r) { r.classList.add('visible'); });
  } else {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (r) { obs.observe(r); });
  }
})();
