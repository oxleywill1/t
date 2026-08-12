# -*- coding: utf-8 -*-
"""
Service x city pages for TipRun.
These target searches distinct from suburb pages: "mattress removal melbourne",
"office clearance sydney", "deceased estate clearance brisbane", etc.
Each combination gets its own intro so pages aren't templated duplicates.
"""

# Cities we write service pages for, with a short local framing per city.
SERVICE_CITIES = [
    dict(city="Sydney",     state="NSW", slug="sydney"),
    dict(city="Melbourne",  state="VIC", slug="melbourne"),
    dict(city="Brisbane",   state="QLD", slug="brisbane"),
    dict(city="Perth",      state="WA",  slug="perth"),
    dict(city="Adelaide",   state="SA",  slug="adelaide"),
    dict(city="Gold Coast", state="QLD", slug="gold-coast"),
    dict(city="Canberra",   state="ACT", slug="canberra"),
]

# Services. `intros` maps city slug -> a genuinely city-specific opening paragraph.
SERVICES = [

dict(slug="mattress-removal", name="Mattress removal",
 blurb="Old mattresses taken from anywhere in the property and sorted to a recycler rather than landfill.",
 points=["Single items or whole houses","Carried down from upstairs and units","Sorted to mattress recyclers","Bed bases and frames too"],
 body="""
<p>Mattresses are the single most awkward household item to get rid of. They don't fit in a bin, most councils limit how many they'll take in a hard waste collection, and transfer stations charge a per-mattress fee on top of the trip. They're also among the most dumped items in Australia, which is why councils have tightened enforcement.</p>
<p>We take mattresses of any size and condition, from single items to whole-property clearances, and we do the carrying — including from upstairs bedrooms, walk-up flats and units with lift access to arrange. Bed bases, ensembles and frames go on the same load.</p>
<h2>What happens to them</h2>
<p>A typical mattress is around 75 to 90 percent recoverable by weight. Steel springs go to scrap metal, foam is reprocessed into carpet underlay and matting, timber goes to chip, and textiles become industrial felt. We sort mattresses to recyclers wherever the pathway exists rather than sending them straight to landfill.</p>
<h2>Before we arrive</h2>
<p>Keep the mattress dry if you can — a rain-soaked mattress often can't be recycled. If there's any bed bug history, tell us and seal it in plastic first so it isn't carried through the building uncovered.</p>
""",
 intros=dict(
  sydney="From walk-up flats in the eastern suburbs to family homes out west, Sydney mattress pickups are mostly a carrying job — stairs, tight terrace hallways and units without lifts. We handle all of it.",
  melbourne="Melbourne's mix of Victorian terraces, walk-up blocks and outer-suburb family homes means every mattress job is different. Narrow hallways and no rear access are routine for us.",
  brisbane="Queenslanders with steep stairs and under-house storage make Brisbane mattress removals a two-person job more often than not. We bring the crew rather than asking you to drag it to the kerb.",
  perth="Perth mattress pickups run from beachside apartments in Scarborough to big family homes in the northern corridor — single items or a full house of them.",
  adelaide="Adelaide villas with narrow side access and bay-side unit blocks are our common mattress jobs. Everything comes out through the front with floors protected.",
  **{"gold-coast":"Holiday apartments and rental turnovers keep Gold Coast mattress removals busy year-round — we coordinate lift bookings with building managers so cleanouts don't stall."},
  canberra="Canberra's bulky waste rules are strict and mattresses are limited in kerbside collections. We take what the council collection won't, on your timing.",
 )),

dict(slug="furniture-removal", name="Furniture removal",
 blurb="Lounges, wardrobes, dining settings and everything else too big for a bin — donated where usable.",
 points=["Single pieces or full households","Dismantling where needed","Charity donation of usable items","Stairs and tight access no problem"],
 body="""
<p>Furniture takes up more landfill volume than almost any other household item, and a lot of what's thrown out is still perfectly usable. Our approach is to sort as we load: anything genuinely saleable goes to charity, timber is separated where it can be recovered, and only the finished items go as residual.</p>
<p>We take lounges and modulars, wardrobes, chests of drawers, dining tables and chairs, bed frames, bookshelves, desks, outdoor settings and everything in between. Where something won't fit through a doorway, we dismantle it rather than leaving it with you.</p>
<h2>Worth donating instead?</h2>
<p>If a piece is clean, structurally sound and something you'd accept into your own home, a charity may well take it — and that's a better outcome than any removal. Phone them first and describe it honestly. Where an item won't pass that test, we'll take it and sort it properly.</p>
<h2>What we can't take</h2>
<p>We handle furniture of any kind, but not the hazardous material that often sits alongside it in a garage — paint, chemicals, gas bottles and the like. We'll point you to the right free program for those.</p>
""",
 intros=dict(
  sydney="Sydney terraces with no rear access, apartment blocks needing lift bookings, and big Hills District homes being downsized — furniture removal here is mostly about access, and we work all three.",
  melbourne="From Richmond worker's cottages to Glen Waverley family homes being cleared before a knock-down rebuild, Melbourne furniture jobs range from a single couch to an entire household.",
  brisbane="Multi-level Queenslanders and steep western-suburbs blocks make Brisbane furniture removals a stairs job. Our crew carries everything up or down so you don't have to.",
  perth="Perth furniture pickups run from Fremantle's tight heritage cottages to big Joondalup family homes — single pieces, downsizing clearances and everything between.",
  adelaide="Adelaide's bluestone villas have narrow side access, so furniture comes through the front with floor protection down. Bay-side units we handle with lift access arranged.",
  **{"gold-coast":"Canal-front homes, high-rise units and holiday apartments — Gold Coast furniture removal usually means coordinating building access before we arrive."},
  canberra="Downsizing from a Woden Valley or Belconnen family home is our most common Canberra furniture job — respectful, room by room, with usable pieces donated locally.",
 )),

dict(slug="deceased-estate-clearance", name="Deceased estate clearance",
 blurb="Careful, respectful whole-property clearances for executors and families, with valuables and documents set aside.",
 points=["Documents and valuables set aside, not binned","Room-by-room, at your pace","Before and after photos for estate records","Donation-first sorting"],
 body="""
<p>Clearing a deceased person's home is difficult practical work arriving at a difficult time, often under pressure from a settlement date or a solicitor's timeline. We work carefully rather than fast.</p>
<h2>How we approach it</h2>
<p>Nothing gets bulk-loaded without a look. Paperwork, photographs, jewellery boxes, tins and drawers are set aside for you to go through rather than binned — wills, deeds, share certificates and cash turn up in unlikely places in older homes, and once a house is cleared they're gone.</p>
<p>We work room by room, and we're comfortable taking direction from an executor, a family member or a solicitor. Where beneficiaries are spread across the country, we provide before and after photographs so there's a record of what was there.</p>
<h2>Before you book</h2>
<p>Establish who has authority to deal with the estate's property, and don't rush the sentimental sorting — families rarely regret taking longer, and frequently regret speed. Our guide on clearing a deceased estate covers the full sequence, including what to search for before anything is moved.</p>
<h2>What needs separate handling</h2>
<p>Older properties commonly contain paint, chemicals, old fuel, gas bottles, medications and sometimes firearms, all of which need their own route. Fibro sheeting and eaves in pre-1990 homes may contain asbestos, which requires a licensed removalist. We'll identify these rather than loading them.</p>
""",
 intros=dict(
  sydney="Executors dealing with a Sydney estate are often interstate, working to a settlement date on a property they can't visit. We work from video walk-throughs and send photographs at every stage.",
  melbourne="Melbourne estate clearances often involve long-held family homes in the eastern and northern suburbs — decades of belongings, and a search that can't be rushed.",
  brisbane="Brisbane Queenslanders hold a lifetime under the house as well as in it. Estate clearances here almost always turn up more volume than the walk-through suggested.",
  perth="Perth estate work often comes with FIFO-era family spread across the state or interstate. We photograph as we go so everyone can see what was there.",
  adelaide="Adelaide's long-held villas and bay-side units are our common estate jobs — careful searching, donation-first sorting, and a documented process for the executor.",
  **{"gold-coast":"Gold Coast estates are frequently held by families living elsewhere, so we work remotely by default: video walk-through, written quote, photographs throughout."},
  canberra="Canberra estate clearances often involve a garaged older car, decades of paperwork and a family home held since the suburb was built. We take the search seriously.",
 )),

dict(slug="office-clearance", name="Office & commercial clearance",
 blurb="Strip-outs, make-good clearances and office furniture removal, worked around your trading hours.",
 points=["After-hours and weekend access","E-waste sorted to licensed recyclers","Furniture offered to charities first","Disposal dockets for your records"],
 body="""
<p>Commercial clearances have constraints residential ones don't: lease make-good obligations, building access rules, data security, and work that usually can't disrupt trading.</p>
<h2>Make-good</h2>
<p>Most commercial leases require the premises returned to a defined condition. What that means varies enormously between leases, so read the clause before scoping the job — the cost difference between interpretations can be substantial, and make-good is one of the most commonly disputed parts of a commercial tenancy.</p>
<h2>Data and equipment</h2>
<p>Computers, servers, phones and photocopiers all hold data, and photocopiers in particular are routinely overlooked. Handle destruction or drive removal before equipment leaves the building. We sort e-waste to licensed recyclers and can provide disposal dockets for your records.</p>
<h2>Furniture</h2>
<p>Used office furniture has thin resale value, but charities, schools, community groups and social enterprises will often take good desks and chairs. Start those conversations weeks ahead — nobody collects furniture at two days' notice. Whatever isn't placed, we clear.</p>
<h2>Access</h2>
<p>Most buildings restrict removals to after hours or weekends and require dock bookings, contractor insurance certificates and sometimes inductions. Tell us early; it's usually the constraint that sets the schedule.</p>
""",
 intros=dict(
  sydney="Sydney CBD and North Sydney towers mean dock bookings, after-hours windows and lift protection. We do Chatswood and Parramatta office strip-outs the same way — outside trading hours, in and out.",
  melbourne="From Dandenong warehouses to CBD tenancies and Brunswick shopfronts, Melbourne commercial clearances run the full range. Pallets, partitions, workstations and fit-out debris.",
  brisbane="Fortitude Valley venues and offices book us for pre-dawn clearances so they never close. Chermside and Southside commercial work runs to the same after-hours pattern.",
  perth="Perth commercial jobs are often Cannington and Midland workshops and warehouses — machinery, shelving, scrap and office furniture in the same clearance.",
  adelaide="Port Adelaide warehouses and city tenancies make up most of our Adelaide commercial work, from single-office strip-outs to full industrial site clearances.",
  **{"gold-coast":"Southport offices and Surfers hospitality fit-outs are our common Gold Coast commercial jobs, always worked around trading and check-in times."},
  canberra="Canberra office clearances often involve government or professional tenancies with strict security and documentation requirements. We work to them.",
 )),

dict(slug="hoarding-cleanup", name="Hoarding clean-ups",
 blurb="Staged, respectful clearances of heavily accumulated properties, with careful searching for valuables and documents.",
 points=["Safety assessment before we start","Staged, not a single-day blitz","Careful searching for cash and documents","Discreet, unmarked where you prefer"],
 body="""
<p>Hoarding clean-ups need a different approach from ordinary cleanouts. The practical challenges are real — volume, hazards, access — but the human ones matter more, and getting that part wrong tends to undo the work.</p>
<h2>How we work</h2>
<p>Safety assessment first. Heavily accumulated properties commonly involve structural loading on floors, blocked exits, vermin and insect activity, mould, rotting material and buried chemicals or gas bottles. We assess before anyone starts, and we bring appropriate protection.</p>
<p>Then we work in stages rather than attempting to clear everything in a day: create access and a sorting space, remove the clearly hazardous and rotting material, sort systematically, and search carefully. Cash, jewellery, documents and irreplaceable photographs are routinely found deep in hoarded material, and anything paper-based gets checked before disposal.</p>
<h2>Where the person is still living there</h2>
<p>Hoarding disorder is a recognised mental health condition, and forced clear-outs conducted without the person's involvement frequently result in rapid re-accumulation. Where the resident is present, we work at their pace and with their agreement. It takes longer and the outcome lasts.</p>
<h2>Expect volume</h2>
<p>Hoarded properties generate far more material than a walk-through suggests — commonly multiple full truck loads from a single house. We quote realistically rather than optimistically.</p>
""",
 intros=dict(
  sydney="Sydney hoarding jobs range from eastern suburbs flats to full houses out west. Access is often the first problem — we work discreetly and, where you'd prefer, without signage.",
  melbourne="St Kilda rooming houses and northern-suburbs family homes make up much of our Melbourne hoarding work. Discreet, staged, and paced to the situation.",
  brisbane="Brisbane hoarding clean-ups often involve under-house accumulation as well as the house itself, plus humidity-driven mould that needs proper protection.",
  perth="Perth hoarding work frequently comes through family or support services rather than the resident directly. We're comfortable working alongside case workers.",
  adelaide="Adelaide hoarding clearances are usually long-held properties where accumulation built up over decades. We search carefully rather than clearing fast.",
  **{"gold-coast":"Gold Coast hoarding jobs often involve unit blocks, which adds strata coordination and lift access to an already sensitive job. We handle both."},
  canberra="Canberra hoarding clean-ups often come with strict property and tenancy requirements. We document as we go and work to whatever process applies.",
 )),

dict(slug="green-waste-removal", name="Green waste removal",
 blurb="Branches, clippings, hedges and whole-yard clean-ups, separated for mulching rather than landfill.",
 points=["Whole-yard clean-ups","Separated for mulching","Storm and fire-season clearing","Soil, pots and timber sorted out"],
 body="""
<p>Garden waste is heavy, seasonal and almost entirely recoverable — which is why we keep it separate. Clean green waste goes to mulching and composting rather than landfill, and separating it also keeps disposal costs down.</p>
<p>We take prunings, hedge and tree cuttings, branches, grass clippings, weeds, palm fronds, old turf and whole-yard clean-ups. What we sort out of the load: plastic plant pots, soil and rock, and treated or painted timber, all of which contaminate a green load.</p>
<h2>Consider mulching on site first</h2>
<p>The cheapest option is often not removing it. Chipped prunings make excellent mulch, suppress weeds and hold moisture, and chipper hire is inexpensive for a day. If you've had a tree job done, arborists will frequently leave chip on site free. Where the volume is beyond that, we'll take it.</p>
<h2>A note on burning</h2>
<p>Rules on burning garden waste are stricter than most people assume — prohibited outright in most metropolitan areas, and permit-only with seasonal restrictions in many regional ones. Check with your council and fire authority before lighting anything.</p>
""",
 intros=dict(
  sydney="Gum trees over every driveway means Sydney green waste is constant — leaf drop, bark, sap-stained branches and the annual pre-summer clean-up around the Shire and northern suburbs.",
  melbourne="Melbourne yards produce green waste in bursts: spring prunings, summer hedge work and autumn leaf fall. Outer-suburb blocks generate more than a green bin can handle.",
  brisbane="Brisbane's growing season never really stops, and storm season brings down branches by the trailer load. We clear whole yards and post-storm debris.",
  perth="Perth green waste is dominated by summer prep — clearing dry material and overhanging growth before fire season, plus the usual hedge and lawn volume.",
  adelaide="Adelaide blocks in the northern and southern suburbs run to big yards and long driveways, which means green waste in volumes a fortnightly bin won't cover.",
  **{"gold-coast":"Gold Coast growth is relentless and storm season adds to it. Canal-front and hinterland properties both generate green waste faster than kerbside collection handles."},
  canberra="Canberra's established gardens drop heavily in autumn, and pre-fire-season clearing is a genuine safety job rather than a tidy-up. We do both.",
 )),

dict(slug="whitegoods-and-appliance-removal", name="Whitegoods & appliance removal",
 blurb="Fridges, freezers, washers and dryers taken from wherever they sit, degassed and recycled properly.",
 points=["Fridges and freezers degassed properly","Carried from upstairs and laundries","Scrap metal recovery","Doors removed for safety"],
 body="""
<p>Whitegoods are heavy, awkward and — in the case of anything with a refrigeration circuit — subject to environmental handling requirements. We take fridges, freezers, washing machines, dryers, dishwashers, ovens, cooktops and air conditioners.</p>
<h2>The degassing requirement</h2>
<p>Fridges, freezers and air conditioners contain refrigerant gases that are potent greenhouse gases and, in older units, ozone-depleting. Australian law restricts their handling and release, which means these units need to reach a facility equipped to degas them before dismantling — not a backyard or a general tip face.</p>
<h2>The safety step</h2>
<p>Remove the door, or secure it open, on any fridge or freezer left unattended even briefly. Children have died in disused fridges, which is why most councils refuse to collect one with an intact door. If yours is waiting for us, do this first.</p>
<h2>If it still works</h2>
<p>A working appliance under about ten years old has real value. Charities accept working whitegoods in genuinely serviceable condition, and washing machines and fridges in good order sell readily. Worth trying before disposal.</p>
<h2>Moving them safely</h2>
<p>Whitegoods cause a lot of back injuries and crushed fingers. Don't attempt stairs alone — that's what we're for.</p>
""",
 intros=dict(
  sydney="Sydney apartment laundries and walk-up flats mean whitegoods have to be carried, often down several flights. We bring trolleys and the crew to do it safely.",
  melbourne="Melbourne rental turnovers and kitchen renovations produce most of our whitegoods jobs — old fridges, failed washers and ovens pulled out mid-reno.",
  brisbane="Brisbane humidity and heat retire appliances early, and under-house laundries add a stairs problem. We handle both.",
  perth="Perth whitegoods pickups often come from northern-corridor family homes and coastal units where salt air has finished off an older machine.",
  adelaide="Adelaide whitegoods jobs run from single-appliance pickups in bay-side units to full kitchen strip-outs in the eastern suburbs.",
  **{"gold-coast":"Gold Coast holiday apartments turn over appliances constantly, and lift access needs booking. We coordinate with building managers before arriving."},
  canberra="Canberra kerbside collections limit appliances and require doors removed. We take what the council won't, whenever suits you.",
 )),

dict(slug="renovation-waste-removal", name="Renovation & builders waste",
 blurb="Strip-out debris, plasterboard, timber, tiles and rubble cleared fast so trades can keep moving.",
 points=["Same-day strip-out clearances","Materials separated for recovery","Site tidy-ups between trades","We can't take asbestos — see below"],
 body="""
<p>Renovation waste appears fast and in volume. A single bathroom strip-out fills more than people estimate, because rubble doesn't stack. We clear sites between trades so work isn't held up by a pile in the driveway.</p>
<p>We take plasterboard, timber, tiles, concrete and brick rubble, old kitchens and bathroom fittings, carpet and underlay, roofing, fencing, packaging and general site waste.</p>
<h2>Separation saves money</h2>
<p>Mixed loads cost more than separated ones because contaminated material can't be recovered. Where there's space, keep clean concrete and brick, scrap metal, untreated timber and plasterboard in separate piles — the difference in disposal cost is real.</p>
<h2>Asbestos: check before you demolish</h2>
<p>Any Australian home built or renovated before 1990 may contain asbestos — in fibro sheeting, eaves, bathroom linings, vinyl backing and fencing. It cannot go in a bin, a skip or on our truck. If you're renovating a pre-1990 property, have it assessed before demolition and engage a licensed removalist if it's present. This derails more renovation timelines than anything else, and doing it wrong carries serious consequences.</p>
<h2>Salvage first where you can</h2>
<p>Architectural recyclers and building reuse centres take doors, windows, timber, bricks and quality fittings. Careful demolition recovers material with genuine value and reduces the volume you're paying to remove.</p>
""",
 intros=dict(
  sydney="Sydney renovations run hot across the inner west and north shore, and access is usually the problem — terrace frontages, no rear lane, and a skip that won't fit. We load from the street.",
  melbourne="Melbourne's inner-west and eastern-suburbs renovation boom keeps us clearing plaster, timber and old fittings from Victorian and Edwardian homes weekly.",
  brisbane="Brisbane post-war homes and Queenslanders being renovated produce constant strip-out volume, often with under-house material to clear at the same time.",
  perth="Perth renovation clearances range from Fremantle heritage cottages needing careful access to big northern-suburb rebuilds generating multiple loads.",
  adelaide="Adelaide's bluestone and villa renovations mean narrow access and heavy rubble. We work with what the site allows rather than needing a skip footprint.",
  **{"gold-coast":"Gold Coast unit renovations bring strata rules, lift bookings and restricted hours. We plan the disposal route with building management first."},
  canberra="Canberra renovations often run to tight seasonal windows before winter. We clear between trades so the schedule holds.",
 )),
]
