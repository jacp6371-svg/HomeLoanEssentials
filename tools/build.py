#!/usr/bin/env python3
"""Home Loan Essentials site builder.

The website is plain HTML hosted on Vercel with no build step there. This script runs on a
computer before committing and does three jobs:

  1. Copies the one master header (tools/partials/header.html) and footer
     (tools/partials/footer.html) into every page between the @header / @footer markers,
     so the menu and footer stay identical everywhere.
  2. Generates the service, calculator, article and about pages from the content files in tools/.
  3. Writes sitemap.xml.

Run it from the repository root:  python3 tools/build.py
"""
import html, json, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SITE = "https://www.homeloanessentials.com.au"
# TODO (Jack): when you choose a booking tool (Calendly, Cal.com, Acuity...), put its link here and rerun this script.
BOOKING_URL = "/#contact"
TODAY = date.today().isoformat()

CHEV = '<svg class="hd-chev" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CALC_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="2.5" width="16" height="19" rx="2.5"/><path d="M8 6.5h8M8 11h.01M12 11h.01M16 11h.01M8 14.5h.01M12 14.5h.01M16 14.5h.01M8 18h.01M12 18h4"/></svg>'


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def write(p, s):
    full = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(s)


def partial(name):
    s = read(f"tools/partials/{name}.html")
    return s.replace("{{CHEV}}", CHEV).replace("{{BOOKING_URL}}", BOOKING_URL).strip()


HEADER = partial("header")
FOOTER = partial("footer")


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=1, ensure_ascii=False) + "\n</script>"


def breadcrumbs_ld(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE + url}
            for i, (name, url) in enumerate(trail)
        ],
    }


def faq_ld(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def head(title, desc, path, extra_css=(), ld=(), og_type="website", extra_head=""):
    url = SITE + path
    css = "".join(f'<link rel="stylesheet" href="/assets/{c}"/>\n' for c in ("base.css", "site.css", "inner.css") + tuple(extra_css))
    lds = "\n".join(jsonld(o) for o in ld)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}"/>
<link rel="canonical" href="{url}"/>
<meta property="og:title" content="{esc(title)}"/>
<meta property="og:description" content="{esc(desc)}"/>
<meta property="og:type" content="{og_type}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:image" content="{SITE}/images/share.jpg"/>
<meta property="og:locale" content="en_AU"/>
<meta name="twitter:card" content="summary_large_image"/>
<link rel="icon" type="image/png" href="/favicon.png"/>
<link rel="apple-touch-icon" href="/favicon.png"/>
<meta name="theme-color" content="#1c2b27"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"/>
{css}<script>document.documentElement.classList.add('js')</script>
{extra_head}{lds}
</head>
<body>
<!-- @header -->
{HEADER}
<!-- /@header -->
<main id="main">
"""


def foot(scripts=()):
    js = "".join(f'<script src="{s if s.startswith("http") else "/assets/" + s}" defer></script>\n' for s in ("site.js", "track.js") + tuple(scripts))
    return f"""</main>
<!-- @footer -->
{FOOTER}
<!-- /@footer -->
{js}</body>
</html>
"""


def crumbs_html(trail):
    items = []
    for i, (name, url) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            items.append(f'<li><a href="{url}">{esc(name)}</a></li>')
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">' + "".join(items) + "</ol></nav>"


def cta_band(title="Ready to talk it <em>through?</em>", text="No obligation, no jargon. Just honest advice from a broker who stays with you from the first question to settlement."):
    return f"""
<section class="cta-band" aria-labelledby="cta-title">
  <div class="wrap">
    <div>
      <h2 id="cta-title">{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-actions">
      <a href="/#contact" class="btn-green">Send Jack a message</a>
      <a href="tel:0478938981" class="btn-line btn-line--light">Call 0478 938 981</a>
    </div>
  </div>
</section>
"""


def faq_html(faqs):
    out = ['<div class="faqs">']
    for q, a in faqs:
        out.append(f"<details><summary>{esc(q)}</summary><div class=\"ans\"><p>{esc(a)}</p></div></details>")
    out.append("</div>")
    return "\n".join(out)


# ---------------------------------------------------------------- services
def build_services():
    from content_services import SERVICES
    by_slug = {s["slug"]: s for s in SERVICES}
    from content_calcs import CALCS
    calc_names = {c["slug"]: c for c in CALCS}
    for s in SERVICES:
        path = f"/services/{s['slug']}.html"
        trail = [("Home", "/"), ("Services", "/#services"), (s["nav"], path)]
        service_ld = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": strip_tags(s["h1"]),
            "serviceType": s["group"],
            "description": s["meta"],
            "areaServed": [{"@type": "State", "name": "Queensland"}, {"@type": "Country", "name": "Australia"}],
            "provider": {"@type": "FinancialService", "name": "Home Loan Essentials", "url": SITE + "/", "telephone": "+61478938981"},
            "url": SITE + path,
        }
        page = head(f"{s['title']} | Home Loan Essentials", s["meta"], path,
                    ld=[service_ld, breadcrumbs_ld(trail), faq_ld(s["faqs"])])
        suits = "".join(f"<li>{esc(x)}</li>" for x in s["suits"])
        steps = "".join(f"<li class=\"step\"><h3>{esc(t)}</h3><p>{esc(d)}</p></li>" for t, d in s["steps"])
        referral = ""
        if s.get("referral"):
            referral = ('<p class="note-box">Home lending is Jack\'s focus. For business and asset finance, he can look after '
                        'straightforward deals himself or refer you to a trusted asset finance specialist where that gets you a better result, '
                        'and he will always tell you which.</p>')
        extra = ""
        if s.get("extra_html"):
            extra = f"""
<section class="sec sec--tight sec--white" aria-labelledby="extra-title">
  <div class="wrap">
    <p class="eyebrow">Good to know</p>
    <h2 class="h2" id="extra-title">{esc(s['extra_title'])}</h2>
    {s['extra_html']}
  </div>
</section>"""
        cslug, cname, cblurb = s["calc"]
        related = "".join(
            f'<a class="card" href="/services/{r}.html"><span class="card-tag">{esc(by_slug[r]["group"])}</span>'
            f'<h3>{esc(by_slug[r]["nav"])}</h3><p>{esc(by_slug[r]["intro"].split(". ")[0])}.</p>'
            f'<span class="more">Read more {ARROW}</span></a>'
            for r in s["related"])
        page += f"""
<section class="page-hero">
  <div class="wrap">
    {crumbs_html(trail)}
    <p class="eyebrow">{esc(s['group'])}</p>
    <h1>{s['h1']}</h1>
    <p class="lead">{esc(s['intro'])}</p>
    <div class="hero-actions">
      <a href="/#contact" class="btn-green">Talk to Jack</a>
      <a href="tel:0478938981" class="btn-line btn-line--light">Call 0478 938 981</a>
    </div>
  </div>
</section>

<section class="sec sec--tight sec--paper" aria-labelledby="suits-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Who it suits</p>
      <h2 class="h2" id="suits-title">Is this <em>you?</em></h2>
      <p class="lead">If any of these sound familiar, this is the right place to start.</p>
    </div>
    <ul class="ticks">{suits}</ul>
  </div>
</section>

<section class="sec sec--tight sec--cream" aria-labelledby="how-title">
  <div class="wrap">
    <p class="eyebrow">How it works</p>
    <h2 class="h2" id="how-title">Step by <em>step</em></h2>
    <ol class="steps">{steps}</ol>
    {referral}
  </div>
</section>
{extra}
<section class="sec sec--tight sec--paper" aria-labelledby="needs-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Before we start</p>
      <h2 class="h2" id="needs-title">What Jack needs <em>from you</em></h2>
    </div>
    <div>
      <p class="lead" style="max-width:none">{esc(s['needs'])}</p>
      <div style="margin-top:2rem"><a class="callout" href="/calculators/{cslug}.html"><span class="callout-icon">{CALC_ICON}</span><span><strong class="callout-title">{esc(cname)}</strong><span class="callout-text">{esc(cblurb)}</span></span><span class="go">{ARROW}</span></a></div>
    </div>
  </div>
</section>

<section class="sec sec--tight sec--white" aria-labelledby="faq-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Common questions</p>
      <h2 class="h2" id="faq-title">Questions people <em>ask</em></h2>
      <p class="lead">Still unsure? <a href="/faq.html" style="color:var(--green)">See the full FAQ</a> or ask Jack directly.</p>
    </div>
    {faq_html(s['faqs'])}
  </div>
</section>

<section class="sec sec--tight sec--paper" aria-labelledby="rel-title">
  <div class="wrap">
    <p class="eyebrow">Related</p>
    <h2 class="h2" id="rel-title">You might also <em>need</em></h2>
    <div class="cards">{related}</div>
  </div>
</section>
{cta_band()}
"""
        page += foot()
        write(path.lstrip("/"), page)
    print("services:", len(SERVICES))


# ---------------------------------------------------------------- inject header/footer into hand-written pages
def inject_shared(files):
    for f in files:
        s = read(f)
        s2 = re.sub(r"<!-- @header -->.*?<!-- /@header -->", "<!-- @header -->\n" + HEADER + "\n<!-- /@header -->", s, flags=re.S)
        s2 = re.sub(r"<!-- @footer -->.*?<!-- /@footer -->", "<!-- @footer -->\n" + FOOTER + "\n<!-- /@footer -->", s2, flags=re.S)
        if "<!-- @header -->" not in s2:
            raise SystemExit(f"{f}: no @header marker")
        if s2 != s:
            write(f, s2)


if __name__ == "__main__":
    build_services()
    import build_more
    build_more.run()
    inject_shared([f for f in ("index.html", "diy.html", "faq.html", "privacy.html", "terms.html") if os.path.exists(os.path.join(ROOT, f))])
