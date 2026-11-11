# Starter articles. DRAFTS: Jack to review every article before it goes live.
# Each becomes /articles/<slug>.html via tools/build_more.py and appears on /resources.html.

ARTICLES = [
{
 "slug": "how-much-can-i-borrow",
 "title": "How much can I borrow?",
 "category": "Buying",
 "date": "2026-11-11",
 "read": 6,
 "meta": "How Australian lenders work out your borrowing power, the 3% buffer, living expenses and credit cards, and five practical ways to borrow more.",
 "summary": "How lenders actually work out your borrowing power, and the handful of things that move the number the most.",
 "calc": ("borrowing-power", "Borrowing Power calculator"),
 "body": """
<p>It is the first question almost everyone asks, and the honest answer is: it depends on the lender. Two banks can look at the same payslips and land tens of thousands of dollars apart. Here is how they get to their number, and what you can do about it.</p>

<h2>The short version</h2>
<p>Lenders work out how much income you have left each month after tax, living costs and existing debts, then test whether that surplus could cover repayments at a rate about 3% higher than the one you will actually pay. The loan size that fits inside that surplus is your borrowing power.</p>

<h2>What lenders look at</h2>
<ul>
  <li><strong>Income after tax.</strong> Base salary counts in full. Overtime, bonuses, commission and rental income are often counted at a discount, commonly around 80%, because they can change.</li>
  <li><strong>Living expenses.</strong> Lenders compare what you tell them with a benchmark called the Household Expenditure Measure (HEM) and use whichever is higher. You cannot borrow more by under-reporting your spending.</li>
  <li><strong>Existing debts.</strong> Car loans, personal loans, buy now pay later and HECS-HELP all reduce what is left over.</li>
  <li><strong>Credit card limits.</strong> This one surprises people. Lenders count a monthly cost based on the limit, not the balance. A $20,000 limit you never touch still reduces your borrowing power.</li>
  <li><strong>Dependants.</strong> Each child adds to the living expense benchmark.</li>
  <li><strong>The assessment rate.</strong> APRA expects lenders to test your repayments at a buffer of about 3% above the loan's rate, so you can cope if rates rise.</li>
</ul>

<h2>Why two lenders give different answers</h2>
<p>Every lender has its own policy on things like how much overtime it counts, how it treats self-employed income, which benchmark it uses for expenses and how it handles rental income. That is a big part of why using a broker helps: we know which lenders are more generous with your type of income.</p>

<h2>Five ways to borrow more</h2>
<ol>
  <li><strong>Cut or close credit cards</strong> you do not need, or reduce the limits.</li>
  <li><strong>Pay off small debts</strong> like a car loan or personal loan before applying, if your savings allow.</li>
  <li><strong>Choose the right lender</strong> for your income type, especially if you are self-employed or rely on overtime.</li>
  <li><strong>Consider a longer loan term</strong>, which lowers the assessed repayment. You can still pay it off faster.</li>
  <li><strong>Apply with a second income</strong> if you are buying with a partner.</li>
</ol>

<h2>Borrowing power is not the same as a comfortable budget</h2>
<p>Being approved for a figure does not mean you should borrow all of it. We always talk about what repayment feels comfortable alongside the rest of your life, not just what the bank will allow.</p>

<h2>Try the numbers</h2>
<p>Our <a href="/calculators/borrowing-power.html">Borrowing Power calculator</a> gives you an estimated range using the same building blocks: after-tax income, a minimum expense figure, your debts and card limits, and the 3% buffer. It is a starting point, not a pre-approval.</p>
""",
},
{
 "slug": "fixed-vs-variable-2026",
 "title": "Fixed vs variable in 2026",
 "category": "Rates",
 "date": "2026-11-11",
 "read": 6,
 "meta": "Fixed or variable home loan rate? The real trade-offs between certainty and flexibility, when a split loan makes sense, and the questions to ask before you lock in.",
 "summary": "Certainty or flexibility? The real trade-offs, and why a split loan often makes sense.",
 "calc": ("loan-repayments", "Loan Repayments calculator"),
 "body": """
<!-- DRAFT NOTE (Jack): this article deliberately avoids quoting current rates or rate forecasts, which date quickly. Add a line on current market conditions when you publish if you want to, and keep it general. -->
<p>Fixed or variable is one of the most common questions we get, and there is no answer that is right for everyone. Nobody knows exactly where rates will go, including the banks. What you can control is choosing a structure that suits how you live and how much certainty you need.</p>

<h2>Variable rates: flexibility</h2>
<p>A variable rate moves up and down with the lender's pricing, which usually follows the Reserve Bank's cash rate.</p>
<ul>
  <li><strong>You can usually make unlimited extra repayments</strong> and redraw them.</li>
  <li><strong>Offset accounts are common</strong>, so savings sitting in your account reduce the interest you pay.</li>
  <li><strong>You can refinance or sell</strong> without break costs.</li>
  <li><strong>The catch:</strong> if rates rise, so do your repayments.</li>
</ul>

<h2>Fixed rates: certainty</h2>
<p>A fixed rate locks your rate for a set period, commonly one to five years.</p>
<ul>
  <li><strong>Your repayments stay the same</strong> for the fixed period, which makes budgeting easier.</li>
  <li><strong>Extra repayments are often capped</strong>, and offset accounts are less common.</li>
  <li><strong>Breaking a fixed loan early can cost you.</strong> If you sell, refinance or pay it off during the fixed period, the lender may charge break costs, which can be significant.</li>
  <li><strong>The catch:</strong> if rates fall, you stay on the higher rate until the fixed term ends.</li>
</ul>

<h2>The middle ground: split loans</h2>
<p>Many people split their loan, fixing part of it for certainty and leaving part variable for flexibility, extra repayments and an offset. It is not about guessing rates correctly. It is about not being caught out either way.</p>

<h2>Questions to ask yourself</h2>
<ol>
  <li>Could my budget handle a rise in repayments right now?</li>
  <li>Am I likely to sell, refinance or make large extra repayments in the next few years?</li>
  <li>Do I have savings that would work harder in an offset account?</li>
  <li>How would I feel if I fixed and rates then fell, or stayed variable and rates rose?</li>
</ol>

<h2>What happens when a fixed rate ends</h2>
<p>When the fixed period finishes, most loans roll onto the lender's standard variable rate, which is often higher than what new customers are offered. Put the date in your calendar and get your loan reviewed a couple of months before it expires.</p>

<h2>Run your own numbers</h2>
<p>Use our <a href="/calculators/loan-repayments.html">Loan Repayments calculator</a> to see how your repayments change at different rates. Then talk to Jack about how a fixed, variable or split structure would work for you.</p>
""",
},
{
 "slug": "should-i-refinance",
 "title": "Should I refinance?",
 "category": "Refinancing",
 "date": "2026-11-11",
 "read": 5,
 "meta": "When refinancing your home loan makes sense, what it costs, and a simple checklist to work out whether switching lenders will actually save you money.",
 "summary": "When switching lenders pays off, what it costs, and a quick checklist before you move.",
 "calc": ("loan-repayments", "Loan Repayments calculator"),
 "body": """
<p>Lenders tend to save their sharpest rates for new customers. If you have had the same loan for a few years, there is a fair chance you are paying more than you need to. Refinancing is not always the answer, though. Here is how to tell.</p>

<h2>Signs it is worth a look</h2>
<ul>
  <li>You have not reviewed your rate in the last year or two.</li>
  <li>Your fixed rate is ending soon.</li>
  <li>Your property has gone up in value, so your loan is now a smaller share of it.</li>
  <li>You want to release equity for renovations or an investment.</li>
  <li>You are juggling credit cards or personal loans at much higher rates.</li>
  <li>Your loan is missing features you want, such as an offset account.</li>
</ul>

<h2>What it costs to switch</h2>
<p>Refinancing is rarely free, so we always add up the costs before recommending it:</p>
<ul>
  <li><strong>Discharge fee</strong> from your current lender.</li>
  <li><strong>Government fees</strong> to discharge and register the mortgage.</li>
  <li><strong>Application or valuation fees</strong> with some new lenders.</li>
  <li><strong>Break costs</strong> if you are leaving a fixed rate early.</li>
  <li><strong>Lenders Mortgage Insurance</strong> again if your new loan is above 80% of the property's value.</li>
</ul>
<p>Some lenders offer cashback to cover these costs. A cashback is only good value if the rate and fees are competitive for the years ahead, not just on day one.</p>

<h2>Try asking your current lender first</h2>
<p>Sometimes a single phone call gets a lower rate without moving at all. If they will not budge, at least you know you have tested it. We are happy to tell you if staying put is the better option.</p>

<h2>A quick checklist</h2>
<ol>
  <li>What is my current rate, and what are new customers being offered?</li>
  <li>How much will switching cost, all up?</li>
  <li>How long until the saving covers those costs?</li>
  <li>Am I planning to sell or make other changes soon?</li>
  <li>Does the new loan have the features I actually use?</li>
</ol>

<h2>Be careful with debt consolidation</h2>
<p>Rolling a car loan or credit card into your home loan usually lowers your monthly repayment, but stretching a short-term debt over 30 years can mean paying more interest overall. If you consolidate, plan to pay that part off faster.</p>

<h2>See the difference</h2>
<p>Put your current loan into our <a href="/calculators/loan-repayments.html">Loan Repayments calculator</a>, then try a lower rate to see what it could save. Or ask Jack for a free loan health check and he will compare it across our panel for you.</p>
""",
},
]
