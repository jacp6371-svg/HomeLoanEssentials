# Content for the service pages. Each entry becomes /services/<slug>.html via tools/build.py.
# Written for Home Loan Essentials in Jack's voice: plain, direct, no hard sell.
# Figures for government schemes were checked on 11 November 2026; sources are noted beside each one
# and repeated as HTML comments on the built page. Re-check them before relying on them.

SERVICES = [
# ---------------------------------------------------------------- HOME LOANS
{
 "slug": "buying-a-home",
 "group": "Home Loans",
 "nav": "Buying a Home",
 "title": "Home Loans for Buying Your Next Home",
 "h1": "Buying a <em>Home</em>",
 "meta": "Buying your next home on the Gold Coast or anywhere in Australia? Jack Perkins compares 30+ lenders, sorts pre-approval and stays with you to settlement.",
 "intro": "Whether it is your second home, an upsize or a move interstate, the loan you pick shapes the next 30 years. We compare 30+ lenders, line up pre-approval before you start bidding, and stay with you from application to settlement.",
 "suits": [
  "Owner-occupiers buying their next home, upgrading or downsizing",
  "People selling and buying at the same time who need bridging or a clear plan for the gap",
  "Buyers moving to Queensland from interstate, or anywhere in Australia",
  "Anyone who wants a loan that fits how they actually live, with an offset, redraw or split",
 ],
 "steps": [
  ("A straight conversation", "We talk through your income, savings, the home you are after and how you like to manage money. No obligation and no cost to you."),
  ("Borrowing power and budget", "Jack works out what lenders are likely to approve and, just as important, what repayment feels comfortable for you."),
  ("Compare and choose", "We shortlist loans across our panel on rate, fees and features, and explain the trade-offs in plain language."),
  ("Pre-approval", "We lodge with the lender you choose so you can make offers with confidence and know your ceiling."),
  ("Offer to settlement", "Once you find the place, we handle the formal approval, valuation and paperwork, and keep you, your solicitor and agent in the loop until you get the keys."),
 ],
 "needs": "Jack will ask about your income, your savings and deposit, any debts and credit cards, and your regular living costs. We will send you a short list of what the lender wants to see once we know which loan suits, so you are not chasing paperwork you will never use.",
 "faqs": [
  ("How much deposit do I need to buy a home?", "Most lenders want 20% of the purchase price to avoid Lenders Mortgage Insurance (LMI). Many will lend with 5% to 10% if you pay LMI, and some professionals can have it reduced or waived. Jack can show you what each option costs."),
  ("Should I sell first or buy first?", "It depends on your equity, the market and your nerves. Selling first gives certainty on price; buying first secures the home you want but may need bridging finance. We map out both so you can see the numbers side by side."),
  ("Does using a broker cost me anything?", "No. Lenders pay brokers a commission when a loan settles, so our service costs you nothing. We will always tell you how we are paid."),
  ("How long does pre-approval last?", "Usually three to six months depending on the lender. If it is close to expiring, we can refresh it."),
 ],
 "calc": ("borrowing-power", "Borrowing Power calculator", "Get a rough idea of your price range before you start inspecting."),
 "related": ["first-home-buyers", "refinancing", "building-a-new-home"],
},
{
 "slug": "first-home-buyers",
 "group": "Home Loans",
 "nav": "Becoming a First Home Buyer",
 "title": "First Home Buyer Loans, Grants and Schemes",
 "h1": "Becoming a <em>First Home Buyer</em>",
 "meta": "First home buyer in Queensland or anywhere in Australia? Jack explains the 5% Deposit Scheme, the QLD First Home Owner Grant and stamp duty concessions, and finds the right loan.",
 "intro": "Buying your first home comes with a lot of moving parts: deposits, grants, government schemes and stamp duty. We cut through the noise, check which help you qualify for, and make the process straightforward from your first question to settlement.",
 "suits": [
  "First home buyers saving a deposit and wondering when they can buy",
  "Buyers who want to use the 5% Deposit Scheme to avoid Lenders Mortgage Insurance",
  "Couples and singles buying or building a new home in Queensland",
  "People who have never bought before and want someone to explain every step",
 ],
 "steps": [
  ("Where you stand today", "We look at your income, savings and spending, and talk about the kind of home and area you have in mind."),
  ("Check the help available", "Jack checks whether you are likely to qualify for the 5% Deposit Scheme, the First Home Owner Grant and stamp duty concessions in your state."),
  ("Pre-approval", "We compare lenders, including those taking part in the government scheme, and get you pre-approved so you know your budget."),
  ("Find your home", "You go shopping. We are on the phone when you need a quick answer about a property or a contract."),
  ("Approval to keys", "We manage the formal approval, grant application and paperwork, and keep your conveyancer and agent updated until settlement."),
 ],
 "needs": "Expect questions about your income, savings history, any debts and your regular spending. Government schemes have their own eligibility rules, so we will also confirm things like citizenship or residency and whether you have owned property before.",
 "extra_title": "Government help for first home buyers",
 "extra_html": """
<!-- Sources checked 11 November 2026:
     5% Deposit Scheme price caps: https://www.firsthomebuyers.gov.au/australian-government-5-percent-deposit-scheme/property-price-caps
     5% Deposit Scheme changes from 1 October 2025 (no income caps, no limit on places): firsthomebuyers.gov.au fact sheet, 1 October 2025
     QLD First Home Owner Grant: https://www.qld.gov.au/housing/buying-owning-home/financial-help-concessions/first-home-owner-grant
     QLD first home concession: https://qro.qld.gov.au/duties/transfer-duty/first-home/
     QLD first home (new home) concession: https://qro.qld.gov.au/duties/transfer-duty/concessions/homes/first-home-new-home/ -->
<div class="info-grid">
  <article class="info-card">
    <p class="info-tag">Australia-wide</p>
    <h3>Australian Government 5% Deposit Scheme</h3>
    <p>Lets eligible first home buyers buy with as little as a 5% deposit without paying Lenders Mortgage Insurance, because the government guarantees part of the loan. Since 1 October 2025 there are no income caps and no limit on the number of places.</p>
    <p>Property price caps apply. In Queensland they are <strong>$1,000,000</strong> in the capital city and regional centres (including the Gold Coast and Sunshine Coast) and <strong>$700,000</strong> in other areas.</p>
  </article>
  <article class="info-card">
    <p class="info-tag">Queensland</p>
    <h3>First Home Owner Grant</h3>
    <p>A <strong>$30,000</strong> grant for eligible first home buyers who buy or build a <strong>new</strong> home in Queensland valued under <strong>$750,000</strong> (including land). Established homes do not qualify.</p>
  </article>
  <article class="info-card">
    <p class="info-tag">Queensland</p>
    <h3>Stamp duty (transfer duty) concessions</h3>
    <p><strong>New homes:</strong> eligible first home buyers pay no transfer duty on a new home or off-the-plan purchase, with no value cap, for contracts signed on or after 1 May 2025.</p>
    <p><strong>Established homes:</strong> no transfer duty on a first home valued at $700,000 or less, with a partial concession up to $800,000.</p>
    <p>From 1 August 2026 these concessions are generally limited to Australian citizens, permanent residents and specified foreign retirees.</p>
  </article>
</div>
<p class="fine">Scheme rules, caps and grant amounts change, and eligibility depends on your circumstances. Always confirm current eligibility with <a href="https://www.firsthomebuyers.gov.au/" target="_blank" rel="noopener">Housing Australia</a> and the <a href="https://qro.qld.gov.au/property-concessions-grants/" target="_blank" rel="noopener">Queensland Revenue Office</a> (or your state's revenue office) before you sign a contract. Jack will check this with you as part of your application.</p>
""",
 "faqs": [
  ("How much deposit do I need for my first home?", "With the 5% Deposit Scheme, as little as 5% of the purchase price if you are eligible and the home is under the price cap. Without it, 20% avoids LMI, and many lenders accept 5% to 10% with LMI added. You will also need money for stamp duty (if it applies), legal fees and moving costs."),
  ("Can I get the First Home Owner Grant on an established home in Queensland?", "No. The Queensland grant is for new homes only, valued under $750,000 including land. Buyers of established homes may still benefit from the first home stamp duty concession."),
  ("Can I use the grant and the 5% Deposit Scheme together?", "In many cases, yes. They are separate programs with separate rules, so Jack will check you against each one."),
  ("Do I need pre-approval before I make an offer?", "It is strongly recommended. It tells you your budget and shows agents you are serious. It is not a final approval, so we still need the lender to sign off on the property itself."),
  ("Does a broker cost first home buyers anything?", "No. Our service is free to you because lenders pay us when your loan settles."),
 ],
 "calc": ("stamp-duty", "Stamp Duty calculator", "See what you might pay in transfer duty, with first home concessions included."),
 "related": ["buying-a-home", "building-a-new-home", "professional-packages"],
},
{
 "slug": "building-a-new-home",
 "group": "Home Loans",
 "nav": "Building a New Home",
 "title": "Construction Home Loans for Building a New Home",
 "h1": "Building a <em>New Home</em>",
 "meta": "Building a new home or a house and land package? Jack Perkins arranges construction loans with progress payments and keeps your builder, lender and solicitor on the same page.",
 "intro": "Building works differently from buying. The loan is paid out in stages as your builder finishes each part of the job, and you usually only pay interest on what has been drawn. We set it up properly from the start so the money flows when your builder needs it.",
 "suits": [
  "House and land packages",
  "Knockdown rebuilds on land you already own",
  "First home buyers building to use the Queensland First Home Owner Grant",
  "Anyone signing a fixed-price building contract with a registered builder",
 ],
 "steps": [
  ("Plans, contract and budget", "We look at your land, building contract and any extras or variations so the loan covers the full cost."),
  ("Pre-approval", "We compare lenders that are comfortable with construction lending and get you pre-approved."),
  ("Land settlement", "If you are buying land, the land portion settles first."),
  ("Progress payments", "As the builder hits each stage (slab, frame, lock-up, fixing, completion), they invoice and we help get each payment released."),
  ("Completion", "A final inspection, the last payment, and your loan moves to normal repayments."),
 ],
 "needs": "Along with your income and savings, building loans need the fixed-price building contract, plans and specifications, and the builder's details. Jack will tell you exactly what your chosen lender wants before you sign anything with the builder.",
 "faqs": [
  ("How do construction loan repayments work?", "During the build you normally pay interest only on the amount drawn so far. Once the home is complete, the loan switches to principal and interest repayments."),
  ("What if my build goes over budget?", "Variations need to be covered by your own funds or an increase to the loan, which needs the lender's approval. That is why we check your contract for allowances before you sign."),
  ("Can I get the First Home Owner Grant if I build?", "If you are an eligible first home buyer building a new home in Queensland valued under $750,000 including land, you may be eligible for the grant. Confirm current rules with the Queensland Revenue Office."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Check repayments once your build is finished and the loan is fully drawn."),
 "related": ["construction-land-loans", "first-home-buyers", "buying-a-home"],
},
{
 "slug": "refinancing",
 "group": "Home Loans",
 "nav": "Refinancing",
 "title": "Refinance Your Home Loan",
 "h1": "<em>Refinancing</em> Your Home Loan",
 "meta": "Paying too much on your home loan? Jack Perkins checks the market across 30+ lenders and tells you plainly whether refinancing will save you money.",
 "intro": "Your current lender is counting on you not to shop around. We check the market, compare your loan against 30+ lenders and tell you plainly whether moving, or simply asking your lender for a better deal, will save you money.",
 "suits": [
  "Homeowners who have not reviewed their rate in a year or more",
  "Anyone coming off a fixed rate",
  "People wanting to release equity for renovations or investing",
  "Households looking to combine debts into one lower repayment",
 ],
 "steps": [
  ("Loan health check", "We look at your current rate, fees, features and how long is left on any fixed term."),
  ("Compare the market", "Jack compares your loan with options across our panel, including any cashback offers, and works out the real saving after switching costs."),
  ("Your call", "If staying put is the better move, we will tell you. Sometimes a phone call to your current lender is all it takes."),
  ("Switch", "If you go ahead, we handle the application, valuation and discharge with your old lender."),
 ],
 "needs": "Recent statements for your home loan and any other debts, details of your income, and an idea of your goals. We will look at break costs or discharge fees up front so there are no surprises.",
 "faqs": [
  ("How often should I review my home loan?", "Once a year is a good habit, and any time your fixed rate is about to end or your circumstances change."),
  ("What does it cost to refinance?", "Typical costs include a discharge fee from your current lender, government registration fees and sometimes an application or valuation fee. Breaking a fixed rate early can attract break costs. We add it all up before you decide."),
  ("Can I refinance if my property has gone down in value?", "Possibly, but if your loan is above 80% of the property's value you may need to pay Lenders Mortgage Insurance again. We will check this first."),
  ("Are cashback offers worth it?", "Sometimes. A cashback is only worth it if the rate and fees are also competitive over the life of the loan. We compare both."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "See what a lower rate would do to your repayments."),
 "related": ["debt-consolidation", "investing-in-property", "buying-a-home"],
},
{
 "slug": "investing-in-property",
 "group": "Home Loans",
 "nav": "Investing in Property",
 "title": "Investment Property Loans",
 "h1": "Investing in <em>Property</em>",
 "meta": "Buying an investment property? Jack Perkins helps you structure the loan properly from day one, using equity, interest-only and split loans where they make sense.",
 "intro": "The right loan structure matters as much as the rate. We help investors borrow smart from day one, so your debt is set up in a way that suits your tax position, your cash flow and your next purchase.",
 "suits": [
  "First-time investors using equity in their home",
  "Investors building a portfolio who need each loan structured cleanly",
  "People weighing up interest-only against principal and interest",
  "Anyone who wants their broker to talk to their accountant",
 ],
 "steps": [
  ("Goals and numbers", "We look at your income, existing loans, equity and what you want the property to do for you."),
  ("Structure", "Jack sets out a loan structure (splits, offset accounts, interest-only periods) and, with your permission, runs it past your accountant."),
  ("Pre-approval", "We compare lenders on rate and on how they treat rental income and existing debts."),
  ("Purchase and settlement", "We handle approval, valuation and settlement, and keep your records tidy for tax time."),
 ],
 "needs": "Income details, statements for your current loans, information on any rental income, and your plans for the property. Tax questions belong with your accountant; Jack works alongside your accountant and his father Duncan's practice where that helps.",
 "faqs": [
  ("Can I use the equity in my home to buy an investment property?", "Often, yes. Lenders will usually lend up to 80% of your home's value without LMI, less what you already owe. That usable equity can cover the deposit and costs on an investment."),
  ("Should I choose interest-only for an investment loan?", "Interest-only can help cash flow, but you pay more interest overall and lenders assess it strictly. It suits some investors and not others; talk it through with Jack and your accountant."),
  ("Do investor loans have higher rates?", "Usually, yes. Investment loans and interest-only loans generally carry higher rates than owner-occupied principal and interest loans."),
 ],
 "calc": ("borrowing-power", "Borrowing Power calculator", "Get a rough idea of how much more you could borrow."),
 "related": ["refinancing", "smsf-loans", "construction-land-loans"],
},
# ---------------------------------------------------------------- BUSINESS LOANS
{
 "slug": "asset-equipment-finance",
 "group": "Business Loans",
 "nav": "Asset & Equipment Finance",
 "title": "Asset and Equipment Finance",
 "h1": "Asset &amp; <em>Equipment Finance</em>",
 "meta": "Finance for vehicles, machinery and equipment for your business. Jack Perkins can help directly or refer you to a trusted asset finance specialist.",
 "intro": "Vehicles, machinery, tools and technology keep a business moving. Asset finance spreads the cost over the useful life of the equipment, so you keep cash in the business for everything else.",
 "suits": [
  "Tradies and small businesses buying utes, vans or trucks",
  "Businesses upgrading machinery, equipment or IT",
  "Sole traders and companies who want predictable repayments",
 ],
 "steps": [
  ("What you need and why", "We talk about the asset, its cost, how long you will use it and your business's cash flow."),
  ("Options", "We explain the common structures, such as a chattel mortgage, finance lease or rental, in plain terms. Your accountant can confirm the tax side."),
  ("Application", "We prepare the application, or refer you to a specialist where that gets you a better result."),
  ("Settlement", "Funds are paid to the supplier and you take delivery."),
 ],
 "needs": "Your ABN and business details, a quote or invoice for the asset, and recent financials or tax returns depending on the lender and loan size.",
 "referral": True,
 "faqs": [
  ("What is a chattel mortgage?", "A loan where the business owns the asset from day one and the lender holds it as security. It is one of the most common ways to finance vehicles and equipment."),
  ("Can new businesses get equipment finance?", "Some lenders will lend to businesses that have only recently registered an ABN, often with a deposit or extra conditions. We can tell you who is likely to say yes."),
  ("Do you only do home loans?", "Home lending is Jack's focus. For business and asset finance he will either look after it directly or refer you to a trusted asset finance specialist, and he will tell you which."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Rough out repayments on the amount you need."),
 "related": ["business-finance", "commercial-property-finance", "self-employed-low-doc-loans"],
},
{
 "slug": "business-finance",
 "group": "Business Loans",
 "nav": "Business Finance",
 "title": "Business Loans and Finance",
 "h1": "Business <em>Finance</em>",
 "meta": "Business loans, overdrafts and working capital for small businesses. Jack Perkins helps directly or refers you to a trusted business finance specialist.",
 "intro": "Growing a business usually means funding something before it pays for itself. Whether it is working capital, an overdraft or a loan to buy into a business, we help you find finance that matches how your business earns.",
 "suits": [
  "Small business owners who need working capital or an overdraft",
  "People buying into or buying out a business",
  "Businesses wanting to use property equity to fund growth",
 ],
 "steps": [
  ("Understand the business", "We look at what the money is for, how the business earns and what security is available."),
  ("Match the lender", "Banks and specialist lenders see business risk very differently, so we match you to the right one."),
  ("Prepare and apply", "We help package the application, or refer you to a specialist where needed."),
  ("Approval", "We track the application through to funding."),
 ],
 "needs": "Business financials and tax returns, bank statements, details of what the funds are for and any security on offer. Requirements vary a lot by lender and loan size.",
 "referral": True,
 "faqs": [
  ("Do I need property as security for a business loan?", "Not always. Unsecured and asset-backed options exist, but rates are usually lower when property is offered as security."),
  ("How long do business loans take?", "Simple loans can be quick; larger or more complex deals can take several weeks. We will give you a realistic timeline up front."),
  ("Will you refer me to someone else?", "Where a business finance specialist will get you a better outcome, Jack will refer you and stay in touch about any home loan side of things."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Estimate repayments on a business loan amount."),
 "related": ["asset-equipment-finance", "commercial-property-finance", "self-employed-low-doc-loans"],
},
{
 "slug": "commercial-property-finance",
 "group": "Business Loans",
 "nav": "Commercial Property Finance",
 "title": "Commercial Property Loans",
 "h1": "Commercial <em>Property Finance</em>",
 "meta": "Finance for offices, shops, warehouses and other commercial property. Jack Perkins helps directly or refers you to a trusted commercial finance specialist.",
 "intro": "Buying the premises your business operates from, or a commercial investment, comes with different rules from residential lending: lower loan-to-value ratios, shorter terms and a close look at the lease. We help you understand them before you commit.",
 "suits": [
  "Business owners buying their own premises",
  "Investors buying shops, offices, warehouses or mixed-use property",
  "Owners refinancing an existing commercial loan",
 ],
 "steps": [
  ("The property and the plan", "We look at the property, the lease or your own use of it, and your finances."),
  ("Lender fit", "Commercial lenders assess leases, tenants and industries differently, so we match you carefully."),
  ("Application", "We prepare the application or bring in a commercial specialist where it helps."),
  ("Valuation to settlement", "We manage the process through to settlement."),
 ],
 "needs": "Details of the property and any leases, your business or personal financials, and information on the purpose of the purchase.",
 "referral": True,
 "faqs": [
  ("How much deposit do I need for commercial property?", "Commonly 20% to 40% of the price, depending on the property type, lease and lender."),
  ("Is commercial lending the same as a home loan?", "No. Terms are often shorter, rates and fees differ, and lenders look closely at rental income and lease quality."),
  ("Can I buy commercial property in my SMSF?", "In some cases, yes, using a limited recourse borrowing arrangement. See our SMSF Loans page and get advice from a licensed adviser first."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Estimate repayments on a commercial loan amount."),
 "related": ["business-finance", "smsf-loans", "asset-equipment-finance"],
},
# ---------------------------------------------------------------- SPECIALIST LENDING
{
 "slug": "self-employed-low-doc-loans",
 "group": "Specialist Lending",
 "nav": "Self-Employed & Low Doc Loans",
 "title": "Home Loans for Self-Employed Borrowers",
 "h1": "Self-Employed &amp; <em>Low Doc Loans</em>",
 "meta": "Self-employed and finding it hard to get a home loan? Jack Perkins knows which lenders understand business income, including low doc options.",
 "intro": "Being your own boss should not make buying a home harder, but it often does. Some lenders understand business income far better than others. We know who they are and how to present your situation so it gets a fair look.",
 "suits": [
  "Sole traders, contractors and company directors",
  "Business owners whose tax returns do not show the full picture",
  "People who have recently started a business or changed industry",
  "Borrowers who need a low doc option using BAS or accountant's declarations",
 ],
 "steps": [
  ("How your business earns", "We look at your returns, BAS and how your income has moved over time."),
  ("Find the right lender", "Some lenders accept one year of financials, others add back certain expenses. We match you to the best fit."),
  ("Work with your accountant", "With your permission, we talk to your accountant so the numbers are presented clearly."),
  ("Apply and settle", "We handle the application through to settlement."),
 ],
 "needs": "Usually recent tax returns and financials for you and your business, or for low doc loans, BAS statements, business bank statements or an accountant's letter. Jack will tell you which route fits before you gather anything.",
 "faqs": [
  ("What is a low doc loan?", "A loan for self-employed borrowers that uses alternative evidence of income, such as BAS statements or business bank statements, instead of full tax returns. Rates are usually a bit higher and deposits larger."),
  ("How long do I need to have been self-employed?", "Many lenders like two years of trading, but some will consider one year, and a few will look at less where you have worked in the same industry before."),
  ("Will my tax minimisation hurt my borrowing power?", "It can. Some lenders add back items like depreciation or one-off expenses. Choosing the right lender makes a real difference here."),
 ],
 "calc": ("borrowing-power", "Borrowing Power calculator", "A starting point; self-employed income is assessed case by case."),
 "related": ["business-finance", "buying-a-home", "refinancing"],
},
{
 "slug": "foreign-investment-finance",
 "group": "Specialist Lending",
 "nav": "Foreign Investment Finance",
 "title": "Home Loans for Foreign Buyers and Non-Residents",
 "h1": "Foreign Investment <em>Finance</em>",
 "meta": "Home loans for foreign buyers, non-residents and temporary visa holders buying in Australia. General information on FIRB, surcharges and lender requirements.",
 "intro": "Buying in Australia as a foreign person, a temporary visa holder or an Australian living overseas comes with extra rules and costs. Fewer lenders will help, and those that do look for larger deposits. We explain how it works and who may be able to lend.",
 "suits": [
  "Temporary visa holders living and working in Australia",
  "Australian citizens and permanent residents living overseas",
  "Foreign buyers purchasing new property with FIRB approval",
 ],
 "steps": [
  ("Your residency position", "We confirm your visa or residency status and where your income is earned."),
  ("Rules and costs", "We outline Foreign Investment Review Board (FIRB) requirements, state surcharges and what lenders typically require."),
  ("Lender options", "Jack checks which lenders on our panel will consider your situation."),
  ("Approval and settlement", "We manage the application through to settlement."),
 ],
 "needs": "Proof of identity and residency or visa status, evidence of income (sometimes in a foreign currency), and FIRB approval where required. Lenders may ask for more than usual, so we will set expectations early.",
 "extra_title": "Things to know before you start",
 "extra_html": """
<!-- Sources checked 11 November 2026:
     Two-year ban on foreign persons buying established dwellings (1 April 2025 to 31 March 2027): Treasurer's media release, 16 February 2025, https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/media-releases/albanese-government-clamping-down-foreign-purchase
     QLD additional foreign acquirer duty 8%: https://qro.qld.gov.au/duties/transfer-duty/calculate/rates/ -->
<ul class="ticks">
  <li><strong>FIRB approval:</strong> foreign persons generally need approval from the Foreign Investment Review Board before buying residential property in Australia.</li>
  <li><strong>Established homes:</strong> the federal government has banned most foreign persons from buying established dwellings from 1 April 2025 to 31 March 2027, with limited exceptions.</li>
  <li><strong>State surcharges:</strong> in Queensland, foreign buyers pay an additional 8% transfer duty on residential land, on top of normal duty. Other states have their own surcharges.</li>
  <li><strong>Bigger deposits:</strong> lenders that accept foreign or non-resident borrowers usually lend at lower loan-to-value ratios.</li>
</ul>
<!-- TODO (Jack): confirm which lenders on your panel currently accept foreign buyers, temporary visa holders and Australians living overseas, and on what terms, before this page goes live. -->
<p class="fine">This is general information only and is not legal or tax advice. Rules for foreign buyers change; confirm current requirements with FIRB, the ATO and your state revenue office, and get legal advice before signing a contract.</p>
""",
 "faqs": [
  ("Can a temporary visa holder get a home loan in Australia?", "Some lenders will lend to temporary residents, usually with a larger deposit and depending on the visa type and time remaining on it."),
  ("Do Australians living overseas count as foreign buyers?", "Australian citizens are generally not foreign persons for FIRB purposes, but lenders still treat overseas income and residency carefully."),
  ("Do foreign buyers pay extra stamp duty in Queensland?", "Yes. Queensland charges an additional 8% foreign acquirer duty on residential land, on top of normal transfer duty."),
 ],
 "calc": ("stamp-duty", "Stamp Duty calculator", "Includes the foreign buyer surcharge option."),
 "related": ["buying-a-home", "investing-in-property", "self-employed-low-doc-loans"],
},
{
 "slug": "professional-packages",
 "group": "Specialist Lending",
 "nav": "Professional Packages",
 "title": "Home Loans for Medical, Legal and Accounting Professionals",
 "h1": "Professional <em>Packages</em>",
 "meta": "Doctors, lawyers, accountants and other eligible professionals may be able to buy with a smaller deposit and reduced or waived LMI. Jack checks which lenders offer it.",
 "intro": "Some lenders offer special terms to eligible professionals, such as reduced or waived Lenders Mortgage Insurance (LMI) with a smaller deposit. That can save thousands and get you into a home sooner. We check whether you qualify and which lenders offer the best version.",
 "suits": [
  "Doctors, specialists, dentists and other medical professionals",
  "Lawyers and barristers",
  "Accountants",
  "Professionals early in their career with strong future income",
 ],
 "steps": [
  ("Check your eligibility", "Each lender has its own list of eligible professions, memberships and income levels."),
  ("Compare the offers", "We compare which lenders waive or reduce LMI and up to what loan size and deposit."),
  ("Pre-approval", "We lodge with the lender that gives you the best overall deal."),
  ("Settlement", "We manage the process through to settlement."),
 ],
 "needs": "Details of your profession and registration or membership, your income and employment, and your savings. Lenders confirm eligibility case by case.",
 "extra_title": "Who may qualify",
 "extra_html": """
<!-- TODO (Jack): confirm which lenders on your panel currently offer reduced or waived LMI for medical, legal and accounting professionals, the eligible professions, maximum loan-to-value ratios and loan size limits. Update this section before it goes live so the page never promises a product you cannot deliver. -->
<p>Eligibility, the maximum loan size and the smallest deposit allowed all vary by lender and change over time. Common examples include medical practitioners, dentists, lawyers and accountants who hold the right registration or professional membership. Jack will check the current options for your profession before you apply.</p>
""",
 "faqs": [
  ("What is an LMI waiver?", "Lenders Mortgage Insurance protects the lender, not you, and is normally charged when you borrow more than 80% of the property's value. An LMI waiver means the lender does not charge it, even with a smaller deposit."),
  ("Which professions are eligible?", "It depends on the lender. Medical, legal and accounting professions are the most common. Jack will check your profession against current lender policies."),
  ("Can I use a professional package for an investment property?", "Some lenders allow it, others only for owner-occupied homes. We will confirm before you apply."),
 ],
 "calc": ("lmi", "LMI calculator", "See roughly what Lenders Mortgage Insurance could cost without a waiver."),
 "related": ["first-home-buyers", "buying-a-home", "investing-in-property"],
},
{
 "slug": "debt-consolidation",
 "group": "Specialist Lending",
 "nav": "Debt Consolidation",
 "title": "Debt Consolidation Home Loans",
 "h1": "Debt <em>Consolidation</em>",
 "meta": "Rolling credit cards, car loans and personal loans into your home loan can lower repayments. Jack Perkins explains the trade-offs so you can decide.",
 "intro": "Juggling credit cards, a car loan and a personal loan gets expensive. Rolling them into your home loan can cut your total repayment and make life simpler, but it needs a plan so short-term debts are not stretched over 30 years.",
 "suits": [
  "Homeowners with high-interest credit cards or personal loans",
  "People wanting one repayment instead of several",
  "Borrowers with enough equity to refinance",
 ],
 "steps": [
  ("List every debt", "We put all your debts, rates and repayments on one page."),
  ("Run the numbers", "Jack shows you the repayment saving and, importantly, the total interest over time."),
  ("Plan the payoff", "We suggest ways to clear the consolidated amount faster, such as a separate split or higher repayments."),
  ("Refinance", "If it makes sense, we handle the application and pay out your other debts at settlement."),
 ],
 "needs": "Statements for your home loan and every debt you want to consolidate, income details and your regular living costs.",
 "faqs": [
  ("Does debt consolidation save money?", "It usually lowers your monthly repayment because home loan rates are lower than credit card or personal loan rates. But if you take 30 years to repay what was a 3-year car loan, you can pay more interest overall. That is why we plan the payoff."),
  ("Will consolidating hurt my credit score?", "A refinance involves a credit enquiry, but closing several debts and making one reliable repayment often helps over time."),
  ("Should I close my credit cards after consolidating?", "Usually, yes. Lenders count your card limits when assessing borrowing power, and keeping them open can lead straight back into debt."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Compare your current repayments with a single loan."),
 "related": ["refinancing", "buying-a-home", "self-employed-low-doc-loans"],
},
{
 "slug": "construction-land-loans",
 "group": "Specialist Lending",
 "nav": "Construction & Land Loans",
 "title": "Land Loans and Construction Finance",
 "h1": "Construction &amp; <em>Land Loans</em>",
 "meta": "Loans to buy vacant land now and build later, owner-builder and investment construction. Jack Perkins explains lender requirements and finds the right fit.",
 "intro": "Buying a block now and building later, building an investment, or taking on more of the build yourself all need lenders who are comfortable with the extra risk. We know which lenders will consider your project and what they will ask for.",
 "suits": [
  "Buyers purchasing vacant land to build on later",
  "Investors building a dwelling, duplex or dual occupancy",
  "Owner-builders (lender options are limited)",
  "Anyone whose build does not fit a standard house and land package",
 ],
 "steps": [
  ("The land and the plan", "We look at the block, zoning, your building timeline and budget."),
  ("Lender requirements", "Land loans often need bigger deposits, and owner-builder loans have strict rules. We set clear expectations."),
  ("Approval", "We secure approval for the land, the construction, or both."),
  ("Progress payments", "During the build we help release each progress payment as stages are completed."),
 ],
 "needs": "Contract for the land, plans and building contract or quotes, council approvals where relevant, plus your income and savings details.",
 "faqs": [
  ("Can I buy land now and build later?", "Yes. Many lenders offer land loans, though some have time limits on when building must start and may need a larger deposit."),
  ("Can owner-builders get finance?", "A small number of lenders will consider owner-builder loans, usually with a bigger deposit and detailed costings. It is harder, but not impossible."),
  ("Are there stamp duty concessions for vacant land in Queensland?", "Queensland has a first home vacant land concession for eligible buyers building their first home. Check current rules with the Queensland Revenue Office."),
 ],
 "calc": ("stamp-duty", "Stamp Duty calculator", "Estimate transfer duty on the land purchase."),
 "related": ["building-a-new-home", "investing-in-property", "first-home-buyers"],
},
{
 "slug": "smsf-loans",
 "group": "Specialist Lending",
 "nav": "SMSF Loans",
 "title": "SMSF Property Loans",
 "h1": "<em>SMSF</em> Loans",
 "meta": "Borrowing to buy property in a self-managed super fund. General information on limited recourse borrowing arrangements and what lenders require.",
 "intro": "A self-managed super fund can borrow to buy residential or commercial property using a limited recourse borrowing arrangement (LRBA). The rules are strict and only a handful of lenders offer these loans. We arrange the lending once you have advice that it is right for your fund.",
 "suits": [
  "SMSF trustees who have received advice to buy property in their fund",
  "Business owners looking at buying their premises through super",
  "Funds with enough balance to cover the deposit, costs and a buffer",
 ],
 "steps": [
  ("Get advice first", "Whether to borrow in your SMSF is a financial advice decision. Speak with a licensed financial adviser and your accountant before you start."),
  ("Structure", "An LRBA needs a separate holding (bare) trust and correct legal documents."),
  ("Lender options", "Jack compares the few lenders that offer SMSF loans on rate, deposit and fund balance requirements."),
  ("Approval and settlement", "We coordinate with your accountant, adviser and solicitor through to settlement."),
 ],
 "needs": "The SMSF trust deed and recent financial statements, member details and balances, the holding trust documents and evidence of advice. Requirements are strict and vary by lender.",
 "faqs": [
  ("Can I live in a property my SMSF owns?", "No. A residential property owned by your SMSF cannot be lived in or rented by you or your relatives."),
  ("How much deposit does an SMSF loan need?", "Lenders typically require a larger deposit than a standard home loan, along with a minimum fund balance after purchase."),
  ("Do you give SMSF advice?", "No. Jack arranges the lending. Advice on whether to borrow in your fund must come from a licensed financial adviser; Jack can work alongside yours."),
 ],
 "calc": ("loan-repayments", "Loan Repayments calculator", "Check how repayments fit your fund's cash flow."),
 "related": ["investing-in-property", "commercial-property-finance", "business-finance"],
},
]
