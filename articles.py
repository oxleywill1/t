# -*- coding: utf-8 -*-
"""
Article library for TipRun. Each article is a dict:
  slug, title (page <title>), h1, cat (category), mins, excerpt, desc (meta), body (HTML)
Add more by appending to ARTICLES — generate.py builds the pages and hub automatically.
"""

CATEGORIES = [
    ("costs",     "Costs &amp; pricing",   "What things cost, what drives the price, and how to compare quotes."),
    ("council",   "Council &amp; rules",   "Kerbside collections, what councils accept, and the rules on dumping."),
    ("disposal",  "Disposing of things",   "Item-by-item guides for the things bins won't take."),
    ("situations","Big cleanouts",         "Deceased estates, hoarding, end of lease, moving and renovating."),
    ("agents",    "For agents &amp; landlords", "Tenancy law, abandoned goods and property turnarounds."),
]

ARTICLES = [

# ---------------- COSTS ----------------
dict(slug="rubbish-removal-cost-australia", cat="costs", mins=8,
 title="How Much Does Rubbish Removal Cost in Australia?",
 h1="How much does rubbish removal cost in Australia?",
 desc="What drives rubbish removal pricing in Australia, how volume-based quotes work, and the questions to ask before you book.",
 excerpt="Understand how volume pricing works, what pushes a quote up, and how to compare operators fairly.",
 body="""
<p>Rubbish removal in Australia is almost always priced on <strong>volume</strong> — how much space your load takes up on the truck — rather than by the hour or by weight. Understanding that one fact makes every quote you receive easier to read.</p>

<h2>Why volume, not weight or time</h2>
<p>Transfer stations charge operators by the tonne, but customers find weight impossible to estimate. Volume is something you can see. Most operators describe loads as a fraction of a truck: a quarter load, a half load, three-quarters, or a full truck. A quarter load is usually described as roughly a ute tray — a couch, a fridge and a few bags.</p>
<p>Hourly pricing exists but is less common, and it works against you when access is difficult. If your job involves stairs, a long carry or a tight driveway, an hourly operator has no incentive to hurry. A fixed volume quote puts that risk on them.</p>

<h2>What actually moves the price</h2>
<ul>
<li><strong>Volume.</strong> The single biggest factor. Bulky-but-light items like mattresses, lounges and trampolines cost more than their weight suggests because they eat truck space.</li>
<li><strong>Disposal fees.</strong> Transfer station gate fees vary significantly between councils and states, and certain items attract surcharges — mattresses and tyres in particular.</li>
<li><strong>Access.</strong> Ground floor with a driveway is cheapest. Stairs, apartment lifts, long carries from a back yard, or street parking with no loading zone all add labour time.</li>
<li><strong>Sorting.</strong> A load that's already sorted, or that's all one material, is faster to process than a mixed pile that needs separating at the tip.</li>
<li><strong>Problem items.</strong> Anything requiring special handling — degassing a fridge, e-waste, tyres — is often quoted separately.</li>
<li><strong>Timing.</strong> Same-day and weekend work sometimes carries a premium.</li>
</ul>

<h2>What should be included</h2>
<p>A quote worth taking seriously includes labour, loading, transport and tip fees in one number. Be alert to operators who quote a low headline figure and then add disposal costs afterwards — the gap between the two can be substantial.</p>
<p>You should not be asked to move anything to the kerb. Part of what you're paying for is that the crew does the lifting from wherever the items sit.</p>

<h2>Getting an accurate quote</h2>
<p>Photos are the fastest route to an accurate price. A couple of phone photos showing the pile and the access route lets an operator quote confidently without a site visit. Be honest about scale — a quote based on an optimistic description gets revised upward on the day, which is how disputes start.</p>
<p>Ask three questions before booking: is the price fixed or an estimate, are tip fees included, and what happens if the load turns out larger than described. Clear answers to those three tell you a lot about who you're dealing with.</p>

<h2>When a skip bin is the better option</h2>
<p>If you're working through a project over several days — a renovation, a slow garage cleanout — a skip you fill yourself can work out cheaper, provided you're able to do the lifting and have somewhere legal to put it. For a single pile that needs to be gone today, a removal service is usually faster and involves no permits.</p>
"""),

dict(slug="skip-bin-vs-rubbish-removal", cat="costs", mins=7,
 title="Skip Bin or Rubbish Removal Service: Which Should You Choose?",
 h1="Skip bin or rubbish removal service?",
 desc="A practical comparison of hiring a skip bin versus booking a rubbish removal crew — cost, effort, permits and which suits which job.",
 excerpt="Both clear the same rubbish. The right choice depends on time, access, permits and who's doing the lifting.",
 body="""
<p>Both options end with your rubbish gone. The difference is who does the work, how long you have, and whether you need council permission.</p>

<h2>The core trade-off</h2>
<p>A skip bin is a container dropped at your property for a set period — typically three to seven days. You fill it yourself. A rubbish removal service sends a crew and a truck; they load everything and leave the same day.</p>
<p>Skips generally cost less per cubic metre. Removal services cost more per cubic metre but include all the labour. Which is cheaper overall depends entirely on how you value your own time and whether you're physically able to do the loading.</p>

<h2>When a skip bin makes sense</h2>
<ul>
<li>You're working across several days — a renovation, a gradual declutter, a landscaping project.</li>
<li>The waste is being generated progressively rather than sitting in one pile.</li>
<li>You have off-street space to put it, ideally a driveway.</li>
<li>You're fit enough to lift everything, and you have help for the heavy items.</li>
<li>The material is uniform — all soil, all bricks, all green waste — which usually attracts cheaper rates.</li>
</ul>

<h2>When a removal service makes sense</h2>
<ul>
<li>The rubbish already exists as a pile and you want it gone today.</li>
<li>There's no legal or practical place to put a skip.</li>
<li>Stairs, apartments or difficult access are involved.</li>
<li>You physically can't or shouldn't be lifting heavy items.</li>
<li>You're on a deadline — settlement, end of lease, an inspection.</li>
<li>The load contains items needing sorting for recycling, donation or special disposal.</li>
</ul>

<h2>The permit question</h2>
<p>If a skip needs to sit on the road, nature strip or footpath rather than on your own property, most Australian councils require a permit. Application times, conditions and fees vary widely, and permits are usually the responsibility of the person hiring the bin, not the bin company. Check with your local council early — this catches people out regularly and can add days to a job.</p>

<h2>What skips won't take</h2>
<p>Skip bin operators have restrictions, and breaching them attracts contamination charges. Commonly prohibited: asbestos, liquid paint, chemicals, gas bottles, batteries, tyres and food waste. Some also restrict mattresses and whitegoods or charge extra for them. Removal services have similar restrictions on hazardous material but can usually take the awkward bulky items a skip won't.</p>

<h2>A middle path</h2>
<p>For larger projects, some people use both — a skip for the bulk of the renovation debris they generate over a week, then a removal crew at the end for the heavy or awkward items they couldn't lift into it. There's no rule saying you must choose one.</p>
"""),

# ---------------- COUNCIL ----------------
dict(slug="hard-rubbish-collection-australia", cat="council", mins=8,
 title="Council Hard Rubbish Collection: How It Works in Australia",
 h1="Council hard rubbish collection: how it actually works",
 desc="How council hard waste and kerbside bulky collections work across Australia, what's usually accepted, and what to do when you need more than they'll take.",
 excerpt="Booked collections, scheduled sweeps, item limits and the rules that vary street by street.",
 body="""
<p>Nearly every Australian council offers some form of hard rubbish or bulky waste collection. The systems differ enough between councils that assuming your old suburb's rules apply in your new one is a reliable way to get a notice.</p>

<h2>The two main models</h2>
<p><strong>Booked collections</strong> are the most common now. You contact the council, book a date, and place items out the night before. Most councils allow one or two free bookings per household per year, with additional collections charged.</p>
<p><strong>Scheduled area sweeps</strong> still operate in some council areas — the truck comes through your zone on a set date and everyone puts material out in a defined window. These are becoming less common because they generate scavenging, mess and illegal dumping.</p>

<h2>What's generally accepted</h2>
<p>Most councils take furniture, mattresses, whitegoods with doors removed, general bulky household items, and often a limited volume of timber or metal. Green waste is frequently a separate collection with its own rules.</p>

<h2>What's generally refused</h2>
<p>Common exclusions across councils: building and renovation waste, soil, bricks, concrete, tyres, car parts, asbestos, chemicals, paint, gas bottles, and commercial quantities of anything. Councils are also strict about volume — a typical limit is around two to three cubic metres, roughly a small trailer load.</p>

<h2>The rules that catch people out</h2>
<ul>
<li><strong>Timing windows.</strong> Placing material out too early is an offence in many council areas. The standard requirement is no more than 24 to 48 hours before collection.</li>
<li><strong>Placement.</strong> Items must sit on the nature strip clear of the footpath, driveways, drains, power poles and street trees.</li>
<li><strong>Separation.</strong> Many councils now require material sorted into piles — metal, mattresses, general — and may skip loads that aren't.</li>
<li><strong>Renters and unit blocks.</strong> Apartment buildings often have entirely different arrangements through the body corporate. Check before putting anything out.</li>
</ul>

<h2>What happens if you get it wrong</h2>
<p>Material placed out at the wrong time, in the wrong place, or in excess of limits can be classified as illegal dumping. Councils increasingly issue infringements for this, and the fines are meaningful — often several hundred dollars for a household, and considerably more for repeat or commercial offences. Enforcement varies by council but has tightened significantly in recent years.</p>

<h2>When council collection isn't enough</h2>
<p>The common scenarios: you've already used your free bookings, the wait for a booking date is weeks and you have a deadline, your volume exceeds the limit, or your material is on the excluded list. In those cases a private removal service takes what the council won't, on your timeline rather than theirs.</p>
<p>Always check your own council's current rules directly — they're published on every council website and they do change.</p>
"""),

dict(slug="illegal-dumping-australia", cat="council", mins=7,
 title="Illegal Dumping in Australia: The Rules and the Risks",
 h1="Illegal dumping: what counts, and what it costs",
 desc="What legally counts as illegal dumping in Australia, how councils and EPAs enforce it, and how to avoid liability when you pay someone else to take your rubbish.",
 excerpt="Including the part most people miss — you can be liable for rubbish you paid someone else to remove.",
 body="""
<p>Illegal dumping is one of the most heavily enforced waste offences in Australia, and the penalties have increased substantially over the past decade. It's also an area where people become liable without realising it.</p>

<h2>What counts</h2>
<p>Illegal dumping covers depositing waste anywhere it isn't lawfully permitted. That includes obvious cases like leaving material on vacant land, in bushland, in a laneway or beside a charity bin. It also includes less obvious ones: putting hard rubbish out well outside your council's collection window, exceeding kerbside volume limits, using someone else's bins without permission, and leaving items beside a public bin because it's full.</p>

<h2>Who enforces it</h2>
<p>Councils handle most residential matters through infringement notices. State environment protection authorities handle larger and commercial matters, and their penalties are dramatically higher — particularly for anything involving asbestos or hazardous material. Surveillance cameras at known dumping hotspots are now routine, and material is regularly searched for documents identifying the source.</p>

<h2>The liability trap</h2>
<p>This is the part worth understanding properly. In most Australian jurisdictions, the person who generated the waste can be held responsible for its ultimate disposal — not only whoever physically dumped it. If you hire a cheap operator who takes your load and tips it in bushland, and something in that load identifies you, you can face enforcement action.</p>
<p>This is why the cheapest quote is sometimes the most expensive outcome. An operator charging well below the market rate may not be paying transfer station fees at all, and their savings are your risk.</p>

<h2>Protecting yourself</h2>
<ul>
<li>Ask where the material is going. A legitimate operator will name the transfer station or facility without hesitation.</li>
<li>Ask whether they can provide a disposal receipt or docket. For business, estate or strata work, request one as standard.</li>
<li>Check for a real business presence — ABN, insurance, a traceable address.</li>
<li>Be sceptical of quotes far below everyone else's. Tip fees are a large fixed cost that nobody can avoid legitimately.</li>
<li>Remove personal documents from anything you're disposing of, regardless of who takes it.</li>
</ul>

<h2>Asbestos deserves separate mention</h2>
<p>Illegally dumping asbestos attracts the most severe penalties in the waste system, and for good reason. It cannot go in general rubbish, cannot go in a skip, and cannot be handled by a general rubbish removal service. It requires a licensed asbestos removalist and disposal at a facility specifically licensed to receive it. If you suspect asbestos, stop and get it assessed before anything is moved.</p>
"""),

# ---------------- DISPOSAL ----------------
dict(slug="how-to-dispose-of-a-mattress", cat="disposal", mins=6,
 title="How to Dispose of a Mattress in Australia",
 h1="How to dispose of a mattress",
 desc="Your options for getting rid of an old mattress in Australia — council collection, recycling, retailer takeback and removal services.",
 excerpt="Mattresses are among the worst items for landfill and among the most recyclable. Here's how to do it properly.",
 body="""
<p>Mattresses are one of the most problematic items in Australian waste. They're bulky, they don't compact, they damage landfill machinery, and they're dumped illegally more often than almost anything else. They're also highly recyclable — a typical mattress is around 75 to 90 percent recoverable material.</p>

<h2>Your options, roughly in order of preference</h2>

<h3>1. Retailer takeback</h3>
<p>Most major bedding retailers will remove your old mattress when they deliver a new one, sometimes free and sometimes for a modest fee. If you're replacing rather than simply disposing, ask at the point of sale — it's the easiest path and the old mattress usually goes to a recycler.</p>

<h3>2. Dedicated mattress recycling</h3>
<p>Specialist recyclers operate in most Australian capitals. They strip the mattress into components: steel springs to scrap metal, foam into carpet underlay and gym matting, timber to mulch or particleboard, and textiles into industrial felt. Some accept drop-offs for a fee; some collect.</p>

<h3>3. Council hard rubbish</h3>
<p>Most councils accept mattresses in booked hard waste collections, though many limit the number per collection and some charge a surcharge. Check your council's rules before booking, and keep the mattress dry until collection — a rain-soaked mattress is often rejected because wet material can't be recycled.</p>

<h3>4. Transfer station drop-off</h3>
<p>You can take a mattress to a transfer station yourself. Nearly all charge a per-mattress fee, which reflects the genuine cost of processing it. Bring a way to secure it to your vehicle; loose mattresses on car roofs are both dangerous and illegal.</p>

<h3>5. Removal service</h3>
<p>Practical when you can't transport it, can't wait for a collection date, or have several to move at once. A reputable operator will take mattresses to a recycler rather than landfill.</p>

<h2>What not to do</h2>
<p>Don't leave it beside a charity bin or a public bin — that's illegal dumping and charities can't sell used mattresses regardless. Don't put it out weeks ahead of a collection date. Don't donate a mattress with any sign of bed bugs, staining or structural collapse; charities will refuse it and you'll have simply moved the problem.</p>

<h2>Bed bugs</h2>
<p>If the mattress has bed bugs, seal it in plastic before moving it and tell whoever handles it. Moving an infested mattress through a building uncovered spreads the problem to neighbours, and in shared buildings that becomes an expensive collective issue.</p>
"""),

dict(slug="how-to-dispose-of-fridges-whitegoods", cat="disposal", mins=7,
 title="How to Dispose of a Fridge, Freezer or Washing Machine",
 h1="Disposing of fridges, freezers and whitegoods",
 desc="How to get rid of old whitegoods in Australia — degassing requirements for fridges, scrap metal value, council collection and safety steps.",
 excerpt="Fridges and freezers have legal handling requirements that other appliances don't. Here's what's involved.",
 body="""
<p>Whitegoods are heavy, valuable as scrap, and — in the case of anything with a refrigeration circuit — subject to environmental handling requirements.</p>

<h2>Fridges and freezers: the degassing requirement</h2>
<p>Refrigerators, freezers and air conditioners contain refrigerant gases that are potent greenhouse gases and, in older units, ozone-depleting. Australian law restricts the handling and release of these gases. In practice this means a fridge should be degassed by someone appropriately licensed before it's dismantled or crushed.</p>
<p>You don't need to arrange this personally in most cases — transfer stations, scrap metal yards and legitimate removal operators handle degassing as part of their process. What matters is that the unit goes to somewhere equipped to do it, rather than being abandoned or broken up in a backyard.</p>

<h2>The safety step everyone forgets</h2>
<p>Remove the door, or at minimum remove the seal and secure the door open, on any fridge or freezer that will sit unattended even briefly. Children have died in disused fridges. Many councils will refuse to collect a fridge with an intact door, and this is why.</p>

<h2>Options for disposal</h2>
<ul>
<li><strong>Retailer takeback</strong> — most major appliance retailers will remove the old unit when delivering a replacement, often for a small fee.</li>
<li><strong>Scrap metal yards</strong> — whitegoods have genuine scrap value. Some yards pay for washing machines, dryers and dishwashers; fridges are often accepted free rather than paid for, because of the degassing cost.</li>
<li><strong>Council hard rubbish</strong> — widely accepted, with the door-removal rule enforced.</li>
<li><strong>Transfer station</strong> — accepted everywhere, sometimes free for scrap metal, sometimes with a fee for refrigerated units.</li>
<li><strong>Removal service</strong> — the practical choice for upstairs units, multiple appliances, or when you can't safely move something that heavy.</li>
</ul>

<h2>If it still works</h2>
<p>A working appliance under about ten years old has real value. Charities including major second-hand retailers accept working whitegoods, though most require them to be in genuinely serviceable condition and some won't take fridges at all. Selling privately is straightforward for washing machines and fridges in good order.</p>

<h2>Moving them safely</h2>
<p>Whitegoods regularly cause back injuries and crushed fingers. Use a trolley, keep the load low, and never attempt stairs alone. Fridges should be transported upright where possible; if laid down, they need to stand upright for several hours before being switched on again.</p>
"""),

dict(slug="e-waste-disposal-australia", cat="disposal", mins=7,
 title="E-Waste Disposal in Australia: TVs, Computers and Electronics",
 h1="E-waste: how to dispose of electronics properly",
 desc="Why e-waste is banned from landfill in parts of Australia, where to take old TVs, computers and batteries, and how to wipe data before disposal.",
 excerpt="Landfill bans, free drop-off schemes, battery fires, and the data you should erase first.",
 body="""
<p>Electronic waste is the fastest-growing waste stream in Australia, and the rules around it have tightened considerably. In Victoria, e-waste has been banned from landfill since 2019, and other jurisdictions have introduced their own restrictions and collection requirements. Regardless of where you live, throwing electronics in a general bin is the worst available option.</p>

<h2>Why it matters</h2>
<p>Electronics contain recoverable materials — gold, copper, aluminium, rare earths — alongside genuinely hazardous ones including lead, mercury and cadmium. In landfill the hazardous components leach; the valuable ones are lost. Recovery rates from proper e-waste recycling are high, and the material displaces newly mined resources.</p>

<h2>Where to take it</h2>
<ul>
<li><strong>Council e-waste drop-offs.</strong> Most councils run permanent e-waste points at transfer stations or periodic collection events, usually free for households.</li>
<li><strong>National TV and computer recycling.</strong> A co-regulatory scheme provides free drop-off points for televisions, computers, printers and peripherals in most population centres.</li>
<li><strong>Retailer takeback.</strong> Several major electronics and phone retailers accept old devices, batteries and small appliances in-store.</li>
<li><strong>Mobile phone recycling.</strong> A long-running industry scheme accepts phones, chargers, batteries and accessories through post and drop-off points.</li>
<li><strong>Removal services.</strong> Practical for office clear-outs or when you have volume — a legitimate operator sorts e-waste to a licensed recycler rather than landfill.</li>
</ul>

<h2>Batteries deserve their own paragraph</h2>
<p>Lithium-ion batteries are now a leading cause of fires in waste trucks and recycling facilities across Australia. When compacted or punctured they can ignite, and those fires are extremely difficult to extinguish. Never place batteries — or devices with built-in batteries, including vapes, power banks, cordless tools and laptops — in any kerbside bin. Dedicated battery drop-off points are available at most supermarkets, hardware chains and council facilities.</p>
<p>If a battery is swollen, damaged or leaking, don't put it in a container with others. Handle it separately and tell the drop-off point.</p>

<h2>Wipe your data first</h2>
<p>Recycling doesn't guarantee data destruction. Before disposing of any device: sign out of accounts, perform a full factory reset, and remove SIM and memory cards. For computers, a factory reset is the practical minimum; for anything holding sensitive material, physically removing the drive is safer. Business equipment often requires certified destruction with documentation.</p>

<h2>If it still works</h2>
<p>Working computers and phones have real value to charities that refurbish devices for people who can't afford them. A five-year-old laptop that's useless to you may be transformative for a student. Wipe it, include the charger, and check the organisation's condition requirements first.</p>
"""),

dict(slug="hazardous-waste-disposal-australia", cat="disposal", mins=8,
 title="Paint, Chemicals and Gas Bottles: Hazardous Waste Disposal",
 h1="Paint, chemicals, gas bottles and other things bins won't take",
 desc="How to safely dispose of paint, garden chemicals, motor oil, gas bottles, batteries and asbestos in Australia — and why rubbish removal services can't take them.",
 excerpt="The category no removal service, skip or bin will accept — and the free programs that will.",
 body="""
<p>Every rubbish removal operator, skip bin company and council collection excludes the same category of material: hazardous household waste. This isn't a matter of preference — it's a licensing and safety issue, and the exclusions are near-universal.</p>

<h2>What's on the excluded list</h2>
<p>Wet or liquid paint, solvents, thinners, adhesives, pool chemicals, garden pesticides and herbicides, motor oil, brake and transmission fluid, coolant, acids, gas bottles and cylinders, fire extinguishers, flares, ammunition, batteries, fluorescent tubes, smoke detectors, medical sharps, and asbestos in any form.</p>

<h2>Where it can go instead</h2>

<h3>Household chemical collection programs</h3>
<p>Every Australian state and territory runs some form of free household hazardous waste collection — permanent drop-off sites, mobile collection events, or both. These accept most of the list above from householders at no charge. Search your state EPA or environment department's site for current locations and dates; commercial quantities are handled differently and usually attract a fee.</p>

<h3>Paint</h3>
<p>A national paint stewardship scheme operates drop-off points across Australia accepting both water-based and solvent-based paint from households and trade. There are limits per container size and per visit. Empty, fully dried paint tins can usually go in general or metal recycling — the restriction applies to liquid paint. Small quantities of leftover water-based paint can be dried out by leaving the lid off in a ventilated area away from children and pets.</p>

<h3>Gas bottles</h3>
<p>LPG cylinders must never go in a bin, skip or removal truck — they explode in compaction equipment and have caused serious incidents. Many gas suppliers and hardware retailers accept old cylinders through swap-and-go arrangements, and transfer stations generally accept them at a dedicated point. The same applies to camping canisters and fire extinguishers.</p>

<h3>Motor oil</h3>
<p>Used oil is highly recyclable and heavily regulated. Most transfer stations and many service centres accept it free in reasonable quantities. Never pour it down a drain or onto ground — a single litre contaminates a very large volume of water.</p>

<h3>Sharps and medicines</h3>
<p>Needles require a rigid, approved sharps container and return to a participating pharmacy, hospital or council collection point. Unwanted medicines should go back to any pharmacy under the national return scheme — not into bins, and not down the toilet.</p>

<h2>Asbestos</h2>
<p>Asbestos is in a category of its own. It cannot go in a bin, a skip, or on a removal truck, and disturbing it without controls is genuinely dangerous. Any Australian home built or renovated before 1990 may contain it — in fibro sheeting, eaves, bathroom linings, vinyl backing and fencing. If you suspect it, don't cut, sand, drill or break it. Have it assessed, and engage a licensed asbestos removalist; disposal must go to a facility specifically licensed to receive it. Penalties for mishandling are among the highest in the waste system.</p>

<h2>The practical approach</h2>
<p>When planning a cleanout, separate anything suspicious into its own pile before the crew arrives. It saves time on the day and avoids the awkward situation of a truck being loaded with something that has to come back off it.</p>
"""),

dict(slug="what-to-do-with-old-furniture", cat="disposal", mins=7,
 title="What to Do With Old Furniture: Donate, Sell or Dispose",
 h1="Old furniture: donate, sell, or dispose?",
 desc="How to decide whether old furniture is worth donating or selling, what charities will and won't accept, and how to dispose of what's left responsibly.",
 excerpt="Charities reject a large share of donated furniture. Knowing what they'll take saves everyone a wasted trip.",
 body="""
<p>Furniture occupies more landfill volume than almost any other household item, and a significant proportion of what's thrown away is still perfectly usable. The reverse is also true: charities spend a great deal of money disposing of donations they never should have received.</p>

<h2>The honest test</h2>
<p>Before deciding something is donation-worthy, ask whether you would accept it into your own home if you needed furniture and had no money. If the answer is no, it isn't a donation — it's a disposal that you're passing to someone else at their cost.</p>

<h2>What charities generally accept</h2>
<p>Clean, structurally sound furniture in current condition: dining tables and chairs, bed frames, wardrobes, chests of drawers, bookshelves, sofas without tears or stains, working appliances. Items should be complete, assembled or with all fittings, and free of odour.</p>

<h2>What they generally refuse</h2>
<ul>
<li>Anything torn, stained, smoke-affected or mouldy</li>
<li>Flat-pack furniture that has been disassembled, or that's water-damaged at the joints</li>
<li>Sofas and upholstered items without compliant fire labelling in some states</li>
<li>Used mattresses — almost universally refused</li>
<li>Cots, prams and car seats, which have safety standards and expiry considerations</li>
<li>Anything with visible pest activity</li>
</ul>
<p>Leaving refused items outside a charity store after hours is illegal dumping, and it's a serious cost burden for the organisations involved. If in doubt, phone first and describe the item honestly — most will tell you immediately.</p>

<h2>Selling</h2>
<p>Solid timber furniture, mid-century pieces, quality outdoor settings and recognisable brands sell readily on marketplace platforms. Photograph in daylight, measure everything, be upfront about flaws, and price for a quick sale rather than the best possible price if your real goal is having it gone. Anything still unsold after two weeks probably isn't going to sell.</p>

<h2>Free to a good home</h2>
<p>Verge-side giveaway pages, community groups and "buy nothing" networks move usable furniture quickly. The rule is simple: put it out on the day someone is coming, not indefinitely. Furniture left on a nature strip "for anyone" that nobody takes becomes illegal dumping and your responsibility.</p>

<h2>Disposal</h2>
<p>For what's genuinely finished: council hard rubbish handles most furniture, transfer stations accept it directly, and removal services take it from wherever it sits. Timber furniture can often be recovered for chipping if it's separated from upholstered items — worth mentioning to whoever collects it.</p>

<h2>A note on timing</h2>
<p>The most common mistake is leaving the decision until moving day. Sorting furniture takes time you won't have. Start the donate-sell-dispose triage two to three weeks out, and book the disposal for the last item, not the first.</p>
"""),

dict(slug="green-waste-disposal", cat="disposal", mins=6,
 title="Green Waste Disposal: Branches, Clippings and Garden Clean-Ups",
 h1="Green waste: what to do with garden rubbish",
 desc="How to deal with garden waste in Australia — kerbside green bins, mulching, transfer stations, and rules on burning off and moving plant material.",
 excerpt="Green waste is the easiest material to keep out of landfill — and the rules on burning it are stricter than most people expect.",
 body="""
<p>Garden waste is heavy, seasonal, and almost entirely recoverable. It's also the material most often burned illegally.</p>

<h2>Kerbside green bins</h2>
<p>Most metropolitan councils provide a green organics bin, typically collected fortnightly. Accepted material usually includes grass clippings, leaves, prunings, small branches and weeds. Many councils now also accept food scraps in the same bin — check yours, because contamination rules matter and a contaminated load can be sent to landfill.</p>
<p>What's generally excluded: soil and rocks, treated timber, plastic plant pots, and branches above a certain diameter or length.</p>

<h2>Bigger jobs</h2>
<p>A green bin is useless when you've just removed a hedge. Options for volume:</p>
<ul>
<li><strong>Transfer station drop-off.</strong> Green waste is usually charged at a lower rate than general waste because it's processed into mulch and compost. Keep it separated — mixing it with general rubbish means paying the higher rate on the whole load.</li>
<li><strong>Green waste skip.</strong> Cheaper per cubic metre than a mixed skip for the same reason.</li>
<li><strong>Removal service.</strong> Practical for large one-off clean-ups where you don't want to handle heavy, awkward branches.</li>
<li><strong>Council green waste collections.</strong> Many councils run seasonal bundled-branch collections, often timed before bushfire season.</li>
</ul>

<h2>Mulching on site</h2>
<p>The cheapest option is often not removing it at all. Chipped prunings make excellent mulch, suppress weeds and retain moisture. Chipper hire is inexpensive for a day, and arborists will frequently leave chip on site free after a tree job. Grass clippings are better left on the lawn than bagged.</p>

<h2>Burning off</h2>
<p>Rules on burning garden waste are far stricter than most people assume and vary by council, state and season. In most metropolitan areas it's prohibited outright. In regional areas it's often permitted only with a permit, only outside fire danger periods, and only for specified material. Burning treated timber, painted timber or any household waste is prohibited everywhere. Check with your council and fire authority before lighting anything — penalties are significant and liability for escaped fires is serious.</p>

<h2>Weeds and biosecurity</h2>
<p>Some declared weeds have movement restrictions, and moving soil or plant material between regions can spread pathogens like Phytophthora and myrtle rust. For invasive species, check your state's requirements rather than assuming the green bin is appropriate — some must be bagged and sent to landfill specifically to prevent them propagating through compost.</p>
"""),

# ---------------- SITUATIONS ----------------
dict(slug="deceased-estate-cleanout-guide", cat="situations", mins=10,
 title="Clearing a Deceased Estate: A Practical Guide",
 h1="Clearing a deceased estate: where to start",
 desc="A step-by-step guide for executors and families clearing a deceased estate property — timing, probate, valuables, documents, and organising the clearance.",
 excerpt="What to do first, what to never rush, and the documents to find before anything leaves the house.",
 body="""
<p>Clearing a deceased person's home is one of the harder practical tasks most people encounter, and it usually arrives alongside grief and administrative pressure. This guide covers the practical sequence. It isn't legal advice — for questions about authority, probate or entitlements, speak to the estate's solicitor.</p>

<h2>Before anything is moved</h2>
<p><strong>Establish who has authority.</strong> The executor named in the will, or an administrator appointed by the court, is the person entitled to deal with the estate's property. Family members clearing a house without that authority — however well-intentioned — can create real disputes. If there's any uncertainty, wait.</p>
<p><strong>Secure the property.</strong> Change locks if keys are unaccounted for, and check what the insurer requires. Standard home insurance is often affected once a property becomes unoccupied, and many policies have vacancy clauses that reduce or void cover after a set period. Notify the insurer.</p>
<p><strong>Photograph everything.</strong> Room-by-room photos before anything moves protect the executor and settle later questions about what was there.</p>

<h2>Find the documents first</h2>
<p>Before any bulk clearing, search deliberately for: the will, title deeds, insurance policies, bank and superannuation statements, share certificates, tax records, funeral bonds, and cemetery or memorial documentation. These turn up in unexpected places — taped inside wardrobes, in freezer bags, between book pages, in biscuit tins. So does cash and jewellery.</p>

<h2>Don't rush the sentimental sorting</h2>
<p>Photographs, letters, films and handwritten material are irreplaceable and easily lost in a fast clearance. Set aside a single box for anything of this kind as you go, and deal with it separately later. Families rarely regret taking longer here; they frequently regret speed.</p>

<h2>Valuables</h2>
<p>Jewellery, antiques, coins, stamps, artwork, tools and quality furniture may have significant value. If the estate has multiple beneficiaries or the value is unclear, a valuation before disposal protects the executor. Auction houses provide appraisals, and specialist dealers will assess collections. Be cautious of anyone offering to buy the contents of a house sight-unseen at a flat price.</p>

<h2>Sorting the rest</h2>
<p>A workable method is four categories, room by room:</p>
<ul>
<li><strong>Keep</strong> — for family, clearly allocated</li>
<li><strong>Sell</strong> — auction, marketplace or dealer</li>
<li><strong>Donate</strong> — clean, functional, genuinely usable</li>
<li><strong>Dispose</strong> — everything else</li>
</ul>
<p>Work one room at a time and finish it before starting another. Kitchens and bathrooms are quickest and build momentum; sheds, garages and paperwork are slowest, so leave them for when you've found your rhythm.</p>

<h2>The things that need special handling</h2>
<p>Older properties commonly contain material that can't go in a general load: paint and chemicals in the shed, gas bottles, old fuel, medications, firearms and ammunition (which must go to police), and potentially asbestos in fibro sheeting or eaves. Set these aside rather than assuming a removal crew will take them.</p>

<h2>Booking the clearance</h2>
<p>When you're ready, a full house clearance is usually a one-day job for a crew. Useful things to arrange: confirm the operator can provide completion photos, ask them to sort for donation rather than sending everything to landfill, and if the estate has multiple beneficiaries, keep a record of what was disposed of and when.</p>

<h2>If the property is hoarded</h2>
<p>Hoarded properties need a different approach — safety assessment first, staged clearing, and a slower search process because valuables and documents are genuinely buried. Don't attempt it as a weekend family project. There's a separate guide on this.</p>

<h2>Pace</h2>
<p>Unless there's a settlement date or an insurance issue forcing the timeline, there is usually less urgency than families feel. Rushing produces decisions people regret. If you can take three weekends instead of one, take them.</p>
"""),

dict(slug="hoarding-cleanup-guide", cat="situations", mins=9,
 title="Hoarding Clean-Ups: A Practical and Respectful Approach",
 h1="Clearing a hoarded property",
 desc="How to approach a hoarding clean-up safely and respectfully — assessing hazards, working in stages, finding valuables, and supporting the person involved.",
 excerpt="Safety assessment, staged clearing, and why the fastest approach is usually the wrong one.",
 body="""
<p>Hoarding situations require a different approach from ordinary cleanouts. The practical challenges are real, but the human ones matter more — and getting that part wrong can undo the work entirely.</p>

<h2>Understand what you're dealing with</h2>
<p>Hoarding disorder is a recognised mental health condition, distinct from ordinary untidiness or collecting. For the person affected, the possessions carry genuine meaning and distress at their removal is not obstinance. Forced clear-outs conducted without the person's involvement frequently result in rapid re-accumulation and lasting damage to relationships and trust.</p>
<p>Where the person is still living in the property, involving them in decisions — even slowly, even inefficiently — produces better and more durable outcomes. Where the property is a deceased estate, the same respect applies to how their belongings are handled in front of family.</p>

<h2>Safety assessment first</h2>
<p>Before anyone starts, assess the hazards. Common ones in heavily hoarded properties:</p>
<ul>
<li>Structural loading — accumulated material is extremely heavy, and floors can be compromised</li>
<li>Blocked exits and collapsed stacks</li>
<li>Vermin, insect infestation and animal waste</li>
<li>Mould and poor air quality</li>
<li>Rotting food and biological hazards</li>
<li>Buried chemicals, gas bottles and expired products</li>
<li>Non-functioning utilities, exposed wiring, no working lighting</li>
<li>Sharps, broken glass, and needles in some cases</li>
</ul>
<p>Appropriate protection means at minimum sturdy footwear, cut-resistant gloves, and respiratory protection rated for particulates and mould. In severe cases — animal waste, biological contamination, suspected contamination from drug manufacture — this becomes specialist work and shouldn't be attempted privately.</p>

<h2>Work in stages</h2>
<p>Attempting to clear a heavily hoarded property in a single day is how valuables get destroyed and relationships get damaged. A staged approach works better:</p>
<ol>
<li><strong>Create access.</strong> Clear pathways to exits, and clear one room to use as a sorting space.</li>
<li><strong>Remove the obvious.</strong> Rotting material, contaminated items and clear rubbish, with the person's agreement where they're present.</li>
<li><strong>Sort systematically.</strong> One area at a time, with defined categories.</li>
<li><strong>Search carefully.</strong> Cash, jewellery, documents and irreplaceable photographs are routinely found deep in hoarded material. Anything paper-based should be checked before disposal.</li>
<li><strong>Clean.</strong> Once cleared, properties usually need a deep clean, and sometimes pest treatment or odour remediation.</li>
</ol>

<h2>Expect volume</h2>
<p>Hoarded properties generate far more material than people estimate — commonly multiple full truck loads from a single house. Budget and plan accordingly, and expect the scope to be larger than the initial walk-through suggested.</p>

<h2>If you're supporting someone</h2>
<p>Pace matters more than progress. Give the person genuine decision-making authority over their belongings. Avoid negotiating over individual items in front of others. Recognise that clearing the property doesn't address the underlying condition — professional support alongside the practical work makes recurrence far less likely. Australian mental health services and hoarding-specific support programs exist in most states, and a GP is a reasonable starting point.</p>

<h2>For landlords and agents</h2>
<p>Hoarding in a rental raises tenancy law obligations that vary by state, including notice requirements, the handling of goods, and considerations relating to disability discrimination. Take advice before acting — the wrong process can be both unlawful and counterproductive.</p>
"""),

dict(slug="end-of-lease-rubbish-removal", cat="situations", mins=7,
 title="End of Lease Cleanouts: Getting Your Bond Back",
 h1="End of lease: clearing out without losing your bond",
 desc="What tenants need to remove before a final inspection, common bond deductions for rubbish, and how to time an end-of-lease cleanout.",
 excerpt="Leaving rubbish behind is one of the most common and most avoidable bond deductions.",
 body="""
<p>Rubbish left behind is one of the most frequent reasons for bond deductions, and one of the easiest to avoid. Landlords are entitled to charge for removal, and the amounts claimed are often well above what you'd have paid to deal with it yourself.</p>

<h2>What has to go</h2>
<p>Everything that wasn't there when you moved in. That includes items you consider improvements — a shed you installed, a garden bed you built, shelving you mounted — unless the landlord has agreed in writing that they stay. Check your entry condition report; it's the reference point for any dispute.</p>
<p>Commonly missed: the garage or carport, the garden shed, under the house, side passages, the top of built-in wardrobes, and behind or under appliances.</p>

<h2>Timing it properly</h2>
<p>The sequence that works:</p>
<ol>
<li><strong>Two to three weeks out:</strong> sort and start moving out anything you're donating or selling.</li>
<li><strong>One week out:</strong> book your rubbish removal or check your council's hard waste availability. Council collections often have multi-week waits, which is exactly the mistake that causes last-minute panic.</li>
<li><strong>Moving day:</strong> furniture and possessions out.</li>
<li><strong>After the furniture, before the clean:</strong> rubbish removal. Cleaning an empty property is far faster and produces a better result.</li>
<li><strong>Last:</strong> the bond clean, then the inspection.</li>
</ol>
<p>Doing the clean before the rubbish is gone means doing it twice.</p>

<h2>The bin trap</h2>
<p>Kerbside bins hold far less than people expect and are collected on one fixed day. Overfilled bins with lids that won't close are frequently left uncollected, which leaves you with the same rubbish and less time. If you're generating more than a bin's worth, plan a different route from the start.</p>
<p>Using neighbours' bins without asking is both antisocial and, in many council areas, an offence.</p>

<h2>Items that need planning</h2>
<p>Mattresses, lounges, fridges and washing machines can't go in a bin and often can't wait for a council collection date. These are the items that most commonly get abandoned in a garage on the final day. Deal with them first, not last.</p>

<h2>Documentation</h2>
<p>Photograph every room, the garage, the shed and the yard once emptied and cleaned. Date-stamped photos are the most effective evidence in a bond dispute, and they cost nothing to take. Keep any receipt from a rubbish removal service — it demonstrates the property was cleared.</p>

<h2>If a deduction is claimed anyway</h2>
<p>Bond disputes are handled by the residential tenancy authority in each state, and the process is designed to be accessible without a lawyer. Landlords must substantiate deductions with evidence and actual costs, not estimates. Your entry condition report and exit photos are what decide most of these matters.</p>
"""),

dict(slug="moving-house-declutter-checklist", cat="situations", mins=7,
 title="Moving House: A Decluttering Checklist That Actually Works",
 h1="Decluttering before a move",
 desc="A practical timeline for decluttering before moving house — what to sort when, what removalists won't take, and how to avoid paying to move rubbish.",
 excerpt="Every box you don't move is money saved. Here's the sequence that works.",
 body="""
<p>Removalists charge by volume and time. Every unnecessary box is money spent moving something you'll throw away at the other end — and the other end is where you'll have least energy to deal with it.</p>

<h2>The six-week sequence</h2>

<h3>Six weeks out — the easy wins</h3>
<p>Start with categories that require no emotional decisions: expired food and medicines, broken items you've been meaning to fix, obsolete cables and electronics, worn-out linen and towels, and anything in the garage you haven't touched since you last moved.</p>

<h3>Four weeks out — sell and donate</h3>
<p>Anything with resale value needs lead time. List furniture and appliances now, because a piece that hasn't sold three days before the truck arrives becomes a disposal problem. Book donation pickups early; charities that collect furniture often have waiting lists.</p>

<h3>Three weeks out — room by room</h3>
<p>Work through each room with four piles: take, sell, donate, dispose. Finish a room before starting the next. Wardrobes, the linen cupboard and the kitchen usually produce the most volume.</p>

<h3>Two weeks out — the hard categories</h3>
<p>Paperwork, photographs, sentimental items and children's artwork. These take longest because each item is a decision. Set a container limit in advance — one box for sentimental items, and if it's full, something comes out before something goes in.</p>

<h3>One week out — book the disposal</h3>
<p>By now you know what's actually leaving. Book a rubbish removal or check council collection availability. This is the point at which most people discover their council's next hard waste date is after they've moved.</p>

<h3>Moving day — after the truck</h3>
<p>A final sweep of the empty house always turns up more, particularly in the shed, garage and side passage.</p>

<h2>What removalists won't take</h2>
<p>Removalists generally refuse flammable liquids, gas bottles, chemicals, paint, fuel, aerosols, batteries and firearms. Some won't take plants, opened food, or fridges that haven't been defrosted. Check with your removalist early — finding out on the day leaves you with a pile and no plan.</p>

<h2>The garage rule</h2>
<p>Garages and sheds hold the highest proportion of material that will never be used again, and they're always tackled last when energy is lowest. Do the shed first instead. It's the single most effective change to this process.</p>

<h2>A note on "just in case"</h2>
<p>The most common category of moved-then-discarded item is the thing kept "just in case." A useful test: if you needed this item and didn't have it, could you replace it for under fifty dollars within a day? If yes, and you haven't used it in a year, moving it costs more than replacing it would.</p>
"""),

dict(slug="renovation-waste-disposal", cat="situations", mins=7,
 title="Renovation Waste: Planning Disposal Before You Start",
 h1="Renovation waste: plan the disposal before the demolition",
 desc="How to handle renovation and demolition waste in Australia — separating materials, asbestos in pre-1990 homes, and choosing between skips and removal services.",
 excerpt="Demolition generates far more volume than people expect, and one material can stop the whole job.",
 body="""
<p>Renovation waste is heavy, high-volume and awkward, and it accumulates faster than any other domestic waste stream. Planning disposal before demolition starts is the difference between a smooth job and a driveway full of rubble for three weeks.</p>

<h2>Check for asbestos first</h2>
<p>This is the step that matters most. Any Australian home built or renovated before 1990 may contain asbestos — in fibro wall and ceiling sheeting, eaves, bathroom and laundry linings, vinyl floor backing, textured ceilings, fencing and around old heaters and hot water systems.</p>
<p>Asbestos is safe while undisturbed and dangerous when cut, drilled, sanded or broken. If you're renovating a pre-1990 property, have a licensed assessor inspect before demolition. If asbestos is present, it must be removed by a licensed removalist and disposed of at a facility licensed to receive it. It cannot go in a skip, a general bin, or a rubbish removal truck. This single issue derails more renovation timelines than anything else, and doing it wrong carries serious health and legal consequences.</p>

<h2>Separate as you go</h2>
<p>Mixed loads cost more to dispose of than separated ones, because contaminated material can't be recovered. Where you have space, keep separate piles for:</p>
<ul>
<li><strong>Clean concrete, brick and tile</strong> — crushed into road base, usually the cheapest to dispose of</li>
<li><strong>Scrap metal</strong> — has genuine value; roofing, framing, pipework and old appliances</li>
<li><strong>Untreated timber</strong> — chipped or recovered; keep it separate from treated and painted timber</li>
<li><strong>Plasterboard</strong> — recyclable but a contaminant in other streams; many facilities want it separate</li>
<li><strong>General mixed waste</strong> — everything else, and the most expensive per cubic metre</li>
</ul>

<h2>Skip or removal service</h2>
<p>For a renovation generating waste over days or weeks, a skip on site usually makes sense — provided you have somewhere legal to put it and can do the loading. Note that heavy material like concrete and soil is often restricted to specific skip types, and overloading a skip means it can't legally be lifted.</p>
<p>A removal crew makes more sense for the strip-out phase, where a large volume appears at once and you want it gone the same day, or where there's no space for a skip. Many renovations use both.</p>

<h2>Volume is always underestimated</h2>
<p>A single bathroom strip-out — tiles, vanity, bath, plasterboard, waterproofing — commonly fills more than people expect, because rubble doesn't stack. Kitchen strip-outs are similar. Budget more volume than your visual estimate suggests, consistently.</p>

<h2>Reuse before disposal</h2>
<p>Salvage yards, architectural recyclers and building reuse centres buy or accept doors, windows, timber, bricks, fixtures, and quality hardware. Demolishing carefully rather than smashing takes longer but recovers material with genuine value — and reduces the volume you're paying to remove.</p>
"""),

dict(slug="garage-and-shed-cleanout", cat="situations", mins=6,
 title="Garage and Shed Clean-Outs: How to Get Through It",
 h1="Clearing out the garage or shed",
 desc="A practical method for clearing a garage or shed, including what needs special disposal and the safety issues in long-neglected storage spaces.",
 excerpt="The space everyone puts off. A method that gets it done in a weekend.",
 body="""
<p>Garages and sheds accumulate the widest range of material of any space in a house, and they're the hardest to start because there's no obvious first step.</p>

<h2>The method</h2>
<p><strong>Empty it onto the driveway.</strong> This sounds extreme and it's the thing that works. Sorting inside a full garage means shuffling items between piles in a confined space. With everything visible in daylight, decisions get faster and you see duplicates immediately — most garages contain three of something nobody knew they had two of.</p>
<p>Pick a day with clear weather, start early, and commit to finishing. Half-emptied garages stay half-emptied for months.</p>

<h2>Sort into six</h2>
<ul>
<li><strong>Keep and store properly</strong></li>
<li><strong>Sell</strong> — tools, bikes, camping gear and sporting equipment hold value well</li>
<li><strong>Donate</strong></li>
<li><strong>Scrap metal</strong> — worth separating; yards pay for it</li>
<li><strong>Hazardous</strong> — see below</li>
<li><strong>Dispose</strong></li>
</ul>

<h2>The hazardous pile is bigger than you think</h2>
<p>Garages and sheds are where household hazardous waste lives. Expect to find: old paint tins, thinners and solvents, garden chemicals and pesticides, motor oil and coolant, fuel containers, gas bottles, car batteries, fluorescent tubes, and aerosols. None of these can go in a bin, a skip or on a removal truck.</p>
<p>These go to a household chemical collection or a transfer station's dedicated point — usually free for households. Set them aside in a separate area as you sort, ideally in a crate, and deal with them as one trip.</p>

<h2>Safety in neglected spaces</h2>
<p>Sheds that haven't been opened in years commonly contain redback and white-tail spiders, snakes in warmer regions, rodent nests and droppings, wasp nests, and rusted metal. Wear enclosed shoes and gloves, open everything up and let it air before working in it, and be cautious with anything you can't see into. Rodent droppings warrant a mask.</p>
<p>Older sheds may have asbestos sheeting in the walls or roof. Don't drill, cut or break it, and get it assessed before any demolition.</p>

<h2>Storage that survives</h2>
<p>Wall-mounted storage keeps the floor clear and is the main reason some garages stay tidy and others don't. Clear labelled containers beat cardboard boxes, which absorb moisture and collapse. Keep frequently used items at waist height and rarely used ones high.</p>

<h2>Getting rid of the pile</h2>
<p>Garage cleanouts typically produce more volume than council hard waste limits allow, and often include items councils exclude. If you've emptied everything onto the driveway, a same-day removal is worth booking in advance for that afternoon — the pile has to be gone before you can put the car back in.</p>
"""),

# ---------------- AGENTS ----------------
dict(slug="abandoned-goods-rental-property", cat="agents", mins=8,
 title="Goods Left Behind by Tenants: What Landlords and Agents Need to Know",
 h1="Tenant goods left behind: the process",
 desc="How Australian tenancy law treats goods abandoned by former tenants, why the disposal process matters, and how to document a rental property cleanout.",
 excerpt="Disposing of a former tenant's belongings incorrectly can make a landlord liable for their value.",
 body="""
<p>When a tenancy ends and possessions remain, the temptation is to skip-bin the lot and re-list the property. In every Australian jurisdiction, that's a risk — abandoned goods are governed by specific processes, and disposing of them incorrectly can leave the landlord liable for their value.</p>
<p>This is general information, not legal advice. Requirements differ meaningfully between states and change over time, so check your state's residential tenancies legislation and your tenancy authority's current guidance before acting.</p>

<h2>The general shape of the rules</h2>
<p>Across Australian jurisdictions the common elements are:</p>
<ul>
<li><strong>Goods are categorised.</strong> Perishable food, rubbish and items below a value threshold can usually be disposed of immediately. Goods above that threshold, and personal documents, cannot.</li>
<li><strong>Personal documents are treated separately.</strong> Identity documents, photographs and personal papers generally must be retained for a defined period and returned if claimed, regardless of value.</li>
<li><strong>Notice is usually required.</strong> Most jurisdictions require written notice to the former tenant at their last known address, and sometimes public notice, before goods can be sold or disposed of.</li>
<li><strong>Storage periods apply.</strong> Goods above the threshold typically must be stored for a set period before disposal.</li>
<li><strong>Proceeds are accounted for.</strong> Where goods are sold, proceeds usually go toward storage and disposal costs, with any remainder held for the tenant or paid to a designated authority.</li>
</ul>

<h2>Why documentation matters</h2>
<p>The most common failure isn't malice — it's an agent clearing a property quickly with no record of what was there. If the former tenant later claims a valuable item was disposed of, the absence of evidence works against the landlord.</p>
<p>A defensible process looks like: photograph every room before anything is touched; itemise anything of apparent value; record the date; retain personal documents separately; keep the disposal receipt; and keep copies of any notices sent.</p>

<h2>Practical steps for a turnover</h2>
<ol>
<li>Confirm the tenancy has actually ended and, if abandonment is suspected rather than confirmed, follow your state's abandonment process — entering and clearing prematurely is a serious problem.</li>
<li>Photograph and inventory before clearing.</li>
<li>Separate: rubbish and perishables, goods of apparent value, and personal documents.</li>
<li>Deal with each category per your jurisdiction's requirements.</li>
<li>Book the clearance, and keep the receipt.</li>
</ol>

<h2>What to expect from a removal operator</h2>
<p>For rental turnovers, useful things to ask for: same-week availability, a written quote before work starts, completion photographs, and a disposal receipt for the file. If the property contains items you're required to retain, tell the crew clearly — the pile they're taking should be only what you've cleared for disposal.</p>

<h2>Hoarding and severely neglected properties</h2>
<p>These raise additional considerations, including possible disability discrimination issues and the need for safety assessment before entry. They also generate far more volume than a standard turnover — commonly several truck loads. Budget and schedule accordingly, and take advice on the tenancy law side before issuing notices.</p>
"""),

dict(slug="pre-sale-property-declutter", cat="agents", mins=6,
 title="Clearing a Property Before Sale: What Actually Adds Value",
 h1="Clearing a property before sale",
 desc="Why decluttering before listing is one of the highest-return preparations for an Australian property sale, and what to prioritise on a limited budget.",
 excerpt="The cheapest preparation with the highest return — and the areas buyers judge hardest.",
 body="""
<p>Of everything a seller can do before listing, clearing clutter is consistently the cheapest and among the most effective. It costs a fraction of renovation and changes how every photograph and inspection reads.</p>

<h2>Why it works</h2>
<p>Buyers assess space, light and condition. Clutter obscures all three. A room full of furniture reads as small; a garage full of boxes reads as inadequate storage; an overgrown yard reads as deferred maintenance across the whole property. Buyers also mentally price in the work they think they'd have to do — and a property that looks neglected invites lower offers regardless of its actual condition.</p>

<h2>Priorities on a limited budget</h2>
<ol>
<li><strong>The exterior and approach.</strong> The first impression sets expectations for everything after it. Clear the front yard, remove dead plants, tidy the entry, and get rid of anything stored down the side passage.</li>
<li><strong>The garage or shed.</strong> Buyers open these, and a full garage reads as a house without storage. An empty one reads as a bonus room.</li>
<li><strong>Kitchen benches and bathroom surfaces.</strong> Clear surfaces photograph dramatically better.</li>
<li><strong>Excess furniture.</strong> Removing a third of the furniture from most rooms makes them read larger. This is the single change professional stylists make most often.</li>
<li><strong>Wardrobes and cupboards.</strong> Buyers open them. Half-full reads as generous storage; overflowing reads as insufficient.</li>
<li><strong>The yard.</strong> Green waste, old play equipment, dead cars and unused materials.</li>
</ol>

<h2>Sequence with the photography</h2>
<p>Photographs are taken once and carry the entire online campaign. Clear and clean before the photographer attends, not after. A surprising number of listings are photographed mid-declutter, and those images work against the property for the whole campaign.</p>

<h2>Personal items</h2>
<p>Family photographs, religious items, trophies and collections make it harder for buyers to imagine themselves in the space. This isn't about erasing personality entirely — it's about reducing the visual noise that stops someone picturing their own life there.</p>

<h2>Timing for a deceased estate or long-held property</h2>
<p>Properties held for decades generate far more volume than owners anticipate, and the clearance often takes longer than the campaign timeline allows. If a sale is planned, start the clearing well before you list — agents will tell you the number of campaigns delayed by a garage that took three weeks instead of a weekend.</p>

<h2>What not to bother with</h2>
<p>Major renovations rarely return their cost in a short pre-sale window. Cleaning, clearing, minor repairs, garden tidying and a coat of paint reliably do. Spend the budget in that order.</p>
"""),
]

from articles2 import ARTICLES_2
ARTICLES = ARTICLES + ARTICLES_2
