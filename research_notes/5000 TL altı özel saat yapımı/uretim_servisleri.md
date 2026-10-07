# Manufacturing services and 2026 pricing for one-off custom watch parts (PCB dial + metal case), hobbyist in Turkey

Research date: 2026-10-07. All prices are in their original currency. "From" prices are vendor floor prices, not quotes for this part. Live instant quotes were NOT obtainable through the fetch tools (JLCPCB/PCBWay/JLC3DP/JLCCNC quote pages need an uploaded file or a session), so no exact totals for the specific parts below were found. Reddit could not be searched (domain blocked to the research tool), so Reddit precedent is missing.

## Q1. PCB dial: JLCPCB / PCBWay price, availability and design rules for a ~30 mm round, 0.4/0.6 mm, 2-layer FR4, ENIG, black mask, white silkscreen (5 pcs)

### Takeaway
Both JLCPCB and PCBWay list 0.4 mm and 0.6 mm FR4 with a thickness tolerance of ±0.1 mm. At JLCPCB, 0.4 mm requires ENIG (or OSP) and black mask is a standard color. Neither vendor publishes a total price for this exact spec. On JLCPCB's documented formula, the ENIG area surcharge on a 30 mm board comes to cents, but the base fees for the ENIG and thin-board options can only be seen in the instant quote. Silkscreen is the weak point: the minimum is 0.15 mm line width and 1.0 mm text height (JLCPCB) or 0.8 mm (PCBWay), and legibility drops below about 1 mm. Fine dial art should be done in copper/ENIG plus mask openings, not silkscreen.

### Cited Findings

**JLCPCB: thickness, finish and color availability**
- FR-4 thickness options are 0.4, 0.6, 0.8, 1.0, 1.2, 1.6 and 2.0 mm. Tolerance is ±0.1 mm below 1.0 mm (so 0.4 mm can come out at 0.3–0.5 mm and 0.6 mm at 0.5–0.7 mm), and ±10% at 1.0 mm and above. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- HASL is not supported for boards ≤0.4 mm, so ENIG or OSP is required. Thin boards get a manual review of minimum dimensions, and the 3×3 mm minimum board size is stated for ≥0.6 mm. Castellated holes, plated edges and V-cut need ≥0.6 mm. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- A search snippet (not a fetched page) reports that 0.4 mm boards at JLCPCB accept only ENIG, cannot be panelized, and are not available as 1-layer. — [JLCPCB "Choose the Thickness of PCB"](https://jlcpcb.com/resources/pcb-thickness) (snippet; verify in the quote tool)
- A search summary of the JLCPCB quote page says leaded HASL is not available for 2-layer 0.6 mm boards, and that 0.6 mm boards are limited to ≤100×100 mm. The page metadata looked old. — [JLCPCB Online Quote](https://cart.jlcpcb.com/quote)
- The JLCPCB surface-finish guide (updated Sep 09, 2026) calls ENIG "suitable for thin PCBs (such as 0.4 mm boards)". Gold is offered at 1 or 2 µin (about 0.025–0.05 µm) over about 3–6 µm of nickel. ENIG "incurs a substantial surcharge per square meter" tied to gold prices. OSP costs nothing extra. — [JLCPCB Surface Finishes Guide](https://jlcpcb.com/help/article/jlcpcb-surface-finish)
- Solder mask colors are Green, Purple, Red, Yellow, Blue, White and Black. The capabilities page does not mention matte black. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- JLCPCB says there are "no extra color fees for most orders" and that 2-layer orders start at $2 for 5 pcs. — [JLCPCB blog: solder mask colors](https://jlcpcb.com/blog/pcb-solder-mask-colors-performance)
- Matte black at JLCPCB: a JLCPCB staff member on the EasyEDA forum (about 6 years old) said matte black was unavailable because it scratches easily, and described their black as between matte and glossy. A later commenter called it "very close to matte". — [EasyEDA forum: Matte black soldermask](https://easyeda.com/forum/topic/Matte-black-soldermask-06523918727340fb9a0c27a7806ec749)
- A hackaday.io log (undated) says JLCPCB's black mask hides the traces and is a "dirt and grease magnet". — [hackaday.io project 165559 log](https://hackaday.io/project/165559/log/164310)
- The JLCPCB watch case study (Aug 12, 2026) lists its 40 mm round watch PCB as 2-layer FR-4, 1.0 mm, ENIG, "Matte Black / Dark Green" mask, white silkscreen. It does not say which mask color was actually used. — [JLCPCB blog: 72-LED watch](https://jlcpcb.com/blog/precision-72-led-watch-jlcpcb-case)

**JLCPCB: upcharges**
- ENIG area surcharge applies only when exposed ENIG exceeds 30% of board area (top and bottom combined, out of 200%). The rate is $0.8992/m² per 1% over 30% for 1U" gold, and $1.7985/m² per 1% for 2U". If a side has no mask, the Gerbers must include fully opened mask layers so the area is calculated correctly. — [JLCPCB: In what cases will there be charged extra?](https://jlcpcb.com/help/article/in-what-cases-will-there-be-charged-extra)
- Small boards: deburring and corner rounding cost $0.02/pc for boards 1.5–3 cm on a side, and $0.05/pc under 1.5 cm. Boards ≤3 cm on one side ordered in batch as "Single PCB" carry an extra charge (amount only in an image). — [JLCPCB extra charges](https://jlcpcb.com/help/article/in-what-cases-will-there-be-charged-extra)
- Slot and cutout routing fee: applies for slot width 0.8–1.0 mm with a routing path ≥80 m/m², or width >1.0 mm with a path ≥120 m/m² (amount not stated). — [JLCPCB extra charges](https://jlcpcb.com/help/article/in-what-cases-will-there-be-charged-extra)
- The extra-charges page does not list a fee for a non-rectangular outline or for black mask. — [JLCPCB extra charges](https://jlcpcb.com/help/article/in-what-cases-will-there-be-charged-extra)
- Historical price data point (May 2022, old): a forum user complained that JLCPCB charged $36 extra for black + ENIG. A later reply estimated a 2-layer black ENIG board at about $28. — [EasyEDA forum: Solder mask colours](https://easyeda.com/forum/topic/Solder-mask-colours-27bfd24dc5324612b62da3591fdd04c3) (old; this predates the "no color fee" policy)
- EEVblog users (threads about 2+ years old) report surprise extra fees, such as $30 attributed to ENIG area and >$20 on a panel of tiny boards. One user saw the quote for identical boards change between visits (about $13). — [EEVblog: JLCPCB "random" fees](https://www.eevblog.com/forum/manufacture/jlcpcb-random-fees/); [EEVblog: Odd JLCPCB pricing](https://www.eevblog.com/forum/eda/odd-jlcpcb-pricing/)
- JLCPCB's own blog says ENIG costs about 20–40% more than HASL. — [JLCPCB blog: PCB pricing breakdown](https://jlcpcb.com/blog/pcb-pricing-breakdown) (via search summary)
- lcamtuf's vendor comparison (updated Jan 2026): a 6.5×9 cm HASL board cost about $1.50–2.00 shipped at JLCPCB, "closer to $4" in Jan 2026 because of US tariffs (US-specific). PCBWay was about $3–4 with courier shipping. — [lcamtuf: Comparing hobby PCB vendors](https://blog.coredump.cx/p/comparing-hobby-pcb-vendors)

**JLCPCB: design rules relevant to a dial**
- Silkscreen: minimum line width ≥0.15 mm, minimum text height 1.0 mm (40 mil), preferred width-to-height ratio 1:6, pad-to-silkscreen clearance 0.15 mm. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- Silkscreen quality: JLCPCB's silkscreen is "competent, but legibility drops below 1 mm", with slight improvement noted in 2025. JLCPCB's mask is "thinner and scratches more easily". — [lcamtuf: Comparing hobby PCB vendors](https://blog.coredump.cx/p/comparing-hobby-pcb-vendors)
- Minimum non-plated hole (NPTH) is 0.50 mm on 2+ layer boards. Hole tolerance is +0.13/-0.08 mm. Minimum non-plated slot width is 1.0 mm, minimum plated slot width is 0.5 mm (2-layer), and slot length must be ≥2× width. Non-plated slot tolerance is ±0.2 mm. Rectangular holes or slots without rounded corners are not supported. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- Outline: routed edge tolerance is ±0.2 mm (regular) or ±0.1 mm (high precision). High precision requires a board of at least 50×50 mm with three 1.5 mm tooling holes. Copper must be ≥0.2 mm from routed edges and slots. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- The JLCPCB watch case study says CNC routing held its 40 mm circle to ±0.1 mm, giving a drop-in fit in a commercial 40 mm case. It used a rectangular frame with mouse-bite tabs (0.5 mm holes at 0.8 mm pitch) and ≥0.3 mm edge-to-copper clearance. — [JLCPCB blog: 72-LED watch](https://jlcpcb.com/blog/precision-72-led-watch-jlcpcb-case)
- Solder mask bridge (dam) at 1 oz copper is 0.13 mm for black and white masks and 0.10 mm for other colors. Mask expansion is 1:1, with ≥0.09 mm between mask openings and adjacent traces. — [JLCPCB PCB Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities)
- Mask registration is described as tight (±0.025 mm) for all seven colors. — [JLCPCB blog: solder mask colors](https://jlcpcb.com/blog/pcb-solder-mask-colors-performance)

**PCBWay: availability, upcharges and design rules**
- The standard thickness range is 0.2–3.2 mm and includes 0.4 and 0.6 mm. Tolerance is ±0.1 mm below 1.0 mm and ±10% at 1.0 mm and above. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Below 1.0 mm, finished thickness tends to come out on the "+" side because of electroless copper, mask and surface finish. — [PCBWay Manufacturing tolerances](https://www.pcbway.com/pcb_prototype/PCB_Manufacturing_tolerances.html) (via search summary)
- Standard mask colors include Green, Red, Yellow, Blue, White, Black, Matt green, Matte black and Purple. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Green, red, yellow, blue, white and black mask cost the same. Purple, pink, grey, orange, matte black, matte green and clear masks carry an extra charge. — [PCBWay Solder mask page](https://www.pcbway.com/pcb_prototype/PCB_Solder_mask.html) (via search summary)
- A ModWiggler post (~5 years old) said PCBWay "do ENIG but not MATTE black. Their black is glossy". This conflicts with the current official list. — [ModWiggler: Matte Black and Gold PCBs?](https://www.modwiggler.com/forum/viewtopic.php?t=157778) (old)
- Silkscreen colors are White, Black, Yellow and None. White and black carry no extra charge. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Standard finishes include HASL, Immersion Gold (ENIG), OSP, Hard Gold, Immersion Silver, Immersion Tin and ENEPIG. Advanced ENIG is 100–150 µin nickel and 1–8 µin gold. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- The capabilities page states no restriction on 0.4 mm with ENIG or colored mask. Below 0.4 mm, panel size is limited to 14 in. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Silkscreen: minimum line or character width 0.15 mm, minimum character height 0.8 mm, recommended ratio 1:5. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- PCBWay's engineering-review note says legends on the solder mask layer (i.e., mask-opening text) need ≥1.2 mm height and ≥0.2 mm width. — [PCBWay help: silkscreen size and spacing in solder mask layer](https://www.pcbway.com/helpcenter/Engineering_Questions/silkscreen_size_and_spacing_in_solder_mask_layer.html) (via search summary)
- PCBWay support told a Hackaday builder that white silkscreen is machine-aligned, while other colors are aligned manually with an unavoidable "+/-6mil offset". The Advanced PCB overview lists a ±2 mil silkscreen offset. — [Hackaday.io: Black FR-4 and transparent soldermask by PCBWay](https://hackaday.io/project/194683-plasma-toroid-sky-guided-pcb-edition/log/230233-9-black-fr-4-and-transparent-soldermask-by-pcbway)
- Holes and slots: drill range 0.15–6.0 mm (extra charge under 0.2 mm). NPTH tolerance is ±0.05 mm. Non-plated slot minimum is 0.8 mm, plated slot minimum is 0.5 mm, and slot length-to-width should be ≥2. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Outline tolerance is ±0.2 mm for CNC routing (±0.5 mm V-score). Trace-to-edge distance is 0.25 mm. Minimum board size is 3×3 mm. — [PCBWay Capabilities](https://www.pcbway.com/capabilities.html)
- Matte black needs a larger solder bridge between pads: 0.35 mm on 3 oz copper, versus 0.30 mm for black and 0.25 mm for green. — [PCBWay Solder mask page](https://www.pcbway.com/pcb_prototype/PCB_Solder_mask.html) (via search summary)
- Price data point (old, about 2022, Advanced PCB): 10 pcs of 50×50 mm, 1.2 mm, black mask, yellow silkscreen, ENIG cost $116. — [CIRCUITSTATE: PCBWay adds new mask colors](https://www.circuitstate.com/news/pcbway-adds-orange-grey-pink-and-transparent-solder-mask-options-to-advanced-pcb-section/)

**Exposed copper art (ENIG) and copper-under-mask**
- Exposed ENIG art is explicitly priced, not prohibited: JLCPCB's >30% ENIG-area surcharge rule and its instruction to draw fully opened mask layers show the vendor expects large exposed-copper areas. — [JLCPCB extra charges](https://jlcpcb.com/help/article/in-what-cases-will-there-be-charged-extra)
- ENIG deposits only on copper that the mask leaves open, so the mask openings define where gold appears. — [Wikipedia: ENIG](https://en.wikipedia.org/wiki/Electroless_nickel_immersion_gold) (via search summary)
- A Hackaday commenter advised making dial text and lines from copper plus mask layers rather than silkscreen, because "silkscreen is usually low resolution while copper can be much finer". The maker agreed to try it. — [Hackaday: Fabbing a fab new watch face (Mar 7, 2024)](https://hackaday.com/2024/03/07/fabbing-a-fab-new-watch-face/)
- A commenter on the same post said copper layers can be "super high definition" and finished in silver (HASL) or gold (ENIG), while silkscreen is comparatively coarse. — [Hackaday: Fabbing a fab new watch face](https://hackaday.com/2024/03/07/fabbing-a-fab-new-watch-face/) (via search summary)
- On PCBWay's black FR-4 with transparent mask, ENIG gold "looks like it always does" and creates "a neat kind of sandy two-tone". — [Hackaday.io: Black FR-4 and transparent soldermask](https://hackaday.io/project/194683-plasma-toroid-sky-guided-pcb-edition/log/230233-9-black-fr-4-and-transparent-soldermask-by-pcbway)
- Black mask gives the lowest contrast between traces and board, so copper-under-mask patterns are subtle on black. — [Altium: solder mask types](https://resources.altium.com/p/how-choose-correct-solder-mask-your-pcb) (via search summary)

### Inferences
- On JLCPCB's formula, the ENIG area surcharge for 5 pcs of a ~30 mm board is negligible. For example, at 80% combined exposed area, 5 × 30×30 mm = 0.0045 m² × 50 points × $0.8992 ≈ $0.20. Most of the cost will be the fixed ENIG and thin-board option fees shown in the quote tool. Older forum data suggests the total for small black ENIG boards was on the order of $15–35 before shipping, but this is not verified for 2026.
- Because the JLCPCB high-precision ±0.1 mm outline requires a ≥50×50 mm board with tooling holes, a 30 mm dial should be expected at ±0.2 mm unless it is ordered in a panel or frame. The JLCPCB case study got ±0.1 mm with a mouse-bite frame. Design the dial-to-case seat with ≥0.2 mm radial clearance.
- For NH35-type dials (28.5 mm per the AliExpress listings in Q5), a 1.0 mm minimum silkscreen text height is coarse. Indices and numerals look sharper as ENIG copper features in mask openings, or as copper under black mask. Silkscreen should be white (machine-aligned) and used only for larger elements.
- The date window and the center (cannon pinion) hole will be non-plated cutouts. At JLCPCB the minimum is a 0.5 mm NPTH and a 1.0 mm non-plated slot width, with ±0.2 mm slot tolerance and rounded corners only, so a date window will have rounded corners of at least about 0.5 mm radius.
- Thickness choice: 0.4 mm is closer to a typical metal dial thickness but forces ENIG and shows ±0.1 mm variance (25%). 0.6 mm is stiffer and supports more options, but may interfere with hand clearance. This must be checked against the movement's dial-to-hour-wheel height (not sourced here).

### Gaps
- No live 2026 instant-quote total was obtained for 5 pcs of a 30 mm, 0.4 or 0.6 mm, ENIG, black, white-silkscreen board at either JLCPCB or PCBWay. The quote tools require a Gerber upload. The user should run both quotes.
- The exact JLCPCB fees for the 0.4/0.6 mm thickness option and the base ENIG option for small 2-layer boards are not published as text.
- Whether JLCPCB currently offers matte black (as opposed to its semi-matte black) is unconfirmed for 2026. The JLCPCB case study lists "Matte Black / Dark Green" ambiguously.
- PCBWay's matte black surcharge amount was not found.
- No source confirms whether PCBWay charges extra for 0.4 mm boards or for internal cutouts on small boards.

## Q2. PCB dial precedent: real examples and lessons learned

### Takeaway
There are several documented PCB watch dials: Neeraj Rane's NH35 build at PCBWay, an Instructables Seiko 5 mod, an Omega Calypso replacement dial on Hackaday, and electronic PCB watch faces with matte black + ENIG. The recurring lessons are: silkscreen shifts and is low-resolution, so use copper/ENIG for fine art; attach with dial feet, dial dots or dial tape rather than glue; mind the height under the date wheel; and lume works best in through-cutouts at the indices.

### Cited Findings
- **Neeraj Rane (PCBWay community, Aug 19, 2024), PCB dial for an NH35 watch** with a PCBWay CNC-machined case (Part 1, Jun 15, 2024). Designed in Altium; case in Fusion 360. Lessons he listed: "use copper layers only as there are high chances of a shift in the silkscreen layer"; add O-rings for water resistance; add a case back; improve dust control. Thickness, price and attachment are not stated. — [PCBWay: Dial using PCB, DIY Mechanical Watch Part 2](https://www.pcbway.com/project/shareproject/Dial_using_Printed_Circuited_Board_PCB_DIY_Mechanical_Watch_Part_2_ec745a12.html); [PCBWay: CNC Your Own Watch Case, Part 1](https://www.pcbway.com/project/shareproject/CNC_Your_Own_Watch_Case_DIY_Mechanical_Watch_Part_1_66c76a46.html)
- A search summary of the same project says the order spec was a clear core, white mask, black silkscreen and gold pads. — [PCBWay project page](https://www.pcbway.com/project/shareproject/Dial_using_Printed_Circuited_Board_PCB_DIY_Mechanical_Watch_Part_2_ec745a12.html) (via search summary; not confirmed on fetch)
- **Instructables "PCB Dial Mod for Mechanical Watch" (Seiko 5 SNKK27):** PCBWay-sponsored. The maker says only a few manufacturers could make boards at the 0.2 mm thickness the dial needed. Because the shape differed from the original dial, a 3D-printed holder was used to mount it to the movement. Enamel paint is in the supply list. Traces were routed between hour markers, minute markers and silkscreen text were added, and a logo was placed on exposed copper. — [Instructables: PCB Dial Mod](https://www.instructables.com/PCB-Dial-Mechanical-Watch/) (via search summary; page body did not load on fetch)
- **Hackaday, Mar 7, 2024: Omega Seamaster Calypso replacement dial** by Alex Lorman (STR-Alorman). Workflow: scale-referenced DSLR photos, then Illustrator vectors, then KiCad. He ordered two versions, with and without holes at the indices for lume. The version with cutouts worked better. The dial was glued to the movement with CA glue; getting the glue height right so it would not interfere with the date wheel took about 3 attempts. Commenters recommended dial feet, dial dots or dial adhesive tape instead. The black PCB face shows the board only in certain light. — [Hackaday: Fabbing a fab new watch face](https://hackaday.com/2024/03/07/fabbing-a-fab-new-watch-face/)
- **LumiDial (Hackster):** a 72-LED analog wristwatch PCB ordered with matte black mask and ENIG. The gold hour labels are described as gold-finished. — [Hackster: LumiDial](https://www.hackster.io/taifur/lumidial-a-72-led-analog-wristwatch-powered-by-atmega328-3f6539) (via search summary)
- **JLCPCB case study (Aug 12, 2026):** 40 mm round, 1.0 mm, 2-layer, ENIG, white silkscreen. Thickness was "chosen to fit the watch case", and the board was routed to ±0.1 mm in a mouse-bite frame. — [JLCPCB blog: 72-LED watch](https://jlcpcb.com/blog/precision-72-led-watch-jlcpcb-case)
- **PCB Binary Watch (Electromaker):** a black PCB with ENIG. Top-layer traces were left uncovered (no mask) so the routing shows, with ENIG used to stop the bare traces from corroding. — [Electromaker: PCB Binary Watch](https://www.electromaker.io/project/view/pcb-binary-watch)
- Low-cost PCBs are usually HASL, which can corrode visibly when exposed. This is one reason ENIG is recommended for visible copper. — [Hackster: PCB binary watch news](https://www.hackster.io/news/build-this-stylish-pcb-binary-watch-for-your-wrist-with-a-handful-of-parts-b53541fa3ed0) (via search summary)
- **PCBWay black FR-4 + transparent mask:** ENIG produces a "sandy two-tone". The grey silkscreen was slightly misaligned from the other layers, and PCBWay said non-white silkscreen has a ±6 mil manual-alignment offset. — [Hackaday.io log #9](https://hackaday.io/project/194683-plasma-toroid-sky-guided-pcb-edition/log/230233-9-black-fr-4-and-transparent-soldermask-by-pcbway)
- Restoration-oriented commenters note that watch repairers generally prefer to clean or replace dials rather than modify them. — [Hackaday: Fabbing a fab new watch face](https://hackaday.com/2024/03/07/fabbing-a-fab-new-watch-face/)

### Inferences
- The "copper/ENIG art, minimal silkscreen" approach is the consistent recommendation across the independent sources (Rane, the Hackaday commenters, lcamtuf's silkscreen assessment).
- For an NH35 build, dial feet are not available on a PCB unless brass pins are soldered or pressed into plated holes. Dial dots or dial tape are the pragmatic attachment, with a check on total stack height under the hour wheel and date ring.
- The Hackaday result suggests lume in through-cutouts (lume filled from the front over a backing) is the more reliable approach on a PCB dial.

### Gaps
- Reddit (r/watchmaking, r/SeikoMods, r/PrintedCircuitBoard) could not be searched; the domain is inaccessible to the research tool.
- No precedent source gives a numerical PCB dial thickness for NH35 that worked. Only the 0.2 mm Seiko 5 case (Instructables) and the 1.0 mm electronic watch (JLCPCB) were found.
- No source documented prices paid for a PCB dial order.
- The standard NH35 dial thickness and dial-feet positions were not sourced in this research.

## Q3. Metal case: JLC3DP / JLCCNC / PCBWay prices, tolerances, finishes, threads, lead times, and real reports for a ~40×47×11 mm case

### Takeaway
JLC3DP lists SLM 316L and SLM Ti TC4 from $8 (72–96 h build), with ±0.3 mm tolerance, 1.5 mm minimum wall and a rough Ra 3.2–12 µm surface. Titanium prices were cut 47% on July 24, 2026. No published price exists for a watch-case-sized part. JLC3DP's own 2026 titanium guide puts SLM at $5–20/cm³ and a 30×20×10 mm bracket at $80–150. JLCCNC and PCBWay CNC are quote-only (from $5), with ±0.05 mm CNC tolerance. Real one-off CNC watch-case costs reported elsewhere run from a $150 sample price (Chinese supplier) up to $500–1,000 (an older forum estimate). SLM tolerance is too loose for crystal and gasket seats without post-machining.

### Cited Findings

**JLC3DP SLM / BJ metal**
- JLC3DP homepage: SLM metal (316L, Ti TC4) from $8.00, 3 days, ±0.3 mm. CNC from $5.00, 3 days, ±0.05 mm. SLA resin from $0.30, 2 days, ±0.2 mm. BJ (binder jet) from $5.00, 5 days. All are "From" prices; the final price is from the instant quote. — [JLC3DP homepage](https://jlc3dp.com/)
- SLM 316L spec: from $8.00, 72 h build, tolerance "±0.3mm or within 0.4%", recommended wall 2.0 mm (1.5 mm minimum), max 390×390×290 mm, surface "Ra 3.2–12µm" with minor pitting, 600 MPa tensile, 28 HRC after heat treatment. Updated Sep 08, 2026. — [JLC3DP: 316L Stainless Steel](https://jlc3dp.com/help/article/316l-stainless-steel)
- SLM Ti TC4 spec: from $8.0, 96 h build, ±0.3 mm within 100 mm, recommended wall >1.5 mm, "rough surface (minor pitting)", silver gray. Updated May 21, 2025. — [JLC3DP: Titanium TC4](https://jlc3dp.com/help/article/titanium-tc4)
- BJ-316L spec: from $5.0, 96 h build, ±0.3 mm or ±0.4% for parts ≤50 mm and ±1.3% above 50 mm, wall >1.5 mm, max 100×100×100 mm, Ra 4.0–8.0 µm. Deformation and warping risk increases above 50 mm. Updated May 27, 2026. — [JLC3DP: BJ-316L](https://jlc3dp.com/help/article/bj-316l-stainless-steel)
- July 24, 2026 price update: Titanium TC4 down 47%, PAC-HP nylon down 70%, PA12-CF down 24%, PLA-P down 18%, full-color resin down 11%, ABS down 9%. Spray painting up 16.67%, oil spraying up 14.29%. 316L SLM and BJ-316L are not listed as changed. — [JLC3DP: Material & Service Price Updates, July 2026](https://jlc3dp.com/news/materials-finishing-pricing-update-july2026)
- JLC3DP titanium cost guide (Apr 29, 2026): typical Ti SLM $5–20/cm³; small bracket 30×20×10 mm $80–150; ~25 cm³ solid part ≈ $210 and ~14 cm³ lattice ≈ $160 (example cases). Cost share: machine time 40–70%, post-processing 20–50%, material 10–30%. Tolerance ±0.1–0.2 mm, and tighter tolerances require secondary CNC finishing. — [JLC3DP blog: Titanium 3D printing cost 2026](https://jlc3dp.com/blog/titanium-3d-printing-cost)
- Polishing: JLC3DP offers standard polishing (deburr and brighten) mainly for BJ parts. Fine (near-mirror) polishing was "in internal testing" and not orderable online (help page about 8 months old). No SLM-specific polishing option was found. — [JLC3DP: Metal 3D Printing Polishing](https://jlc3dp.com/help/article/metal-3d-printing-polishing-services) (via search summary)
- JLC3DP's general estimate for mirror polishing is $50–200 per part (about 0.025–0.1 µm Ra). — [JLC3DP blog: Metal surface polishing](https://jlc3dp.com/blog/metal-surface-polishing) (via search summary)
- JLC3DP offers sanding, sandblasting, painting, dyeing and polishing as finishing services in general. — [JLC3DP 316L page / services](https://jlc3dp.com/help/article/316l-stainless-steel) (via search summary)
- An older user review of a JLC3DP stainless print says the results were "top-notch and better than if I printed it myself" (no price given; >2 years old). — [stlDenise3D: 3D printing a stainless steel dumpster fire](https://stldenise3d.com/3d-printing-a-stainless-steel-dumpster-fire/) (via search summary)

**JLCCNC**
- CNC milling and turning from $5.00 with a 3-day build. Materials include aluminum, copper, plastic, steel alloy and stainless steel. — [JLCCNC homepage](https://jlccnc.com/)
- Quotes come back within 2–4 h (Mon–Sat, 9am–6pm GMT+8), with an itemized breakdown of material, machining and heat treatment. Unit price varies with 3- vs 5-axis machining and batch size. — [JLCCNC blog: instant CNC quotation](https://jlccnc.com/blog/instant-cnc-quotation) (via search summary)
- Real totals: a UK forum user got four anodized 7075 parts shipped for about £150, versus £150 for one part elsewhere. A PCBWay forum user got under $180 including shipping from JLCCNC, versus about $422 from another supplier. — [mig-welding.co.uk forum](https://www.mig-welding.co.uk/forum/threads/anyone-got-recommendations-for-wallet-friendly-cnc-milling-services.141021/); [PCBWay: I asked a quote to JLCCNC](https://www.pcbway.com/project/question/I_asked_a_quote_to_JLCCNC.html) (both via search summary; older)
- A Trustpilot reviewer had anodizing defects and had to pay import duties. A remake would have meant another ~$65 in duties. — [Trustpilot: JLCCNC](https://www.trustpilot.com/review/jlccnc.com) (via search summary; ~16 months old)

**PCBWay CNC / metal 3D printing**
- Titanium Gr5 (TC4) CNC is quote-only (five-"$" scale). — [PCBWay CNC titanium](https://www.pcbway.com/rapid-prototyping/cnc-machining/metal/titanium/)
- 316L SLM is quote-only (five-"$" scale). Finishes listed on the page (standard, spray painting, bead blast + anodizing, anodizing, brushed, #1000 sanding) apply to CNC, not to metal printing. — [PCBWay 3D printing stainless steel](https://www.pcbway.com/rapid-prototyping/3d-printing/metal/Stainless-steel/)
- A forum user paid about $30 and waited ~10 days for a PCBWay stainless-printed model engine crankcase. Its four radial lugs warped. — [HomeModelEngineMachinist: Metal 3D print](https://www.homemodelenginemachinist.com/threads/metal-3d-print.36238/) (via search summary; older)
- A 2023 review of PCBWay aluminum CNC found PCBWay cheaper than EU shops, where the cheapest competing quote was $630. Parts arrived 3 days after completion. — [Let's Talk About Tech: PCBWay CNC machining (Mar 2023)](https://www.lets-talk-about.tech/2023/03/pcbway-cnc-machining.html) (via search summary)
- Neeraj Rane's watch case was CNC machined by PCBWay (2024), but material, price and tolerances are not stated. — [PCBWay: CNC Your Own Watch Case](https://www.pcbway.com/project/shareproject/CNC_Your_Own_Watch_Case_DIY_Mechanical_Watch_Part_1_66c76a46.html)
- Trustpilot reviewers report CNC parts in 7075 aluminum and Gr5 titanium with excellent build quality (no prices). — [Trustpilot: PCBWay](https://au.trustpilot.com/review/pcbway.com) (via search summary)

**Other one-off CNC watch-case price signals**
- Easion (Made-in-China): CNC 316L watch case $35–70 at a 100-pc MOQ, with a sample listed at $150/pc. — [Made-in-China: Easion CNC stainless watch case](https://easioncnc.en.made-in-china.com/product/RFZfgdErOpGA/China-China-Custom-CNC-Machining-Milling-Stainless-Steel-Watch-Case.html) (via search summary)
- WatchUSeek (~7 years old): one member estimated a custom case at $500–1,000 if a shop would take it. Another said setup and fixturing, not spindle time, dominate, and planning alone could approach $1,000. A plastic 3D-printed prototype was guessed at under $50. — [WatchUSeek: Custom Watch Case](https://www.watchuseek.com/threads/custom-watch-case.5066347/) (via search summary)
- A volume benchmark puts a 316L case at $6–10/unit at MOQ 300+, with PVD +$2–4. — [Romlicen: Customize watches in China 2026](https://www.romlicen.com/customize-watches-in-china-2026-cost-breakdown-moq-pricing-guide/) (via search summary)
- Stock alternatives: a 40 mm titanium case for NH35/NH36/2824/PT5000 was listed at about $42 on eBay. — [eBay: Titanium watch case 40mm](https://ebay.com/itm/186041292968) (via search summary)
- A 2026 price guide puts 316L printing at $8–20/cm³ and typical stainless parts at $200–800. It says a mid-size stainless bracket CNC'd for about $30 would cost $300–600 printed. — [3dprintmap: How much does 3D printing cost (2026)](https://www.3dprintmap.com/blog/how-much-does-3d-printing-cost) (via search summary)
- A 2024 comparison of instant quotes for the same metal part: Xometry $575.26, Unionfab $45.49, Facfox $46.93. — [Unionfab: Stainless steel 3D printing guide](https://www.unionfab.com/blog/2024/07/3d-printing-stainless-steel) (via search summary)

### Inferences
- A 40×47×11 mm case with a ~2 mm wall probably has a solid volume of roughly 6–12 cm³ (my estimate; not sourced). At JLC3DP's own $5–20/cm³ titanium range, that is about $30–240 before finishing and shipping. The July 2026 47% titanium cut puts the realistic end lower. This needs a real quote.
- At ±0.3 mm and Ra 3.2–12 µm, as-printed SLM cannot hold crystal press-fit seats, gasket grooves or caseback threads. These would need secondary machining (JLC's own guide says tighter tolerances need CNC finishing). Printing is suited to case-shape prototypes or a case that a local machinist then finishes.
- BJ-316L (from $5) is limited to parts ≤50 mm for ±0.3 mm accuracy. A 47 mm case is just inside that limit but is at warping risk.
- SLA resin from $0.30 at ±0.2 mm makes a resin fit-test print of the case very cheap. A few dollars is likely, but this is unverified without a quote.
- CNC (±0.05 mm, JLCCNC/PCBWay) is the only route among these services that can deliver functional seats and threads in one step. One-off realistic pricing is probably in the low hundreds of USD, judging from the $150 sample price and the JLCCNC anecdotes. Import duties into Turkey must be added.

### Gaps
- No real-world report was found of someone ordering a watch case specifically from JLC3DP or JLCCNC with the price paid.
- Thread capability was not documented: neither JLC3DP SLM pages nor JLCCNC pages fetched here state thread support or minimum thread size for watch-scale (e.g., M30×0.5 caseback) threads.
- No published brushing or bead-blast option or price was found for JLC3DP SLM metal parts. PCBWay finishes listed are for CNC only.
- No exact SLA resin price was found for a part of this size.
- Shipping cost and Turkish customs/duty treatment for these orders were not researched. Turkey's current e-commerce duty-free limit and rates were not sourced.

## Q4. Turkey local options: metal SLM, one-off CNC, stainless laser cutting, caseback laser engraving, PCB manufacturing

### Takeaway
Several Istanbul firms claim SLM metal printing in 316L and Ti-6Al-4V: Alpha Tech Design (İkitelli OSB), 3Dbaskıcı (Ümraniye/İkitelli) and Printly Studio (7–10 days). None publishes prices. Turkish CNC is priced by the hour: 2026 vendor estimates are 500–2,000 TL/h for turning, 700–3,000 TL/h for milling and 2,000–7,000 TL/h for 5-axis, with the setup cost loaded fully onto a one-off. Local PCB prototypes cost more than JLCPCB: about $25 for 5 pcs domestic (2023), 500 TL for 1 pc (2025), or $120–125 minimums for imported runs through resellers. No caseback-engraving price list was found.

### Cited Findings

**Metal 3D printing (SLM/DMLS) in Turkey**
- Alpha Tech Design, İkitelli OSB Metal İş Sanayi Sitesi 12B Blok, Başakşehir/İstanbul: SLM metal printing in titanium, 316L and aluminum. — [Alpha Tech Design: Metal 3D baskı](https://alphatechdesign.com.tr/metal-baski-teknolojisi/)
- 3Dbaskıcı: production in Ümraniye and a technical office in İkitelli. Materials: 316L, 17-4 PH, Ti-6Al-4V, AlSi10Mg, CoCrMo, Inconel, H13. — [3Dbaskıcı: Metal baskı teknolojisi](https://3dbaskici.com/metal-baski-teknolojisi/)
- Printly Studio (Istanbul) claims metal DMLS/EBM in titanium, stainless and aluminum, with 7–10 day lead time for metal. — [Printly Studio](https://printly.studio/en/)
- Xometry Türkiye offers online DMLS (aluminum, steel, stainless, Ti-6Al-4V). It states standard as-printed roughness of 150–400 µin Ra. — [Xometry TR: DMLS](https://xometry.com.tr/tr/3d-baski-dmls/)
- Korkmaz Çelik (Ümraniye DOSB) said in 2022 it planned to start metal 3D services (current status unknown). — [Korkmaz Çelik: 3D metal ürün hizmetleri](https://www.korkmazcelik.com/3d-metal-urun-hizmetleri)
- Armut lists "164 3D metal baskı firması" for Istanbul, but many listed providers only do FDM plastics. — [Armut: İstanbul 3D metal baskı](https://armut.com/istanbul-3d-metal-baski)
- A Turkish source says the main cost in steel printing is print time and post-processing rather than material quantity. — [arti90: 3D baskı fiyatları](https://arti90.com/tr/3d-baski-fiyatlari/) (via search summary)

**One-off CNC machining in Turkey**
- A 2026 Turkmaksan estimate for industrial zones including Istanbul: CNC turning (2–3 axis) 500–2,000 TL/h, milling 700–3,000 TL/h, 5-axis 2,000–7,000 TL/h. Programming time, fixturing trials and measurement are loaded fully onto a single part. — [Turkmaksan: CNC işleme fiyatları 2026](https://www.turkmaksan.com.tr/cnc-isleme-fiyatlari/) (via search summary)
- Armut Istanbul CNC contract machining shows a general band of 500–10,000 TL. One example request (a 7000-series aluminum box) had a 650–1,000 TL budget. These are customer budgets, not quotes. — [Armut: İstanbul CNC fason imalat fiyatları 2026](https://armut.com/fiyatlari/istanbul-cnc-fason-imalat_198_34); [Armut: CNC fason imalat fiyatları 2026](https://armut.com/fiyatlari/cnc-fason-imalat_198)
- Tornelle (İkitelli OSB) does CNC turning and milling from prototype to series, and claims same-day price and lead-time replies when sent a drawing. — [Tornelle](https://www.tornelle.com/)
- Sural Makina takes one-off prototypes through to series (location unverified). — [Sural Makina](https://suralmakina.com.tr/talasli-imalat-cnc-isleme-ve-hassas-parca-uretimi-sural-makina/)
- Ostim (Ankara): Öz Alper CNC (turning and milling, 600 m², active since 2010) and Model CNC Makina (founded 2004 in Ostim). — [OSTİM: Öz Alper CNC](https://www.ostim.org.tr/oz-alper-cnc); [OSTİM Savunma: Model CNC](https://www.ostimsavunma.org/companies/model-cnc-makina-sanayi-limited-sirketi-1)
- "Perpa Makina" is a machine-tool importer and seller rather than a job shop. — [MAKTEK: Perpa Makina](https://www.maktekfuari.com/katilimci-listesi/perpa-makina-endustri-sanayi-ve-ticltdsti-145537-3162)

**Stainless laser cutting**
- Stainless sheet laser cutting costs about 25–45 TL/kg (example range; may or may not include material). Many holes and small geometries raise cost. Published Aug 19, 2026, updated Sep 2026. — [Bilgin Metal: CNC sac kesim fiyatları 2026](https://bilginmetal.net/cnc-sac-kesim-fiyatlari-2026/)
- Armut laser-cutting pages show no prices and direct users to request quotes (e.g., 646 laser-cutting firms listed for Eyüp). — [Armut: Eyüp lazer kesim](https://armut.com/eyup-lazer-kesim)

**Caseback laser engraving**
- No Turkish price list for caseback engraving was found. Casio Turkey's personalization program gives an 85×85 mm engraving area; large engravings take twice as long, and laser engraving offers no color choice. — [Casio TR: Saatlerini özelleştirerek hediye edin](https://www.casio-intl.com/tr/tr/wat/for_gift/)
- Caseback engraving is typically 15–20 characters per line depending on case size. Engraving on sapphire casebacks is much harder than on metal (article about 5 years old). — [Horobox: Saatinizin arkasına yazı yazdırmak](https://www.horobox.com/haber-detay/saatinizin-arkasina-yazi-yazdirmak)
- Raw stainless needs fiber or IR lasers; a blue diode laser is ineffective on raw stainless. — [Atomm: How to engrave metal (2026)](https://www.atomm.com/uk/blog/2204-how-to-engrave-metal) (via search summary)

**PCB manufacturing in Turkey**
- On a Turkish Q&A thread (Nov 2023–Oct 2025):
  - Erkar Elektronik (İzmir) quoted 5 pcs domestic for $25 incl. VAT, also valid for 1 pc.
  - Some firms quoted about $150 for a single-sided sample.
  - Sedat Dijital quoted 3 pcs for $29 (Mar 2024).
  - İstanbul PCB Üretimi quoted 1 pc for 500 TL incl. shipping (Apr 2025); a commenter noted VAT and stamp tax of 443.70 TL.
  — [prototippcb.com.tr: Numune baskı devre fiyatı](https://www.prototippcb.com.tr/76/numune-bask%C4%B1-devre-fiyat%C4%B1)
- The same site names Özde PCB and Güler PCB as good value for domestic samples. An anonymous answer claims most "domestic" sellers actually resell JLCPCB boards (unverified). — [prototippcb.com.tr: Türkiye'de PCB üretimi yapan firmalar 2026](https://prototippcb.com.tr/701/t%C3%BCrkiyede-pcb-%C3%BCretimi-yapan-firmalar-2026-g%C3%BCncel)
- İzmir PCB's imported sample service is a $125 fixed price incl. VAT (e.g., 700 pcs at 30×30 mm). — [İzmir Numune PCB: Fiyat hesaplama](https://www.izmirnumunepcb.com/prototip-pcb-fiyat-hesaplama-siparis-formu) (via search summary)
- Another seller has a $120 minimum for imported prototypes with 8–21 day delivery. — [prototippcb.com.tr](https://prototippcb.com.tr/19/pcb-t%C3%BCrkiye) (via search summary)
- Pratik PCB offers Express 1-day, 3-day and 1-week production in Turkey (Manisa and Istanbul). 5–10 pc prototypes are made in China and air-freighted. — [Pratik PCB](https://pratikpcb.com/) (via search summary)
- Turkish reseller extra fees: up to about $30 per design for 5–30 pc prototype orders; ENIG about $30/m². — [Infoset: PCB üretiminde ekstra ödemeler](https://infoset.help/wdzfhxvzjbmlhbrc/tr/articles/3480-pcb-baski-devre-karti-uretiminde-ekstra-odemeler) (via search summary)

### Inferences
- For a one-off case, the most cost-effective local route is probably to print a resin or metal blank abroad (or locally) and have an Istanbul CNC job shop machine the functional features (crystal seat, caseback thread). One to two hours of turning or milling at 500–3,000 TL/h is plausible, plus setup. This is unverified without quotes.
- For the PCB dial, local options are more expensive than ordering directly from JLCPCB/PCBWay. Local resellers mostly import from China anyway, and they rarely state ENIG + black + 0.4 mm capability.

### Gaps
- No published TL prices for SLM metal printing from any Turkish provider. All require a quote.
- No sample quote for a one-off watch case from İkitelli, Perpa or Ostim shops.
- No price list for laser engraving a stainless caseback in Turkey (e.g., per-piece jeweler or engraver fees).
- No confirmed Turkish domestic PCB maker capable of 0.4 mm + ENIG + black mask.

## Q5. AliExpress and other custom services: custom-printed dials, engraved casebacks, rotors, bezel inserts

### Takeaway
AliExpress sellers offer custom logo or text printed onto stock NH35-size dials (26.8, 28.5, 31 and 35 mm). Search pages show prices of about $6.77–34.39. An older WatchUSeek report quoted $50 for a logo template plus $10 per print, applied to a pre-made dial rather than a fully custom artwork dial. Custom engraved NH35 rotors are mostly on Etsy at about $46–65. No print-your-own bezel insert service was found.

### Cited Findings
- AliExpress custom-logo NH35 dial listings come in 26.8, 28.5 and 35 mm sizes (some 31 mm), in black, white and brushed finishes, with silk-printed or laser-printed logos. One results page showed prices of about $6.77–34.39. — [AliExpress: Custom watch dial logo printing](https://www.aliexpress.com/w/wholesale-custom-watch-dial-logo-printing.html); [AliExpress: Custom watch dials for NH35](https://www.aliexpress.com/w/wholesale-custom-watch-dials.html) (via search summary)
- A specific listing offers a "Customized Personalization Custom Logo Laser Print Name/Logo Watch Dial" in brass, 28.5–31 mm, fitting NH35/NH36/ETA2824/2836/Miyota 8215 (listing about 1,764 days old). — [AliExpress item 1005001280608555](https://www.aliexpress.com/item/1005001280608555.html) (via search summary)
- A WatchUSeek thread (over 3 years old) reported a seller quote of $50 for the logo template, $35 for the text, then $10 per printing. The service only added text or a logo onto a pre-made dial. — [WatchUSeek: Custom dials on Ali Express](https://www.watchuseek.com/threads/custom-dials-on-ali-express-has-anyone-done-one.5504320/) (via search summary; thread body blocked at fetch)
- None of the AliExpress listings found states an MOQ for custom-logo dials. — [AliExpress: Custom watch dial](https://www.aliexpress.com/w/wholesale-custom-watch-dial.html) (via search summary)
- Custom engraved NH35 rotors on Etsy cost about $46 and $65 (two listing snapshots). A decorative wave-pattern rotor cover overlay costs about $7.59. — [Etsy: NH35 rotor custom](https://www.etsy.com/market/nh35_rotor_custom); [Etsy: NH35 rotor engraved](https://www.etsy.com/market/nh35_rotor_engraved) (via search summary)
- AliExpress "custom watch NH35" results mostly return complete watches with a customizable logo, at about $79.5–106. — [AliExpress: Custom watch NH35](https://www.aliexpress.com/w/wholesale-custom-watch-nh35.html) (via search summary)
- Stock aftermarket NH35 dials in specialty designs (carbon fiber, meteorite) cost about $30–165 from an eBay store. — [eBay: dialmarker store](https://www.ebay.com/str/dialmarker) (via search summary)

### Inferences
- An AliExpress logo-on-stock-dial service is the cheapest "custom dial" route (probably under $20–60 total for 1 pc, including template fees), but it is not a fully custom artwork dial. A PCB dial from JLCPCB/PCBWay offers more design freedom at a similar price.

### Gaps
- No current (2026) AliExpress seller data on full-artwork custom dials (MOQ, setup fee, per-piece price).
- No AliExpress or other service found for custom-printed bezel inserts from your own artwork.
- No AliExpress custom-engraved caseback service or price found.
- AliExpress product pages were not fetched directly (prices are from search-result snapshots).
