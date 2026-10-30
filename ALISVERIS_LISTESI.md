# Alışveriş Listesi — Zekaland Robot Ördek (Feetech HD-1910)

> Parçaların tam listesi ve Çin fiyatları: [02-malzeme-listesi-bom.md](belgeler/02-malzeme-listesi-bom.md).
> Bu sayfa her parçanın **Türkiye'de, AliExpress'te ve JLCPCB'de** nereden alınacağını anlatır.
> Fiyatlar 31 Ekim 2026'daki yaklaşık referans fiyatlardır. Siparişten önce mutlaka kontrol edin.

**Önce karar verin:** Bu liste **Feetech HD-1910** servolu sürüm içindir. **Dynamixel XL330** servolu sürümle parçalar **birbirine uymaz**. Baskı parçaları da farklıdır.

## Özet

| Grup | Nereden | Yaklaşık tutar |
|---|---|---|
| A. Servolar + programlama kartı | AliExpress / yurt dışı | 200–530 $ (asıl maliyet) |
| B. Ana kart + sensörler | AliExpress | 70–110 $ |
| C. Özel devre kartları | JLCPCB (dizgili) | 40–80 $ + kargo |
| D. Standart parçalar | Türkiye | ~1.500–2.500 TL (tahmin) |
| E. 3D baskı | Kendi yazıcınız (PLA + TPU) | ~411 g filament, ~22 saat |

Çin içi toplam fiyat ~2.440 ¥ (≈ 340 $). Türkiye'ye getirince kargo ve gümrük eklenir. Gerçekçi bütçe **350–600 $**. Bu tutarın neresinde kalacağınızı en çok servoların nereden alındığı belirler.

---

## A. Servolar — yurt dışından

| # | Parça | Adet | Nereden | Arama kelimesi | Referans fiyat |
|---|---|---|---|---|---|
| A1 | **Feetech HD-1910-C001** (10 kg·cm, coreless, metal dişli, TTL veri yolu) | **15** | AliExpress, [openelab](https://openelab.com/products/feetech-hd1910-microduck-coreless-servo), [rcdrone.top](https://rcdrone.top/products/feetech-hd-1910-c001-10kg-cm-coreless-metal-gear-servo-for-microduck-diy-robot) | `Feetech HD-1910-C001`, `HD1910 microduck` | Çin'de 95 ¥/adet (~13 $). Avrupa/ABD dükkânlarında 30–35 $/adet |
| A2 | **Feetech FE-URT-2** USB servo programlama kartı | 1 | AliExpress, [RobotShop](https://www.robotshop.com/products/feetech-fe-urt-2-usb-to-ttl-485-bus-programmer) | `FE-URT-2`, `FE-URT2-C001` | 15–20 $ |
| A3 | Yedek servo | 1–2 | A1 ile aynı sipariş | — | İsteğe bağlı. Yeniden sipariş haftalar sürebileceği için önerilir. Servo sorunları için bkz. [14-tuzaklar.md](belgeler/14-tuzaklar.md) |

⚠️ **Servo uyarıları**
- Satıcılar voltaj ve tork bilgisini birbiriyle çelişecek şekilde yazıyor (4.8 V / 6 V / 8.4 V). Robot 2S pil kullanıyor ve dolu pilde veri yolu **8,4 V**'a çıkıyor. Satıcıya 8,4 V'u desteklediğini yazılı olarak teyit ettirin.
- Birkaç kişi birlikte yapıyorsanız servoları tek siparişte toplayın; kargo ve gümrük bir kez ödenir, adet artınca satıcıdan pazarlık şansı da doğar.
- 15 servoyu tek satıcıdan, tek siparişte alın. Hem gümrük işlemi tek seferde biter hem de aynı modeli aldığınızdan emin olursunuz.

## B. Ana kart ve sensörler — AliExpress

| # | Parça | Adet | Arama kelimesi | Referans | Not |
|---|---|---|---|---|---|
| B1 | **Radxa ZERO 3W** | 1 | `Radxa Zero 3W` | 309 ¥ / 20–40 $ | 1–2 GB RAM, eMMC'siz sürüm yeterli. Türkçe satış sayfası: [rcdrone.top](https://rcdrone.top/tr/products/radxa-zero-3w). Resmi satıcılar: [radxa.com/distributors](https://radxa.com/distributors). Bir partide (V1.12J) özel boot ayarı gerekiyor, bkz. [14-tuzaklar.md](belgeler/14-tuzaklar.md) |
| B2 | **IMX219 kamera modülü** (Raspberry Pi kamera v2 uyumlu) | 1 | `IMX219 camera module` | 46,8 ¥ | Kablo uzunluğu ve konnektör tipi Zero formuna (22 pin mini CSI) uymalı. Detay: [06-elektronik-satin-alma.md](belgeler/06-elektronik-satin-alma.md) |
| B3 | **VL53L8CX ToF mesafe sensörü** modülü | 1 | `VL53L8CX module` | 49,5 ¥ | Türkiye'de Farnell'de var ama çok pahalı. AliExpress'ten alın |

## C. Özel devre kartları — JLCPCB (dizgili sipariş)

Üç kartı **tek siparişte** birleştirin. Hem kargo hem gümrük bir kez ödenir.

| # | Kart | Adet | Dosya | Referans | Not |
|---|---|---|---|---|---|
| C1 | **RPI Robot HAT** (Pollen Robotics, açık kaynak) | 1 | [pollen-robotics/elec_RPI_Robot_HAT → production/](https://github.com/pollen-robotics/elec_RPI_Robot_HAT/tree/main/production) | 120 ¥ | Gerber, BOM ve CPL hazır, doğrudan JLCPCB PCBA'ya yüklenir. Ses çipi, amfi, RS-485 ve regülatör üzerinde. **Pil şarj devresi yok.** HAT basmadan kurmak için: [08-hat-olmadan-kurulum.md](belgeler/08-hat-olmadan-kurulum.md) |
| C2 | **imu_to_dxl** (servo veri yolundaki IMU kartı, ID 200) | 1 | [hardware/imu_to_dxl](https://github.com/fanhao375/microduck-replica/tree/master/hardware/imu_to_dxl) (EasyEDA Pro `.eprj2`, şema PDF, etkileşimli BOM) | 80 ¥ | `.eprj2` dosyasını EasyEDA Pro'da açıp Gerber/BOM/CPL dışa aktarın. Yeni v2 (`imu_to_dxl_1V0A`) 20 Ekim itibarıyla **henüz test edilmedi**. Bağlantı: [09-imu-kablo-tablosu.md](belgeler/09-imu-kablo-tablosu.md) |
| C3 | **Pil arayüz kartı** (banana PCB / POGO_PIN_1V0A) | 1 | [hardware/新版/POGO_PIN_1V0A](https://github.com/fanhao375/microduck-replica/tree/master/hardware/%E6%96%B0%E7%89%88) | 20 ¥ | Basit 2 katlı kart, dizgi gerekmez |

Kartların ayrıntıları: [13-devre-kartlari.md](belgeler/13-devre-kartlari.md).
JLCPCB'nin minimum adedi 5'tir. Fazla kartları atölye ya da başka kurucularla paylaşabilirsiniz.

## D. Türkiye'den alınacaklar

Bunlar standart parçalar. Robotistan, direnc.net, Hepsiburada, Trendyol, rulmancılar ve hırdavatçılarda bulunur.

| # | Parça | Adet | Nerede aranır | Not |
|---|---|---|---|---|
| D1 | **Sony NP-F550** uyumlu pil (2S, 7,4 V) | 1 (+1 yedek) | Fotoğrafçılık mağazaları, Hepsiburada, Trendyol: `NP-F550` | **NP-F970 yuvaya sığmaz.** HAT şarj etmez, ayrı şarj aleti alın |
| D2 | NP-F serisi şarj aleti | 1 | Aynı yerler | — |
| D3 | microSD kart, 32–64 GB (A1/U3) | 1 | Her yerde | — |
| D4 | Mini hoparlör (~8 Ω, 1–2 W, ince tip) | 1 | Robotistan, direnc.net: `mini hoparlör 8 ohm` | Boyut kafa içine sığmalı |
| D5 | 2,5 mm banana konnektör (PCB tipi, dişi) | 2 | direnc.net, Robotistan: `2.5mm banana soket` | Pil kartına lehimlenir |
| D6 | Servo uzatma kabloları | birkaç | Robotistan | Feetech kablo/konnektör tipine dikkat edin. Ayrıntı: [06-elektronik-satin-alma.md](belgeler/06-elektronik-satin-alma.md) |
| D7 | Rulman **16×22×4** (6704ZZ / 61704) | **11** | Rulmancı, Trendyol: `6704 rulman` | En kritik rulman |
| D8 | Rulman **10×15×3** (6700ZZ / 61700) | **3** | Rulmancı: `6700 rulman` | — |
| D9 | Rulman **6×12×3** | **4** | Rulmancı, model yapı dükkânları | Paten rulmanı olarak da satılır |
| D10 | Düz uçlu sac vidası: **M2×5, M2×6, M2×8, M2,5×6, M2,5×8** | birer paket | Hırdavat, Trendyol: `M2 sac vidası` | Toplamda yaklaşık 325 vida gidiyor, bol alın. Ayrıntı: [07-vidalar-ve-baglanti.md](belgeler/07-vidalar-ve-baglanti.md) |
| D11 | M2 ısıl ankraj (heat-set insert) | ~60 | Robotistan, 3D baskı dükkânları: `M2 heat insert` | Havya ucuyla takılır |
| D12 | **Loctite 243** vida sabitleyici (orta mukavemet, mavi) | 1 | Hırdavat, oto yedek parça | 263 (kırmızı) değil, 243 |
| D13 | Kaymaz taban pedi / silikon ped | 1 tabaka | Hırdavat, Trendyol: `kaymaz ped yapışkanlı` | Ayak tabanları için |
| D14 | Lehim teli, makaron, ince silikon kablo (24–26 AWG) | — | Robotistan, direnc.net | Atölyede yoksa |

## E. 3D baskı (kendi yazıcınızla)

Robotta 33 baskı parçası var. Listenin tamamı [02-malzeme-listesi-bom.md](belgeler/02-malzeme-listesi-bom.md)'de, baskı notları [12-baski-ve-cad.md](belgeler/12-baski-ve-cad.md)'de.

| Malzeme | Parçalar | Not |
|---|---|---|
| **PLA** | Neredeyse hepsi | ~1 makara yeter |
| **TPU (95A)** | Yumuşak çene, yumuşak ağız üstü, birleşik teker | Bambu A1 TPU basabilir. AMS'siz, doğrudan beslemeyle |
| *(isteğe bağlı)* alüminyum | Boyun, gövde tabanı, üst bacak plakaları, rulman makarası | PLA ile başlamak yeterli |

**Baskı dosyaları bu repoda:** [`modeller/feetech/zekaland-robot-ordek-feetech.3mf`](modeller/feetech/zekaland-robot-ordek-feetech.3mf) (Bambu Studio, ayarlar hazır) ve [`modeller/feetech/stl/`](modeller/feetech/stl/) (diğer dilimleyiciler). Ayak tabanlarında ZEKALAND yazısı var.

---

## Gümrük ve sipariş taktikleri

- **Siparişleri birleştirin:** Ayrı paketler gelirse her biri ayrı gümrük işlemine girer. Üç kartı tek JLCPCB siparişinde, servolarla URT-2 kartını da tek AliExpress satıcısından alın.
- **Gümrük kurallarını sipariş günü kontrol edin:** Posta/kargo ile gelen yurt dışı alışverişlerin vergi muafiyet limiti ve oranları Türkiye'de sık değişiyor.
- **Servolarda acele etmeyin:** 15 servonun Avrupa fiyatıyla Çin fiyatı arasındaki fark tek başına 250 $'ı geçebiliyor.
- **Sıralama:** Önce servoları ve URT-2 kartını sipariş edin, en uzun teslim süresi onlarda. Beklerken 3D baskıları yapın ve kartları JLCPCB'ye verin.

## Güncellik

Fiyatlar ve linkler 31 Ekim 2026 tarihlidir. Eskiyen bir link görürseniz issue açın.
