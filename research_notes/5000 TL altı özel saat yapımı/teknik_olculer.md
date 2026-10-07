# Technical dimensions for custom dial + case design: Seiko/TMI NH35A family (NH35A, NH36A, NH38A, NH39A, NH70A/NH72A)

Notes on method. All primary numbers below come from the official SII/TMI "Watch Movement Specification and Drawing" PDFs. I downloaded them, rendered them to images and read the drawings directly. Every drawing is dimensioned in **1/100 mm** (title block: "Unit: 1=1/100mm"), so "2850" means 28.50 mm. I have converted everything to mm.

Polar coordinates (radius, and angle measured clockwise from 12 o'clock, seen from the dial side) are **my own arithmetic** from the X/Y dimensions in the drawings. They are marked "(calc.)".

Primary sources:
- TMI NH35A spec sheet, revised 16-11-2022: [TMI NH35_SS.pdf](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- SII NH35A spec, issued 14-Feb-2011: [SII/Hattori NH35 Specification](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- SII NH35A spec, rev. 11-Dec-2013, bundled with the NH3-series Technical Guide: [okta.ua NH35A PDF](https://okta.ua/files/pdf/1482851267NH35A.PDF)
- NH3 Technical Guide & Parts Catalogue: [NH35_TG.pdf](https://watch-help.ru/upload/iblock/f76/1wrteqbztomm6zep30qs6rl1babauix4/NH35_TG.pdf)
- TMI sheets for the other calibres: [NH36](https://timemodule.com/upload/category/25/spec_sheet/NH36_SS.pdf), [NH38](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf), [NH39](https://timemodule.com/upload/category/28/spec_sheet/NH39_SS.pdf), [NH70](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf), [NH72](https://timemodule.com/upload/category/31/spec_sheet/NH72_SS.pdf)
- Sheets that also exist but were not read in detail: [NH34](https://timemodule.com/upload/category/23/spec_sheet/NH34_SS.pdf), [NH37](https://timemodule.com/upload/category/26/spec_sheet/NH37_SS.pdf), [NH71](https://timemodule.com/upload/category/30/spec_sheet/NH71_SS.pdf)

## 1. Movement: core dimensions, stem, and functional specs

### Takeaway
The NH35A is Ø27.40 mm bare and 5.32 mm thick, and Ø29.36 mm with the dial-holding spacer. The case bore for the spacer is Ø29.30 ±0.03 mm. The stem axis is 1.92 mm below the dial-seat surface, and the stem thread is S0.90 × P0.225 (tap 10). Function specs: 21,600 vph, 24 jewels, >41 h reserve, hacking and hand-winding. The current official accuracy figure is −20/+40 s/day; the 2011 sheet said −25/+35.

### Cited Findings
**Size and height**
- Outside diameter Ø27.40 mm. Casing diameter Ø29.36 mm with the dial-holding spacer. Total height 5.32 mm. 12 ligne. — [TMI NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf); [SII 2011 spec](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- Casing drawing: spacer "case fitting diameter" is Ø29.36 +0.10/−0.03. Two other spacer diameters are drawn: Ø29.255 and Ø27.40 ±0.03. The back of the movement shows Ø26.80 and Ø23.94. — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Centre-post height above the "main plate surface" is H1 = 2.267 mm (Type M) or 2.667 mm (Type L). Total height including the movement is H2 = 7.587 mm (M) or 7.987 mm (L). — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Third-party figures for comparison: Lucius Atelier gives an "installed height" of 7.59 mm for NH35/36/38 and 7.99 mm for NH34. Caliber Corner lists 7.55 mm "with cannon pinion". — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows); [Caliber Corner NH35A](https://calibercorner.com/seiko-caliber-nh35a/) (search snippet)

**Vertical stack from the official casing and assembly drawings (Type M)**
- Measured from the dial-seat reference ("main plate surface"):
  - Stem axis is 1.92 mm below it.
  - The spacer extends 2.94 mm below it (a second step at 2.62 mm), and the spacer's lower foot is 0.68 mm wide radially.
  - A spacer step sits 0.59 mm below it.
- At the back of the movement: the rotor rim chamfer is 0.304 mm and the central boss 0.15 mm. Clearance from the lowest point to the case-back plane is 0.40 mm.
- — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Assembly plan dimensions:
  - F, dial top to glass underside: 2.36 mm (M) / 2.76 mm (L).
  - G, glass underside to the spacer step: 3.35 mm (M) / 3.75 mm (L).
  - Dial top to case-back inner surface: 6.12 mm.
  - Rotor to case back: 0.40 mm at the centre and 0.55 mm at the periphery.
  - Case bore height: 2.18 mm.
  - Case bore ("Casing diameter"): Ø29.30 ±0.03 mm.
  - "Dimension to press the projections": 0.03 mm radial and 0.17 mm.
  - — [TMI NH35_SS, "Assembly Plan"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Stem pull-out strokes: "First pull out stroke 39.9" and "Second pull out stroke 40.0" in 1/100 mm, i.e. about 0.40 mm per click. — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Plan view (stem pointing up): 25.05 mm from the movement centre to the stem end, 13.95 mm to an intermediate point, and a "210" (2.10 mm) dimension at the stem. — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)

**Stem**
- Stem part 0351 200. Thread S90×P22.5, i.e. Ø0.90 mm × 0.225 mm pitch. Overall length B = 21.48 mm, A = 11.00 mm. Shaft and shoulder diameters are Ø1.10 mm (one listed as Ø1.10 +0.001/−0.01). Other dimensions: 2.966, 0.134 and 0.40 mm. — [TMI NH35_SS, "Hand Setting Stem"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Third-party confirmation: Caliber Corner lists stem #351-200 as tap 10. Esslinger equates "tap 10" with 0.90 mm. — [Caliber Corner NH35A](https://calibercorner.com/seiko-caliber-nh35a/); [Esslinger screw-down crown kit](https://www.esslinger.com/extra-large-threaded-screw-down-crown-and-tube-kit/)
- A WatchUSeek post independently quotes the 1.92 mm stem height "from front of movement" as critical. — [WatchUSeek](https://www.watchuseek.com/threads/help-where-do-i-find-internal-case-dimensions.5463097/)

**Functions and performance**
- 24 jewels. 21,600 vph (6 beats/s). Duration "more than 41 hours". Antimagnetic ≥4800 A/m (DC). Manual winding plus automatic winding with ball bearing ("both winding with one way clutch"). Date with quick correction. "Second hand stop mechanism", i.e. hacking. — [TMI NH35_SS, "Specification"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Crown functions:
  - Normal position: clockwise winds, counter-clockwise is free.
  - 1st click: counter-clockwise sets the date.
  - 2nd click: time setting with second-hand reset.
  - — [SII 2011 spec](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- Accuracy:
  - **−20 to +40 s/day** at 23 ±2 °C in the 2013 and 2022 sheets.
  - **−25 to +35 s/day** in the 2011 SII sheet.
  - Retail listings that cite Seiko's own 4R38 figure give −35/+45.
  - — [TMI NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf); [okta.ua 2013 rev.](https://okta.ua/files/pdf/1482851267NH35A.PDF); [SII 2011](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf); [Grail Watch 4R38](https://reference.grail-watch.com/movement/4r38/) (search snippet)
- Technical Guide:
  - Lift angle 53°.
  - Measured in 3 positions; posture difference under 60 s across 4 positions; isochronism −20/+40 s/day.
  - Fully wound by at least 55 crown turns, or 8 turns of the ratchet-wheel screw.
  - — [NH3 TG](https://watch-help.ru/upload/iblock/f76/1wrteqbztomm6zep30qs6rl1babauix4/NH35_TG.pdf)
- Casing requirements: "The movement is fixed by dial holding spacer". "Screw type case back is required". "Non-corresponding with Diver's watch". — [SII 2011 spec](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf); [TMI NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Hand-fitting force limits: hour and minute < 50 N, second < 30 N. — [SII 2011 spec](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)

### Inferences
- Stem axis height for a 0.40 mm dial, Type M (calc.):
  - 2.32 mm below the dial top.
  - 4.68 mm below the crystal underside (2.36 + 0.40 + 1.92).
  - 3.80 mm above the case-back inner surface (6.12 − 2.32).
  - Use this to position the crown-tube bore. With the stem axis at 1.92 mm below the dial seat, the tube hole centre must sit at exactly that height relative to the case's dial-seat ledge.
- Minimum inner cavity, crystal underside to case-back inner face (calc.): 2.36 + 6.12 = **8.48 mm (Type M)** or **8.88 mm (Type L)**. Crystal and case-back thicknesses come on top of that.
- Spacer fit (calc.): the Ø29.36 projections go into a Ø29.30 bore, a nominal 0.06 mm diametral interference (0.03 per side, matching the drawing's "3"). This is a light press fit; the screw case back then presses the spacer axially. The spacer body at Ø29.255 has about 0.045 mm diametral clearance.
- The casing plan view is drawn from the **case-back side**. The dial-leg holes appear mirrored relative to the dial drawing; the angle check works out to 41.9° from the stem in both views.

### Gaps
- What the 13.95 mm and 2.10 mm stem-area dimensions refer to is my interpretation; the drawing gives no label.
- The 0.17 mm "dimension to press the projections" is not explained further in the sheet.
- No official crown-tube or crown dimensions exist; Seiko leaves these to the case maker.
- The stem cut length for a given case cannot be derived without the case's tube and crown geometry.
- I found no source saying whether retail NH35A movements ship as Type M or Type L. Check the hour-wheel height (0.88 vs 1.28 mm) or ask the supplier.

## 2. Model differences: date / no-date, open heart, skeleton, and where the openings are

### Takeaway
NH35 = 3 hands + date. NH36 = day-date. NH37 = date + 24 h. NH38 = 3 hands, no date, open-heart dial opening. NH39 = no date + 24 h hand + open-heart opening. NH70A and NH72A are skeletons with no date; they differ only in plating (nickel vs ruthenium grey). The NH38/NH39 open-heart window is up to Ø10.00 mm, centred 6.85 mm from the centre at about 265° (just below 9 o'clock). NH70/72 are mechanically different to case: Ø31.50 ring dial, casing ring and two clamps, and different dial-foot positions.

### Cited Findings
- Functions table in the NH3-series Technical Guide:

  | Calibre | Date | Day | 24 h |
  |---|---|---|---|
  | NH35 | yes | – | – |
  | NH36 | yes | yes | – |
  | NH37 | yes | – | yes |
  | NH38 | – | – | – |
  | NH39 | – | – | yes |

  All five have 3 hands, manual and automatic winding, and stop-seconds. — [NH3 TG](https://watch-help.ru/upload/iblock/f76/1wrteqbztomm6zep30qs6rl1babauix4/NH35_TG.pdf); [Cousins NH3 part sheet](https://cousinsuk.com/pdf/categories/6810_seiko%20nh3%20series%20part%20sheet.pdf)
- NH38A spec: "Three Hands". 24 jewels, −20/+40 s/day, 21,600 vph, >41 h, ≥4800 A/m, screw case back required. — [TMI NH38_SS](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf)
- **NH38A open-heart dial opening:**
  - Diameter: MAX Ø10.00 mm.
  - Centre: x = −6.827 mm (towards 9 H), y = −0.558 mm (below the 3–9 axis).
  - Same dial (Ø28.50) and same feet F1/F2 as the NH35.
  - — [TMI NH38_SS, "Dial"](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf)
- **NH39A dial:**
  - Same MAX Ø10.00 open-heart opening at the same position (682.7 / 55.8).
  - 24-hour hand hole Ø0.80 ±0.05 at x = −3.656, y = +4.478; drawn as R 5.781 mm at 50.8° above the 9 H axis.
  - Same feet as NH35.
  - — [TMI NH39_SS, "Dial"](https://timemodule.com/upload/category/28/spec_sheet/NH39_SS.pdf)
- Secondary confirmation: the 4R38/NH38 open-heart balance is described as "at 9:00". — [Grail Watch 4R38](https://reference.grail-watch.com/movement/4r38/) (search snippet); [Caliber Corner NH38A](https://calibercorner.com/seiko-sii-caliber-nh38a/) (search snippet)
- Lucius Atelier: open-heart dials "ship with two legs and are built for a 3 o'clock crown only". — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows)
- **NH70A** spec: "Three Hands (skeleton), Nickel plating". 24 jewels, −20/+40 s/day, 21,600 vph, >41 h. "Non-corresponding with Diver's watch". No screw-back requirement is listed. — [TMI NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- **NH72A** spec: "Three Hands (skeleton), Ruthenium grey plating". Otherwise identical to NH70A. — [TMI NH72_SS](https://timemodule.com/upload/category/31/spec_sheet/NH72_SS.pdf)
- **NH70A/NH72A dial (ring):**
  - Outer Ø31.50 ±0.05; thickness 0.40 ±0.04; inner aperture Ø23.90 MAX.
  - Feet: F1 at x = −10.60, y = +7.428; F2 at x = +8.322, y = −9.932.
  - Foot Ø0.74 +0.015/−0.01; length 2.00 +0.05/−0.10; base MAX Ø1.00.
  - The feet go into a "dial leg pin" with 1.66 mm engagement.
  - — [TMI NH70_SS, "Dial"](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf); [TMI NH72_SS, "Dial"](https://timemodule.com/upload/category/31/spec_sheet/NH72_SS.pdf)
- **NH70A casing:**
  - No dial-holding spacer. The sheet lists a "Casing Ring", a "Dial support" and a "Casing clamp".
  - Movement case-fit diameter Ø27.00 +0/−0.032; dial support Ø27.45; stem axis 1.92 mm below the main-plate surface, as on the NH35.
  - Single pull-out stroke of 0.427 mm (no date position).
  - Clamp screw S100×P17.5, i.e. M1.0 × 0.175.
  - — [TMI NH70_SS, "Casing"](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- NH70A casing ring (SUS304):
  - Outer Ø32.30 −0.02/−0.07; inner Ø27.03 ±0.02.
  - Other diameters: Ø27.40, Ø27.60, Ø27.85, (Ø29.60), (Ø31.35), (Ø32.00). Height (3.75).
  - Stem slot 2.00 ±0.05 wide at 3 H.
  - Two clamp notches 2.40 ±0.05 wide at R15.15, located 25.3° ±0.5° above 3 H and 126.7° ±0.5° below 3 H.
  - Case "Casing diameter" Ø32.30 ±0.03. Clearances *30 (0.30 mm) and *40 (0.40 mm) are "STRONGLY RECOMMENDED … without modifications".
  - — [TMI NH70_SS, "Casing Ring" and "Assembly Plan"](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- NH70A casing clamp: 2.10 ±0.03 wide, 1.05 + 5.00 long (6.05 mm), 0.45 ±0.01 thick, hole Ø1.15 ±0.02, R0.50 corners, SUS631-CSP 3/4H at Hv500 ±30. — [TMI NH70_SS, "Casing Clamp"](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- Conflicts between third-party claims and the official sheets:
  - Caliber Corner says the NH72's dial feet "sit in the same positions as the other NHXX calibers". The official sheets show different coordinates and a 0.74 mm foot instead of 0.64 mm. — [Caliber Corner NH72](https://calibercorner.com/seiko-caliber-nh72/) (search snippet), contradicted by [TMI NH72_SS](https://timemodule.com/upload/category/31/spec_sheet/NH72_SS.pdf)
  - Lucius says the NH70/71/72 "with the spacer fitted … match the ø29.36mm casing diameter". The official NH70 sheet specifies a Ø32.30 casing ring and no spacer. — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows), contradicted by [TMI NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
  - Caliber Corner also gives the NH70 "casing diameter" as 27 mm, which matches the official Ø27.00 movement fit (search snippet).

### Inferences
- NH38/NH39 open-heart centre (calc.): **r = 6.850 mm at 265.3°** clockwise from 12, which is 4.7° below the 9 o'clock line.
  - The Ø10.00 window spans radially from 1.85 to 11.85 mm. Its edge is about 0.82 mm from the edge of the Ø2.05 centre hole.
  - Do not exceed Ø10.00; a smaller aperture centred on the same point is safe.
- NH39 24 h hand hole (calc.): r = 5.781 mm at 320.8°.
- NH70/72 dial feet (calc.): F1 r = 12.94 mm at 305.0°, F2 r = 12.96 mm at 140.0°.
- NH70/72 clamps (calc., converted from the back-view drawing to dial view): r = 12.56 mm at about 64.7° and 216.7°. These match the ring-notch angles (90 − 25.3 = 64.7° and 90 + 126.7 = 216.7°).
- A case designed for the NH35 (Ø29.30 bore, spacer press-fit) will **not** accept an NH70/72 without the Ø32.30 casing ring. Choose the calibre before cutting the case.
- For a no-date design, the NH38A is the official option with a Ø28.50 dial and NH35 feet. A plain no-date dial covers its balance unless you cut the Ø≤10 mm window.

### Gaps
- I did not read the NH70/72 "Dial support" page in detail; its exact geometry was not extracted.
- NH71 (gilt skeleton) is listed by third parties, and a TMI sheet exists for it (category 30), but I did not read it.
- The NH34 (GMT) sheet was not read. Lucius says the NH34 needs a 2.7 mm dial centre hole.

## 3. Dial: diameter, thickness, feet, centre hole, date window, under-dial space

### Takeaway
Official NH35/36/38/39 dial values:
- Ø28.50 ±0.05 mm diameter, 0.40 ±0.04 mm thick, Ø2.05 ±0.05 mm centre hole.
- Two feet, Ø0.64 mm × 2.15 mm long, at r ≈ 13.0 mm and about 48.1° / 226.7° (crown at 3).
- Date window at 3 H: 2.90 mm (radial) × 2.00 mm, centred 10.55 mm from the centre.
- NH36 day-date window: 7.00 × 2.00 mm, centred at 8.45 mm.
- For a 3.8/4 o'clock crown the feet move by about 24° (Lucius: the 12- and 42-minute positions). Date-numeral orientation in that layout is not covered officially.

### Cited Findings
**Dial blank and feet (NH35A "Dial-1")**
- Dial Ø28.50 ±0.05. Thickness 0.40 ±0.04. Centre hole Ø2.05 ±0.05. — [TMI NH35_SS, "Dial-1"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Feet (crown at 3 H): **F1 at x = +9.672, y = +8.667** (upper right). **F2 at x = −9.466, y = −8.930** (lower left). — [TMI NH35_SS, "Dial-1"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Foot geometry: Ø0.64 +0.015/−0.01; length 2.15 ±0.10; tip chamfer 25° over 0.15 mm; base or attachment Ø1.00. — [TMI NH35_SS, "Dial-1"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- The spacer's dial-leg holes are drawn on the casing plan view on a circle labelled Ø27.40 ±0.03. — [TMI NH35_SS, "Casing"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- "The dial is fixed by two dial leg holes of dial holding spacer". — [SII 2011 spec](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- Crown-at-9 version ("Dial-2"): the same layout mirrored through 180°. F2 at (+9.466, +8.93), F1 at (−9.672, −8.667), date window at 9 H. — [TMI NH35_SS, "Dial-2"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- NH36A, NH38A and NH39A dial sheets repeat Ø28.50, 0.40, Ø2.05 and the same F1/F2 coordinates and foot dimensions. — [NH36_SS](https://timemodule.com/upload/category/25/spec_sheet/NH36_SS.pdf); [NH38_SS](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf); [NH39_SS](https://timemodule.com/upload/category/28/spec_sheet/NH39_SS.pdf)

**Date windows**
- NH35A date window at 3 H: **2.90 mm wide (radial) × 2.00 mm tall**, centre 10.55 mm right of centre. — [TMI NH35_SS, "Dial-1"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- The same sheet also draws a 6 H window: 2.00 wide × 2.90 tall, centre 10.55 mm below centre. — [TMI NH35_SS, "Dial-1"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- NH36A day-date window at 3 H: **7.00 mm (radial) × 2.00 mm**, centre 8.45 mm from centre. A 6 H variant is also drawn. — [TMI NH36_SS, "Dial"](https://timemodule.com/upload/category/25/spec_sheet/NH36_SS.pdf)
- The parts catalogue lists only date dials for crown 3 H / frame 3 H: 0878 208 (NH35/NH37, black on white) and 0878 206 (NH36). — [NH3 TG](https://watch-help.ru/upload/iblock/f76/1wrteqbztomm6zep30qs6rl1babauix4/NH35_TG.pdf); [Cousins NH3 part sheet](https://cousinsuk.com/pdf/categories/6810_seiko%20nh3%20series%20part%20sheet.pdf)
- Lucius says a 6 H date needs a special-order "NH35 Date @ 6H". It also says "a standard NH35's date sits at the 4:30 position"; that statement is unclear and unverified. — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows)

**Crown at 3.8 / 4 o'clock**
- Lucius: aftermarket dials carry four feet in two pairs. Keep the pair under the **8 and 38 minute markers** for a 3 o'clock crown, and the pair under the **12 and 42 minute markers** for a 4 o'clock crown. After clipping, "about 0.1–0.2 mm still protrudes". — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows)
- Watch-Modz dials have four feet "for either a 3:00 or 3:45 crown". Dial Maker offers feet at 3.0 or 3.8, and its selector also lists 3.18. — [Watch-Modz cage dial](https://watch-modz.com/product/nh35-dial-silver-cage/); [Dial Maker](https://www.dialmaker.shop/products/skeletonized-dial-for-nh35-1) (search snippets)
- A forum reply says the date "lines up at 3 and 3.8", while a day wheel is orientation-specific. The same poster says cheap eBay movements use the grey spacer and real Seiko cases need the black spacer. — [WatchRepairTalk (bklake)](https://www.watchrepairtalk.com/profile/7015-bklake/content/) (search snippet; unverified)
- Forum guidance: an NH35 "3" and "3.8" date-only movement are the same and can go in a 4.1 case using dial dots; an NH36 should not be used in a 4.1 case. — [WatchRepairTalk dial feet thread](https://www.watchrepairtalk.com/topic/23165-dial-feet-position-nh35-vs-eta-2824/) (search snippet)
- Aftermarket listings sell NH35/NH36 movements described as "crown at 3.8". — [eBay listing](https://www.ebay.de/itm/177534110382)

**Dial diameters in use**
- "The Seiko dial standard is ø28.5mm". A slightly oversized dial "up to around 29mm" still fits. — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows)
- Many aftermarket dials are 28.5 mm; one seller lists 0.44 mm thickness. — [Watch-Modz](https://watch-modz.com/product/nh35-dial-silver-cage/) (search snippet)
- Some NH35 cases are sold as suiting "28.5mm–30.5mm" dials, and a 40 mm square case is described as fitting a 30.5 mm dial. — marketplace and video listings (search snippets; low reliability)
- 31.50 mm is the official NH70/72 skeleton ring-dial size. — [TMI NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)

**Dial thickness tolerance (practitioner)**
- 0.4 mm is ideal. 0.5 mm adds about 0.1 mm to case height. 0.6 mm is "the practical limit". About 1.2 mm is a hard wall because the hour hand cannot seat. — [Lucius Atelier guide](https://luciusatelier.com/blogs/news/complete-seiko-mod-dial-compatibility-guide-nh34-nh35-nh36-dial-feet-sizes-date-windows)

### Inferences
- **NH35 feet in polar form, crown at 3 (calc.):**
  - F1: r = 12.987 mm at 48.14° (the 8.0-minute mark).
  - F2: r = 13.013 mm at 226.67° (the 37.8-minute mark).
  - They are not diametrically opposite; the angular separation is 178.5°.
  - This matches Lucius's "8 and 38 minute markers" exactly, so the official sheet and the practitioner guide agree.
- **Feet for a crown at 3.8 (calc.):** rotate by about +24° (or +23.2°, two date steps, since 360/31 = 11.61° per step).
  - F1 ≈ 72.1° → (x = 12.36, y = 3.98).
  - F2 ≈ 250.7° → (x = −12.28, y = −4.31).
  - This matches Lucius's "12 and 42 minute markers" for the 4 o'clock pair. **Verify on a real movement before cutting.**
- **Date window at 3 H (calc.):** the window spans radially from r = 9.10 to 12.00 mm, and its outer edge is 2.25 mm inside the Ø28.50 dial edge.
  - Keep a printed chapter ring or minute track either outside r = 12.0 mm or interrupted around the window.
  - A smaller, tidier cut-out can sit inside the 2.90 × 2.00 frame. The numeral itself is smaller than the frame, but its height was not given.
- **Day-date window (calc.):** spans r = 4.95–11.95 mm.
- **Crown at 3.8:** the window stays at the dial's 3 o'clock (r = 10.55). Because the disc indexes in 11.6° steps, a 23.2° rotation lands centred on a numeral, but standard 3 H-printed numerals would appear tilted by about 23°. I could not verify whether "3.8" movements use a disc printed to compensate (as Seiko does for its own crown-at-4 4R models).
- **Under-dial space:** the dial lies directly on the movement's top reference surface. In the hand-fitting drawing, D = 0.40 is the dial thickness, measured from the movement surface to the dial top. The date disc and its maintaining plate therefore sit inside the 5.32 mm movement height, under that surface. Raised dial features must go upward (into the 0.60 mm dial-to-hour-hand gap), not downward.
- **Larger dial (29–31.5 mm) on NH35:** the spacer is Ø29.36, so a dial above about 29.3 mm overhangs the spacer. The case then needs a dial-seat ledge or recess above the spacer step (the 0.59 mm zone in the drawing). This is my inference from the casing drawing.

### Gaps
- Exact date-numeral height and font position on the date disc: not on the dial sheet.
- Date-disc thickness and depth below the dial surface: not found. The visible depth through the window needs measuring on a sample.
- Official confirmation of a crown-at-3.8 NH35A variant and its date-disc part number: none found (the TG lists only 3 H).
- The official foot positions for a 4.1 crown are not given anywhere.

## 4. Hands: hole diameters, heights, clearances, and the effect of a thicker dial

### Takeaway
Official hand holes: hour Ø1.50, minute Ø0.88, seconds Ø0.198 mm. Shaft diameters: hour-wheel pipe Ø1.506, cannon pinion Ø0.891, fourth pinion Ø0.215 (tapered). For Type M with a 0.40 mm dial the stack is:

| From dial top | Height (mm) |
|---|---|
| Dial to hour hand underside | 0.60 |
| Hour hand top | 0.78 |
| Minute hand top | 1.37 |
| Seconds hand top | 1.91 |
| Seconds hand to crystal (minimum) | 0.45 |

That puts the crystal underside 2.36 mm above the dial (2.76 mm for Type L). A 0.6 mm dial eats 0.2 mm of the 0.60 mm hour-hand gap.

### Cited Findings
- Hand holes, from the "Hands" page:
  - Hour: Ø1.50 +0.005/−0.003; boss Ø1.76 (max 1.79); blade 0.18 (max 0.21); boss height 0.60 (max 0.70).
  - Minute: Ø0.88 +0.005/−0.003; boss Ø1.05 (max 1.08); blade 0.18 (max 0.21); boss height 0.30 (max 0.33).
  - Seconds: Ø0.198 +0.004/−0.005; tube Ø0.35 (max 0.37); blade 0.10 ±0.02; tube 0.45; overall 0.60 (max 0.64, min 0.50).
  - — [TMI NH35_SS, "Hands"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Hand fitting: hour-wheel pipe Ø1.506 +0.006/0. Cannon pinion Ø0.891 ±0.005. Fourth pinion Ø0.215 ±0.005 with a 90° point and 4°36′ taper. — [TMI NH35_SS, "Hand Fitting"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Shaft heights and part numbers:
  - H1 (hour-wheel pipe height): 0.88 (M) / 1.28 (L), plus a 0.30 lead.
  - H2 (cannon pinion fitting length): 0.61, plus 0.09.
  - H3 (fourth pinion fitting length): 0.42, plus 0.13.
  - Hour wheel 0273 182 (M) / 0273 184 (L). Cannon pinion 0225 425 / 0225 426. Fourth wheel 0144 184 / 0144 185.
  - — [TMI NH35_SS, "Hand Fitting"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- Height stack, Type M / Type L, in mm:

  | Dimension | Type M | Type L |
  |---|---|---|
  | A, hour-hand top above dial | 0.78 | 1.18 |
  | B, minute-hand top | 1.37 | 1.77 |
  | C, seconds-hand top | 1.91 | 2.31 |
  | D, dial thickness | 0.40 | 0.40 |
  | E, seconds hand to glass | 0.45 | 0.45 |
  | F, minute-to-seconds gap | 0.44 | 0.44 |
  | G, hour-to-minute gap | 0.41 | 0.41 |
  | H, dial-to-hour-hand gap | 0.60 | 1.00 |
  | t1, hour-hand thickness | 0.18 | 0.18 |
  | t2, minute-hand thickness | 0.18 | 0.18 |
  | t3, seconds-hand thickness | 0.10 | 0.10 |

  — [TMI NH35_SS, "Hand Fitting"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)
- The assembly plan repeats A–E. Dial top to glass is F = 2.36 (M) / 2.76 (L). The NH70A assembly table uses identical A–F values. — [TMI NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf); [TMI NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- Hand unbalance limits: hour ≤1.50 µN·m and minute ≤1.25 µN·m. Seconds is ≤0.60 µN·m in the 2022 sheets and the hand-fitting page, but ≤0.20 µN·m on the 2011 and 2013 specification pages. — [TMI NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf); contradicted by [SII 2011](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- Retailer figures agree: H 1.5 mm, M 0.88 mm, S 0.2 mm (Lucius NH38 listing). — [Lucius Atelier NH38](https://luciusatelier.com/products/seiko-sii-nh38-open-heart-automatic-movement) (search snippet)

### Inferences
- **How the hour hand seats (calc., Type M):**
  - Pipe top = 0.88 + 0.30 = 1.18 mm above the movement surface.
  - Hour-hand top = 0.40 (dial) + 0.78 = 1.18 mm, flush with the pipe top.
  - The 0.60 mm boss therefore grips the pipe from 0.58 to 1.18 mm.
- **With a thicker dial, there are two options:**
  - (a) Seat the hand at the standard height. The dial-to-hour-hand gap drops from 0.60 to 0.40 mm (0.5 mm dial) or 0.20 mm (0.6 mm dial). The boss (Ø1.76) passes into the Ø2.05 dial hole, so it does not hit the dial.
  - (b) Raise the hand to keep the gap. Boss engagement on the pipe shortens by the same amount: 0.60 → 0.40 mm for a 0.6 mm dial. Grip is weaker and the hand may be loose.
  - Either way, about 0.6 mm is the realistic limit for Type M, which matches Lucius's "practical limit".
  - Applied indices, lume plots or raised logos must stay under about 0.60 mm minus a safety margin (e.g. ≤0.3–0.4 mm) within the hour-hand sweep radius.
- **Type L** gives 1.00 mm under the hour hand. It is the better choice for thick enamel or sandwich dials or tall applied indices, at the cost of 0.40 mm more case height.
- **Hand clearance at the crystal:** the 0.45 mm E clearance is to a flat crystal underside. A domed or box crystal needs the seconds-hand tip path checked along the whole radius.

### Gaps
- The "Hands" page does not give a minimum dial-to-hand clearance distinct from H. Seiko's H = 0.60 is the design nominal, not a stated minimum.
- Hand-length limits come only from the unbalance limits (µN·m). No maximum hand length is given.

## 5. Case design: crystal, gaskets, case back, crown tube, spring bars, lug width, walls, movement retention

### Takeaway
Seiko defines only the movement interface:
- Ø29.30 ±0.03 mm bore with spacer press-fit.
- Screw case back required.
- 8.48 mm (M) minimum inner stack from crystal underside to case-back inner face.
- Stem axis 1.92 mm below the dial seat.
- 0.40 mm rotor-to-back clearance.

Crystal, gasket, tube, spring-bar and wall numbers come only from aftermarket parts and practice:
- SKX-type 42 mm cases: 31.5 × 2.5 mm crystal, 31.5 × 1.5 × 0.38 mm L-gasket, 22 mm lugs with 2.5 mm "fat" spring bars.
- Standard spring bars: 1.5 or 1.8 mm body with 0.8 mm tips.
- Crown tubes for tap 10: commonly 2.5 mm case-side diameter.

I found no authoritative minimum-wall-thickness standard.

### Cited Findings
**Movement retention (official)**
- NH35-type: "The movement is fixed by dial holding spacer". "Screw type case back is required". "Non-corresponding with Diver's watch". The spacer carries small projections ("*Projection to fix movement to case"; 8 marked in the plan view) that are pressed into the Ø29.30 ±0.03 case bore ("3 (dimension to press the projections)"). — [TMI NH35_SS, "Casing" & "Assembly Plan"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf); [SII 2011](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf)
- NH70/72-type: SUS304 casing ring (case bore Ø32.30 ±0.03), plus two SUS631 casing clamps screwed into the movement (M1.0 × 0.175), plus a dial support. Recommended clearances are 0.30 and 0.40 mm. — [TMI NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf)
- Rotor to case back: 0.40 mm at the centre and 0.55 mm at the periphery. Dial top to case-back inner surface: 6.12 mm. — [TMI NH35_SS, "Assembly Plan"](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf)

**Crystal and gasket (aftermarket and forum)**
- SKX007 (42 mm case): the stock Hardlex crystal (Seiko 315P15HN02) is quoted as 31.5 mm × 2.5 mm. — [WatchUSeek SKX007 crystal gasket](https://www.watchuseek.com/threads/seiko-skx007-crystal-gasket.830056/) (search snippet)
- Aftermarket flat sapphire for SKX007/009/SRPD is sold at 31.5 mm. — [Weezmods](https://weezmods.com/en-us/products/skx007-flat-sapphire-crystal-with-bevel-edge) (search snippet)
- SKX crystal L-gasket: 31.5 × 1.5 × 0.38 mm. — [WR Accessories](https://wraccessories.com/products/skx007-crystal-gasket) (search snippet). Weezmods lists "31.5 × 5.5 mm", which conflicts and is unresolved.
- Practitioner rule: case bore = gasket OD, gasket ID = crystal OD. One measured example: case ID 30.5, crystal 29.5, gasket ID 29.5, giving about 0.1 mm compression. — [WatchRepairTalk gasket sizing](https://www.watchrepairtalk.com/topic/8906-questions-regarding-crystal-gasket-sizing-and-compression/) (search snippet; exact thread attribution uncertain)

**Crown and tube (aftermarket)**
- Esslinger screw-down kits: all tap 10 (0.90 mm). Smooth case-side tube diameters are 2.3, 2.5, 2.7, 2.8 and 3.0 mm; threaded tube ends are 4.0, 4.5 and 5.0 mm. Example: crown 83.715, Ø7.0 mm, 4.5 mm thread, 2.5 mm smooth end, 4.0 mm tube length. — [Esslinger kit](https://www.esslinger.com/extra-large-threaded-screw-down-crown-and-tube-kit/) (search snippet)
- Cousins Ø4.00 × 0.35 mm thread crown: taps 9, 10 and 12, with pendant tube Ø4.00 × 2.50 and ID Ø1.80. — [Cousins UK](https://www.cousinsuk.com/product/ss-0400-x-035mm-thread) (search snippet)
- An NH35/4R36 screw-down tube listing: length about 3.7 mm, ID about 2.3 mm. — [eBay listing](https://www.ebay.de/itm/134467754739) (search snippet)
- Builders report that stems cut too short are a common failure with screw-down crowns. — [WatchRepairTalk](https://www.watchrepairtalk.com/topic/27018-stem-length-on-screw-down-crown-seiko-nh35-movement/) (search snippet)

**Spring bars and lugs**
- Crystaltimes CT700 (SKX007/SRPD replacement case) takes 22 mm, 2.5 mm "fat" spring bars. — [Crystaltimes CT700](https://usa.crystaltimes.net/shop/skx007-mod-parts/skx007-cases/ct700/) (search snippet)
- Standard spring bars are 1.5 mm diameter; 1.8 mm is recommended for sports and tool watches. — [Milano Straps](https://milanostraps.com/products/omega-20mm-spring-bars-1-5mm-1-8mm-thickness-premium-swiss-standard) (search snippet)
- 0.8 mm is "a fairly common tip size". Standard quick-release bars typically have 0.8 mm tips. — [Helm SB1](https://futuresite.helmwatches.com/?p=3185); [Milano Straps QR bars](https://milanostraps.com/products/curved-quick-release-spring-bars-swiss-standard) (search snippets)
- Example 40 mm NH35 build: 13 mm thick, 316L, screw-down crown, sapphire, 20 mm lug width, 200 m. — [Stirling Timepieces Campbell](https://stirlingtimepieces.com/pages/campbell-project-specifications) (search snippet)

### Inferences
- **Stack for a 39–40 mm NH35 case, Type M (calc.):**
  - Crystal thickness (e.g. 2.0–2.5 mm sapphire) + 8.48 mm inner stack + case-back plate (about 1.0–1.5 mm, more for a display back).
  - Total about 11.5–12.5 mm before any bezel or crystal dome. This agrees with the 12–13 mm thickness of 40 mm NH35 builds.
  - The crystal, case-back and margin values are design assumptions, not sourced.
- **Crystal OD:** the crystal sits above the dial. A 28.5 mm dial with a chapter ring or rehaut typically needs a crystal opening slightly larger than the visible dial; 30–31.5 mm crystals are the common range. Only the 31.5 mm SKX value is sourced; 30–31 mm is my inference for 39–40 mm cases.
- **Wall at the movement bore (calc.):** (39 − 29.30)/2 = 4.85 mm for a 39 mm case and 5.35 mm for 40 mm, minus the case-back thread and gasket groove. The crown-tube hole (Ø2.5 tube) passes through this wall at the stem-axis height computed in section 1.
- **Lug holes:** for 0.8 mm tips, drill slightly above 0.8 mm. A 1.0 mm hole gives 0.1 mm per side, which feels loose according to Milano's "play" warning. Seiko-style fat bars need larger holes. **Unverified.** Confirm against the spring-bar supplier's recommended hole.
- **Lug width:** 20 mm is the common choice for a 39–40 mm case (one example sourced); 22 mm suits 42 mm SKX-style cases.

### Gaps
- No authoritative case-design standard was found for minimum wall thickness, case-back thread pitch, gasket groove geometry, or case-back deflection allowance.
  - One patent example (attribution among US 4,075,828 / 4,002,020 / 4,594,008 uncertain) calls for about 0.60 mm space behind a 0.6 mm thick back at 4 atm. This is not verified.
  - ISO 22810 (water resistance) and ISO 6425 (divers' watches) were not checked.
- No official Seiko crown-tube specification exists. Tube OD, crown post length and stem cut length must be set by the chosen crown/tube supplier.
- Spacer colour (grey vs black) and any dimensional difference between them are unverified.

## 6. Official datasheets, CAD models, and open-source case designs

### Takeaway
The official SII/TMI spec sheets with full engineering drawings are publicly downloadable for NH34, NH35, NH36, NH37, NH38, NH39, NH70, NH71 and NH72 from timemodule.com. These are the authoritative CAD reference. Free 3D models are scarce and unverified: one rough GrabCAD NH35 model, one Instructables/theprintablewatch.com 3D-printable NH35 case, a Cults3D case body and a MakerWorld movement holder. I found no GitHub CAD repository.

### Cited Findings
- Official TMI spec sheet URL pattern: `https://timemodule.com/upload/category/{23..31}/spec_sheet/NH3x_SS.pdf`. The NH35 sheet (11 pages, revised 16-11-2022) contains: Specification, Appearance 1/2, Casing, Hand Fitting, Hand Setting Stem, Dial-1/Dial-2, Assembly Plan, Hands. — [NH35_SS](https://timemodule.com/upload/category/24/spec_sheet/NH35_SS.pdf), [NH38_SS](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf), [NH70_SS](https://timemodule.com/upload/category/29/spec_sheet/NH70_SS.pdf), [NH72_SS](https://timemodule.com/upload/category/31/spec_sheet/NH72_SS.pdf)
- Older SII versions: [SII NH35A 2011](https://gleave.london/content/TECH/Hattori%20NH35%20-%20Specification.pdf); [SII NH35A rev. 2013 + NH3 TG](https://okta.ua/files/pdf/1482851267NH35A.PDF)
- Technical Guides and parts catalogues: [NH3 TG](https://watch-help.ru/upload/iblock/f76/1wrteqbztomm6zep30qs6rl1babauix4/NH35_TG.pdf); [TMI NH37 TG](https://www.timemodule.com/uploads/attachments/download/Technical%20Guide/NH37_TG.pdf); [Cousins NH3 part sheet](https://cousinsuk.com/pdf/categories/6810_seiko%20nh3%20series%20part%20sheet.pdf)
- GrabCAD "Seiko NH35 Watch Movement": described as a rough model for prototyping cases and renderings. Format and licence were not confirmed. — [GrabCAD (Ruhaan Jain)](https://grabcad.com/ruhaan.jain-1/models) (search snippet)
- "The Printable Watch" (Instructables): an NH35-based design with 5 printed parts (case, case back, movement bracket, chapter ring/glass bracket, crown) plus a glass-pressing tool, downloadable as a zip from theprintablewatch.com. — [Instructables 3D Printed Watch](https://www.instructables.com/3D-Printed-Watch) (search snippet)
- Cults3D: an octagonal (Genta-inspired) middle case for NH35/Miyota 9015, body only. — [Cults3D](https://cults3d.com/:4118112) (search snippet)
- MakerWorld: a printable NH35/NH34 movement holder. — [MakerWorld 668644](https://makerworld.com/models/668644) (search snippet)
- A GitHub repository search for "NH35" and "NH35 watch case" returned no CAD repositories. The only related result is a text guide. — [GitHub seiko-mod-guide](https://github.com/xiaobaitolaobai2-cyber/seiko-mod-guide)

### Inferences
- The fastest accurate CAD route is to build the dial and movement envelope directly from the TMI drawings, using the numbers in sections 1–4. The available third-party 3D models are explicitly "rough" or unverified and should not be used for tolerancing.
- For a 3D-printed fit check, prints are typically accurate to only about ±0.1 mm, while the spacer press-fit is 0.03 mm per side. Final case bores need machining, or should be printed slightly undersize and reamed. This is my inference, not sourced.

### Gaps
- I did not search Printables directly and could not confirm any Printables NH35 listing.
- No STEP file of the NH35 from SII/TMI or from a reputable supplier was found.
- Licence terms for the GrabCAD, Cults3D and Instructables models were not checked.
- The "Appearance-1/2" pages (outline views, which may show the balance and calendar layout) were not extracted in detail.
