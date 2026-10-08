# Klasik dress-saat kadranlarının tasarım dili: Roma rakamları, dakika halkası, guilloché, açık kalp, ibreler

Hazırlanma tarihi: 8 Ekim 2026. Amaç: "ozgur" için Ø28,5 mm kadran (görünen alan yaklaşık Ø27 mm, yani R ≈ 13,5 mm). Fotoğraftaki sahte "Patek" saatin havası korunacak, ama zevkli ve dürüst olacak: sahte alt kadran yok, sahte marka yok.

**Erişim ve yöntem notu**
- Bu turun WebSearch kotası (200 arama, tüm alt ajanlarla paylaşılan) bu görev başlarken **dolmuştu**. Bu yüzden hiç arama yapılamadı.
- Bilinen ya da gezinerek bulunan URL'ler doğrudan okundu (WebFetch/curl). Fratello'da etiket ve marka arşivleri gezildi, Patek, Breguet, Longines, Orient ve Seiko'nun ürün sayfaları okundu.
- **Erişilemeyenler:**
  - hodinkee.com: araç engelledi.
  - frederiqueconstant.com ve cartier.com: 403.
  - breguet.com: curl ile 000, WebFetch ile okunabildi.
  - Monochrome ve aBlogtoWatch etiket sayfaları: 404.
  - WatchUSeek: 202 (bot engeli).
- **Ölçüler:** "(ölçümüm)" diye işaretli oranlar, markaların resmi ürün fotoğraflarından piksel üzerinde benim yaptığım ölçümlerdir. Hata payı yaklaşık ±%5. FC fotoğrafı perspektifli olduğu için daha kaba.
- Kardeş notlar:
  - `ekonomi_ve_sahtecilik.md`: sahte saatin mekanizması, maliyeti ve hukuku
  - `beyaz_kadran_malzemeleri.md`: lazer/PCB malzemeleri
  - `roma_parcalari.md`: ibre ve kasa fiyatları
  - `../5000 TL altı özel saat yapımı/teknik_olculer.md`: TMI NH35/NH38 ölçüleri

---

## 0. Kısa cevap (karar için en önemli 8 madde)

1. **Sahte saati "zengin" gösteren şey çok sayıda gösterge değil, doku bölgelemesi ve ışık oyunudur.** Merkezde desen, çevrede düz bir saat halkası ve parlayan uygulamalı işaretler bunu sağlar. Saygın saatlerin hepsi bunu yapıyor:
   - FC Classic Heart Beat FC-930: dış çevre beyaz lake, üzerinde boyalı Roma rakamları; merkez güneş ışını (sunburst) ([Fratello, 29 Ağu 2022](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/)).
   - Breguet 7337: dışarı kaydırılmış saat bölgesinde Clous de Paris, dış kadranda dairesel arpa tanesi (barleycorn) deseni ([Fratello, 4 Eki 2022](https://www.fratellowatches.com/breguets-new-classique-7337-calendrier-moonphase/)).

   Bunu bir lazer/PCB kadranında, sahte alt kadranlar olmadan yapmak mümkün.
2. **NH38A'nın balansı saat 9'da, 6'da değil.** Açık kalp penceresi en fazla Ø10 mm olabilir. Pencerenin merkezi kadran merkezinden 6,85 mm uzakta, saat 12'den saat yönünde 265,3°'de, yani 9 çizgisinin 4,7° altında ([TMI NH38 föyü](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf), `teknik_olculer.md` notunda hesaplandı, 7 Eki 2026).
   - Seiko Presage SSA405 (4R38) ve Orient Bambino Open Heart pencereyi tam burada kullanıyor. İkisi de dakika halkasını kesintisiz bırakıyor ve 9 işaretini pencerenin dışına kısaltarak koyuyor (ölçümüm, resmi fotoğraflar, 8 Eki 2026).
   - Bizim küçük kadranımızda Ø10 pencere kadran çapının %37'sini kaplar (Seiko'da yaklaşık %31). Bu yüzden **IX düşmeli**, 8'deki işaret kısalmalı. Pencereyi Ø9 mm açıklık + 0,3 mm çerçeve yapmak daha dengeli olur (§4).
3. **Roma rakamı boyu:** uygulamalı tarz Orient Bambino V2'de yaklaşık 0,16R; uzun/basılı tarz Orient AC0J'de yaklaşık 0,27R (ölçümüm). Bizim R = 13,5 mm için bu **2,2–2,7 mm** (kompakt) ya da **3,2–3,6 mm** (Cartier tarzı ince uzun) demek. Rakamların dış kenarı dakika halkasının iç kenarından yaklaşık 0,05–0,07R (0,7–0,9 mm) içeride durmalı.
4. **İbre boyu:** akrep, rakamların iç kenarına; yelkovan, dakika halkasına uzanır.
   - Breguet 7225 için: "The blue central hour hand aligns with the Roman-numeral-adorned ring, while the minute hand stretches far beyond it to the minute track" ([Fratello, 23 Eki 2025](https://www.fratellowatches.com/introducing-the-breguet-classique-7225-and-7235/)).
   - Ölçümüm: akrep ucu yaklaşık 0,54–0,57R, yelkovan ucu yaklaşık 0,79–0,85R (Bambino V2, SSA405).
   - Ø28,5 kadran için piyasa setleri: Lucius Breguet **8/12/12,75 mm**, Namoki yaprak **9/13/13 mm** ([Lucius](https://luciusatelier.com/products/breguet-hands-polished-blue), [Namoki](https://www.namokimods.com/products/watch-hands-leaf-blue), 8 Eki 2026).
5. **IIII kullanılmalı, IV değil.** Saat kadranlarında IIII + IX alışılmış kullanımdır ([Wikipedia "Roman numerals"](https://en.wikipedia.org/wiki/Roman_numerals), okundu 8 Eki 2026). IIII'ün VIII ile görsel denge kurduğu, 4'lü üç grup oluşturduğu ve kadranın iki yarısında 14'er karakter verdiği söyleniyor ([Fratello, 22 Nis 2022](https://www.fratellowatches.com/watchmakers-four-uncertain-origins/)).
6. **Ucuz görünümün 1 numaralı sebebi kalabalık yazı ve gösterge.**
   - "Empty dials are awesome for dress watches. Full paragraphs are best on Fratello rather than any watch dial." ([Fratello, 31 Eki 2022](https://www.fratellowatches.com/an-ode-to-the-empty-dial/))
   - "Some decoration here, an extra color there, and let's do a cool sunburst too. Legibility is usually the first casualty." ([Fratello, 22 Eyl 2023](https://www.fratellowatches.com/watch-design-what-makes-a-watch-highly-legible/))

   Kural: kadranda tek satır logo olsun. "AUTOMATIC", "WATER RESISTANT", "SWISS MADE" ve sahte marka yazılmamalı.
7. **Lazerle yapılan desene "guilloché" denmemeli.** Monochrome'a göre damgalı (stamped) desenler "lack definition, sharpness and precision". Fark "even more pronounced with laser-engraving techniques" ([Monochrome, 3 May 2024](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials)). Desenin ince, düzenli ve yalnızca bir bölgede olması (merkez) daha iyi sonuç verir.
8. **Dürüstlük tarih boyunca da tasarımın parçası olmuş.** Breguet guilloché'yi ve 1795'teki gizli imzayı kısmen sahtecilere karşı geliştirdi: guilloché "way too ambitious for counterfeiters looking to cash in on his name" ([Fratello, 3 Eki 2025](https://www.fratellowatches.com/who-was-abraham-louis-breguet/)). Sahte saatin "PATEK PHILIPPE / SWISS MADE" yazısı tam bu geleneğin tersidir.

---

## 1. Saygın dress saatlerde Roma rakamı düzeni

### 1.1 Model model gözlemler

| Saat | Hangi saatlerde rakam | Stil, yön | Uygulamalı / basılı | Kaynak (tarih) |
|---|---|---|---|---|
| Breguet Classique 7337 | Roma rakamları, mavi Breguet ibreleri | Saat bölgesi merkezden aşağı kaydırılmış; merkezde Clous de Paris, dışta dairesel barleycorn | Kaynak belirtmiyor | [Fratello, 4 Eki 2022](https://www.fratellowatches.com/breguets-new-classique-7337-calendrier-moonphase/); [Breguet 7337BR/12/9VU](https://www.breguet.com/en/watches/classique/classique-calendrier-7337/7337br129vu) (okundu 8 Eki 2026): "hours chapter is off-centred towards the bottom", rose engine üzerinde el guilloché'si |
| Breguet Classique 7225 | Roma rakamlı saat halkası | Akrep halkaya kadar, yelkovan dakika halkasına kadar uzanıyor | — | [Fratello, 23 Eki 2025](https://www.fratellowatches.com/introducing-the-breguet-classique-7225-and-7235/) |
| Breguet Classique 5177 | Breguet rakamları (Arap rakamı tarzı; siyah emaye platin versiyonda) | "graceful Breguet numerals", "minute track must be one of the most beautiful ones ever" | Grand Feu emaye | [Fratello, 12 Eki 2025](https://www.fratellowatches.com/sunday-morning-showdown-breguet-classique-5177-vs-a-lange-sohne-saxonia-thin-onyx/); [Breguet 5177](https://www.breguet.com/en/watches/classique/classique-5177/5177br2n9v602): 38 mm, 8,8 mm, "Breguet hollow apple" ibreler (okundu 8 Eki 2026) |
| Breguet genel | **Breguet rakamları Roma değil, Arap rakamıdır.** "designed by Abraham-Louis Breguet in 1783 and prized for elegance and legibility" | — | — | [Breguet Classique koleksiyonu](https://www.breguet.com/en/watches/classique) (okundu 8 Eki 2026) |
| Patek Calatrava (2026 güncel seri) | Güncel 18 referansın **hiçbirinde Roma rakamı yok.** 7200R ve 7200/50G'de "applied Breguet numerals", 6119R ve 6196P'de "obus" çubuk, 5227G'de trapez işaret | 7200: "pear-shaped hands"; 6119/6196: "faceted dauphine-style hands" | Uygulamalı altın | [Patek Calatrava tümü](https://www.patek.com/en/collection/calatrava/all-watches); [6119R-001](https://www.patek.com/en/collection/calatrava/6119r-001); [7200R-001](https://www.patek.com/en/collection/calatrava/7200r-001); [6196P-001](https://www.patek.com/en/collection/calatrava/6196p-001) (hepsi okundu 8 Eki 2026) |
| Patek eski Roma rakamlı Calatravalar | Bir okur yorumu: Patek çoğu Roma rakamlı saatinde (3593, 3919) IIII, yalnızca 5035'te IV kullanmış | — | — | [Fratello yorumu, 22 Nis 2022](https://www.fratellowatches.com/watchmakers-four-uncertain-origins/), **düşük güvenilirlik (okur yorumu)** |
| Cartier Tank | Roma rakamları ve "chemin de fer chapter ring" Tank'ın tanımlayıcı özellikleri; "sword-shaped blued steel hands", safir kabaşonlu kurma kolu | "characteristic large, black Roman numerals on a clean white dial" | Basılı (siyah) | [Wikipedia Cartier Tank](https://en.wikipedia.org/wiki/Cartier_Tank); [Fratello, 3 Mar 2022](https://www.fratellowatches.com/why-you-cant-help-but-love-the-cartier-tank/) |
| Cartier Tank Française (2023) | Her saatte rakam | İlk basın numunesinde basılı; üretim versiyonunda "high-polished Roman numerals" ve mavi ibre | Uygulamalı (üretimde) | [Fratello Top 5 Cartier, 26 Oca 2024](https://www.fratellowatches.com/fratellos-top-5-current-cartier-watches-featuring-the-tank-must-tank-louis-cartier-and-the-santos/) |
| Cartier Santos (lake kadran) | "high-polished Roman numerals at each hour"; koyu kadranda bazen "kayboluyorlar" | — | Uygulamalı | Aynı kaynak (26 Oca 2024) |
| FC Classic Heart Beat Manufacture FC-930 (2022) | 11 rakam; VI'nın yerini pencere alıyor | "stylized painted Roman numerals", radyal (alt yarıdakiler ters). Rakamların içinde ikinci bir demiryolu (chemin de fer) halkası var, sunburst merkezi saran (ölçümüm/gözlemim) | Boyalı (basılı) | [Fratello, 29 Ağu 2022](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/); [FC görseli](https://i0.wp.com/www.fratellowatches.com/cdn-cgi/image/anim%3Dfalse/wp-content/uploads/2022/08/Frederique_Constant_FC-930EM3H6_Photo%C2%A9Eric_Rossier_Hero_HD.jpg?w=900&ssl=1) |
| Orient Bambino Version 2 (TAC00009W0, 40,5 mm) | Çift saatlerde Roma (XII, II, IIII, VI, VIII, X), tek saatlerde uygulamalı çubuk; 3'te tarih | **Okunur yön:** üst yarıda tabanı merkeze, alt yarıda tepesi merkeze bakıyor (VI düz okunuyor). **IIII** kullanılıyor | Uygulamalı, cilalı | [Orient USA ürün](https://www.orientwatchusa.com/products/tac00009w0) ve resmi görsel (okundu 8 Eki 2026; açıklama: "Roman Numeral hour markers and and onion-styled crown") |
| Orient RA-AC0J06S30B | Çift saatlerde ince uzun Roma, tek saatlerde ince çubuk | **Tam radyal** (tabanı merkeze bakıyor, alt yarıdaki VI ters). IIII. Eğimli flanşta dakika halkası | Basılı | [Orient USA](https://www.orientwatchusa.com/products/ra-ac0j06s30b) ("bold Roman Numerals and a clean dial"), görsel 8 Eki 2026 |
| Orient Bambino 38 no-date (2026) | "Roman numerals at alternating hours with baton markers in between"; saat işaretlerinin hemen dışında 3 Hz saniye halkası, en dışta ayrı dakika halkası | — | — | [Fratello, 25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/) |
| Longines Master Collection 190th | 12 "beautifully engraved numerals" (Arap rakamı), kumlanmış gümüş kadran, mavi ibre | Gravür | — | [Fratello, 14 Eyl 2022](https://www.fratellowatches.com/longines-master-collection-190th-anniversary/) |
| Longines Master Collection (2026 ABD sayfası) | 24 ürün gösteriliyor; Roma rakamı geçmiyor. Kadranlar "barleycorn" (gümüş, mavi, açık mavi), sunray, sedef | — | — | [longines.com Master Collection](https://www.longines.com/en-us/watches/master/master-collection); [L2.949.4.73.6](https://www.longines.com/en-us/p/watch-the-longines-master-collection-l2-949-4-73-6): "Silver "barleycorn" dial", 39 mm, 2.650 $ (okundu 8 Eki 2026) |

### 1.2 Oranlar (ölçümüm, resmi görseller, 8 Eki 2026)
R = kadranın görünen düz yarıçapı.

| Saat | Rakam yüksekliği | Rakamın radyal aralığı | Dakika halkası | Akrep ucu | Yelkovan ucu |
|---|---|---|---|---|---|
| Orient Bambino V2 (uygulamalı Roma) | ≈0,16R | ≈0,58–0,76R (fotoğraf eğimi yüzünden XII ve VI farklı çıktı: 0,56–0,72 ve 0,64–0,80) | ≈0,83–0,93R (dakika sayıları 05…55 halkanın dışında) | ≈0,54R | ≈0,79R (saniye ≈0,85R) |
| Orient AC0J (basılı, ince uzun) | ≈0,27R | ≈0,67–0,93R | Eğimli flanşta, düz kadranın dışında | — | — |
| Seiko SSA405 (çubuk + açık kalp) | işaretler ≈0,62–0,94R | — | ≈0,88–0,97R | ≈0,57R | ≈0,83R |
| Orient Bambino Open Heart (çubuk) | çubuklar ≈0,55–0,84R | — | ≈0,86–0,90R | — | ≈0,85R |

- Görseller:
  - [Bambino V2](https://cdn.shopify.com/s/files/1/0026/4978/4385/files/orient-bambino-version-2-2838279.png?v=1787002575)
  - [AC0J](https://cdn.shopify.com/s/files/1/0026/4978/4385/files/ra-ac0j06s30b-7823021.png?v=1787002216)
  - [SSA405J1](https://www.seikowatches.com/tr-tr/-/media/Images/Product--Image/All/Seiko/2022/02/20/03/15/SSA405J1/SSA405J1.png)
  - [Bambino Open Heart](https://cdn.shopify.com/s/files/1/0026/4978/4385/files/orient-bambino-open-heart-4213292.png?v=1787002576)
- **Çıkarım (benim):**
  - İbre uçları hedefe değmez, hedefin 0,03–0,05R kadar içinde durur. R = 13,5 mm'de bu 0,4–0,7 mm eder.
  - Rakamlar dakika halkasından en az yaklaşık 0,05R (≈0,7 mm) uzak durur.

### 1.3 Yön kuralları
- **Tam radyal** (her rakamın tabanı merkeze bakar, alt yarıdakiler ters okunur). Klasik saat kulesi ve Cartier geleneği. Orient AC0J ve FC-930'da görülüyor (gözlemim).
- **Okunur radyal** (alt yarıdakiler 180° çevrilmiş, VI düz okunur). Orient Bambino V2'de görülüyor (gözlemim). ozgur'un mevcut `roma_rakami()` fonksiyonu bu yöntemi kullanıyor (`tasarim/kadran/kadran.py`).
- **Dik** (bütün rakamlar ekran yatayına göre dik). Fotoğraftaki sahte saatte XII, III ve IX böyle (kullanıcının fotoğrafı).
- **Öneri:** sadece XII-III-VI-IX kullanılırsa okunur radyal ile dik aynı sonucu verir. 12 rakam kullanılırsa tam radyal daha "klasik" durur.

### 1.4 IIII mi IV mü
- "Modern clock faces that use Roman numerals still very often use IIII for four o'clock but IX for nine o'clock". Gelenek Wells Katedrali saatine (14. yy sonu) kadar gidiyor. Ama "this is far from universal": Elizabeth Tower IV kullanıyor ([Wikipedia "Roman numerals"](https://en.wikipedia.org/wiki/Roman_numerals), 8 Eki 2026).
- FHH'nin gerekçeleri: IIII, VIII ile dengeli duruyor, dört karakterli üç grup oluşturuyor (I–IIII, V–VIII, IX–XII), kadranın iki yarısında 14'er karakter veriyor ([Fratello, 22 Nis 2022](https://www.fratellowatches.com/watchmakers-four-uncertain-origins/)).

---

## 2. Dakika halkaları ve saat işaretleri

- **Demiryolu (chemin de fer)** halkası, iki ince çember ve aralarındaki 60 çentikten oluşur.
  - Cartier Tank'ın tanımlayıcı özelliğidir ([Wikipedia](https://en.wikipedia.org/wiki/Cartier_Tank)).
  - Rolex 1908 için: "The railroad minute track and the combination of fonts used for the dial work really well" ([Fratello, 7 Oca 2024](https://www.fratellowatches.com/sunday-morning-showdown-rolex-perpetual-1908-vs-breguet-classique-5157/)).
  - Tank Must'ta da "rectangular minuterié and the Roman numerals" var ([Fratello, 29 May 2021](https://www.fratellowatches.com/a-closer-look-at-the-new-cartier-tank-must/)).
- **Breguet 5177'nin dakika halkası** "must be one of the most beautiful ones ever"; bir okur da "hands, fonts and minute track have much more personality" diyor ([Fratello, 12 Eki 2025](https://www.fratellowatches.com/sunday-morning-showdown-breguet-classique-5177-vs-a-lange-sohne-saxonia-thin-onyx/)).
- **Halkayı kesme.** VPC'nin tasarım günlüğünde "determined not to let it break up the minute or seconds tracks… Breaking up the minute or seconds track makes no sense" deniyor ([Fratello, 19 Nis 2023](https://www.fratellowatches.com/building-a-watch-brand-episode-7-dial-design/)). Seiko SSA405 ve Bambino Open Heart da açık kalbin yanında halkayı kesintisiz bırakıyor (gözlemim). FC-930 ise iç demiryolu halkasını pencereyle kesiyor ama dış halkayı koruyor (gözlemim).
- **İki halka (saniye + dakika).** Bambino 38: "The two scales add visual interest, even if one could easily do the job alone" ([Fratello, 25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)). Küçük Ø27 kadranda tek halka yeterli. Bu benim önerim.
- **İşaret biçimleri:**
  - Patek "obus" çubuklar ve trapez işaretler ([6119R](https://www.patek.com/en/collection/calatrava/6119r-001), [5227G](https://www.patek.com/en/collection/calatrava/5227g-010)).
  - Bambino 38 LE'de "hour markers almost look like fir needles" ([Fratello, 16 Ara 2023](https://www.fratellowatches.com/hands-on-with-the-orient-bambino-38-in-four-delicious-limited-edition-colors/)).
  - Rolex 1908'de alt kadran "visually rests on the cut-off indices at 5 and 7 o'clock" ([Fratello, 7 Oca 2024](https://www.fratellowatches.com/sunday-morning-showdown-rolex-perpetual-1908-vs-breguet-classique-5157/)). Bu, bir pencerenin işaretleri nasıl kesebileceğine iyi bir örnek.

---

## 3. Guilloché desenleri ve bölgeleme

### 3.1 Tanımlar
- **Düz hat makinesi (straight-line engine):** "carves fine grooves into a metal surface in repetitive geometric patterns". Çizgiler istenen açıyla kesişebilir, Clous de Paris böyle elde edilir.
- **Rose engine:** "can produce curved lines", rozet adlı kamlarla ([Patek – Guillochage](https://www.patek.com/en/manufacture/artisans-of-time/guillochage), okundu 8 Eki 2026).
- **Desen adları:** "hobnail (clous de Paris) and pavé de Paris, sunburst, barleycorn or grain d'orge, waves and checkerboard". Flinqué'nin diğer adı "waves" ([Monochrome, 3 May 2024](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials)).
- **Breguet'nin gerekçesi:** guilloché'yi "to counter the effect of light rays on smooth surfaces and thus improve legibility" uygulamış ([Breguet – Craftsmanship](https://www.breguet.com/en/craftsmanship), okundu 8 Eki 2026). İlk guilloché kadranlı Breguet cep saati 1786 tarihli. Desen tozu gizliyor ve ışığı daha yumuşak yansıtıyor ([Fratello, 3 Eki 2025](https://www.fratellowatches.com/who-was-abraham-louis-breguet/)).
- **Breguet hands:** 1783 ([Wikipedia A.-L. Breguet](https://en.wikipedia.org/wiki/Abraham-Louis_Breguet), [Wikipedia Breguet (brand)](https://en.wikipedia.org/wiki/Breguet_(brand)), okundu 8 Eki 2026). Markanın imzası: "coin-edge cases, guilloché dials and blue pomme hands".

### 3.2 Bölgeleme örnekleri
| Saat | Merkez | Saat halkası / dış | Kaynak |
|---|---|---|---|
| Breguet 7337 | Clous de Paris (dışarı kaydırılmış saat bölgesi) | Dairesel barleycorn | [Fratello, 4 Eki 2022](https://www.fratellowatches.com/breguets-new-classique-7337-calendrier-moonphase/); [Monochrome, 2024](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials) |
| Breguet 7225 | "Quai de l'Horloge" el guilloché'si | Dairesel fırçalı, gravürlü ve mavi skalalı alt kadran halkaları kontrast sağlıyor | [Fratello, 23 Eki 2025](https://www.fratellowatches.com/introducing-the-breguet-classique-7225-and-7235/) |
| Breguet 7235 | Desen alt göstergelerde ölçek ve düzen değiştiriyor ("to help provide contrast") | Ayrıntılı chapter ring | Aynı kaynak |
| FC Classic Heart Beat FC-930 | Sunburst | Beyaz lake, boyalı Roma rakamları | [Fratello, 29 Ağu 2022](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/) |
| FC Art Déco Carrée (bayan) | Gümüş guilloché merkez | Beyaz sedef çevre, siyah basılı Roma rakamları | Aynı kaynak. Yazar bu formülün (dikdörtgen + Roma + guilloché merkez + mavi kabaşon) "a very, very iconic watch design"a (Cartier) fazla yaklaştığını ve FC'yi ayıran şeyin kendi lug, kurma kolu ve kasa detayları olduğunu yazıyor |
| Patek 4997/200G | Kadran plakası "first embossed with a concentric wave motif" ve üstüne onlarca kat şeffaf lake | — | [Patek 4997/200G-001](https://www.patek.com/en/collection/calatrava/4997-200g-001) (okundu 8 Eki 2026). **Not:** Patek de baskı/kabartma desen kullanıyor; dürüst sunulursa sorun değil |
| Patek 6119R | "Silvery grained" kadran; Clous de Paris **kasa çerçevesinde**, kadranda değil | — | [Patek 6119R-001](https://www.patek.com/en/collection/calatrava/6119r-001) ("guilloched hobnail-pattern bezel") |
| Patek 7130G World Time | "guilloché work at the center of its opaline dial" | — | [Patek – Guillochage](https://www.patek.com/en/manufacture/artisans-of-time/guillochage) |
| Seiko Presage Sharp Edged | Asanoha (kenevir yaprağı) deseni bütün kadranda | — | [Fratello, 27 Kas 2022](https://www.fratellowatches.com/a-closer-look-at-the-seiko-presage-sharp-edged-series-spb305-and-spb311/). Bir okur: "that particular pattern looks a little heavy for the dial" |
| Louis Erard Excellence Petite Seconde | Flinqué + basketweave, **damgalı** | — | [Monochrome, 3 May 2024](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials) |
| Cartier Pasha Chronograph | Gümüş flinqué kadran, mavi ibreler | — | [Fratello, 16 Mar 2022](https://www.fratellowatches.com/best-cartier-watches/) |

- Monochrome'a göre desenler "can be used to delineate different subdials or to highlight specific indicators" ([Monochrome, 2024](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials)).
- **Endüstriyel yöntemler:**
  - CNC "great precision and repeatability".
  - Damgalı kadranlar "tend to lack definition, sharpness and precision, with textures that appear less crisp, without the same depth or volume".
  - El işçiliğiyle fark "even more pronounced with laser-engraving techniques".
  - "If the dial is too perfect or too regular" CNC olabilir (Monochrome, 2024).
- Uzun, basit çizgiler küçük ve narin desenlerden "far more unforgiving". En ufak sapmayı gösteriyor ([Fratello Louis Erard, 2 Mar 2022](https://www.fratellowatches.com/louis-erard-excellence-guilloche-main-ii/)). Lazerde ise sapma yok. Bu yüzden **uzun ve sade eş merkezli/dalgalı çizgiler lazer için avantajlı** (benim çıkarımım).

---

## 4. Açık kalp (open-heart) penceresi

### 4.1 Gözlemler
| Saat | Konum | Boyut (ölçümüm) | Çerçeve | Düşürülen işaret | Kaynak |
|---|---|---|---|---|---|
| Seiko Presage SSA405J1 (4R38 ≈ NH38), 40,5 mm | 9'da, eksenin biraz altında | Çerçeve dahil çap ≈0,61R (kadran çapının ≈%31'i). Merkez ≈0,39R'de. TMI'deki 6,85 mm ölçek alınırsa pencere ≈10,8 mm, görünen kadran ≈35 mm | İnce cilalı halka | Hiçbiri. 9 işareti pencerenin hemen dışında başlıyor, dakika halkası kesintisiz | [Seiko TR SSA405J1](https://www.seikowatches.com/tr-tr/products/presage/ssa405j1) (4R38, 40,5 mm, 35.495 TL, okundu 8 Eki 2026) ve resmi görsel |
| Orient Bambino Open Heart RA-AG0002S30B, 40,5 mm | 9'da | Pencere ≈ kadran çapının %26–29'u, merkez ≈0,45–0,47R | Cilalı eğimli halka | 9 işareti kısaltılmış, dakika halkası kesintisiz | [Orient USA](https://www.orientwatchusa.com/products/ra-ag0002s30b) (295 $ indirimli, 455 $ liste, okundu 8 Eki 2026) ve görsel |
| Seiko Presage SPB311 / SPB415 | 9'da; "the aperture at 9 o'clock, exhibiting the oscillating balance wheel as well as the moving escapement" | — | SPB415'te pencereye kenevir yaprağı deseni eklenmiş: "The 6R calibers aren't the last word in fine finishing, and open hearts always looked a bit coarse as a result. This nicely detailed decoration makes it look significantly more refined." | — | [Fratello, 27 Kas 2022](https://www.fratellowatches.com/a-closer-look-at-the-seiko-presage-sharp-edged-series-spb305-and-spb311/); [Fratello, 27 Nis 2023](https://www.fratellowatches.com/introducing-the-new-seiko-presage-sharp-edged-series-spb415-spb417/) |
| FC Classic Heart Beat FC-930 (kendi kalibresi), 39 mm | 6'da | Büyük, yuvarlak (≈ kadran çapının %40'ı, perspektifli fotoğraf, kaba ölçüm) | Kalın cilalı çerçeve | VI düşürülmüş; iç demiryolu halkası kesilmiş | [Fratello, 29 Ağu 2022](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/): "The previous comma-shaped aperture is now perfectly round" |
| Sahte "Patek" (fotoğraf) | 6'da, "tourbillon" görünümlü | — | — | — | Kullanıcı fotoğrafı. Bkz. `ekonomi_ve_sahtecilik.md` |

- **"Tourbillon deliği" yorgunluğu:** "The hole in the dial at 6 o'clock once made people crazy… These holes are everywhere now, and nobody wants to look inside." ([Fratello, 31 Tem 2025](https://www.fratellowatches.com/dream-about-a-tourbillon-watch/)). Saat 6'da sahte "tourbillon" penceresi ucuzluk işaretidir. NH38'in dürüst 9 konumu daha iyi bir hikâye anlatır: "kalp atışı".

### 4.2 Bizim kadran için hesap (benim hesabım; geometri TMI NH38'den)
- **Konum:** pencere merkezi r = 6,85 mm, açı 265,3°. Ø10 açıklık radyal olarak r = 1,85 ile 11,85 mm arasını kaplıyor. Kenarı merkez deliğine yaklaşık 0,82 mm kalıyor ([`teknik_olculer.md`](../5000%20TL%20altı%20özel%20saat%20yapımı/teknik_olculer.md); [TMI NH38_SS](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf)).
- **Oran:** R = 13,5 için pencere çapı 0,74R ve merkez 0,51R. Seiko'da bu değerler 0,61R ve 0,39R. Yani bizim kadranda pencere **orantısal olarak yaklaşık %20–30 daha baskın**.
- **Bloklanan radyal aralıklar** (pencere + çerçeve + 0,2 mm boşluk):

| Açıklık + çerçeve | Saat 8 (240°) | Saat 9 (270°) | Saat 10 (300°) |
|---|---|---|---|
| Ø10 + 0 | 1,9–10,49 mm | 1,66–11,99 | 2,2–9,07 |
| Ø10 + 0,3 | 1,54–10,84 | 1,36–12,29 | 1,76–9,51 |
| Ø9 + 0,3 | 2,14–10,24 | 1,86–11,79 | 2,51–8,76 |
| Ø8 + 0,3 | 2,78–9,61 | 2,37–11,29 | 3,39–7,87 |

- **Sonuçlar:**
  - **IX hiçbir seçenekte sığmaz.** Saat 9'da 11,3–12,3 mm'ye kadar alan dolu.
  - Mevcut `stil_roma` yaprak işaretleri r = 10,10'da başlıyor. Ø10 + 0,3 çerçeveyle **8'deki işaret pencereye çarpar**; r ≥ 10,85'ten başlamalı. 10'daki işaret sorun değil.
  - Ø9 + 0,3 çerçeveyle 8'deki işaret r ≥ 10,25'te başlarsa sığar.
  - Dakika halkası (12,65–13,13) her durumda kesintisiz kalabilir.

---

## 5. Roma kadranına uyan ibreler

- **Breguet (pomme):** "These time-telling ballerinas will make the finest sword hands look like sumo wrestlers." Classique 5157'de halkalar "crescent-shaped and impossibly thin at the top", ideal olarak ısıl mavileştirilmiş ([Fratello Part One, 1 Eki 2022](https://www.fratellowatches.com/styles-of-watch-hands-and-who-does-them-best-part-one/)). Breguet 7337: mavi Breguet ibreleri + Roma rakamları ([Fratello, 4 Eki 2022](https://www.fratellowatches.com/breguets-new-classique-7337-calendrier-moonphase/)).
- **Yaprak (feuille):** "elegantly minimalist, but their soft, sleek shapes will easily show any imperfections in the craftsmanship… lend a dial an air of soft formality" (aynı kaynak). **Ucuz yan sanayi ibrede kusur gösterme riski var.** Benim çıkarımım: cilası iyi bir set seçilmeli.
- **Dauphine:** Grand Seiko'da "flat tops come to a perfect point". Patek 6119/6196/5227'de "faceted dauphine-style hands" ([Patek ürün sayfaları](https://www.patek.com/en/collection/calatrava/6119r-001), 8 Eki 2026). Bambino 40.5'te "sharp dauphine hands" ([Fratello, 25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)).
- **Kılıç (sword), mavi:** Cartier Tank Solo'da "delicate, sharp, and beautifully colored. The tint of heat-blued hands will add an extra dimension to any dial, and on a crisp silvery-white Cartier dial, they are just right." ([Fratello Part Two, 8 Eki 2022](https://www.fratellowatches.com/styles-of-watch-hands-and-who-does-them-best-part-two-from-mercedes-to-sword-with-rolex-cartier-kikuchi-nakagawa-and-more/)).
- **Spade ve Assegai:** Kikuchi Nakagawa Murakumo'nun spade ibreleri; Laurent Ferrier'in Assegai'leri "feuille hands but taken to their sleek extremes" (aynı kaynak).
- **Armut (pear-shaped):** Patek 7200'de Breguet rakamlarıyla birlikte ([7200R-001](https://www.patek.com/en/collection/calatrava/7200r-001)).
- **Okunurluk:** "if the watch has a silvered dial, I will want to see blued hands" (okur yorumu, [Fratello, 2 Kas 2023](https://www.fratellowatches.com/watch-features-i-appreciate-details-more-brands-should-get-right/)). Bambino 38 ivory: "blue-coated hands and silver markers feels effortlessly classic" ([Fratello, 25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)).
- **Kısa ibre bir kusurdur:** ilk nesil 39 mm Rolex Explorer için "most people either feel the handset is optically too short" ([Fratello, 4 Ağu 2023](https://www.fratellowatches.com/is-there-objective-beauty-in-watches/)).
- **Ø28,5 kadran için set boyları:**
  - Lucius Breguet: 8 / 12 / 12,75 mm, pinyonlar 1,50 / 0,88 / 0,198, NH35/NH38/NH39 uyumlu, S$47 ([Lucius](https://luciusatelier.com/products/breguet-hands-polished-blue), 8 Eki 2026; mavinin ısıl mı boya mı olduğu belirtilmemiş).
  - Namoki yaprak mavi: 9 / 13 / 13 mm, S$29, backorder ([Namoki](https://www.namokimods.com/products/watch-hands-leaf-blue), 8 Eki 2026).
  - Fiyat ve yurt içi bulunabilirlik için bkz. `roma_parcalari.md`: klasik ibreler yurt içinde bulunamadı.
- **Hesap (benim):** R = 13,5'te 8 mm akrep 0,59R'ye, 12 mm yelkovan 0,89R'ye denk geliyor. 9 mm akrep 0,67R'ye, 13 mm yelkovan 0,96R'ye. Bu yüzden:
  - **9/13 set:** rakam iç kenarı yaklaşık 9,3–9,5 mm, dakika halkası 12,65–13,13 mm. Mevcut `stil_roma` (rakam merkezi r = 10,70, boy 2,6 → yaklaşık 9,4–12,0) ile birebir uyumlu.
  - **8/12 set:** rakam iç kenarı yaklaşık 8,4–8,6 mm, dakika halkası 12,2–12,7 mm olmalı.

---

## 6. Ucuz homage/sahte saati ucuz gösteren şeyler ve kaçınma kuralları

| Ucuzluk işareti | Kanıt | ozgur kuralı |
|---|---|---|
| Sahte marka ya da menşe yazısı ("PATEK PHILIPPE", "SWISS MADE") | Breguet guilloché ve gizli imzayı sahtecilere karşı kullanmıştı ([Fratello, 3 Eki 2025](https://www.fratellowatches.com/who-was-abraham-louis-breguet/)). Hukuki yönü için `ekonomi_ve_sahtecilik.md` | Yalnızca "ozgur" (ya da OZGUR) yazılmalı. Menşe kadrana yazılacaksa doğru olmalı; arka kapakta daha iyi |
| Kalabalık yazı | "If you look at watches from the 1930s–1970s, there was a maximum of two lines of text on most… Empty dials are awesome for dress watches" ([Fratello, 31 Eki 2022](https://www.fratellowatches.com/an-ode-to-the-empty-dial/)). Bambino'nun "Water Resistant" yazısı iki ayrı yazıda eleştirilmiş ([16 Ara 2023](https://www.fratellowatches.com/hands-on-with-the-orient-bambino-38-in-four-delicious-limited-edition-colors/), [25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)) | 12'nin altında tek satır logo, 6'da yazı yok. "AUTOMATIC", "21 JEWELS" ya da "WATER RESISTANT" yazılmamalı |
| Çok doku, çok renk, çok parlaklık | "sunburst vignette dials, shiny materials everywhere, too many colors and textures stacked on top of each other" ([Fratello, 17 Oca 2024](https://www.fratellowatches.com/has-watch-design-gone-from-pizza-margherita-to-hawaiian-deep-dish-with-stuffed-double-crust/)). Örnek alınan Breguet 5157 ise "a pizza with two perfectly chosen toppings": guilloché kadran + coin-edge kasa (aynı kaynak) | En fazla **iki doku**: merkez desen + düz/saten saat halkası. İki metal rengi (ör. gümüş + mavi ibre) yeterli |
| Görsel hiyerarşi yok | "The eye should go to the most important stuff first and only notice secondary functions and decorations afterward" ([Fratello, 22 Eyl 2023](https://www.fratellowatches.com/watch-design-what-makes-a-watch-highly-legible/)) | Önce ibreler (en koyu, en kontrastlı), sonra rakamlar, en son desen (en düşük kontrast, ton-ton) |
| Sahte ya da gereksiz göstergeler (çift tarih, sahte "tourbillon") | Sahte saatte hem 12'de büyük tarih hem 3'te ibreli tarih var. Biri süs olabilir (`ekonomi_ve_sahtecilik.md` §3). "Tourbillon" delikleri "everywhere now" ([Fratello, 31 Tem 2025](https://www.fratellowatches.com/dream-about-a-tourbillon-watch/)) | Kadranda yalnızca mekanizmanın gerçekten yaptığı şey olmalı: NH38'de saat, dakika, saniye ve balans. Alt kadran yok |
| Tarih penceresi kadranı bozuyor | "Often, a date display kind of ruins a good dress watch" ([Fratello Longines, 14 Eyl 2022](https://www.fratellowatches.com/longines-master-collection-190th-anniversary/)). 5177'nin 3'teki penceresi "isn't the best date window" ([Fratello, 12 Eki 2025](https://www.fratellowatches.com/sunday-morning-showdown-breguet-classique-5177-vs-a-lange-sohne-saxonia-thin-onyx/)). Bambino LE'de "the date wheel doesn't match the dial color" ([16 Ara 2023](https://www.fratellowatches.com/hands-on-with-the-orient-bambino-38-in-four-delicious-limited-edition-colors/)) | NH38A (tarihsiz). NH35A kullanılırsa tarih penceresi çerçevesiz ve rakam boyunda olmalı, beyaz tarih diski seçilmeli |
| Dakika halkasını yazıyla ya da pencereyle kırmak | VPC: "determined not to let it break up the minute or seconds tracks" ([Fratello, 19 Nis 2023](https://www.fratellowatches.com/building-a-watch-brand-episode-7-dial-design/)) | Açık kalp pencere r ≤ 12,3'te bitmeli, halka 12,65'ten başlamalı |
| Kısa ibre | Explorer 39 örneği ([Fratello, 4 Ağu 2023](https://www.fratellowatches.com/is-there-objective-beauty-in-watches/)) | Akrep rakam iç kenarına, yelkovan halkaya ulaşmalı (§5) |
| Damgalı desenin yumuşak, net olmayan kenarları | Monochrome 2024 (yukarıda) | Desen çizgileri ince ve eşit aralıklı olmalı. Lazer veya PCB'nin keskinliği bir avantaj olarak kullanılmalı. "Hand guilloché" denmemeli |
| Fazla yazı tipi | Rolex 1908'de bilinçli iki font eşleşmesi beğeniliyor ([Fratello, 7 Oca 2024](https://www.fratellowatches.com/sunday-morning-showdown-rolex-perpetual-1908-vs-breguet-classique-5157/)) | En fazla iki aile; tercihen rakam ve logo için tek serif aile (mevcut: Cinzel) |
| Ünlü bir tasarıma fazla yaklaşmak | FC'nin Art Déco Carrée'si için "creeping perilously close to a very, very iconic watch design" ([Fratello, 29 Ağu 2022](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/)) | Patek veya Breguet'ye özgü işaretler (Calatrava haçı, "secret signature", Breguet adı) kullanılmamalı. Kendi işaretimiz olsun, ör. yaprak işaret |
| Dress saat için büyük kasa | Bambino 40.5 için okur: "always too large for a dressy design like this" ([Fratello, 25 Tem 2026](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)). Breguet Souscription "rather portly 40mm" ([Fratello, 14 Kas 2025](https://www.fratellowatches.com/fratello-dress-watch-season-semifinal-2-patek-philippe-calatrava-6196p-vs-breguet-classique-souscription-2025/)) | 38–39 mm kasa (28,5 mm kadranla uyumlu; bkz. `roma_parcalari.md`) |

---

## 7. ozgur Roma kadranı için somut ölçü önerisi (benim sentezim, yukarıdaki oranlardan)

Kadran Ø28,5 mm, görünen alan Ø27 (R = 13,5). Ölçüler merkezden yarıçap olarak, mm cinsinden.

| Öğe | Öneri | Gerekçe |
|---|---|---|
| Dakika halkası (demiryolu) | İki çember 12,65 ve 13,13 (çizgi 0,12–0,16); 60 çentik 0,15; 5 dakikalar 0,25–0,30 ya da nokta | Mevcut `stil_roma` ile aynı. Halka yaklaşık 0,94–0,97R'de, Seiko'nun 0,88–0,97R'sine yakın |
| Saat halkası (rakam bölgesi) | 9,2–12,3 arası **desensiz** (düz ya da saten) | FC-930 ve Breguet bölgelemesi |
| Ayırıcı çember | r ≈ 9,1'de 0,10–0,12 mm tek çizgi | Doku sınırını netleştirir |
| Roma rakamları | Kompakt: yükseklik 2,3–2,6 (0,17–0,19R), merkez r ≈ 10,7. Ya da Cartier tarzı: 3,2–3,5 (0,24–0,26R), dar font. **IIII**. Seçenekler: (a) yalnız XII-III-VI(-IX yok) + yaprak işaretler, (b) çift saatler (XII, II, IIII, VI, VIII, X) + yaprak işaretler (Bambino düzeni) | Bambino V2 0,16R, AC0J 0,27R |
| Yaprak işaretler | r 10,1–12,25, en geniş 0,7–0,8. **8'deki işaret** Ø10 pencereyle r ≥ 10,85'ten, Ø9 pencereyle r ≥ 10,25'ten başlamalı | §4.2 hesabı |
| Açık kalp (NH38A) | Ø9,0 açıklık + 0,3 mm çerçeve halkası (cilalı/altın renkli bakır ya da beyaz çizgi). IX yok. Halka kesintisiz | Seiko/Orient pratiği. Küçük kadranda baskınlığı azaltır |
| Merkez desen | r 1,6–9,0 arası eş merkezli ince dalga ya da Clous de Paris; çizgi 0,12–0,16, adım 0,30–0,35; düşük kontrast (ton-ton) | Breguet 7337 / Patek 4997 mantığı. Malzeme sınırları için bkz. `beyaz_kadran_malzemeleri.md` |
| Logo | 12 altında, r ≈ 5,3, yükseklik 1,2–1,4, tek satır. Başka yazı yok | Fratello "empty dial" |
| İbreler | Mavi Breguet ya da yaprak. 9/13/13 set bu düzene uyar. 8/12 set kullanılırsa rakamlar yaklaşık 0,8 mm içeri alınmalı | §5 |

---

## Kaynakça (hepsi 8 Ekim 2026'da okundu; yayın tarihleri parantez içinde)

**Fratello:**
- [Who Was A.-L. Breguet (2025-10-03)](https://www.fratellowatches.com/who-was-abraham-louis-breguet/)
- [Breguet 5177 vs Saxonia (2025-10-12)](https://www.fratellowatches.com/sunday-morning-showdown-breguet-classique-5177-vs-a-lange-sohne-saxonia-thin-onyx/)
- [Breguet 7225/7235 (2025-10-23)](https://www.fratellowatches.com/introducing-the-breguet-classique-7225-and-7235/)
- [Breguet 7337 (2022-10-04)](https://www.fratellowatches.com/breguets-new-classique-7337-calendrier-moonphase/)
- [6196P vs Souscription (2025-11-14)](https://www.fratellowatches.com/fratello-dress-watch-season-semifinal-2-patek-philippe-calatrava-6196p-vs-breguet-classique-souscription-2025/)
- [Calatrava (2025-11-03)](https://www.fratellowatches.com/why-every-watch-collector-needs-a-calatrava/)
- [Bambino no-date (2026-07-25)](https://www.fratellowatches.com/orient-expands-the-bambino-range-including-no-date-38mm-options/)
- [Bambino LE (2023-12-16)](https://www.fratellowatches.com/hands-on-with-the-orient-bambino-38-in-four-delicious-limited-edition-colors/)
- [Hands 1 (2022-10-01)](https://www.fratellowatches.com/styles-of-watch-hands-and-who-does-them-best-part-one/)
- [Hands 2 (2022-10-08)](https://www.fratellowatches.com/styles-of-watch-hands-and-who-does-them-best-part-two-from-mercedes-to-sword-with-rolex-cartier-kikuchi-nakagawa-and-more/)
- [IIII (2022-04-22)](https://www.fratellowatches.com/watchmakers-four-uncertain-origins/)
- [Tank love (2022-03-03)](https://www.fratellowatches.com/why-you-cant-help-but-love-the-cartier-tank/)
- [Tank LC (2022-04-12)](https://www.fratellowatches.com/the-new-cartier-tank-louis-cartier-a-truly-iconic-wristwatch-at-its-purest-and-best/)
- [Top 5 Cartier (2024-01-26)](https://www.fratellowatches.com/fratellos-top-5-current-cartier-watches-featuring-the-tank-must-tank-louis-cartier-and-the-santos/)
- [Tank Must (2021-05-29)](https://www.fratellowatches.com/a-closer-look-at-the-new-cartier-tank-must/)
- [Best Cartier (2022-03-16)](https://www.fratellowatches.com/best-cartier-watches/)
- [Longines 190th (2022-09-14)](https://www.fratellowatches.com/longines-master-collection-190th-anniversary/)
- [SPB305/311 (2022-11-27)](https://www.fratellowatches.com/a-closer-look-at-the-seiko-presage-sharp-edged-series-spb305-and-spb311/)
- [SPB415/417 (2023-04-27)](https://www.fratellowatches.com/introducing-the-new-seiko-presage-sharp-edged-series-spb415-spb417/)
- [FC GWD 2022 (2022-08-29)](https://www.fratellowatches.com/frederique-constant-geneva-watch-days-releases/)
- [Empty dial (2022-10-31)](https://www.fratellowatches.com/an-ode-to-the-empty-dial/)
- [Legibility (2023-09-22)](https://www.fratellowatches.com/watch-design-what-makes-a-watch-highly-legible/)
- [Pizza (2024-01-17)](https://www.fratellowatches.com/has-watch-design-gone-from-pizza-margherita-to-hawaiian-deep-dish-with-stuffed-double-crust/)
- [Features (2023-11-02)](https://www.fratellowatches.com/watch-features-i-appreciate-details-more-brands-should-get-right/)
- [Objective beauty (2023-08-04)](https://www.fratellowatches.com/is-there-objective-beauty-in-watches/)
- [Dial design ep.7 (2023-04-19)](https://www.fratellowatches.com/building-a-watch-brand-episode-7-dial-design/)
- [Tourbillon (2025-07-31)](https://www.fratellowatches.com/dream-about-a-tourbillon-watch/)
- [Louis Erard (2022-03-02)](https://www.fratellowatches.com/louis-erard-excellence-guilloche-main-ii/)
- [1908 vs 5157 (2024-01-07)](https://www.fratellowatches.com/sunday-morning-showdown-rolex-perpetual-1908-vs-breguet-classique-5157/)

**Diğer kaynaklar:**
- **Monochrome:** [guilloché technical perspective, Xavier Markl (2024-05-03)](https://monochrome-watches.com/technical-perspective-the-art-of-guilloche-dials-examples-of-guilloche-patterns-comparison-stamped-cnc-dials)
- **Patek:** [Guillochage](https://www.patek.com/en/manufacture/artisans-of-time/guillochage), [Calatrava tümü](https://www.patek.com/en/collection/calatrava/all-watches), 6119R-001, 6196P-001, 7200R-001, 7200/50G-001, 4997/200G-001, 5227G-010, 5088/100P-001 ürün sayfaları
- **Breguet:** [Classique](https://www.breguet.com/en/watches/classique), [5177BR/2N](https://www.breguet.com/en/watches/classique/classique-5177/5177br2n9v602), [5177BB/29](https://www.breguet.com/en/watches/classique/classique-5177/5177bb299v6), [5177BB/2Y](https://www.breguet.com/en/watches/classique/classique-5177/5177bb2y9v6), [7337](https://www.breguet.com/en/watches/classique/classique-calendrier-7337/7337br129vu), [Craftsmanship](https://www.breguet.com/en/craftsmanship)
- **Orient:** [TAC00009W0](https://www.orientwatchusa.com/products/tac00009w0), [RA-AC0J06S30B](https://www.orientwatchusa.com/products/ra-ac0j06s30b), [RA-AG0002S30B](https://www.orientwatchusa.com/products/ra-ag0002s30b), [UK RA-AC0031S](https://www.orientwatch.co.uk/or/en_GB/brands/orient/orient-bambino-40-5mm/p/RA-AC0031S) (£294,99, "tasteful roman numerals")
- **Seiko:** [SSA405J1](https://www.seikowatches.com/tr-tr/products/presage/ssa405j1), [SSA343J1](https://www.seikowatches.com/tr-tr/products/presage/ssa343j1) (4R57, 40.195 TL), [SSA441J1](https://www.seikowatches.com/tr-tr/products/presage/ssa441j1) (4R38, 35.495 TL)
- **Longines:** [Master Collection](https://www.longines.com/en-us/watches/master/master-collection), [L2.949.4.73.6](https://www.longines.com/en-us/p/watch-the-longines-master-collection-l2-949-4-73-6)
- **İbre setleri:** [Lucius Breguet](https://luciusatelier.com/products/breguet-hands-polished-blue), [Namoki Leaf](https://www.namokimods.com/products/watch-hands-leaf-blue)
- **Wikipedia:** [Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals), [Clock face](https://en.wikipedia.org/wiki/Clock_face), [Cartier Tank](https://en.wikipedia.org/wiki/Cartier_Tank), [Breguet (brand)](https://en.wikipedia.org/wiki/Breguet_(brand)), [A.-L. Breguet](https://en.wikipedia.org/wiki/Abraham-Louis_Breguet), [Guilloché](https://en.wikipedia.org/wiki/Guilloch%C3%A9)
- **TMI:** [NH38_SS](https://timemodule.com/upload/category/27/spec_sheet/NH38_SS.pdf) (kardeş not üzerinden)

## Boşluklar
- WebSearch kotası doluydu. Hodinkee, WatchUSeek ve aBlogtoWatch'ın Roma kadranı incelemeleri okunamadı.
- Cartier ve Frederique Constant'ın resmi sayfaları 403 verdi.
- Cartier Tank'ın rakam yönü, "gizli imza" konumu ve IIII kullanımı **doğrulanmadı**.
- Patek'in güncel Calatrava serisinde Roma rakamlı model yok. Eski 3919/5119 bilgisi yalnızca okur yorumuna dayanıyor.
- Breguet'nin resmi sayfaları rakam tipini (Roma veya Breguet) belirtmiyor. 5177'nin beyaz emaye versiyonunun Roma rakamlı olup olmadığı doğrulanmadı.
- Longines Master Collection'ın Roma rakamlı güncel bir referansı bulunamadı (gösterilen 24/101 ürün).
- Oranlar resmi fotoğraflardan yaptığım ölçümler (±%5). Rakam yükseklikleri için marka verisi yok.
- NH38 balans çarkının gerçek çapı bulunamadı. Ø9 pencerenin balansı tam gösterip göstermediği numune üzerinde kontrol edilmeli.
