# Making one custom 28.5 mm watch dial inside Turkey (October 2026): domestic production routes, prices, minimums, file formats, lead times

Scope: one disc, Ø28.5 mm, 0.4–0.5 mm thick, Ø2.1 mm centre hole, fine gold-on-black geometric pattern (smallest features ~0.12–0.2 mm). Turkey-domestic purchase only, because a personal JLCPCB/PCBWay parcel now costs ~5,600 TL+ in broker/stamp fees. The dial budget is about 1,000 TL.
All web pages were accessed on 2026-10-07 unless noted. Prices are as listed on that date. Anything marked **(ESTIMATE)** is my own reasoning, not a quote.

---

## 1. Turkish PCB manufacturers / prototype services: 0.4/0.6 mm, ENIG, black mask, price, MOQ, lead time, individual Gerber orders

### Takeaway
I found **no Turkish factory that makes a 0.4/0.6 mm, ENIG, black-mask prototype in Turkey.** The İzmir firm that did domestic prototypes stopped in March 2026. The Ankara shops left are basic: green mask, silver plating, no ENIG. The workable route is **Robotistan PCB Servisi**, a Turkish retailer. It takes a Gerber upload, offers 0.4/0.6 mm, ENIG and black mask, and quotes **"Gümrük, KDV ve Kargo Dahil"** (customs, VAT and shipping included). That sidesteps the ~5,600 TL personal import cost. The boards are almost certainly made in China. The listed base price is roughly **730–860 TL incl. VAT for 5 pieces**. The ENIG surcharge is unknown. Lead time is about 4 weeks standard or about 2 weeks by DHL express.

### Cited Findings

**Robotistan PCB Servisi (İstanbul retailer, online Gerber calculator)**
- The calculator page offers thicknesses of 0.4, 0.6, 0.8, 1.0, 1.2, 1.6 and 2.0 mm. Surface finish includes ENIG with gold thickness options of 1 µ" or 2 µ". Mask colours are green, red, yellow, blue, white, black and purple, and silkscreen is white or black. The minimum is 5 pieces (range 5–5,000). — [Robotistan PCB Servisi calculator](https://www.robotistan.com/pcb-servisi)
- The same page states "Gümrük, KDV ve Kargo Dahildir" (customs, VAT and shipping included) and free shipping on orders of 1,500 TL or more. The on-screen amount is a preliminary price ("ön fiyat"). The final price is confirmed after a Gerber manufacturability check, and "special production requirements" can raise it. — [Robotistan PCB Servisi calculator](https://www.robotistan.com/pcb-servisi)
- Lead time on the calculator page is about 4 weeks standard and about 2 weeks express (DHL). The comparison table gives 2–4 weeks for PCB only and 5–7 weeks with assembly. — [Robotistan PCB Servisi calculator](https://www.robotistan.com/pcb-servisi)
- The page has a notice that a Chinese public holiday (25 Sep – 7 Oct) may push processing to 8 October. This implies production in China, although the page never names the production country. — [Robotistan PCB Servisi calculator](https://www.robotistan.com/pcb-servisi)
- File rules: Gerber as .zip or .rar, at most 4 MB, with no Turkish characters in file names. — [Robotistan PCB Servisi calculator](https://www.robotistan.com/pcb-servisi)
- Prices:
  - The product listing "Robotistan PCB Servisi" (code P7) shows 717.57 TL + KDV = **861.09 TL incl. VAT**, or 703.22 TL + KDV by bank transfer. It is marked "Tükendi" (sold out) on 2026-10-07. It also states a ±0.1 mm thickness tolerance below 1 mm, ±0.2 mm standard edge tolerance and ±0.1 mm "precision cutting", the IPC-A-600 standard, a 7-day window to report defects, and white silkscreen on non-white boards. — [Robotistan PCB hizmeti product page](https://www.robotistan.com/pcb-hizmeti)
  - A search snippet of the same listing showed an earlier price of 611.40 TL + KDV = 733.68 TL. The "Üretim Servisleri" page lists 712.91 TL. Neither says what board configuration the price covers. — [Robotistan PCB hizmeti](https://www.robotistan.com/pcb-hizmeti); [Robotistan Üretim Servisleri](https://www.robotistan.com/uretim-servis)
- User reports:
  - One Technopat user received a Robotistan PCB order in about 1.5 weeks and says they chose Robotistan over PCBWay "lojistik gümrük sıkıntı çıkartmasın diye" (to avoid logistics and customs trouble). — [Technopat: Robotistan PCB ne zaman ulaşır?](https://www.technopat.net/sosyal/konu/robotistan-pcb-ne-zaman-ulasir.4150859/)
  - Older forum users priced 5 pieces of 100×100 mm at about $19.58 excl. VAT, and saw a price jump once one board edge exceeds 100 mm. — [mekatronik.org: Robotistan yeni PCB hizmeti](https://mekatronik.org/forum/threads/robotistan-yeni-pcb-hizmeti.8118/)
  - An Ekşi Sözlük user complained of about $23 for 5 two-layer 10×10 cm boards. — [Ekşi Sözlük: robotistan](https://eksisozluk.com/robotistan--2488784)
  - In a 2025 R10 thread, users describe customs problems on direct imports and recommend Robotistan's PCB service. — [R10.net: PCB yaptıracak firma](https://www.r10.net/sorum-var/4442565-pcb-yaptiracak-firma.html)

**İzmir Numune PCB / ERKAR (İzmir, Konak; imports via JETON Teknoloji Ltd. Şti.)**
- The firm's "About" page says: "2026 mart ayından itibaren yerli baskı devre kartı üretimlerimiz yüksek maliyetlerden dolayı süresiz olarak durdurulmuştur" (domestic PCB production stopped indefinitely from March 2026 because of high costs). It also says "Numune pcb üretimleri 2026 yılı mart ayında süresiz durdurulmuştur." The firm now runs an import service from China on a roughly 3-week cycle. — [İzmir Numune PCB – Hakkımızda](https://www.izmirnumunepcb.com/hakkimizda)
- Its technical table, dated 26 Dec 2016, shows the old domestic line was very limited:
  - Domestic boards: 1.0 or 1.6 mm only, minimum trace/space 0.35 mm, minimum drill 0.3 mm, 8/15-day lead time. The domestic row is now marked "Üretim Durduruldu" (production stopped).
  - Imported boards (China): 0.6–2.4 mm, minimum trace/space 0.15 mm, black mask, ENIG, a minimum order of "Min. 120$ KDV Dahil", and 8/28 days.
  - [İzmir Numune PCB – teknik üretim kabiliyeti](https://www.izmirnumunepcb.com/pcb-teknik-uretim-kabiliyeti-becerileri.html)
- The homepage still advertises "2026 numune PCB fiyatları 125 USD KDV dahil sabit fiyatla başlıyor" (a fixed 125 USD starting price), but the underlying article is dated 2019. An older price table lists $120 for 700 pieces of a 30×30 mm 1–2 layer FR4 board and is dated 15.10.2021. The calculator wants Gerber files in RS-274X format only. — [İzmir Numune PCB homepage](https://www.izmirnumunepcb.com/); [PCB baskı devre fiyatları](https://www.izmirnumunepcb.com/pcb-baski-devre-fiyatlari-ve-yapimi.html); [Hızlı PCB fiyat hesapla](https://www.izmirnumunepcb.com/hizli-pcb-fiyat-hesapla.html)

**Pratik PCB (Manisa; Meşe Bilişim)**
- The site says: "5-10 Adet prototip için Çin'de, daha yüksek adetli olanlar Türkiye'de de yapılmaktadır" (5–10 piece prototypes are made in China, larger runs also in Turkey).
- Express options of 1 day, 3 days or 1 week are made in Turkey (Manisa and İstanbul). Boards made in China are flown in and customs-cleared by the firm.
- The site has an online "PCB Fiyat Hesapla" calculator and order panel. ENIG, black mask and 0.4/0.6 mm options are not mentioned on the homepage.
- [Pratik PCB](https://pratikpcb.com/)

**Şimşek Elektronik (Ankara, Ulus – Konya Sokak, Kardeşler İşhanı)**
- Single- and double-sided boards. Urgent samples take 1–4 business days, and single-sided unmasked boards are delivered within 24 hours.
- Mask is green or a custom colour on request; black is not listed. The finish is silver plating, with no ENIG.
- No thickness, trace/space or price information. The site was last updated around 2023.
- Phone +90 532 737 34 30.
- [Şimşek Elektronik](https://www.simsekteknoloji.com/)

**Ankara Baskı Devre (ankarapcb.net, Ulus)**
- A search snippet says single- and double-sided prototypes are delivered "in a few days" and that solder mask is applied even on small quantities. — [ankarapcb.net (search result)](http://www.ankarapcb.net/)
- The domain did **not resolve** (DNS error) on 2026-10-07, so the business may be closed or offline.

**Other names that appear in searches (all imports, or production location unclear)**
- **Utronix (İstanbul):** describes itself as İstanbul's fastest PCB manufacturer *and importer*, with "haftalık iki kargo yüklemesi" (two cargo shipments a week) and 10–12 day delivery. — [Utronix](https://www.u-tronix.com/)
- **Özdisan (distributor):** a PCB sourcing page lists black mask and HASL, lead-free HASL, ENIG and OSP finishes. — [Özdisan PCB tedariği](https://www.ozdisan.com/pcb-tedarigi/teklif)
- **WellPCB Türkiye:** an online calculator with a Gerber upload and express production at +50% surcharge (24–48 h). It appears to be the Turkish front-end of a foreign maker, and I did not verify that it handles customs. — [WellPCB Turkey calculator](https://wellpcbturkey.com/calculator)
- **Armut:** lists 39 "PCB üretim" providers for Menemen (İzmir), with free quote requests. — [Armut Menemen PCB üretim](https://armut.com/menemen-pcb-uretim)
- **Technopat opinion:** one user asserts "Türkiye'de PCB üreten bir firma yok hepsi Çin'deki firmalara ürettirip getirtiyor" (no firm in Turkey makes PCBs; they all have them made in China). This is opinion, but it agrees with what I found. — [Technopat: Robotistan PCB ne zaman ulaşır?](https://www.technopat.net/sosyal/konu/robotistan-pcb-ne-zaman-ulasir.4150859/)

### Inferences
- **"Domestic production" of a fine ENIG/black PCB dial is effectively not available in Turkey in Oct 2026.** The practical route is a Turkish company that imports in bulk and sells all-in (Robotistan, possibly Pratik PCB or Utronix). For the buyer it is a domestic purchase with no personal customs paperwork.
- **Price (ESTIMATE):**
  - 5 boards of about 30×30 mm, 2-layer, 0.6 mm, ENIG, black mask from Robotistan: roughly **800–1,300 TL incl. VAT and shipping**.
  - Reasoning: the base listing is 733–861 TL; ENIG and possibly a non-standard thickness usually add a surcharge, and orders under 1,500 TL may pay shipping.
  - This is borderline for a 1,000 TL dial budget. Get the real number from the calculator.
- **Fit with the dial spec (based on Robotistan's published tolerances):**
  - Thickness tolerance is ±0.1 mm below 1 mm, so a "0.4 mm" board may arrive between 0.3 and 0.5 mm.
  - Edge tolerance is ±0.2 mm standard, so a 28.5 mm round outline may arrive between 28.3 and 28.7 mm. Order "precision cutting" (±0.1 mm) or plan to sand the edge.
  - Specify the Ø2.1 mm centre hole as **non-plated (NPTH)**.
- **Pattern detail:** the gold pattern would be exposed copper with ENIG inside solder-mask openings. Robotistan does not publish minimum trace/space or minimum mask web. Features of 0.12 mm are near typical limits for low-cost 2-layer boards (general industry knowledge, not sourced). Expect a DFM check to flag them. Thickening the finest lines toward 0.15–0.2 mm is safer.
- ENIG gold looks pale and flat compared with a polished brass or gilt dial. Note it as an aesthetic caveat.
- **Timing:** an order placed on about 8 Oct 2026, after the Chinese holiday, should arrive in early November with standard shipping or late October with express (estimate based on the stated 2–4 weeks).

### Gaps
- I could not get a real calculator quote for 30×30 mm, 0.6 mm, ENIG and black. The JavaScript calculator showed "..." placeholders to the fetch tool, and it is unclear what board the 861 TL "P7" product price covers. The product was also shown as sold out.
- Robotistan's minimum trace/space, minimum drill and minimum mask web are not published.
- None of the pages explicitly confirms that private individuals (bireysel) can order. Robotistan's form asks for a name and surname, and its users on forums are clearly individuals.
- I found no PCB maker located in Konya. No Turkish shop confirms 0.4 mm with ENIG and black mask produced in Turkey.
- Utronix and Pratik PCB prices for this configuration are not published.

---

## 2. Laser engraving route: cutting a 28.5 mm disc, paint ablation on brass or anodised aluminium, minimum job charge, formats, online services

### Takeaway
This is the **cheapest and fastest domestic route**, likely **about 500–1,000 TL all-in (ESTIMATE).**
- **Material:** Halsa (İstanbul, Başakşehir) sells a laser-markable **0.45–0.5 mm aluminium sheet with a black surface over a gold layer** ("Edico … Siyah–Altın"), 30×60 cm, for **310.20 TL**, in stock. Laser ablation of the black top layer reveals gold, which gives a gold-on-black look in exactly the needed thickness.
- **Processing:** a fiber-laser shop marks the pattern and cuts the disc and Ø2.1 hole. Ostim Etiket (Ankara) accepts single prototype pieces with no minimum order and works by cargo nationwide.
- **Typical prices:** Armut lists small laser-marking jobs in 2026 at 500–1,000 TL each, with a 500–3,500 TL overall average.

### Cited Findings

**Material for gold-on-black via laser ablation**
- Halsa lists six "Edico Lazer İle Markalanan Alüminyum 0,5 mm Plakalar" colour pairs at 30×60 cm for **310.20 TRY (6.60 USD)** each.
  - Colour pairs include **"Siyah – Altın"** and "Altın – Siyah", both in stock on 2026-10-07.
  - The descriptions give the thickness as **0.45 mm** (the titles say 0.5 mm). The top anodised coating reveals a different background colour when engraved. The plates can be cut with metal guillotines and stamp (kaşe) cutters. They are made in China.
  - [Halsa – Alüminyum Levhalar](https://halsa.com.tr/product-category/kazima-plakalari/aluminyum-levhalar/)
- Halsa company details: Ziya Gökalp Mah., Süleyman Demirel Bulvarı, Sinpaş İş Modern E Blok No:12, Başakşehir, İstanbul; tel +90 212 659 95 55; email trodat@trodat.com.tr. — [Halsa 0.5 mm laser plates](https://halsa.com.tr/product-category/kazima-plakalari/0-5-mm-lazer-ile-kazinan-plakalar/)
- **Caution:** Halsa's "Flexibrass 0.5 mm Fırçalı Altın–Siyah" (120×60 cm, 2,820 TRY) is **acrylic with a metal look, not metal**. Its engraving depth is 0.08 mm. It is not a metal dial substrate. — [Halsa 0.5 mm laser plates](https://halsa.com.tr/product-category/kazima-plakalari/0-5-mm-lazer-ile-kazinan-plakalar/)
- Other gold/black engraving sheets seen only in search snippets (not opened, thickness or material unverified):
  - Malzemesatis lists Rowmark brushed gold/black at 582.21 TL (30×40 cm). — [Malzemesatis lazer plakaları](https://www.malzemesatis.com/kategori/lazer-plakalari)
  - Ardadanal lists gold-black 0.8 mm sheets. — [Ardadanal lazer kazıma plakaları](https://www.ardadanal.com/lazer-kazima-plakalari/)
  - Lazerci lists ABS (plastic) "satine altın-siyah 0.8 mm". — [Lazerci](https://www.lazerci.com/rezopal-abs-lazer-kazima-plakasi-satine-altin-siyah-fircali-mat-08mm-60x40-cm-1-parca)

**Laser shops (single piece)**
- **Ostim Etiket (Ankara, Macunköy/Ostim)**, laser marking:
  - Accepts "tek parça prototip lazer markalama" (single-piece prototype marking). The FAQ answers **"Hayır"** to "is there a minimum order?" and claims prices "adet başı 1 TL'den başlayan" (from 1 TL per piece; marketing claim).
  - Equipment: four fiber lasers (20/30/50/100 W), one CO2 laser and one UV laser.
  - Materials include brass, anodised aluminium and **painted surfaces ("boyalı yüzeyler")**. Resolution is claimed "0.01 mm'ye kadar".
  - Quotes in 1–3 hours. Typical turnaround is 2–7 business days, and parts can be sent and returned by cargo from anywhere in Turkey.
  - Contact: 0545 168 45 45 (WhatsApp), ostimetiket@gmail.com.
  - Accepted file formats are not listed.
  - [Ostim Etiket – Lazer Markalama Ankara](https://ostimetiket.net/lazer-markalama-ankara)
- Ostim Etiket's brass page lists laser cutting for contours, CNC milling, laser engraving, and enamel fill, paint fill or UV print. Thicknesses are 0.3, 0.5, 0.8, 1.0, 1.5 and 2.0 mm CuZn37 (MS63), with nickel, chrome, gold or lacquer coatings. It gives no price and no minimum. — [Ostim Etiket – Pirinç Metal Etiket](https://ostimetiket.net/pirinc-metal-etiket)
- **Armut "Lazer Markalama Fiyatları 2026"**: the average is **500–3,500 TL**. Recent individual job prices:
  - Pen logo and name, İzmir, 11 Jan 2026: **500 TL**
  - Numbers and emblem on a 10 mm star, İzmir, 30 Jul 2026: **500–1,111 TL**
  - Keychain text, İstanbul, 17 Sep 2026: **1,000 TL**
  - Converting a PDF logo to **DXF for laser marking**, Ümraniye, 12 May 2026: **1,000 TL**
  - Key marking, Şişli, Dec 2025: 300–2,000 TL
  - [Armut – Lazer Markalama Fiyatları](https://armut.com/fiyatlari/lazer-markalama_52497)
- **Armut "Pirinç Lazer Kesim" (Ümraniye):**
  - Price range 500–4,000 TL depending on the job. 60 firms serve the area, and most requests get quotes within 30–240 minutes.
  - Listed providers include "Mert G." (1000 W fiber laser for thin sheet and metal labels), "Marka Lazer Etiket ve Reklam Hizmetleri" (laser marking on metal), "FUBA Lazer Kesim ve Markalama" and "Gülsan Lazer" (CO2 and fiber since 2008).
  - The Armut guarantee covers jobs up to 2,000 TL.
  - [Armut – Ümraniye pirinç lazer kesim](https://armut.com/umraniye-pirinc-lazer-kesim)
- Armut's Ümraniye laser-marking listing gives a 300–2,000 TL range. — [Armut – Ümraniye lazer markalama](https://armut.com/umraniye-lazer-markalama)
- **Beylikdüzü Baskı (İstanbul):**
  - Sells custom laser-marked brass plates and "Siyah Metal Eloksal Alüminyum Etiket" (black anodised aluminium labels).
  - A small 27×37 mm brass item is listed at **29.51 TL** (undated, quantity pricing). Name engraving on a cake knife is 344.25 TL.
  - [Beylikdüzü Baskı – lazer markalama](https://beylikduzubaski.com/urun-kategori/istanbul-celik-uzerine-yazi-yazma-metal-uzerine-kazima-markalama-ve-logo-baskilari-yapilmaktadir/); [Siyah eloksal alüminyum etiket](https://beylikduzubaski.com/urun/siyah-metal-eloksal-aluminyum-etiket-dis-mekan-dayanikli-kalici-lazer-baskili-plaka/)
- **Etiketciniz** (anodised aluminium fiber-engraved labels) applies a **minimum order of 50 pieces**, so online label shops are not suitable for a single piece. — [Etiketciniz – eloksallı fiber kazıma etiket](https://etiketciniz.net/eloksalli-fiber-kazima-etiket)
- Other shops that state they do brass laser engraving, with no prices:
  - Space Reklam (Gebze): does brass, stainless and aluminium, with delivery to the customer's address. — [Space Reklam](https://spacereklam.com/metal-lazer-kazima-etiket/)
  - Biz Lazer Baskı Merkezi: does one-off personalised work. — [Biz Lazer](https://www.bizlazerbaski.com/)
  - Birmak Lazer: makes samples, and warns that cheaper settings lower visual quality. — [Birmak Lazer](https://birmaklazer.com/)
- **Trendyol:** no seller was found offering upload-your-design laser engraving on brass. Results were mostly acrylic licence-plate holders and a 10 mm brass letter charm. — [Trendyol lazer kesim plakalık](https://www.trendyol.com/lazer-kesim-plakalik-y-s113640); [Trendyol yfhobi brass charm](https://www.trendyol.com/yfhobi/1-adet-10-mm-y-harfi-lazer-kazima-pirinc-metal-pul-altin-kaplama-metal-uc-1-kalite-kararmaz-p-782497484)

### Inferences
- **Recommended single-piece workflow (ESTIMATE):**
  1. Buy one Edico "Siyah–Altın" 30×60 cm sheet for 310 TL plus shipping. It is enough for dozens of attempts.
  2. Send it, or a small cut piece, to a fiber-laser shop with a vector file. The shop ablates the pattern, then cuts the Ø28.5 disc and Ø2.1 hole, either by multiple fiber passes or by punch/guillotine as Halsa suggests.
  3. Expected shop charge is about 300–1,000 TL, based on Armut job prices. Expected total is about **600–1,300 TL**, with turnaround of about 1 week by cargo.
- **Detail:** fiber marking lasers have spot sizes of a few tens of microns (general knowledge, not sourced), so 0.12–0.2 mm lines are plausible. Ask for a test mark on an offcut first.
- **Colour caveats:**
  - **Black-anodised aluminium engraves white or silver, not gold.** It only gives "gold-on-black" if the substrate already has a gold layer, as Edico Siyah–Altın does.
  - The cut edge of an anodised aluminium disc shows raw silver aluminium. It is hidden under the chapter ring or case, but it should be noted.
- **Brass alternative:** spray a brass disc black (or have it lacquered) and let the fiber laser ablate the paint to reveal brass, then clear-lacquer it. Ostim Etiket lists both brass and painted surfaces. You still need a brass disc first; see section 4.
- **File formats:** no shop publishes a list. The Armut request shows DXF is the format shops expect, and converting a PDF to DXF was billed at 1,000 TL. Bring a clean **DXF** (and ideally SVG and PDF) at 1:1 scale, with the pattern as closed filled regions and the cut paths on a separate layer.

### Gaps
- No shop publishes a per-piece price for "cut a 28.5 mm disc from 0.45–0.5 mm sheet + mark a pattern". All figures above are platform averages or other jobs.
- I could not confirm the shade of Edico's gold layer (metallic gold or yellow), or whether its coating survives fine fiber marking without halos.
- A search summary mentioned a fason (contract) rate of about 150–200 TL per minute for marking anodised aluminium, but I could not identify or open the source page, so it is excluded.
- Armut, Hepsiburada and Etsy-TR: no upload-your-file laser service with a fixed listed price was found.

---

## 3. Chemical etching / photo-etching route: Turkish metal nameplate makers

### Takeaway
Ankara (Ostim and İvedik OSB) has several brass acid-etching ("asit indirme") nameplate makers that fill the etched areas with paint or enamel. The most detailed spec comes from the Ostim Etiket family of sites:
- CuZn37, 0.3–1.5 mm (0.5 mm included)
- minimum line **0.15 mm**
- etch depth 0.1–0.5 mm
- epoxy or enamel fill
- **MOQ 50 pieces**
- 5–7 business days

No setup or single-piece prices are published. The 0.12 mm smallest features are below their stated 0.15 mm limit. The 50-piece minimum makes this route likely to exceed 1,000 TL for one dial (ESTIMATE).

### Cited Findings
- **Ostim Etiket – Pirinç Asit İndirme:**
  - Thicknesses 0.3, **0.5**, 0.8, 1.0 and 1.5 mm, in CuZn37 (CW508L) or CuZn40.
  - **Minimum line thickness 0.15 mm.** Etch depth 0.1–0.5 mm; 0.1–0.2 mm is recommended for fine detail.
  - Fill is epoxy or enamel, Pantone-matched.
  - **Minimum order 50 pieces.** Lead time about 5–7 business days.
  - Tolerance ±0.05–0.1 mm, and etch-depth tolerance ±0.02 mm.
  - Perforated or cut-out parts can be made by double-sided chemical milling, with laser cutting as an alternative.
  - Finishes are polished, satin, brushed, antique, or nickel/chrome plated.
  - No prices, setup or film cost, or file formats are published. Quotes are given by phone or WhatsApp.
  - [Ostim Etiket – Pirinç Asit İndirme](https://ostimetiket.net/pirinc-asit-indirme-etiket)
- **pirincmetaletiket.com.tr** offers chemical etching and laser engraving on brass and says it produces **"from a single piece up to bulk orders"**. It has the **same address and phone (0545 168 45 45) as Ostim Etiket**, so it is the same business under another domain. Etiketciniz.net also carries the Ostim Etiket branding. — [Pirinç Metal Etiket](https://pirincmetaletiket.com.tr/); [Etiketciniz – Pirinç Metal Asit İndirme](https://etiketciniz.net/pirinc-metal-asit-indirme)
- **Metal Etiket Ankara / Damla Reklam (İvedik OSB):** brass labels with a "profesyonel asit indirme tesisi" (professional acid-etching facility), painting or filling after etching, and cargo shipping across Turkey. No prices. Some pages appear several years old. — [Metal Etiket Ankara – Pirinç](https://www.metaletiketankara.com/pirinc-metal-etiket/); [Asit indirme etiket](https://metaletiketankara.com/asit-indirme-etiket)
- **Other etching shops (no prices or specs):**
  - Ayka Serigrafi does brass labels by acid etching and paints the etched areas on request. — [Ayka Serigrafi – Metal Etiket](https://aykaserigrafi.com/urunler/metal-etiket/)
  - Vera advertises "Asit İndirme Etiket (Sınırsız Renk Seçeneği)" (unlimited colour options). — [Vera](https://vera.com.tr/asit-indirme-etiket/)
  - Semercioğlu Reklam has a "Pirinç Etiket 2026" page. — [Semercioğlu Reklam](https://www.semercioglureklam.com.tr/pirinc-etiket.html)
  - Bora Ajans does metal and aluminium labels. — [Bora Ajans](https://boraajans.com/aluminyum-etiket-metal-etiket-2/)
- **Background:** a Dicle University thesis (2011) chemically machined X5CrNi18-8 stainless with FeCl3 and found a 32 Bé solution best. This is relevant only if someone tries DIY photo-etching. — [Dicle Üniversitesi açık erişim](https://acikerisim.dicle.edu.tr/items/28a9e6e5-be3b-49d3-a04d-4e2c8c38ac5d)

### Inferences
- **The best etched look would be:**
  1. Etch the background about 0.1 mm deep.
  2. Fill it with black epoxy or enamel.
  3. Leave the pattern as raised, polished brass, optionally gold-plated, since Ostim lists gold coating.
  4. Cut the outline by chemical milling (double-sided etch) or laser.

  This is closest to a real dial, but it needs a photo-tool (film) and a 50-piece run.
- **Cost (ESTIMATE):** with a 50-piece minimum plus film or setup, one etched dial is unlikely to cost under 1,000 TL, unless the shop agrees to put the dial on a panel alongside another customer's job. Ask explicitly for "tek adet numune" (single sample) pricing. pirincmetaletiket.com.tr says single pieces are possible, but probably by laser rather than etching.
- **Detail:** 0.12 mm features are below the stated 0.15 mm minimum line. Etching undercut also widens recesses, so the finest lines should be designed at 0.15–0.2 mm for this route. Paint-filling grooves 0.12–0.15 mm wide is also difficult.

### Gaps
- No Turkish etcher publishes a film or setup fee ("film/kalıp ücreti") or a single-piece price. These must be obtained by phone or WhatsApp quote.
- No confirmation that black fill is available. The spec says "Pantone-matched", and black is presumably possible.
- No İstanbul or İzmir photo-etcher with published specs was found. The searches surfaced mostly Ankara shops.

---

## 4. Where to buy thin brass sheet (pirinç levha 0.4/0.5 mm) or ready brass discs in Turkey

### Takeaway
0.5 mm brass is sold domestically **only in large sheets or by the kilo**:
- Ege Teknik Metal via Metaldepom: 250×1000 mm for **1,365.83 TL + KDV**
- Metal Reyonu: about **1,040–1,195 TL/kg**

Hobby strips (Gvn Art 0.5×15 mm, 70 TL) are too narrow for a 28.5 mm disc. I found no ready-made 28.5 mm brass dial blanks or discs for sale in Turkey. The practical choice is to have the laser or etch shop supply the material (Ostim lists CuZn37 0.5 mm in stock) or to buy an offcut. 10×10 cm copper plates (Trendyol/Hepsiburada) are a cheap alternative substrate.

### Cited Findings
- **Ege Teknik Metal (via Metaldepom), 0.5 mm brass sheet:**

  | Size | Price |
  |---|---|
  | 250×1000 mm | **1,365.83 TL + KDV** |
  | 750×1000 mm | 2,972.50 TL + KDV |
  | 1000×1000 mm | 4,005 TL + KDV |

  The Metaldepom product URL returned 404 on fetch on 2026-10-07, so these prices are from search snippets. — [Metaldepom 0.5 mm pirinç levha](https://www.metaldepom.com/urun/0-5-mm-pirinc-levha-sac-plaka-1000x1000-mm); [Hepsiburada – Ege Teknik Metal 0.5 mm 1000×1000](https://www.hepsiburada.com/ege-teknik-metal-0-5-mm-pirinc-levha-sac-plaka-1000x1000-mm-pm-HBC000047Z9GO)
- A Metaldepom snippet also showed a 0.5 mm brass sheet at 559.88 TL + KDV, size not visible. — [Metaldepom pirinç plaka ölçüleri](https://www.metaldepom.com/pirinc-plaka-olculeri,TA-201.html)
- **Metal Reyonu** lists 0.50 mm brass sheet per kg at 1,039.50 TL/kg and 1,195.42 TL/kg; the VAT status is unclear. — [Metal Reyonu – Pirinç Levha](https://metalreyonu.com.tr/urunler/pirinc-levha)
- **Weight:** 0.50 mm brass sheet weighs 4.250 kg/m². — [Bilgimetal – Pirinç Levha](https://bilgimetal.com.tr/pirinc-levha.php)
- **Gvn Art (hobby):**
  - Brass strip 0.5 mm × 15 mm × 100 cm: **70 TL**. It is too narrow for Ø28.5 mm. — [Gvn Art pirinç şerit 0.5×15](https://www.guvensanat.com/metal-cubuk-princ-serit-levha-lama-05x-15mm-1mt-1k-14ad210t-72962)
  - The 20×30 cm brass sheet is only 0.05 mm thick. — [Gvn Art 0.05 mm levha](https://www.guvensanat.com/princ-pirinc-levha-kalinlik-005-mm-x-20x30cm-80917)
- **Copper alternative:** HDG "Kaplamasız Saf Bakır Levha Plaka 10×10 cm" is sold on Trendyol (2-piece pack about 550 TL per search snippet). A Hepsiburada copper listing shows 10×10 cm at 0.50 mm. — [Trendyol HDG bakır levha 10×10 (2 adet)](https://www.trendyol.com/hdg/kaplamasiz-saf-bakir-levha-plaka-10x10-cm-2-adet-p-266677693); [Hepsiburada bakır levha 10×10](https://www.hepsiburada.com/kaplamasiz-saf-bakir-levha-plaka-10x10-cm-1-adet-pm-HBC0000CF8L80)
- **Shop-supplied material:** Ostim Etiket lists CuZn37 at 0.3 and 0.5 mm as standard material options for its etched brass. This implies, but does not confirm, that the shop can supply the brass. — [Ostim Etiket – Pirinç Asit İndirme](https://ostimetiket.net/pirinc-asit-indirme-etiket)

### Inferences
- A 30×30 mm blank of 0.5 mm brass weighs about 3.8 g (4.25 kg/m² × 0.0009 m²). At about 1,100 TL/kg that is roughly **4 TL of metal**. The real cost driver is the minimum sale unit, about 1,600 TL incl. VAT for the smallest 250×1000 mm sheet. That alone exceeds the dial budget.
- Better options, in order (ESTIMATE):
  - (a) Ask the laser or etch shop to supply a 30×30 mm piece of its own stock.
  - (b) Ask a local metal or sign shop (tabelacı, rozet/plaket maker) for an offcut ("kırpıntı").
  - (c) Use the 0.45 mm Edico black-gold aluminium (310 TL) from section 2.
  - (d) Use a 10×10 cm copper plate.
- I found no 0.4 mm brass listing, but 0.4 mm is not essential since 0.45–0.5 mm meets the spec.

### Gaps
- No ready-cut brass discs or "pul" (blanks) near 28–30 mm diameter were found. The only brass "pul" found was a 10 mm letter charm.
- The live price and stock of the Metaldepom 250×1000 mm sheet could not be re-verified because the page returned 404.
- No K&S-type small hobby brass sheet (e.g. 100×250 mm, 0.5 mm) was found on Turkish sites.

---

## 5. Turkish makers or Instagram/Etsy shops that already produce custom watch dials (özel saat kadranı)

### Takeaway
I found **no Turkish workshop or online shop that manufactures custom watch dials to order.** The Turkish Seiko-mod scene, for example SeikoModsTR, sells complete modded watches priced in USD and sources its dials abroad. Watch-parts sellers stock only standard replacement dials. Forum users import dials and have local watchmakers fit them. The custom dial itself therefore has to come from one of the general fabrication routes in sections 1–3.

### Cited Findings
- **SeikoModsTR (smodstr.com)** sells complete NH35 mod watches (Submariner, Royal Oak, Nautilus and similar styles) and Gym Watch chronographs.
  - Prices are in USD, for example $352.93 and $389.47.
  - No standalone dials or dial-printing service is listed.
  - There are "Create Your Watch" and "Services" links whose contents were not visible. Contact +90 530 448 0544.
  - [Seiko Mod Türkiye shop](https://www.smodstr.com/en/shop)
- **saatparcasi.com (İzmir, Kemeraltı)** lists "1. Kalite Seiko 5 Otomatik Saat Kadranı" replacement dials (white with gold or silver stripes, for 7009/7S26). The fetched page showed 0.00 TL placeholders, and a search snippet showed **389.95 TL**. No black or blank 28.5 mm NH35 dials were listed. — [saatparcasi.com – Kadran](https://saatparcasi.com/saatci-el-aletleri-malzemeleri-kadran)
- **Technopat:** a user looking for someone in Turkey to swap an NH35 dial was pointed to an İstanbul watch service. — [Technopat: Türkiye'de Seiko mod yapan yer önerisi](https://www.technopat.net/sosyal/konu/tuerkiyede-seiko-mod-yapan-yer-oenerisi.3819408/)
- **Türkiye Saat Forumu (about 5 years old):** members describe ordering dials from abroad and having a watchmaker in İzmir build an NH35 "Seiko Hulk" mod. — [TSF – Seiko modlama referansı](http://www.forum.saatforumu.com/viewtopic.php?f=12&t=37089)
- **Technopat (Ankara watchmaker thread):** one user claims "Türkiye'de hiçbir bağımsız usta" works to European standards (no independent watchmaker in Turkey does). This is an opinion, but it notes that some watchmakers work by cargo, e.g. "Saat Kulesi Çelik Saat – Tuncer usta". — [Technopat: Ankara'da saat tamircisi önerisi](https://www.technopat.net/sosyal/konu/ankarada-saat-tamircisi-onerisi.4138671/)
- **Ma Atölye** sells a finished 30 mm black-dial chronograph watch for 3,000 TL. It is a complete watch; no dial service is offered. — [Atölye Ma – 30MM chrono siyah kadran](https://atolyema.com/30mm---chrono-siyah-kadran-saat)
- **Çiçeksepeti** "kişiye özel kol saati" listings let buyers choose the dial text, font and colour. These are printed dials on ready-made watches, not dial manufacturing. — [Çiçeksepeti – kişiye özel kol saati](https://www.ciceksepeti.com/d/kisiye-ozel-kol-saati)
- **Kadran Watch (İstanbul)** is a luxury and vintage watch retailer and repairer, not a dial maker. — [Kadran Watch](https://kadranwatch.com/)
- **Import benchmark (not domestic):** Alibaba lists "28.5mm Sterile Dial Fit for seiko NH39 Movement" with optional custom logo. — [Alibaba – Seiko mod](https://www.alibaba.com/showroom/seiko-mod.html)

### Inferences
- Because no Turkish dial maker exists for one-offs, the dial must be made as a **flat "nameplate-type" part**: a laser-marked anodised or painted disc, an ENIG PCB, or an etched brass plate. A local watchmaker can then fit dial feet or use dial dots or adhesive. A 28.5 mm, Ø2.1 mm-hole dial matches the NH35/NH36/NH39 dial format, judging from the Alibaba 28.5 mm NH39 listing.
- **Overall route comparison for one dial, Oct 2026 (ESTIMATES unless sourced):**

  | Route | Look | Expected cost | Lead time | Minimum | Main risk |
  |---|---|---|---|---|---|
  | **Edico Siyah–Altın 0.45 mm Al (Halsa, 310 TL) + fiber-laser shop (e.g. Ostim Etiket, no MOQ)** | Gold pattern on black, metal | ~600–1,300 TL | ~1–2 weeks incl. cargo | none at the laser shop; a whole 30×60 sheet must be bought | gold shade and halo quality; silver cut edge |
  | **Robotistan PCB (0.4/0.6 mm, ENIG, black; customs included)** | Pale ENIG gold on black mask | ~800–1,300 TL for 5 pcs | ~2–4 weeks | 5 pcs | 0.12 mm features vs DFM limits; ±0.2 mm outline; boards made in China (but no personal customs) |
  | **Brass disc + black paint + laser ablation** | Brass pattern on black | ~500–1,500 TL, plus brass sourcing | ~1–2 weeks | none for laser; brass minimum-sale problem | needs a brass blank; paint durability |
  | **Acid-etched brass + black fill (Ankara etchers)** | Most "real dial" look | likely >1,000 TL because of 50 pc MOQ and film | 5–7 business days plus quote | 50 pcs (Ostim) | 0.15 mm min line > 0.12 mm features; no published price |
  | **Domestic PCB fab (Ankara Ulus shops)** | not suitable | — | 1–4 days | — | no ENIG or black; İzmir domestic line stopped March 2026 |

### Gaps
- Instagram and Etsy-TR could not be searched effectively with these tools. Small Instagram dial artists may exist but were not found.
- No Turkish source gives prices for applying dial feet or fitting a custom flat dial to an NH35 movement. A watchmaker quote is needed.
