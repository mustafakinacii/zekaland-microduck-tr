# Donanıma giriş: kart kart anlatım

> Bu belge tek bir soruyu yanıtlar: **Microduck'un içinde kaç kart var ve her biri ne işe yarıyor.**
>
> Diğer iki belgeyle iş bölümü:
> [Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md) **çıkarım süreci ve kanıt kaynaklarıdır** (doğrulamak isteyenler için),
> [Donanım özellikleri hızlı başvuru](04-donanim-ozellikleri.md) **tek sayfalık özellik tablosudur** (konuyu zaten bilenlerin bakması için).
> Bu belge ise **giriş anlatımıdır**; projeye yeni başladığınız varsayılır.
>
> Tüm sonuçlar kendiniz tarafından yeniden doğrulanabilir — son bölüm,
> [Kendiniz doğrulayın: replika öncesi yapılacak beş kontrol](#9-kendiniz-doğrulayın-replika-öncesi-yapılacak-beş-kontrol),
> bunun nasıl yapılacağını anlatır.

---

## 1. Önce genel tablo: beş modül, yalnızca ikisi kendiniz yapılacak

```
                    ┌─────────────────────────────────────────┐
                    │  Baş (MJCF'deki jaw_soft katı gövdesi)   │
                    │                                          │
   MIPI CSI ────────┤  ④ IMX219 kamera + M12 lens              │
   (yaklaşık 13 mm, │        ↕ aynı katı gövde, arada eklem yok │
    boyundan geçmez)│  ① Radxa Zero 3W    ana kart             │
                    │        ↕ istif aralığı 7,3 mm, 40 pin    │
                    │  ② RPI Robot HAT    güç dağıtımı / ses / veri yolu │
                    │        └─ Stemma portu ──► ⑤ ToF modülü   │
                    │  hoparlör                                 │
                    └──────────────┬──────────────────────────┘
                                   │
                    ═══════════════╪══════ üç serbestlik dereceli boyundan geçer ══════
                     servo veri yolu│ pil besleme kablosu
                     (1 çift)       │ (+BATT)
                    ┌──────────────┴──────────────────────────┐
                    │  Gövde (trunk_base)                       │
                    │   iki adet hip_yaw XL330 — iç boşluk neredeyse dolu │
                    │   ③ imu_to_dxl kartı (servo veri yoluna bağlı)      │
                    └──────────────┬──────────────────────────┘
                                   │
                     NP-F550 pil ──┘ gövdenin arka alt kısmında dışarıda
                     71 mm uzunluğunun yaklaşık 40 mm'si kabuğun dışında,
                     iki adet power_support parçası tarafından dışarıdan sıkıştırılır
```

| # | Modül | Tek cümleyle | Nasıl temin edilir |
|---|---|---|---|
| ① | **Radxa Zero 3W** | Beyin. Linux, sinir ağı politikası ve görüntü işleme burada çalışır | 🛒 Satın alınır |
| ② | **RPI Robot HAT** | Güç dağıtım panosu + ses kartı + servo veri yolu arayüzü | 🏭 **Resmi olarak açık kaynak, kendiniz üretirsiniz** |
| ③ | **imu_to_dxl** | IMU'yu sahte bir servo gibi gösterir | ✏️ **Kendiniz çizmelisiniz** |
| ④ | **IMX219 kamera** | Gözler | 🛒 Satın alınır |
| ⑤ | **ToF modülü** | 8×8 bölgeli mesafe ölçümü, lidar değildir | 🛒 Satın alınır |

> ⚠️ **Sık yapılan üç yanlış anlama**
> 1. **Lidar yok.** ToF, çok bölgeli mesafe ölçüm modülüdür (4×4 veya 8×8 bölge); radar değildir.
> 2. **Ses ayrı bir modül değil.** Codec, yükselteç ve mikrofon HAT üzerindedir.
> 3. **Ana kart gövdede değil, baştadır.** En kolay karıştırılan nokta budur ve hangi uzunlukta flat kablo alacağınızı doğrudan etkiler.

---

## 2. ① Ana kart · Radxa Zero 3W

**Ne yapar**: Armbian Linux'u, Rust çalışma zamanı `robotd`'yi, ONNX politika çıkarımını ve görüntü işlemeyi çalıştırır.
Kısacası — **motorları sürmek dışındaki her şeyi o yapar**.

| Öğe | Değer |
|---|---|
| SoC | Rockchip **RK3566**, dört çekirdekli Cortex-A55 @1,6GHz |
| NPU | 0,8–1 TOPS INT8, düğüm `npu@fde40000`, **Armbian'da varsayılan olarak kapalıdır**, overlay yüklenmesi gerekir |
| Form | **65 × 30 mm**, Raspberry Pi Zero formunda, 40 pinli header |
| Sistem | Armbian **headless** imajı |

**Neden Raspberry Pi değil de bu kart**: Bu bir **piyasada satılan modüldür**, özel taşıyıcı kart değildir — bu çok önemlidir,
çünkü replika için ana kart üretmenize gerek olmadığı anlamına gelir. Aygıt ağacında `compatible = "radxa,zero-3w"` yazılıdır.

**40 pinden hangilerini kullanır** (resmi HAT şemasından çıkarılmıştır):

| Pin | Kullanım | Linux aygıtı |
|---|---|---|
| **GPIO14 / GPIO15** | **Dynamixel UART Tx / Rx** | `/dev/ttyS2` @ 1 Mbps |
| **GPIO02 / GPIO03** | I²C — IMU + ses + Stemma | `i2c3` @ 400 kHz |
| GPIO18 / 19 / 20 / 21 | Ses PCM Clk / FS / Din / Dout | `i2s3_2ch` |
| GPIO06 | Kapanma algılama (Switch off detection) | |
| GPIO22 | HAT üzerindeki BMI088'in kesme pini (**yazılım kullanmaz**) | |
| GPIO00 / 01 | HAT kimlik tanıma I²C'si (ayrılmış) | ⚠️ HAT bölümüne bakın |
| GPIO04/05, 08/09, 10/11 | Ek Stemma/QT I²C | |
| MIPI CSI | Kamera | |

**Hangi yapılandırma alınmalı**: 1G veya 2G, **eMMC'siz** çıplak kart; yanına 32 GB microSD kart, yalnızca resmi kanaldan. Gerçek denemeler ve gerekçeler için [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «Hangi yapılandırma alınmalı» bölümüne bakın.
Resmi kaynaklarda 1 GB bellek, 32 GB depolama yazar (eMMC olduğu belirtilmemiştir). (2026-10-12 düzeltmesi: daha önce yazılan «2G / 16G eMMC» gereksizdi.)

---

## 3. ② RPI Robot HAT — tek kart dört iş yapar

**Bu, resmi olarak tamamen açık kaynak olan tek karttır** ([`pollen-robotics/elec_RPI_Robot_HAT`](https://github.com/pollen-robotics/elec_RPI_Robot_HAT),
Apache-2.0; KiCad projesi + Gerber + BOM + yerleşim koordinatlarını içerir).

**Özellikler** (Gerber'den ölçülmüştür): 4 katmanlı kart, **65,0 × 30,9 mm**, köşe yuvarlatması R3,5, BOM 47 satır / 123 adet,
bunların 5 satırı 9 adet DNP (takılmaz), fiilen **113 konuma** parça yerleştirilir.

### İşlev bloğu 1: Güç dağıtımı

```
NP-F550 pil ──► +BATT ──┬──► servolar (doğrudan, düşürmeden)
  2S, 6,6–8,2V           │
                         └──► U9 AP63205 + L4 6,8µH ──► Q2 / U10 LM5050-1 ──► +5V
                                buck, 2A, Fsw 1,1MHz      ideal diyot + kapanma algılama │
                                                                                     ├─► ana kart 40 pin
                                                                                     ├─► PAM8406D yükselteç
                                                                                     └─► U3 XC6206P182 → +1V8 (codec)
```

**Burada sezgiye ters bir gerçek var: servolar 5V değil, pilin ham gerilimini yer.**

XL330'un resmi nominal değeri **3,7–6,0 V, önerilen 5,0 V**'tur; burada ise **6,6–8,2 V** verilir.
Kanıt tahmin değil, şemada doğrudan yazar: J13/J14/J3/J11 dört Dynamixel konektörünün güç pinleri hep `+BATT`'e bağlıdır,
yan nota «3A max» yazılıdır. Ayrıca **kartın tamamında yalnızca bir buck (U9) ve bir bobin (L4) vardır**; o 5V hattı ana kart içindir
— 2A'lik AP63205 de 15 XL330'u sürüklemez (tek bir servonun sıkışma akımı yaklaşık 1,5A'dir).

Ayrıntı için: [Gerilim gerçeği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/执行器选型.md#-电压真相xl330-被超压运行).

> `+3V3` ise tersine **ana kartın 40 pin üzerinden HAT'e verdiği** gerilimdir, HAT kendisi üretmez.

### İşlev bloğu 2: Servo veri yolu (yarı çift yönlü TTL)

Dynamixel / Feetech gibi veri yolu servolarının hepsi **tek telli yarı çift yönlüdür** — tek tel hem gönderir hem alır, yön kontrolüyle geçiş yapılır.

| Bileşen | Görevi |
|---|---|
| **U6 `SN74LVC1G125`** | Üç durumlu tampon, gönderme yönü |
| **U7 `SN74LVC1G126`** | Üç durumlu tampon, alma yönü |
| **U5 `74LVC1G08`** | VE kapısı, yön mantığında yer alır |
| **U8 `SIT3088E`** | RS-485 alıcı-verici (4P'li iki port için) |
| **TH1 100R** | Termistör, aşırı akım koruması |

Yönü `Dynamixel_dir` kontrol eder; resmi açıklamada **«Dynamixel_dir is based on Tx»** yazar — yön, gönderme sinyalinden otomatik türetilir.

**Dört konektör, iki tür**:

| Konum | Tür | Kim kullanır |
|---|---|---|
| **J13 / J14** | **JST EH 3P** (TTL) | **Microduck'un XL330'ları bu ikisine takılır**, TH1 üzerinden `+BATT`'e gider |
| J3 / J11 | JST EH 4P (RS-485) | U8 sürer, doğrudan `+BATT` |

> 💡 **JST EH 2,5 mm adımlıdır**, Feetech servo kablolarında yazan **5264 terminali** de 2,5 mm'dir.
> Çin piyasasında «5264» hemen hemen 2,5mm 3P'nin genel adıdır — büyük olasılıkla doğrudan takılır, ancak gövde mandalı ayrıntılarını
> eldeki parçayla doğrulamanız önerilir.

### İşlev bloğu 3: Ses

| Bileşen | Görevi | Adres |
|---|---|---|
| **U2 `TLV320AIC3104`** | Ses codec'i, I²S veri + I²C kontrol | i2c3 `0x18` |
| **U1 `PAM8406D`** | D sınıfı yükselteç | |
| **MK1** | Kart üzerindeki MEMS mikrofon (LCSC `C7587901`, resmi kaynak model vermemiştir) | |
| J1 | Wago vidasız klemens, **5W hoparlör** bağlanır | |
| J2 / J9 | Wago klemens, harici mikrofon bağlanır | |

Ses saati: MCLK 12 MHz sabit kristal, I²S sysclk 12,288 MHz (256 × 48 kHz).

> **Kayıt ve hoparlör istemiyorsanız bu bloğun tamamını atlayabilirsiniz.**

### İşlev bloğu 4: Sensör genişletme

- **J5–J8**: JST SH 1,0 mm 4P (Qwiic / Stemma QT) — ToF buraya takılır
- **U11 `BMI088`**: ⚠️ **Lehimlenmiş ama yazılım hiç kullanmıyor.** Aygıt ağacı yorumunda orijinal ifade `dormant`,
  `unused but still connected` şeklindedir. Dışarıda Microduck'un «iki IMU'su var» denmesi bunu kastediyor
- **U4 `CAT24C32`** EEPROM: ⚠️ **DNP, takılmaz** — bu yüzden bu kart **kendini tanıtan bir HAT değildir**,
  şemada «HAT Identification: I2C add. 0x50 / Standard Class HAT+» yazsa da

### Bu kart satın alınamıyor, ne yapılır

**Pollen tek başına satmaz**, yalnızca komple robotu satar. İki yol vardır:

1. **Aslına sadık üretim** — resmi Gerber + BOM + yerleşim koordinatlarıyla JLCPCB'ye sipariş verin. 4 katmanlı kart + SMT, birkaç yüz ¥'den başlar (¥ = Çin yuanı), asgari sipariş adedi vardır.
2. **Hazır modüllerle ikame** — ¥22'lik bir ST/SC yarı çift yönlü dönüştürücü kart + bir UBEC, «servo veri yolu» ve
   «güç dağıtımı» olmak üzere iki zorunlu işlevi karşılar, ToF doğrudan i2c3'e takılır. Bedeli kart üstü sesten vazgeçmektir. Bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «İki PCB» bölümü.

---

## 4. ③ imu_to_dxl — tüm elektronikteki en akıllı hamle

**Bu kart tek bir iş yapar: IMU'yu sahte bir servo gibi gösterir.**

**STM32G031F8P6 + LSM6DSV16X** (ST altı eksenli IMU) + yarı çift yönlü tampondan oluşur,
dışarıya servo veri yoluna bağlı bir bağımlı (slave) cihaz gibi görünür, **ID = 200**.

### Neden bu kadar dolambaçlı

Akla gelen yol, IMU'yu I²C veya SPI ile doğrudan ana karta bağlamaktır. Ama bunun bir sorunu var:

**IMU verisi ile servo verisi iki farklı yoldan gelir, örnekleme anları hizalanmaz.**

Politika 50 Hz çalışır; her tick'te hem «gövde duruşunu» hem «15 eklem açısını» aynı anda bilmesi gerekir.
IMU I²C'den, servolar UART'tan gelirse ikisi arasında birkaç milisaniyelik titreşim (jitter) olur — ve bu jitter politika girdisini doğrudan bozar.

Pollen'ın yaptığı, **IMU'ya da servo dilini konuşturmak**tır; böylece ana kart bir tick'te yalnızca **tek bir `sync_read`** gönderir
ve IMU duruşunu + 15 servo konumunu birlikte alır, **zaman damgaları doğal olarak hizalıdır**.

### Protokol ve register'lar

| Öğe | Değer |
|---|---|
| Protokol | Dynamixel **Protocol V2** |
| ID | **200** |
| Baud hızı | **1 Mbps** (EEPROM register'ı `baud_rate = 3`) |
| Başlangıç register'ı | **124** |
| Uzunluk | **12 bayt** |

12 baytlık düzen:

| Ofset | İçerik |
|---|---|
| `0..6` | gyro x/y/z, `i16` little-endian ham sayım, aralık **±500 dps**, **17,5 mdps/LSB** |
| `6..12` | SFLP kuaterniyon x/y/z, **IEEE yarım duyarlıklı fp16**; `w = √(1 − x² − y² − z²)` |

**Dikkat: `w` iletilmez** — birim kuaterniyon kısıtından ana taraf hesaplar, 2 bayt tasarruf edilir.

**SFLP**, LSM6DSV16X çipinin içindeki **donanım sensör füzyon bloğudur**, doğrudan oyun rotasyon kuaterniyonu çıkarır
— ana kartın duruş füzyonunu kendisinin çalıştırması gerekmez.

### Veri yolunda toplam 16 cihaz

```
ID  10 11 12 13 14   sağ bacak
ID  20 21 22 23 24   sol bacak
ID  30 31 32 33 34   boyun / baş / ağız
ID  200              imu_to_dxl kartı
```

15 servo + 1 IMU kartı = **16 cihaz, tek `sync_read` ile hepsi geri okunur**.

### Replika yaparken dikkat edilecekler

- **Protokol ve register düzeni tamamen çözüldü**, bakarak uygulanabilir ([Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md))
- **Konektör 2,5 mm adımlı 3P kullanın** (JST EH / 5264)
- **Giriş kapasitörünün dayanım gerilimi ≥25 V olmalı** — veri yolu dolu pilde 8,4 V'tur, 10 V sınıfı yeterli pay bırakmaz (MLCC'lerde DC öngerilim kaybı da vardır)
- **CS pinine pull-up ekleyin** — bir sonraki bölümdeki gerçek örneğe bakın
- **DATA hattına TVS ekleyin** — servoları enerjili takıp çıkarmak olağandır

---

## 5. ④ IMX219 kamera

MIPI CSI arayüzü, 8 megapiksel. Aygıt ağacı overlay'i `radxa-zero3-rpi-camera-v2` kullanır,
ISP yapılandırması `SENSOR = imx219`.

**İki tuzak:**

1. **180° ters montaj değil, 90° dönüktür.** Kodda şu yazar:
   `/// 90, because the head camera is mounted a quarter turn off, and this is the one place
   that fact is written down.` Bazı eski kaynaklar 180 yazar, o **alpha makinesinin** verisidir.
2. **Flat kabloyu en kısa olandan alın.** Kamera ile ana kart **aynı katı gövdededir, aralarında yaklaşık 13 mm vardır, arada eklem yoktur** —
   MIPI kablosu boyundan geçmez. 4–15 cm yeter, 30 cm almayın.

> ⚠️ Radxa resmi belgesi yalnızca «1x4-lane MIPI CSI» yazar, **pin sayısı ve adımı vermez**.
> Ancak kart Pi Zero formundadır ve CSI soketi Micro HDMI ile aynı kenardadır; **büyük olasılıkla dar ağızlı 22 pin 0,5 mm'dir**,
> genel IMX219 modülleri ise standart 15 pinle gelir — bir dönüştürücü kablo bulundurun (birkaç ¥).

---

## 6. ⑤ ToF modülü

**Lidar değildir.** ST FlightSense çok bölgeli mesafe ölçüm çipidir, **8×8 mesafe matrisi** çıkarır.

| Öğe | Değer |
|---|---|
| Model | **VL53L5CX veya VL53L8CX**, firmware revision ID'ye göre otomatik tanır (`0x02` = L5cx, `0x0C` = L8cx) |
| Arayüz | I²C, **i2c3 @ 400 kHz** üzerinde |
| Adres | **`0x29` veya `0x52`** (iki aday da denenir) |
| Fiziksel bağlantı | HAT üzerindeki **JST SH 1,0 mm 4P** (Qwiic / Stemma QT) |
| Kare hızı | 15 Hz |

> ⚠️ **VL53L0X almayın** — o **tek noktalı** mesafe ölçerdir, firmware tanımaz.
> **VL53L7CX de L8CX değildir** (L7, 90° görüş açılı başka bir çiptir).

---

## 7. Bir tick içinde neler olur

Politika 50 Hz çalışır, yani **her 20 ms'de bir tur**:

```
   ① tek sync_read                  ttyS2 @ 1 Mbps
      ├─ ID 200  → gyro + kuaterniyon ┐
      ├─ ID 10~14 → sağ bacak 5 açı    ├ 12 bayt × 16 cihaz
      ├─ ID 20~24 → sol bacak 5 açı    │  zaman damgaları doğal olarak hizalı
      └─ ID 30~34 → boyun/baş/ağız 5   ┘

   ② 61 boyutlu gözlem vektörü oluşturulur

   ③ ONNX politika çıkarımı (775 KiB'lık küçük ağ) → 14 boyutlu eylem

   ④ Gerilime uyum: scale × (7.4 / ölçülen pil gerilimi EMA)
      — pil 8,4V'tan 6,5V'a düşünce aynı PWM'in torku çok değişir, telafi edilmezse politika sapar

   ⑤ Tek sync_write ile 14 hedef konum gönderilir
```

Yan hatta ayrıca şunlar çalışır: **i2c3** üzerinde ToF (15 Hz) ve ses codec'i, **MIPI CSI** üzerinde kamera.

> ⚠️ **20 ms bütçesi çok dar ve bu yalnızca Feetech'in sorunu değil.**
> Resmi kaynak kodda şu yazar: XL330 fabrika ayarı `return_delay_time = 250`, yani **her cihaz için 500 µs dönüş (turnaround) gecikmesi**,
> «Across 16 devices that is **8 ms per tick — 40% of a 20 ms budget**».
> Resmi çözüm bu register'a **0 yazmaktır**.
> Hangi servoya geçilirse geçilsin bu adım yeniden yapılmalı ve gerçekten ölçülmelidir.

---

## 8. Feetech yolunu seçerseniz neler değişir

Birçok kişi (bu depo dahil) XL330 yerine Feetech servo kullanmayı değerlendiriyor. Etkiler ciddiyet sırasına göre:

| Etki | Açıklama |
|---|---|
| 🔴 **Resmi 9 ONNX politikasının büyük olasılıkla geçersiz kalması** | Servo değişti; tork eğrisi, kütle, hatta redüksiyon oranı bile farklı olabilir. **Yeniden eğitim şart** (CUDA GPU veya HF jobs gerekir) |
| 🟡 **Veri yolu zamanlaması mutlaka ölçülmeli** | Feetech kendi STS/SCS komut setini kullanır (`0x82 SYNC READ` dahil), paket biçimi farklıdır. **Ama mutlaka daha yavaş olduğunu varsaymayın** — resmi Dynamixel yolunda da cihaz başına dönüş gecikmesi vardır (yukarıya bakın). Elinize geçince ilk iş karşılaştırma testini çalıştırmaktır, yanında bir **FE-URT-1 programlama/test kartı** bulundurun |
| 🟡 **`imu_to_dxl`'nin yeniden konumlandırılması gerekir** | Veri yolu protokolü değişti; bu kart ya Feetech bağımlı cihazını taklit edecek şekilde değiştirilmeli ya da «veri yoluna bağlama» tasarımından vazgeçilip IMU SPI ile doğrudan bağlanmalı. **Öneri: donanım aynı kalsın, firmware çift protokollü olsun** — ikisinin fiziksel katmanı tamamen aynıdır (yarı çift yönlü tek tel TTL / 1 Mbps / 3 kablo), fark **paket biçimi** ve **fabrika varsayılanlarındadır**, bkz. [Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md) belgesindeki «Feetech STS/SCS protokol karşılaştırması» |
| 🟢 **Gerilim açısından daha uygun** | Feetech HD-1910 doğal olarak 5–8,4 V çalışır, XL330 gibi aşırı gerilimle çalıştırmaya gerek yoktur |

---

## 9. Kendiniz doğrulayın: replika öncesi yapılacak beş kontrol

**Bu bölüm yukarıdakilerin hepsinden daha önemlidir.**

Açık kaynak projelerin belgeleri eskir, hata içerir; yapay zekâ üretimi şemalarda bu daha da geçerlidir. Aşağıdakiler, bu depoda
pratikte biriken doğrulama adımlarıdır — her biri gerçek bir başarısızlığa karşılık gelir.

### 1. Pin tanımları: veri sayfasındaki pin tablosunu tek tek karşılaştırın

**Gerçek örnek:** Bu depoya `imu_to_dxl` için bir şema PR'ı geldi. Çizim eksiksiz görünüyordu ama
LSM6DSV16X'in pinlerini yanlış bağlamıştı — **ST DS13510 Rev 1 Table 1** (sayfa 10) ile karşılaştırınca şunlar görüldü:

| Pin | Kılavuzdaki tanım | PR'da çizilen |
|---|---|---|
| **12** | **CS** (çip seçimi) | ❌ kaymış |
| **13** | **SCL** (SPI saati) | ❌ kaymış |
| **14** | **SDA** (SPI verisi) | ❌ kaymış |
| **2 / 3** | **SDx / SCx yardımcı arayüz**, kullanılmadığında kılavuz **GND'ye bağlanmasını** ister | ❌ ana arayüz sanılmış |

Bu kart yapılsaydı **çalışmayacaktı**. Bunu fark etmek için tek şey yeterliydi: **veri sayfasını açıp pin tablosuna gidip satır satır karşılaştırmak**.

> **Veri sayfasına bakmadan şema çizmek, hiç çizmemek gibidir.** Bu cümlenin istisnası yoktur.

### 2. Gerilim payı: her kapasitörün dayanım gerilimi ile gerçek veri yolu gerilimi

Aynı PR'da giriş kapasitörü **10 V** olarak işaretlenmişti, veri yolu ise dolu pilde **8,4 V**. Pay varmış gibi görünür, ama:
- MLCC'lerde **DC öngerilim etkisi** vardır; 10 V sınıfı bir MLCC'ye 8,4 V uygulandığında gerçek kapasitans yarıdan fazla düşebilir
- Pilde ve motor ters EMF'sinde tepe gerilimler olur

**Kural: dayanım gerilimi çalışma geriliminin en az 2 katı olmalı.** 8,4 V'luk veri yolu için 25 V kullanın.

### 3. Güç açılış durumu: mod seçme pinlerinin açılış anındaki seviyesi

LSM6DSV16X'in CS pini seviyesi **güç açılışında SPI mı I²C mi kullanılacağını belirler**. CS askıda bırakılırsa
açılış anında belirsizdir — bazen çalışır, bazen çalışmaz; bulunması en zor hata türü budur.

**3V3'e 10 kΩ'luk bir pull-up ekleyin**, SPI modunu kilitleyin.

### 4. ERC çalıştırın ve 0 hata 0 uyarıya kadar götürün

KiCad komut satırıyla çalıştırılabilir:

```bash
kicad-cli sch erc --output erc.rpt your.kicad_sch
```

Yaygın gerçek sorunlar: güç pininde sürücü kaynak yok (`PWR_FLAG` eksik), iki Power output çakışıyor,
pin koordinatı bağlantı ızgarasında değil (bağlanmış görünür ama aslında bağlı değildir).

### 5. Çapraz doğrulama: yazılım kaynak kodundaki adres ve register'lar ile donanım

Microduck'un yazılımı açık kaynaktır, **kod = özellik şartnamesidir**. Donanımdaki her adresin kodda bir karşılığı bulunabilir:

| Donanım | Yazılımdaki kanıt |
|---|---|
| Ses codec'i `0x18` | `deploy/audio/i2c3-pihat.dts` |
| ToF `0x29` / `0x52` | `tof/src/main.rs` içindeki `ADDRESS_CANDIDATES` |
| IMU kartı ID 200 | `duck-control/src/model.rs` içindeki `IMU_DXL_ID` |
| Servo ID dağılımı | aynı yerde, `JOINT_IDS` |
| i2c3 400 kHz | `i2c3-pihat.dts` içindeki `clock-frequency` |
| BMI088 kullanılmıyor | `i2c3-pihat.dts` yorumu: `dormant`, `unused but still connected` |

**Uyuşmuyorsa taraflardan biri yanlıştır.**

---

## Ek: Bu belgedeki tüm sonuçların kaynakları

| Sonuç | Kaynak |
|---|---|
| Kartların nereye takıldığı | `robot_walk.xml:235` (HAT), `:247` (ana kart), ikisi de `jaw_soft` body'sinde |
| 40 pin ataması | `ASE01187-C1_elec_RPI_Robot_HAT_SCH.pdf` GPIO tablosu |
| HAT kart özellikleri | Gerber `Edge_Cuts.gm1` ölçümü; BOM.csv 47 satır / POS.csv 117 satır |
| Servoların `+BATT`'e bağlanması | Şemadaki Dynamixel sayfası (4/6), yan not «3A max» |
| Yalnızca bir buck | BOM.csv'nin tamamında yalnızca L4 bobini var (FB1/2/3 ferrit boncuktur) |
| 12 baytlık register düzeni | `robotd` kaynak kodu, bkz. [Donanım çözümünün tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md) |
| Kameranın 90° dönük olması | `mediad/src/main.rs:82` |
| 8 ms dönüş gecikmesi | `duck-control/src/model.rs:84-86` |
| LSM6DSV16X pinleri | **ST DS13510 Rev 1, Table 1, sayfa 10** |

> Bu belge, resmi olarak yayımlanan MJCF modeli, STL ağları, açık kaynak donanım projesi ve çalışma zamanı kaynak kodundan çıkarılmıştır,
> **gerçek donanımla doğrulanmamıştır**. Hata bulursanız issue açın.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
