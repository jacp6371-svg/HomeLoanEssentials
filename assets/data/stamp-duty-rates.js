// Stamp duty (transfer duty) rates used by /calculators/stamp-duty.html and /calculators/rent-vs-buy.html.
// Keep every rate in this one file. Update RATES_LAST_CHECKED whenever you re-check them.
//
// Each band: [from, base, ratePerDollar]  → duty = base + (value - from) * rate, for value above `from`.
// `per100: true` means duty is charged per $100 "or part of $100" (rounded up), as the revenue office states.
//
// Source status:
//   "official"  = read directly from the state revenue office website on the date below
//   "secondary" = the revenue office site could not be read by our tools; figures were cross-checked
//                 against at least two recent independent sources and the arithmetic was verified.
//                 TODO (Jack): confirm "secondary" figures against the official calculator before launch.
window.HLE_DUTY = {
  RATES_LAST_CHECKED: '11 November 2026',
  states: {
    QLD: {
      name: 'Queensland', status: 'official',
      source: 'https://qro.qld.gov.au/duties/transfer-duty/calculate/rates/',
      calculator: 'https://qro.qld.gov.au/duties/transfer-duty/calculate/transfer-duty-estimator/',
      per100: true,
      general: [[0, 0, 0], [5000, 0, 0.015], [75000, 1050, 0.035], [540000, 17325, 0.045], [1000000, 38025, 0.0575]],
      // Home concession rate (owner-occupier) - https://qro.qld.gov.au/duties/transfer-duty/calculate/concession-rates/
      home: [[0, 0, 0.01], [350000, 3500, 0.035], [540000, 10150, 0.045], [1000000, 30850, 0.0575]],
      // First home concession (established homes, contracts from 9 June 2024): amount deducted from home concession duty
      fhbDeduction: [[709999.99, 17350], [719999.99, 15615], [729999.99, 13880], [739999.99, 12145], [749999.99, 10410],
                     [759999.99, 8675], [769999.99, 6940], [779999.99, 5205], [789999.99, 3470], [799999.99, 1735]],
      // First home (new home) concession: full concession, no value cap, contracts on or after 1 May 2025
      // https://qro.qld.gov.au/duties/transfer-duty/concessions/homes/first-home-new-home/
      fhbNewHomeExempt: true,
      foreign: 0.08, foreignSource: 'Additional foreign acquirer duty 8% (QRO)',
      foreignNoConcessions: true, // from 1 Aug 2026 concessions are limited to citizens, PRs and specified foreign retirees
      notes: 'From 1 August 2026, home and first home concessions are generally limited to Australian citizens, permanent residents and specified foreign retirees.'
    },
    NSW: {
      name: 'New South Wales', status: 'secondary',
      source: 'https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/transfer-duty',
      calculator: 'https://www.revenue.nsw.gov.au/_resources/duties-links/calculate-your-transfer-duty',
      per100: true,
      // 2026-27 indexed thresholds (1 July 2026 to 30 June 2027). Cross-checked: Hunter Galloway (3 Nov 2026) and Mallesons 2026-27 budget summary.
      general: [[0, 0, 0.0125], [18000, 225, 0.015], [38000, 525, 0.0175], [103000, 1662, 0.035], [387000, 11602, 0.045], [1290000, 52237, 0.055], [3870000, 194137, 0.07]],
      minimum: 20,
      // First Home Buyers Assistance Scheme (official page, nsw.gov.au): homes exempt to $800,000, concession to $1,000,000.
      // Concession amount = (value - 800,000) x 0.195935, derived from the official sample amounts for 2026-27.
      fhb: { exemptTo: 800000, concessionTo: 1000000, concessionRate: 0.195935 },
      foreign: 0.09, foreignSource: 'Surcharge purchaser duty 9% (Mallesons 2026-27 budget summary)',
      notes: 'First home buyer figures are for homes only; vacant land has separate thresholds.'
    },
    VIC: {
      name: 'Victoria', status: 'secondary',
      source: 'https://www.sro.vic.gov.au/',
      calculator: 'https://www.sro.vic.gov.au/',
      per100: false,
      // General rates. Bands above $960,000: 5.5% of the whole value; above $2,000,000: $110,000 + 6.5% over $2m.
      general: [[0, 0, 0.014], [25000, 350, 0.024], [130000, 2870, 0.06]],
      flatFrom: 960000, flatRate: 0.055, topFrom: 2000000, topBase: 110000, topRate: 0.065,
      // Principal place of residence concession, values $130,000 to $550,000 (Aussie, 27 May 2026)
      ppr: { from: 130000, to: 550000, bands: [[130000, 2870, 0.05], [440000, 18370, 0.06]] },
      // First home buyer: exempt to $600,000, sliding concession to $750,000 (SRO page description; Aussie; Integrated Finance)
      fhb: { exemptTo: 600000, concessionTo: 750000 },
      foreign: 0.08, foreignSource: 'Foreign purchaser additional duty 8% (secondary source)',
      notes: 'Victoria also has an off-the-plan concession not included here.'
    },
    WA: {
      name: 'Western Australia', status: 'official',
      source: 'https://www.wa.gov.au/organisation/department-of-finance/transfer-duty-assessment',
      calculator: 'https://www.wa.gov.au/organisation/department-of-finance/transfer-duty-assessment',
      per100: true,
      general: [[0, 0, 0.019], [120000, 2280, 0.0285], [150000, 3135, 0.038], [360000, 11115, 0.0475], [725000, 28453, 0.0515]],
      // First home owner rate for homes, transactions from 7 May 2026: nil to $600,000; $16.15 per $100 above $600,000 up to $800,000
      fhb: { exemptTo: 600000, concessionTo: 800000, concessionRateOver: 0.1615 },
      foreign: 0.07, foreignSource: 'Foreign transfer duty 7% (WA Department of Finance fact sheet)',
      notes: 'First home owner figures are for homes only; vacant land has separate thresholds.'
    },
    SA: {
      name: 'South Australia', status: 'secondary',
      source: 'https://www.revenuesa.sa.gov.au/',
      calculator: 'https://www.revenuesa.sa.gov.au/',
      per100: true,
      general: [[0, 0, 0.01], [12000, 120, 0.02], [30000, 480, 0.03], [50000, 1080, 0.035], [100000, 2830, 0.04], [200000, 6830, 0.0425], [250000, 8955, 0.0475], [300000, 11330, 0.05], [500000, 21330, 0.055]],
      // First home buyers: full relief on new homes, off-the-plan and land to build on, regardless of value,
      // contracts on or after 13 February 2025 (official RevenueSA page). No concession for established homes.
      fhbNewHomeExempt: true,
      foreign: 0.07, foreignSource: 'Foreign ownership surcharge 7% (Aussie, 19 June 2026)',
      notes: 'South Australia has no first home concession for established homes.'
    },
    // TODO (Jack): add ACT, TAS and NT once their current rates are confirmed. ACT changed its rules on 1 July 2026
    // (all first home buyers exempt), and Tasmania's and the NT's official sites could not be read by our tools.
    ACT: { name: 'Australian Capital Territory', unsupported: true, calculator: 'https://www.revenue.act.gov.au/duties/conveyance-duty' },
    TAS: { name: 'Tasmania', unsupported: true, calculator: 'https://www.sro.tas.gov.au/' },
    NT: { name: 'Northern Territory', unsupported: true, calculator: 'https://treasury.nt.gov.au/' }
  }
};

// Returns { duty, base, concession, foreign, total, note, status } for the inputs.
window.HLE_calcDuty = function (stateCode, value, opts) {
  opts = opts || {};
  var st = window.HLE_DUTY.states[stateCode];
  if (!st || st.unsupported) return { unsupported: true, state: st };
  function scale(bands, v, per100) {
    var b = bands[0];
    for (var i = 0; i < bands.length; i++) if (v > bands[i][0]) b = bands[i];
    var over = v - b[0];
    if (per100) over = Math.ceil(over / 100) * 100;
    return Math.max(0, b[1] + over * b[2]);
  }
  function general(v) {
    if (stateCode === 'VIC') {
      if (v > st.topFrom) return st.topBase + (v - st.topFrom) * st.topRate;
      if (v > st.flatFrom) return v * st.flatRate;
    }
    var d = scale(st.general, v, st.per100);
    if (st.minimum && v > 0) d = Math.max(st.minimum, d);
    return d;
  }
  var full = general(value);
  var duty = full, note = '';
  var foreign = !!opts.foreign;
  var allowConcessions = !(foreign && st.foreignNoConcessions);
  var owner = opts.owner !== false;
  var fhb = !!opts.firstHome && owner;

  if (allowConcessions && owner) {
    if (stateCode === 'QLD') {
      if (fhb && opts.newHome) { duty = 0; note = 'First home (new home) concession: no duty, no value cap.'; }
      else {
        duty = scale(st.home, value, true); note = 'Home concession rate applied.';
        if (fhb) {
          var ded = 0;
          for (var i = 0; i < st.fhbDeduction.length; i++) { if (value <= st.fhbDeduction[i][0]) { ded = st.fhbDeduction[i][1]; break; } }
          if (ded) { duty = Math.max(0, duty - ded); note = 'Home concession plus first home concession applied.'; }
          else note = 'Above $800,000 the first home concession no longer applies; home concession rate used.';
        }
      }
    } else if (stateCode === 'VIC') {
      if (value >= st.ppr.from && value <= st.ppr.to) { duty = scale(st.ppr.bands, value, false); note = 'Principal place of residence concession applied.'; }
      if (fhb) {
        if (value <= st.fhb.exemptTo) { duty = 0; note = 'First home buyer exemption applied.'; }
        else if (value <= st.fhb.concessionTo) { duty = duty * (1 - (st.fhb.concessionTo - value) / (st.fhb.concessionTo - st.fhb.exemptTo)); note = 'First home buyer concession applied (sliding scale).'; }
      }
    } else if (stateCode === 'NSW' && fhb) {
      if (value <= st.fhb.exemptTo) { duty = 0; note = 'First Home Buyers Assistance Scheme: exemption.'; }
      else if (value < st.fhb.concessionTo) { duty = (value - st.fhb.exemptTo) * st.fhb.concessionRate; note = 'First Home Buyers Assistance Scheme: concessional duty.'; }
    } else if (stateCode === 'WA' && fhb) {
      if (value <= st.fhb.exemptTo) { duty = 0; note = 'First home owner rate: no duty.'; }
      else if (value <= st.fhb.concessionTo) { duty = Math.ceil((value - st.fhb.exemptTo) / 100) * 100 * st.fhb.concessionRateOver; note = 'First home owner concessional rate applied.'; }
    } else if (stateCode === 'SA' && fhb) {
      if (opts.newHome) { duty = 0; note = 'First home buyer relief on a new home: no duty.'; }
      else note = 'South Australia has no first home concession for established homes.';
    }
  } else if (foreign && st.foreignNoConcessions && (opts.firstHome || owner)) {
    note = 'Foreign buyers are generally not eligible for home concessions in this state.';
  }
  var surcharge = foreign ? value * (st.foreign || 0) : 0;
  return { duty: duty, base: full, concession: Math.max(0, full - duty), foreign: surcharge, total: duty + surcharge, note: note, status: st.status, state: st };
};
