#!/usr/bin/env python3
"""
Static site generator — TipRun Rubbish Removal
Edit CONFIG + SUBURBS, run `python3 generate.py`, push the /docs folder to GitHub Pages.
"""
import os, html, json, shutil

# ============================================================
# CONFIG — change these, then re-run this script
# ============================================================
BIZ      = "TipRun Rubbish Removal"
PHONE    = "0410 642 507"          # <-- YOUR NUMBER
PHONE_A  = "tel:+61410642507"      # <-- tel: link format
BASE_URL = "https://tiprun.homes"  # custom domain, no trailing slash
FORM_URL = "https://formspree.io/f/mjgnzjon"  # <-- your Formspree endpoint
OUT      = "docs"                  # GitHub Pages can serve from /docs on main branch

# ============================================================
# SUBURB DATA — name, city, state, postcode, unique note, common jobs
# ============================================================
SUBURBS = [
 # --- Sydney ---
 dict(n="Parramatta", c="Sydney", s="NSW", p="2150", note="With apartment towers going up along the river and older fibro homes being cleared in North Parramatta, we handle everything from balcony junk runs to full pre-demolition strip-outs.", jobs=["Apartment cleanouts","Renovation debris","Office strip-outs"]),
 dict(n="Bondi", c="Sydney", s="NSW", p="2026", note="Tight streets, no parking and walk-up flats are no problem — our small trucks fit Bondi's back lanes and we carry everything down from top-floor units ourselves.", jobs=["Unit & flat cleanouts","End-of-lease junk","Furniture removal"]),
 dict(n="Penrith", c="Sydney", s="NSW", p="2750", note="Big blocks out Penrith way mean big cleanups — sheds, yards and garages full of years of gear. We bring the trailer and the muscle.", jobs=["Shed & garage cleanouts","Green waste","Hard rubbish"]),
 dict(n="Blacktown", c="Sydney", s="NSW", p="2148", note="One of Sydney's busiest council areas for kerbside pickups — if you missed the council collection or have more than they'll take, we'll clear it same day.", jobs=["Missed council pickup","Household junk","Whitegoods"]),
 dict(n="Liverpool", c="Sydney", s="NSW", p="2170", note="From new estates around Edmondson Park to established homes in Liverpool itself, we do builder's leftovers, moving-day junk and full house clearances.", jobs=["Builder's waste","House clearances","Moving junk"]),
 dict(n="Chatswood", c="Sydney", s="NSW", p="2067", note="We regularly service Chatswood's apartment blocks and offices — booking dock access and lift protection sorted with your building manager before we arrive.", jobs=["Office junk","Apartment cleanouts","E-waste"]),
 dict(n="Manly", c="Sydney", s="NSW", p="2095", note="Beach-side salt air is hard on outdoor furniture and BBQs — we run regular trips across the Spit clearing decks, balconies and garages on the northern beaches.", jobs=["Outdoor furniture","Garage cleanouts","Deck & balcony junk"]),
 dict(n="Castle Hill", c="Sydney", s="NSW", p="2154", note="Downsizing from a big Hills District family home? We do careful, room-by-room clearances and make sure good furniture goes to charity, not landfill.", jobs=["Downsizing clearances","Furniture removal","Estate cleanups"]),
 dict(n="Bankstown", c="Sydney", s="NSW", p="2200", note="We work with Bankstown landlords and agents on fast end-of-tenancy clear-outs so properties are back on the market within days.", jobs=["End-of-tenancy","Landlord cleanouts","Mattresses & whitegoods"]),
 dict(n="Sutherland", c="Sydney", s="NSW", p="2232", note="Shire jobs are mostly green waste and garage clean-ups — we separate vegetation for mulching rather than dumping it, keeping tip fees down.", jobs=["Green waste","Garage cleanouts","Trampolines & play equipment"]),
 dict(n="Ryde", c="Sydney", s="NSW", p="2112", note="Between unit developments and older homes being renovated, Ryde keeps us busy with strip-out debris, old kitchens and bathroom rip-outs.", jobs=["Kitchen & bathroom rip-outs","Reno debris","Unit cleanouts"]),
 dict(n="Newtown", c="Sydney", s="NSW", p="2042", note="Terrace houses with no rear access are our specialty — everything comes through the front door and straight onto the truck, protected floors included.", jobs=["Terrace house cleanouts","Furniture removal","Share-house junk"]),
 # --- Melbourne ---
 dict(n="Richmond", c="Melbourne", s="VIC", p="3121", note="Richmond's worker's cottages and warehouse conversions mean narrow access and heavy loads — we bring dollies, ramps and a truck that fits the back streets.", jobs=["Cottage cleanouts","Warehouse junk","Reno debris"]),
 dict(n="St Kilda", c="Melbourne", s="VIC", p="3182", note="Art-deco flats and rooming houses around St Kilda often need fast, discreet clearances — we handle deceased estates and hoarding cleanups with care.", jobs=["Flat cleanouts","Deceased estates","Hoarding cleanups"]),
 dict(n="Footscray", c="Melbourne", s="VIC", p="3011", note="The inner west is renovating fast — we clear skip-loads of plaster, timber and old fittings from Footscray's Victorian and Edwardian homes.", jobs=["Renovation waste","Hard rubbish","Shop fit-out junk"]),
 dict(n="Brunswick", c="Melbourne", s="VIC", p="3056", note="Share houses, studios and small factories along Sydney Road — we do everything from single-couch pickups to full commercial clearances.", jobs=["Share-house junk","Studio cleanouts","Commercial waste"]),
 dict(n="Dandenong", c="Melbourne", s="VIC", p="3175", note="We service Dandenong's factories and warehouses with scheduled and one-off industrial junk runs, pallets, and office strip-outs.", jobs=["Industrial junk","Pallets & packaging","Office strip-outs"]),
 dict(n="Frankston", c="Melbourne", s="VIC", p="3199", note="Bayside blocks with big backyards — Frankston jobs are usually sheds, green waste and years of accumulated garage gear headed for the tip.", jobs=["Shed cleanouts","Green waste","Garage junk"]),
 dict(n="Box Hill", c="Melbourne", s="VIC", p="3128", note="With apartments rising all over Box Hill we do a lot of pre-settlement cleanouts and old-home clearances before knock-down rebuilds.", jobs=["Pre-demolition clearances","Apartment junk","Furniture removal"]),
 dict(n="Werribee", c="Melbourne", s="VIC", p="3030", note="New estates across Wyndham mean builder's leftovers, packaging and landscaping waste — we do fast pickups so your new block stays clean.", jobs=["Builder's leftovers","Packaging & boxes","Landscaping waste"]),
 dict(n="Preston", c="Melbourne", s="VIC", p="3072", note="Preston's mix of old family homes and new townhouses keeps us moving — hard rubbish, deceased estates and full house clearances every week.", jobs=["Hard rubbish","House clearances","Whitegoods"]),
 dict(n="Glen Waverley", c="Melbourne", s="VIC", p="3150", note="Downsizers and knock-down-rebuilds dominate Glen Waverley — we clear entire family homes, garages and gardens before demolition day.", jobs=["Full house clearances","Downsizing","Garden waste"]),
 dict(n="Craigieburn", c="Melbourne", s="VIC", p="3064", note="Growing families in Craigieburn's new estates call us for moving-day junk, old furniture and the flat-pack boxes that never got thrown out.", jobs=["Moving junk","Old furniture","Boxes & packaging"]),
 dict(n="Cranbourne", c="Melbourne", s="VIC", p="3977", note="Acreage on the city fringe means bigger loads — we handle green waste, fencing, and multi-trailer property cleanups around Cranbourne.", jobs=["Property cleanups","Fencing & timber","Green waste"]),
 # --- Brisbane ---
 dict(n="Fortitude Valley", c="Brisbane", s="QLD", p="4006", note="Bars, offices and apartments stacked into one postcode — we do after-hours commercial junk runs so Valley businesses never close for a cleanout.", jobs=["Commercial junk","Office strip-outs","Apartment cleanouts"]),
 dict(n="Chermside", c="Brisbane", s="QLD", p="4032", note="Post-war homes on Brisbane's northside are being cleared and renovated fast — we take old fittings, asbestos-free demo waste and garage junk.", jobs=["Reno waste","Garage cleanouts","Old furniture"]),
 dict(n="Ipswich", c="Brisbane", s="QLD", p="4305", note="Queenslanders on big blocks: under-house storage areas full of decades of gear are our bread and butter around Ipswich.", jobs=["Under-house cleanouts","Shed junk","Hard rubbish"]),
 dict(n="Logan Central", c="Brisbane", s="QLD", p="4114", note="We work with Logan property managers on fast rental turnovers — full cleanouts, yard clearing and tip runs, usually within 48 hours.", jobs=["Rental turnovers","Yard clearing","Mattresses & whitegoods"]),
 dict(n="Carindale", c="Brisbane", s="QLD", p="4152", note="Family homes in Carindale call us for garage cleanouts, old play equipment and pre-sale decluttering before hitting the market.", jobs=["Pre-sale decluttering","Garage junk","Play equipment"]),
 dict(n="Indooroopilly", c="Brisbane", s="QLD", p="4068", note="Steep blocks and multi-level homes in the western suburbs — our crew carries everything up (or down) the stairs so you don't have to.", jobs=["Multi-level home cleanouts","Furniture removal","Green waste"]),
 dict(n="Redcliffe", c="Brisbane", s="QLD", p="4020", note="Sea-change downsizers on the peninsula — we clear units and family homes with care, donating what's still usable to local charities.", jobs=["Downsizing","Unit cleanouts","Charity-first clearances"]),
 dict(n="Springfield", c="Brisbane", s="QLD", p="4300", note="One of Australia's fastest-growing areas — Springfield jobs are new-home packaging, landscaping offcuts and moving-day leftovers.", jobs=["Moving junk","Landscaping offcuts","Packaging"]),
 # --- Perth ---
 dict(n="Fremantle", c="Perth", s="WA", p="6160", note="Heritage limestone cottages with tiny access — Freo jobs need small trucks and careful crews, and that's exactly what we run.", jobs=["Cottage cleanouts","Reno debris","Furniture removal"]),
 dict(n="Joondalup", c="Perth", s="WA", p="6027", note="Northern-corridor family homes: garages, sheds and backyard cleanups, with green waste separated for mulching not landfill.", jobs=["Garage cleanouts","Green waste","Hard rubbish"]),
 dict(n="Rockingham", c="Perth", s="WA", p="6168", note="Coastal weather wrecks outdoor gear — we run regular Rockingham trips clearing rusted furniture, old spas and shed junk.", jobs=["Outdoor furniture","Spa & pool equipment","Shed cleanouts"]),
 dict(n="Midland", c="Perth", s="WA", p="6056", note="Older homes and workshops around Midland mean heavy loads — scrap, tools, machinery and full property clearances.", jobs=["Workshop clearances","Scrap metal","Property cleanups"]),
 dict(n="Cannington", c="Perth", s="WA", p="6107", note="We support Cannington businesses and landlords with commercial junk runs and rapid rental-property turnovers.", jobs=["Commercial junk","Rental turnovers","Office furniture"]),
 dict(n="Scarborough", c="Perth", s="WA", p="6019", note="Apartments along the Scarborough beachfront — we handle lift bookings and strata requirements so cleanouts run smoothly.", jobs=["Apartment cleanouts","Balcony junk","End-of-lease"]),
 # --- Adelaide ---
 dict(n="Glenelg", c="Adelaide", s="SA", p="5045", note="Beachside units and older villas around the Bay — we do everything from single-item pickups to complete deceased-estate clearances.", jobs=["Unit cleanouts","Deceased estates","Furniture removal"]),
 dict(n="Norwood", c="Adelaide", s="SA", p="5067", note="Bluestone villas with narrow side access — Norwood cleanouts come through the front with floor protection down and careful hands.", jobs=["Villa cleanouts","Reno debris","Hard rubbish"]),
 dict(n="Salisbury", c="Adelaide", s="SA", p="5108", note="Big northern-suburbs blocks with sheds and years of stored gear — we bring the big trailer for Salisbury jobs.", jobs=["Shed cleanouts","Yard clearing","Whitegoods"]),
 dict(n="Marion", c="Adelaide", s="SA", p="5043", note="Downsizers and rental turnovers keep us busy around Marion — fast quotes, careful crews, and donation-first sorting.", jobs=["Downsizing","Rental turnovers","Furniture removal"]),
 dict(n="Port Adelaide", c="Adelaide", s="SA", p="5015", note="Warehouses, workshops and worker's cottages — the Port's mix means we handle commercial and residential loads in the same day.", jobs=["Warehouse junk","Workshop clearances","House cleanouts"]),
 # --- Gold Coast ---
 dict(n="Southport", c="Gold Coast", s="QLD", p="4215", note="High-rise units and canal homes — we coordinate with building managers for lift access and do canal-front garden waste runs.", jobs=["Unit cleanouts","Garden waste","End-of-lease"]),
 dict(n="Surfers Paradise", c="Gold Coast", s="QLD", p="4217", note="Holiday apartments turn over fast — we do same-day cleanouts between tenants and after short-stay damage, lifts and dock access sorted.", jobs=["Holiday apartment cleanouts","Furniture removal","Mattresses"]),
 dict(n="Robina", c="Gold Coast", s="QLD", p="4226", note="Family homes and townhouses around Robina — garage cleanups, moving junk and pre-sale decluttering are our most common calls.", jobs=["Garage cleanups","Moving junk","Pre-sale decluttering"]),
 # --- Canberra ---
 dict(n="Belconnen", c="Canberra", s="ACT", p="2617", note="Canberra's bulky waste rules are strict — we take everything the kerbside collection won't, from mattresses to full garage loads.", jobs=["Bulky waste","Garage cleanouts","Mattresses & whitegoods"]),
 dict(n="Woden", c="Canberra", s="ACT", p="2606", note="Downsizing from an old Woden Valley family home? We do respectful, room-by-room clearances with donation runs to local charities.", jobs=["Downsizing clearances","Deceased estates","Furniture removal"]),
 # --- Hobart ---
 dict(n="Glenorchy", c="Hobart", s="TAS", p="7010", note="Hobart's northern suburbs — we clear sheds, yards and full properties, with green waste separated for the Glenorchy composting facility.", jobs=["Shed cleanouts","Green waste","Property cleanups"]),
 # --- Newcastle ---
 dict(n="Charlestown", c="Newcastle", s="NSW", p="2290", note="Lake Macquarie families call us for garage cleanouts, old boats-worth of gear and pre-sale property tidy-ups around Charlestown.", jobs=["Garage cleanouts","Pre-sale tidy-ups","Hard rubbish"]),
]

def slug(s): return s.lower().replace(" ", "-").replace("'", "")
for sb in SUBURBS: sb["slug"] = slug(sb["n"])
CITIES = []
for sb in SUBURBS:
    if sb["c"] not in CITIES: CITIES.append(sb["c"])

# ============================================================
# CSS
# ============================================================
CSS = """
:root{
  --ink:#17191c; --paper:#f5f4ef; --hivis:#ffc400; --green:#1f7a4d;
  --steel:#5c626b; --line:#e2e0d6; --white:#ffffff;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important}}
body{font-family:'Archivo',system-ui,sans-serif;background:var(--paper);color:var(--ink);line-height:1.6;font-size:17px}
.display{font-family:'Anton',Impact,sans-serif;text-transform:uppercase;letter-spacing:.01em;line-height:.95;font-weight:400}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.tape{height:14px;background:repeating-linear-gradient(-45deg,var(--ink) 0 16px,var(--hivis) 16px 32px)}
/* header */
header{background:var(--ink);color:var(--paper);position:sticky;top:0;z-index:50}
.nav{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;max-width:1080px;margin:0 auto;gap:16px}
.logo{font-family:'Anton',Impact,sans-serif;font-size:22px;text-transform:uppercase;text-decoration:none;letter-spacing:.03em}
.logo em{color:var(--hivis);font-style:normal}
.nav-links{display:flex;gap:22px;list-style:none;font-size:15px}
.nav-links a{text-decoration:none;opacity:.85}
.nav-links a:hover,.nav-links a:focus{opacity:1;color:var(--hivis)}
.call-btn{background:var(--hivis);color:var(--ink);font-family:'Anton',Impact,sans-serif;font-size:17px;text-transform:uppercase;text-decoration:none;padding:10px 20px;letter-spacing:.03em;white-space:nowrap}
.call-btn:hover,.call-btn:focus{background:var(--white)}
a:focus-visible,button:focus-visible{outline:3px solid var(--hivis);outline-offset:2px}
/* hero */
.hero{background:var(--ink);color:var(--paper);padding:72px 0 64px}
.hero .eyebrow{color:var(--hivis);font-size:14px;letter-spacing:.18em;text-transform:uppercase;font-weight:600;margin-bottom:18px}
.hero h1{font-size:clamp(44px,8vw,96px);color:var(--white)}
.hero h1 .hl{color:var(--hivis)}
.hero p.lede{max-width:560px;margin:24px 0 32px;font-size:19px;color:#c9cbc6}
.hero-ctas{display:flex;gap:14px;flex-wrap:wrap}
.btn-big{background:var(--hivis);color:var(--ink);font-family:'Anton',Impact,sans-serif;font-size:22px;text-transform:uppercase;text-decoration:none;padding:16px 30px;letter-spacing:.03em}
.btn-big:hover,.btn-big:focus{background:var(--white)}
.btn-ghost{border:2px solid var(--steel);color:var(--paper);font-family:'Anton',Impact,sans-serif;font-size:22px;text-transform:uppercase;text-decoration:none;padding:14px 30px;letter-spacing:.03em}
.btn-ghost:hover,.btn-ghost:focus{border-color:var(--hivis);color:var(--hivis)}
/* sections */
section{padding:72px 0}
.sec-label{display:inline-block;background:var(--ink);color:var(--hivis);font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:600;padding:5px 12px;margin-bottom:16px}
h2.display{font-size:clamp(30px,4.5vw,52px);margin-bottom:18px}
.sub{color:var(--steel);max-width:620px;margin-bottom:36px}
/* manifest */
.manifest{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:2px;background:var(--line);border:2px solid var(--ink)}
.manifest div{background:var(--white);padding:16px 18px;font-size:16px}
.manifest div::before{content:"✔";color:var(--green);font-weight:700;margin-right:10px}
.no-take{margin-top:18px;font-size:14px;color:var(--steel)}
/* enquiry form */
.quote-form{border:2px solid var(--ink);background:var(--white);padding:30px;max-width:560px}
.ff{margin-bottom:18px}
.ff label{display:block;font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.ff input,.ff textarea,.ff select{width:100%;border:2px solid var(--line);background:var(--paper);padding:12px 14px;font:inherit;font-size:16px}
.ff select{cursor:pointer;appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--ink) 50%),linear-gradient(135deg,var(--ink) 50%,transparent 50%);background-position:calc(100% - 20px) 55%,calc(100% - 14px) 55%;background-size:6px 6px;background-repeat:no-repeat}
.ff input:focus,.ff textarea:focus,.ff select:focus{outline:none;border-color:var(--ink);background-color:var(--white)}
.form-split{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media(max-width:800px){.form-split{grid-template-columns:1fr}}
/* steps */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:28px}
.step h3{font-family:'Anton',Impact,sans-serif;font-size:22px;text-transform:uppercase;margin:12px 0 8px}
.step .tick{width:44px;height:44px;background:var(--ink);color:var(--hivis);font-family:'Anton',Impact,sans-serif;font-size:22px;display:flex;align-items:center;justify-content:center}
.step p{color:var(--steel);font-size:15px}
/* areas */
.city-block{margin-bottom:34px}
.city-block h3{font-family:'Anton',Impact,sans-serif;font-size:22px;text-transform:uppercase;border-bottom:3px solid var(--hivis);display:inline-block;margin-bottom:14px}
.area-grid{display:flex;flex-wrap:wrap;gap:10px}
.area-grid a{background:var(--white);border:1px solid var(--line);padding:8px 14px;font-size:15px;text-decoration:none}
.area-grid a:hover,.area-grid a:focus{border-color:var(--ink);background:var(--hivis)}
/* faq */
.faq details{background:var(--white);border:1px solid var(--line);margin-bottom:10px}
.faq summary{padding:16px 20px;font-weight:600;cursor:pointer;list-style:none}
.faq summary::after{content:"+";float:right;font-family:'Anton',Impact,sans-serif;font-size:20px}
.faq details[open] summary::after{content:"–"}
.faq details p{padding:0 20px 18px;color:var(--steel)}
/* cta band */
.cta-band{background:var(--ink);color:var(--paper);text-align:center;padding:64px 24px}
.cta-band h2{font-size:clamp(30px,5vw,56px);color:var(--white);margin-bottom:10px}
.cta-band p{color:#c9cbc6;margin-bottom:28px}
/* footer */
footer{background:var(--ink);color:#9a9e97;font-size:14px;border-top:1px solid #2c2f33}
.foot{max-width:1080px;margin:0 auto;padding:36px 24px;display:flex;flex-wrap:wrap;gap:28px;justify-content:space-between}
.foot a{color:#c9cbc6;text-decoration:none}
.foot a:hover{color:var(--hivis)}
.foot-areas{max-width:1080px;margin:0 auto;padding:0 24px 36px;font-size:13px;line-height:2}
.foot-areas a{color:#7f847d;text-decoration:none;margin-right:14px}
.foot-areas a:hover{color:var(--hivis)}
/* suburb page bits */
.crumb{font-size:14px;color:var(--steel);padding:20px 0 0}
.crumb a{color:var(--steel)}
.jobs-chips{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0}
.jobs-chips span{background:var(--ink);color:var(--hivis);font-size:14px;padding:7px 14px;font-weight:600}
.two-col{display:grid;grid-template-columns:1.2fr .8fr;gap:48px}
@media(max-width:800px){.two-col{grid-template-columns:1fr}}
.side-card{border:2px solid var(--ink);background:var(--white);padding:26px;height:fit-content}
.side-card h3{font-family:'Anton',Impact,sans-serif;font-size:20px;text-transform:uppercase;margin-bottom:12px}
.side-card ul{list-style:none}
.side-card li{padding:7px 0;border-bottom:1px solid var(--line)}
.side-card li a{text-decoration:none}
.side-card li a:hover{color:var(--green);text-decoration:underline}
"""

# ============================================================
# HTML building blocks
# ============================================================
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;600;700&display=swap" rel="stylesheet">'

def head(title, desc, canonical, css_path, extra_schema=""):
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
{FONTS}
<link rel="stylesheet" href="{css_path}style.css">
{extra_schema}
</head>
<body>"""

def header_nav(root=""):
    return f"""<header>
<nav class="nav" aria-label="Main">
  <a class="logo" href="{root}index.html">Tip<em>Run</em></a>
  <ul class="nav-links">
    <li><a href="{root}index.html#what-we-take">What we take</a></li>
    <li><a href="{root}index.html#quote">Get a quote</a></li>
    <li><a href="{root}locations/index.html">Service areas</a></li>
  </ul>
  <a class="call-btn" href="{PHONE_A}">Call {PHONE}</a>
</nav>
</header>
<div class="tape" aria-hidden="true"></div>"""

def quote_form(suburb=None):
    sub_val = f' value="{suburb}"' if suburb else ' placeholder="e.g. Bondi"'
    return f"""<form class="quote-form" action="{FORM_URL}" method="POST">
  <div class="ff"><label for="qf-name">Your name</label><input id="qf-name" type="text" name="name" required autocomplete="name"></div>
  <div class="ff"><label for="qf-phone">Phone number</label><input id="qf-phone" type="tel" name="phone" required autocomplete="tel"></div>
  <div class="ff"><label for="qf-suburb">Suburb</label><input id="qf-suburb" type="text" name="suburb" required{sub_val}></div>
  <div class="ff"><label for="qf-type">What type of rubbish?</label>
    <select id="qf-type" name="rubbish_type" required>
      <option value="" disabled selected>Choose one…</option>
      <option>Furniture &amp; mattresses</option>
      <option>Whitegoods &amp; appliances</option>
      <option>Green waste / garden</option>
      <option>Renovation / building debris</option>
      <option>Garage or shed cleanout</option>
      <option>Full house clearance</option>
      <option>Deceased estate</option>
      <option>Office / commercial junk</option>
      <option>Mixed household junk</option>
      <option>Other</option>
    </select></div>
  <div class="ff"><label for="qf-size">Roughly how much?</label>
    <select id="qf-size" name="load_size" required>
      <option value="" disabled selected>Choose one…</option>
      <option>A few items (1–3 pieces)</option>
      <option>About a ute load</option>
      <option>A small truck load</option>
      <option>A full truck load or more</option>
      <option>Not sure — need a look</option>
    </select></div>
  <div class="ff"><label for="qf-access">Access at the property?</label>
    <select id="qf-access" name="access" required>
      <option value="" disabled selected>Choose one…</option>
      <option>Ground floor / easy access</option>
      <option>Stairs involved</option>
      <option>Apartment with lift</option>
      <option>Tight or difficult access</option>
    </select></div>
  <button type="submit" class="btn-big" style="border:none;cursor:pointer;width:100%">Send my enquiry</button>
  <p class="no-take" style="margin-top:12px">We'll get back to you fast with a free, no-obligation quote — or skip the form and call <a href="{PHONE_A}"><strong>{PHONE}</strong></a>.</p>
</form>"""

def steps():
    return """<div class="steps">
  <div class="step"><div class="tick">1</div><h3>Call or text a photo</h3><p>Snap the pile, send it through, get a ballpark price in minutes.</p></div>
  <div class="step"><div class="tick">2</div><h3>We show up & quote</h3><p>Fixed price on the spot. Happy? We start loading immediately.</p></div>
  <div class="step"><div class="tick">3</div><h3>Gone. Swept. Sorted.</h3><p>We load everything, sweep the area, and recycle or donate what we can.</p></div>
</div>"""

MANIFEST_ITEMS = ["Furniture & mattresses","Whitegoods & appliances","Green waste & branches","Renovation debris","E-waste & TVs","Office & commercial junk","Garage & shed contents","Deceased estate contents","Hot tubs & trampolines","Scrap metal","Carpet & underlay","General household junk"]
def manifest():
    cells = "".join(f"<div>{i}</div>" for i in MANIFEST_ITEMS)
    return f"""<div class="manifest">{cells}</div>
<p class="no-take"><strong>We can't take:</strong> asbestos, wet paint, chemicals, gas bottles or food waste — but we'll point you to the right licensed facility for those.</p>"""

def footer_block(root=""):
    links = " ".join(f'<a href="{root}locations/{s["slug"]}.html">{s["n"]}</a>' for s in SUBURBS)
    return f"""<div class="cta-band">
  <h2 class="display">One call. <span style="color:var(--hivis)">Gone today.</span></h2>
  <p>Free quotes, 7 days. We load it, we sweep up, we're gone.</p>
  <a class="btn-big" href="{PHONE_A}">Call {PHONE}</a>
</div>
<footer>
  <div class="foot">
    <div><strong style="color:#fff">{BIZ}</strong><br>Fast, friendly rubbish removal across Australia.<br>7 days &middot; Free quotes</div>
    <div><a href="{PHONE_A}">{PHONE}</a><br><a href="{root}locations/index.html">All service areas</a></div>
  </div>
  <div class="foot-areas"><strong style="color:#c9cbc6">Service areas:</strong><br>{links}</div>
  <div style="text-align:center;padding:0 24px 28px;color:#5c626b">&copy; 2026 {BIZ}. ABN 00 000 000 000.</div>
</footer>
</body></html>"""

def faq_html(pairs):
    out = '<div class="faq">'
    for q,a in pairs:
        out += f"<details><summary>{q}</summary><p>{a}</p></details>"
    return out + "</div>"

def faq_schema(pairs):
    data = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'

def biz_schema(area=None):
    d = {"@context":"https://schema.org","@type":"LocalBusiness","name":BIZ,
         "telephone":PHONE,"url":BASE_URL,
         "openingHours":"Mo-Su 07:00-19:00",
         "description":"Same-day rubbish removal — furniture, whitegoods, green waste, renovation debris and full house clearances."}
    if area: d["areaServed"] = {"@type":"City","name":f"{area['n']}, {area['s']}"}
    else: d["areaServed"] = {"@type":"Country","name":"Australia"}
    return f'<script type="application/ld+json">{json.dumps(d)}</script>'

# ============================================================
# PAGES
# ============================================================
os.makedirs(f"{OUT}/locations", exist_ok=True)
with open(f"{OUT}/style.css","w") as f: f.write(CSS)

# ---- Homepage ----
home_faq = [
 ("How fast can you get here?","Most jobs are done same-day or next-day. Call before 10am and we can usually be there that afternoon."),
 ("How do quotes work?","Send a photo or fill in the enquiry form and we'll come back with a free, no-obligation quote. The quote we confirm on site is the price you pay — labour, loading and tip fees all included, no surprises."),
 ("Do I need to move anything?","No. Point at it and it's gone. Our crew does all the lifting, carrying and loading — stairs, lifts and tight access included."),
 ("What happens to my stuff?","We sort every load. Usable furniture goes to charity, metals and e-waste to recyclers, green waste to mulching. Landfill is our last resort."),
 ("Are you insured?","Yes — fully insured for public liability, and our crews are trained for safe manual handling."),
]
title = f"Rubbish Removal Australia | Same-Day Junk Pickup | {BIZ}"
desc  = "Same-day rubbish removal across 50+ Australian suburbs. We load it, sweep up & recycle what we can. Free quotes, 7 days. Call now."
page = head(title, desc, f"{BASE_URL}/", "", biz_schema()+faq_schema(home_faq))
page += header_nav()
page += f"""
<div class="hero"><div class="wrap">
  <p class="eyebrow">Same-day service &middot; 7 days &middot; Free quotes</p>
  <h1 class="display">Rubbish.<br><span class="hl">Gone today.</span></h1>
  <p class="lede">We turn up, quote on the spot, load everything ourselves and sweep up after. Furniture, green waste, whole houses — if it's junk to you, it's a job for us.</p>
  <div class="hero-ctas"><a class="btn-big" href="{PHONE_A}">Call {PHONE}</a><a class="btn-ghost" href="locations/index.html">Find your suburb</a></div>
</div></div>
<section id="what-we-take"><div class="wrap">
  <span class="sec-label">The manifest</span>
  <h2 class="display">What we take</h2>
  <p class="sub">If two people can carry it, it goes on the truck. Here's what's on almost every load:</p>
  {manifest()}
</div></section>
<div class="tape" aria-hidden="true"></div>
<section id="quote"><div class="wrap">
  <div class="form-split">
    <div>
      <span class="sec-label">Free quote</span>
      <h2 class="display">Tell us what's got to go</h2>
      <p class="sub">Fill in the form or call us — either way you'll get a fast, free, no-obligation quote. The price we confirm on site is the price you pay, tip fees and all the lifting included.</p>
      <a class="btn-big" href="{PHONE_A}">Call {PHONE}</a>
    </div>
    {quote_form()}
  </div>
</div></section>
<section style="background:var(--white)"><div class="wrap">
  <span class="sec-label">How it works</span>
  <h2 class="display">Three steps. Zero lifting.</h2>
  {steps()}
</div></section>
<section><div class="wrap">
  <span class="sec-label">Service areas</span>
  <h2 class="display">Where we work</h2>
  <p class="sub">Crews in every major city. Find your suburb for local details:</p>"""
for city in CITIES:
    subs = [s for s in SUBURBS if s["c"]==city]
    links = "".join(f'<a href="locations/{s["slug"]}.html">{s["n"]}</a>' for s in subs)
    page += f'<div class="city-block"><h3>{city}</h3><div class="area-grid">{links}</div></div>'
page += f"""</div></section>
<section style="background:var(--white)"><div class="wrap">
  <span class="sec-label">Questions</span>
  <h2 class="display">Before you call</h2>
  {faq_html(home_faq)}
</div></section>"""
page += footer_block()
with open(f"{OUT}/index.html","w") as f: f.write(page)

# ---- Locations index ----
title = f"Service Areas | Rubbish Removal in 50+ Australian Suburbs | {BIZ}"
desc = "Find same-day rubbish removal in your suburb. Local crews across Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, Canberra, Hobart & Newcastle."
page = head(title, desc, f"{BASE_URL}/locations/", "../", biz_schema())
page += header_nav("../")
page += """<section><div class="wrap">
  <span class="sec-label">Service areas</span>
  <h2 class="display">Pick your suburb</h2>
  <p class="sub">Every area below has same-day crews, local tip knowledge and free on-site quotes.</p>"""
for city in CITIES:
    subs = [s for s in SUBURBS if s["c"]==city]
    links = "".join(f'<a href="{s["slug"]}.html">{s["n"]} {s["p"]}</a>' for s in subs)
    page += f'<div class="city-block"><h3>{city}</h3><div class="area-grid">{links}</div></div>'
page += "</div></section>"
page += footer_block("../")
with open(f"{OUT}/locations/index.html","w") as f: f.write(page)

# ---- Suburb pages ----
for sb in SUBURBS:
    same_city = [s for s in SUBURBS if s["c"]==sb["c"] and s["n"]!=sb["n"]][:6]
    if len(same_city) < 3:
        same_city += [s for s in SUBURBS if s["s"]==sb["s"] and s["n"]!=sb["n"] and s not in same_city][:3]
    sfaq = [
     (f"How much does rubbish removal cost in {sb['n']}?", f"Every {sb['n']} job is different, so we quote each one individually — send a photo or fill in the enquiry form for a fast free quote. The price we confirm on site is fixed before we load anything, and it includes all labour and tip fees."),
     (f"Can you do same-day pickup in {sb['n']}?", f"Usually, yes. Call before 10am and we can typically have a crew in {sb['n']} the same afternoon. Otherwise it's next-day at the latest."),
     (f"What do you take in {sb['n']}?", f"Furniture, mattresses, whitegoods, green waste, renovation debris, e-waste and full house or office clearances. The only things we can't carry are asbestos, chemicals, wet paint and gas bottles."),
     ("Where does it all go?", "We sort every load — usable items to charity, metal and e-waste to recyclers, green waste to mulching. Landfill is the last resort, not the first."),
    ]
    jl = ", ".join(sb["jobs"][:-1]) + " and " + sb["jobs"][-1].lower()
    title = f"Rubbish Removal {sb['n']} {sb['s']} {sb['p']} | Same-Day Junk Pickup | {BIZ}"
    desc = f"Same-day rubbish removal in {sb['n']} {sb['p']}. {sb['jobs'][0]}, {sb['jobs'][1].lower()} & more. We load, sweep & recycle. Free quotes — call {PHONE}."
    canonical = f"{BASE_URL}/locations/{sb['slug']}.html"
    page = head(title, desc, canonical, "../", biz_schema(sb)+faq_schema(sfaq))
    page += header_nav("../")
    chips = "".join(f"<span>{j}</span>" for j in sb["jobs"])
    nearby = "".join(f'<li><a href="{s["slug"]}.html">Rubbish removal {s["n"]}</a></li>' for s in same_city)
    page += f"""
<div class="hero" style="padding:56px 0"><div class="wrap">
  <p class="eyebrow">{sb['c']} &middot; {sb['s']} {sb['p']} &middot; Same-day service</p>
  <h1 class="display" style="font-size:clamp(38px,6.5vw,76px)">Rubbish removal<br><span class="hl">{sb['n']}</span></h1>
  <p class="lede">{sb['note']}</p>
  <div class="jobs-chips">{chips}</div>
  <div class="hero-ctas" style="margin-top:30px"><a class="btn-big" href="{PHONE_A}">Call {PHONE}</a></div>
</div></div>
<section><div class="wrap"><div class="two-col">
  <div>
    <span class="sec-label">{sb['n']} jobs</span>
    <h2 class="display" style="font-size:clamp(26px,3.5vw,40px)">What we clear in {sb['n']}</h2>
    <p>Our {sb['c']} crew handles {jl} across {sb['n']} and the surrounding {sb['s']} suburbs — plus everything else on the standard manifest: furniture, mattresses, whitegoods, e-waste, green waste and renovation debris.</p>
    <p style="margin-top:14px">Every job works the same way: send a photo or book a free quote, we arrive and give you a fixed price on the spot, and if you're happy we start loading immediately. Your {sb['n']} junk is usually gone within hours of your call — loaded, swept up after, and sorted for recycling and charity before anything touches landfill.</p>
    <h2 class="display" style="font-size:clamp(24px,3vw,34px);margin-top:44px">Get a free quote in {sb['n']}</h2>
    <p class="sub" style="margin-bottom:22px">Tell us what needs to go and we'll come back fast with a free, no-obligation quote:</p>
    {quote_form(sb['n'])}
  </div>
  <aside class="side-card">
    <h3>Nearby areas we service</h3>
    <ul>{nearby}<li><a href="index.html">All service areas →</a></li></ul>
  </aside>
</div></div></section>
<section style="background:var(--white)"><div class="wrap">
  <span class="sec-label">Questions</span>
  <h2 class="display" style="font-size:clamp(24px,3vw,36px)">Rubbish removal in {sb['n']} — FAQs</h2>
  {faq_html(sfaq)}
</div></section>"""
    page += footer_block("../")
    with open(f"{OUT}/locations/{sb['slug']}.html","w") as f: f.write(page)

# ---- 404 ----
page = head(f"Page not found | {BIZ}", "That page has been taken to the tip. Head back to the homepage.", f"{BASE_URL}/404.html", "")
page += header_nav()
page += f"""<section style="text-align:center;padding:110px 24px"><h1 class="display" style="font-size:clamp(40px,7vw,80px)">This page went<br><span style="color:var(--green)">to the tip.</span></h1><p style="margin:20px 0 30px;color:var(--steel)">The junk's gone and so is this URL.</p><a class="btn-big" href="index.html">Back to homepage</a></section>"""
page += footer_block()
with open(f"{OUT}/404.html","w") as f: f.write(page)

# ---- sitemap.xml & robots.txt ----
urls = [f"{BASE_URL}/", f"{BASE_URL}/locations/"] + [f"{BASE_URL}/locations/{s['slug']}.html" for s in SUBURBS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls: sm += f"  <url><loc>{u}</loc><changefreq>monthly</changefreq></url>\n"
sm += "</urlset>\n"
with open(f"{OUT}/sitemap.xml","w") as f: f.write(sm)
with open(f"{OUT}/robots.txt","w") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")
# CNAME file — required by GitHub Pages for the custom domain; regenerating it here
# means it survives every rebuild/re-upload of the docs folder
with open(f"{OUT}/CNAME","w") as f: f.write("tiprun.homes\n")

print(f"Built {len(SUBURBS)} suburb pages + homepage, locations index, 404, sitemap, robots.txt into /{OUT}")
