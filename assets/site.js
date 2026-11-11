// Home Loan Essentials: shared header (dropdowns, mobile menu), current-page marking and reveal.
(function () {
  var header = document.getElementById('siteHeader');
  var nav = document.getElementById('hdNav');
  var toggle = document.getElementById('hdToggle');
  var mq = window.matchMedia('(max-width: 1080px)');
  var items = Array.prototype.slice.call(document.querySelectorAll('.hd-item.has-drop'));
  var closeTimer = null;

  function setItem(item, open) {
    item.classList.toggle('open', open);
    var btn = item.querySelector('.hd-top');
    if (btn) btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  function closeAll(except) { items.forEach(function (i) { if (i !== except) setItem(i, false); }); }

  items.forEach(function (item) {
    var btn = item.querySelector('.hd-top');
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var open = !item.classList.contains('open');
      if (!mq.matches) closeAll(item);
      setItem(item, open);
    });
    // Hover opens on desktop pointers only
    item.addEventListener('mouseenter', function () {
      if (mq.matches || !window.matchMedia('(hover: hover)').matches) return;
      clearTimeout(closeTimer); closeAll(item); setItem(item, true);
    });
    item.addEventListener('mouseleave', function () {
      if (mq.matches || !window.matchMedia('(hover: hover)').matches) return;
      closeTimer = setTimeout(function () { setItem(item, false); }, 160);
    });
    // Leaving the dropdown with the keyboard closes it
    item.addEventListener('focusout', function (e) {
      if (mq.matches) return;
      if (!item.contains(e.relatedTarget)) setItem(item, false);
    });
  });

  document.addEventListener('click', function (e) {
    if (!mq.matches && !e.target.closest('.hd-item.has-drop')) closeAll();
  });

  function setMenu(open) {
    if (!nav || !toggle) return;
    nav.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    document.body.classList.toggle('menu-open', open);
    if (!open) closeAll();
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    mq.addEventListener ? mq.addEventListener('change', function () { setMenu(false); }) : mq.addListener(function () { setMenu(false); });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var open = items.filter(function (i) { return i.classList.contains('open'); })[0];
    if (open && !mq.matches) { setItem(open, false); open.querySelector('.hd-top').focus(); return; }
    if (nav && nav.classList.contains('open')) { setMenu(false); toggle.focus(); }
  });

  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mark the current page in the menu
  var path = window.location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('.site-header a[href]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href.indexOf('#') > -1 || href.indexOf('tel:') === 0) return;
    if (href === path || href === path.replace(/\.html$/, '')) {
      a.setAttribute('aria-current', 'page');
      var top = a.closest('.hd-item.has-drop');
      if (top) top.querySelector('.hd-top').classList.add('is-current');
    }
  });

  // Gentle reveal on scroll (older pages); shows at once without IntersectionObserver
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
