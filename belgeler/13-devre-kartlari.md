# Devre Kartları

---

## 1. Donanım Projeleri

Üç özel yapım devre kartı, Radxa ana kart ve resmî açık kaynak HAT için tek giriş noktası.

| Kart | Satın alma / proje girişi | Tasarım önizlemesi | Malzemeler |
|---|---|---|---|
| **Veri yolu IMU kartı v2** | [imu_to_dxl_1V0A](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/imu_to_dxl_1V0A/) | [3B](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/imu-to-dxl-1v0a-3d.png) · [PCB](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/imu-to-dxl-1v0a-pcb.png) | JLCPCB EDA (EasyEDA) Pro projesi, şema PDF'i, PCB STEP; [yeni sürüm açıklaması](#2-yeni-sürüm-donanım-2026-10-kaynak-hardware新版readmemd) |
| **Servo veri yolu HUB'ı** | [wire_hub_1V0A](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/wire_hub_1V0A/) | [3B](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/wire-hub-1v0a-3d.png) · [PCB](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/wire-hub-1v0a-pcb.png) | JLCPCB EDA (EasyEDA) Pro projesi, PCB STEP; [yeni sürüm açıklaması](#2-yeni-sürüm-donanım-2026-10-kaynak-hardware新版readmemd) |
| **Batarya arayüz kartı** | [POGO_PIN_1V0A](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/POGO_PIN_1V0A/) | [3B](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/pogo-pin-1v0a-3d.png) · [PCB](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/pogo-pin-1v0a-pcb.png) | JLCPCB EDA (EasyEDA) Pro projesi, PCB STEP; [yeni sürüm açıklaması](#2-yeni-sürüm-donanım-2026-10-kaynak-hardware新版readmemd) |
| **Radxa ZERO 3W ana kart** | [Ana kart satın alma (Taobao)](https://item.taobao.com/item.htm?id=763812025816) | [Resmî kart görseli](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/radxa-zero3w-official.webp) | [Resmî dokümanlar](https://docs.radxa.com/en/zero/zero3) · [Donanım tasarım dosyaları](https://docs.radxa.com/en/zero/zero3/download#hardware-design): şema, 2B ölçüler ve 3B model |
| **Resmî RPI Robot HAT** | [Pollen Robotics KiCad projesi](https://github.com/pollen-robotics/elec_RPI_Robot_HAT) | [Resmî tasarım görseli](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/rpi-robot-hat-official.png) | [Üretim/prototip dosyaları](https://github.com/pollen-robotics/elec_RPI_Robot_HAT/tree/main/production): Gerber, BOM, bileşen yerleşim (pick-and-place) koordinatları, şema ve STEP |

Her kartın tasarım durumu, kablolaması ve doğrulama kayıtları ilgili proje açıklamasındadır.

[Eski sürüm veri yolu IMU kartı ve yazılımı (firmware)](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/README.md): devre projesi, şema, kablo tablosu, karttaki BOM ve firmware malzemelerini korur.

[Komple montaj satın alma listesi](02-malzeme-listesi-bom.md) · [Donanıma giriş](03-donanim-baslangic.md) · [Ana sayfaya dön](01-proje-tanitimi.md)

---

## 2. Yeni Sürüm Donanım, 2026-10

### Yeni sürüm donanım (2026-10)

Üç kartın tamamı JLCPCB EDA (EasyEDA) Pro projesidir (`.eprj2`, şema ve PCB aynı dosyada). Her kart için bir klasör var:

| Klasör | Ne olduğu | Durum (2026-10-20) |
|---|---|---|
| [`imu_to_dxl_1V0A/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/imu_to_dxl_1V0A/) | Veri yolu IMU kartı v2. Eski sürüm ve firmware [`../imu_to_dxl/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/) içinde | Yönlendirme (routing) tamam, DRC'de yalnızca montaj deliklerinin tekrar tanımlanması kaldı (12 kayıt, kart üretimini etkilemiyor); henüz teslim alınıp gerçek ölçüm yapılmadı |
| [`wire_hub_1V0A/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/wire_hub_1V0A/) | Servo veri yolu HUB'ı: batarya girişi + veri yolu dağıtımı | Henüz prototip üretilmedi; CN1 yüksekliğinin değiştirilmesi gerekiyor |
| [`POGO_PIN_1V0A/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/POGO_PIN_1V0A/) | Batarya bağlantı kartı: iki banana soket + kablo lehim pedi | Delikler, pedler ve izler referans karta göre düzenlendi; henüz prototip üretilmedi |

Her klasörde:

- `<kart adı>.eprj2`: proje
- `<kart adı>-PCB.step`: tüm kartın 3B modeli, mekanik tarafın yapıyla uyumu için
- `<kart adı>-原理图.pdf` (şema PDF'i): şu an yalnızca IMU kartında var

Gerber, BOM ve kablo tablosu henüz çıkarılmadı; eski sürümün durumu için bkz. [`../imu_to_dxl/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/).

### imu_to_dxl_1V0A: Veri yolu IMU kartı v2

İşlev eski sürümle aynıdır: LSM6DSV16X, STM32G031'e bağlıdır; MCU kendini veri yolunda bir slave olarak tanıtır ve servolarla aynı tek hatlı yarı çift yönlü (half-duplex) veri yolunu kullanır. Protokol ve firmware için bkz. [`../imu_to_dxl/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/). Devre eski sürüme göredir; yerleşim yeniden yapıldı, konnektörler değiştirildi.

| Referans | Model | Görevi |
|---|---|---|
| U1 | STM32G031F8P6 | Ana denetleyici (MCU) |
| U2 | LSM6DSV16XTR | IMU |
| U3 | SN74LVC2G241DCUR | Yarı çift yönlü veri yolu alıcı-verici |
| U4 | HT7533-1 | 3.3 V LDO |
| F1 / D1 | MF-NSMF020X-2 / SMF12A | Kendiliğinden sıfırlanan sigorta / TVS |
| D2 | BZT52C5V1 | Veri yolu veri hattı 5.1 V kıskaç (clamp) |
| R6 | 0 Ω (C21189) | Veri yolu seri direnci, ilk kartta 150 Ω idi |
| J1 | A2007WR-3P | Servo veri yolu, 2.0 mm 3P dik (açılı) geçmeli. 1 = DXL_BUS, 2 = VDD_BUS, 3 = GND |
| J2 | BM03B-ACHSS-GAN-ETF | 1.2 mm ACH 3P yatay SMD. 1 = GND, 2 = VDD_BUS, 3 = DXL_BUS |
| J3 | PZ254V-11-06P | 2.54 mm 6P hata ayıklama portu: 1 = GND, 2 = SWDCLK, 3 = SWDIO, 4 = UART_RX, 5 = UART_TX, 6 = 3.3V |

Ayrıca 0402/0603 dirençler ve kondansatörler var; toplam 24 bileşen.

Eski sürümle karşılaştırma:

- Eski sürümdeki servo soketi `B3B-PH-K-S`, Feetech kablosunun fişine takılamıyordu (eski sürüm README'sinde kayıtlı); bu sürümde A2007WR-3P'ye geçildi
- Harici kristal X1 kaldırıldı (firmware zaten dahili HSI16 kullanıyor), firmware 0.2.0 değiştirilmeden yazılabilir
- R6, 150 Ω'dan 0 Ω'a düşürüldü: veri yolundaki her servoda pull-up var, paralel bağlanınca seri direnç düşük seviyeyi yükseltir. Kart geldiğinde yanıt paketi sırasında veri yolundaki düşük seviye gerilimi ölçülmelidir
- U2 180° döndürüldü ve kart şekli de değişti; ördeğe takıldıktan sonra IMU eksen eşlemesinin yeniden belirlenmesi gerekir. Firmware, çipin ham duruşunu (attitude) döndürmeden verir, bu nedenle yalnızca üst taraftaki (host) montaj döndürmesi değiştirilir; üç duruşta statik doğrulama yapılır
- Eski sürüm README'sinde v2 için kayıtlı yapılacaklar arasında bulunan **reset düğmesi ve çalışma gösterge LED'i bu sürümde yoktur**
- J3'ün PCB'de 3B modeli yok, dışa aktarılan STEP'te bu pin başlık eksiktir

### wire_hub_1V0A: Veri yolu HUB'ı

Aktif bileşen yoktur, yalnızca konnektörler vardır. Tüm konnektörler yalnızca `Battery`, `DXL_BUS` ve `GND` ağlarını (net) taşır.

| Referans | Model | Özellik |
|---|---|---|
| J1 | HC-1.2-3PWT | 1.2 mm 3P yatay SMD (Pico-EZmate uyumlu), 1.5 A |
| J2 | BM03B-ACHSS-GAN-ETF | 1.2 mm ACH 3P yatay SMD, 2 A |
| J3, J4 | A2007WR-3P | 2.0 mm 3P dik (açılı) geçmeli, 4 A |
| J5, J6 | A2007WV-3P | 2.0 mm 3P düz (dikey) geçmeli, 4 A |
| CN1 | DB125-2.54-2P-GN-S | Batarya girişi, yeşil vidalı terminal, 7 A, **kart üzerinde yükseklik 8.4 mm** |

Pin sıraları IMU kartıyla uyumludur: HUB'ın J1 ve J2'si ile IMU kartının J2'sinde 1 = GND, 2 = güç, 3 = DXL_BUS olup aynı yönlü kabloyla doğrudan bağlanır; HUB'ın J3–J6'sı ile IMU kartının J1'inde 1 = DXL_BUS, 2 = güç, 3 = GND'dir.

Yapılacaklar:

- CN1 çok yüksek, yapıyla çakışıyor; o konuma yalnızca yaklaşık 5 mm yüksekliğinde bir şey konabilir. Adaylar: 4 mm aralıklı SMD basmalı terminal (WAGO 2060 gibi, yükseklik 4.5 mm) veya terminal koymadan doğrudan kablo lehimlemek

### POGO_PIN_1V0A: Batarya bağlantı kartı

Şekil ve delikler, referans kart banana_pcb'ye (KiCad projesi, yalnızca Gerber mevcut) göre düzenlendi. Kart 39.19 × 6.79 mm.

| Konum | Ağ (net) | Ölçü |
|---|---|---|
| U2 (sol) | GND | Banana soket deliği Ø1.7 mm metalize, ped Ø3.2 mm |
| U1 (sağ) | Battery | Aynı, iki delik merkezi arası 33.8 mm |
| Ortadaki iki ped | Sol GND, sağ Battery | Üst katman SMD ped 2.4 × 4.4 mm, aralık 4.0 mm, deliksiz, kablo lehimlemek için |

İki pedin konumu da referans karta göredir: GND pedi sol delikten 10.98 mm, Battery pedi sol delikten 14.98 mm uzaklıkta; ikisi de iki deliği birleştiren çizginin 0.59 mm altındadır. 4.0 mm aralık, doğrudan 4 mm aralıklı bir basmalı terminal yapıştırmaya da tam uyar.

Proje adı POGO_PIN olsa da kartta artık yaylı pin (pogo pin) yoktur, yalnızca kablo lehim pedleridir.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
