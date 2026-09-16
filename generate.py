#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EMAIL = "sales@aettram.ind.in"
PHONE = "+91 97899 91992"
PHONE_TEL = "+919789991992"
WA = "https://wa.me/919789991992"
SITE = "https://aettram.ind.in"

SERVICES_NAV = [
    ("CNC Machining", [
        ("cnc-milling.html", "CNC Milling"),
        ("cnc-turning.html", "CNC Turning"),
        ("cnc-routing.html", "CNC Routing"),
        ("swiss-machining.html", "Swiss Machining"),
        ("micro-machining.html", "Micro Machining"),
    ]),
    ("Sheet Metal", [
        ("sheet-metal-fabrication.html", "Fabrication"),
        ("sheet-cutting.html", "Sheet Cutting"),
        ("laser-cutting.html", "Laser Cutting"),
        ("waterjet-cutting.html", "Waterjet Cutting"),
        ("laser-tube-cutting.html", "Laser Tube Cutting"),
        ("tube-bending.html", "Tube Bending"),
    ]),
    ("Automation", [
        ("automation-spm.html", "Assembly Automation"),
        ("machine-tending.html", "Machine Tending"),
        ("robotic-assembly-testing.html", "Robotic Assembly & Testing"),
        ("vision-inspection.html", "Vision Inspection"),
    ]),
]

INDUSTRIES_NAV = [
    ("aerospace.html", "Aerospace"),
    ("automotive.html", "Automotive"),
    ("medical-devices.html", "Medical Devices"),
    ("industrial-machinery.html", "Industrial Machinery"),
    ("electronics.html", "Electronics"),
    ("energy.html", "Energy"),
    ("robotics.html", "Robotics"),
]


def pfx(depth):
    return "../" * depth


def cdn():
    return """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/css/glightbox.min.css">
<link rel="stylesheet" href="https://unpkg.com/splitting@1.0.6/dist/splitting.css">
"""


def scripts():
    return """
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/glightbox@3.3.0/dist/js/glightbox.min.js" defer></script>
<script src="https://unpkg.com/splitting@1.0.6/dist/splitting.min.js" defer></script>
"""


def head(depth, title, desc, path):
    a = pfx(depth)
    canon = f"{SITE}/{path.lstrip('/')}" if path != "index.html" else f"{SITE}/"
    og = f"{a}assets/images/hero/cnc-closeup.webp"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<link rel="icon" href="{a}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{a}favicon.ico">
<link rel="apple-touch-icon" href="{a}apple-touch-icon.png">
{cdn()}
<link rel="stylesheet" href="{a}assets/css/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


CARET = (
    '<svg class="nav-caret" width="12" height="12" viewBox="0 0 12 12" fill="none" '
    'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
    '<path d="M2.2 4.2L6 8l3.8-3.8" fill="none" stroke="#D8D6D2" stroke-width="1.6" '
    'stroke-linecap="round" stroke-linejoin="round"/></svg>'
)


def nav(depth, active=""):
    a = pfx(depth)
    s = a + "services/"
    i = a + "industries/"

    def act(name):
        return ' is-active' if active == name else ""

    cols = ""
    for heading, links in SERVICES_NAV:
        lis = "".join(f'<a href="{s}{href}">{label}</a>' for href, label in links)
        cols += f"<div><h4>{heading}</h4>{lis}</div>"
    ind = "".join(f'<a href="{i}{href}">{label}</a>' for href, label in INDUSTRIES_NAV)
    return f"""
<header class="site-header">
  <div class="nav-inner">
    <a class="logo" href="{a}index.html" aria-label="Aettram home">
      <span class="logo-mark" aria-hidden="true">A</span>
      <span class="logo-word">AETTRAM</span>
    </a>
    <nav class="nav-links" aria-label="Primary">
      <a class="nav-link{act('home')}" href="{a}index.html">Home</a>
      <a class="nav-link{act('about')}" href="{a}about.html">About</a>
      <div class="dropdown">
        <a class="nav-link{act('services')}" href="{a}services.html">Services {CARET}</a>
        <div class="dropdown-menu wide" role="menu">{cols}</div>
      </div>
      <a class="nav-link{act('mfg')}" href="{a}manufacturing.html">Manufacturing</a>
      <div class="dropdown">
        <a class="nav-link{act('industries')}" href="{a}industries.html">Industries {CARET}</a>
        <div class="dropdown-menu align-end" role="menu">{ind}</div>
      </div>
      <a class="nav-link{act('contact')}" href="{a}contact.html">Contact</a>
    </nav>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<nav class="mobile-panel" aria-label="Mobile">
  <a href="{a}index.html">Home</a>
  <a href="{a}about.html">About</a>
  <a href="{a}services.html">Services</a>
  <a href="{a}manufacturing.html">Manufacturing</a>
  <a href="{a}industries.html">Industries</a>
  <a href="{a}contact.html">Contact</a>
</nav>
"""


def contact_ctas():
    return f"""
    <div class="cta-grid">
      <a class="cta-card cta-card--solid" href="{WA}" target="_blank" rel="noopener">
        <span class="cta-icon" aria-hidden="true">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        </span>
        <span class="cta-copy"><strong>WhatsApp</strong><small>{PHONE}</small></span>
      </a>
      <a class="cta-card" href="mailto:{EMAIL}">
        <span class="cta-icon" aria-hidden="true">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 7 9-7"/></svg>
        </span>
        <span class="cta-copy"><strong>Email</strong><small>{EMAIL}</small></span>
      </a>
    </div>
"""


def contact_strip(depth):
    return f"""
<section class="contact-strip grain" id="talk">
  <div class="container">
    <p class="eyebrow">Contact</p>
    <h2>Let's talk shop.</h2>
    <p>WhatsApp or email — no forms.</p>
    {contact_ctas()}
  </div>
</section>
"""


def footer(depth):
    a = pfx(depth)
    s = a + "services/"
    i = a + "industries/"
    svc = "".join(
        f'<a href="{s}{href}">{label}</a>'
        for _, links in SERVICES_NAV for href, label in links[:3]
    )
    ind = "".join(f'<a href="{i}{href}">{label}</a>' for href, label in INDUSTRIES_NAV)
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="logo" href="{a}index.html"><span class="logo-mark">A</span><span class="logo-word">AETTRAM</span></a>
      <p style="margin-top:16px">From concept to production, we build practical solutions under one roof.</p>
    </div>
    <div>
      <h4>Services</h4>
      {svc}
      <a href="{a}services.html">All services</a>
    </div>
    <div>
      <h4>Industries</h4>
      {ind}
    </div>
    <div>
      <h4>Company</h4>
      <a href="{a}about.html">About / Facility</a>
      <a href="{a}manufacturing.html">Manufacturing</a>
      <a href="{a}contact.html">Contact</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© 2026 Aettram. All rights reserved.</p>
    <p>Precision manufacturing · India</p>
  </div>
</footer>
{scripts()}
<script src="{a}assets/js/main.js" defer></script>
</body>
</html>
"""


def close_main(depth):
    return "</main>" + contact_strip(depth) + footer(depth)


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def page_hero(title, eyebrow, sub, img, depth):
    a = pfx(depth)
    return f"""
<header class="page-hero grain">
  <div class="bg"><img src="{a}{img}" alt=""></div>
  <div class="container">
    <p class="eyebrow">{eyebrow}</p>
    <h1 data-aos="fade-up">{title}</h1>
    <p class="lead" data-aos="fade-up" data-aos-delay="80">{sub}</p>
  </div>
</header>
"""


# ---------- pages ----------
def index():
    d = 0
    html = head(d, "Aettram — We Engineer. We Manufacture. We Deliver.", "Aettram designs and manufactures CNC parts, sheet-metal assemblies, and automation systems in our own production center.", "index.html")
    html += nav(d, "home")
    slides = ""
    for src, title, cap in [
        ("assets/images/services/robot-metal.webp", "Custom Robotic Assembly Cell", "Fanuc-class cell · in-house tooling"),
        ("assets/images/products/bracket.webp", "Aerospace Bracket — 5-Axis Milled", "Ti-6Al-4V · ±0.02 mm"),
        ("assets/images/products/machined-parts.webp", "Precision Housing Set", "Al 6061-T6 · anodize ready"),
        ("assets/images/products/gears.webp", "Industrial Gear Train", "Hardened steel · ground teeth"),
        ("assets/images/services/laser.webp", "Laser-Cut Enclosure", "Mild steel · powder coat"),
        ("assets/images/products/aluminum.webp", "Micro-Finished Manifold", "SS 316 · CMM mapped"),
        ("assets/images/services/sheet-metal.webp", "Sheet-Metal Chassis", "1.5 mm CRS · PEM inserts"),
        ("assets/images/products/assembly-cell.webp", "Vision Inspection Station", "Inline cameras · PLC logic"),
    ]:
        slides += f"""
        <div class="swiper-slide">
          <a class="card glightbox" href="{src}" data-gallery="home">
            <div class="card-media"><img src="{src}" alt="{title}" loading="lazy"></div>
            <div class="card-body"><h3>{title}</h3><p>{cap}</p></div>
          </a>
        </div>"""
    sectors = ""
    for n, (slug, name, blurb) in enumerate([
        ("aerospace", "Aerospace", "Brackets, housings, and tooling we mill and inspect to drawing."),
        ("automotive", "Automotive", "Powertrain parts, EV enclosures, and cell fixtures from our bays."),
        ("medical-devices", "Medical Devices", "Instruments and diagnostic frames in clean, documented lots."),
        ("industrial-machinery", "Industrial Machinery", "Gears, shafts, manifolds, and guards we ship as assemblies."),
        ("electronics", "Electronics", "Chassis, heat-spreader plates, and semiconductor tooling plates."),
        ("robotics", "Robotics", "End-effectors, bases, and test cells we design around our robots."),
    ], start=1):
        sectors += f'<a class="card" href="industries/{slug}.html"><div class="card-body"><p class="eyebrow">{n:02d}</p><h3>{name}</h3><p>{blurb}</p></div></a>'
    html += f"""
<main id="main">
<section class="hero grain">
  <div class="hero-media" data-hero-media>
    <video autoplay muted loop playsinline poster="assets/images/hero/cnc-closeup.webp">
      <source src="assets/video/hero-laser.mp4" type="video/mp4">
    </video>
  </div>
  <div class="hero-overlay"></div>
  <div class="container">
    <p class="eyebrow">Precision Manufacturing · In-House</p>
    <h1 data-splitting>We Engineer. We Manufacture. We Deliver.</h1>
    <p class="sub">Aettram runs its own production center. We design product lines, machine components, fabricate sheet metal, and build automation cells — all on our floor.</p>
    <div class="hero-actions">
      <a class="btn btn--solid" href="contact.html">Contact Us</a>
      <a class="btn" href="services.html">Explore Services</a>
    </div>
  </div>
</section>

<section class="section section--light" id="about">
  <div class="container grid-2">
    <div>
      <p class="eyebrow">Who we are</p>
      <h2>A production company, not a pitch deck.</h2>
      <p class="lead">We started manufacturing under our own name so quality, schedule, and tooling stay in one building. CAD, CNC, fabrication, and cell integration sit on the same floor — we own the chain from drawing to finished assembly.</p>
      <a class="link-arrow" href="about.html">Our facility →</a>
      <div class="grid-3" style="margin-top:32px;grid-template-columns:1fr 1fr 1fr">
        <div class="pillar"><div class="num">01</div><h3>In-House Production</h3><p>Machines, brakes, lasers, and robots we program and run ourselves.</p></div>
        <div class="pillar"><div class="num">02</div><h3>ISO-Certified Process</h3><p>Documented QC from first article through CMM and surface verification.</p></div>
        <div class="pillar"><div class="num">03</div><h3>End-to-End Capability</h3><p>From billet and sheet to assembled, inspected, packed product.</p></div>
      </div>
    </div>
    <div class="frame">
      <img src="assets/images/facility/factory-interior.webp" alt="Aettram production floor interior" loading="lazy">
    </div>
  </div>
</section>

<section class="section section--graphite">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Capabilities</p>
      <h2>What we run in-house</h2>
    </div>
    <div class="grid-3">
      <a class="card" href="services.html">
        <div class="card-media"><img src="assets/images/hero/cnc-closeup.webp" alt="CNC machining"></div>
        <div class="card-body"><h3>CNC Machining</h3><p>Milling, turning, Swiss, and micro work on metals we specify and stock.</p><span class="link-arrow">Open CNC →</span></div>
      </a>
      <a class="card" href="services.html">
        <div class="card-media"><img src="assets/images/services/sheet-metal.webp" alt="Sheet metal fabrication"></div>
        <div class="card-body"><h3>Sheet Metal</h3><p>Laser, waterjet, tube, brake, and welded assemblies from our fab bay.</p><span class="link-arrow">Open fabrication →</span></div>
      </a>
      <a class="card" href="services.html">
        <div class="card-media"><img src="assets/images/services/robot-arm.webp" alt="Industrial robot arm"></div>
        <div class="card-body"><h3>Industrial Automation</h3><p>Cells we design, build, and prove out before they leave our floor.</p><span class="link-arrow">Open automation →</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Manufacturing</p>
      <h2>Featured work from our floor</h2>
      <p>Representative parts and systems we design and build. Full gallery on Manufacturing.</p>
    </div>
    <div class="swiper" data-swiper>
      <div class="swiper-wrapper">
        {slides}
      </div>
    </div>
    <p style="margin-top:28px"><a class="btn" href="manufacturing.html">Manufacturing gallery</a></p>
  </div>
</section>

<section class="section section--graphite">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Sectors</p>
      <h2>Work we manufacture for</h2>
    </div>
    <div class="grid-3">
      {sectors}
    </div>
    <p style="margin-top:28px"><a class="link-arrow" href="industries.html">All sectors →</a></p>
  </div>
</section>
"""
    html += close_main(d)
    write("index.html", html)


def about():
    d = 0
    html = head(d, "About — Aettram Facility", "Aettram runs its own production center: founding story, ISO process, and why we manufacture in-house.", "about.html")
    html += nav(d, "about")
    html += """
<main id="main">
""" + page_hero("We manufacture under our own name.", "About / Facility", "Aettram exists to design and build hardware on a floor we control — not to broker jobs across a vendor list.", "assets/images/facility/factory-floor.webp", d) + f"""
<section class="section section--light">
  <div class="container grid-2">
    <div>
      <p class="eyebrow">Story</p>
      <h2>From drawings to dock, one address.</h2>
      <p>We built Aettram as a production company: programmers, machinists, fabricators, and automation engineers sharing the same tooling library. When a part moves from mill to brake to cell, it does not leave our custody.</p>
      <p>ISO-certified process sits over that floor — travelers, first-article, CMM, and surface records — so the work we ship is the work we measured.</p>
    </div>
    <div class="frame"><img src="assets/images/facility/plant-aerial.webp" alt="Manufacturing plant interior" loading="lazy"></div>
  </div>
  <div class="container stats">
    <div><div class="stat-num" data-count="3">0</div><p>Core bays: CNC, sheet, automation</p></div>
    <div><div class="stat-num" data-count="4">0</div><p>Documented production stages</p></div>
    <div><div class="stat-num" data-count="7">0</div><p>Sectors we currently manufacture in</p></div>
  </div>
</section>
<section class="section section--graphite">
  <div class="container">
    <p class="eyebrow">Why in-house matters</p>
    <h2>Quality, speed, no middleman.</h2>
    <div class="values" style="margin-top:32px">
      <div class="pillar"><h3>Quality control</h3><p>Inspection happens next to the spindle, not after a third-party hop.</p></div>
      <div class="pillar"><h3>Schedule</h3><p>We queue our own machines. Fixture changes do not wait on someone else's calendar.</p></div>
      <div class="pillar"><h3>Knowledge</h3><p>Tooling, CAM, and PLC logic stay with the people who designed the product.</p></div>
    </div>
  </div>
</section>
<section class="section section--light">
  <div class="container">
    <p class="eyebrow">People on the floor</p>
    <h2>Engineering and operations</h2>
    <div class="grid-3" style="margin-top:28px">
      <div class="card"><div class="card-media"><img src="assets/images/team/cad-engineer.webp" alt="Engineer at CAD workstation" loading="lazy"></div><div class="card-body"><h3>Design</h3><p>CAD, CAM, and fixture design before metal moves.</p></div></div>
      <div class="card"><div class="card-media"><img src="assets/images/team/safety-worker.webp" alt="Operator in safety gear" loading="lazy"></div><div class="card-body"><h3>Production</h3><p>Setup, running, and in-process checks on our cells.</p></div></div>
      <div class="card"><div class="card-media"><img src="assets/images/team/metrology.webp" alt="Metrology and inspection" loading="lazy"></div><div class="card-body"><h3>Quality</h3><p>CMM, gauges, and surface finish against the drawing.</p></div></div>
    </div>
  </div>
</section>
"""
    html += close_main(d)
    write("about.html", html)


WORK = [
    ("cnc", "Aerospace Bracket — 5-Axis", "Ti-6Al-4V · 5-axis mill · ±0.02 mm", "assets/images/products/bracket.webp"),
    ("cnc", "Aluminum Housing Cluster", "Al 6061-T6 · 3-axis + face mill", "assets/images/products/machined-parts.webp"),
    ("cnc", "Hardened Gear Set", "AISI 4340 · hob / grind", "assets/images/products/gears.webp"),
    ("cnc", "Micro Manifold", "SS 316 · Swiss + mill", "assets/images/products/aluminum.webp"),
    ("sheet", "Laser Enclosure", "CRS 1.5 mm · fiber laser", "assets/images/services/laser.webp"),
    ("sheet", "Formed Chassis", "Sheet fab · PEM · powder", "assets/images/services/sheet-metal.webp"),
    ("sheet", "Tube Frame", "Laser tube + bend", "assets/images/services/tube.webp"),
    ("sheet", "Press-Brake Panel", "Brake · hem · weld prep", "assets/images/services/press-brake.webp"),
    ("auto", "Robotic Assembly Cell", "6-axis · custom EOAT", "assets/images/services/robot-metal.webp"),
    ("auto", "Weld Cell", "Robot + fixture table", "assets/images/services/robot-weld.webp"),
    ("assy", "Machine-Tend Pair", "Lathe tend · dual gripper", "assets/images/services/robot-arm.webp"),
    ("assy", "Vision Station", "Cameras · PLC · reject gate", "assets/images/products/assembly-cell.webp"),
    ("assy", "Sub-Assembly Kit", "Machined + sheet stack", "assets/images/products/components.webp"),
    ("cnc", "CNC Close Work", "Live tooling turning", "assets/images/hero/cnc-closeup.webp"),
    ("sheet", "Waterjet Nest", "Thick plate · abrasive jet", "assets/images/services/waterjet.webp"),
]


def manufacturing():
    d = 0
    html = head(d, "Manufacturing & Products — Aettram", "Portfolio of CNC parts, sheet-metal assemblies, and automation systems built in Aettram's facility.", "manufacturing.html")
    html += nav(d, "mfg")
    cards = ""
    for cat, title, spec, src in WORK:
        cards += f"""
        <a class="work-item glightbox" data-cat="{cat}" href="{src}" data-gallery="mfg">
          <div class="card-media frame"><img src="{src}" alt="{title}" loading="lazy"></div>
          <div class="work-caption"><strong>{title}</strong><span>{spec}</span></div>
        </a>"""
    html += """
<main id="main">
""" + page_hero("What we actually make.", "Manufacturing / Products", "A wall of work from our spindles, lasers, brakes, and cells. Filter by process. Open any image.", "assets/images/products/machined-parts.webp", d) + f"""
<section class="section section--light">
  <div class="container">
    <div class="filters" role="toolbar" aria-label="Filter gallery">
      <button class="filter-btn is-active" data-filter="all" aria-pressed="true">All</button>
      <button class="filter-btn" data-filter="cnc" aria-pressed="false">CNC Parts</button>
      <button class="filter-btn" data-filter="sheet" aria-pressed="false">Sheet Metal</button>
      <button class="filter-btn" data-filter="auto" aria-pressed="false">Automation Systems</button>
      <button class="filter-btn" data-filter="assy" aria-pressed="false">Assemblies</button>
    </div>
    <div class="masonry">{cards}</div>
  </div>
</section>
"""
    html += close_main(d)
    write("manufacturing.html", html)


def services_hub():
    d = 0
    html = head(d, "Services — Aettram In-House Capabilities", "CNC machining, sheet-metal fabrication, and industrial automation run as Aettram's own production capabilities.", "services.html")
    html += nav(d, "services")
    blocks = ""
    for heading, links in SERVICES_NAV:
        cards = ""
        for href, label in links:
            cards += f'<a class="card" href="services/{href}"><div class="card-body"><h3>{label}</h3><p>Built and run in our facility.</p><span class="link-arrow">Open →</span></div></a>'
        blocks += f'<div class="section-head"><p class="eyebrow">Capability</p><h2>{heading}</h2></div><div class="grid-3" style="margin-bottom:56px">{cards}</div>'
    html += """
<main id="main">
""" + page_hero("Capabilities we own.", "Services", "These are not subcontract menus. They are bays in our plant, with machines we program and maintain.", "assets/images/services/cnc-machines.webp", d) + f"""
<section class="section section--light"><div class="container">{blocks}</div></section>
"""
    html += close_main(d)
    write("services.html", html)


def industries_hub():
    d = 0
    html = head(d, "Industries — Work We Manufacture", "Aerospace, automotive, medical, machinery, electronics, energy, and robotics hardware built by Aettram.", "industries.html")
    html += nav(d, "industries")
    cards = "".join(
        f'<a class="card" href="industries/{href}"><div class="card-media"><img src="assets/images/{img}" alt="{label}" loading="lazy"></div><div class="card-body"><h3>{label}</h3><p>Hardware we have designed and built for this sector.</p></div></a>'
        for href, label, img in [
            ("aerospace.html", "Aerospace", "industries/aerospace.webp"),
            ("automotive.html", "Automotive", "industries/automotive.webp"),
            ("medical-devices.html", "Medical Devices", "industries/medical.webp"),
            ("industrial-machinery.html", "Industrial Machinery", "industries/machinery.webp"),
            ("electronics.html", "Electronics", "industries/electronics.webp"),
            ("energy.html", "Energy", "industries/energy.webp"),
            ("robotics.html", "Robotics", "industries/robotics.webp"),
        ]
    )
    html += """
<main id="main">
""" + page_hero("Sectors we manufacture in.", "Industries", "Depth over a vendor checklist. These are the fields our floor currently ships into.", "assets/images/industries/automotive.webp", d) + f"""
<section class="section section--light"><div class="container"><div class="grid-3">{cards}</div></div></section>
"""
    html += close_main(d)
    write("industries.html", html)


def contact():
    d = 0
    html = head(d, "Contact — Aettram", "Reach Aettram by WhatsApp or email. Production center, India. No contact form.", "contact.html")
    html += nav(d, "contact")
    html += f"""
<main id="main">
<section class="contact-block grain">
  <div class="container">
    <p class="eyebrow">Aettram</p>
    <h1>Talk to the floor.</h1>
    <p class="lead" style="margin-inline:auto">WhatsApp or email the people who run the machines. No forms.</p>
    {contact_ctas()}
    <p class="hours" style="margin-top:28px">Production Center · India<br>Monday–Saturday · 09:00–18:00 IST</p>
  </div>
</section>
"""
    html += footer(d)
    write("contact.html", html)


def error404():
    d = 0
    html = head(d, "404 — Aettram", "This page is not on the Aettram site.", "404.html")
    html += nav(d, "")
    html += f"""
<main id="main" class="error-page grain">
  <div>
    <p class="eyebrow">Error</p>
    <h1>404</h1>
    <p>That path is not in the plant map.</p>
    <a class="btn btn--solid" href="index.html">Back to home</a>
  </div>
</main>
""" + footer(d)
    write("404.html", html)


SERVICES = [
    dict(file="cnc-milling.html", title="CNC Milling", eyebrow="CNC · Milling",
         desc="Multi-axis milling of housings, brackets, and plates on machines we program in-house.",
         img="assets/images/hero/cnc-closeup.webp",
         highlights=[("3- and 5-axis", "Complex contours and compound angles in one setup."),
                     ("Fixture design", "Soft jaws and plates we cut for repeat families."),
                     ("Metals we run", "Aluminum, steels, stainless, titanium, engineering plastics."),
                     ("In-process probe", "Datums confirmed on the machine before the next op.")],
         gallery=["assets/images/hero/cnc-closeup.webp", "assets/images/services/cnc-milling.webp", "assets/images/products/bracket.webp", "assets/images/products/machined-parts.webp", "assets/images/team/metrology.webp", "assets/images/facility/factory-floor.webp"],
         spec=[("Typical tolerance", "±0.02 mm on critical features"), ("Envelope", "Up to 800 × 500 × 400 mm"), ("Materials", "Al 6061/7075, SS 304/316, Ti-6Al-4V, PEEK"), ("Machines", "3-axis VMCs, 5-axis mill")],
         related=["cnc-turning.html", "micro-machining.html", "swiss-machining.html"]),
    dict(file="cnc-turning.html", title="CNC Turning", eyebrow="CNC · Turning",
         desc="Live-tool turning for shafts, bushings, and rotational parts we finish on our lathes.",
         img="assets/images/services/turning.webp",
         highlights=[("Live tooling", "Mill-turn features without a second chucking when the drawing allows."),
                     ("Bar and chuck", "Prototype singles and production bar-fed lots."),
                     ("Hard turning", "Finish after heat treat on selected grades."),
                     ("Thread control", "UN, metric, and custom pitches we verify with gauges.")],
         gallery=["assets/images/services/turning.webp", "assets/images/services/cnc-machines.webp", "assets/images/products/aluminum.webp", "assets/images/products/gears.webp", "assets/images/hero/sparks.webp", "assets/images/team/safety-worker.webp"],
         spec=[("Typical tolerance", "±0.015 mm diameter"), ("Capacity", "Ø 320 mm × 500 mm between centers"), ("Materials", "Steels, stainless, brass, aluminum"), ("Machines", "Live-tool CNC lathes")],
         related=["cnc-milling.html", "swiss-machining.html", "cnc-routing.html"]),
    dict(file="cnc-routing.html", title="CNC Routing", eyebrow="CNC · Routing",
         desc="Large-format routing of plates, patterns, and non-ferrous panels on our routers.",
         img="assets/images/services/cnc-machines.webp",
         highlights=[("Large sheet", "Nested parts from plate we fixture on vacuum or T-slot."),
                     ("Patterns", "Jigs and form tools used later on our own fab line."),
                     ("Plastics & Al", "Clean edges on acetal, polycarb, and aluminum sheet."),
                     ("CAM nests", "Utilization we control because the stock is ours.")],
         gallery=["assets/images/services/cnc-machines.webp", "assets/images/products/components.webp", "assets/images/services/sheet-metal.webp", "assets/images/facility/factory-interior.webp", "assets/images/products/bracket.webp", "assets/images/hero/factory-dark.webp"],
         spec=[("Bed", "Up to 1200 × 2400 mm class"), ("Spindle", "High-speed router + mill tools"), ("Materials", "Al sheet, plastics, wood patterns"), ("Finish", "Deburr and edge break in-house")],
         related=["cnc-milling.html", "sheet-cutting.html", "laser-cutting.html"]),
    dict(file="swiss-machining.html", title="Swiss Machining", eyebrow="CNC · Swiss",
         desc="Slim, high-aspect parts from Swiss-type machines we keep for medical and precision lots.",
         img="assets/images/products/aluminum.webp",
         highlights=[("Guide bushing", "Long slender parts without whip."),
                     ("Sub-spindle", "Complete parts in one cycle."),
                     ("Small diameters", "Watch-class and instrument shafts."),
                     ("Lot discipline", "First-article then lights-out capable runs.")],
         gallery=["assets/images/products/aluminum.webp", "assets/images/products/machined-parts.webp", "assets/images/services/turning.webp", "assets/images/team/lab.webp", "assets/images/industries/medical.webp", "assets/images/hero/cnc-closeup.webp"],
         spec=[("Diameter", "Ø 1–32 mm typical"), ("Tolerance", "±0.01 mm on diameters"), ("Materials", "SS 303/316, Ti, brass"), ("Machines", "Swiss-type CNC")],
         related=["micro-machining.html", "cnc-turning.html", "cnc-milling.html"]),
    dict(file="micro-machining.html", title="Micro Machining", eyebrow="CNC · Micro",
         desc="Small features, fine tools, and tight finishes for instruments we mill in a controlled bay.",
         img="assets/images/products/machined-parts.webp",
         highlights=[("Fine tools", "Micro end mills and high-rpm spindles."),
                     ("Burr control", "Edges we inspect under magnification."),
                     ("Clean handling", "Lots bagged to drawing, not dumped in bins."),
                     ("Metrology", "Optical and CMM on features you cannot finger-check.")],
         gallery=["assets/images/products/machined-parts.webp", "assets/images/team/metrology.webp", "assets/images/industries/electronics.webp", "assets/images/products/aluminum.webp", "assets/images/team/lab.webp", "assets/images/hero/cnc-closeup.webp"],
         spec=[("Features", "Sub-millimeter pockets and holes"), ("Finish", "Ra targets per drawing"), ("Materials", "SS, Ti, Al, PEEK"), ("Inspection", "CMM + optical")],
         related=["swiss-machining.html", "cnc-milling.html", "vision-inspection.html"]),
    dict(file="sheet-metal-fabrication.html", title="Sheet Metal Fabrication", eyebrow="Sheet · Fabrication",
         desc="Cut, form, weld, and finish sheet assemblies we build as product — not as job-shop leftovers.",
         img="assets/images/services/sheet-metal.webp",
         highlights=[("Full bay", "Laser to brake to weld under one roof."),
                     ("Hardware", "PEM, nutserts, hinges we install."),
                     ("Finish", "Powder and wet we schedule with our painters."),
                     ("Assemblies", "Doors, racks, and covers that leave as units.")],
         gallery=["assets/images/services/sheet-metal.webp", "assets/images/services/press-brake.webp", "assets/images/services/laser.webp", "assets/images/products/components.webp", "assets/images/facility/factory-interior.webp", "assets/images/services/assembly.webp"],
         spec=[("Thickness", "0.5–6 mm typical CRS / SS / Al"), ("Process", "Cut · form · weld · finish"), ("Hardware", "PEM and clinch in-house"), ("QC", "First-article fit on our fixtures")],
         related=["laser-cutting.html", "sheet-cutting.html", "tube-bending.html"]),
    dict(file="sheet-cutting.html", title="Sheet Cutting", eyebrow="Sheet · Cutting",
         desc="Nests we cut on laser and waterjet from stock we hold, then send next door to form.",
         img="assets/images/services/waterjet.webp",
         highlights=[("Nesting", "Yield we own because the plate is ours."),
                     ("Mixed process", "Laser for speed, waterjet for thick or reflective."),
                     ("Etch & mark", "Part IDs burned in for travelers."),
                     ("Deburr", "Edges prepped before they hit the brake.")],
         gallery=["assets/images/services/waterjet.webp", "assets/images/services/laser.webp", "assets/images/services/sheet-metal.webp", "assets/images/hero/sparks.webp", "assets/images/products/components.webp", "assets/images/facility/factory-floor.webp"],
         spec=[("Laser", "Fiber on steel, stainless, aluminum"), ("Waterjet", "Thick plate and stacked nests"), ("Nest software", "In-house CAM"), ("Handoff", "Straight to brake / weld")],
         related=["laser-cutting.html", "waterjet-cutting.html", "sheet-metal-fabrication.html"]),
    dict(file="laser-cutting.html", title="Laser Cutting", eyebrow="Sheet · Laser",
         desc="Fiber laser cutting of sheet we nest, inspect, and pass to forming on the same shift.",
         img="assets/images/services/laser.webp",
         highlights=[("Fiber source", "Speed on CRS and stainless."),
                     ("Fine kerf", "Small holes and tags we design for our brake."),
                     ("Tapping assist", "Pilot holes for hardware we install."),
                     ("Overnight nests", "Lights-on cutting when the queue says so.")],
         gallery=["assets/images/services/laser.webp", "assets/images/hero/sparks.webp", "assets/images/services/sheet-metal.webp", "assets/images/products/assembly-cell.webp", "assets/images/services/press-brake.webp", "assets/images/hero/factory-dark.webp"],
         spec=[("Source", "Fiber laser"), ("Typical range", "0.5–12 mm steel class"), ("Assist gas", "N2 / O2 per spec"), ("Output", "Deburred blanks")],
         related=["laser-tube-cutting.html", "sheet-cutting.html", "waterjet-cutting.html"]),
    dict(file="waterjet-cutting.html", title="Waterjet Cutting", eyebrow="Sheet · Waterjet",
         desc="Abrasive waterjet for thick plate, laminates, and metals we will not heat-affect.",
         img="assets/images/services/waterjet.webp",
         highlights=[("No HAZ", "Edges ready for weld or machine."),
                     ("Stack cutting", "When the nest economics work."),
                     ("Hard alloys", "Tool steels and titanium plate."),
                     ("Taper control", "Quality maps we pick per drawing.")],
         gallery=["assets/images/services/waterjet.webp", "assets/images/services/cnc-machines.webp", "assets/images/products/gears.webp", "assets/images/industries/energy.webp", "assets/images/facility/factory-interior.webp", "assets/images/services/sheet-metal.webp"],
         spec=[("Process", "Abrasive waterjet"), ("Thickness", "Up to heavy plate"), ("Materials", "Metals, composites, stone-class stock"), ("Taper", "Q-value by feature")],
         related=["laser-cutting.html", "sheet-cutting.html", "cnc-milling.html"]),
    dict(file="laser-tube-cutting.html", title="Laser Tube Cutting", eyebrow="Sheet · Tube laser",
         desc="Profiles, miters, and holes in tube we later bend and weld into frames.",
         img="assets/images/services/tube.webp",
         highlights=[("3D path", "Fishmouths and copes for weld-ready joints."),
                     ("Round / square", "Stock we keep for product frames."),
                     ("Tab features", "Self-fixturing joints we designed."),
                     ("Marking", "Bend and weld clocks etched on the stick.")],
         gallery=["assets/images/services/tube.webp", "assets/images/services/laser.webp", "assets/images/industries/machinery.webp", "assets/images/products/assembly-cell.webp", "assets/images/services/robot-weld.webp", "assets/images/facility/factory-floor.webp"],
         spec=[("Sections", "Round, square, rectangle"), ("Ops", "Cut, miter, hole, slot"), ("Next bay", "CNC tube bend + weld"), ("Materials", "CRS, SS, Al tube")],
         related=["tube-bending.html", "laser-cutting.html", "sheet-metal-fabrication.html"]),
    dict(file="tube-bending.html", title="Tube Bending", eyebrow="Sheet · Bending",
         desc="CNC tube bending for frames, handles, and fluid lines we assemble ourselves.",
         img="assets/images/services/press-brake.webp",
         highlights=[("CNC bend", "Repeatable radii on our bender."),
                     ("Springback", "Offsets we learned on our own materials."),
                     ("Weld after", "Bent sticks go to our weld cell."),
                     ("Check fixtures", "Go/no-go we mill in-house.")],
         gallery=["assets/images/services/press-brake.webp", "assets/images/services/tube.webp", "assets/images/industries/automotive.webp", "assets/images/services/sheet-metal.webp", "assets/images/products/components.webp", "assets/images/hero/sparks.webp"],
         spec=[("Process", "CNC rotary draw / brake as required"), ("Tube", "Round and square per cell"), ("QC", "Fixture check"), ("Finish", "Weld, grind, coat")],
         related=["laser-tube-cutting.html", "sheet-metal-fabrication.html", "automation-spm.html"]),
    dict(file="automation-spm.html", title="Assembly Automation", eyebrow="Automation · Assembly",
         desc="Assembly cells we design, tool, and prove on our floor before they ship as Aettram systems.",
         img="assets/images/services/assembly.webp",
         highlights=[("Cell architecture", "Stations we layout around our own cycle-time studies."),
                     ("Tooling", "EOAT and nests we mill and print."),
                     ("PLC / HMI", "Logic we write and keep."),
                     ("FAT", "Buy-off happens in our bay.")],
         gallery=["assets/images/services/assembly.webp", "assets/images/services/robot-metal.webp", "assets/images/products/assembly-cell.webp", "assets/images/services/robot-arm.webp", "assets/images/industries/robotics.webp", "assets/images/facility/factory-interior.webp"],
         spec=[("Scope", "Single station to linked line"), ("Controls", "PLC, HMI, safety"), ("Mechanics", "Frames we fabricate"), ("Prove-out", "FAT at Aettram")],
         related=["robotic-assembly-testing.html", "machine-tending.html", "vision-inspection.html"]),
    dict(file="machine-tending.html", title="Machine Tending", eyebrow="Automation · Tending",
         desc="Robots that load our mills and lathes — cells we run every day, then replicate as product.",
         img="assets/images/services/robot-arm.webp",
         highlights=[("Dual gripper", "Load/unload without starving the spindle."),
                     ("Drawer / conveyor", "Infeed we build to the machine."),
                     ("Probe handshake", "Robot waits on our CNC ready bits."),
                     ("Cage & safety", "Fencing and scanners we integrate.")],
         gallery=["assets/images/services/robot-arm.webp", "assets/images/services/cnc-machines.webp", "assets/images/services/robot-metal.webp", "assets/images/hero/cnc-closeup.webp", "assets/images/team/safety-worker.webp", "assets/images/products/machined-parts.webp"],
         spec=[("Robots", "6-axis tending cells"), ("Machines", "VMC and lathe tend"), ("Payload", "Sized to our chucks"), ("Software", "PLC + robot TP we own")],
         related=["automation-spm.html", "cnc-milling.html", "cnc-turning.html"]),
    dict(file="robotic-assembly-testing.html", title="Robotic Assembly & Testing", eyebrow="Automation · Robotics",
         desc="Robots that assemble and test hardware we also machine — one closed loop on our floor.",
         img="assets/images/services/robot-weld.webp",
         highlights=[("Press & snap", "Force-controlled assembly we tune."),
                     ("End-of-line test", "Electrical and leak tests we specify."),
                     ("Weld assist", "Robot weld on frames we cut."),
                     ("Data", "Cycle logs we keep with the lot.")],
         gallery=["assets/images/services/robot-weld.webp", "assets/images/services/robot-metal.webp", "assets/images/industries/robotics.webp", "assets/images/products/assembly-cell.webp", "assets/images/industries/automotive.webp", "assets/images/services/assembly.webp"],
         spec=[("Tasks", "Assemble, weld, test"), ("Sensing", "Force, vision, IO"), ("Safety", "ISO-style cell fencing"), ("Output", "Serialized results")],
         related=["automation-spm.html", "vision-inspection.html", "machine-tending.html"]),
    dict(file="vision-inspection.html", title="Vision Inspection", eyebrow="Automation · Vision",
         desc="Camera systems we mount on our lines to catch geometry and presence before pack-out.",
         img="assets/images/products/assembly-cell.webp",
         highlights=[("Presence / gauging", "Pixels tied to our CMM datums."),
                     ("Reject handling", "Gates and bins we fabricate."),
                     ("Lighting", "Rigs we design for metal parts."),
                     ("Trace", "Images stored with the traveler.")],
         gallery=["assets/images/products/assembly-cell.webp", "assets/images/industries/electronics.webp", "assets/images/team/metrology.webp", "assets/images/services/assembly.webp", "assets/images/industries/medical.webp", "assets/images/team/lab.webp"],
         spec=[("Cameras", "Area and line scan"), ("Logic", "PLC + vision controller"), ("Use", "Inline and audit stations"), ("Output", "Pass/fail + image archive")],
         related=["robotic-assembly-testing.html", "micro-machining.html", "automation-spm.html"]),
]

INDUSTRIES = [
    dict(file="aerospace.html", title="Aerospace", eyebrow="Sector",
         desc="Structural brackets, tooling, and interiors hardware we mill and inspect to drawing.",
         img="assets/images/industries/aerospace.webp",
         highlights=[("Flight hardware families", "Brackets and fittings in Al and Ti."),
                     ("Tooling", "Drill jigs and form tools we also use in-house."),
                     ("Trace", "Certs and CMM with the crate."),
                     ("Finish", "Anodize and paint we schedule.")],
         gallery=["assets/images/industries/aerospace.webp", "assets/images/products/bracket.webp", "assets/images/products/machined-parts.webp", "assets/images/hero/cnc-closeup.webp", "assets/images/team/metrology.webp", "assets/images/facility/factory-floor.webp"],
         spec=[("Typical parts", "Brackets, housings, tooling"), ("Materials", "Al 7075, Ti-6Al-4V, SS"), ("QC", "CMM vs GD&T"), ("Process", "5-axis mill + finish")],
         related=["automotive.html", "energy.html", "industrial-machinery.html"], kind="ind"),
    dict(file="automotive.html", title="Automotive", eyebrow="Sector",
         desc="Powertrain components, EV enclosures, and fixtures we fabricate and machine.",
         img="assets/images/industries/automotive.webp",
         highlights=[("Powertrain", "Shafts, housings, manifolds."),
                     ("EV pack skins", "Sheet enclosures we laser and form."),
                     ("Line fixtures", "Nests for cells we also build."),
                     ("Volume", "Repeat families on our lathes.")],
         gallery=["assets/images/industries/automotive.webp", "assets/images/products/gears.webp", "assets/images/services/sheet-metal.webp", "assets/images/services/robot-weld.webp", "assets/images/services/turning.webp", "assets/images/hero/sparks.webp"],
         spec=[("Parts", "Powertrain, enclosures, fixtures"), ("Metals", "Steels, Al, coated sheet"), ("Automation", "Tend and weld cells"), ("QC", "First-article + CMM")],
         related=["aerospace.html", "robotics.html", "industrial-machinery.html"], kind="ind"),
    dict(file="medical-devices.html", title="Medical Devices", eyebrow="Sector",
         desc="Instruments, frames, and diagnostic hardware we machine in documented lots.",
         img="assets/images/industries/medical.webp",
         highlights=[("Instruments", "Swiss and micro features."),
                     ("Frames", "Sheet and mill hybrid assemblies."),
                     ("Clean handling", "Bagged lots, labeled travelers."),
                     ("Finish", "Passivate and polish per spec.")],
         gallery=["assets/images/industries/medical.webp", "assets/images/products/aluminum.webp", "assets/images/team/lab.webp", "assets/images/services/turning.webp", "assets/images/team/metrology.webp", "assets/images/products/machined-parts.webp"],
         spec=[("Parts", "Instruments, housings, carts"), ("Materials", "SS 316, Ti, PEEK"), ("Process", "Swiss, micro mill, fab"), ("QC", "Optical + CMM")],
         related=["electronics.html", "robotics.html", "aerospace.html"], kind="ind"),
    dict(file="industrial-machinery.html", title="Industrial Machinery", eyebrow="Sector",
         desc="Gears, shafts, guards, and hydraulic manifolds we ship as assemblies.",
         img="assets/images/industries/machinery.webp",
         highlights=[("Power transmission", "Gears and shafts we turn and grind-prep."),
                     ("Hydraulics", "Manifolds milled from billet."),
                     ("Guarding", "Sheet we laser and weld."),
                     ("Spares", "Families we keep CAM for.")],
         gallery=["assets/images/industries/machinery.webp", "assets/images/products/gears.webp", "assets/images/services/cnc-machines.webp", "assets/images/services/press-brake.webp", "assets/images/facility/factory-interior.webp", "assets/images/products/components.webp"],
         spec=[("Parts", "Gears, shafts, manifolds, guards"), ("Materials", "Alloy steels, CI, Al"), ("Process", "Mill, turn, fab"), ("QC", "CMM + hardness as specified")],
         related=["energy.html", "automotive.html", "robotics.html"], kind="ind"),
    dict(file="electronics.html", title="Electronics", eyebrow="Sector",
         desc="Chassis, cold plates, and semiconductor tooling plates we mill and fabricate.",
         img="assets/images/industries/electronics.webp",
         highlights=[("Chassis", "EMI-minded sheet we form."),
                     ("Thermal", "Al plates we mill and tap."),
                     ("Tooling plates", "Flatness we inspect."),
                     ("Hardware", "PEM maps we install.")],
         gallery=["assets/images/industries/electronics.webp", "assets/images/industries/electronics-2.webp", "assets/images/services/sheet-metal.webp", "assets/images/products/aluminum.webp", "assets/images/products/assembly-cell.webp", "assets/images/hero/cnc-closeup.webp"],
         spec=[("Parts", "Chassis, plates, shields"), ("Materials", "Al, CRS, copper class"), ("Process", "Mill + laser + PEM"), ("QC", "Flatness and tap gauge")],
         related=["medical-devices.html", "energy.html", "robotics.html"], kind="ind"),
    dict(file="energy.html", title="Energy", eyebrow="Sector",
         desc="Plate work, manifolds, and enclosure hardware for generation and distribution equipment we build.",
         img="assets/images/industries/energy.webp",
         highlights=[("Heavy plate", "Waterjet and mill on thick stock."),
                     ("Skids", "Frames we tube-cut and weld."),
                     ("Corrosion", "SS and coated CRS we specify."),
                     ("Field fit", "Interfaces we check on fixture.")],
         gallery=["assets/images/industries/energy.webp", "assets/images/industries/energy-plant.webp", "assets/images/services/waterjet.webp", "assets/images/services/tube.webp", "assets/images/facility/factory-floor.webp", "assets/images/hero/factory-dark.webp"],
         spec=[("Parts", "Manifolds, skids, enclosures"), ("Materials", "CS, SS, Al"), ("Process", "Waterjet, mill, weld"), ("QC", "Pressure-face finish + CMM")],
         related=["industrial-machinery.html", "aerospace.html", "electronics.html"], kind="ind"),
    dict(file="robotics.html", title="Robotics", eyebrow="Sector",
         desc="Bases, EOAT, and test cells we design around robots that also run our own plant.",
         img="assets/images/industries/robotics.webp",
         highlights=[("EOAT", "Grippers we mill and print."),
                     ("Pedestals", "Weldments from our fab bay."),
                     ("Test cells", "Vision and force we integrate."),
                     ("Dogfooding", "Same robots tend our CNCs.")],
         gallery=["assets/images/industries/robotics.webp", "assets/images/services/robot-arm.webp", "assets/images/services/robot-metal.webp", "assets/images/services/robot-weld.webp", "assets/images/products/assembly-cell.webp", "assets/images/services/assembly.webp"],
         spec=[("Parts", "EOAT, bases, cells"), ("Process", "Mill, fab, robot integrate"), ("Controls", "PLC + TP"), ("Prove-out", "FAT on our floor")],
         related=["automotive.html", "industrial-machinery.html", "medical-devices.html"], kind="ind"),
]


def detail_page(item, folder):
    d = 1
    a = pfx(d)
    kind = item.get("kind", "svc")
    title = item["title"]
    path = f"{folder}/{item['file']}"
    meta = f"{title} at Aettram — in-house manufacturing capability and representative work."
    html = head(d, f"{title} — Aettram", meta, path)
    html += nav(d, "services" if folder == "services" else "industries")
    highs = "".join(f'<div class="pillar"><h3>{h[0]}</h3><p>{h[1]}</p></div>' for h in item["highlights"])
    gals = "".join(
        f'<a class="work-item glightbox" href="{a}{src}" data-gallery="{item["file"]}"><div class="card-media frame"><img src="{a}{src}" alt="{title} gallery" loading="lazy"></div></a>'
        for src in item["gallery"]
    )
    specs = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in item["spec"])
    rels = ""
    for rf in item["related"]:
        label = rf.replace(".html", "").replace("-", " ").title()
        rels += f'<a class="card" href="{rf}"><div class="card-body"><h3>{label}</h3><span class="link-arrow">Open →</span></div></a>'
    html += f"""
<main id="main">
{page_hero(title + ".", item["eyebrow"], item["desc"], item["img"], d)}
<section class="section section--light">
  <div class="container">
    <p class="eyebrow">Highlights</p>
    <div class="grid-3">{highs}</div>
  </div>
</section>
<section class="section section--graphite">
  <div class="container">
    <p class="eyebrow">Work</p>
    <h2>From this bay</h2>
    <div class="masonry" style="margin-top:24px">{gals}</div>
  </div>
</section>
<section class="section section--light">
  <div class="container grid-2">
    <div>
      <p class="eyebrow">Specification</p>
      <h2>What we run</h2>
      <table class="spec">{specs}</table>
    </div>
    <div>
      <p class="eyebrow">Related</p>
      <h2>Also on the floor</h2>
      <div class="related" style="grid-template-columns:1fr">{rels}</div>
    </div>
  </div>
</section>
"""
    html += close_main(d)
    write(path, html)


def sitemap():
    urls = [
        "index.html", "about.html", "manufacturing.html",
        "services.html", "industries.html", "contact.html",
    ]
    urls += [f"services/{s['file']}" for s in SERVICES]
    urls += [f"industries/{i['file']}" for i in INDUSTRIES]
    body = "".join(
        f"  <url><loc>{SITE}/{u if u != 'index.html' else ''}</loc><changefreq>monthly</changefreq></url>\n"
        for u in urls
    )
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}</urlset>
"""
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("wrote sitemap + robots")


def credits():
    (ROOT / "credits.txt").write_text(
        """Image & video credits (free commercial use)
Unsplash (unsplash.com/license):
- photo-1565043666747-69f6646db940 CNC close-up
- photo-1504917595217-d4dc5ebe6122 Factory dark
- photo-1504328345606-18bbc8c9d7d1 Sparks / metalwork
- photo-1537462715879-360eeb61a0ad Factory interior
- photo-1581094794329-c8112a89af12 Factory floor
- photo-1581091226825-a6a2a5aee158 CAD / engineer
- photo-1581092918056-0c4c3acd3789 Safety gear
- photo-1581092160562-40aa08e78837 Metrology / plant
- photo-1485827404703-89b55fcc595e Robot arm
- photo-1610557892470-55d9e80c0bce Machined parts
- photo-1558618666-fcd25c85cd64 Sheet metal / pipes
- photo-1518770660439-4636190af475 Electronics
- photo-1486262715619-67b85e0b08d3 Automotive
- photo-1576091160399-112ba8d25d1d Medical
- photo-1473341304170-971dccb5ac1e Energy
- photo-1513828583688-c52646db42da Energy plant
- photo-1550751827-4bd374c3f58b Electronics 2
- photo-1752614671119-4868a91efc14 Robot on metal
- photo-1752614671144-7eee784abf74 Robot weld
- photo-1581092160607-ee22621dd758 Aluminum parts
- photo-1581092795360-fd1ca04f0952 Assembly
Pexels:
- 159298 gears, 46148 aircraft, 1108101 CNC, 162553 workshop
- 257736 laser/industrial, 2760241 components, 3862379 waterjet
- 3862130 press, 2599244 robotics, 3846508 machinery
- 2280571 lab, 1267338 assembly, 236705 tube, 3861969 bracket
Video: existing Aettram hero clip Metal_bar_cut_by_laser (assets/video/hero-laser.mp4)
""",
        encoding="utf-8",
    )


def favicon_svg():
    (ROOT / "favicon.svg").write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" fill="#0F0F10"/>
<rect x="6" y="6" width="52" height="52" fill="none" stroke="#C1440E" stroke-width="2"/>
<path d="M8 8h10M8 8v10M56 8h-10M56 8v10M8 56h10M8 56v-10M56 56h-10M56 56v-10" stroke="#C1440E" stroke-width="2" fill="none"/>
<text x="32" y="42" text-anchor="middle" font-family="Arial Black, sans-serif" font-size="28" fill="#C1440E">A</text>
</svg>""",
        encoding="utf-8",
    )


def redirects():
    (ROOT / "_redirects").write_text("/*    /404.html   404\n", encoding="utf-8")


if __name__ == "__main__":
    index()
    about()
    manufacturing()
    services_hub()
    industries_hub()
    contact()
    error404()
    for s in SERVICES:
        detail_page(s, "services")
    for i in INDUSTRIES:
        detail_page(i, "industries")
    sitemap()
    credits()
    favicon_svg()
    redirects()
    print("done")
