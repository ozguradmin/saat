# Donör saat planı: teknik kimlik ve kadran geometrisi

Bu not, sahte "PATEK PHILIPPE" saatinin logosuz ikizinin hangi mekanizmayı kullandığını ve kadranı nasıl yerleştirildiğini inceliyor. Saatin düzeni şöyle: 12'nin altında iki haneli büyük tarih, 9'da gün ve 24 saat, 3'te "tarih" alt kadranı, 6'da açık kalp. Notun amacı, bu saatin kadranını "ozgur" yazılı özel bir kadranla değiştirmenin teknik koşullarını çıkarmak.

Araştırma tarihi: **2026-10-08**. Her iddianın yanında kaynak URL'si ve tarihi var. "Arama özeti" yazan yerlerde sayfa otomatik erişimi engelledi, bilgi arama motoru özetinden alındı. "Kendi ölçümüm" yazan değerler, bir ürün fotoğrafından piksel ölçümüyle hesaplandı. Bunlar **spesifikasyon değildir**, hata payı yaklaşık ±0,3–0,5 mm.

---

## 0. Özet

1. **Mekanizma sınıfı:** Bu düzeni üreten mekanizmalar Ø30,40 mm (13½''') çaplı, "ST25 formatındaki" Çin otomatikleri. Düzen şu: 12'de büyük tarih, 3 ve 9'da ibreli iki alt kadran, 6'da açık balans ("fly wheel").
   - Bu sınıftaki markalı mekanizma **Sea-Gull TY2525 / ST2525 / TY2625**. 3'te gün, 9'da ay var, yükseklik 7,90 mm.
   - Ucuz jenerik ikizler **H47 (2L27)**, **2L55** ve **W03**. Bunlarda 3'te **ay**, 9'da **gün** var, yükseklik 6,8–7,1 mm, fiyat £23,95–39,95 (Cousins 2018/2020).
   - Kullanıcının saatinde gün 9'da. Bu, **H47/2L55/W03 tipine** uyuyor.
2. **Elenen adaylar:**
   - TY2871 (12'de büyük tarih, ama 6'da 24 saat ve gün/gece var, açık kalp yok, Ø26–28 mm).
   - TY28xx/ST16 ailesinin geri kalanı.
   - Mingzhu/DG 2813/8205/8215 türevleri ve "6 ibreli" DG38xx: hepsi Ø26 mm. 6'da 24 saat ya da ay göstergesi var, büyük tarih + açık kalp birlikte yok.
3. **Gerçek ve süs göstergeler:** Bu sınıfın hiçbir mekanizmasında 24 saat ibresi ya da ibreli tarih yok.
   - Gerçek olanlar: büyük tarih (iki disk), gün ibresi ve ay ibresi.
   - 9'daki 24 saat skalası büyük olasılıkla **baskı süsü**. Patek'in 5327 tipi takvim kadranından kopyalanmış.
   - 3'teki "1…39" rakamlı halka **gerçek bir tarih halkası değil**. Altındaki ibre büyük olasılıkla ayda bir adım atan **ay ibresi** (12 konum).
4. **Hazır yedek kadran yok:** Bu mekanizmalar için AliExpress/eBay'de hazır ya da özel baskılı kadran bulunamadı. Kadran ayağı, alt kadran pinyonu ve pencere koordinatlarını veren teknik çizim de yayımlanmamış. **Özel kadran, donör saatin kendi kadranı şablon alınarak** (tarayıcı ve kumpasla ölçülerek) yapılmak zorunda.
5. **Mevcut tasarım uyumsuz:** Projede daha önce yapılan Ø28,5 mm NH38A/NH39 kadranları bu donöre **uymaz**. Kadran çapı, ayaklar ve açık kalp konumu farklı (NH38'de açık kalp 9'un altında, burada 6'da).
   - `tasarim/kadran/kadran.py` içindeki "coklu" stil bu düzen için doğru başlangıç noktası.
   - Ancak `sag_tip: "tarih"` büyük olasılıkla **"ay"** olmalı.

---

## 1. Aday mekanizmalar ve karşılaştırma

### 1.1 Ø30,40 mm sınıfı: büyük tarih 12 + iki alt kadran + açık balans 6 (uyan sınıf)

| Kalibre | Ø × H (mm) | 12 | 3 | 9 | 6 | Fiyat / not | Kaynak (tarih) |
|---|---|---|---|---|---|---|---|
| Sea-Gull **TY2525 / ST2525** | 30,40 × 7,90 | büyük tarih | gün ibresi | ay ibresi | açık balans, köprülü | 29 taş | [Grail TY2500 ailesi](https://reference.grail-watch.com/family/tianjin-ty2500) (sayfa güncelleme 28 Haz 2019; okundu 2026-10-08) |
| Sea-Gull **TY2625 / ST2625** (Seagull'un güncel listesi; TY2525 ile aynı düzen) | ≈30,40 × ≈7,90 | big date | "week hand" | "month" | "flywheel" | 29 taş, 21.600 A/s, 45 saat rezerv, stop-saniye, **54 $** | [en.seagullwatch.com TY2625](https://en.seagullwatch.com/products/open-heart-flywheel-movement-ty2625-st2625) (2026-10-08) |
| Cousins "TY2525" | 30,40 × 7,90 | Big Date @12 | Week Hand @3h | Month Hand @9h | Fly Wheel @6h | **£44,50** | [Cousins 2018 katalog, s.69](https://www.cousinsuk.com/PDF/products/8662_Cousins%202018%20WATCH%20MOVEMENTS%20Catalogue.pdf) (PDF 4 Oca 2018) |
| **H47 (2L27)** (jenerik) | 30,40 × **6,8** | Big Date @12h | **Month** | **Day** | Fly Wheel at 6h | **£28,50**. Kurma mili parça no H47401 | Cousins 2018 s.69 ve [Cousins 2020 s.74](https://www.cousinsuk.com/pdf/products/8662_cousins%202020%20watch%20movements%20catalogue1.pdf) (PDF 6 Ara 2019) |
| **2L55** (jenerik) | 30,40 × **7,10** | Big Date @12h | **Month** | **Day** | Fly Wheel at 6h | **£39,95** | Cousins 2018 s.69, 2020 s.74 |
| **W03** (jenerik) | 30,40 × **6,8** | Big Date @12h | **Month** | **Day** | Fly Wheel at 6h | **£23,95**. İbre delikleri: dakika Ø0,90, akrep Ø1,50, saniye Ø0,20 | Cousins 2018 s.70 (2020 katalogda yok) |
| Sea-Gull ST2575 | – | büyük tarih | – | – | açık kalp | alt kadran yok. Sea-Gull 819.382: 40 mm kasa, 14,5 mm kalınlık, safir, Roma rakamı | [longislandwatch 819.382](https://longislandwatch.com/products/sea-gull-automatic-big-date-watch-819-382) (2026-10-08, tükendi) |

Notlar:
- Cousins 2018 kataloğu TY2525 için "Hour, Minute & Small Seconds" yazıyor. Grail ve Caliber Corner ise merkez saniye diyor. Katalog satırı büyük olasılıkla TY2526'dan kopyalanmış bir hata.
- Grail tablosunda TY2525'in "Open Heart" sütunu "With bridge" yazıyor. Yani balans, kadran tarafında bir köprüyle tutuluyor. Cousins'in ST2501–2505 satırları da "Fly Wheel at 6h with extended pivot" diyor.
- **Seagull'un kendi mekanizmasını gerçek markalar da kullanıyor:** Thomas Earnshaw Baron ES-8187 "Grand Date Calendar Open Heart" için verilen motor kodu **"SG-TY2625-3A"** ([everywatch/Jomashop ilanı](https://asset.everywatch.com/thomas-earnshaw/watch-13376262), arama özeti, 2026-10-08). Earnshaw Admiral Duncan ES-8312: 43 mm, mineral cam, 229 $, kalibre adı verilmemiş ([watches.com](https://www.watches.com/products/admiral-duncan-grand-date-calendar-open-heart-automatic-scone-silver), 2026-10-08).
- **Ucuz saatte Sea-Gull ST2525 doğrulaması:** WatchUSeek/BudgetLightForum'daki "Cheap Chinese Watch Review #4" incelemesi Megir M3206'yı ele alıyor. Saatte 12'de büyük tarih, 3'te gün, 9'da ay, 6'da açık kalp var. İnceleyen içinde "what appears to be a Sea-Gull ST2525" bulmuş. Mekanizmada üretici işareti yok ("no observable manufacturer marks"). ([budgetlightforum.com/node/46561](https://budgetlightforum.com/node/46561), 5 May 2016)

### 1.2 Elenen adaylar ve elenme nedenleri

| Aday | Düzen | Ø × H | Neden uymuyor | Kaynak (tarih) |
|---|---|---|---|---|
| Tianjin **TY2871 / ST1661 / ST16L** | 12 büyük tarih, 3 ay, 6'da 24 saat ve gün/gece, 9 gün | Grail: 28,00 × 6,57. Caliber Corner: 26 mm (çelişkili) | 6'da açık kalp değil, 24 saat ve gün/gece var | [Grail TY2800 ailesi](https://reference.grail-watch.com/family/tianjin-ty2800) (2026-10-08). Caliber Corner TY2871 (arama özeti, 403): "26mm … 6.57mm". CC forumunda bir moderatör 26 mm'yi ST16 = Miyota 82xx benzerliğinden **çıkarıyor**, ölçüm değil |
| TY28xx (ST16) multifonksiyon: TY2867, TY2872, TY2876, ST16S2… | 3 tarih, 6 24 saat + gün/gece, 9 gün, 12 ay | Ø26–29,4 × 5,76–6,98 | 6'da hep 24 saat ya da gün/gece. Yalnız TY2876SK iskelet | Grail TY2800 (2026-10-08) |
| Mingzhu/Dixmont **DG2813 / 8205 / 8215**, "6-hands" **DG3836** vb. | DG3836: 3 tarih, 6 24 saat, 9 gün. DG3847: 3 ay, 6 24 saat, 9 gün, 12 yıl | Ø26,00 × 6,02–6,22 | Büyük tarih yok. 6 o'clock 24 saat alt kadranı | Cousins 2018 s.65–66. DG28 = Miyota 8215 klonu ([chinesewatchwiki DG28](https://chinesewatchwiki.net/DG28), son düzenleme 11 Kas 2014) |
| ML6102 | 2 sun/moon, 10'da 24 saat, 6'da fly wheel | Ø26 × 4,56 | Büyük tarih yok | Cousins 2018 s.65 |
| LB06 | 3 tarih, 9 gün, 12 güneş/ay, 6 fly wheel | Ø30,40 × 6,48. £13,95 | Büyük tarih yok (12'de güneş/ay var) | Cousins 2018 s.69 |
| R45 | 12 büyük tarih, 3 ay, 6 retro küçük saniye, 9 gün | Ø30,40 × 6,85 | 6'da açık kalp yok | Cousins 2018 s.69 |
| Sea-Gull TY2529 | 12 büyük tarih, 3 gün, 6'da 24 saat, 9 ay | 30,40 × 7,90 | Açık kalp yok | Grail TY2500 |
| "Shanghai 2650" | – | – | Kaynak bulunamadı. Grail'deki 2650 bir **ETA** kalibresi (bayan, 7¾''') | arama özeti 2026-10-08 |
| Hangzhou 2196 | 3 alt kadran: tarih, 24 saat, gün | – | Bir forumcuya göre kadran plakası balansı kapatıyor (tek kaynak) | arama özeti, Caliber Corner (403) |

**Sonuç:** Kullanıcının tarif ettiği düzen (12 büyük tarih + 3/9 alt kadran + 6 açık kalp) yalnızca **Ø30,40 mm ST25 formatı** ile örtüşüyor. 9'da gün olması, onu Sea-Gull TY2525/2625'ten (gün 3'te) ayırıp **H47 (2L27) / 2L55 / W03 jenerik tipine** yaklaştırıyor. Bu son kısım bir çıkarım. Kesin kimlik ancak arka kapak açılınca görülebilir, ama mekanizmalar çoğu zaman işaretsiz.

---

## 2. Hangi göstergeler gerçek, nasıl ayarlanır?

- **Büyük tarih (12):** Gerçek. Tasarım iki diskli:
  - Onlar diskinde 0–3, birler diskinde 0–9 var.
  - TY2625 ürün fotoğrafında sol disk "0 1 2 3" dizisini tekrarlıyor, sağ disk 0–9 rakamlarını taşıyor (kendi gözlemim, [ürün görseli](https://en.seagullwatch.com/cdn/shop/files/2625.jpg), 2026-10-08).
  - WUS'ta bir kullanıcıya göre, büyük tarih "two smaller wheels" olduğu için 6'daki açık kalbe engel olmuyor (arama özeti, [WatchUSeek "open heart with date"](https://www.watchuseek.com/threads/looking-for-a-watch-with-open-heart-and-date-function.5608133/), 2025 başı; site tollbit ile engelli).
- **Gün ve ay ibreleri:** Sea-Gull TY2525/2625'te 3'te gün, 9'da ay var. H47/2L55/W03'te tersine, 3'te ay, 9'da gün. Bu sınıfın hiçbir kataloğunda **24 saat ibresi ya da ibreli 1–31 tarih yok** (Grail TY2500 tablosu; Cousins 2018 s.68–70; Cousins 2020 s.74).
- **Yan düğmeler:** Megir M3206 (ST2525 benzeri) incelemesinde iki gizli düğme var: "The top one changes the date, and the bottom changes the month." 4'teki bir düğme de "do function" deniyor ([budgetlightforum](https://budgetlightforum.com/node/46561), 5 May 2016). Haftanın gününün nasıl ayarlandığı yazılmamış. H47 tipinin düğme ataması için **kaynak bulunamadı**.
- **Genel kural (benzer Çin multifonksiyon kılavuzu):** Earnshaw ES-8043 (gün/tarih/ay/24 saat) kılavuzu şöyle diyor:
  - Tarih 4'teki düğmeyle, gün 8'dekiyle, ay 10'dakiyle düzeltiliyor.
  - "You must not use this quick change corrector between 11:30 p.m. and 5:30 a.m."
  - Ayar sırası: ibreleri 06:00'ya getir, düzelticileri kullan, sonra ibreleri ileri çevir.
  - Kaynak: [ES_IM_ES-8043.pdf](https://cdn.shopify.com/s/files/1/0717/1979/files/ES_IM_ES-8043.pdf) (PDF değişiklik tarihi 19 Tem 2018). **Farklı bir mekanizma**, yalnız genel yöntem olarak alınmalı.
- **Patek kopyası olan tasarım dili:** Patek 5327'nin işlevleri resmi sayfada "Day, date, month, leap year and 24-hour indication by hands" ([patek.com 5327G-001](https://www.patek.com/en/collection/grand-complications/5327G-001), 2026-10-08). Bir ilan özetine göre yerleşim şöyle: 9'da "combination 24-hour/radial day register", 3'te "month/leap year", 6'da "moon phase/radial date" (arama özeti, 5327G ilanları, 2026-10-08).
  - Sahte kadran bu dili taklit ediyor: 9'da gün + 24 saat, 3'te takvim halkası. Ama altındaki ucuz mekanizma 24 saati sürmüyor (çıkarım).

**Donör satın alınmadan önce yapılacak test (öneri):**
1. Kurmayı ikinci konuma çek. İbreleri 2–3 kez 24 saat ileri çevir.
2. Gece yarısı büyük tarih ve gün ibresi atlamalı. 9'da ayrı bir 24 saat ibresi varsa günde bir tur dönmeli.
3. 3'teki ibre bu sırada hiç oynamıyorsa ve yalnız bir düğmeyle 1/12 tur atlıyorsa, o bir **ay** ibresidir.
4. Düğmelere basmadan önce saat 06:00 civarına getirilmeli.

---

## 3. 3'teki "39"a kadar giden rakamlar neden olabilir?

1. **En olası açıklama, baskı ile işlev uyuşmazlığı:** Bu sınıfta 3'teki ibre **ay** (H47/2L55/W03) ya da **gün** (TY2525/2625). İkisi de 1–31 tarih değil. Kadrandaki rakam halkası ibrenin işleviyle eşleştirilmeden basılmış bir süs.
   - 31'den büyük rakamlar, halkanın hiçbir takvim işlevine bağlı olmadığını gösteriyor (çıkarım).
   - Sahte saatlerde çalışmayan ya da anlamsız alt kadranlar sık görülen bir işaret. Montres-Passion'ın EYKI incelemesine göre "some elements … serve no purpose and are present purely for aesthetics" ([montres-passion.fr](https://www.montres-passion.fr/?p=11518), 5 Şub 2026, önceki notlardan).
2. **Rakam büyük tarih penceresinde görüldüyse:** İki diskli bazı büyük tarih mekanizmaları 31'den sonra 32…39 ve 00 üzerinden 01'e geçer. Bu, elle düzeltme gerektiren bilinen bir tasarım özelliği.
   - Caliber Corner Ronda 509/519 için bunu yazıyor: "counts through 32 to 39 and then 00 before it reaches 01", ayrıca "doesn't point to a counterfeit" ([calibercorner – big date](https://calibercorner.com/how-big-date-complication-works), arama özeti, 403).
   - Bir Davis kılavuzu da iki halkalı büyük tarihin 31'den 1'e elle çevrilmesi gerektiğini yazıyor (libble.eu, arama özeti, 403).
   - TY2625'in birler diski yalnız 0–9 rakamlarını taşıyor (fotoğraf). Yani 31'den 01'e geçişin nasıl çözüldüğü belirsiz.
   - **Bu mekanizmanın 32–39 gösterip göstermediği doğrulanmadı.**
3. Hangisi olduğunu kesinleştirmek için §2'deki test yeterli.

---

## 4. Geometri: mekanizma, kadran, ibreler, pencereler

### 4.1 Mekanizma
- **Çap:** 30,40 mm, yani 13½'''. Grail ailesi "30.40 or 37.20 mm". 37,20 mm yalnız TY2553/2561/2563'te geçiyor.
- **Yükseklik:** TY2525/2625 7,90 mm, 2L55 7,10 mm, H47/W03 6,8 mm (Grail; seagullwatch; Cousins).
- **Ayar ve kurma:** ST25 ailesi Incabloc, elle kurulabilir, stop-saniyeli, 21.600 A/s, 45–48 saat rezerv. Kaynak: Caliber Corner ST25, arama özeti (403). Seagull TY2625 sayfası "Stop-seconds" ve "45 reserve hours" diyor.
- **Kasa referansı:** Sea-Gull'un ST25'li 42 mm saatleri 13–14 mm kalınlıkta (arama özeti, seagullwatches.com ürün sayfaları, 2026-10-08). Sea-Gull 819.382 (ST2575): 40 × 14,5 mm.

### 4.2 Kadran çapı ve kalınlığı
- Ø30,4'lük ST25 formatı için satılan kadranlar 34,5–37 mm aralığında:
  - "**37 mm** Parnis weißes Zifferblatt passt Seagull ST2505" ([eBay 173239156168](https://www.ebay.de/itm/173239156168), arama özeti, 403).
  - "**34,5 mm** … Zifferblatt passt Seagull 2555.2557 GMT" ([eBay 175727448275](https://www.ebay.de/itm/175727448275), arama özeti). Bu bir satıcı iddiası, ölçüm değil.
- **Donörün kadran çapı bilinmiyor.** 42 mm kasada 34,5–37 mm aralığı makul, ama ölçülmeli.
- **Kalınlık:** Kadran boş diskleri 0,4 mm pirinç olarak satılıyor ("Thickness of disc is 0.4mm", Ø1,8 mm delik, 8,95 $; [Esslinger](https://esslinger.com/watch-dials-blank-brass-dial-discs), 2026-10-08). NH35 resmi kadranı da 0,40 ± 0,04 mm (önceki not: `5000 TL altı…/teknik_olculer.md`). Ucuz Çin multifonksiyon kadranının kalınlığı ve malzemesi için **kaynak yok**. Mikrometreyle ölçülmeli.

### 4.3 Kadran ayakları
- ST25, TY2625, H47, 2L55 ve W03 için **yayımlanmış ayak konumu bulunamadı.**
- Benzer bir dilekte, bir WRT kullanıcısı NH35 dışındaki mekanizmalar için şablon bulamadığını, kadranı kâğıda bastırıp ayak izini çıkardığını yazıyor (arama özeti, [watchrepairtalk 27725](https://watchrepairtalk.com/topic/27725-dial-feet-stencil-for-seiko-dials), 2026-10-08).
- Esslinger ilanlarında ayak yerleri yalnız fotoğrafta işaretli, sayısal değer yok (NN4801 ve TY2504 sayfaları, 2026-10-08).
- Ayak çapı için genel piyasa ölçüsü: Boley pirinç kadran ayağı "2.5 × 0.64 × 3.00 mm" (arama özeti; boyut etiketi belirsiz).

### 4.4 İbre delikleri

| Mekanizma | Akrep | Yelkovan | Saniye | Alt kadran | Kaynak |
|---|---|---|---|---|---|
| W03 (jenerik, H47 sınıfı) | Ø1,50 | Ø0,90 | Ø0,20 | – | Cousins 2018 s.70 |
| TY2504 (ST25 ailesi) | 1,50 | 1,0 | 0,21 | 0,20 (tarih/hafta ibreleri) | [Esslinger TY2504](https://www.esslinger.com/chinese-seagull-5-hand-automatic-watch-movement-ty2504-retrograde-week-at-2-30-retrograde-date-at-9-30-fly-wheel-at-6-00-overall-height-9-1mm/), 59,95 $. Toplam yükseklik 9,1 mm, mekanizma 7,40 mm (2026-10-08) |
| 2501 (ST25) | Ø1,55 | Ø1,00 | Ø0,26 | – | Cousins 2018 s.68 |
| DG3886 (Ø26 multifonksiyon, karşılaştırma) | Ø1,52 | Ø1,00 | Ø0,17 | Ø0,16 | Cousins 2018 s.68 |

Donör planında ibreler büyük olasılıkla **yeniden kullanılır**. Bu değerler ancak ibre değişirse gerekir.

### 4.5 Alt kadran pinyonları, büyük tarih penceresi, açık kalp (kendi ölçümüm)

**Yöntem:**
- Görsel: Seagull'un TY2625 ürün fotoğrafı ([2625.jpg](https://en.seagullwatch.com/cdn/shop/files/2625.jpg), 1997×1721 px, 2026-10-08).
- Mekanizma kenarının alt yarısına daire uydurdum: merkez (886,5; 833,3) px, R = 629,4 px.
- 30,40 mm çapa göre ölçek 41,4 px/mm. Merkez pinyonu, uydurulan merkeze 0,27 mm içinde düştü.
- Değerler **yalnız TY2625 için** ve fotoğraf perspektifi nedeniyle ±0,3–0,5 mm hatalı olabilir.
- H47/2L55/W03'ün aynı koordinatları paylaştığı **doğrulanmadı**. Bu mekanizmalarda 3 ile 9'un işlevi ters, yani farklı bir tasarım.

| Öğe | Konum (merkeze göre, 12 = 0°, saat yönü) | Boyut |
|---|---|---|
| 9 alt kadran pinyonu | r ≈ **7,2 mm**, ≈ 271° | – |
| 3 alt kadran pinyonu | r ≈ **7,0 mm**, ≈ 92° | – |
| Büyük tarih (iki rakamın göründüğü yer) | merkez ≈ **6,8 mm yukarıda**, 0° | rakam yüksekliği ≈ 2,3 mm. İki rakamın toplam eni ≈ 4,1 mm. Pencere için ≈ 4,5 × 2,8 mm gerekir (benim tahminim) |
| Balans ekseni (açık kalp merkezi) | ≈ **7,9–8,0 mm aşağıda**, 180° | platin açıklığı ≈ 10,4 × 9,7 mm. Kadran tarafı balans köprüsünün eni ≈ 17,5 mm, iki taş vidası arası ≈ 14,2 mm, köprü yüksekliği (düzlemde) ≈ 3,3 mm |

**Projedeki `kadran.py` "coklu" ayarlarıyla karşılaştırma (çıkarım):**
- Projede şu oranlar kullanılıyor: `sol/sag_merkez ±0,430·R`, `kalp_merkez −0,445·R`, `buyuk_tarih_merkez +0,330·R`.
- R = 17,5 mm (35 mm kadran) alınırsa bunlar 7,5 / 7,8 / 5,8 mm eder. TY2625 ölçümüm 7,0–7,2 / 7,9–8,0 / 6,8 mm.
- Büyük tarih penceresi yaklaşık 1 mm farklı. Değerler **donörden ölçülmeden** üretim yapılmamalı.
- Ayrıca `sag_tip: "tarih"` (3'te 1–31 halka) H47/2L55/W03'te **ay** olmalı. Saatte gün 3'teyse (TY2625) `sol/sag` tipleri yer değiştirmeli.

---

## 5. Yedek ve özel kadran bulunabilirliği

- **Hazır kadran:** ST2525/TY2625/H47/2L55/W03 büyük tarih düzeni için AliExpress/eBay'de **hiç kadran ilanı bulunamadı** (arama: "ST2525 dial", "TY2525 dial", "海鸥 2525 表盘 尺寸 脚位", 2026-10-08).
  - Bulunan ST25 "Datumsscheibe" ilanı TY2530 içindi (3'te tarih). Bu, 12'deki büyük tarih düzenine uymuyor ([eBay 305722385081](https://www.ebay.de/itm/305722385081), arama özeti).
  - Homage-forum'da bir kullanıcı, NH35 dışındaki az bilinen mekanizmalar için AliExpress'te özel logolu kadran bulamadığını yazıyor (arama özeti, homage-forum, 2026-10-08).
- **Çıplak mekanizma** bulunabiliyor:
  - ST2525 eBay'de yaklaşık £24–39 (arama özeti).
  - Seagull TY2625 54 $ (resmi, 2026-10-08).
  - H47 £28,50 ve 2L55 £39,95 (Cousins 2020 katalog fiyatı; güncel stok bilinmiyor; cousinsuk.com 403).
  - Yani **mekanizma arızasında** aynı sınıftan yedek bulunabilir. Ancak ayak ve pinyon uyumu teyitsiz.
- **Kadran ayağı ve pinyon uyumu:** Farklı mekanizmalarda ayak yerlerinin değiştiği, alt kadran aralığının küçük farklarla kaydığı forumlarda sık geçiyor. Örnek: ST19 ile 7733 kadranları "won't swap directly" (homage-forum, arama özeti). **Kadran, donörün kendi mekanizmasından ölçülmeli.**

---

## 6. Donör planına teknik sonuçlar

1. **Donör satın alırken:**
   - Satıcıdan kadran ve arka kapak fotoğrafı ile ibrelerin döndüğü bir video istenmeli.
   - 12'de büyük tarih, 9 ve 3'te alt kadran, 6'da açık balans olmalı.
   - 9'da tek ibre mi iki ibre mi olduğuna bakılmalı (24 saat gerçek mi?).
2. **Saatçide (sökme ve ölçme):**
   - (a) Mekanizma çapı ve yüksekliği. Ø30,4 ve 6,8–7,9 bekleniyor.
   - (b) Kadran çapı ve kalınlığı.
   - (c) İbreler çıkarılınca kadranın her iki yüzü 2400 dpi düz yataklı tarayıcıda, cetvelle birlikte taranmalı.
   - (d) Mekanizmanın kadran tarafı da aynı şekilde taranmalı.
   - (e) Tarama üzerinden şunların koordinatları çıkarılmalı: merkez deliği, iki pinyon deliği, büyük tarih penceresi, açık kalp kesiği, ayaklar. NH35 föyü gibi resmi bir föy **olmadığı için tek güvenilir yol bu**.
3. **Yeni kadran:**
   - Aynı dış çap ve kalınlıkta olmalı (çok farklı kalınlık ibre boşluklarını bozar).
   - Ayaklar aynı yerde olmalı. Pinyon delikleri, alt kadran ibrelerinin pinyon çapından biraz büyük açılmalı.
   - Büyük tarih penceresi rakamların tam üstüne gelmeli.
   - 6'daki kesik, kadran tarafındaki balans köprüsünü (yaklaşık 17,5 mm genişlik) ve balansı serbest bırakmalı.
   - 3'teki alt kadran **ay** olarak (12 bölme) basılmalı. Gün 3'teyse işlevler yer değiştirmeli.
   - 9'a 24 saat halkası basılacaksa yalnız süs olacağı bilinmeli. Daha temiz çözüm: sadece gün.
4. **Projedeki NH38A/NH39 Ø28,5 tasarımları bu donöre uymaz.** "coklu" stil donörden ölçülen değerlerle yeniden üretilmeli.

---

## 7. Boşluklar ve erişim engelleri

- ST25, TY2625, H47, 2L55 ve W03 için **resmi teknik çizim yok.** Kadran ayakları, pinyon koordinatları, büyük tarih penceresi ve açık kalp ölçüsü yayımlanmamış. Elimdeki tek veri fotoğraftan yapılan tahmin.
- H47 (2L27), 2L55 ve W03'ün **üreticisi bilinmiyor.** Tek kaynak Cousins'in 2018/2020 katalogları. W03 2020'de yok. Güncel fiyat ve stok bilinmiyor. WatchRepairTalk'ta bir kullanıcı CH2L27 için patlatılmış çizim bulamamış ([WRT 2276](https://watchrepairtalk.com/topic/2276-chinese-movement-info), 2 Haz 2015).
- Türkiye'deki sahte Patek ya da Forsining/Winner donörünün içinde **hangi kalibrenin olduğu doğrulanmadı.** Burada yalnız düzen eşleşmesine dayanan bir çıkarım var.
- H47 tipinde düğme atamaları ve gün ayarı doğrulanmadı.
- ST25 büyük tarihinin 31'den 01'e geçişi (32–39 görünüp görünmediği) doğrulanmadı.
- Donör kadranının çapı, kalınlığı ve malzemesi (pirinç mi, alüminyum mu) bilinmiyor.
- **Engellenen siteler (yalnız arama özetleri kullanıldı):** calibercorner.com (403), watchuseek.com (tollbit 307), cousinsuk.com web sayfaları (403; PDF kataloglar indirilip okundu), ebay (403), amazon (500), hourstriker ve watchbase (403), libble.eu ve manuals.plus (403).

## 8. Kaynak listesi
- Grail Watch Reference – Tianjin TY2500 family: https://reference.grail-watch.com/family/tianjin-ty2500 (güncelleme 28 Haz 2019; okundu 2026-10-08)
- Grail Watch Reference – Tianjin TY2800 family: https://reference.grail-watch.com/family/tianjin-ty2800 (okundu 2026-10-08)
- Seagull resmi – TY2625/ST2625: https://en.seagullwatch.com/products/open-heart-flywheel-movement-ty2625-st2625 ve görsel https://en.seagullwatch.com/cdn/shop/files/2625.jpg (2026-10-08)
- Seagull resmi – TY2502/ST2502: https://en.seagullwatch.com/products/open-heart-flywheel-movement-ty2502-st2502 (Ø30,40, 7,40 mm, 29 taş, 48 $; 2026-10-08)
- Cousins UK 2018 Watch Movements Catalogue (s.65–70): https://www.cousinsuk.com/PDF/products/8662_Cousins%202018%20WATCH%20MOVEMENTS%20Catalogue.pdf (PDF oluşturma 4 Oca 2018)
- Cousins UK 2020 Watch Movements Catalogue (s.74): https://www.cousinsuk.com/pdf/products/8662_cousins%202020%20watch%20movements%20catalogue1.pdf (PDF oluşturma 6 Ara 2019)
- BudgetLightForum – Megir 3206 w/ Sea-Gull ST2525: https://budgetlightforum.com/node/46561 (5 May 2016)
- Esslinger TY2504: https://www.esslinger.com/chinese-seagull-5-hand-automatic-watch-movement-ty2504-retrograde-week-at-2-30-retrograde-date-at-9-30-fly-wheel-at-6-00-overall-height-9-1mm/ (2026-10-08)
- Esslinger NN4801 (12'de büyük tarih, 25,6 mm, akrep 1,00, 39,95 $): https://www.esslinger.com/chinese-1-hand-automatic-gents-watch-movement-nn4801-big-date-at-12-00-movement-overall-height-7-3mm/ (2026-10-08)
- Esslinger boş pirinç kadran diski: https://esslinger.com/watch-dials-blank-brass-dial-discs (2026-10-08)
- Earnshaw ES-8043 kılavuzu: https://cdn.shopify.com/s/files/1/0717/1979/files/ES_IM_ES-8043.pdf (19 Tem 2018)
- Earnshaw Baron ES-8187 "SG-TY2625-3A": https://asset.everywatch.com/thomas-earnshaw/watch-13376262 (arama özeti, 2026-10-08)
- watches.com Admiral Duncan ES-8312: https://www.watches.com/products/admiral-duncan-grand-date-calendar-open-heart-automatic-scone-silver (2026-10-08)
- Long Island Watch Sea-Gull 819.382 (ST2575): https://longislandwatch.com/products/sea-gull-automatic-big-date-watch-819-382 (2026-10-08)
- Patek 5327G-001 resmi: https://www.patek.com/en/collection/grand-complications/5327G-001 (2026-10-08)
- Caliber Corner – big date 32–39: https://calibercorner.com/how-big-date-complication-works (arama özeti, 403)
- Chinese Watch Wiki – DG28: https://chinesewatchwiki.net/DG28 (11 Kas 2014)
- Chinese Watch Wiki – Chinese tourbillon watches ("marketing of open-heart watches as 'tourbillon'"): https://chinesewatchwiki.net/Chinese_tourbillon_watches (2026-10-08)
- East Watch Review – Guangzhou day/date/month/24h (42 mm, 6'da 24 saat): https://www.eastwatchreview.com/blog/2015/6/10/hands-on-guangzhou-automatic-with-date-day-month-24-hour-dislplay (10 Haz 2015)
