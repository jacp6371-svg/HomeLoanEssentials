// Amortisation schedule with optional extra monthly repayment. Chart.js draws the chart if it loads; the table always works.
(function () {
  var chart = null, lastRows = [];
  function schedule(P, r, n, extra) {
    var i = r / 100 / 12, pay = HLE.payment(P, r, n * 12, 12), bal = P, years = [], m = 0, totI = 0;
    var y = { p: 0, i: 0 };
    while (bal > 0.005 && m < n * 12 + 1) {
      var int = bal * i, prin = Math.min(bal, pay + extra - int);
      if (prin <= 0) break;
      bal -= prin; totI += int; y.p += prin; y.i += int; m++;
      if (m % 12 === 0 || bal <= 0.005) { years.push({ year: Math.ceil(m / 12), p: y.p, i: y.i, bal: Math.max(0, bal) }); y = { p: 0, i: 0 }; }
    }
    return { pay: pay, months: m, interest: totI, years: years };
  }
  function draw(rows) {
    if (!window.Chart) return;
    var ctx = document.getElementById('am-chart');
    var data = {
      labels: rows.map(function (r) { return 'Yr ' + r.year; }),
      datasets: [
        { type: 'bar', label: 'Principal', data: rows.map(function (r) { return Math.round(r.p); }), backgroundColor: '#2a5c45', stack: 's', yAxisID: 'y' },
        { type: 'bar', label: 'Interest', data: rows.map(function (r) { return Math.round(r.i); }), backgroundColor: '#e8b26a', stack: 's', yAxisID: 'y' },
        { type: 'line', label: 'Remaining balance', data: rows.map(function (r) { return Math.round(r.bal); }), borderColor: '#8fc9a8', backgroundColor: '#8fc9a8', pointRadius: 0, borderWidth: 2.5, tension: .25, yAxisID: 'y1' }
      ]
    };
    var money = function (v) { return '$' + (v >= 1e6 ? (v / 1e6).toFixed(1) + 'm' : Math.round(v / 1000) + 'k'); };
    if (chart) { chart.data = data; chart.update('none'); return; }
    chart = new Chart(ctx, {
      data: data,
      options: {
        responsive: true, maintainAspectRatio: false, animation: false,
        interaction: { mode: 'index', intersect: false },
        plugins: { legend: { display: false }, tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + HLE.aud(c.raw); } } } },
        scales: {
          x: { stacked: true, grid: { display: false }, ticks: { maxRotation: 0, autoSkipPadding: 12, font: { family: 'Inter' } } },
          y: { stacked: true, position: 'left', ticks: { callback: money, font: { family: 'Inter' } }, title: { display: true, text: 'Paid each year' } },
          y1: { position: 'right', grid: { display: false }, ticks: { callback: money, font: { family: 'Inter' } }, title: { display: true, text: 'Balance' } }
        }
      }
    });
  }
  HLE.calculator('calcForm', 'amortisation', function () {
    var P = HLE.num('am-amount'), r = HLE.num('am-rate'), n = HLE.num('am-term') || 30, extra = HLE.num('am-extra');
    var base = schedule(P, r, n, 0), withX = schedule(P, r, n, extra);
    HLE.html('am-pay', HLE.aud(base.pay, true) + ' <small>/ month</small>');
    HLE.set('am-sub', extra > 0 ? 'Plus ' + HLE.aud(extra) + ' extra each month, ' + HLE.aud(base.pay + extra, true) + ' in total.' : 'Principal and interest over ' + n + ' years.');
    HLE.set('am-int0', HLE.aud(base.interest));
    HLE.set('am-int1', HLE.aud(withX.interest));
    HLE.set('am-saved', HLE.aud(base.interest - withX.interest));
    HLE.set('am-time', extra > 0 ? HLE.years(base.months - withX.months) : '–');
    HLE.set('am-payoff', HLE.years(withX.months));
    HLE.html('am-table', withX.years.map(function (y) {
      return '<tr><td>' + y.year + '</td><td>' + HLE.aud(y.p) + '</td><td>' + HLE.aud(y.i) + '</td><td>' + HLE.aud(y.bal) + '</td></tr>';
    }).join(''));
    lastRows = withX.years;
    draw(lastRows);
  });
  // Chart.js may finish loading after the first calculation; draw once it is ready (without counting as a use).
  window.addEventListener('load', function () { draw(lastRows); }, { once: true });
})();
