"""Generates the calculator pages, about page, articles index and articles, credit guide placeholder,
sitemap.xml and llms.txt. Called from tools/build.py."""
import os
from datetime import date

from build import (ARROW, CALC_ICON, ROOT, SITE, TODAY, breadcrumbs_ld, crumbs_html, cta_band, esc, faq_html,
                   faq_ld, foot, head, strip_tags, write)
from content_articles import ARTICLES
from content_calcs import CALCS
from content_services import SERVICES

CHART_JS = "https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"

DISCLAIMER = ("This calculator gives an estimate only. It is general information, not credit or financial advice, and it does not "
              "take your objectives, financial situation or needs into account. Results depend on the figures you enter and the "
              "assumptions listed above, and they are not a quote, an offer or a loan approval. Lender policies, rates and fees "
              "change. Speak with Jack before making any decision.")


def nice_date(iso):
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def calc_card(c):
    return (f'<a class="card" href="/calculators/{c["slug"]}.html"><span class="card-tag">Calculator</span>'
            f'<h3>{esc(c["name"])}</h3><p>{esc(c["blurb"])}</p><span class="more">Open calculator {ARROW}</span></a>')


# ---------------------------------------------------------------- calculators
def build_calculators():
    hub_trail = [("Home", "/"), ("Calculators", "/calculators/")]
    for c in CALCS:
        path = f"/calculators/{c['slug']}.html"
        trail = hub_trail + [(c["name"], path)]
        app_ld = {
            "@context": "https://schema.org",
            "@type": "WebApplication",
            "name": f"{c['name']} calculator",
            "applicationCategory": "FinanceApplication",
            "operatingSystem": "Any",
            "description": c["meta"],
            "url": SITE + path,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "AUD"},
            "provider": {"@type": "FinancialService", "name": "Home Loan Essentials", "url": SITE + "/"},
        }
        page = head(f"{c['title']} | Home Loan Essentials", c["meta"], path, extra_css=("calc.css",),
                    ld=[app_ld, breadcrumbs_ld(trail), faq_ld(c["faqs"])])
        assume = "".join(f"<li>{esc(a)}</li>" for a in c["assume"])
        others = "".join(calc_card(o) for o in CALCS if o["slug"] != c["slug"])
        page += f"""
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">Calculator</p>
    <h1>{c['h1']}</h1>
    <p class="lead">{esc(c['intro'])}</p>
  </div>
</section>

<section class="calc-sec" aria-label="{esc(c['name'])} calculator">
  <div class="wrap">
    <div class="calc">
      <form class="calc-form" id="calcForm" novalidate>
        {c['form']}
        <p class="fine" style="margin-top:1.5rem">Results update as you type.</p>
      </form>
      <aside class="calc-out" aria-live="polite" aria-label="Your results">
        {c['out']}
        <div class="out-cta">
          <p>Want Jack to run the real numbers? Get in touch.</p>
          <a href="/#contact" class="btn-green" data-cta="calculator">Get in touch</a>
        </div>
      </aside>
    </div>
    {c.get('wide', '')}
    <p class="disclaimer">{esc(DISCLAIMER)}</p>
  </div>
</section>

<section class="sec sec--tight sec--white" aria-labelledby="assume-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">How it works</p>
      <h2 class="h2" id="assume-title">The <em>assumptions</em></h2>
      <p class="lead">Every calculator simplifies. Here is exactly what this one assumes, so you know how far to trust the number.</p>
    </div>
    <ul class="assume">{assume}</ul>
  </div>
</section>

<section class="sec sec--tight sec--paper" aria-labelledby="faq-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Common questions</p>
      <h2 class="h2" id="faq-title">Questions people <em>ask</em></h2>
    </div>
    {faq_html(c['faqs'])}
  </div>
</section>

<section class="sec sec--tight sec--cream" aria-labelledby="more-title">
  <div class="wrap">
    <p class="eyebrow">More tools</p>
    <h2 class="h2" id="more-title">Other <em>calculators</em></h2>
    <div class="cards">{others}</div>
  </div>
</section>
{cta_band()}
"""
        scripts = ["calc.js"]
        if c.get("duty"):
            scripts.append("data/stamp-duty-rates.js")
        if c.get("chart"):
            scripts.append(CHART_JS)
        scripts.append("calcs/" + c["script"])
        page += foot(scripts)
        write(path.lstrip("/"), page)

    # hub
    desc = "Free home loan calculators: borrowing power, repayments, amortisation, rent vs buy, dead money, stamp duty and LMI. Estimates only."
    page = head("Home Loan Calculators | Home Loan Essentials", desc, "/calculators/", ld=[breadcrumbs_ld(hub_trail)])
    page += f"""
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(hub_trail)}
    <p class="eyebrow">Resources &amp; tools</p>
    <h1>Home loan <em>calculators</em></h1>
    <p class="lead">Quick, honest estimates to help you get your bearings. Each one lists its assumptions, and none of them ask for your details.</p>
  </div>
</section>
<section class="sec sec--tight sec--paper" aria-label="All calculators">
  <div class="wrap">
    <div class="cards" style="margin-top:0">{''.join(calc_card(c) for c in CALCS)}</div>
    <p class="disclaimer">These calculators give estimates only and are general information, not advice. Speak with Jack for numbers based on your actual situation.</p>
  </div>
</section>
{cta_band("Want the <em>real numbers?</em>", "Calculators are a starting point. Jack can run your situation across 30+ lenders and tell you what is actually possible.")}
"""
    page += foot()
    write("calculators/index.html", page)
    print("calculators:", len(CALCS) + 1)


# ---------------------------------------------------------------- about
def build_about():
    path = "/about.html"
    trail = [("Home", "/"), ("About", path)]
    desc = ("Jack Perkins is a Gold Coast mortgage broker from a four-generation banking family. How he works, "
            "and how he works alongside his dad Duncan, a broker, financial planner and tax agent.")
    person_ld = {
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "url": SITE + path,
        "mainEntity": {
            "@type": "Person",
            "name": "Jack Perkins",
            "jobTitle": "Finance Broker",
            "worksFor": {"@type": "FinancialService", "name": "Home Loan Essentials", "url": SITE + "/"},
            "image": SITE + "/images/jack-perkins.jpg",
            "sameAs": ["https://www.linkedin.com/in/jack-perkins-homeloanessentials/", "https://www.instagram.com/homeloanessentials/"],
        },
    }
    page = head("About Jack Perkins | Home Loan Essentials", desc, path, extra_css=("home.css",),
                ld=[person_ld, breadcrumbs_ld(trail)], og_type="profile")
    page += f"""
<section class="page-hero page-hero--photo" style="--hero-img:url('/images/aerial-22.webp')">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">About Jack</p>
    <h1>Banking is in Jack's <em>blood</em></h1>
    <p class="lead">From the Bank of NSW in the 1930s to Home Loan Essentials today. A family story built on trust and service spanning nearly a century.</p>
  </div>
</section>

<section class="sec about" aria-labelledby="story-title">
  <div class="wrap">
    <div class="about-grid">
      <div class="about-photo">
        <picture><source srcset="/images/jack-perkins.webp" type="image/webp"/><img src="/images/jack-perkins.jpg" alt="Jack Perkins, finance broker at Home Loan Essentials" width="900" height="1200" loading="lazy"/></picture>
        <div class="about-name"><strong>Jack Perkins</strong><span>Finance Broker &middot; Home Loan Essentials</span></div>
      </div>
      <div class="about-copy">
        <p class="eyebrow">The story</p>
        <h2 class="h2" id="story-title">Four generations of <em>banking</em></h2>
        <p class="bio">Jack grew up in a banking family. His great-grandfather started at the Bank of NSW in the 1930s, his grandfather spent over 30 years at Westpac, and both his parents worked in financial services.</p>
        <p class="bio">He started Home Loan Essentials to offer something that is harder to find than it should be: straight answers, no hard sell, and a broker who stays with you through the entire process.</p>
        <p class="bio">Jack is based in Helensvale on the Gold Coast and works with clients right across Australia, in person or entirely online.</p>
        <a href="/#contact" class="btn-green">Get in Touch</a>
      </div>
    </div>
    <ol class="timeline">
      <li class="tl">
        <div class="tl-era">1930s</div>
        <h3>Great-Grandfather</h3>
        <div class="tl-bank">Bank of NSW</div>
        <p>The foundation was laid. A career built on community banking at a time when a handshake meant everything.</p>
      </li>
      <li class="tl">
        <div class="tl-era">1960s to 1990s</div>
        <h3>Grandfather Peter</h3>
        <div class="tl-bank">Westpac</div>
        <p>Over 30 dedicated years at Westpac, Peter built a reputation for integrity, sound advice, and genuine care for every client.</p>
      </li>
      <li class="tl">
        <div class="tl-era">2000s to Present</div>
        <h3>Mum &amp; Dad</h3>
        <div class="tl-bank">Westpac &amp; Finance</div>
        <p>Both parents continued the legacy in Westpac's banking sector. Jack's father later branched into finance broking, financial planning, and now runs his own accounting practice.</p>
      </li>
      <li class="tl tl--now">
        <div class="tl-era">Today</div>
        <h3>Jack</h3>
        <div class="tl-bank">Home Loan Essentials</div>
        <p>Four generations of financial experience, brought together in a modern broking practice that puts the client first.</p>
      </li>
    </ol>
  </div>
</section>

<!-- TODO (Jack): check this section describes how you and Duncan actually work together, and edit anything that is not quite right. -->
<section class="sec sec--tight sec--cream" aria-labelledby="duncan-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Working with Duncan</p>
      <h2 class="h2" id="duncan-title">Two generations, <em>one plan</em></h2>
      <p class="lead">Jack's dad, Duncan Perkins, has more than 40 years across banking, finance broking, accounting and financial planning. He is the owner of Tax Time Accountants &amp; Home Loan Essentials.</p>
      <!-- TODO (Jack): replace these placeholders with real photos of you and Duncan (landscape, at least 1200px wide, saved as .webp in /images/). -->
      <div class="ph" style="margin-top:2rem" role="img" aria-label="Photo placeholder">Photo to come: Jack and Duncan</div>
    </div>
    <div>
      <p class="lead" style="max-width:none">A home loan rarely sits on its own. It touches your tax, your cash flow, your business and your long-term plans. Because Duncan is a broker, a financial planner and a tax agent, Jack can bring him into the conversation when a loan decision has a tax or planning side to it.</p>
      <ul class="ticks" style="margin-top:2rem">
        <li>Structuring investment loans so they make sense at tax time, not just on settlement day.</li>
        <li>Self-employed clients whose income needs an accountant's eye before it goes to a lender.</li>
        <li>Thinking about debt, investing and your own business as one picture, not separate decisions.</li>
      </ul>
      <p class="fine">Jack also works alongside your own accountant, solicitor and builder if you already have people you trust.</p>
      <a class="callout" style="margin-top:2rem" href="https://www.youtube.com/watch?v=-MDItGVBamI" target="_blank" rel="noopener"><span class="callout-icon"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg></span><span><strong class="callout-title">Watch Duncan explain his approach</strong><span class="callout-text">Holistic Financial Advice: Why Your Business Might Be Your Best Investment (YouTube)</span></span><span class="go">{ARROW}</span></a>
    </div>
  </div>
</section>

<section class="sec sec--tight sec--paper" aria-labelledby="how-title">
  <div class="wrap">
    <p class="eyebrow">How Jack works</p>
    <h2 class="h2" id="how-title">What you can <em>expect</em></h2>
    <ol class="steps">
      <li class="step"><h3>A free first conversation</h3><p>No cost and no obligation. Jack listens first, then tells you honestly what is possible and what is not.</p></li>
      <li class="step"><h3>The people around you</h3><p>Jack works with your accountant, solicitor and builder so everyone is on the same page and nothing falls through the gaps.</p></li>
      <li class="step"><h3>30+ lenders compared</h3><p>Banks, credit unions and non-bank lenders, so the recommendation fits your situation rather than one lender's product list.</p></li>
      <li class="step"><h3>With you to settlement</h3><p>The same person from the first call to the keys, and still there when it is time to review your loan.</p></li>
    </ol>
    <div class="info-grid" style="margin-top:3rem">
      <div class="ph" role="img" aria-label="Photo placeholder">Photo to come: Jack with clients</div>
      <div class="ph" role="img" aria-label="Photo placeholder">Photo to come: Helensvale office or local area</div>
    </div>
  </div>
</section>
{cta_band()}
"""
    page += foot()
    write("about.html", page)
    print("about: 1")


# ---------------------------------------------------------------- articles
def article_card(a):
    return (f'<a class="card" href="/articles/{a["slug"]}.html"><span class="card-tag">{esc(a["category"])}</span>'
            f'<h3>{esc(a["title"])}</h3><p>{esc(a["summary"])}</p>'
            f'<span class="card-meta"><time datetime="{a["date"]}">{nice_date(a["date"])}</time><span>{a["read"]} min read</span></span>'
            f'<span class="more">Read article {ARROW}</span></a>')


def build_articles():
    for a in ARTICLES:
        path = f"/articles/{a['slug']}.html"
        trail = [("Home", "/"), ("Articles", "/resources.html"), (a["title"], path)]
        art_ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": a["title"],
            "description": a["meta"],
            "datePublished": a["date"],
            "dateModified": a["date"],
            "author": {"@type": "Person", "name": "Jack Perkins", "jobTitle": "Finance Broker", "url": SITE + "/about.html"},
            "publisher": {"@type": "Organization", "name": "Home Loan Essentials", "logo": {"@type": "ImageObject", "url": SITE + "/images/logo.png"}},
            "mainEntityOfPage": SITE + path,
            "image": SITE + "/images/share.jpg",
        }
        # DRAFT: noindex until Jack has reviewed and approved the article. Delete the robots meta line in
        # tools/build_more.py (search "DRAFT") when the articles are approved, then rerun the build.
        page = head(f"{a['title']} | Home Loan Essentials", a["meta"], path, ld=[art_ld, breadcrumbs_ld(trail)],
                    og_type="article", extra_head='<meta name="robots" content="noindex"/>\n')
        cslug, cname = a["calc"]
        others = "".join(f'<li><a href="/articles/{o["slug"]}.html">{esc(o["title"])}</a></li>' for o in ARTICLES if o["slug"] != a["slug"])
        page += f"""
<!-- DRAFT: written for Jack to review. Not yet approved for publishing. -->
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">{esc(a['category'])}</p>
    <h1>{esc(a['title'])}</h1>
    <p class="lead">{esc(a['summary'])}</p>
    <p class="meta-line"><span>By Jack Perkins</span><time datetime="{a['date']}">{nice_date(a['date'])}</time><span>{a['read']} min read</span></p>
  </div>
</section>

<section class="sec sec--tight sec--paper">
  <div class="wrap article-layout">
    <article class="prose">
      {a['body'].strip()}
      <p class="fine">This article is general information only and does not take into account your objectives, financial situation or needs. Talk to Jack before making a decision about a loan.</p>
    </article>
    <aside class="aside-card" aria-label="Talk to Jack">
      <h2>Talk it through with Jack</h2>
      <p>Free, no-obligation and specific to your situation.</p>
      <a href="/#contact" class="btn-green">Send Jack a message</a>
      <a href="tel:0478938981" class="btn-line" style="width:100%;margin-top:.6rem">Call 0478 938 981</a>
      <h2 style="margin-top:1.75rem;font-size:1rem">Try the numbers</h2>
      <ul><li><a href="/calculators/{cslug}.html">{esc(cname)}</a></li></ul>
      <h2 style="margin-top:1.25rem;font-size:1rem">More articles</h2>
      <ul>{others}</ul>
    </aside>
  </div>
</section>
{cta_band()}
"""
        page += foot()
        write(path.lstrip("/"), page)

    # index (replaces the old resources page, keeping its government schemes, video and follow sections)
    path = "/resources.html"
    trail = [("Home", "/"), ("Articles & Resources", path)]
    desc = ("Plain-English home loan articles from Jack Perkins, free calculators, and the government schemes and "
            "resources worth knowing about.")
    page = head("Articles & Resources | Home Loan Essentials", desc, path, extra_css=("calc.css",), ld=[breadcrumbs_ld(trail)])
    li_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'
    page += f"""
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">Articles &amp; resources</p>
    <h1>Straight answers, <em>written down</em></h1>
    <p class="lead">Plain-English articles on the questions Jack hears most, plus the calculators and government resources worth bookmarking.</p>
  </div>
</section>

<!-- DRAFT: the three articles below are drafts for Jack to review before launch. -->
<section class="sec sec--tight sec--paper" aria-labelledby="art-title">
  <div class="wrap">
    <p class="eyebrow">Latest articles</p>
    <h2 class="h2" id="art-title">From the <em>blog</em></h2>
    <div class="cards">{''.join(article_card(a) for a in ARTICLES)}</div>
  </div>
</section>

<section class="sec sec--tight sec--white" aria-labelledby="tools-title">
  <div class="wrap">
    <p class="eyebrow">Tools</p>
    <h2 class="h2" id="tools-title">Run the <em>numbers</em></h2>
    <div class="cards">{''.join(calc_card(c) for c in CALCS)}</div>
  </div>
</section>

<section class="sec sec--tight sec--cream" aria-labelledby="gov-title">
  <div class="wrap">
    <p class="eyebrow">Government support</p>
    <h2 class="h2" id="gov-title">Government schemes <em>&amp; tools</em></h2>
    <div class="info-grid">
      <div class="info-card">
        <p class="info-tag">Official Australian Government</p>
        <h3>Australian Government 5% Deposit Scheme</h3>
        <!-- TODO (Jack): the "248,000 Australians" figure came from the old page. Confirm it against firsthomebuyers.gov.au or remove it. -->
        <p>Buy your first home with as little as a 5% deposit. No Lenders Mortgage Insurance, no income caps, no waitlist. Over 248,000 Australians have already used this scheme. Find out if you're eligible.</p>
        <p><a class="more" style="color:var(--green);font-weight:600" href="https://firsthomebuyers.gov.au/australian-government-5-percent-deposit-scheme/property-price-caps/" target="_blank" rel="noopener">View property price caps &#8599;</a></p>
        <p><a class="more" style="color:var(--green);font-weight:600" href="https://firsthomebuyers.gov.au/" target="_blank" rel="noopener">Check your eligibility &#8599;</a></p>
      </div>
      <div class="info-card">
        <p class="info-tag">ASIC: Government resource</p>
        <h3>Moneysmart</h3>
        <p>Australia's government-backed financial literacy hub. Use their mortgage calculators, budgeting tools and loan comparison guides.</p>
        <p><a style="color:var(--green);font-weight:600" href="https://moneysmart.gov.au/" target="_blank" rel="noopener">Visit Moneysmart &#8599;</a></p>
      </div>
      <div class="info-card">
        <p class="info-tag">Government housing body</p>
        <h3>Housing Australia</h3>
        <p>The body that administers the 5% Deposit Scheme and other government housing support programs.</p>
        <p><a style="color:var(--green);font-weight:600" href="https://www.housingaustralia.gov.au/" target="_blank" rel="noopener">Visit Housing Australia &#8599;</a></p>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--tight sec--paper" aria-labelledby="video-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Watch &amp; learn</p>
      <h2 class="h2" id="video-title">From our video <em>library</em></h2>
    </div>
    <div>
      <h3 class="h3">Holistic Financial Advice: Why Your Business Might Be Your Best Investment</h3>
      <p class="fine" style="margin-top:.75rem">Duncan Perkins, Owner of Tax Time Accountants &amp; Home Loan Essentials &middot; 40+ years across banking, finance broking, accounting &amp; financial planning</p>
      <p class="lead" style="max-width:none;margin-top:1rem">Jack's father Duncan Perkins covers the big financial ideas most advisers never tell you, from how to think about debt and investment, to why your own business or education might be your smartest financial move. Worth a watch if you are thinking about building wealth over the long term.</p>
      <a href="https://www.youtube.com/watch?v=-MDItGVBamI" target="_blank" rel="noopener" class="btn-green" style="margin-top:1.5rem">Watch on YouTube <span aria-hidden="true">&#8599;</span></a>
    </div>
  </div>
</section>

<section class="sec sec--tight sec--white" aria-labelledby="follow-title">
  <div class="wrap">
    <p class="eyebrow">Follow along</p>
    <h2 class="h2" id="follow-title">Connect <em>with us</em></h2>
    <p class="lead">Follow Jack and Duncan on LinkedIn, and Home Loan Essentials on Instagram, for ongoing insights, tips, and financial commentary.</p>
    <div class="info-grid">
      <div class="info-card">
        <p class="info-tag">Finance Broker, Home Loan Essentials</p>
        <h3>Jack Perkins</h3>
        <p>Jack works with first home buyers, investors and self-employed clients to find the right lending solution for their situation. Follow along for tips, updates and insights.</p>
        <a href="https://www.linkedin.com/in/jack-perkins-homeloanessentials/" target="_blank" rel="noopener" class="btn-line" style="margin-top:1.25rem">{li_svg}Connect with Jack</a>
      </div>
      <div class="info-card">
        <p class="info-tag">Owner, Tax Time Accountants &amp; Home Loan Essentials</p>
        <h3>Duncan Perkins</h3>
        <p>Duncan brings 40+ years across banking, broking, accounting and financial planning. Follow him for holistic financial thinking you won't hear anywhere else.</p>
        <a href="https://www.linkedin.com/in/duncan-perkins/" target="_blank" rel="noopener" class="btn-line" style="margin-top:1.25rem">{li_svg}Connect with Duncan</a>
      </div>
      <div class="info-card">
        <p class="info-tag">Instagram</p>
        <h3>@homeloanessentials</h3>
        <p>Behind the scenes, quick tips and updates from Home Loan Essentials.</p>
        <a href="https://www.instagram.com/homeloanessentials/" target="_blank" rel="noopener" class="btn-line" style="margin-top:1.25rem">Follow on Instagram</a>
      </div>
    </div>
  </div>
</section>
{cta_band("Ready to take the <em>next step?</em>", "No obligation. No jargon. Just honest answers from Jack.")}
"""
    page += foot()
    write("resources.html", page)
    print("articles:", len(ARTICLES), "+ index")


# ---------------------------------------------------------------- credit guide placeholder
def build_credit_guide():
    path = "/credit-guide.html"
    trail = [("Home", "/"), ("Credit Guide", path)]
    page = head("Credit Guide | Home Loan Essentials", "Home Loan Essentials Credit Guide.", path,
                ld=[breadcrumbs_ld(trail)], extra_head='<meta name="robots" content="noindex"/>\n')
    page += f"""
<!-- TODO (Jack): your licensee (aggregator) supplies an approved Credit Guide. Paste its text into this page, or upload the PDF
     to /docs/credit-guide.pdf and link it below. Then remove the robots noindex line in tools/build_more.py and rerun the build. -->
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">Legal</p>
    <h1>Credit <em>Guide</em></h1>
    <p class="lead">Our Credit Guide explains who we are, how we are paid, and what to do if you have a complaint.</p>
  </div>
</section>
<section class="sec sec--tight sec--paper">
  <div class="wrap">
    <div class="prose">
      <p>Our current Credit Guide is available on request. Call Jack on <a href="tel:0478938981">0478 938 981</a> or email <a href="mailto:jack@homeloanessentials.com.au">jack@homeloanessentials.com.au</a> and we will send you a copy.</p>
    </div>
  </div>
</section>
"""
    page += foot()
    write("credit-guide.html", page)


# ---------------------------------------------------------------- sitemap, llms.txt
def build_sitemap():
    urls = [("/", "1.0"), ("/about.html", "0.8"), ("/diy.html", "0.8"), ("/faq.html", "0.7"), ("/resources.html", "0.7"),
            ("/calculators/", "0.8")]
    urls += [(f"/services/{s['slug']}.html", "0.8") for s in SERVICES]
    urls += [(f"/calculators/{c['slug']}.html", "0.7") for c in CALCS]
    # Draft articles and the credit guide placeholder are left out until approved.
    urls += [("/privacy.html", "0.3"), ("/terms.html", "0.3")]
    body = "".join(f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <priority>{p}</priority>\n  </url>\n" for u, p in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n')
    print("sitemap urls:", len(urls))


def build_llms():
    groups = {}
    for s in SERVICES:
        groups.setdefault(s["group"], []).append(s)
    lines = [
        "# Home Loan Essentials",
        "",
        "> Home Loan Essentials is a mortgage broking business run by Jack Perkins, based in Helensvale on the Gold Coast, Queensland, "
        "and serving clients across Australia. Jack compares home loans from a panel of 30+ banks, credit unions and non-bank lenders. "
        "There is no broker fee to the client; brokers are usually paid by the lender.",
        "",
        "- Phone: 0478 938 981",
        "- Email: jack@homeloanessentials.com.au",
        "- Location: Helensvale, Gold Coast QLD. Works with clients in every state and territory, in person or online.",
        "- All content on this site is general information only, not personal credit or financial advice.",
        "",
    ]
    for g, items in groups.items():
        lines.append(f"## {g}")
        lines.append("")
        for s in items:
            lines.append(f"- [{s['nav']}]({SITE}/services/{s['slug']}.html): {s['meta']}")
        lines.append("")
    lines += ["## Calculators", ""]
    lines += [f"- [{c['name']}]({SITE}/calculators/{c['slug']}.html): {c['meta']}" for c in CALCS]
    lines += ["", "## About and guides", "",
              f"- [About Jack Perkins]({SITE}/about.html): Background, four generations of banking, and how Jack works with his dad Duncan.",
              f"- [DIY Home Loan]({SITE}/diy.html): A home loan structure using a split loan and line of credit to pay down debt while investing.",
              f"- [FAQ]({SITE}/faq.html): Common questions about using a mortgage broker.",
              f"- [Articles & Resources]({SITE}/resources.html): Articles, calculators and government schemes.",
              ""]
    write("llms.txt", "\n".join(lines))


def run():
    build_calculators()
    build_about()
    build_articles()
    build_credit_guide()
    build_sitemap()
    build_llms()
