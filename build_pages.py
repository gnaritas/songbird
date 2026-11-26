#!/usr/bin/env python3
"""Songbird (Raleigh NC) — template v2 build (t_fbffb777, 2026-11-26).
9 pages: index · programs · 2 detail (morning / cocktails+dinner) · visit ·
contact · privacy + thanks/404. Custom hand-rolled HTML/CSS, day-to-dusk
identity (morning cream bands turning to dusk plum/night), zero third-party
JS, one local stylesheet. Facts only from the card's verified sources:
News & Observer opening coverage, owner's Substack launch post (Meg Paradise),
visitraleigh listing, GBP/press facts. No phone/email published -> contact
form + Resy only. No prices -> no priceRange claims."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "public")
ORIGIN = "https://songbird-demo.up.railway.app"
ADDR = "1020 E Whitaker Mill Rd, Ste 130"
CITY = "Raleigh, NC 27608"
NAP = ADDR + ", " + CITY
IG_URL = "https://www.instagram.com/songbird.nc/"
RESY_URL = "https://resy.com/cities/raleigh-nc/venues/songbird-nc"
MAP_EMBED = ("https://www.google.com/maps?q=1020+E+Whitaker+Mill+Rd,+Ste+130,"
             "+Raleigh,+NC+27608&amp;output=embed")
MAP_LINK = ("https://www.google.com/maps/search/?api=1&query="
            "1020+E+Whitaker+Mill+Rd,+Ste+130,+Raleigh,+NC+27608")
BUILT = "BUILT-2026-11-26 t_fbffb777"

CSS = """
:root{--paper:#faf3e6;--paper2:#fffdf8;--ink:#241f31;--mut:#5d5568;--sun:#dfa04e;--coral:#c25a3b;--sage:#6e8c5a;--dusk:#2b2240;--dusk2:#3a2e52;--night:#1b1628;--cream:#faf3e6;--line:#e6d7bd;--lineD:rgba(250,243,230,.16);--display:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;--body:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:var(--body);background:var(--paper);color:var(--ink);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--coral)}a:hover{color:var(--sun)}:focus-visible{outline:3px solid var(--sun);outline-offset:2px;border-radius:6px}
.skip{position:absolute;left:-6000px}.skip:focus{left:12px;top:12px;z-index:30;background:var(--ink);color:var(--cream);padding:8px 14px;border-radius:8px}
h1,h2,h3{font-family:var(--display);font-weight:700;line-height:1.12;letter-spacing:-.01em;margin:0}
.kicker{font-family:var(--mono);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--coral);margin:0 0 14px}
.band-evening .kicker,.footline .kicker{color:var(--sun)}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
header.site{position:sticky;top:0;z-index:20;background:rgba(27,22,40,.97);backdrop-filter:blur(8px);border-bottom:1px solid var(--lineD)}
.navrow{display:flex;align-items:center;gap:18px;padding:12px 22px;max-width:1120px;margin:0 auto;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;color:var(--cream);text-decoration:none;font-family:var(--display);font-size:23px;font-weight:700}
.brand svg{width:34px;height:34px;display:block}
.brand small{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.16em;color:rgba(250,243,230,.6);text-transform:uppercase;line-height:1.2;margin-top:2px}
.nav{display:flex;gap:4px;align-items:center;flex-wrap:wrap;margin-left:auto}
.nav a{color:rgba(250,243,230,.82);text-decoration:none;font-size:14.5px;padding:8px 11px;border-radius:999px}
.nav a:hover{background:rgba(250,243,230,.1);color:var(--cream)}
.nav a.on{background:rgba(223,160,78,.18);color:var(--sun)}
.nav a.btn{background:var(--coral);color:#fffdf6;font-weight:600;margin-left:8px;padding:9px 16px}
.nav a.btn:hover{background:#d16a4a;color:#fffdf6}
.btn{display:inline-block;border-radius:999px;text-decoration:none;font-weight:650;font-size:15.5px;padding:13px 24px;transition:background .15s}
.btn.p{background:var(--coral);color:#fffdf6}.btn.p:hover{background:#d16a4a;color:#fffdf6}
.btn.g{border:1.5px solid rgba(36,31,49,.32);color:var(--ink)}.btn.g:hover{border-color:var(--ink)}
.btn.gl{border:1.5px solid var(--lineD);color:var(--cream)}.btn.gl:hover{border-color:var(--cream);color:var(--cream)}
.btn.sm{font-size:14px;padding:9px 17px}
.chip{display:inline-flex;align-items:center;gap:7px;font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;background:var(--paper2);border:1px solid var(--line);border-radius:999px;padding:7px 13px;color:var(--mut)}
.chip i{width:8px;height:8px;border-radius:50%;background:var(--sun);display:inline-block}
.chip.d{background:rgba(250,243,230,.08);border-color:var(--lineD);color:rgba(250,243,230,.75)}
.hero{position:relative;background:radial-gradient(1000px 520px at -10% -20%,#f7dfb8 0%,rgba(247,223,184,0) 60%),radial-gradient(700px 420px at 110% 130%,#c98a63 0%,rgba(201,138,99,0) 55%),var(--paper);padding:66px 0 54px;border-bottom:1px solid var(--line)}
.hero-grid{display:grid;grid-template-columns:1.08fr 1fr;gap:46px;align-items:center}
.hero h1{font-size:clamp(42px,5.9vw,66px)}
.hero h1 em{display:block;font-style:normal;color:var(--coral)}
.lead{font-size:19px;color:var(--mut);max-width:35ch;margin:18px 0 22px}
.cta-row{display:flex;gap:12px;flex-wrap:wrap;margin-top:8px}
.hero-art svg{width:100%;height:auto;display:block;border-radius:22px;box-shadow:0 22px 48px rgba(36,31,49,.18)}
section.block{padding:62px 0}
.band-evening{background:linear-gradient(180deg,var(--dusk) 0%,var(--dusk2) 100%);color:var(--cream)}
.band-evening h2,.band-evening h3{color:var(--cream)}
.band-evening .mut{color:rgba(250,243,230,.72)}
.band-morning{background:var(--paper)}
.sec-head{max-width:640px;margin:0 0 32px}
.sec-head h2{font-size:clamp(29px,3.9vw,41px)}
.sec-head p{color:var(--mut);margin:14px 0 0;font-size:17.5px}
.band-evening .sec-head p{color:rgba(250,243,230,.72)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(225px,1fr));gap:16px}
.card{background:var(--paper2);border:1px solid var(--line);border-radius:16px;padding:22px}
.band-evening .card{background:rgba(250,243,230,.06);border-color:var(--lineD)}
.card .ic{width:34px;height:34px;margin-bottom:13px;color:var(--coral)}
.band-evening .card .ic{color:var(--sun)}
.card .ic svg{width:34px;height:34px;display:block}
.card h3{font-size:21px;margin-bottom:8px}
.card p{margin:0;color:var(--mut);font-size:15.5px;line-height:1.55}
.band-evening .card p{color:rgba(250,243,230,.72)}
.bandnote{margin-top:26px;display:flex;gap:16px;align-items:center;flex-wrap:wrap;color:var(--mut);font-size:15.5px}
.bandnote strong{color:inherit}
.band-evening .bandnote{color:rgba(250,243,230,.84)}
.band-evening .bandnote strong{color:var(--cream)}
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:44px;align-items:center}
.infocard{background:var(--paper2);border:1px solid var(--line);border-radius:18px;padding:26px}
.band-evening .infocard{background:rgba(250,243,230,.06);border-color:var(--lineD)}
.hours{width:100%;border-collapse:collapse;font-size:16px;margin:6px 0 14px}
.hours th,.hours td{text-align:left;padding:10px 4px;border-bottom:1px solid var(--line)}
.band-evening .hours th,.band-evening .hours td{border-color:var(--lineD)}
.hours th{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);font-weight:600}
.band-evening .hours th{color:rgba(250,243,230,.62)}
.hours td:last-child,.hours th:last-child{text-align:right;font-family:var(--mono);font-size:14.5px}
.mapframe{border-radius:16px;overflow:hidden;border:1px solid var(--line);margin-top:16px}
.mapframe iframe{width:100%;height:340px;border:0;display:block}
.addrline{font-style:normal}
.pagehead{background:radial-gradient(900px 380px at 115% -30%,rgba(223,160,78,.28) 0%,rgba(223,160,78,0) 60%),var(--paper);padding:54px 0 30px;border-bottom:1px solid var(--line)}
.pagehead h1{font-size:clamp(34px,4.8vw,52px);max-width:24ch}
.pagehead .lead{max-width:58ch}
.detail{display:grid;grid-template-columns:1fr 340px;gap:44px;padding:48px 0 62px;align-items:start}
.detail h3{font-size:22px;margin:30px 0 8px}.detail h3:first-child{margin-top:0}
.detail p{margin:0 0 14px;color:var(--mut);max-width:62ch}
.aside{position:sticky;top:86px;display:grid;gap:14px}
.aside .infocard{padding:22px}
.aside h3{font-size:17px;font-family:var(--body);letter-spacing:.02em;margin:0 0 8px}
.aside p{margin:0;font-size:14.5px;color:var(--mut)}
.aside .row{display:flex;gap:10px;flex-wrap:wrap}
.linklist{list-style:none;margin:14px 0 0;padding:0}
.linklist li{padding:9px 0;border-bottom:1px solid var(--line);font-size:15px}
.linklist li:last-child{border-bottom:0}
details.faq{border-bottom:1px solid var(--line);padding:14px 0}
details.faq summary{font-weight:650;cursor:pointer;list-style:none;display:flex;gap:10px;align-items:baseline}
details.faq summary::before{content:"+";font-family:var(--mono);color:var(--coral);font-size:19px}
details.faq[open] summary::before{content:"–"}
details.faq p{margin:10px 0 2px;color:var(--mut);font-size:15.5px;max-width:64ch}
.cform{display:grid;gap:14px;margin-top:8px}
.cform label{font-weight:650;font-size:14.5px;display:grid;gap:6px}
.cform input,.cform textarea{font:inherit;font-size:15.5px;padding:12px 14px;border:1.5px solid var(--line);border-radius:11px;background:var(--paper2);color:var(--ink);width:100%}
.cform textarea{min-height:140px;resize:vertical}
.cform button{margin-top:4px;justify-self:start}
.hintline{font-size:13.5px;color:var(--mut)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid-2x2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}
.tile{display:flex;flex-direction:column;background:var(--paper2);border:1px solid var(--line);border-radius:18px;padding:26px;text-decoration:none;color:inherit;transition:transform .12s,border-color .12s}
.tile:hover{border-color:var(--coral);transform:translateY(-2px);color:inherit}
.tile h3{font-size:24px;margin-bottom:8px}.tile p{color:var(--mut);margin:0;font-size:15.5px}
.tile .go{display:inline-block;margin-top:auto;padding-top:16px;font-weight:650;color:var(--coral);font-size:14.5px}
.footline{background:var(--night);color:rgba(250,243,230,.78);padding:52px 0 0}
.footline a{color:rgba(250,243,230,.78);text-decoration:none}.footline a:hover{color:var(--sun)}
.footgrid{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:34px;padding-bottom:40px}
.footgrid h3{font-family:var(--body);font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:rgba(250,243,230,.55);margin:0 0 14px;font-weight:650}
.footgrid ul{list-style:none;margin:0;padding:0}
.footgrid li{padding:5px 0;font-size:14.5px}
.footgrid .bname{font-family:var(--display);font-size:24px;color:var(--cream);margin-bottom:12px}
.footgrid address{font-style:normal;font-size:14.5px;line-height:1.7}
.footbar{border-top:1px solid var(--lineD);padding:18px 0 22px;display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;font-family:var(--mono);font-size:12px;letter-spacing:.08em;color:rgba(250,243,230,.5)}
.seasonstrip{background:linear-gradient(90deg,#f4dfbc 0%,#eab87a 34%,#b06a4d 68%,#3f3158 100%);padding:5px 0}
@media (max-width:900px){.hero-grid,.split,.detail{grid-template-columns:1fr}.hero{padding:44px 0 40px}.hero-art{margin-top:8px}.detail{gap:26px}.aside{position:static}.footgrid{grid-template-columns:1fr 1fr}}
@media (max-width:600px){body{font-size:16px}.footgrid{grid-template-columns:1fr}.navrow{padding:10px 16px}.nav{margin-left:0}.brand{font-size:20px}section.block{padding:48px 0}.mapframe iframe{height:280px}}
"""

def head(title, desc, path, no_og=False):
    url = ORIGIN + path
    meta = [
        '<!DOCTYPE html><html lang="en"><head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>' + title + '</title>',
        '<meta name="description" content="' + desc + '">',
        '<meta name="robots" content="noindex, nofollow">',
        '<link rel="canonical" href="' + url + '">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="stylesheet" href="/style.css">',
    ]
    if not no_og:
        meta += [
            '<meta property="og:type" content="website">',
            '<meta property="og:site_name" content="Songbird">',
            '<meta property="og:title" content="' + title + '">',
            '<meta property="og:description" content="' + desc + '">',
            '<meta property="og:image" content="' + ORIGIN + '/og.png">',
            '<meta property="og:url" content="' + url + '">',
            '<meta name="twitter:card" content="summary_large_image">',
            '<meta name="twitter:title" content="' + title + '">',
            '<meta name="twitter:description" content="' + desc + '">',
        ]
    meta.append('<!-- ' + BUILT + ' -->')
    return "\n".join(meta) + "</head><body>" + \
        '<a class="skip" href="#main">Skip to content</a>'

MARK = ('<svg viewBox="0 0 40 40" aria-hidden="true">'
        '<circle cx="20" cy="20" r="19" fill="#1b1628" stroke="rgba(250,243,230,.28)" stroke-width="1.5"/>'
        '<circle cx="25.5" cy="15" r="6.2" fill="#dfa04e"/>'
        '<path d="M8 29.5a13 13 0 0 1 13-13 10 10 0 0 1 6 2 11 11 0 0 0-19 11z" fill="#faf3e6" opacity=".92"/>'
        '<path d="M27 24.5a5.5 5.5 0 0 1 0 8" stroke="#c25a3b" stroke-width="2" fill="none" stroke-linecap="round"/>'
        '<circle cx="14.5" cy="17.5" r="2.4" fill="#1b1628"/>'
        '<path d="M6 20.5a5.5 5.5 0 0 1 0 8" stroke="#dfa04e" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".75"/>'
        '</svg>')

def header(active):
    items = [("/programs", "Programs"), ("/morning-program-raleigh", "Mornings"),
             ("/cocktails-dinner-raleigh", "Evenings"), ("/visit", "Visit")]
    links = []
    for href, label in items:
        on = ' class="on" aria-current="page"' if href == active else ""
        links.append('<a href="' + href + '"' + on + ">" + label + "</a>")
    links.append('<a href="/contact" class="btn"' +
                 (' aria-current="page"' if active == "/contact" else "") + ">Contact</a>")
    return ('<header class="site"><div class="navrow">'
            '<a class="brand" href="' + ORIGIN + '/" aria-label="Songbird home">' + MARK +
            '<span>Songbird<small>Daylight to dusk · East End Market</small></span></a>'
            '<nav class="nav" aria-label="Main">' + "\n".join(links) + "</nav></div></header>")

FOOTER = ('<footer class="footline"><div class="wrap"><div class="footgrid">'
          '<div><p class="bname">Songbird</p><address>' + ADDR + '<br>Inside East End Market<br>' + CITY +
          '</address><p style="margin:14px 0 0;font-size:14.5px">Mornings 8 AM–2 PM, every day<br>'
          'Evenings: Sun–Wed 4–10 · Thu–Sat 4 till midnight</p></div>'
          '<div><h3>Pages</h3><ul>'
          '<li><a href="/programs">Programs</a></li>'
          '<li><a href="/morning-program-raleigh">Morning program</a></li>'
          '<li><a href="/cocktails-dinner-raleigh">Cocktails and dinner</a></li>'
          '<li><a href="/visit">Hours and directions</a></li>'
          '<li><a href="/contact">Contact</a></li>'
          '<li><a href="/privacy">Privacy</a></li></ul></div>'
          '<div><h3>Find us</h3><ul>'
          '<li><a href="' + IG_URL + '">Instagram</a></li>'
          '<li><a href="' + RESY_URL + '">Book an evening table on Resy</a></li>'
          '<li><a href="' + MAP_LINK + '">Get directions</a></li></ul></div></div>'
          '<div class="footbar"><span>© 2026 Songbird · East End Market</span><span>Raleigh, North Carolina</span></div></div></footer>')

def ld(blocks):
    out = []
    for b in blocks:
        out.append('<script type="application/ld+json">' +
                   json.dumps(b, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    return "\n".join(out)

GEO = {"@type": "GeoCoordinates", "latitude": 35.8075042, "longitude": -78.6235994}
ADDRESS = {"@type": "PostalAddress", "streetAddress": ADDR, "addressLocality": "Raleigh",
           "addressRegion": "NC", "postalCode": "27608", "addressCountry": "US"}

ENTITY = {
    "@context": "https://schema.org",
    "@type": ["BarOrPub", "CafeOrCoffeeShop"],
    "name": "Songbird",
    "url": ORIGIN + "/",
    "image": ORIGIN + "/og.png",
    "description": ("Daylight-to-dusk bar inside East End Market in Raleigh, North Carolina — "
                    "coffee, juice, tea, and morning plates 8 AM to 2 PM daily; seasonal "
                    "cocktails, natural wine, and dinner from 4 PM."),
    "address": ADDRESS,
    "geo": GEO,
    "hasMap": MAP_LINK,
    "foundingDate": "2026-06",
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
         "opens": "08:00", "closes": "14:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday"],
         "opens": "16:00", "closes": "22:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Thursday", "Friday", "Saturday"],
         "opens": "16:00", "closes": "23:59"},
    ],
    "sameAs": [IG_URL, RESY_URL],
}

def crumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + p}
                for i, (n, p) in enumerate(items)]}

def service(name, desc, url):
    return {"@context": "https://schema.org", "@type": "Service", "name": name,
            "description": desc, "url": url,
            "areaServed": {"@type": "City", "name": "Raleigh",
                           "containedInPlace": {"@type": "State", "name": "North Carolina"}},
            "provider": {"@type": ["BarOrPub", "CafeOrCoffeeShop"], "name": "Songbird",
                         "address": ADDRESS, "url": ORIGIN + "/"}}

ICON = {
    "cup": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h12v6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V9z"/><path d="M16 10h2a2.5 2.5 0 0 1 0 5h-2"/><path d="M7 3.5c.8.9.8 1.6 0 2.5M11 3.5c.8.9.8 1.6 0 2.5"/></svg>',
    "juice": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 2.5h6M10 2.5v3.5l-2.2 3A2 2 0 0 0 7.4 10v8.5a3 3 0 0 0 3 3h3.2a3 3 0 0 0 3-3V10a2 2 0 0 0-.4-1.1L14 6V2.5"/><path d="M8 13h8"/><path d="M16.5 4.5c3 1 3 4.5 1 6"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 4c-9 0-15 5-15 13 0 1.2.2 2.4.7 3.5C16 19 20.5 13 20 4z"/><path d="M5.7 20.5C8 15 12.5 10.5 17 8"/></svg>',
    "bread": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 17c1-6 5-10 9-10s8 4 9 10"/><path d="M3 17c2.5 2 5.5 3 9 3s6.5-1 9-3"/><path d="M8.5 12.5c1 1 2.2 1.6 3.5 1.6s2.5-.6 3.5-1.6"/></svg>',
    "coupe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4.5h16l-7 8v6.5"/><path d="M9.5 19h7"/><path d="M6.2 8.5h11.6"/></svg>',
    "wine": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 2.5h10c0 6.5-2.2 10-5 10s-5-3.5-5-10z"/><path d="M12 12.5v7"/><path d="M8 19.5h8"/></svg>',
    "plate": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/></svg>',
    "cloche": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 16a8.5 8.5 0 0 1 17 0"/><path d="M2 16h20"/><path d="M12 7.5V5"/><circle cx="12" cy="3.8" r="1.2"/></svg>',
}

def card(ic, title, body, dark=False):
    return ('<div class="card"><div class="ic">' + ICON[ic] + "</div><h3>" + title +
            "</h3><p>" + body + "</p></div>")

HERO_ART = (
    '<svg viewBox="0 0 560 430" role="img" aria-label="Sun, songbird, and moon across a day-to-dusk sky" preserveAspectRatio="xMidYMid meet">'
    '<defs><linearGradient id="sky" x1="0" y1="0" x2="1" y2="0">'
    '<stop offset="0" stop-color="#fbf1de"/><stop offset=".36" stop-color="#f2c48b"/>'
    '<stop offset=".64" stop-color="#b06a4d"/><stop offset=".86" stop-color="#5c4066"/>'
    '<stop offset="1" stop-color="#2b2240"/></linearGradient></defs>'
    '<rect x="8" y="8" width="544" height="366" rx="24" fill="url(#sky)" stroke="rgba(36,31,49,.18)" stroke-width="2"/>'
    '<circle cx="100" cy="118" r="44" fill="#dfa04e"/>'
    '<circle cx="100" cy="118" r="58" fill="none" stroke="#dfa04e" stroke-width="2" opacity=".4"/>'
    '<path d="M150 118 Q 280 16 424 92" fill="none" stroke="#c25a3b" stroke-width="3" stroke-dasharray="7 11" stroke-linecap="round" opacity=".75"/>'
    '<path d="M447 66 A 30 30 0 1 0 447 126 A 24 24 0 0 1 447 66 Z" fill="#fbf3e2"/>'
    '<circle cx="398" cy="58" r="2.6" fill="#fbf3e2" opacity=".9"/>'
    '<circle cx="420" cy="152" r="2.2" fill="#fbf3e2" opacity=".8"/>'
    '<circle cx="470" cy="118" r="3" fill="#fbf3e2" opacity=".9"/>'
    '<circle cx="492" cy="66" r="2.4" fill="#fbf3e2" opacity=".8"/>'
    '<circle cx="378" cy="104" r="2" fill="#fbf3e2" opacity=".7"/>'
    '<line x1="34" y1="298" x2="526" y2="298" stroke="#241f31" stroke-width="3" opacity=".42"/>'
    '<line x1="118" y1="312" x2="332" y2="312" stroke="#241f31" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
    '<path d="M150 312 q 12 -16 30 -13 q -9 18 -30 13" fill="#6e8c5a"/>'
    '<path d="M296 312 q 12 -16 30 -13 q -9 18 -30 13" fill="#6e8c5a" opacity=".8"/>'
    '<polygon points="210,300 150,272 192,312" fill="#241f31"/>'
    '<ellipse cx="236" cy="292" rx="33" ry="25" fill="#241f31"/>'
    '<circle cx="264" cy="268" r="16" fill="#241f31"/>'
    '<polygon points="279,261 300,255 280,269" fill="#dfa04e"/>'
    '<circle cx="268" cy="264" r="2.4" fill="#fbf3e2"/>'
    '<ellipse cx="228" cy="288" rx="17" ry="10" fill="#dfa04e" opacity=".9" transform="rotate(-14 228 288)"/>'
    '<path d="M306 240 A 18 18 0 0 1 306 270" fill="none" stroke="#c25a3b" stroke-width="3.5" stroke-linecap="round" opacity=".9"/>'
    '<path d="M316 232 A 30 30 0 0 1 316 278" fill="none" stroke="#c25a3b" stroke-width="3" stroke-linecap="round" opacity=".75"/>'
    '<path d="M326 224 A 42 42 0 0 1 326 286" fill="none" stroke="#c25a3b" stroke-width="2.5" stroke-linecap="round" opacity=".55"/>'
    '<text x="34" y="352" font-family="Menlo,monospace" font-size="12.5" letter-spacing="2" fill="#241f31" opacity=".62">8 AM ————————————————— 2 PM ———————— 4 PM ————————————————— LATE</text>'
    '</svg>')

MAP_IFRAME = ('<div class="mapframe"><iframe '
              'src="' + MAP_EMBED + '" '
              'title="Map to Songbird at 1020 East Whitaker Mill Road, Raleigh" '
              'referrerpolicy="no-referrer-when-downgrade"></iframe></div>')

HOURS_TABLE = ('<table class="hours"><thead><tr><th>Program</th><th>Days</th><th>Time</th></tr></thead><tbody>'
               '<tr><td>Mornings — coffee, juice, tea, morning plates</td><td>Every day</td><td>8 AM–2 PM</td></tr>'
               '<tr><td>Evenings — cocktails, wine, dinner</td><td>Sun–Wed</td><td>4–10 PM</td></tr>'
               '<tr><td>Evenings — cocktails, wine, dinner</td><td>Thu–Sat</td><td>4 PM–midnight</td></tr>'
               '</tbody></table>')

# ---------------------------------------------------------------- index
def page_index():
    h1 = "Daylight to dusk."
    l1 = "<em>Coffee to cocktails.</em>"
    parts = [head("Songbird — Daylight-to-Dusk Bar at East End Market, Raleigh NC",
                  ("Daylight-to-dusk bar inside East End Market, 1020 E Whitaker Mill Rd, Raleigh NC. "
                   "Mornings 8 AM–2 PM daily with coffee, juice, tea, and morning plates. Seasonal "
                   "cocktails, natural wine, and dinner from 4 PM."), "/"),
             header("/home")]
    body = ['<main id="main">',
            '<section class="hero"><div class="wrap"><div class="hero-grid">',
            '<div class="hero-copy">',
            '<p class="kicker">East End Market · Raleigh, North Carolina · opened June 2026</p>',
            '<h1>' + h1 + l1 + '</h1>',
            '<p class="lead">Songbird is a bar that keeps two clocks. Mornings are bright: coffee '
            'roasted a few blocks away, pressed juice, tea, matcha, and something from the oven. '
            'After 4, the same room turns into a full bar — seasonal cocktails, natural wine, and '
            'dinner till late.</p>',
            '<p style="display:flex;gap:9px;flex-wrap:wrap;margin:0 0 22px">'
            '<span class="chip"><i></i>Mornings 8–2 daily</span>'
            '<span class="chip"><i></i>Evenings from 4</span>'
            '<span class="chip"><i></i>Thu–Sat till midnight</span></p>',
            '<div class="cta-row"><a class="btn p" href="' + RESY_URL + '">Book an evening table</a>'
            '<a class="btn g" href="/programs">See the programs</a></div></div>',
            '<div class="hero-art">' + HERO_ART + '</div></div></div></section>',
            '<div class="seasonstrip" aria-hidden="true"></div>',
            '<section class="block band-morning"><div class="wrap">',
            '<div class="sec-head"><p class="kicker">The morning program</p>'
            '<h2>Bright, seven days a week</h2>'
            '<p>8 AM to 2 PM, every day. Walk in, or grab it at the walk-up window on your way past.</p></div>',
            '<div class="cards">',
            card("cup", "Coffee", "Espresso and brewed coffee, roasted a few blocks away by Willow House Coffee."),
            card("juice", "Juice and smoothies", "Cold-pressed juice and seasonal smoothies, blended from Piedmont fruit as it turns."),
            card("leaf", "Tea and matcha", "Custom tea blends from Tin Roof Teas, plus matcha drinks from Frame."),
            card("bread", "From the oven", "Pastries and morning plates from makers around the neighborhood."),
            '</div><p class="bandnote"><a class="btn g sm" href="/morning-program-raleigh">See the full morning program</a></p>',
            '</div></section>',
            '<section class="block band-evening"><div class="wrap">',
            '<div class="sec-head"><p class="kicker">The evening program</p>'
            '<h2>The same room, after four</h2>'
            '<p>From 4 o’clock Songbird turns into a full bar: cocktails built on the season, a '
            'natural-leaning wine list, and dinner — just over 40 seats, plus a patio.</p></div>',
            '<div class="cards">',
            card("coupe", "Cocktails", "Ingredient-driven drinks built around the season — zero-proof, low, and full-strength, with the ABV printed on every drink."),
            card("wine", "Natural wine", "A natural-leaning list for slow evenings."),
            card("plate", "Small plates", "Seasonal plates for sharing — produce from farms like Goodness Grove, plus things the kitchen fermented and put by."),
            card("cloche", "Prix fixe dinner", "A four-course dinner that reads like the moment: fermentation, preservation, foraged greens."),
            '</div><p class="bandnote"><strong>Sun–Wed 4–10 PM · Thu–Sat 4 till midnight</strong> '
            '<a class="btn p sm" href="' + RESY_URL + '">Book an evening table on Resy</a></p>',
            '</div></section>',
            '<section class="block"><div class="wrap"><div class="split">',
            '<div><p class="kicker">Built on the season</p><h2>Menus that follow the moment</h2>'
            '<p style="color:var(--mut)">Songbird was built around seasonality and locality. The menus '
            'shift as the Piedmont’s micro-seasons shift — produce from farms like Goodness Grove, '
            'things the kitchen fermented and preserved, and foraged greens when they show up. The '
            'drink list moves on the same clock.</p>'
            '<div class="cta-row"><a class="btn g" href="/visit">Hours, directions, and reservations</a></div></div>',
            '<div><address class="addrline"><strong>Songbird</strong><br>' + ADDR + '<br>Inside East End Market<br>' + CITY +
            '</address>' + MAP_IFRAME + '</div>',
            '</div></div></section>',
            ld([ENTITY,
                {"@context": "https://schema.org", "@type": "WebSite", "name": "Songbird",
                 "url": ORIGIN + "/"}]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# ------------------------------------------------------------- programs
def page_programs():
    parts = [head("Programs — Songbird, Raleigh NC",
                  ("Two programs, one room inside East End Market: a bright morning program 8 AM–2 PM "
                   "every day, and a full bar with seasonal cocktails, natural wine, and dinner from 4 PM."),
                  "/programs"),
             header("/programs")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Programs · East End Market</p>',
            '<h1>Two programs, one room</h1>',
            '<p class="lead">Mornings belong to coffee, juice, and the oven. Evenings belong to the '
            'bar. Same tables, same people, two very different lights.</p></div></section>',
            '<section class="block"><div class="wrap">',
            '<div class="grid-2x2">',
            '<a class="tile" href="/morning-program-raleigh"><div class="ic" style="width:34px;height:34px;color:var(--coral)">' + ICON["cup"] + '</div>'
            '<h3>Mornings — 8 AM to 2 PM, daily</h3>'
            '<p>Willow House Coffee, cold-pressed juice, seasonal smoothies, Tin Roof Teas blends, '
            'matcha from Frame, and pastries and morning plates from neighborhood makers. Walk-up '
            'window for grab-and-go.</p><span class="go">See the morning program →</span></a>',
            '<a class="tile" href="/cocktails-dinner-raleigh"><div class="ic" style="width:34px;height:34px;color:var(--coral)">' + ICON["coupe"] + '</div>'
            '<h3>Evenings — from 4 PM</h3>'
            '<p>Seasonal cocktails with ABV printed on every drink, a natural-leaning wine list, '
            'small plates for sharing, and a four-course prix fixe dinner. Sun–Wed till 10, Thu–Sat '
            'till midnight.</p><span class="go">See the evening program →</span></a>',
            '</div>',
            '<div class="infocard" style="margin-top:20px"><h3 style="font-size:21px">The clock behind it all</h3>'
            '<p style="color:var(--mut);margin:8px 0 0">Every part of the menu tracks the Piedmont’s '
            'micro-seasons — fermentation, preservation, and foraged greens included. What pours and '
            'what plates changes as the moment changes; the hours and the two-program shape stay put.</p></div>',
            '</div></section>',
            ld([crumbs([("Home", "/"), ("Programs", "/programs")])]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# -------------------------------------------------------------- morning
def page_morning():
    parts = [head("Morning Coffee, Juice and Matcha — Songbird, Raleigh NC",
                  ("Mornings at Songbird: coffee roasted nearby by Willow House Coffee, cold-pressed "
                   "juice and seasonal smoothies, Tin Roof Teas blends, matcha from Frame, and pastries "
                   "and morning plates — 8 AM–2 PM, every day."),
                  "/morning-program-raleigh"),
             header("/morning-program-raleigh")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Mornings · 8 AM–2 PM · every day</p>',
            '<h1>Coffee, juice, tea, and something from the oven</h1>',
            '<p class="lead">No reservations needed in the morning. Walk in, or order at the walk-up '
            'window on the East End Market side.</p></div></section>',
            '<div class="wrap"><div class="detail">',
            '<div class="detail-main">',
            '<h3>The coffee</h3><p>Espresso and brewed coffee from beans roasted close by on South '
            'Saunders Street — Willow House Coffee is the roaster, a few blocks out. Morning cups lean '
            'on those local beans.</p>',
            '<h3>Pressed and blended</h3><p>Cold-pressed juice and seasonal smoothies, blended from '
            'Piedmont fruit as it turns. What is on the list changes with the moment.</p>',
            '<h3>Tea and matcha</h3><p>Custom tea blends made for Songbird by Tin Roof Teas, plus '
            'matcha drinks built with tea from Frame — hot or iced.</p>',
            '<h3>From the oven</h3><p>Pastries and morning plates from makers around the neighborhood, '
            'set out through the morning.</p>',
            '<h3>The walk-up window</h3><p>In a hurry? The morning program runs a walk-up window for '
            'grab-and-go at East End Market.</p>',
            '</div>',
            '<aside class="aside">',
            '<div class="infocard"><h3>Morning hours</h3><p>Every day<br><strong>8 AM–2 PM</strong></p>'
            '<p style="margin-top:10px">Evenings, from 4 PM — <a href="/cocktails-dinner-raleigh">see the dinner program</a>.</p></div>',
            '<div class="infocard"><h3>Where</h3><p>' + ADDR + '<br>' + CITY + '<br>Inside East End Market</p>'
            '<div class="row" style="margin-top:12px"><a class="btn g sm" href="' + MAP_LINK + '">Directions</a></div></div>',
            '<div class="infocard"><h3>A question?</h3><p>Pastries, morning plates, or the window — leave a note and we will answer.</p>'
            '<div class="row" style="margin-top:12px"><a class="btn g sm" href="/contact">Contact us</a></div></div>',
            '</aside></div></div>',
            ld([service("Morning Program at Songbird",
                        "Coffee, juice, smoothies, tea, matcha, and morning plates 8 AM–2 PM daily inside East End Market, Raleigh NC.",
                        ORIGIN + "/morning-program-raleigh"),
                crumbs([("Home", "/"), ("Programs", "/programs"), ("Morning program", "/morning-program-raleigh")])]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# -------------------------------------------------------------- evening
def page_evening():
    parts = [head("Cocktails, Natural Wine and Prix Fixe Dinner — Songbird, Raleigh NC",
                  ("Evenings at Songbird: seasonal ingredient-driven cocktails with ABV printed, a "
                   "natural-leaning wine list, small plates, and a four-course prix fixe dinner. "
                   "Sun–Wed 4–10 PM, Thu–Sat 4 till midnight."),
                  "/cocktails-dinner-raleigh"),
             header("/cocktails-dinner-raleigh")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Evenings · from 4 PM</p>',
            '<h1>Cocktails, natural wine, and a dinner worth staying for</h1>',
            '<p class="lead">The bar program reads the same way the kitchen does: by season, by farm, '
            'by what is in front of us tonight.</p></div></section>',
            '<div class="wrap"><div class="detail">',
            '<div class="detail-main">',
            '<h3>The cocktail program</h3><p>Ingredient-driven drinks built around the season. Zero-proof, '
            'low, and full-strength all sit on the same list, and every drink prints its ABV — you will '
            'never have to guess what you are in for.</p>',
            '<h3>The wine list</h3><p>A natural-leaning list alongside the cocktails, poured through the '
            'evening.</p>',
            '<h3>Small plates</h3><p>Seasonal plates made for sharing: produce from farms like Goodness '
            'Grove, plus the fermented and preserved things the kitchen put by for moments like this.</p>',
            '<h3>Four-course prix fixe</h3><p>The full dinner — four courses that read like the moment, '
            'fermentation, preservation, and foraged greens included.</p>',
            '<h3>The room</h3><p>Just over 40 seats, plus a patio. A mural by Dain Kim runs along the '
            'wall, drinks land on ceramics from Piedmont Clay Works, and the big cedar communal table '
            'is made from reclaimed wood.</p>',
            '</div>',
            '<aside class="aside">',
            '<div class="infocard"><h3>Evening hours</h3><p>Sun–Wed<br><strong>4–10 PM</strong></p>'
            '<p>Thu–Sat<br><strong>4 PM–midnight</strong></p>'
            '<p style="margin-top:10px">Mornings run 8 AM–2 PM daily — <a href="/morning-program-raleigh">see the morning program</a>.</p></div>',
            '<div class="infocard"><h3>Book it</h3><p>Evening tables open on Resy — reservations are the fastest way to get a seat for dinner.</p>'
            '<div class="row" style="margin-top:12px"><a class="btn p sm" href="' + RESY_URL + '">Book on Resy</a></div></div>',
            '<div class="infocard"><h3>Where</h3><p>' + ADDR + '<br>' + CITY + '<br>Inside East End Market</p>'
            '<div class="row" style="margin-top:12px"><a class="btn g sm" href="' + MAP_LINK + '">Directions</a></div></div>',
            '</aside></div></div>',
            ld([service("Cocktails and Dinner at Songbird",
                        "Seasonal cocktails with ABV printed, natural-leaning wine, small plates, and a four-course prix fixe dinner — evenings from 4 PM, Raleigh NC.",
                        ORIGIN + "/cocktails-dinner-raleigh"),
                crumbs([("Home", "/"), ("Programs", "/programs"), ("Cocktails and dinner", "/cocktails-dinner-raleigh")])]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# ---------------------------------------------------------------- visit
FAQS = [
    ("What are the hours?",
     "Mornings run 8 AM–2 PM every day. Evenings: Sunday–Wednesday 4–10 PM, Thursday–Saturday 4 PM till midnight."),
    ("Do I need a reservation?",
     "Mornings need nothing — walk in or use the walk-up window. For evenings, tables open on Resy: book ahead and we will have a seat ready."),
    ("Are you open every day?",
     "Yes — Songbird is open all seven days, morning program to evening program."),
    ("Can I get a serious drink with no alcohol?",
     "Yes. The cocktail list carries a full zero-proof program alongside low-ABV and full-strength drinks, and every drink prints its ABV."),
    ("Is there food at night?",
     "Seasonal small plates for sharing and a four-course prix fixe dinner, from 4 PM."),
]

def page_visit():
    faq_html, faq_ld = [], []
    for q, a in FAQS:
        faq_html.append("<details class=\"faq\"><summary>" + q + "</summary><p>" + a + "</p></details>")
        faq_ld.append({"@type": "Question", "name": q,
                       "acceptedAnswer": {"@type": "Answer", "text": a}})
    parts = [head("Hours, Directions and Reservations — Songbird, Raleigh NC",
                  ("Songbird hours and directions: inside East End Market at 1020 E Whitaker Mill Rd, "
                   "Ste 130, Raleigh NC 27608. Mornings 8 AM–2 PM daily; evenings from 4 PM — Resy "
                   "reservations for dinner service."),
                  "/visit"),
             header("/visit")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Visit</p>',
            '<h1>Hours, directions, and reservations</h1>',
            '<p class="lead">East End Market, between Wake Forest Road and Atlantic Avenue. Mornings '
            'are walk-in. Evenings book on Resy.</p></div></section>',
            '<section class="block"><div class="wrap"><div class="split">',
            '<div>',
            '<div class="infocard">', HOURS_TABLE,
            '<p class="hintline">The morning program ends at 2 PM; the bar reopens for the room’s evening program at 4 PM.</p>',
            '</div>',
            '<h3 style="margin-top:26px">Reservations</h3>',
            '<p style="color:var(--mut);max-width:60ch">Mornings: no reservation needed — walk in or '
            'use the walk-up window. Evenings: tables open on <a href="' + RESY_URL + '">Resy</a>, and '
            'booking ahead is the surest way to get a seat for dinner.</p>',
            '</div><div>',
            '<address class="addrline"><strong>Songbird</strong><br>' + ADDR + '<br>Inside East End Market, between Wake Forest Road and Atlantic Avenue<br>' + CITY + '</address>',
            MAP_IFRAME,
            '<div class="cta-row" style="margin-top:16px"><a class="btn p" href="' + RESY_URL + '">Book an evening table</a>'
            '<a class="btn g" href="/contact">Send us a note</a></div>',
            '</div></div></div></section>',
            '<section class="block" style="padding-top:10px"><div class="wrap">',
            '<h2>Good to know</h2>',
            "\n".join(faq_html),
            '</div></section>',
            '<section class="block band-evening"><div class="wrap"><div class="split">',
            '<div><p class="kicker">The people</p><h2>Who runs the room</h2>'
            '<p class="mut">Songbird is run by Meg Paradise and Charlie Blue Arm, with kitchen programs '
            'led by Chef Dave Mitchell. It opened inside East End Market in June 2026, built around '
            'seasonality, locality, and a room that works in two lights.</p></div>',
            '<div class="infocard"><h3>Written about</h3><ul class="linklist" style="color:inherit">'
            '<li><a href="https://www.newsobserver.com/restaurant/south-carolina/charlotte/article315828601.html">News &amp; Observer — the opening night</a></li>'
            '<li><a href="https://www.newsobserver.com/restaurant/south-carolina/charlotte/article314823761.html">News &amp; Observer — the concept and the address</a></li>'
            '<li><a href="https://www.visitraleigh.com/listing/songbird/78948/">VisitRaleigh — official listing</a></li>'
            '<li><a href="' + IG_URL + '">Instagram: @songbird.nc</a></li></ul></div>',
            '</div></div></section>',
            ld([crumbs([("Home", "/"), ("Visit", "/visit")]),
                {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faq_ld}]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# -------------------------------------------------------------- contact
def page_contact():
    parts = [head("Contact — Songbird, Raleigh NC",
                  ("Contact Songbird, a daylight-to-dusk bar inside East End Market at 1020 E Whitaker "
                   "Mill Rd, Raleigh NC. Leave a note — we answer by email. Evening tables book on Resy."),
                  "/contact"),
             header("/contact")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Contact</p>',
            '<h1>Leave us a note</h1>',
            '<p class="lead">Questions about the room, the programs, or what is pouring tonight — the '
            'form below lands straight with us, and we answer by email.</p></div></section>',
            '<div class="wrap"><div class="detail">',
            '<div class="detail-main">',
            '<form class="cform" method="post" action="/contact" accept-charset="utf-8">',
            '<label for="f-name">Name *</label><input id="f-name" name="name" type="text" maxlength="120" required autocomplete="name">',
            '<label for="f-email">Email *</label><input id="f-email" name="email" type="email" maxlength="120" required autocomplete="email" placeholder="you@example.com">',
            '<label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" maxlength="60" autocomplete="tel" placeholder="optional">',
            '<label for="f-msg">Message *</label><textarea id="f-msg" name="message" maxlength="4000" required placeholder="What would you like to ask?"></textarea>',
            '<button class="btn p" type="submit">Send note</button>',
            '<p class="hintline">* required. We use what you leave here only to answer you.</p>',
            '</form></div>',
            '<aside class="aside">',
            '<div class="infocard"><h3>Faster ways</h3><p>Evening table: <a href="' + RESY_URL + '">book on Resy</a>.<br>Morning grab-and-go: the walk-up window, 8 AM–2 PM.</p></div>',
            '<div class="infocard"><h3>Where and when</h3><p>' + ADDR + '<br>' + CITY + '</p>'
            '<p style="margin-top:10px">Mornings daily 8 AM–2 PM.<br>Evenings: Sun–Wed 4–10, Thu–Sat till midnight.</p>'
            '<div class="row" style="margin-top:12px"><a class="btn g sm" href="' + MAP_LINK + '">Directions</a></div></div>',
            '</aside></div></div>',
            ld([service("Contact Songbird",
                        "Leave a note for Songbird, a daylight-to-dusk bar at East End Market, Raleigh NC — we answer by email.",
                        ORIGIN + "/contact"),
                crumbs([("Home", "/"), ("Contact", "/contact")])]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# -------------------------------------------------------------- privacy
def page_privacy():
    parts = [head("Privacy — Songbird, Raleigh NC",
                  ("How Songbird handles what you send through its contact form: name, email, and your "
                   "note, used only to answer you. No cookies, no third-party trackers."),
                  "/privacy"),
             header("/privacy")]
    body = ['<main id="main">',
            '<section class="pagehead"><div class="wrap">',
            '<p class="kicker">Privacy</p>',
            '<h1>What this site keeps</h1></div></section>',
            '<section class="block"><div class="wrap"><div class="detail-main" style="max-width:720px">',
            '<h3>The contact form</h3><p>When you send a note, we collect your name, your email '
            '(optional phone), and your message. It is used for one thing: answering you. It is not '
            'sold, and it is not added to a marketing list.</p>',
            '<h3>Cookies and trackers</h3><p>This site sets no cookies and runs no third-party '
            'analytics or advertising scripts. The map on the visit page is a Google Maps embed, which '
            'may set its own cookies when you interact with it.</p>',
            '<h3>Your note, your call</h3><p>Sent us something and want it gone? Leave a note in the '
            'contact form asking us to delete it, and we will remove it from the inbox it landed in.</p>',
            '<h3>Questions</h3><p>Use the <a href="/contact">contact form</a> for anything privacy-related.</p>',
            '</div></div></section>',
            ld([crumbs([("Home", "/"), ("Privacy", "/privacy")]),
                service("Privacy Policy at Songbird",
                        "How Songbird's contact form and demo site handle the details you send.",
                        ORIGIN + "/privacy")]),
            '</main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

# -------------------------------------------------------- utility pages
def page_thanks():
    parts = [head("Thank You — Songbird, Raleigh NC",
                  ("Your note reached Songbird — we answer by email as soon as we can. Evening tables "
                   "book on Resy; mornings walk up from 8 AM."),
                  "/thanks", no_og=True),
             header("/thanks")]
    body = ['<main id="main" style="padding:88px 0 96px"><div class="wrap" style="max-width:640px">',
            '<p class="kicker">Message sent</p>',
            '<h1>Your note is in.</h1>',
            '<p class="lead" style="max-width:46ch">We answer email as soon as we can. If you are '
            'after an evening table, Resy is the fastest path.</p>',
            '<div class="cta-row"><a class="btn p" href="' + RESY_URL + '">Book an evening table</a>'
            '<a class="btn g" href="/programs">See the programs</a>'
            '<a class="btn g" href="' + ORIGIN + '/">Home</a></div></div></main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

def page_404():
    parts = [head("Page Not Found — Songbird, Raleigh NC",
                  ("That page is not here. Find the morning program, the evening program, hours, and "
                   "reservations from the Songbird home page."),
                  "/404", no_og=True),
             header("/404")]
    body = ['<main id="main" style="padding:88px 0 96px"><div class="wrap" style="max-width:640px">',
            '<p class="kicker">Error 404</p>',
            '<h1>That page is not here.</h1>',
            '<p class="lead" style="max-width:46ch">The sun moved — try one of these instead:</p>',
            '<div class="cta-row"><a class="btn p" href="/programs">Programs</a>'
            '<a class="btn g" href="/visit">Hours and directions</a>'
            '<a class="btn g" href="/contact">Contact</a></div></div></main>']
    return "\n".join(parts + body + [FOOTER, "</body></html>"])

def main():
    os.makedirs(PUBLIC, exist_ok=True)
    pages = {
        "index.html": page_index(),
        "programs.html": page_programs(),
        "morning-program-raleigh.html": page_morning(),
        "cocktails-dinner-raleigh.html": page_evening(),
        "visit.html": page_visit(),
        "contact.html": page_contact(),
        "privacy.html": page_privacy(),
        "thanks.html": page_thanks(),
        "404.html": page_404(),
    }
    pages["style.css"] = CSS
    pages["robots.txt"] = ("User-agent: *\nDisallow: /thanks\nDisallow: /404\n"
                           "Sitemap: " + ORIGIN + "/sitemap.xml\n")
    locs = ["/", "/programs", "/morning-program-raleigh", "/cocktails-dinner-raleigh",
            "/visit", "/contact", "/privacy"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>']
    sm.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for p in locs:
        sm.append('<url><loc>' + ORIGIN + p + '</loc><lastmod>2026-11-26</lastmod></url>')
    sm.append("</urlset>")
    pages["sitemap.xml"] = "\n".join(sm) + "\n"
    pages["favicon.svg"] = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        '<rect width="64" height="64" rx="14" fill="#1b1628"/>'
        '<circle cx="41" cy="24" r="10" fill="#dfa04e"/>'
        '<path d="M13 47a21 21 0 0 1 21-21 16 16 0 0 1 10 3.5 17.8 17.8 0 0 0-31 17.5z" fill="#faf3e6"/>'
        '<path d="M43 40a9.5 9.5 0 0 1 0 14" stroke="#c25a3b" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
        '<circle cx="23.5" cy="28" r="4" fill="#1b1628"/>'
        '</svg>')
    for name, content in pages.items():
        with open(os.path.join(PUBLIC, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote", name, len(content.encode("utf-8")), "B")

if __name__ == "__main__":
    main()
