# Calculator page content. Each entry becomes /calculators/<slug>.html via tools/build_more.py.
# The maths lives in /assets/calcs/<slug>.js, shared helpers in /assets/calc.js.


def money(i, label, value, hint="", full=False):
    h = f'<span class="hint" id="{i}-hint">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{i}-hint"' if hint else ""
    return (f'<div class="field{" field--full" if full else ""}"><label for="{i}">{label}</label>'
            f'<div class="input has-pre"><span class="pre" aria-hidden="true">$</span>'
            f'<input id="{i}" name="{i}" type="text" inputmode="decimal" autocomplete="off" value="{value}"{desc}/></div>{h}</div>')


def pct(i, label, value, hint="", suf="%"):
    h = f'<span class="hint" id="{i}-hint">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{i}-hint"' if hint else ""
    return (f'<div class="field"><label for="{i}">{label}</label>'
            f'<div class="input has-suf"><input id="{i}" name="{i}" type="text" inputmode="decimal" autocomplete="off" value="{value}"{desc}/>'
            f'<span class="suf" aria-hidden="true">{suf}</span></div>{h}</div>')


def count(i, label, value, suf="years", hint=""):
    return pct(i, label, value, hint, suf)


def seg(name, label, options, checked, full=True):
    opts = "".join(
        f'<label><input type="radio" name="{name}" value="{v}"{" checked" if v == checked else ""}/><span>{t}</span></label>'
        for v, t in options)
    return f'<div class="field{" field--full" if full else ""}" role="radiogroup" aria-labelledby="{name}-lbl"><span class="lbl" id="{name}-lbl">{label}</span><div class="seg">{opts}</div></div>'


def check(i, label, checked=False):
    return f'<div class="field field--full"><label class="check" for="{i}"><input type="checkbox" id="{i}" name="{i}"{" checked" if checked else ""}/><span>{label}</span></label></div>'


def select(i, label, options, selected, hint=""):
    o = "".join(f'<option value="{v}"{" selected" if v == selected else ""}>{t}</option>' for v, t in options)
    h = f'<span class="hint" id="{i}-hint">{hint}</span>' if hint else ""
    return f'<div class="field"><label for="{i}">{label}</label><select id="{i}" name="{i}">{o}</select>{h}</div>'


def fs(legend, *fields):
    return f'<fieldset><legend>{legend}</legend><div class="fields">{"".join(fields)}</div></fieldset>'


def out(label, big_id, sub_id="", items=(), extra=""):
    lis = "".join(f'<li><span>{t}</span><strong id="{i}">–</strong></li>' for t, i in items)
    sub = f'<p class="out-sub" id="{sub_id}"></p>' if sub_id else ""
    ul = f'<ul class="out-list">{lis}</ul>' if lis else ""
    return f'<p class="out-label">{label}</p><p class="out-big" id="{big_id}">–</p>{sub}{ul}{extra}'


STATES = [("QLD", "Queensland"), ("NSW", "New South Wales"), ("VIC", "Victoria"), ("WA", "Western Australia"),
          ("SA", "South Australia"), ("ACT", "ACT"), ("TAS", "Tasmania"), ("NT", "Northern Territory")]

CALCS = [
{
 "slug": "borrowing-power",
 "name": "Borrowing Power",
 "title": "Borrowing Power Calculator: How Much Can I Borrow?",
 "h1": "How much can I <em>borrow?</em>",
 "meta": "Estimate how much you could borrow for a home loan in Australia. Includes a 3% serviceability buffer, living expense floor and credit card limits. Indicative only.",
 "intro": "A quick estimate of your borrowing power, worked out roughly the way lenders do it: after-tax income, a minimum living expense figure, your existing debts and a 3% buffer on the interest rate.",
 "blurb": "See roughly what lenders may let you borrow.",
 "form": fs("Income",
            money("bp-inc1", "Applicant 1 income (before tax, per year)", "95,000"),
            money("bp-inc2", "Applicant 2 income (before tax, per year)", "0", "Leave at 0 if buying on your own"),
            money("bp-other", "Other income (per year)", "0", "Rent, bonuses, etc. Lenders usually count 80%", full=True))
       + fs("Spending and debts",
            money("bp-exp", "Living expenses (per month)", "2,800", "Groceries, bills, transport, kids, insurance"),
            money("bp-debts", "Existing loan repayments (per month)", "0", "Car, personal, HECS-HELP etc."),
            money("bp-cards", "Total credit card limits", "5,000", "Limits, not balances"),
            count("bp-deps", "Dependants", "0", "kids"))
       + fs("Loan",
            pct("bp-rate", "Interest rate", "6.0"),
            count("bp-term", "Loan term", "30")),
 "out": out("Estimated borrowing power", "bp-range", "bp-sub",
            [("Assessed at (rate + 3% buffer)", "bp-arate"), ("Monthly net income", "bp-net"), ("Expenses used", "bp-expused"),
             ("Monthly surplus for repayments", "bp-surplus"), ("Repayment on top figure at your rate", "bp-pay")],
            '<p class="out-note" id="bp-note"></p>'),
 "assume": [
  "Income tax is worked out at 2026-27 resident rates plus the 2% Medicare levy. Offsets, HELP repayments and salary packaging are ignored.",
  "Other income is counted at 80%, which is common lender practice for rent and variable income.",
  "Living expenses are the higher of what you enter and a minimum benchmark based on household size. This is a simplified stand-in for the Household Expenditure Measure (HEM) lenders use, not the real HEM table.",
  "Credit cards are counted at 3.8% of the limit each month, whether or not you use them.",
  "Repayments are tested at your rate plus a 3% serviceability buffer, as APRA expects of lenders.",
  "The result is shown as a range because lenders differ. It is capped at six times gross income, a level many lenders treat as a ceiling.",
 ],
 "faqs": [
  ("Why is my borrowing power lower than I expected?", "Lenders test your repayments at a higher rate than you will actually pay (the 3% buffer) and use a minimum living expense figure. Credit card limits and existing debts also reduce it, even if you rarely use them."),
  ("How can I increase my borrowing power?", "Reducing or closing credit cards, paying off small debts, adding a second income, or choosing a lender that treats your income type more generously can all help. Jack can show which makes the biggest difference for you."),
  ("Is this what a bank will lend me?", "No. It is an estimate only. Each lender has its own policy, and the real figure depends on a full assessment of your situation."),
 ],
 "script": "borrowing-power.js",
},
{
 "slug": "loan-repayments",
 "name": "Loan Repayments",
 "title": "Home Loan Repayment Calculator",
 "h1": "Loan <em>repayments</em>",
 "meta": "Work out weekly, fortnightly or monthly home loan repayments, principal and interest or interest only, and the total interest you would pay.",
 "intro": "Work out your repayments weekly, fortnightly or monthly, for principal and interest or an interest-only period, and see the total interest over the life of the loan.",
 "blurb": "Weekly, fortnightly or monthly, P&I or interest only.",
 "form": fs("Loan",
            money("lr-amount", "Loan amount", "600,000"),
            pct("lr-rate", "Interest rate", "6.0"),
            count("lr-term", "Loan term", "30"),
            seg("lr-freq", "Repayment frequency", [("52", "Weekly"), ("26", "Fortnightly"), ("12", "Monthly")], "12"),
            seg("lr-type", "Repayment type", [("pi", "Principal &amp; interest"), ("io", "Interest only")], "pi"),
            count("lr-io", "Interest-only period", "5", "years", "Used when interest only is selected")),
 "out": out("Your repayment", "lr-pay", "lr-sub",
            [("Total interest", "lr-interest"), ("Total repaid", "lr-total"), ("Repayment after interest-only period", "lr-after")]),
 "assume": [
  "The rate stays the same for the whole loan. In practice rates move.",
  "Weekly and fortnightly repayments use the annual rate divided by 52 or 26. Some lenders calculate them differently.",
  "Interest only: you pay interest only for the period chosen, then principal and interest over the remaining term.",
  "Fees, offset accounts and extra repayments are not included.",
 ],
 "faqs": [
  ("Do fortnightly repayments save money?", "Paying half your monthly repayment every fortnight means 26 half-payments a year, which is the same as 13 monthly payments. That extra month each year can take years off the loan. This calculator shows the exact fortnightly equivalent, so use the Amortisation calculator's extra repayment field to see that effect."),
  ("What is the difference between principal and interest and interest only?", "Principal and interest repayments pay off the loan as well as the interest. Interest-only repayments are lower for a while but the loan does not go down, and repayments rise when the interest-only period ends."),
  ("Why do investors use interest only?", "It can improve cash flow and suit some tax strategies. It costs more interest overall, so talk it through with Jack and your accountant."),
 ],
 "script": "loan-repayments.js",
},
{
 "slug": "amortisation",
 "name": "Amortisation Schedule",
 "title": "Home Loan Amortisation Schedule Calculator",
 "h1": "Amortisation <em>schedule</em>",
 "meta": "See how your home loan balance falls year by year, how much goes to principal and interest, and how extra repayments cut time and interest.",
 "intro": "See year by year how your loan balance falls, how much of each year's repayments goes to interest versus principal, and how much time and interest an extra repayment could save.",
 "blurb": "Year-by-year balance, plus the effect of extra repayments.",
 "form": fs("Loan",
            money("am-amount", "Loan amount", "600,000"),
            pct("am-rate", "Interest rate", "6.0"),
            count("am-term", "Loan term", "30"),
            money("am-extra", "Extra repayment (per month)", "200", "Optional. Set to 0 to see the standard schedule")),
 "out": out("Monthly repayment", "am-pay", "am-sub",
            [("Total interest (standard)", "am-int0"), ("Total interest (with extra)", "am-int1"), ("Interest saved", "am-saved"), ("Time saved", "am-time"), ("Paid off in", "am-payoff")]),
 "wide": '<div class="calc-wide"><h2>Principal, interest and balance by year</h2><div class="legend"><span><i style="background:#2a5c45"></i>Principal</span><span><i style="background:#e8b26a"></i>Interest</span><span><i style="background:#8fc9a8"></i>Remaining balance</span></div><div class="chart-box"><canvas id="am-chart" role="img" aria-label="Chart of principal and interest paid each year and the remaining balance"></canvas></div><div class="table-scroll"><table class="data-table"><caption class="sr-only">Yearly amortisation schedule</caption><thead><tr><th scope="col">Year</th><th scope="col">Principal paid</th><th scope="col">Interest paid</th><th scope="col">Balance at year end</th></tr></thead><tbody id="am-table"></tbody></table></div></div>',
 "chart": True,
 "assume": [
  "Monthly repayments at a fixed rate for the whole term.",
  "The extra repayment is added every month from the first month.",
  "Fees and offset accounts are not included.",
 ],
 "faqs": [
  ("What is an amortisation schedule?", "A table that shows each repayment split into interest and principal, and the balance remaining. Early on, most of each repayment is interest; later, most of it reduces the loan."),
  ("Are extra repayments worth it?", "Usually. Every extra dollar reduces the balance that interest is charged on. Check whether your loan allows extra repayments without fees, especially on fixed rates."),
 ],
 "script": "amortisation.js",
},
{
 "slug": "rent-vs-buy",
 "name": "Rent vs Buy",
 "title": "Rent vs Buy Calculator",
 "h1": "Rent or <em>buy?</em>",
 "meta": "Compare the total cost of renting against buying over the years ahead, including rent increases, property growth, stamp duty, ongoing costs and the opportunity cost of your deposit.",
 "intro": "Compare where you could end up after a number of years if you buy versus keep renting and invest your deposit instead. It includes rent increases, property growth, stamp duty, ongoing costs and what your deposit could have earned elsewhere.",
 "blurb": "Compare the long-run cost of renting and buying.",
 "form": fs("Buying",
            money("rb-price", "Property price", "750,000"),
            money("rb-deposit", "Deposit", "75,000"),
            pct("rb-rate", "Interest rate", "6.0"),
            count("rb-term", "Loan term", "30"),
            select("rb-state", "State (for stamp duty)", STATES[:5], "QLD"),
            check("rb-fhb", "I'm a first home buyer", True),
            money("rb-costs", "Other purchase costs", "3,000", "Legal, inspections, loan fees"),
            pct("rb-own", "Ongoing ownership costs", "1.0", "% of value per year: rates, insurance, maintenance"),
            pct("rb-growth", "Property growth", "4.0", "Per year"),
            pct("rb-sell", "Selling costs if sold at the end", "2.5", "Agent and marketing"))
       + fs("Renting",
            money("rb-rent", "Weekly rent", "650"),
            pct("rb-rentup", "Rent increase", "4.0", "Per year"),
            pct("rb-return", "Investment return on your deposit", "6.0", "Per year, if you rent and invest instead"))
       + fs("Timeframe", count("rb-years", "Compare over", "10")),
 "out": out("After <span id=\"rb-yrs\">10</span> years you'd be ahead by", "rb-winner", "rb-sub",
            [("Wealth if you buy", "rb-wbuy"), ("Wealth if you rent and invest", "rb-wrent"), ("Stamp duty (estimate)", "rb-duty"),
             ("Total rent paid", "rb-totrent"), ("Interest + ownership costs", "rb-dead"), ("Opportunity cost of deposit and costs", "rb-opp")],
            '<div class="bars" id="rb-bars"></div>'),
 "assume": [
  "Buying: your wealth is the property's value at the end, less the loan balance and selling costs.",
  "Renting: you invest the deposit and purchase costs at the return you enter. Each year, whichever option costs less to live in invests the difference at the same return.",
  "Stamp duty uses our Stamp Duty calculator's rates for an owner-occupier, with first home concessions if ticked (established home).",
  "Tax, capital gains, Lenders Mortgage Insurance and changes in interest rates are not included.",
 ],
 "faqs": [
  ("Is it always better to buy than rent?", "No. Over short periods, the upfront costs of buying (stamp duty, legal fees and selling costs) often outweigh any growth. Over longer periods buying tends to come out ahead, but it depends on prices, rents and rates."),
  ("What is the opportunity cost of a deposit?", "Money tied up in a deposit cannot be invested elsewhere. If you rented, that money could earn a return, so the calculator counts it."),
 ],
 "script": "rent-vs-buy.js",
 "duty": True,
},
{
 "slug": "dead-money",
 "name": "Dead Money",
 "title": "Dead Money Calculator: Rent vs Interest",
 "h1": "Dead money: <em>rent vs interest</em>",
 "meta": "How much of what you pay over the next few years is money you never see again? Compare rent with mortgage interest and ownership costs.",
 "intro": "People call rent dead money, but interest, rates and insurance are dead money too. This shows how much of your payments over the next few years you would never see again, renting versus owning, and how much an owner keeps as equity.",
 "blurb": "How much of your payments you never see again.",
 "form": fs("Renting",
            money("dm-rent", "Weekly rent", "650"),
            pct("dm-rentup", "Rent increase", "4.0", "Per year"))
       + fs("Owning",
            money("dm-price", "Property price", "750,000"),
            money("dm-loan", "Loan amount", "675,000"),
            pct("dm-rate", "Interest rate", "6.0"),
            count("dm-term", "Loan term", "30"),
            pct("dm-own", "Ownership costs", "1.0", "% of value per year: rates, insurance, maintenance"),
            money("dm-upfront", "Upfront costs", "15,000", "Stamp duty, legal, loan fees"))
       + fs("Timeframe", count("dm-years", "Over the next", "5")),
 "out": out("Dead money if you rent", "dm-rentdead", "dm-sub",
            [("Dead money if you own", "dm-owndead"), ("Of which interest", "dm-int"), ("Of which ownership costs", "dm-ocost"), ("Upfront costs", "dm-up"), ("Principal repaid (equity you keep)", "dm-prin")],
            '<div class="bars" id="dm-bars"></div>'),
 "assume": [
  "Dead money means payments you do not get back: rent for renters; interest, ownership costs and upfront purchase costs for owners.",
  "Principal repayments are not dead money because they build your equity. Property growth is not included here; see the Rent vs Buy calculator for that.",
  "Monthly principal and interest repayments at a fixed rate.",
 ],
 "faqs": [
  ("Is rent really dead money?", "Rent buys you a place to live and flexibility. It does not build equity, but owning has its own non-recoverable costs. This calculator puts the two side by side."),
  ("Why include upfront costs?", "Stamp duty, legal fees and loan costs are paid once and are not recovered, so they count as dead money for an owner, especially over short timeframes."),
 ],
 "script": "dead-money.js",
},
{
 "slug": "stamp-duty",
 "name": "Stamp Duty",
 "title": "Stamp Duty Calculator (QLD and Other States)",
 "h1": "Stamp duty <em>calculator</em>",
 "meta": "Estimate stamp duty (transfer duty) in Queensland and other states, with first home buyer and home concessions, owner-occupier or investor, and foreign buyer surcharges.",
 "intro": "Estimate transfer duty (stamp duty) on a property purchase, with home and first home buyer concessions, owner-occupier or investor rates and foreign buyer surcharges. Queensland is the default.",
 "blurb": "QLD by default, with first home concessions.",
 "form": fs("Property",
            select("sd-state", "State or territory", STATES, "QLD"),
            money("sd-price", "Purchase price or value", "750,000"),
            seg("sd-use", "How will you use it?", [("owner", "Live in it"), ("investor", "Investment")], "owner"),
            seg("sd-type", "Property type", [("established", "Established home"), ("new", "New home or off the plan")], "established"),
            check("sd-fhb", "I'm a first home buyer", False),
            check("sd-foreign", "I'm a foreign buyer (surcharge applies)", False)),
 "out": out("Estimated stamp duty", "sd-total", "sd-sub",
            [("Duty before concessions", "sd-base"), ("Concessions", "sd-conc"), ("Foreign buyer surcharge", "sd-for")],
            '<p class="out-note" id="sd-note"></p><p class="out-note">Rates last checked: <span id="sd-checked"></span>. <span id="sd-status"></span></p>'),
 "assume": [
  "Rates are kept in one data file and were last checked on the date shown. Queensland and Western Australia figures come straight from the official revenue office websites; New South Wales, Victoria and South Australia were cross-checked against independent sources because their official pages could not be read automatically.",
  "Queensland: the home concession rate applies when you live in the home. First home buyers pay no duty on new homes (contracts from 1 May 2025, no value cap) and get a concession on established homes up to $800,000.",
  "Concessions have conditions, such as moving in within a set time and citizenship or residency rules. Vacant land concessions and off-the-plan schemes are not included.",
  "ACT, Tasmania and the Northern Territory are not yet included; use their official calculators.",
 ],
 "faqs": [
  ("Do first home buyers pay stamp duty in Queensland?", "Eligible first home buyers pay no transfer duty on a new home or off-the-plan purchase (contracts from 1 May 2025, no value cap), and no duty on an established home valued at $700,000 or less, with a partial concession up to $800,000. Conditions apply."),
  ("What is the Queensland home concession?", "A lower rate of transfer duty for people buying a home they will live in. It is applied automatically in this calculator when you choose Live in it."),
  ("When is stamp duty paid?", "Usually at or before settlement. Your conveyancer or solicitor will arrange it. Check the exact due date with your state's revenue office."),
 ],
 "script": "stamp-duty.js",
 "duty": True,
},
{
 "slug": "lmi",
 "name": "Lenders Mortgage Insurance",
 "title": "LMI Calculator: Estimate Lenders Mortgage Insurance",
 "h1": "Lenders Mortgage <em>Insurance</em>",
 "meta": "Get an indicative estimate of Lenders Mortgage Insurance (LMI) based on your loan amount and LVR. LMI varies by lender and insurer.",
 "intro": "Lenders Mortgage Insurance (LMI) is usually charged when you borrow more than 80% of a property's value. It protects the lender, not you. This gives an indicative estimate only; the real premium depends on the lender and insurer.",
 "blurb": "An indicative estimate when you borrow over 80%.",
 "form": fs("Loan",
            money("lmi-value", "Property value", "750,000"),
            money("lmi-loan", "Loan amount", "675,000", "Before any LMI is added"),
            check("lmi-fhb", "I'm a first home buyer", False),
            check("lmi-qld", "Buying in Queensland", True)),
 "out": out("Indicative LMI premium", "lmi-est", "lmi-sub",
            [("Loan to value ratio (LVR)", "lmi-lvr"), ("Likely range", "lmi-range"), ("Deposit needed to avoid LMI", "lmi-avoid")],
            '<p class="out-note" id="lmi-note"></p>'),
 "assume": [
  "Indicative estimate only. Premiums here come from a simplified table based on LVR and loan size bands, not from any lender or insurer. LMI varies by lender, insurer, loan type and your circumstances.",
  "Premiums may also attract stamp duty and are often added to the loan, which can push the LVR higher.",
  "Eligible first home buyers may avoid LMI with a 5% deposit under the Australian Government 5% Deposit Scheme, if the property is under the price cap.",
  "Some lenders waive or reduce LMI for eligible professionals such as doctors, lawyers and accountants.",
 ],
 "faqs": [
  ("When do I pay LMI?", "Usually when your loan is more than 80% of the property's value. The premium is a one-off cost, typically added to the loan or paid at settlement."),
  ("How can I avoid LMI?", "Save a 20% deposit, use the 5% Deposit Scheme if you are an eligible first home buyer, have a family member provide a guarantee, or check whether your profession qualifies for a waiver."),
  ("Is LMI refundable if I refinance?", "Generally no, or only a small portion within a short time. If you refinance above 80% later, you may pay it again."),
 ],
 "script": "lmi.js",
},
]
