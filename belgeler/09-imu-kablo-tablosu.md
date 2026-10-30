# imu_to_dxl kablo tablosu

> El ile bağlantı yaparken kullanılır. Bileşen konum numaraları (referans tasarımcılar) `microduck-replica/BOM.md` ile aynıdır.
> Durum: taslak çözüm, gerçek donanımda doğrulanmadı.

## Bileşen listesi (JLCPCB/LCSC numaralarıyla)

(¥ = Çin yuanı; bu belgede fiyat yoktur. "立创编号" = JLCPCB/LCSC parça numarası.)

| Konum | Bileşen | Kılıf | LCSC no. |
|---|---|---|---|
| U1 | STM32G031F8P6 | TSSOP-20 | C529334 |
| U2 | LSM6DSV16XTR | LGA-14 | C5267406 |
| U3 | SN74LVC2G241DCUR | VSSOP-8 | C10430 |
| U4 | HT7533-1 (30V giriş, 100mA) | SOT-89 | C14289 |
| F1 | PPTC MF-NSMF020X-2 (24V / 200mA tutma) | 1206 | C210358 |
| D1 | TVS SMF12A | SOD-123FL | C2943870 |
| R1, R2, R4, R5 | 10kΩ | **0603** | C25804 |
| R6 | 150Ω | **0603** | C22808 |
| D2 | BZT52C5V1 5,1V zener diyot | **SOD-123** | C151588 |
| C1–C4, C8 | 100nF 50V | **0603** | C14663 |
| C5 | 4,7µF / 16V X5R | 0603 | C19666 |
| C6 | 10µF / 25V X5R | 0805 | C15850 |
| C7 | 10µF / 10V | 0603 | C19702 |
| J1, J2 | B3B-EH-A (3P **2,5mm**, Dynamixel / resmi HAT kablosu) | geçmeli (THT) | C160259 |
| **J4, J5** | **B3B-PH-K-S (3P 2,0mm dikey, Feetech `AMP2.0-3P` karşılığı)** | geçmeli (THT) | belirlenmedi |
| J3 | SWD+seri 6P pin header PZ254V-11-06P | geçmeli (THT) | C492405 |

## Net listesi (23 net)

### VDD_BUS — servo veri yolu ham gerilimi (2S Li-ion, 6,0–8,4V)
J1.2 · J2.2 · **J4.2** · **J5.2** · F1.1

> Dört soketin `VDD_BUS` hattı **doğrudan geçişli bakır alandır:** `J1.2 → J2.2 → J5.2 → J4.2`, baştan sona 0,76 mm.

### VDD_F — sigortadan sonra
F1.2 · D1 katot · C6.1 · C8.1 · U4.2 (Vin)

### +3V3
U4.3 (Vout) · C7.1 · U1.4 (VDD/VDDA) · C4.1 · C5.1 · R2.2 ·
U2.5 (Vdd_IO) · U2.8 (Vdd) · C1.1 · C2.1 · R1.2 ·
U3.8 (VCC) · C3.1 · J3.6 · **R7.2**

### GND
D1 anot · C6.2 · C8.2 · U4.1 (GND) · C7.2 ·
U1.5 (VSS/VSSA) · C4.2 · C5.2 ·
U2.2 (SDx) · U2.3 (SCx) · U2.6 (GND) · U2.7 (GND) · C1.2 · C2.2 ·
U3.4 (GND) · C3.2 · J1.1 · J2.1 · J3.1 · **J4.3** · **J5.3** · C9.2 · X1.2

### Reset
| Net | Bağlantı noktaları |
|---|---|
| NRST | U1.6 (PF2-NRST) · R2.1 |

R2'nin öbür ucu (R2.2) +3V3'e bağlıdır; 10k pull-up oluşturur.

### Dört pull-up direnci (R1/R2/R4/R5, öbür uçların hepsi +3V3'e)

| Konum | Neyi çeker | Neden |
|---|---|---|
| **R1** | `SPI_CS` | Güç verme ve reset sırasında PA4 yüksek empedanstadır; CS havada kalırsa IMU onu I²C moduna geçiş sanabilir veya yol gürültüsünü komut sanabilir. **Zorunlu** |
| **R2** | `NRST` | Çipin içinde zaten ~40 kΩ'luk zayıf bir pull-up vardır; ek 10 kΩ parazit bağışıklığını artırır. Güçlendirme öğesi |
| **R4** | `DE` | `1OE#` **düşük seviyede gönderimi etkinleştirir.** Reset sırasında PA1 yüksek empedanstadır; bu pin düşüğe yüzerse gönderim tamponu açılır, kart veri yoluna veri basar ve 15 servoyla çakışır. **Zorunlu** |
| **R5** | `DXL_DATA` | Veri yolu boştayken ve kimse sürmüyorken `2A` CMOS girişi yüzerse geçiş (shoot-through) akımı oluşur, UART da gürültüyü başlangıç biti sanabilir. Kart boşta seviyesini kendisi tanımlar, ana bilgisayara bağımlı olmaz |

> R4 ve R5, 2026-09-06'da topluluk değerlendirmesi üzerine eklendi. Önceden yalnızca CS'ye pull-up konmuştu;
> **aynı gerekçe DE'ye yaygınlaştırılmamıştı, bu bir eksikti.**

### IMU (SPI dört tel + iki kesme)
| Net | U1 (STM32) | U2 (LSM6DSV16X) | Diğer |
|---|---|---|---|
| SPI_CS   | 11 · PA4 | 12 · CS       | R1.1 (R1.2 +3V3 pull-up'a) |
| SPI_SCK  | 12 · PA5 | 13 · SCL      | |
| SPI_MISO | 13 · PA6 | 1 · SDO/SA0   | |
| SPI_MOSI | 14 · PA7 | 14 · SDA      | |
| IMU_INT1 | 7 · PA0  | 4 · INT1      | |
| IMU_INT2 | 15 · PB0/PA8 | 9 · INT2  | |

### Yarı çift yönlü veri yolu (U3 = SN74LVC2G241 çift tampon)
| Net | Bağlantı noktaları |
|---|---|
| MCU_TX   | U1.9 (PA2 · USART2_TX) · U3.2 (1A) |
| MCU_RX   | U1.10 (PA3 · USART2_RX) · U3.3 (2Y) |
| DE       | U1.8 (PA1 · USART2_DE) · U3.1 (1OE#) · **R4.1** |
| DXL_DATA | U3.6 (1Y) · U3.5 (2A) · **R5.1** · **R6.1** — tampon tarafı |
| **DXL_BUS** | **R6.2** · **D2 katot** · J1.3 · J2.3 · **J4.1** · **J5.1** — konnektör tarafı |
| **RX_EN** | **U1.1 (PB7/PB8)** · **U3.7 (2OE)** · **R7.1** — alım tamponu etkinleştirme, 2026-09-07'de eklendi |

`U3.7 (2OE)` önceden doğrudan +3V3'e bağlıydı; 2026-09-07'de **`RX_EN` neti** yapıldı: **R7 10 kΩ ile +3V3'e pull-up** edilir,
aynı zamanda **U1.1 (PB7/PB8)**'e bir tel çekilir.

**Varsayılan davranış değişmedi** — MCU reset sırasında PB7 yüksek empedanstadır, R7 `2OE`'yi yukarı çeker, alım tamponu her zamanki gibi açık kalır;
yazılımda tek satır yazılmasa da değişiklikten öncesiyle aynıdır. Bu bir **rezervasyondur:** gönderim sırasındaki yankıyı (echo) kapatmak istenirse PB7 push-pull çıkış olarak yapılandırılıp düşüğe çekilir;
aynı zamanda `2Y` yüksek empedansa geçtiğinde RX'in yüzmesini önlemek için `MCU_RX` pininin dahili pull-up'ı açılır.

### Hata ayıklama portu J3 (6P, `PZ254V-11-06P` / `C492405`)

| Pin | Net | Kaynak |
|---|---|---|
| 1 | GND | |
| 2 | SWDCLK | U1.19 (PA14) |
| 3 | SWDIO | U1.18 (PA13) |
| 4 | **UART_RX** | **U1.17** `PA12[PA10]` → **PA10** = `USART1_RX` olarak yeniden eşlenir; USB-TTL'in TX'ine bağlanır (3,3V seviye) |
| 5 | **UART_TX** | **U1.16** `PA11[PA9]` → **PA9** = `USART1_TX` olarak yeniden eşlenir; USB-TTL'in RX'ine bağlanır (3,3V seviye) |
| 6 | +3V3 | Hata ayıklayıcının VTref gerilim referansı; 5V'a bağlamayın |

**2026-09-21 düzeltmesi:** Bu dizindeki 2026-09-08 tarihli [şema PDF'i](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/imu_to_dxl-原理图.pdf) ile karşılaştırıldığında,
SWD **1, 2, 3, 6** numaralı pinlere bağlıdır; 4. ve 5. pinler seri porttur. Eski dört telli flat kablo 1–4. pinlere topluca takılamaz;
4. pin 3,3V ya da VTref sanılamaz. Bağlamadan önce gerçek kartın 1. pin işaretini ve hata ayıklayıcı arayüzü tanımını kontrol edin.

16/17. pinlerin yeniden eşlenmesi `SYSCFG_CFGR1` ile yapılır (DS12992 Rev 3, Table 12 dipnot 4).

**Neden USB yok:** STM32G031'in **USB çevre birimi yoktur** (kılavuzda "USB" aranırsa sıfır sonuç; Development support bölümünde yalnızca
"serial wire debug (SWD)" yazar). USB eklemek için ek bir CH340/CP2102 gerekir, 45×22 mm kartta buna değmez.
Hata ayıklama için SWD yeterlidir:

| Yöntem | Ne gerekir | Açıklama |
|---|---|---|
| **RTT** (önerilen) | J3'ün 1, 2, 3, 6 pinleri | `probe-rs` CMSIS-DAP üzerinden RTT çalıştırmayı destekler, hedef RAM'i doğrudan okur, **CPU'yu durdurmaz**, 50 Hz kontrol döngüsünü etkilemez |
| Seri printf | J3'ün 4/5 pinleri + herhangi bir USB-TTL | USART1 üzerinden |
| Semihosting | yalnızca J3 | Her printf CPU'yu durdurur, kontrol döngüsü çöker, **kullanmayın** |
| ~~SWO / ITM~~ | — | **Cortex-M0+'ta yoktur;** M3 ve üstünde vardır |

### Servo arayüzü — iki takım bir arada, ⚠️ **pin sıraları terstir**

Kartta dört servo veri yolu soketi vardır, ikişer ikişer iki grup; üç tel birebir paralel bağlıdır (aynı elektriksel düğüm),
**ancak iki grubun pin sıraları tamamen terstir** — çünkü iki üreticinin kablo sırası zaten farklıdır.

**`J1` / `J2` — `B3B-EH-A`, 2,5 mm, Dynamixel / resmi HAT kablo demetine uygun**

| Pin | Net |
|---|---|
| 1 | GND |
| 2 | VDD_BUS |
| 3 | **DXL_BUS** |

**`J4` / `J5` — `B3B-PH-K-S`, 2,0 mm, Feetech HD-1910 kablo demetine uygun**

| Pin | Net |
|---|---|
| 1 | **DXL_BUS** |
| 2 | VDD_BUS |
| 3 | **GND** |

> ⚠️ **`J1`'in netlerini kopyalayıp `J4`'e vermeyin.** Feetech "HD-1910-C001 Seri Şartname" A/0,
> 3./7. sayfa madde 6-7, kablo ucunun `1=Signal / 2=Vcc / 3=GND` olduğunu yazar; Dynamixel tarafıyla baştan sona terstir.
> Neyse ki **2,0 mm ile 2,5 mm birbirine takılamaz,** yanlış takma fiziksel olarak engellenmiştir; geriye yalnızca "yanlış çizme" ihtimali kalır.
> Dört soketin pin sırası 2026-09-08'de PCB net listesinden geri okunarak doğrulandı, hepsi doğru.
>
> Ayrıca **`AMP2.0` 2,0 mm, `JST EH` 2,5 mm'dir;** Feetech kablosu `J1`/`J2`'ye takılamaz,
> ⚠️ ilk kartta yapılan gerçek denemede (2026-09-17): `B3B-PH-K-S`'nin **gövdesi** Feetech konnektörüne uymuyor, takılamıyor; gövdeyi kesip yalnızca pinleri bırakmak işe yarıyor. v2'de Feetech kablosuna gerçekten uyan bir soket kullanılacak.
> Tersi de geçerlidir — hangi servo takımı kullanılıyorsa o grup kullanılır.

> 📌 **3. pin önceden bu tabloda yanlışlıkla `DXL_DATA` olarak yazılmıştı.** 2026-09-06'da `R6` 150 Ω seri direnci eklenince
> tampon tarafı (`DXL_DATA`) ile konnektör tarafı (`DXL_BUS`) iki ayrı net oldu; konnektördeki `DXL_BUS`'tur.
> 2026-09-08'de düzeltildi.

## Boşta pinler

- U1: **3 (PC15-OSC32_OUT), 20 (PB3/PB4/PB5/PB6)**
  - 3. pin lehim pedine çıkarılmıştır, 2. pinle birlikte aktif osilatör için ayrılmış yeri oluşturur (varsayılan olarak takılmaz), aşağıdaki "Saat" bölümüne bakın
  - 20. pin tek tamamen boş GPIO'dur (PB3/PB4/PB5/PB6 dört portu birleştirir, en esnek olanıdır), sonraki kullanım için bırakılmıştır
  - 1. pin (PB7/PB8) aslında boştu, 2026-09-07'den itibaren `RX_EN` olarak kullanılıyor
  - 2. pin (PC14-OSC32_IN) `OSC_IN`'e, 16/17. pinler (PA9/PA10) `UART_TX`/`UART_RX`'e bağlıdır
    — bu tablo önceden bunları yanlışlıkla boşta olarak listelemişti, 2026-09-07'de düzeltildi
- U2: 10 (OCS_Aux), 11 (SDO_Aux) — yardımcı SPI kullanılmıyor, ST DS13510 havada bırakılmasına izin verir; temkinli yaklaşım OCS_Aux'u Vdd_IO'ya bağlamaktır

**U2.2 (SDx) ve U2.3 (SCx) mutlaka toprağa bağlanmalıdır,** havada bırakılamaz — ST DS13510 Rev 1, Table 1.

## Saat: dahili HSI16 kullanılır, kristal yeri ayrılmış ama takılmaz

**Bu kılıf pasif kristal bağlayamaz.** DS12992 Rev 3, Table 12 (s.36): TSSOP20'nin 2. pininin (`PC14-OSC32_IN`) ek işlevleri arasında `OSC_IN` vardır, ancak 3. pin (`PC15-OSC32_OUT`) yalnızca `OSC32_OUT`'tur,
**`OSC_OUT` yoktur;** `PF0`/`PF1` bu kılıfta dışarı çıkarılmamıştır. Pasif kristalin titreşmeye başlaması için iki pin gerekir.

| Çözüm | Uygulanabilirlik |
|---|---|
| Pasif yüksek hızlı kristal | ❌ `OSC_OUT` yok |
| Aktif osilatör, HSE bypass (2. pine verilir, 3. pin `OSC_EN` olabilir) | ✅ |
| 32,768 kHz LSE pasif kristal | ✅ ama PLL'ye saat veremez, yalnızca HSI16'yı kalibre etmeye yarar |

HSI16 doğruluğu (Table 41, s.64): fabrika −%0,75/+%0,5, 0–85 °C sıcaklık kayması ±%1, gerilim kayması ±%0,1
→ en kötü durumda yaklaşık **−%1,85 / +%1,55**. 1 Mbps UART için tipik tolerans ±%3'tür, yeterlidir ama pay fazla değildir.

**Yaklaşım:** 2 ve 3. pinler lehim pedine çıkarılır, 3225 aktif osilatör yeri + ayrıştırma (decoupling) yeri bırakılır. Başlangıçta varsayılan olarak takılmazdı; 2026-09-08'den itibaren X1 / R3 / C9 varsayılan olarak takılıdır;
yazılım önce HSI16 kullanır, 1 Mbps'de gerçek ölçümde bit hatası görülürse HSE bypass etkinleştirilir.
Dikkat: şemada X1'in `Tri-state` etkinleştirme pini **sabit olarak 3,3 V'a bağlıdır;** yukarıda söylenen "3. pin (PC15) `OSC_EN` olabilir" şemaya çizilmemiştir, PC15 boştadır. İlk kartta MCU'nun osilatörü kontrol etmesi isteniyorsa PC15 → X1.1 jumper tel çekilir; bkz. README "Değerlendirme kaydı · 2026-09-16".

## Etkinleştirme polaritesi açıklaması

`1OE#` düşük seviyede gönderim tamponunu etkinleştirir, `2OE` yüksek seviyeye bağlanarak alım tamponunu sürekli açık tutar.

- PA1, USART2'nin donanımsal DE pinidir; `CR3.DEP = 1` ayarlanır (DE düşük etkin), gönderim/alım geçişi donanımla yapılır
- Alımın sürekli açık olması, gönderim sırasında RX'te kendi yankısının alınması demektir; yazılım gönderim uzunluğuna göre bunu atar
- Alternatif çözüm `2OE`'yi de DE'ye bağlamaktır (gönderim sırasında alım tamponunu kapatır), ancak o zaman gönderim sırasında MCU'nun RX pini havada kalır, yeniden etkinleştirmede sahte başlangıç biti oluşabilir; önerilmez
- **2026-09-07 iyileştirmesi:** `2OE` artık doğrudan +3V3'e sert bağlı değil, R7 10 kΩ ile pull-up edilir ve aynı zamanda `U1.1 (PB7/PB8)`'e çekilir.
  Varsayılan hâlâ sürekli açıktır (davranış aynı), ancak yazılıma bir seçenek eklenmiştir — alımı kapatmak istendiğinde PB7 düşüğe çekilir ve MCU RX pininin
  dahili pull-up'ı açılarak yüzme sorunu çözülür. DE'ye bağlamaktan daha esnektir: kapatılıp kapatılmayacağı ve ne zaman kapatılacağı yazılımın kararıdır

## HD-1910-C001 gerçek parametreleri (Feetech resmi ürün sayfası, ön satış dönemi)

Feetech'in "küçük ördek" için özel yaptığı modeldir; sayfa başlığı "**Açık kaynak küçük ördek servosu** — seri veri yolu servo, küçük ördek AI oyuncağı için özel geliştirildi".
Servonun üzerinde yazan: **"üç pinli arayüz · TTL seri veri yolu"**.

| Madde | Değer |
|---|---|
| Gerilim aralığı | **5 V – 8,4 V** |
| Sıkışma (stall) torku | **10 kg·cm = 0,98 N·m** |
| Anma yükü | **3,0 kg·cm = 0,294 N·m** |
| Yüksüz hız | 0,09 s/60° (110 RPM) |
| **Bekleme akımı** | **21 mA** |
| **Yüksüz akım** | **140 mA** |
| **Anma akımı** | **500 mA** |
| **Sıkışma akımı** | **1,8 A** |
| Dış boyut | 34 × 20 × 23 mm |
| Ağırlık | 22,5 ± 2 g |
| Gövde | PA + Fiber |

Boyutlar XL330 ile (20×34×26 mm) aynı sınıftadır, mekanik olarak yaklaşık değiştirilebilir; tork XL330-M288'e (0,52 N·m) göre yaklaşık iki kat güçlüdür.

> ⚠️ `HL-2915-C002` şartnamesindeki elektriksel parametreleri bu modele uygulamayın — o 12 V'luk (9–14 V) bir modeldir.
> Ortak kullanılabilecek yalnızca konnektör tanımı ve protokol bölümüdür.

### ⚠️ J1↔J2 doğrudan geçiş yolunda aşırı akım

J1 / J2'nin üç teli birebir paralel bağlıdır; **bu kart zincirin ortasındaysa, alt akımdaki tüm servoların akımı kartın konnektörlerinden ve bakır izlerinden geçer:**

| Çalışma durumu | Tek servo | ×15 |
|---|---|---|
| Bekleme | 21 mA | 0,3 A |
| Yüksüz dönme | 140 mA | 2,1 A |
| **Anma yükü** | **500 mA** | **7,5 A** |
| Sıkışma | 1,8 A | 27 A |

**JST EH'nin anma akımı ise yalnızca 3 A'dir.**

> F1 (200 mA PPTC) **etkilenmez** — yalnızca kartın kendi beslemesi için olan hatta seri bağlıdır
> (`VDD_BUS → F1 → VDD_F → U4`), J1→J2 doğrudan geçiş yolunda değildir.

**İkisinden birini seçin:**

1. **Kartı zincirin ucuna (yaprak düğüm) takın,** yalnızca J1 kullanılsın, J2 boş kalsın veya yalnızca 1 servo bağlansın — karttan geçen akım yaklaşık 12 mA olur. **Önerilen**
2. Zincirin ortasına konması zorunluysa, PCB'de `VDD_BUS` ve `GND` J1'den J2'ye **geniş bakır alanla** (≥ 2 mm veya doğrudan dökme bakır) çekilmeli
   ve alt akımdaki servo sayısının 3 A'i aşmadığı hesaplanmalıdır

## Feetech arayüz tanımı (resmi şartnamede doğrulandı)

**Kaynak:** Feetech "HL-2915-C002 Seri Şartname" A/0, 2026-02-27, sayfa 4, madde 6-7.

```
6-7  连接器和电缆 Connector and Cable
     类型 Type        AMP-3
     材质 Material    PP
     线长 Length      15CM / 25CM
     引脚定义         1  GND
     Pin Definition   2  Vcc
                      3  Signal/TTL
```

(Çince alanlar: 连接器和电缆 = konnektör ve kablo; 类型 = tür; 材质 = malzeme; 线长 = kablo uzunluğu; 引脚定义 = pin tanımı.)

**`1=GND / 2=Vcc / 3=Signal`, Dynamixel ile tamamen aynı → J1/J2'nin mevcut bağlantısı doğrudur.**

İlgili kanıt: `HD-1910-C001.stp` montaj dosyasında konnektör parçasının adı **`AMP-3P`**'dir ve bu montaj
`HL-2915-C002-20260409_ASM`'yi de içerir — iki model aynı platformu paylaşır, arayüz tanımı ortaktır.

### Aynı şartnamedeki diğer kullanılabilir maddeler

| Madde | Değer | Anlamı |
|---|---|---|
| 7-2 Protokol türü | Half Duplex Asynchronous, **8bit / 1stop / No Parity** | Kartla aynı |
| 7-4 Baud hızı | 38400 ~ 1 Mbps, **fabrika varsayılanı 1 Mbps** | Dynamixel ile aynı hız |
| 7-3 ID aralığı | 0–253, **fabrika varsayılanı ID 1** | 15 servonun ID'si tek tek değiştirilmeli; bu kart 200 kullanır, çakışmaz |
| 12 **Sinyal yüksek seviye** | **2 V ~ 5 V** | Aşağıya bakın |
| 12 Sinyal düşük seviye | 0,0 V ~ 0,45 V | |
| 6-6 Açı sensörü | 12 Bit manyetik enkoder | Manyetik enkoder ⇒ **little-endian bayt sırası** |

**Sinyal seviyesine iki yönden de bakmak gerekir:**

1. Kart veri yolunu sürerken — `SN74LVC2G241` 3,3 V beslemede yaklaşık 3,3 V çıkarır, servonun istediği 2–5 V yüksek seviye penceresinin içindedir ✅
2. Servo veri yolunu sürerken — **5 V**'a kadar çıkarabilir; 74LVC 3,3 V beslemede **girişi 5,5 V'a dayanıklıdır** ✅
   (LV/HC yerine LVC seçilmesi tam olarak bu koşulu sağlar)

> ⚠️ Bu şartname **HL-2915-C002** (12 V, 9–14 V) içindir, HD-1910 (5–8,4 V) için değildir.
> **Elektriksel parametreler karıştırılamaz** — besleme aralığı, sıkışma akımı, aşırı gerilim koruma eşiği farklıdır.
> Ortak olan yalnızca **konnektör tanımı ve protokol** bölümüdür.

### Arka plan: Feetech'in farklı serilerinin fiziksel katmanı farklıdır

Resmi serilerin bellek tablosu kılavuzlarının (<http://doc.feetech.cn>, arayüz `getQr/{q}`) özgün metni:

| Seri | Seviye | Varsayılan baud hızı |
|---|---|---|
| **STS** (manyetik enkoderli) | **TTL tek veri yolu** | **1M** |
| SCS (potansiyometreli) | TTL tek veri yolu | 1M / 500k |
| SMS (manyetik enkoderli) | **RS485** | 115200 |
| HLS (manyetik enkoderli) | belirtilmemiş | 1M |
| SHC | CANopen | 125k |

"Feetech = TTL tek tel" yalnızca STS/SCS/HL koluna doğrudur, SMS RS485'tir. Seri değiştirmeden önce o serinin kılavuzuna bakın.

## Protokol otomatik tanıma (jumper yok, DIP anahtar yok)

İki üreticinin paket başlığı doğal olarak ayırt edilebilir; ayırt edici nokta **3. ve 4. baytlardır**:

| | Başlık | Devamı | Sağlama (checksum) |
|---|---|---|---|
| Dynamixel V2 | `FF FF` | **`FD 00`** | CRC-16 (poly 0x8005) |
| Feetech STS/SCS | `FF FF` | `ID` + `LENGTH` | `~(ID+LENGTH+INST+parametreler)` |

Belirsizlik yoktur: Feetech paketinin 3. baytı ID'dir (0xFD olabilir), ama **4. bayt LENGTH asla 0 olamaz**
(en küçüğü 2 = komut + sağlama). Bu yüzden `FF FF FD 00` yalnızca V2 olabilir.

```
状态：未知 / 已锁 V1 / 已锁 V2

未知时，收到 FF FF 开头的包：
    if 字节[2]==0xFD && 字节[3]==0x00:
        按 V2 拆，算 CRC-16 → 过了记一票 V2
    else:
        按 V1 拆，算 ~sum   → 过了记一票 V1
    连续 3 票一致 → 锁定

锁定后：只按锁定协议解析，回复也用同一种
兜底：连续 100 包全解析失败 → 解锁重新识别
```

(Kod bloğundaki yorumların anlamı: Durum: bilinmiyor / V1'e kilitli / V2'ye kilitli. Bilinmiyorken `FF FF` ile başlayan paket gelirse: 3. bayt 0xFD ve 4. bayt 0x00 ise V2 olarak ayrıştır, CRC-16 hesapla, geçerse V2'ye bir oy yaz; değilse V1 olarak ayrıştır, `~sum` hesapla, geçerse V1'e bir oy yaz. Art arda 3 oy aynıysa kilitlen. Kilitlendikten sonra yalnızca kilitli protokole göre ayrıştır, yanıt da aynı protokolle verilir. Yedek: art arda 100 paket tamamen ayrıştırılamazsa kilidi aç ve yeniden tanı.)

Aşağıdakilerin hepsi **Feetech resmi "Servo SCS İletişim Protokolü" özgün metnine** dayanır:

- Çerçeve biçimi: **1 başlangıç biti + 8 veri biti + parite yok + 1 durdurma biti,** toplam 10 bit
- Başlık: art arda iki `0xFF`
- ID aralığı **0～253** (`0x00`～`0xFD`), **yayın (broadcast) ID'si = 254 (`0xFE`)**
- Veri uzunluğu **Length = parametre sayısı N + 2,** bu yüzden **en küçüğü 2'dir, asla 0 olamaz** ← ayırt etmenin belirsizliksiz olmasının dayanağı
- Sağlama toplamı = `~(ID + Length + Instruction + Param1 + … + ParamN)`, 255'i aşarsa düşük bayt alınır
- Senkron okuma `0x82`, senkron yazma `0x83`, PING `0x01`, okuma `0x02`, yazma `0x03`
- ⚠️ **Çok baytlı parametrelerin bayt sırası servo türüne göre değişir:** "potansiyometreli servolarda **big-endian** (yüksek bayt önce), manyetik enkoderli servolarda **little-endian** (düşük bayt önce)"

Üç ana nokta:

1. **Kilitlenmek şarttır, paket paket karar verilemez** — veri yolunda gürültü vardır, bir paketin parazitle `FD 00` gibi görünmesi ileri geri sıçramaya yol açar
2. **Yanıt aynı protokolle verilir** — yalnızca ayrıştırma değil, paket oluşturma da dallanmalıdır
3. **Yedek kilit açma** — servo markası değiştiğinde yazılımı yeniden yazmak gerekmez

Köle (slave) ID'si iki tarafta da **200**'dür; 15 servoyla (genellikle 1–15 numaralı) çakışmaz.

> Feetech STS'nin `Return Delay Time` değeri varsayılan olarak 0'dır ve kılavuzda "Not functional on STS" notu vardır —
> register etkisizdir, yanıt gecikmesini tamamen yazılım belirler.

## Kılıf standardı: tüm direnç/kondansatörler 0603

Tüm direnç ve kondansatörler **0603**, D2 **SOD-123** kullanır; 0402/SOD-323 kullanılmaz.

Gerekçe elle lehimleme değil — kartta LGA-14 kılıflı LSM6DSV16X olduğundan zaten sıcak hava istasyonu gerekir.
**Asıl gerekçe hata ayıklama dönemindeki rework'tür:** seri direnci 150 Ω'dan 33 Ω'a denemek, bir pull-up'ı sökmek, bir ayrıştırma kondansatörü eklemek;
0603 ile havya kullanarak birkaç saniyede değiştirilebilir. Doğrulanmamış ilk kartın birkaç kez değiştirilmesi kaçınılmazdır.

Bedeli: 11 bileşen yaklaşık 16 mm² daha fazla yer kaplar, bu kart alanının %2'sinden azdır. Üstelik bu 0603 değerlerinin hepsi JLCPCB'nin **temel kütüphanesindedir**
(10 kΩ `C25804` · 150 Ω `C22808` · 33 Ω `C23140` · 100 nF `C14663`), 0402'nin genişletilmiş kütüphanesinden de daha ucuza malzeme yüklemesi gerektirir.

> C6 (10 µF/25 V) 0805'te kalır; C5 (4,7 µF) ve C7 (10 µF) zaten 0603'tür.

## Veri hattı koruması (HAT'ın yaptığı gibi)

```
U3.6 (1Y) ──┬─ DXL_DATA ─┬── R5 10k → 3.3V
U3.5 (2A) ──┘            │
                         └── R6 150Ω ──┬── DXL_BUS ── J1.3 / J2.3
                                       │
                                    D2 5V1
                                       ⏚
```

| Bileşen | İşlevi |
|---|---|
| **R6 150 Ω** | Kaynak tarafı seri direnç. Kısa devre akımını sınırlar, kenarları yumuşatarak EMI'yi azaltır. 1 Mbps'de gecikme bit süresinin yaklaşık %3'ünü oluşturur |
| **D2 5V1** | Kenetleme (clamp). Katot `DXL_BUS`'a, anot toprağa bağlıdır |

**Pull-up tampon tarafında kalır** (R5, R6'dan önce): böylece veri yolu takılı olmasa bile `U3.5 (2A)` CMOS girişinin
belirli bir seviyesi olur, yüzmez. HAT'taki `R32` konumuyla aynıdır.

> Resmi HAT, `R33 150R + TH1 100R` seri toplam 250 Ω kullanır, ayrıca `D4 5V1` kenetleme diyodu vardır
> (`dynamixel.kicad_sch`). **D2, HAT'ın D4'ü ile aynı model, farklı kılıftır** — HAT'ta SOD-323 (`C151348`), bu kartta rework kolaylığı için SOD-123 (`C151588`).
> Bu kartta yalnızca 150 Ω kullanılır, çünkü HAT tarafında zaten 250 Ω vardır; veri yoluna çok fazla seri direnç koymak kenarları yavaşlatır.

## Üç aşırı gerilim savunma hattı

1. **F1** PPTC 200mA tutma / 24V — akımı sınırlar, kısa devreyi önler
2. **D1** TVS SMF12A — kenetler, servo geri EMK (back-EMF) sivri uçlarını önler
3. **U4** HT7533-1 30V dayanır — ilk ikisi devre dışı kalsa bile LDO'nun kendisi dayanır

## Yerleşim noktaları

- 2 katmanlı kart, 45 × 22mm, SMD bileşenlerin hepsi ön yüzde
- 3 konnektör (J1/J2/J3) aynı kenarda, geçmeli (THT)
- İki M2 montaj deliği, aralık 34mm (orijinal `banana_pcb_locker` ile uyumlu)
- C1/C2, U2'nin Vdd / Vdd_IO pinlerine bitişik, izler mümkün olduğunca kısa
- C4 (100nF) ve C5 (4,7µF), U1'in 4. pinine bitişik — ST DS12992 Fig.13 "pine mümkün olduğunca yakın veya PCB'nin arka yüzünde tam karşısına" der
- DXL_DATA izi kalın çekilir, SPI'dan uzak tutulur

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
