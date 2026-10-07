# Seiko-mod parts prices for a sub-5000 TL automatic watch: Turkey vs AliExpress import (October 2026)

Research date: 2026-10-07. Reference FX rate: about 49.03 TL per USD (free-market quote, 1 Oct 2026, [hisse.net](https://www.hisse.net/haber/dolar-ve-euro-bugun-ne-kadar-kac-tl-1-ekim-guncel-doviz-kurlari-99449)). All "≈ TL" conversions below use 49 TL/USD and are mine.

Method notes (read before using the numbers):
- **AliExpress:** I pulled the search pages directly on 2026-10-07 (`aliexpress.com/w/wholesale-<query>.html`) with the ship-to region set first to US and then to TR. Prices are the sale price shown on the search card, in USD. Most cards say "Free shipping" and carry `taxRate:"0"`, so **Turkish import taxes are not included**. Prices of $0.33–$1.33 on hand, crown and dial listings are usually new-user "welcome deal" prices, not normal prices. Item URLs follow the pattern `https://www.aliexpress.com/item/<ID>.html`. Store names were not in the search data, and item pages are JavaScript-rendered, so I could not read store names, full specs or reviews. **Dial sizes and specs come from listing titles.**
- **Trendyol, Hepsiburada, n11, Akakçe, Cimri, Technopat, Ekşi Sözlük:** these sites return HTTP 403 (Cloudflare or bot protection) to both direct fetches and WebFetch. Their prices come from search-engine snippets or index snapshots, so the date seen is unknown. I mark these "snapshot, undated" and they need a live check before purchase.
- **Amazon.com.tr search pages:** fetched directly on 2026-10-07. Prices shown are in TL and include KDV (Turkish VAT, normal for Turkish retail). Product pages were later blocked.

---

## Q0 (cross-cutting): Can a buyer in Turkey import parts cheaply in October 2026? (customs regime and AliExpress reachability)

### Takeaway
Since February 2026, Turkey no longer has a duty-free or simplified route for personal online orders. Every AliExpress parcel, even a €1 one, goes through standard import procedures and is taxed. The 2024–2025 comparisons ("AliExpress is cheaper") are therefore obsolete. On top of that, when the AliExpress ship-to region is set to Turkey, the catalogue visibly shrinks and changes. Many mainstream NH35 movement, case and hand listings did not appear, although NH70/NH72 skeleton movements did.

### Cited Findings
- Presidential Decision No. 10813 (dated 6 Jan 2026, Official Gazette 7 Jan 2026) removed the "€30 and below" phrase from Article 126 of Customs Law 4458. Even the smallest foreign e-commerce orders are now subject to customs procedures and taxes. It takes effect 30 days after publication, about 6 Feb 2026 — [Webrazzi, 2026-01-07](https://webrazzi.com/2026/01/07/yurt-disi-alisverislerde-gumruk-muafiyeti-kaldirildi-30-euro-limiti-tarihe-karisti/)
- The Trade Ministry gives the effective date as 1 Feb 2026. It says purchases "will have to be imported through standard customs procedures" and that this "does not amount to an import ban". The old simplified flat rates were 30% for EU-origin goods and 60% for non-EU goods (China), plus 20% for ÖTV-listed goods. Toys, footwear and leather goods had already been excluded from the simplified route by an October 20, 2025 circular — [Turkish Minute, 2026-01-07](https://turkishminute.com/2026/01/07/turkey-ends-low-value-customs-system-raising-costs-for-overseas-online-orders/)
- History: the limit fell from €150 to €30 in Aug 2024, and shipping was counted inside the €30 from 27 Dec 2024, which made it effectively about €27 — [Hürriyet](https://www.hurriyet.com.tr/bilgi/galeri/yurt-disi-gumruk-vergisi-siniri-2026-ne-kadar-oldu-dustu-mu-30-euro-siniri-kalkti-mi-43078592); [Webrazzi](https://webrazzi.com/2026/01/07/yurt-disi-alisverislerde-gumruk-muafiyeti-kaldirildi-30-euro-limiti-tarihe-karisti/)
- A blog dated 27–29 Jan 2026 says AliExpress is still accessible but "not as before". It describes AliExpress as moving toward local stock and warehouses and says it "usually collects the tax at checkout", with possible extra customs costs. This is an unofficial source and the article itself is internally inconsistent — [Cospier](https://cospier.com/aliexpress-kapandi-mi.html)
- Anecdotal costs: one Şikayetvar user reported about 6,300 TL in customs charges on a product worth about 1,200 TL. Another complaint, from April 2026, describes an AliExpress order stuck at customs with a broker asking about $432. Both are single complaints seen only as search snippets; the page returned 403 — [Şikayetvar (AliExpress vergi)](https://www.sikayetvar.com/aliexpress/vergi-ucreti/gumruk-vergisi); [Şikayetvar EN complaint](https://www.sikayetvar.com/en/aliexpress-us/aliexpress-order-stuck-in-turkish-customs-despite-prepaid-taxes)
- Before the change, Turkish modders were already blocked by the €30 limit: "cheapest NH35 on AliExpress was €33–35, above the tax limit, so I couldn't order". The same thread says no Turkish firm imports NH35s online and that local watchmakers mostly stock quartz. The thread is about 1.5 years old — [Technopat thread (via search snippet; page 403)](https://www.technopat.net/sosyal/konu/seiko-nh35-mekanizmasi-nereden-alinir.3727547/)
- **My own observation (2026-10-07):** with the AliExpress ship-to region set to TR, the searches "nh35 movement", "nh35a movement" and "japan original nh35 movement" did not return the mainstream movement listings that appear for the US region. For example, the 3,628-sold "Japan Original NH35 NH35A" (ID 1005007379221598) and the 2,649-sold China NH35 (1005011797439544) were both missing. Instead the results were mostly complete watches, dials and tools with no sales counts. "nh35 case" and "nh35 hands" in the TR region returned 0 "Choice" items out of 60. "nh72 movement" in the TR region did return the usual NH70/NH72 listings (17 Choice items) — [AliExpress search nh35-movement](https://www.aliexpress.com/w/wholesale-nh35-movement.html); [AliExpress search nh72-movement](https://www.aliexpress.com/w/wholesale-nh72-movement.html)
- Hepsiburada's "Yurt Dışından" (cross-border) program: per a Hepsiburada static page seen in search, the seller delivers to Hepsiburada's overseas warehouse and the customs steps are handled on the buyer's behalf. I could not confirm how 2026 taxes are shown at checkout — [Hepsiburada Yurt Dışından page](https://www.hepsiburada.com/staticpage/786700737428161)

### Inferences
- For a 5000 TL budget, direct AliExpress import is now risky and hard to price. A clean "product + 60%" estimate is only plausible if AliExpress collects the tax at checkout. If a parcel lands in formal clearance with broker fees, the fees can exceed the parts' value.
- Turkish marketplace listings marked "Yurt Dışından" (Hepsiburada) are effectively AliExpress-type goods re-sold with the customs work handled. They are probably the most practical "import" channel for a Turkish buyer in 2026.
- Each AliExpress listing must be checked on the item page with a Turkish address before relying on it. The TR-region catalogue differed from the US one.

### Gaps
- I could not find the exact 2026 standard-procedure duty and VAT rate for watch movements and watch parts (GTİP 9108/9111/9114) for individual buyers, or typical broker fees for a small AliExpress parcel. I also could not confirm whether AliExpress Turkey collects duty at checkout as of October 2026.
- I could not confirm whether listings missing from the TR-region search are truly not shippable to Turkey, or whether the search simply ranks them differently.

---

## Q1: Movement prices (NH35A, NH36A, NH38A, NH39A, NH34A GMT, NH70/NH72 skeleton): Turkey vs AliExpress, and genuine vs clone risk

### Takeaway
On AliExpress (US view, 7 Oct 2026), listings claiming to be Japanese/TMI NH35A cluster at **$69–$108**. Clearly labelled "China NH35" clones sit at **$21–$40**. In Turkey, the only standalone NH35 prices found are cross-border Hepsiburada listings at **≈1,590–2,645 TL**, of unclear origin. NH70/72 skeletons on AliExpress run **$62–$97**, the NH34 GMT **$165–$209**, and the NH38A/NH39A **$68–$95**. Western mod shops quote much higher prices ($107–$218) and report NH prices rising through 2025–2026.

### Cited Findings

**A. AliExpress movement listings (USD, 2026-10-07, US ship-to view, free shipping shown, Turkish taxes NOT included)**

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes |
|---|---|---|---|---|---|---|---|
| NH35A "Japan Original", crown at 3/6, white date | AliExpress (Choice) | 95.64 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007379221598.html | 2026-10-07 | 3,628 sold, 4.8★. Not visible in TR-region search |
| NH35A "Japan Genuine" date at 3 | AliExpress (Choice) | 88.56 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005006845396357.html | 2026-10-07 | 917 sold, 4.9★ |
| "Original Japan TMI NH35A", hacking/hand-wind | AliExpress | 108.16 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011843810500.html | 2026-10-07 | 5★, says TMI |
| NH35 "Premium" NH35A, date at 3/3.8/6 | AliExpress | 69.57–72.49 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009295862392.html | 2026-10-07 | 1,922 sold, 5★. "Premium" and no "Japan" claim, so origin unclear |
| "High Accuracy Japan NH35A" multi-variant (NH34/36/38/05/70/71/72) | AliExpress | 68.80 (base) | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005001430226835.html | 2026-10-07 | 594 sold, 4.8★. Long-running listing; price is for the cheapest variant |
| NH35A "Japan Genuine" | AliExpress (Choice) | 129.94–132.86 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005013205588080.html | 2026-10-07 | 101 sold |
| NH35A "Japanese Precision" | AliExpress | 85.10 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012977517878.html | 2026-10-07 | 204 sold |
| **Clone:** "Japan Genuine NH35 … China NH35A" | AliExpress | 22.91–24.99 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011797439544.html | 2026-10-07 | 2,649 sold, 4.6★. Title says both "Japan Genuine" and "China", treat as clone |
| **Clone:** China NH35, black calendar | AliExpress (Choice) | 37.30 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010373780504.html | 2026-10-07 | 521 sold, 4.1★ |
| **Clone:** China NH35, 3 o'clock | AliExpress (Choice) | 36.70–40.28 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010622712844.html | 2026-10-07 | 995 sold, 4.0★ |
| **Clone:** China NH35 "can replace Japanese" | AliExpress | 30.03 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012194182668.html | 2026-10-07 | 537 sold, 4.2★ |
| **Clone:** China NH35 | AliExpress | 21.54–25.78 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010617011393.html | 2026-10-07 | 358 sold, 4.1★ |
| NH36A "Japan Original" day-date | AliExpress | 88.72 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005005699120054.html | 2026-10-07 | 4.8★ |
| NH36A "Original", crown 3.8 | AliExpress | 94.34 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007995354808.html | 2026-10-07 | 4.9★ |
| NH36A "Japan Genuine" multilingual day wheel | AliExpress | 105.33 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011644977862.html | 2026-10-07 | 4.9★ |
| **Clone:** China NH36 | AliExpress (Choice) | 31.94 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005013088357890.html | 2026-10-07 | — |
| NH38A "Japan Genuine" (no date) | AliExpress | 72.88 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008240895208.html | 2026-10-07 | 4.9★ |
| NH38A "Japan Genuine" | AliExpress (Choice) | 83.09–94.57 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010362363754.html ; https://www.aliexpress.com/item/1005010806500239.html | 2026-10-07 | 4.8–4.9★ |
| NH39A "Japan" | AliExpress | 67.98 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010628642991.html | 2026-10-07 | 4.6★. NH39A exists and is listed |
| NH39A "Original Japanese" | AliExpress | 77.69–80.46 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007264345595.html ; https://www.aliexpress.com/item/1005008653314296.html | 2026-10-07 | 5★ |
| NH34A GMT "TMI NH34" | AliExpress | 180.37 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009689287569.html | 2026-10-07 | 4.9★ |
| NH34A GMT "Japan Genuine" | AliExpress | 164.80 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012391311735.html ; https://www.aliexpress.com/item/1005008240723895.html | 2026-10-07 | 4.7–5★ |
| NH34A GMT (BLIGER) | AliExpress | 209.00 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010757235125.html | 2026-10-07 | — |
| NH70/NH71/NH72 skeleton "Japan Original" | AliExpress (Choice) | 73.63 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012138031397.html | 2026-10-07 | 4.8★. Also appeared in TR-region search |
| NH70/71/72 skeleton "Original" | AliExpress (Choice) | 82.98 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009946329043.html | 2026-10-07 | 4.8★ |
| NH70/71/72 skeleton | AliExpress | 62.26–73.50 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012698397310.html ; https://www.aliexpress.com/item/1005011986062168.html ; https://www.aliexpress.com/item/1005009506680810.html | 2026-10-07 | 4.8–5★ |
| NH72A skeleton (gunmetal) | AliExpress | 77.75 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005005267087300.html | 2026-10-07 | 5★ |
| NH72A "Japan Original" | AliExpress | 96.95 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007995401682.html | 2026-10-07 | 4.8★ |

Source search pages: [nh35-movement](https://www.aliexpress.com/w/wholesale-nh35-movement.html), [japan-original-nh35-movement](https://www.aliexpress.com/w/wholesale-japan-original-nh35-movement.html), [nh36a-movement](https://www.aliexpress.com/w/wholesale-nh36a-movement.html), [nh38a-movement](https://www.aliexpress.com/w/wholesale-nh38a-movement.html), [nh39a-movement](https://www.aliexpress.com/w/wholesale-nh39a-movement.html), [nh34a-gmt-movement](https://www.aliexpress.com/w/wholesale-nh34a-gmt-movement.html), [nh72-movement](https://www.aliexpress.com/w/wholesale-nh72-movement.html)

**B. Turkish sellers (standalone movements)**

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes |
|---|---|---|---|---|---|---|---|
| Gui Xulian NH35/NH35A, 3-hand + date | Hepsiburada (seller "Silhouette"), Yurt Dışından | 1,589.78 | TL | TR retail price; cross-border; shipping not stated | https://www.hepsiburada.com/gui-xulian-nh35-nh35a-3-karakterli-takvim-3-igneli-kollu-hareket-yuksek-hassasiyetli-otomatik-mekanik-hareket-degistirme-yurt-disindan-pm-HBC00004VBOMZ | snapshot, undated | ≈ $32, a price that points to a Chinese clone or unknown origin |
| Humble NH35 movement (day-date set) | Hepsiburada (Humble), Yurt Dışından | 2,644.59 | TL | as above | https://www.hepsiburada.com/humble-nh35-hareket-gunu-tarih-seti-yuksek-dogruluk-otomatik-mekanik-saat-bilek-yurt-disindan-pm-HBC00005DDJF3 | snapshot, undated | ≈ $54 |
| Gui Xulian NH38/NH38A + stem + clutch lever | Hepsiburada (Silhouette), Yurt Dışından | 1,856.58 | TL | as above | https://www.hepsiburada.com/gui-xulian-nh38-nh38a-saat-hareketi-celik-kok-debriyaj-kolu-kiti-yuksek-hassasiyetli-otomatik-zincirleme-mekanik-saat-hareketi-yurt-disindan-pm-HBC00004VBNUW | snapshot, undated | page also says "Yurt Dışı Satış Yok", contradictory |
| Humble "2 takım" Japan NH70/NH70A skeleton | Hepsiburada (Humble), Yurt Dışından | 4,139.73 | TL | as above | https://www.hepsiburada.com/humble-2-takim-japonya-nh70-nh70a-ici-bos-otomatik-saat-hareketi-21600-bph-24-mucevher-yuksek-dogruluk-mekanik-saatler-icin-fit-yurt-disindan-pm-HBC00005L8RT7 | snapshot, undated | title says "2 sets"; unclear whether the price covers 1 or 2 |
| Talent NH35A movement | Hepsiburada, Yurt Dışından | unclear (snippet showed 709.99 / 411.75 / 557 TL, possibly from other products) | TL | — | https://www.hepsiburada.com/talent-nh35a-nh35-hareketi-yuksek-hassasiyetli-mekanik-saat-hareketi-tarihi-3-datewheel-24-mucevher-otomatik-kendinden-kurmali-yurt-disindan-pm-HBC00005IGQ1A | snapshot, undated | price unreliable |
| NH35A movement | Fruugo Türkiye | 2,399 + 217.49 shipping (RRP 4,099) | TL | shipping extra | https://www.fruugo.com.tr/nh35a-nh35-mekanik-mekanizma-c/p-125206074-263041589 | ~mid-2024 (delivery date shown was June 2024) | old |
| VENYAA NH35/NH35A + stem + hands | Amazon.com.tr | no price shown | TL | — | https://www.amazon.com.tr/VENYAA-Mekanizmas%C4%B1-Par%C3%A7alar%C4%B1-Otomatik-Hassasiyet/dp/B0CJ4KZCM6 | 2026-10-07 | appears unavailable |
| NH36/NH36A movement kit | Amazon.com.tr | no price shown | TL | — | https://www.amazon.com.tr/dp/B0BK8DMM63 | 2026-10-07 (search) | appears unavailable |
| Plawee NH34/NH34A GMT | Amazon.com.tr | no price in snippet | TL | — | https://www.amazon.com.tr/Plawee-Hareket-Tekerle%C4%9Fi-Hassasiyetli-Hareketi/dp/B0CQQ6QHRQ | snapshot | — |
| "Original Seiko SII NH35/NH35A", white date | Ubuy Türkiye (ships from a US store) | ~21 | KWD (≈ $68) | Ubuy pricing; duty treatment not confirmed (page returned 503) | https://www.ubuy.com.tr/tr/product/2Z69B7O-original-seiko-sii-nh35-nh35a-automatic-watch-movement-date-3-w-white-date-new | snapshot | — |

- Ekşi Sözlük (forum, undated): because of customs, movements can be found from a few tradesmen in **Sirkeci (Istanbul)** at roughly 2× the Chinese price — [Ekşi Sözlük "seiko mods" (via search summary; page 403)](https://eksisozluk.com/seiko-mods--7259896)

**C. Western mod-parts shops (reference for "genuine" pricing)**
- Crystaltimes (US): NH35 (CT501) $107–$114, NH36 $107, NH36 day-date $126–$152, NH38 (CT505) $134, 4R34 GMT (labelled "Genuine Seiko") $204–$218. The shop says "NH Movement prices have been steadily increasing throughout 2025-2026, and supply has been decreasing". It also says it is not affiliated with Seiko — [Crystaltimes movements, 2026-10-07](https://usa.crystaltimes.net/product-category/movements/)
- Nomods: NH70A skeleton $150, NH38A $140, NH34A $160. Its own guide text quotes older, lower prices (NH70 $70, NH36/NH38 $55) — [Nomods](https://nomods.co/collections/seiko-mod-movements)
- Lucius Atelier: TMI NH34 GMT white date $152–$192 — [Lucius Atelier](https://luciusatelier.com/products/seiko-tmi-nh34-automatic-movement-gmt-date-white)
- eBay: genuine NH34 GMT mostly about $195–$235, with China-based sellers around $176–$205 — [eBay NH34 search](https://www.ebay.com/shop/nh34-gmt-movement?_nkw=nh34+gmt+movement)
- Soflypart: "Genuine" new NH35 at $85 — [Soflypart](https://www.soflypart.com/product/seiko-nh35-mechanical-movement/)

**D. Genuine vs clone risk**
- Seiko Türkiye official notice (6 Oct 2025): fake watches are being sold at a discount on marketplaces and social media, some sellers use the Seiko logo to look authorised, and some present items as modified with "aftermarket" parts. Seiko says such watches are not covered by warranty — [Seiko TR notice](https://www.seikowatches.com/tr-tr/news/2025/importantnotice/20251006)
- AliExpress titles are unreliable. One listing says both "Japan Genuine" and "China NH35A" — [AliExpress 1005011797439544](https://www.aliexpress.com/item/1005011797439544.html). "Japan Original" eBay listings are often shipped from Shenzhen — [eBay.de](https://www.ebay.de/itm/146836722365)
- Older Turkish prices for context: an Ekşi user called the NH35 a ~$15 "price/performance monster" and later added that prices had risen. A Türkiye Saat Forumu user (about 3.5 years ago) cited about $20 on Alibaba — [Ekşi "seiko nh35"](https://eksisozluk.com/seiko-nh35--7828369); [TSF forum](https://forum.saatforumu.com/viewtopic.php?f=62&t=39475)
- Alibaba wholesale NH35/NH35A prices are $38–$59, with minimum orders of 1–100 pieces — [Alibaba showroom](https://www.alibaba.com/showroom/seiko-nh35-movement.html)
- A forum user found the quality gap between a Japanese NH35 and the Chinese PT5000 small (opinion) — [TSF forum](https://forum.saatforumu.com/viewtopic.php?f=62&t=39475)

### Inferences
- AliExpress has two price tiers. Listings claiming genuine Japan/TMI cost about $69–$108, roughly 3,400–5,300 TL before Turkish tax. Admitted clones cost about $21–$40 (≈ 1,050–1,960 TL). A genuine NH35A alone uses most of a 5000 TL budget once 2026 import costs are added.
- At about $32 equivalent, the Hepsiburada NH35 (1,589.78 TL) is priced like a Chinese clone, not a genuine TMI unit. Buyers should ask for rotor/bridge photos showing "TMI / Japan" markings before purchase.
- The NH70/NH72 skeleton appears to be the movement most reliably reachable from Turkey on AliExpress, since it showed in the TR-region search. It costs only slightly more than a claimed-genuine NH35.
- The NH34 GMT ($165–$209 ≈ 8,100–10,200 TL) does not fit a 5000 TL total build.

### Gaps
- No Trendyol or n11 listing for a standalone NH35 movement was found. Searches there returned only complete watches.
- No source covers specifically "Seagull" NH35 clones. Seagull appeared only as an ST36 skeleton listing.
- Store names and ratings for AliExpress movement sellers could not be extracted. I found no reliable 2025–2026 r/SeikoMods seller list (the search returned no Reddit pages).
- NH39A features (no-date / open-heart variant) are not verified here.

---

## Q2: NH35-compatible 316L cases (36–40 mm) with sapphire, display back, 50–100 m WR: prices and specs

### Takeaway
On AliExpress (US view), 36/39 mm sapphire cases for NH35 cost **about $12–$37**, and the transparent-back versions are mostly **$26–$48**. Nearly all take a **28.5 mm dial**. Some 38 mm cases take **29–29.5 mm**, and Royal Oak / Nautilus-type cases take **30.5–31.8 mm**. In Turkey the main options are two cross-border Hepsiburada listings: a **36 mm Geervo at 1,345.04 TL** and a **39 mm Humble display-back case at 2,041.21 TL**. Spacer and crown inclusion is rarely stated in the snippets.

### Cited Findings

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes (dial Ø / lug / thickness / WR / back / spacer-crown) |
|---|---|---|---|---|---|---|---|
| Humble 39 mm polished SS case, sapphire, display back | Hepsiburada, Yurt Dışından | 2,041.21 | TL | TR price; cross-border | https://www.hepsiburada.com/humble-39mm-paslanmaz-celik-cilali-kasa-safir-cam-fit-nh35-nh35a-nh36-nh35a-hareketi-seffaf-arka-kapak-yurt-disindan-pm-HBC00005SHPXI | snapshot, undated | dial 28.5–29.3 mm; 20 mm lug; NH35/NH36/Miyota 8215/ETA2824 claimed; spacer/crown not stated |
| Geervo 36 mm Oyster-style 316L case, sapphire | Hepsiburada (PDRPLNT), Yurt Dışından | 1,345.04 | TL | TR price; cross-border | https://www.hepsiburada.com/pdrplnt-geervo-36mm-nh35-kasa-oyster-perpetual-safir-cam-316l-paslanmaz-celik-nh36-hareketli-saat-duzenegi-icin-uygun-yurt-disindan-pm-HBC00005WJF3Q | snapshot, undated | 5 bar (50 m); size excludes crown; 6-month warranty; back type not stated |
| Feiyashi 36/40 mm case (NH34/35/36/38, Miyota 8215) | Turkish reseller page | — | — | — | https://gazianteptknikservisi.com.tr/price-Universal_136126/ | snapshot | claims 100 m; 28.5 mm dial |
| 42 mm domed-sapphire case | Turkish reseller page | — | — | — | https://karacafuar.com.tr/Supply_value_75352.html | snapshot | dial 28.5–29 mm; 22 mm strap |
| BOTIONI 36/39 mm 316L, bevel edge, sapphire | AliExpress (Choice) | 12.23 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007728245487.html | 2026-10-07 | 4.9★; dial/back not in title |
| 36/39 mm "Oyster style", sapphire, 28.5 mm dial | AliExpress | 15.59 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010508799088.html | 2026-10-07 | 4.8★; fits NH35/36/38, 4R36, Miyota 8215 |
| 36/39 mm "Air King", sapphire, 28.5 mm dial | AliExpress | 15.74 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009105620868.html | 2026-10-07 | 4.9★ |
| NEITON 36/39 mm SS, sapphire, 10 ATM | AliExpress (Choice) | 20.38 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007015151133.html | 2026-10-07 | 5★ |
| NEITON 36/39 mm, sapphire, 100 m, President bracelet | AliExpress (Choice) | 26.85 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007037700357.html | 2026-10-07 | 4.9★; NH35/36, ETA2824/2836 |
| Neiton 36/40 mm sapphire + Jubilee | AliExpress (Choice) | 28.00 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005006489129116.html | 2026-10-07 | 4.7★ |
| 36/39 mm NH35 case, 28.5 mm dial, 20 mm strap | AliExpress | 26.41 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007994904239.html | 2026-10-07 | 4.9★ |
| Goutent 39 mm, domed sapphire | AliExpress (Choice) | 32.19 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007628119020.html | 2026-10-07 | 4.9★; NH34/35/36, ETA2824, PT5000 |
| Retro 36/39 mm pilot, sapphire, 20 ATM + leather strap | AliExpress (Choice) | 28.03 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008579097479.html | 2026-10-07 | 4.8★ |
| 38 mm brushed 316L, flat sapphire, **29 mm dial** | AliExpress | 21.01 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011539186526.html | 2026-10-07 | 4.8★; NH35/36/38/70/72 |
| 38 mm fluted, **29.5 mm dial**, 100 m | AliExpress (Choice) | 17.39 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011631155834.html | 2026-10-07 | 5★ |
| 38 mm brushed diver, AR sapphire, 200 m | AliExpress | 16.65 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010238381959.html | 2026-10-07 | 4.9★ |
| 36/39 mm sapphire, **transparent back** + strap | AliExpress (Choice) | 36.34 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008192115118.html | 2026-10-07 | NH35/36/38/70 |
| 40 mm dive case, domed sapphire, **transparent back**, 20 bar + leather strap | AliExpress | 30.46 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005006116886233.html | 2026-10-07 | 5★ |
| SKX007-style 41 mm, 20 ATM, **transparent back**, crown 3.8 + bracelet | AliExpress | 26.10 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009939056576.html | 2026-10-07 | 4.9★; above the 36–40 mm brief |
| 38 mm SKX-style, sapphire, crown 3.8, **transparent or solid back** | AliExpress (Choice) | 47.71 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008940492718.html | 2026-10-07 | NH35/36/70, 4R |
| Grayss 37 mm integrated-bracelet case, sapphire, 20 ATM | AliExpress (Choice) | 19.55 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012736871275.html | 2026-10-07 | 4.9★ |
| 39 mm SS case, sapphire (TR-region visible) | AliExpress | 24.00 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012967653560.html | 2026-10-07 | shown in TR view |
| 39 mm transparent-back "butterfly" with strap (TR-region visible) | AliExpress | 22.50 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012270705511.html | 2026-10-07 | shown in TR view |
| 41 mm transparent-back case + strap (TR-region visible) | AliExpress | 29.85 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012976444235.html | 2026-10-07 | shown in TR view |
| Movement spacer ring NH35/36/38/39/70/72 | AliExpress (Choice) | 2.27–2.39 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010507635707.html ; https://www.aliexpress.com/item/1005010524921614.html | 2026-10-07 | 4.9–5★; buy separately if the case lacks one |

- Neiton 36 mm spec sheet (third-party page): 36 mm, **12.3 mm thick**, **20 mm lug**, 45 mm lug-to-lug, flat sapphire, **open (display) caseback**, **50 m**, screw-down crown, polished 316L. Dial size and spacer inclusion are not stated — [amauxboze Neiton 36 mm spec](https://amauxboze.com/pages/specification-neiton-case-36mm)
- A 10+-year-old Watchuseek owner review called Neiton a Chinese micro-brand, "very heavy" and thick, with good finishing (opinion) — [Watchuseek](https://www.watchuseek.com/threads/affordable-sapphire-automatic-neiton.3034418/)
- Tandorio (case/watch maker sold on AliExpress): a WatchCrunch reviewer measured an SKX-style example at 41 × 13.4 mm, lug-to-lug 45.4 mm, and found the build solid but without AR coating — [WatchCrunch Tandorio review](https://www.watchcrunch.com/Cantaloop/reviews/tandorio-skx-mod-review-45382)
- Search sources: [nh35-case-sapphire-36mm](https://www.aliexpress.com/w/wholesale-nh35-case-sapphire-36mm.html), [nh35-case-39mm-sapphire](https://www.aliexpress.com/w/wholesale-nh35-case-39mm-sapphire.html), [nh35-watch-case-38mm](https://www.aliexpress.com/w/wholesale-nh35-watch-case-38mm.html), [nh35-case-transparent-back-sapphire](https://www.aliexpress.com/w/wholesale-nh35-case-transparent-back-sapphire.html)

### Inferences
- For a 36–40 mm sapphire, display-back NH35 case, plan on about $25–$40 on AliExpress (≈ 1,200–2,000 TL before tax) or about 1,350–2,050 TL from a Hepsiburada cross-border listing. The local route costs about the same as import before tax, so it wins once Turkish import costs are counted.
- Dial-size rule from listing titles: Datejust/Oyster/Air King/SKX-type 36–40 mm cases take 28.5 mm. Some 38 mm field/fluted cases take 29–29.5 mm. Integrated "Oak/Nautilus" styles take 30.5–31.8 mm, and pilot kits ship with 32–33.5 mm dials. Buy the dial after the case.
- Spacers and crowns are cheap ($1–$5) on AliExpress. If a case listing does not explicitly include a spacer and stem/crown, budget about 150–300 TL extra.

### Gaps
- For most listings I could not confirm thickness, whether a spacer or crown is included, or whether the back is solid or display, because AliExpress item pages need JavaScript. Only titles were readable.
- No Trendyol or n11 standalone case listing was found.
- No independent 2025–2026 review ranks AliExpress case sellers (Neiton, Goutent, BOTIONI, Grayss, Tandorio).

---

## Q3: Dials, hand sets, dial dots, crowns: prices

### Takeaway
On AliExpress, normal (non-promotional) prices are about **$6–$12 for an NH35 hand set**, **$9–$15 for a 28.5 mm dial**, **$1–$5 for a crown or stem**, and **about $1 for dial-dot sheets**. In the TR-region view, hands and dials mostly show **$10–$22**. In Turkey I found almost no local dial or hand listings with prices. Hand-fitting tools are sold locally (Binbirsaat: 499 TL remover, 1,499 TL press).

### Cited Findings

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes |
|---|---|---|---|---|---|---|---|
| NH35 hand set, black/grey/gold/silver/rose/gun, green lume | AliExpress (Choice) | 5.70 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005013100851573.html | 2026-10-07 | 4.9★ |
| Datejust-type NH35 hands 8/12/12.5 mm, silver/gold | AliExpress (Choice) | 11.59 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012053052049.html | 2026-10-07 | 4.9★; dauphine/baton style |
| Seamaster 300 style hands | AliExpress (Choice) | 1.33 (promo) | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012013982710.html | 2026-10-07 | welcome-deal price |
| Mercedes/Submariner hands, silver/gold/rose | AliExpress (Choice) | price hidden | USD | — | https://www.aliexpress.com/item/1005008659046962.html | 2026-10-07 | 4.8★ |
| Nautilus hands (NH34/35/36/38/70/72) | AliExpress (Choice) | 7.29 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009540735268.html | 2026-10-07 | 4.9★ |
| Hands, green lume, silver/gold/rose (TR-region visible) | AliExpress | 9.00–10.20 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012164935173.html ; https://www.aliexpress.com/item/1005012730193649.html | 2026-10-07 | shown in TR view |
| GRAYSS sterile 28.5 mm dial, BGW9, date window | AliExpress (Choice) | 10.33 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012910373957.html | 2026-10-07 | 4.9★ |
| 28.5 mm Datejust sunburst dial | AliExpress | 9.25 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011897300914.html | 2026-10-07 | 4.9★ |
| 28.5 mm Roman "S" dial | AliExpress (Choice) | 14.71 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008981425139.html | 2026-10-07 | 4.5★ |
| 28.5 mm Kanagawa wave dial | AliExpress (Choice) | 28.58 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011913278282.html | 2026-10-07 | art dial |
| 28.5 mm sterile dial (TR-region visible) | AliExpress | 19.01 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012168996945.html | 2026-10-07 | shown in TR view |
| 28.5 mm retro green-lume dial (TR-region visible) | AliExpress | 15.00 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005008913101811.html | 2026-10-07 | 5★ |
| 28.5 mm dial + hands set (pilot/blue lume) | AliExpress (Choice) | 1.09 (promo) to 5.79 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010285476501.html | 2026-10-07 | 4.9★ |
| Dial-dot / double-sided adhesive sheets | AliExpress (Choice) | 0.99 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009797404467.html ; https://www.aliexpress.com/item/1005013232330160.html | 2026-10-07 | 4.8–5★; price may be promotional |
| Dial-feet replacement assortment | AliExpress | 12.77 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010177813158.html | 2026-10-07 | for dials without feet |
| SKX007 "S" crown, screw-in, with tube | AliExpress (Choice) | 1.09 (promo) | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005006170100222.html | 2026-10-07 | 5★ |
| High-quality NH35/36 "S" crown | AliExpress (Choice) | 5.38 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009384038946.html | 2026-10-07 | 4.9★ |
| Crown (3 styles) | AliExpress | 2.54 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005010741306783.html | 2026-10-07 | 4.6★ |
| NH34/35/36/38/39 stem kits | AliExpress (Choice) | 1.09 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009426667925.html | 2026-10-07 | 4.9★ |
| Yanluo 28.5 mm dial, green lume, NH35/36/4R/7S, crown 3/3.8/4 | Amazon.com.tr | price not visible | TL | — | https://www.amazon.com.tr/Yanluo-Kadran-Hareket-Saatleri-Par%C3%A7alar%C4%B1/dp/B0B1TW792G | snapshot | only local dial listing found |
| Hand remover tool | Binbirsaat (TR shop) | 499.00 | TL | TR retail (VAT incl. presumed) | https://www.binbirsaat.com/saat-saniye-akrep-yelkovan-cikarma-aleti-kadran-koruyucu-pmu112201 | snapshot | a 1,499 TL hand press is also listed per search summary |
| Movement holder NH35/36/7S26/4R36 | Hepsiburada (Humble), Yurt Dışından | 884.63 | TL | cross-border | https://www.hepsiburada.com/humble-seiko-7s26-7s36-4r36-nh35-nh36-hareket-hareketi-onarim-ve-montaj-araci-icin-saat-hareketi-tutucu-fit-yurt-disindan-pm-HBC00005L8OVC | snapshot | tool |

- eBay reference: NH35/36 hand sets at $14.94 (Shenzhen seller) and $16.50 for C3 lume (California seller). A Hong Kong listing at $30 includes import fees (for Germany) — [eBay.de hands](https://www.ebay.de/itm/395045954564); [eBay hands](https://www.ebay.com/itm/385605828331)
- Search sources: [nh35-hands](https://www.aliexpress.com/w/wholesale-nh35-hands.html), [nh35-dial](https://www.aliexpress.com/w/wholesale-nh35-dial.html), [dial-feet-sticker](https://www.aliexpress.com/w/wholesale-dial-feet-sticker.html), [nh35-crown](https://www.aliexpress.com/w/wholesale-nh35-crown.html)

### Inferences
- Budget about $6–$12 (≈ 300–600 TL) for hands, about $10–$15 (≈ 500–750 TL) for a plain 28.5 mm dial, and about $2–$6 for crown, stem and dial dots, all before Turkish import costs.
- Turkish marketplaces barely stock NH35 dials and hands. For these small parts the realistic options are AliExpress (with 2026 customs exposure) or Sirkeci tradesmen.

### Gaps
- No Trendyol, Hepsiburada or n11 TL prices were found for NH35 hand sets or dials. Cathedral and specific gold dauphine sets were not individually priced.
- I could not verify which "dial dot" listings are genuine watchmaker dial-dots (e.g., Bergeon-type) rather than generic double-sided tape.

---

## Q4: 20 mm straps: Turkish leather makers, rubber/FKM, steel bracelets

### Takeaway
Locally, genuine-leather 20 mm straps cost about **245–749 TL** on Amazon.com.tr and Trendyol. Etsy handmade (non-Turkish) straps are **$55–$95**. On AliExpress, FKM rubber is **$9–$17** and a 20 mm 316L oyster bracelet about **$24**. Buying the strap in Turkey is cheap and avoids customs.

### Cited Findings

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes |
|---|---|---|---|---|---|---|---|
| Black croco-pattern genuine leather 18/20/22/24 mm | Amazon.com.tr | 398.00 | TL | TR retail incl. KDV | https://www.amazon.com.tr/dp/B0CWP7BBFF | 2026-10-07 | — |
| Black genuine leather 18–24 mm | Amazon.com.tr | 398.00 | TL | incl. KDV | https://www.amazon.com.tr/dp/B09VXVQHDX | 2026-10-07 | — |
| Brown domed genuine leather (CHR1178) | Amazon.com.tr | 398.00 | TL | incl. KDV | https://www.amazon.com.tr/dp/B0H7Y5HMZB | 2026-10-07 | — |
| Genuine leather with steel clip, 20–24 mm (LS35) | Amazon.com.tr | 599.90 | TL | incl. KDV | https://www.amazon.com.tr/dp/B0DSLZ9MQF | 2026-10-07 | — |
| VAGAVE croco leather 20/22 mm classic | Amazon.com.tr (sponsored) | 749.00 | TL | incl. KDV | https://www.amazon.com.tr/dp/B0FX1HZYQ2 | 2026-10-07 | — |
| FRO 20 mm genuine Saffiano leather, burgundy, gold buckle | Trendyol | 524.26 (list 574.26) | TL | Trendyol basket price | product URL not captured (from a Trendyol search-engine snippet) | snapshot | search "FRO 20mm Hakiki Deri Safiano" on Trendyol |
| onlinekordon 20 mm croco-pattern leather, quick-release | Trendyol | 245 (from 250) | TL | basket price | https://www.trendyol.com/onlinekordon-saat-kordonu-x-b165249-c109117 | snapshot | "antialerjik deri" |
| Saatse 20 mm black croco | Trendyol | 298 | TL | coupon price | https://www.trendyol.com/suni-deri-saat-kordonu-x-c109117-a14-v105 | snapshot | — |
| Fado&Her "El Yapımı Hakiki Deri 20 mm" | Akakçe listing | price not visible | TL | — | https://www.akakce.com/saat-kordonu/20-mm-saat-kordonu.html | snapshot | Turkish brand explicitly marked handmade |
| Handmade leather strap 19/20 mm, French/Italian leather (HK artisan) | Etsy | 60–95 | USD | + intl shipping + TR customs | https://eternitizzzstrap.patternbyetsy.com/listing/621884111/leather-watch-strap-20mm-watch-strap | snapshot | not Turkish |
| Veg-tan Italian Buttero strap 18–22 mm | Etsy | from 55 | USD | + shipping/customs | https://www.etsy.com/listing/1290769871 | snapshot | — |
| 20 mm FKM rubber, flat end, quick release | AliExpress | 8.91 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009412195682.html | 2026-10-07 | 4.8★ |
| 20 mm FKM curved end, quick release | AliExpress (Choice) | 12.34 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012390664867.html | 2026-10-07 | 4.9★ |
| 20 mm FKM woven, deployant | AliExpress (Choice) | 17.29 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005009468200273.html | 2026-10-07 | 4.8★ |
| 20/21 mm 316L oyster bracelet, deployant | AliExpress | 24.49 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012642405469.html | 2026-10-07 | 4.8★ |

- AliExpress search sources: [20mm-fkm-rubber-strap](https://www.aliexpress.com/w/wholesale-20mm-fkm-rubber-strap.html), [20mm-oyster-bracelet-stainless](https://www.aliexpress.com/w/wholesale-20mm-oyster-bracelet-stainless.html). In the TR-region view, FKM and bracelet searches returned mostly unrelated items (1 FKM strap at $29.70).

### Inferences
- Buy the strap in Turkey. About 400 TL gets a genuine leather 20 mm strap with VAT included and no customs exposure. A Turkish handmade strap (Fado&Her-type) is a likely upgrade, but no price was confirmed.
- A cheap AliExpress FKM strap only makes sense if it ships in the same parcel as other parts.

### Gaps
- I found no confirmed Etsy Türkiye or Turkish artisan (handmade) 20 mm strap with a TL price. The Akakçe and Trendyol product pages were blocked (403).
- No Turkish-market price was found for steel bracelets sold separately.

---

## Q5: Complete-watch references: ready-built Seiko mods and NH35 watches in Turkey, and DIY kits on AliExpress

### Takeaway
A finished NH35/sapphire watch can be bought in Turkey for **about 4,300 TL (Steeldive SD1953 on n11, snapshot)**, which undercuts most DIY paths. Pagani Design NH35 watches are **11,999–14,999 TL**, and a genuine Seiko 5 automatic is **about 10,100–10,750 TL** on Amazon.com.tr. The Turkish mod shop SeikoModsTR lists NH35 "S Mod" builds at **about $377–$438** (≈ 18,500–21,500 TL). On AliExpress, case + dial + hands "mod kits" cost **$20–$67** before a movement is added.

### Cited Findings

| item | seller/site | price | currency | includes shipping/VAT? | URL | date seen | notes |
|---|---|---|---|---|---|---|---|
| Steeldive SD1953, 41 mm, NH35, sapphire, ceramic bezel, 30 bar | n11 (lowest offer) | 4,318.8 | TL | TR retail | https://www.n11.com/urun/steeldive-sd1953-japan-seiko-nh35-41mm-otomatik-erkek-kol-saati-siyah-s1-60801145 | snapshot, undated | strong "buy instead of build" benchmark |
| Raymond NH35-A JPN 41 mm, sapphire, 5 ATM | n11 (8 offers) | from 9,800 | TL | TR retail | https://www.n11.com/urun/raymond-nh35-a-jpn-erkek-kol-saati-59080278 | snapshot | 2-year warranty |
| 2xudc "Nologo" SKX-style NH35, 20 bar, steel bracelet | Hepsiburada, Yurt Dışından | 5,858.49 | TL | cross-border | https://www.hepsiburada.com/2xudc-nologo-kirmizi-siyah-insert-nh35-movt-diver-3-8-mekanik-saat-erkekler-nh35-movt-sunburst-kirmizi-20bar-su-gecirmez-skx-kol-saati-120-tiklama-cerceve-celik-bilezik-relogio-yurt-disindan-pm-HBC00005UUG4K | snapshot | out of stock |
| Pagani Design PD-1645 Datejust, NH35A, sapphire | Trendyol | 11,999 | TL | TR retail | https://www.trendyol.com/pagani-design-x-b160152?pi=2 | snapshot | — |
| Pagani Design PD-1690 Oyster 38 mm, NH35 | Hepsiburada (SBA Saat) | 12,999 | TL | TR retail | https://www.hepsiburada.com/pd-1690-oyster-perpetual-38mm-200m-su-gecirmez-japon-nh35-otomatik-mekanik-saat-safir-kristal-isikli-paslanmaz-celik-is-saati-pm-HBC00009G6P59 | snapshot | title says 200 m but spec says 10 ATM |
| Pagani Design PD-1685 Seamaster 42 mm | Hepsiburada / Trendyol | 13,499 | TL | TR retail | https://www.hepsiburada.com/pd-1685-seamaster-42mm-200m-su-gecirmez-japon-nh35-otomatik-mekanik-saat-safir-kristal-celik-saat-pm-HBC00009CHJQY | snapshot | — |
| Pagani Design PD-1694 40 mm / PD-1673 40 mm | Trendyol (category pages) | 14,999 / 13,999 | TL | TR retail | https://www.trendyol.com/pagani-design-x-b160152?pi=2 ; https://www.trendyol.com/mekanik-saat-y-s20482?pi=4 | snapshot | prices read from category-page snippets |
| Spinnaker Croft SP-5100-22, NH35 | Teksaat | 14,249.99 | TL | TR retail | https://www.teksaat.com/spinnaker-sp-5100-22-erkek-kol-saati | snapshot | — |
| 38 mm "Buxton" CD-1057 automatic, leather / 41 mm "Lydden Hill" CD-1056 | Amazon.com.tr | 14,999.99 / 15,599.99 | TL | incl. KDV | https://www.amazon.com.tr/dp/B0D73RN59J ; https://www.amazon.com.tr/dp/B0D73S7HH6 | 2026-10-07 | appear in the "nh35" search; movement not confirmed |
| Seiko 5 SNK621K (genuine, 7S26) | Amazon.com.tr | 10,750.00 | TL | incl. KDV | https://www.amazon.com.tr/dp/B001S7UJXW | 2026-10-07 | genuine-Seiko benchmark |
| Seiko 5 SNKK27K1 37 mm | Amazon.com.tr | 10,119.08 | TL | incl. KDV | https://www.amazon.com.tr/dp/B076NCJPQM | 2026-10-07 | — |
| Seiko 5 SNK355K1S / SNK381 | Amazon.com.tr | 10,499.00 | TL | incl. KDV | https://www.amazon.com.tr/dp/B000HG9M8S ; https://www.amazon.com.tr/dp/B0009MYUZU | 2026-10-07 | — |
| Seiko 5 Sports SRPG35K / SSK003K1 GMT | Amazon.com.tr | 18,695.00 / 24,020.78 | TL | incl. KDV | https://www.amazon.com.tr/dp/B096G3MNP2 ; https://www.amazon.com.tr/dp/B0B3GJYFQX | 2026-10-07 | — |
| SeikoModsTR "S Mod Classic Serisi" 36/40 mm steel (NH35) | smodstr.com (Turkish mod shop) | 401.62 (was 453.62) | USD as displayed to a US-geo visitor | not stated | https://www.smodstr.com/tr/shop/page/11 | 2026-10-07 | ≈ 19,700 TL; TL list price not shown |
| SeikoModsTR NH35 Submariner / Santos / Datejust / Explorer models | smodstr.com | 377.27–438.13 | USD (displayed) | not stated | https://www.smodstr.com/tr/shop/page/9 | 2026-10-07 | ≈ 18,500–21,500 TL |
| SeikoModsTR Royal Oak "Skeleton" NH72 / Nautilus "Open Heart" NH38 | smodstr.com | 498.98 / 450.30 | USD (displayed) | not stated | https://www.smodstr.com/tr/shop/page/9 | 2026-10-07 | — |
| SeikoModsTR Explorer 2 (orange GMT, NH34) | smodstr.com | 693.72 | USD (displayed) | not stated | https://www.smodstr.com/tr/shop/page/9 | 2026-10-07 | — |
| SeikoModsTR "Gym Watch" chronographs | smodstr.com | 352.93–389.47 | USD (displayed) | not stated | https://www.smodstr.com/en/shop | 2026-10-07 | movement not stated, probably quartz/mecaquartz (my inference) |
| Used "Modded watch Seiko NH35" (2023, Austria) | Chrono24 TR | 3,746 | TL | shipping excl. | https://www.chrono24.com.tr/all/modded-watch-seiko-nh35-movement--id46215930.htm | snapshot | used; negotiable |
| Used Pagani NH35, Tiffany-blue dial | DonanımHaber forum | 3,000 (sold) | TL | — | https://forum.donanimhaber.com/pagani-tiffany-mavisi-kadran-otomatik-seiko-nh35-mekanizma-2600-tl--155372009 | ~2023 | used |
| **DIY kit:** NH35 mod kit 36/39 mm DJ case, sapphire + bracelet | AliExpress | 29.26 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012871435692.html | 2026-10-07 | no movement |
| **DIY kit:** 40 mm GMT case kit, sapphire, ceramic bezel, 20 mm lug | AliExpress | 20.42 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012748518873.html | 2026-10-07 | no movement |
| **DIY kit:** 40 mm Yacht-Master kit + 316 bracelet, 28.5 mm dial | AliExpress (Choice) | 67.28 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005007225628436.html | 2026-10-07 | 4.9★ |
| **DIY kit:** 39 mm pilot case + 33.5 mm dial set, sapphire | AliExpress (Choice) | 34.68 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012726049756.html | 2026-10-07 | 5★ |
| **DIY kit:** 38 mm 10 ATM, glass back + 32 mm dial + hands, sapphire | AliExpress | 25.10 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005011982374424.html | 2026-10-07 | 5★ |
| **DIY kit:** 41 mm "Oak" case + 31.8 mm dial + hands + bracelet, sapphire | AliExpress (Choice) | 31.14 | USD | free shipping, no TR tax | https://www.aliexpress.com/item/1005012687538896.html | 2026-10-07 | 4.8★ |

- Abroad: custom NH35 mods are listed on eBay at about $170–$250, and one "Seiko MOD NH35" sold for €300 on eBay.de — [eBay Seiko NH35 mod](https://www.ebay.com/shop/seiko-nh35-mod?_nkw=seiko+nh35+mod); [eBay.de](https://www.ebay.de/itm/405812944560)
- A Trendyol Pagani listing says that if the watch is worn less than 10 hours a day, it may need hand winding (seller copy) — [Trendyol Pagani V2](https://www.trendyol.com/pagani-design/pagrne-pagani-tasarim-v2-japonya-nh35a-klasik-erkek-spor-saatler-p-743701669)
- AliExpress kit search sources: [nh35-mod-kit](https://www.aliexpress.com/w/wholesale-nh35-mod-kit.html), [nh35-watch-kit-diy](https://www.aliexpress.com/w/wholesale-nh35-watch-kit-diy.html)

### Inferences (illustrative bills of materials, my arithmetic, ~49 TL/USD)
- **A. "Local-first" build (Hepsiburada Yurt Dışından + Amazon TR):** movement 1,589.78 + Humble 39 mm display-back case 2,041.21 + AliExpress-priced dial (~$10 ≈ 500 TL) and hands (~$6 ≈ 300 TL) + leather strap 398 ≈ **4,830 TL**. With the Geervo 36 mm case (1,345.04) ≈ **4,130 TL**. This fits under 5000 TL, but movement origin is unverified and the dial/hands lack a Turkish source.
- **B. AliExpress, clone movement:** clone NH35 $25 + BOTIONI case $12.23 + GRAYSS dial $10.33 + hands $5.70 + spacer $2.39 + FKM $8.91 ≈ **$65 ≈ 3,160 TL before Turkish taxes**. At the old 60% flat rate this would be ≈ 5,060 TL, before any broker fees.
- **C. AliExpress, claimed-genuine NH35A:** same as B with an $88.56 movement ≈ **$128 ≈ 6,290 TL before taxes**, over budget even before customs.
- **D. Buy complete:** Steeldive SD1953 at about 4,319 TL (n11 snapshot) delivers NH35 + sapphire + 300 m-class case under budget. It can serve as a donor or base for a dial/hands mod.
- A boutique Turkish mod (SeikoModsTR, ≈ 18.5–21.5k TL) or a Pagani (12–15k TL) costs 2.5–4× the DIY budget, so DIY or a cheap homage is the only way under 5000 TL.

### Gaps
- SeikoModsTR's TL list prices were not visible. The site shows USD to a US geo-IP visitor. Its movement origin (genuine or clone) and warranty terms were not checked.
- The n11 Steeldive price is an undated snapshot and needs live confirmation.
- No AliExpress "complete kit including movement" listing was confirmed. Kits found exclude the movement, except fully assembled watches.

---

## Q6: Turkish-language modding communities and local part sources

### Takeaway
The Turkish scene is small. One dedicated mod retailer (SeikoModsTR) sells finished watches, not parts. Discussion lives on Türkiye Saat Forumu, DonanımHaber, Technopat and Ekşi Sözlük. Loose movements are reportedly available from a few Sirkeci tradesmen at about 2× the Chinese price. Online, loose NH-series parts are mostly cross-border "Yurt Dışından" Hepsiburada listings (sellers such as Humble, Silhouette/Gui Xulian and PDRPLNT/Geervo).

### Cited Findings
- **SeikoModsTR (smodstr.com)** calls itself "Türkiye'nin lider Seiko Mod mağazası". It offers NH35-based custom and homage models, plus "Saatini Oluştur" (build your watch), "Mod Arşivi" and "Hizmetler" (services) pages. Its shop has 11 pages of finished watches and no loose-parts category was visible — [SeikoModsTR shop](https://www.smodstr.com/tr/shop); [SeikoModsTR EN](https://www.smodstr.com/en/shop)
- **Türkiye Saat Forumu (TSF)** has a thread on NH35 movements in homage watches, with Alibaba prices of about $20 (older) and a PT5000 comparison — [TSF thread](https://forum.saatforumu.com/viewtopic.php?f=62&t=39475)
- **DonanımHaber** has a subforum "Saat Mekanizmaları ve Teknik Bilgiler" and a second-hand NH35 watch marketplace thread — [DonanımHaber subforum](https://forum.donanimhaber.com/saat-mekanizmalari-ve-teknik-bilgiler--f749); [DH sale thread](https://forum.donanimhaber.com/pagani-tiffany-mavisi-kadran-otomatik-seiko-nh35-mekanizma-2600-tl--155372009)
- **Technopat** thread "Seiko NH35 mekanizması nereden alınır?": no Turkish online importer is known, local watchmakers stock quartz, and AliExpress was over the €30 limit — [Technopat](https://www.technopat.net/sosyal/konu/seiko-nh35-mekanizmasi-nereden-alinir.3727547/)
- **Ekşi Sözlük** topics "seiko mods" and "seiko nh35": AliExpress offers many dial, hand and case options but "got more expensive". Sirkeci tradesmen sell movements at about 2× the China price — [Ekşi "seiko nh35"](https://eksisozluk.com/seiko-nh35--7828369); [Ekşi "seiko mods"](https://eksisozluk.com/seiko-mods--7259896)
- Official Seiko distribution in Turkey is Aydın Saat ("Grand Seiko, Seiko, Lorus Türkiye Distribütörü"). It is not a mod-parts source — [Aydın Saat Instagram](https://www.instagram.com/aydnsaat/); [Seiko TR stores](https://www.seikowatches.com/tr-tr/stores)
- Hepsiburada cross-border parts sellers seen: Humble (cases, movements, holders), Silhouette (Gui Xulian NH35/NH38), PDRPLNT (Geervo cases). An NH35 holder is also sold on n11 — [Hepsiburada Humble case](https://www.hepsiburada.com/humble-39mm-paslanmaz-celik-cilali-kasa-safir-cam-fit-nh35-nh35a-nh36-nh35a-hareketi-seffaf-arka-kapak-yurt-disindan-pm-HBC00005SHPXI); [n11 holder](https://m.n11.com/saat-hareketi-tutucu-tabani-nh35-36-7s26-7s36-4r36-hareketi-onarim-araci-gumus-P682496431)
- A teknofinal.com category sells generic hour/minute/second hands (black, white, metal), probably clock or quartz hands, not NH35 — [Teknofinal](https://www.teknofinal.com/akrep-yelkovan-saniye-malzemeleri)

### Inferences
- For a Turkish buyer in October 2026, a realistic sourcing order is: (1) Hepsiburada "Yurt Dışından" listings for movement and case, (2) a Sirkeci tradesman for a movement you can inspect in person (photos of TMI markings), (3) AliExpress only for small parts and only after checking that the listing ships to Turkey and what tax is charged at checkout.
- SeikoModsTR is a price ceiling and design reference, not a parts supplier.

### Gaps
- No Turkish Instagram or Trendyol shop selling loose NH35 dials and hands with TL prices was found. Instagram content is not indexed in the search results I got.
- No names or addresses of the specific Sirkeci tradesmen were found, and the "2× China price" claim is undated.
- Etsy Türkiye watch-part or strap sellers were not identified.
