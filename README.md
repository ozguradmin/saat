# ozgur — kendi kadranlı otomatik kol saati

NH38A (ya da NH35A) mekanizmalı, kadranını kendimiz tasarladığımız bir kol saati projesi.
Mekanizma, kasa, ibreler ve kordon Türkiye'den hazır alınıyor; kadran Türkiye'de lazerle
(ya da baskı devre kartı olarak) üretiliyor. İsteğe bağlı ikinci aşama: 12 köşeli özel çelik kasa.

## Klasör yapısı

| Yol | İçerik |
|---|---|
| `onizleme/index.html` | 3D önizleme + plan sayfası (stil, renk, ibre, kasa, kordon seçimi; parçalara ayrılmış görünüm) |
| `tasarim/kadran/kadran.py` | Kadran üreteci: tek geometriden DXF (lazer), Gerber (PCB), SVG/PNG önizleme |
| `tasarim/kadran/cikti/` | Üretilmiş dosyalar: `ozgur_kadran_<stil>[_tarihli][_ayakli]_{lazer.dxf,gerber.zip}` |
| `tasarim/kasa/kasa.py` | 12 köşeli kasa, arka kapak ve ara halka (CadQuery) |
| `tasarim/kasa/cikti/` | `*.step` (CNC teklifi için), `*.stl` (reçine prova baskısı için), `montaj.glb` + base64 kopyası `montaj_glb.txt` (önizleme sayfası `.glb` sunamadığı için) |
| `reports/5000 TL altı özel saat yapımı.md` | Kaynaklı araştırma raporu: gümrük, fiyatlar, üretim yolları, teknik ölçüler, senaryolar |
| `research_notes/` | Raporun dayandığı ham araştırma notları |

## Kadran stilleri

- **klasik** — ince çubuk saat işaretleri, 12'de çift çubuk, `OZGUR` (Marcellus)
- **rakamli** — 12, 3, 6, 9 rakamları + çubuklar, `ozgur` (Jost)
- **sektor** — eş merkezli halkalar, 1–12 rakamları, artı çizgisi, `OZGUR` (Jost)

```bash
pip install shapely matplotlib pillow ezdxf
cd tasarim/kadran
python3 kadran.py stil=klasik                                  # NH38A için (tarihsiz)
python3 kadran.py stil=klasik tarih_penceresi=true             # NH35A için (saat 3'te tarih)
python3 kadran.py stil=klasik tarih_penceresi=true ayak_delikleri=true   # PCB + pim ile hizalama
python3 kadran.py stil=rakamli logo=özgür                      # logo yazısını değiştirmek
```

Ölçüler Seiko/TMI NH35–NH38 teknik föyünden: kadran Ø28,50 mm, merkez deliği Ø2,10 mm,
tarih penceresi 2,90 × 2,00 mm (r = 10,55 mm), isteğe bağlı ayak delikleri resmî F1/F2 konumlarında.
Ayak delikleri r ≈ 13 mm'de dakika halkasının üstüne denk gelir; pim takılınca saat 1:30 ve 7:30 yönünde
iki küçük nokta olarak görünür. Bu yüzden yalnız tarihli PCB kadranda (pencere hizası için) önerilir.
En ince çizgi 0,15 mm (PCB ve asitle aşındırma sınırı).

## Hangi dosya nereye

- **Lazer (önerilen):** `ozgur_kadran_<stil>_lazer.dxf` + Halsa'dan “Edico siyah–altın” 0,45 mm alüminyum levha.
  Atölyeye: ALTIN katmanı = kaplamayı yak, KESIM katmanı = kes. Önce artık parçada deneme.
- **PCB:** `ozgur_kadran_<stil>_gerber.zip` → Robotistan PCB Servisi (gümrük dahil). 0,4 mm FR4, ENIG,
  siyah / mavi / yeşil maske, merkez delik NPTH. Sipariş numarası için arka yüzde `JLCJLCJLCJLC` alanı var.
- **Özel kasa (Faz 2):** `tasarim/kasa/cikti/*.step` → yerli CNC atölyeleri (İkitelli / Ostim); önce `*.stl` ile reçine prova.

```bash
pip install cadquery trimesh
cd tasarim/kasa && python3 kasa.py
```

## Bütçe özeti (Ekim 2026)

Şubat 2026'dan beri yurt dışı kargolarda 30 € muafiyeti yok; paket başına ≈ 5.634 TL sabit gümrük
masrafı çıkıyor. Bu yüzden tüm parçalar yurt içinden ya da vergiyi sepette alan Türk ithalatçılardan.

| Senaryo | Toplam |
|---|---|
| Önerilen: NH38A + tarihsiz kadran + saatçi montajı | 5.541–7.141 TL |
| En ucuz: NH35A + tarihli kadran | 4.867–6.212 TL |
| Faz 2: 12 köşeli kasa, yerli CNC (tahmin) | ≈ 5.000–25.000 TL |

Ayrıntılar ve kaynaklar raporda.

## Yazı tipleri

`tasarim/kadran/fontlar/` içindeki Jost, Marcellus ve Inter, SIL Open Font License 1.1 ile dağıtılıyor
(lisans metinleri aynı klasörde).
