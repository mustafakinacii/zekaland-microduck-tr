# Microduck donanım özellikleri hızlı başvuru

> **Depoda dört liste ve bir baskı açıklaması var, her biri ayrı konuyu kapsar:**
>
> | Belge | Ne kapsar | Ne kapsamaz |
> |---|---|---|
> | [BOM](02-malzeme-listesi-bom.md) | **Ana tablo**: tüm malzemeler, adetler (MJCF'deki geom referanslarından sayılmıştır), maliyet mertebesi, henüz çözülmemiş boşluklar | Tam olarak nereden alınacağı, nasıl basılacağı |
> | [Elektronik satın alma listesi](06-elektronik-satin-alma.md) | Elektronik parçaların **nereden alınacağı**: ana kart / kamera / ToF / güç / iki PCB / kablolar, Taobao gerçek linkleri + kaçınılacak tuzaklar | Adet dayanağı, mekanik parçalar |
> | [Mekanik satın alma listesi](05-mekanik-satin-alma.md) | Mekanik parçaların **nereden alınacağı**: rulman / bağlantı elemanları / sarf malzemeleri, Taobao gerçek linkleri | Elektronik parçalar |
> | **Donanım özellikleri hızlı başvuru** (bu belge) | **Parametreler**: arayüzler, gerilim, protokol, yazılım tarafında uyulması gereken değerler | Fiyat ve mağaza |
> | [Baskı ve CAD](12-baski-ve-cad.md) | **Baskı girişi**: CAD deposunda sürüm, malzeme ve adet seçimi | Satın alma |
>
> Montajda kullanılan parça numaraları ve vida eşleşmeleri [CAD deposunda](https://github.com/fanhao375/microduck-replica-cad#装配-bom) bulunur.


> 📘 Yeni başlayanlar önce [Donanıma giriş](03-donanim-baslangic.md) belgesine baksın (kart kart anlatım); tam çıkarım için [Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md).

> Tek sayfalık sürüm. Tam çıkarım süreci ve kanıtlar [硬件方案逆向.md](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md) belgesinde.
> Tüm veriler `pollen-robotics/microduck` deposunun kaynak kodundan, aygıt ağaçlarından ve yapılandırma dosyalarından gelir — **kod = özellik şartnamesidir**.

**Tek cümleyle**: Radxa Zero 3W (RK3566) Armbian çalıştırır + 1 Mbps TTL seri veri yoluna 15
Dynamixel XL330 bağlıdır + iki adet özel kart.

---

## Sistem blok diyagramı

```
                ┌──────────────────────────────┐
                │   Radxa Zero 3W (RK3566)     │  65 × 30 mm
                │   Armbian · çekirdek 6.1.115 │  Pi Zero formu
                └──┬────────┬─────────┬────────┘
      /dev/ttyS2   │        │ 40-pin  │ MIPI CSI
      1 Mbps TTL   │        │  I2C3   │
    ┌──────────────┘        │ 400kHz  └── IMX219 kamera (90° dönük)
    │                       │
    │              ┌────────▼─────────────────┐
    │              │  Pollen RPI Robot HAT    │  65×30mm özel kart (açık kaynak)
    │              │   ├ TLV320AIC3104  0x18  │  ses codec'i
    │              │   ├ BMI088   0x19/0x68   │  lehimli ama kullanılmıyor
    │              │   └ Stemma J5 → ToF 0x29 │  VL53L5CX/L8CX
    │              │  pil bu karttan beslenir  │
    │              └──────────────────────────┘
    │
════╪══════════ Dynamixel veri yolu · Protocol V2 · 1 Mbps ══════════
    │
    ├── 15 × XL330   ID sol bacak 20-24 / boyun-baş-ağız 30-34 / sağ bacak 10-14
    └── imu_to_dxl v2 kartı   ID 200   ← LSM6DSV16X
```

**Temel tasarım**: Her şey tek bir veri yoluyla çözülür. IMU, I2C kullanmaz; Dynamixel bağımlı cihazı olarak servo veri yoluna bağlanır
ve 15 servoyla **aynı `sync_read`** içinde okunur. Pil gerilimi için de yakıt göstergesi yoktur,
doğrudan servoların bildirdiği kendi besleme gerilimi okunur.

---

## Ana kart

| Öğe | Değer |
|---|---|
| Modül | **Radxa Zero 3W** — piyasada satılan modül, **özel taşıyıcı kart değildir** |
| SoC | **RK3566** (4× Cortex-A55 + Mali-G52 + NPU) |
| Boyut | 65 × 30 mm, Pi Zero formu, 40 pinli Raspberry Pi uyumlu header |
| Sistem | **Armbian** (Debian tabanlı), vendor çekirdek 6.1.115 |
| Politika çıkarımı | ONNX Runtime ≥1.23 (1.28.0 yüklenir), `dlopen` ile yüklenir |
| NPU çıkarımı | rknn-toolkit2 — **Armbian'da varsayılan olarak kapalıdır**, overlay yazılıp yeniden başlatılması gerekir |

> Dayanak: aygıt ağacı `compatible = "radxa,zero-3w", "rockchip,rk3566"`;
> depoda "radxa" 182 kez geçer.

### Söylentiler neden Raspberry Pi diyor

1. Özel kartın adı **"RPI Robot HAT"**
2. Pi Zero formu + 40 pinli Raspberry Pi uyumlu header
3. Kamera **Raspberry Pi Camera v2** (IMX219)
4. **Prototip aşamasında gerçekten Raspberry Pi Zero 2W kullanılmıştı** — `robotd.toml` yorumu: 50 Hz kontrol döngüsü
   *"is inherited from the prototype, where it was chosen on a Raspberry Pi Zero 2W"*

Öncülü Open Duck Mini v2 **hâlâ Raspberry Pi Zero 2W kullanıyor**, çünkü görüntü işleme ve WebRTC yayını yapmıyor.

### Neden MCU değil de Linux SoC şart

Aynı anda şunlar çalışmalı: 50Hz ONNX politika çıkarımı, 720p30 H.264 donanım kodlama + WebRTC yayını,
NPU nesne algılama, GStreamer tıkanıklık kontrolü (bir çekirdeğin %7,6'sı), Bluetooth kumanda + telefon uygulaması + WiFi.
**STM32 / ESP32 bunu yapamaz.**

---

## Aktüatörler ve veri yolu

| Öğe | Değer |
|---|---|
| Motor | **Dynamixel XL330 × 15** (her biri yaklaşık 18 g) |
| Elektrik katmanı | **Tek telli yarı çift yönlü TTL** (3 kablo: veri + VDD + GND), 3,3V |
| Protokol | **Dynamixel Protocol V2** |
| Hız | **1 Mbps** (EEPROM `baud_rate = 3`) |
| Port | `/dev/ttyS2` = RK3566 **UART2, M0 pinmux** |
| Bağlı cihazlar | **16 adet**: 15 servo + 1 IMU kartı |
| Kontrol döngüsü | **50 Hz**, tek `sync_read` 16 cihazın hepsini kapsar, register 124–136 |
| Rust kütüphanesi | [`rustypot`](https://github.com/pollen-robotics/rustypot) |

> ❗ **RS232 de değil, RS485 de değil.** RS485 iki telli diferansiyeldir, yalnızca Dynamixel'in XM/XH serisi kullanır.
> XL330 tek telli yarı çift yönlü TTL'dir. Depoda `rs485|rs232|direction pin` aramasında **sıfır sonuç** çıkar —
> kodda yön kontrolü GPIO'su yok, yön geçişini donanım otomatik yön devresi yapar (HAT kartında).

### Servo ID dağılımı

```
Sol bacak     20 21 22 23 24    hip_yaw / hip_roll / hip_pitch / knee / ankle
Boyun-baş-ağız 30 31 32 33 34   neck_pitch / head_pitch / head_yaw / head_roll / mouth
Sağ bacak     10 11 12 13 14    (sol bacağın aynası)
IMU kartı     200
```

**15. servo ağızdır (ID 34, indeks 9).** Tüm politikalar `obs[1,61] → act[1,14]` biçimindedir,
eylem vektörü **bu indeksi atlar** — ağız üst katman mantığıyla kontrol edilir, politika kontrol etmez.

### Veri yolu güvenilirliği (resmi ölçüm)

| Gösterge | Değer | Kaynak |
|---|---|---|
| Paket kaybı | **dakikada yaklaşık 8 ≈ %0,27** | *"Measured on a bench robot at ~8 drops a minute"* |
| Resmi nitelendirme | *"One dropped Dynamixel transaction is **ordinary**"* | `robotd/src/main.rs` |
| Belirti | Rastgele küçük sarsıntı (okuma kaybı politikanın bir adım durup hold duruşuna dönmesine yol açar) | aynı yer |
| Tolerans | `COAST_TICKS = 3` son iyi örnekle 60ms boyunca süzülür | aynı yer |
| Tolerans üst sınırı | `max_consecutive_errors = 10` | `robotd.toml` |
| Döngü kararlılığı | `missed=3` / 15022 tick, 50,0 Hz korunur | `roadmap.md` |
| IMU verisi bayatlaması | Özel bir `StaleImuTracker` var, yorumda *"Known to happen"* yazar | `bus.rs` |

Veri yolu kullanım oranı tahmini **yaklaşık %25** (tick başına yaklaşık 500 bayt ÷ 1 Mbps ÷ 20ms) —
**darboğaz bant genişliği değil, sinyal bütünlüğü ve tek hata noktasıdır**: tek uçlu 3,3V sinyal, papatya zinciri bağlı 15 servo,
dinamik bükülen boyundan geçen kablo demeti, hemen yanında motor PWM gürültü kaynağı.

---

## İki Pollen özel kartı (biri açık kaynak, biri kendiniz çizmeli)

### ① `imu_to_dxl` v2 — çok az bileşen, en kolay kendiniz yapılabilen

| Öğe | Değer |
|---|---|
| IMU çipi | **LSM6DSV16X** (ST 6 eksen, SFLP donanım duruş füzyon bloğu içerir) |
| Arayüz | **Dynamixel veri yolu** (I2C değil) |
| Veri yolu ID'si | **200** |
| Register adresi | **124** |
| Kontrol döngüsünde okuma | 12 bayt |
| Tam tanı bloğu | 20 bayt (ham ivme, örnek sayacı, durum bayrakları da dahil) |

**12 baytlık blok düzeni**

| Bayt | İçerik |
|---|---|
| `0..6` | gyro x/y/z, `i16` little-endian, ±500 dps, **17,5 mdps/LSB** |
| `6..12` | SFLP kuaterniyon x/y/z, **IEEE fp16**; `w = √(1 − x² − y² − z²)` |

**Kendiniz yapmak için gerekenler**: LSM6DSV16X + Dynamixel V2 bağımlı cihazı olarak çalışacak küçük bir MCU
(STM32G0/G4, CH32V203, ESP32 olur) + yarı çift yönlü TTL alıcı-verici, besleme veri yolundan alınır.

### ② Pollen RPI Robot HAT — resmi olarak açık kaynak, doğrudan ürettirilebilir

**65,0 × 30,9 mm, kart kalınlığı 1,0 mm, 4 katmanlı kart** (resmi KiCad ve Gerber'den alınmıştır, bkz. [BOM](02-malzeme-listesi-bom.md)). STL ağından ölçülen 65,02 × 30,02 × 0,84 simülasyon yaklaşığıdır, **sipariş verirken kullanmayın**. 40 pinli header'a takılır.

| Bileşen | I2C adresi | Açıklama |
|---|---|---|
| **TLV320AIC3104** | `0x18` | TI ses codec'i, I2S veri + I2C kontrol |
| **BMI088** | `0x19` / `0x68` | **Lehimli ama kullanılmıyor** (yorumun orijinali "dormant") |
| **ToF** | `0x29` | Kart üzerinde değil, **Stemma J5** üzerinden harici bağlanır |

- I2C: 40 pinin **pin 3 / pin 5**'i (`GPIO1_A0`=SDA, `GPIO1_A1`=SCL), **400 kHz**
- Pull-up: **tek çift 10k, R12/R13**
- Ses saati: MCLK **12 MHz**, I2S sysclk **12,288 MHz** (256×48kHz)
- Mikrofon **Mic3R**'a bağlıdır (mono sağ PGA), diğer tüm girişler kapalıdır
- **Robotun iç beslemesi bu karttan geçer**

---

## Sensörler

| Tür | Model | Arayüz | Not |
|---|---|---|---|
| IMU | **LSM6DSV16X** | Dynamixel veri yolu ID 200 | Çip içi SFLP kuaterniyon üretir, ana kart füzyon çalıştırmaz |
| ToF | **VL53L5CX / VL53L8CX** | I2C `0x29` @ i2c3 | 15 Hz, çok bölgeli mesafe ölçümü |
| Kamera | **IMX219** (Raspberry Pi Camera v2) | MIPI CSI, I2C `0x10` | **90° dönük**, bkz. [Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md#七传感器) |

- Kamera sensörü 1920×1080@30 moduna sabitlenmiştir (açılış varsayılan modunun 21 fps sınırından kaçınmak için),
  ISP ile ölçeklenerek çıkar, varsayılan 720p30 @ 2 Mb/s
- Kodlama **Rockchip MPP donanım kodlayıcısı** → WebRTC
- Yatay görüş açısı (HFOV) yaklaşık 62°

---

## Güç ve pil

| Öğe | Değer |
|---|---|
| Pil | **Sony NP-F550** (L serisi kamera pili). ⚠️ Resmi ağ adı `np_f970` yanıltıcı, ölçülen boyut F550'dir |
| Yapılandırma | **2S Li-ion**, nominal 7,2 V |
| Dolu (yük altında) | **8,2 V** |
| Boş (yük altında) | **6,6 V** |
| Yakıt göstergesi | **Yok** |
| ADC | **Yok** |

> Yorumun orijinali: *"There is no fuel gauge and no ADC. The only measurement available is
> what the servos report as their own supply."*

**Gerilim doğrudan Dynamixel protokolüyle servoların bildirdiği kendi besleme geriliminden okunur** — yani «veri yolundan görülen pil»,
yük altında düşer, boştayken geri yükselir. Bu yüzden 6,6–8,2 V **yük altında kullanılabilir aralıktır**, hücre kimyasının gerilim aralığı değildir.

Pil EMA'sı (yaklaşık 10 saniyelik zaman sabiti) 6,6 V'a düşerse → **otomatik olarak düzgünce oturur ve kapanır**.

> 💡 Replika için kolaylık: **hiçbir pil izleme devresi tasarlamanıza gerek yok.**

---

## Tüm arayüzlere genel bakış

| Arayüz | Kullanım | Parametreler |
|---|---|---|
| **UART2** (`ttyS2`) | 15 servo + IMU kartı | 1 Mbps, TTL yarı çift yönlü |
| **I2C3** (pin 3/5, M0) | Ses codec'i / ToF / (kullanılmayan BMI088) | 400 kHz |
| **I2S3** | Ses verisi | MCLK 12 MHz, sysclk 12,288 MHz |
| **MIPI CSI** | IMX219 kamera | I2C kontrol `0x10` |
| Bluetooth | Kumanda (`padd`), telefon uygulaması (`btd`) | kart üstü |
| WiFi | WebRTC yayını, ağ yapılandırma (`configd`) | kart üstü |
| USB-C | Besleme + maskrom ile imaj yazma | **PD müzakeresi overlay yüzünden feda edilir** |

---

## Yazılım tarafında uyulması gereken parametreler

| Parametre | Değer | Açıklama |
|---|---|---|
| Kontrol döngüsü | **50 Hz** | Raspberry Pi prototipinden miras, **Radxa üzerinde hiç yeniden doğrulanmadı** |
| Politika arayüzü | `obs[1,61] → act[1,14]` | Yükleme sırasında doğrulanır, 51 boyutlu eski sürüm reddedilir |
| `action_scale` | 0,9 (yürüme) / 0,8 (paten) | |
| Konum P kazancı | **200** | Ayakta dururken ×0,8 |
| Eylem alçak geçiren filtre | head **0,5** / legs **0,7** | **Eğitimle aynı olmalı**, aksi halde aktarım bozulur |
| Gerilime uyum | Varsayılan kapalı | `scale × (7.4 / ölçülen EMA)`, 6,0–9,5 V arasına sıkıştırılır |

---

## Replika listesi: satın alınabilenler ve kendiniz yapılacaklar

| Parça | Durum | Not |
|---|---|---|
| Radxa Zero 3W | ✅ Doğrudan satın alın | Piyasada satılan modül |
| Dynamixel XL330 × 15 | ✅ Doğrudan satın alın | **Maliyetin büyük kısmı, $359–€629** (kanallar arası fiyat farkı çok büyük, bkz. [BOM](02-malzeme-listesi-bom.md)) |
| **NP-F550** pil + yuva | ✅ Doğrudan satın alın | Genel kamera aksesuarı. **F970 almayın** |
| Raspberry Pi Camera v2 (IMX219) | ✅ Doğrudan satın alın | |
| VL53L8CX modülü | ✅ Doğrudan satın alın | Stemma/Qwiic hazır stokta |
| **`imu_to_dxl` kartı** | 🔧 **Kendiniz çizin** | Protokol tamamen çözüldü, yalnızca 3 çeşit bileşen |
| **HAT kartı** | ✅ Resmi Gerber'i indirip ürettirin | 4 katmanlı kart. Ses ve hoparlör istemiyorsanız tamamen atlanabilir, ama **yarı çift yönlü yön devresi ayrı bir dönüştürücü kartla sağlanmalıdır**, bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «İki PCB» bölümü |
| Kontrol yazılımı | ✅ Resmi Apache-2.0 | Aynı ana kartla **doğrudan çalıştırılabilir** |
| Politika | ✅ Resmi 9 ONNX | Donanım aynı kalırsa kullanılabilir |

> 💰 **Maliyet hatırlatması**: Yalnızca 15 XL330 **$359–€629** tutar (ROBOTIS uluslararası sitede $23,90'dan başlar, Avrupa'da vergiyle en çok €41,95),
> bu, komple robotun **$399** satış fiyatını çoktan aşar. $399 ölçekli üretim fiyatıdır.

---

## Mutlaka düşülecek üç tuzak

1. **Armbian varsayılan olarak UART2 üzerinde giriş konsolu çalıştırır** — `serial-getty@ttyS2`'nin `agetty`'si
   seri portu işgal eder. `systemctl mask serial-getty@ttyS2` yapılmalıdır.
   Resmi ekip bunu `fuser -v /dev/ttyS2` ile buldu.

2. **i2c3 FUSB302 ile pin kavgası yapar** — RK3566'nın i2c3'ü orijinal DTB'de USB-C PD denetleyicisi için M1 pinmux üzerinde çalışır;
   pin 3/5'in M0'ını kullanmak için fusb302 devre dışı bırakılmalı, **PD müzakeresi kaybedilir**.
   Neyse ki FUSB302 açılışta varsayılan olarak CC'yi Rd gösterir, sıradan 5V şarj hâlâ kullanılabilir.

3. **NPU varsayılan olarak kapalıdır** — Armbian fabrika ayarında açmaz, rknn modeli çalıştırmak için overlay yazılıp yeniden başlatılması gerekir.

---

## Sonuç

**Bu donanımda çoğaltılamayacak hiçbir parça yok.** Ana kart piyasada satılan modüldür; iki Pollen özel kartından
**HAT kartı resmi olarak tamamen açık kaynaktır** (KiCad + Gerber + BOM + yerleşim koordinatları, indirip ürettirilebilir),
kendiniz çizmeniz gereken tek kart `imu_to_dxl`'dir — o da çok az bileşenlidir ve protokolü tamamen çözülmüştür.

Gerçek engel teknik değil, **maliyettir** (15 XL330 komple robotun satış fiyatından pahalıdır).

> Veri kaynakları: `duck-control/src/{model,imu,bus}.rs`, `robotd/src/main.rs`,
> `deploy/robotd.toml`, `deploy/audio/*.dts`, `deploy/overlays/*.dts`,
> `tof/src/*.rs`, `mediad/src/*.rs`, `docs/design/robotd-design.md`,
> `docs/project/{media-bringup,roadmap}.md`

---

## Resmi özellikler vs bu deponun tersine mühendisliği (çapraz doğrulama)

Resmi taraf 2026-08-27'de bazı özellikleri yayımladı. Aşağıdaki tablo **resmi olarak duyurulanları** ile **bu depoda kaynak kodundan tersine mühendislikle çıkarılanları**
madde madde karşılaştırır — iki taraf birbirini doğrular, birbirinde olmayan bilgiyi de tamamlar.

| Öğe | Resmi duyuru | Bu depoda tersine mühendislikle çıkan | Sonuç |
|---|---|---|---|
| SoC | RK3566, dört çekirdekli A55 @1,8GHz, Mali-G52, NPU **0,8 TOPS** | RK3566 (aygıt ağacı `compatible`) | ✅ Uyumlu |
| **Ana kart modülü** | **Açıklanmadı** | **Radxa Zero 3W** | 🔍 **Yalnızca tersine mühendislikte var** |
| RAM / depolama | **1 GB bellek / 32 GB depolama** (eMMC olduğu belirtilmedi) | Kaynak kodda doğrulayan yok | 🆕 **Yalnızca resmi tarafta var**.<br>Replika için 1G veya 2G eMMC'siz sürüm + 32 GB microSD yeterli, bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «Hangi yapılandırma alınmalı» bölümü (2026-10-12 düzeltmesi) |
| Pil | **NP-F550, 2600 mAh, yaklaşık 1 saat çalışma** | NP-F550, 2S, 8,2 V dolu / 6,6 V boş | ✅ Uyumlu |
| ToF | **8 × 8** LiDAR | VL53L5CX / VL53L8CX @ `0x29` | ✅ Bu seri tam olarak 8×8'dir |
| Kamera | Göstergeli ön kamera | **IMX219** (Pi Cam v2), I2C `0x10`, **90° dönük** | 🔍 Tersine mühendislik daha ayrıntılı |
| **IMU** | **2 adet (gövde + baş)** | LSM6DSV16X **kullanımda**; BMI088 kaynakta **dormant / unused** olarak işaretli | ⚠️ **Çelişki, aşağıya bakın** |
| Motor | 15 DOF, tutabilen eklemli gaga | 15 × Dynamixel XL330, tam ID tablosuyla | ✅ Uyumlu |
| Boyut ağırlık | Yükseklik 25 cm, genişlik **14 cm**, < 800 g | Ölçülen **144 × 141 × 264 mm**, **737,2 g** | ✅ Uyumlu |
| **NFC** | **Çift anten** | Kaynak kodda **hiç geçmiyor** | 🆕 **Yalnızca resmi tarafta var** |
| Ses | Mikrofon + hoparlör | TLV320AIC3104 @ `0x18`, mikrofon Mic3R'a bağlı | 🔍 Tersine mühendislik daha ayrıntılı |
| **Ana veri yolu** | **Açıklanmadı** | TTL yarı çift yönlü 1 Mbps, `/dev/ttyS2`, Protocol V2 | 🔍 **Yalnızca tersine mühendislikte var** |
| Bağlantı | Wi-Fi, Bluetooth | Aynı (Radxa kart üstü) | ✅ Uyumlu |

### ⚠️ Çelişki: Resmi taraf 2 IMU diyor, yazılım yalnızca 1 tanesini kullanıyor

Resmi özellikler **"2× IMUs (body and head)"** yazıyor, ama kaynak kodunda:

- **Kullanımda olan yalnızca LSM6DSV16X** — `imu.rs`'nin başında *"One IMU, one code path"* yazar
- HAT kartındaki **BMI088**, aygıt ağacı yorumunda **"dormant"**,
  **"(unused but still connected)"** olarak işaretlenmiştir

**Sonuç: İkinci IMU fiziksel olarak kartta lehimli, ama fabrika yazılımı onu kullanmıyor.** Replikada doğrudan atlanabilir.

---

## Açık kaynak durumu: resmi tutum (2026-08 güncellemesi)

> CNX Software haberinin orijinal ifadesi:
> *"While the Microduck's software stack is open source, nothing was said about the
> mechanical and hardware design files, and **Pollen Robotics told the press not to
> refer to the robot as 'open-source hardware' (for now)**."*

**Bu ifade dikkatle yorumlanmalı.** Resmi tarafın reddettiği, robotun tamamına «açık kaynak donanım» **etiketini** yapıştırmaktır;
hiçbir kartın yayımlanmadığı anlamına gelmez — aslında **RPI Robot HAT kartı tamamen açık kaynaktır**
([`elec_RPI_Robot_HAT`](https://github.com/pollen-robotics/elec_RPI_Robot_HAT), Apache-2.0,
KiCad projesi, Gerber, BOM, yerleşim koordinatları dahil). Yayımlanmayanlar `imu_to_dxl` kartı,
düzenlenebilir mekanik CAD, komple BOM ve montaj belgeleridir.

Şu **"(for now)"** bir kapı aralık bırakıyor, ama takvim vermiyor.

> 2026-09-03 düzeltmesi: bu belgede daha önce yazılan «donanımın açık kaynak olmaması resmi tarafın bilerek çizdiği çizgidir» ifadesi fazla güçlüydü, düzeltildi.

### Dış doğrulama: biri bağımsız olarak aynı ana kart sonucuna ulaştı

2026-08-31'de X'te [@tspy](https://x.com/tspy/status/2094249218735300630) bir
«Microduck fiziksel mimari dökümü» yayımladı (169 beğeni), bağımsız olarak şunları sıraladı:

> Aktüatör 15 × Dynamixel XL330 · ana kart **Radxa ZERO 3W / Rockchip RK3566** ·
> 1 GB RAM + 32 GB · çift 6 eksenli IMU · 8×8 ToF · ileri bakan kamera · 2× NFC anteni ·
> pil NP-F550 · kontrol frekansı 50 Hz

**Bu deponun tersine mühendislik sonuçlarıyla tamamen aynıdır**, en kritik madde olan **Radxa Zero 3W** dahil —
iki bağımsız yol aynı yanıta çıktı, güvenilirlik büyük ölçüde arttı.

> 📌 **Dikkat: 2026-08-31 itibarıyla piyasada hiçbir gerçek ürün yok** (Noel'den önce sevk edilecek).
> Bu yüzden şu anki tüm «teardown»lar **açık yazılım ve özelliklere dayalı çıkarımdır**, fiziksel söküm değildir.
> Bu deponun derinliği (I2C adresleri, register düzeni, 12 baytlık veri bloğu, veri yolu protokolü)
> özellik listesinden bir kat ötedir, kaynağı Rust kodunu şartname gibi okumaktır.

Aynı tartışma dizisinde @tspy'ye maliyet sorulduğunda verdiği yanıt da bu depoyla uyumludur: **«Maliyet doğrudan satın almaktan daha yüksek görünüyor»**.

### Topluluğun sormaya devam ettiği üç issue (2026-08-31 itibarıyla resmi taraf hiçbirine yanıt vermedi)

| Issue | İstek |
|---|---|
| [#175](https://github.com/pollen-robotics/microduck/issues/175) | **STEP dosyası** isteniyor — STL'de normal bilgisi yok, eğri yüzeyler çokgen bloklar gibi görünüyor |
| [#173](https://github.com/pollen-robotics/microduck/issues/173) | **3D baskı kaynak dosyaları** isteniyor |
| [#174](https://github.com/pollen-robotics/microduck/issues/174) | Pilin yerinde şarj edilip edilemeyeceğini soruyor ve doğrudan **güç kartı şemasının açık kaynak planında olup olmadığını** soruyor |

Yaklaşık 10 issue incelendi, **Pollen üyelerinden hiçbiri yanıt vermedi**, ama depo hâlâ her gün güncelleniyor.

> Bu da bu deponun yaptığı işin değerli olduğunu gösteriyor: topluluk içinde şu an MJCF'den montaj çizimini tersine çıkaran,
> Rust kaynak kodundan elektronik çözümü sistematik biçimde çıkaran kimse yok.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
