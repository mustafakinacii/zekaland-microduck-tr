# Elektronik Satın Alma Listesi (Çin içi / Taobao)

> **Depoda dört liste ve bir baskı notu var; her biri ayrı işi kapsar:**
>
> | Belge | Ne kapsar | Ne kapsamaz |
> |---|---|---|
> | [BOM](02-malzeme-listesi-bom.md) | **Ana tablo**: tüm malzemeler, adetler (MJCF içindeki geom referanslarından sayılmıştır), maliyet büyüklüğü, henüz çözülmemiş boşluklar | Tam olarak hangi satıcıdan alınacağı, nasıl basılacağı |
> | **Elektronik satın alma listesi** (bu belge) | Elektronik parçaların **nereden alınacağı**: ana kart / kamera / ToF / güç / iki PCB / kablolar; gerçek Taobao linkleri + tuzaklar | Adetlerin dayanağı, mekanik parçalar |
> | [Mekanik satın alma listesi](05-mekanik-satin-alma.md) | Mekanik parçaların **nereden alınacağı**: rulman / bağlantı elemanları / sarf malzemeleri; gerçek Taobao linkleri | Elektronik parçalar |
> | [Donanım özellikleri hızlı başvuru](04-donanim-ozellikleri.md) | **Parametreler**: arayüzler, gerilimler, protokoller, yazılım tarafında uyumlu olması gereken değerler | Fiyat ve mağaza |
> | [Baskı ve CAD](12-baski-ve-cad.md) | **Baskı girişi**: CAD deposunda sürüm, malzeme ve adet seçimi | Satın alma |
>
> Montaj için parça numaraları ve vida eşleşmeleri [CAD deposunda](https://github.com/fanhao375/microduck-replica-cad#装配-bom) bulunur.


> **Anlık görüntü tarihi: 2026-09-04.** Fiyatlar ve satış adetleri değişir, linkler geçersiz hale gelebilir; sipariş vermeden önce fiyatı kendiniz kontrol edin. (¥ = Çin yuanı)
> **2026-10-12 düzeltmesi**: Ana kart yapılandırması için sonuç «1G veya 2G, eMMC'siz + microSD» olarak değiştirildi ve yalnızca resmi kanallar önerilmektedir; bkz. [Hangi yapılandırma alınmalı](#hangi-yapılandırma-alınmalı).
> Mekanik parçalar (rulman / bağlantı elemanları / sarf malzemeleri) için bkz. [Mekanik satın alma listesi](05-mekanik-satin-alma.md).
>
> Bu liste herhangi bir tavsiye veya onay içermez; yalnızca arama sonuçlarının kaydıdır. Mağaza bilgileri (satış adedi, mağaza yaşı) veri çekildiği andaki gösterilen değerlerdir.

---

## Önce şunu netleştirin: kartlar nereye takılıyor

Bu nokta hangi özellikte kablo alacağınızı doğrudan etkiler ve **kolayca yanlış anlaşılır**:

```
Baş (MJCF içindeki jaw_soft gövdesi)
 ├── Raspberry Pi formunda ana kart   ← ana kart başın içinde, gövdede değil
 ├── RPI Robot HAT                    ← ana kartın 7,3 mm üzerine istiflenir
 ├── IMX219 kamera + M12 lens          ← ana kart merkezine yaklaşık 13 mm, aynı gövde, arada eklem yok
 └── Hoparlör

Gövde (trunk_base)
 ├── İki adet hip_yaw XL330           ← iç boşluğu neredeyse tamamen bu ikisi doldurur
 ├── trunk_base taban plakası
 └── NP-F pil — gövdenin arka alt kısmına dışarıdan takılır, 71 mm uzunluğun
      yaklaşık 40 mm'si kabuğun dışında kalır,
      iki adet power_support parçası tarafından dışarıdan sıkıştırılır

Üç serbestlik dereceli boyundan geçenler: servo veri yolu + pilden gelen +BATT besleme hattı
```

**Kanıt**: `robot_walk.xml:235` `mesh="elec_rpi_robot_hat_pcb"`, `:247` `mesh="pcb__raspberry_pi_zero_2_w"`
İki geom da `jaw_soft` body'si içindedir; iki adet 65×30 kartın X/Y'si tam hizalıdır, Z aralığı 7,3 mm'dir; bu standart bir Pi + HAT istiflemesidir.

> ⚠️ **Bu yüzden MIPI flex kablosu boyundan geçmez, en kısasını almak yeterlidir.** Asıl kablo yorulması riski **servo veri yolu ve güç hatlarının boyundan geçmesindedir**
> — bunlar akım taşıyan hatlardır ve risk sinyal flex kablosundan daha fazla dikkate değerdir. Üstelik resmi proje **kablo güzergâhına dair hiçbir bilgi yayımlamamıştır**.

---

## Bir · Ana Kart · Radxa Zero 3W

### Hangi yapılandırma alınmalı

> 📌 **Düzeltme (2026-10-12)**: Buradaki özgün sonuç «2G / 16G eMMC» idi; **bu öneri yanlıştı ve herkesin fazla para harcamasına yol açtı**.
> Resmi belgelerde yalnızca **1 GB bellek, 32 GB depolama** yazıyor, eMMC olduğu belirtilmiyor; kendi ilk makinemizde
> **2 GB, eMMC'siz, microSD kartlı** çıplak kart kullanıldı ve kissqy'nin tam sistemi çalışırken ölçülen kullanım yalnızca 175 MB bellek, 3,3 GB depolama oldu.
> Eski öneriye göre 2G/16G alanlar sorunsuz kullanabilir, yalnızca fazla para ödemişlerdir; değiştirmeye gerek yok.

**Sonuç: 1G veya 2G «eMMC'siz» çıplak kart, yanında 32 GB microSD kart.**

| Yapılandırma | Yeterli mi | Açıklama |
|---|---|---|
| **1G / eMMC'siz** + microSD | ✅ Yeterli | Resmi ile aynı seviye (resmi: 1 GB bellek, 32 GB depolama) |
| **2G / eMMC'siz** + microSD | ✅ Daha rahat | İlk makinemiz bu; ileride kamera açıp algılama modeli çalıştırmak için daha rahat |
| eMMC'li olanlar (8G / 16G / 32G…) | Çalışır, gereksiz | Bir kademe daha pahalı, depolama için bir kart yeter |

**Ölçüm** (2026-10-12, ilk makine: 2G / eMMC'siz / 64 GB microSD, kissqy'nin tüm sistemi + 50 Hz kontrol döngüsü + Bluetooth gamepad çalışırken):
kullanılan bellek **175 MB** (kullanılabilir 1,79 GB), kullanılan depolama **3,3 GB**. O sırada kamera bağlı değildi, kamera servisi açık değildi;
açıldığında GStreamer ve algılama modeli biraz daha bellek tüketir, ancak 1 GB'ın payı yine de var.

**microSD kart**: Köklü marka (SanDisk, Samsung vb.), A1 veya A2 etiketli 32 GB kart alın. Markasız ucuz kartlardan kaçının:
sistem diskinde sorun çıktığında belirtiler çoğu kez başka bir arızaya benzer ve teşhis etmek çok zordur.

Aşağıda depolama ve belleğin ayrı ayrı nasıl tahmin edildiği sürecini görebilirsiniz; sonuç yukarıdaki ölçümle değiştirilmiştir, yalnızca başvuru için bırakılmıştır:

**Depolama tarafı**

| Kalem | Boyut | Dayanak |
|---|---|---|
| Armbian headless rootfs | ~2 GB | `deploy/README.md:144` headless imaj olduğunu doğrular; **2 GB harici deneyim değeridir, depoda dayanağı yoktur** |
| **ONNX Runtime** | **~20 MB** | `docs/design/robotd-design.md:420` aslı: «ONNX Runtime is a board prerequisite … **~20 MB** in every artifact would enlarge every update for nothing» — **kart seviyesinde önceden kurulur, sürüm paketinde yer almaz** |
| **GStreamer yığını** (`mediad` kullanır) | **~100 MB** | `docs/design/updater-design.md:901` «the GStreamer stack for `mediad`, which is **around 100 MB of apt**» |
| RKNN çalışma zamanı `.so` | Bilinmiyor | Depoda dayanağı yok, sayı uydurulmaz |
| daemon çıktısı + saklanan bir eski sürüm | büyüklük mertebesi 10¹ MB | `Cargo.toml:79` «**model artifacts will dwarf a few MB of binary**»; `keep_previous = 1` |
| **9 adet hareket politikası ONNX** — her biri **793.685 B ≈ 775 KiB** | **7 MB** | Ölçüm. `alpha_stand` / `alpha_walking` / `alpha_sitstand` / `alpha_ground_pick` / `ball_kick_left` / `ball_kick_right` / `roller` / `roller_crouch` / `roulade` |
| `duck_detect.onnx` | 10,0 MB | Ölçüm 10.477.940 B |
| `pet_detect.onnx` | 19 KB | Ölçüm 20.201 B |
| journald üst sınırı `SystemMaxUse=200M` | **Varsayılan yapılandırmada diski kullanmaz** | `/var/log` bir zram aygıtıdır (`deploy/README.md:14/402/437`). Ancak README:454 bir geri çekilme yolu verir: `armbian-zram-config` kapatılırsa günlükler eMMC'ye yazılır |
| **Toplam** | **≈ 3 – 4 GB** | |

→ Başlangıçta 3–4 GB tahmin edildi, **ölçülen 3,3 GB**. 32 GB'lık bir microSD kart fazlasıyla yeterlidir, **eMMC gerekmez**.

> 💡 **Yükseltme mekanizması çift rootfs gerektirmez.** Ancak **buna A/B demeyin** — resmi `docs/design/updater-design.md:46`
> bunu özellikle açıklığa kavuşturur: «Update granularity | **Application-level (not A/B image)** | Only daemon + model
> change; OS is static. A/B (RAUC/Mender) would be over-engineering.»
> Gerçekte olan: **sürüm dizini + `current` sembolik bağlantısının atomik geçişi (`rename(2)`) + sağlık denetimi + geri alma**;
> `keep_previous = 1` yalnızca bir eski daemon'u fazladan saklar. (`updater.toml` içindeki `tag_prefix` değeri gerçekte `daemon-v`'dir.)

**Bellek tarafı**

| Kalem | Kullanım |
|---|---|
| Armbian headless | ~250 MB (harici deneyim değeri) |
| robotd + ONNX Runtime + RKNN | Küçük — politika modelleri yalnızca 775 KiB/adet |
| Kamera / GStreamer tamponları + `duck_detect` | ⚠️ **`duck_detect.onnx` NPU'da değil CPU'da çalışır** (`robotd.toml:324` «a `.rknn` runs on the NPU, an `.onnx` on the CPU»; NPU sürümü `.rknn` depoda yok). Ayrıca **RK3566'nın NPU'su ile CPU'su aynı DDR'yi paylaşır, ayrı ekran belleği yoktur** |
| ⚠️ `/var/log` zram aygıtı — **RAM yer, disk değil** | Yer ayırmak gerekir |

→ Başlangıçta «1 GB çalışır ama sıkışık» tahmin edildi, **ölçümde tüm sistem yalnızca 175 MB kullandı**. 1 GB yeterli, 2 GB daha rahat, daha büyüğü gereksiz.

> **Resmi yapılandırma**: Pollen'ın basın bilgi paketi «**1 GB RAM, 32 GB storage**» yazıyor; eMMC mi SD kart mı olduğu belirtilmiyor
> (bu belge daha önce «1 GB / 32 GB eMMC» yazmıştı, eMMC fazladan eklenmişti, düzeltildi). `microduck/` kaynak kodunda da kart SKU'su bulunamadı.

### Kanal — yalnızca resmi kanallar, önce stok var mı bakın

Radxa resmi sitesindeki [bayi sayfası](https://radxa.com/distributors) **Çin anakarası resmi kanallarını** listeler:

| Kanal | Giriş |
|---|---|
| ALLNET (安联新创) Taobao mağazası | [allnetchina.taobao.com](https://allnetchina.taobao.com) |
| Radxa resmi Taobao mağazası | Taobao'da «瑞莎 Radxa» aratın, resmi mağazayı seçin |
| Radxa resmi JD mağazası | JD'de «瑞莎 Radxa» aratın, resmi mağazayı seçin |

Yurt dışı resmi kanallar arasında [ALLNET resmi sitesi](https://shop.allnetchina.cn/products/copy-of-radxa-zero-3w), [Arace](https://arace.tech/) vb. bulunur.
**Önce bu mağazalarda stok olup olmadığına bakın, «eMMC'siz» sürümü seçin**; stok yoksa stoğun gelmesini bekleyin, hızlı olsun diye küçük mağazalarda birkaç kat fazla ödemeyin.

ALLNET resmi sitesindeki gerçek fiyatlar (2026-09-04 anlık görüntüsü, USD, yaklaşık ¥7,2/$):

| Yapılandırma | Fiyat | Yaklaşık karşılığı |
|---|---|---|
| **1G / eMMC'siz** | **$18** | **¥130** ⭐ |
| 1G / 8G eMMC | $22 | ¥158 |
| 2G / 16G eMMC | $32,90 | ¥237 |
| 4G / 32G eMMC | $50 | ¥360 |
| 8G / 32G eMMC | $70 | ¥504 |

(Pinli sürüm +$1. ALLNET 8G/64G seçeneği satmıyor. Bu anlık görüntüde «2G / eMMC'siz» yoktu, ancak böyle bir yapılandırma vardır, ilk makinemiz de budur; fiyat için resmi mağazaya bakın.)

Resmi olmayan küçük mağazaların o andaki fiyatları (olumsuz örnek):

| Mağaza | Yapılandırma | Fiyat | Link |
|---|---|---|---|
| findboard旗舰店 (findboard amiral mağaza) | 8G+64G «Paket 6» (kamera/güç adaptörü/32G kart/HDMI kablosu/soğutucu dahil) | **¥1469** | [tmall 752703346347](https://detail.tmall.com/item.htm?id=752703346347) |
| findboard旗舰店 | 8G+64G çıplak kart | ¥1149 | Aynı |
| 鹭控自动化工控 (Lukong otomasyon endüstriyel kontrol) | Belirtilmemiş (pazarlık) | ¥690 | [taobao 1044607515575](https://item.taobao.com/item.htm?id=1044607515575) |

**3–6 kat fazla fiyat, üstelik hepsi eMMC'li büyük yapılandırmalar.** Yalnızca yukarıdaki resmi kanalları kullanın.

### Paketleri almayın

| Aksesuar | Değer mi |
|---|---|
| Kamera (Radxa'nın kendi IMX219'u, tek başına ¥129,99) | ❌ Genel IMX219 ¥32,8'e var |
| 32G microSD | ⚠️ eMMC'siz sürümde sistem diski olarak şarttır; ancak paketteki kart iyi olmayabilir, A1/A2 markalı kartı ayrıca alın |
| Güç adaptörü | ❌ Makine pille çalışır, yalnızca masa üstü hata ayıklamada gerekir |
| microHDMI kablosu | ❌ Microduck headless çalışır |
| Soğutucu | ✅ Faydalı, ancak ayrıca [¥19,99](https://item.taobao.com/item.htm?id=788387010174)'ya alın |

---

## İki · Ana Kart Alternatifi · Lichuang Taishanpai (立创·泰山派) (değerlendirildi, **sığmıyor**)

Aynı **RK3566**, Çin içinde tedarik istikrarlı, sık sorulur. **Ancak sonuç: kullanılamaz.**

**Gerçek fiyat** (listeleme sayfasındaki ¥22 / ¥45 / ¥195 hepsi en düşük SKU ile yem atmadır; «2G+16G tek ana kart» SKU'su seçildikten sonraki gerçek fiyat):

| Kanal | Yapılandırma | Gerçek fiyat | Link |
|---|---|---|---|
| RK开发板 (RK geliştirme kartı, 9 yıllık mağaza) | 2G+16G tek ana kart | **¥428** (+¥10 kargo) | [taobao 1017038620459](https://item.taobao.com/item.htm?id=1017038620459) |
| 电子元件shop (elektronik bileşen shop, 12 yıllık mağaza, 46 ödeme) | 2G+16G tek kart | **¥480,8** (ücretsiz kargo) | [taobao 800894187326](https://item.taobao.com/item.htm?id=800894187326) |
| Lichuang Mall resmi (立创商城官方) | 2G+16G | **¥580** (eski ¥228, DDR fiyat artışı nedeniyle yükseltildi) | [item.szlcsc.com/20558171](https://item.szlcsc.com/20558171.html) |
| **Karşılaştırma: Radxa Zero 3W** | 1G / eMMC'siz (ayrıca microSD) | **≈¥130** | Resmi kanal |

**Dört madde de aleyhine:**

| | Taishanpai | Radxa Zero 3W |
|---|---|---|
| **Sığar mı** | ❌ **Sığmaz** — ana kart **başın içine** takılır, baş kabuğu toplamda yalnızca 58,8 × 91,8 × 122,7 mm'dir,<br>ana kart yuvası X yönünde yalnızca 30 mm'dir, üstünde ayrıca bir HAT bastırır. Taishanpai **70 × 45**, yeri yok | ✅ 65 × 30, tam olarak bu yuvaya göre tasarlandı |
| 2G+16G gerçek fiyat | ¥428–580 | **≈¥237** |
| **Armbian imajı** | ❌ Resmi dağıtım betiklerinin tamamı Radxa'nın Armbian imajına dayanır<br>(`overlay_prefix=rk35xx`, `armbian-zram-config`, netplan, güncelleyici), yeniden yazılması gerekir | ✅ Doğrudan kullanılır |
| **Aygıt ağacı overlay'i** | ❌ Hepsi yeniden yazılmalı — 40 pinlik pin çoklaması **kart seviyesinde bir eşlemedir**.<br>Microduck `/dev/ttyS2`, `i2c3 @400kHz`, `i2s3_2ch`, MIPI CSI'ye bağımlıdır | ✅ Hazır |
| **HAT mekanik uyumu** | ❌ 70×45 vs Pi Zero 65×30, pin konumları uymaz, **HAT'ın yeniden çizilmesi gerekir** | ✅ İkisi de Pi Zero formunda |
| SoC / NPU / rknn | ✅ Aynı RK3566, çekirdek ve NPU çalışmaları yeniden kullanılabilir | ✅ |
| WiFi | AP6212 (WiFi4 / BT4.x) | WiFi6 / BT5.4 |

**Ancak açık kaynak materyalleri saklamaya değer** (kartı almadan da indirilebilir): tam şematik + PCB **JLCPCB EasyEDA (JLC EDA) formatındadır**,
aynı RK3566'nın güç ağacı, DDR yönlendirmesi, AP6212 bağlantısı doğrudan açılıp incelenebilir —
`imu_to_dxl` çizilirken ya da ileride HAT yeniden çizilirken hazır, yüksek kaliteli bir referanstır.

- [Lichuang açık kaynak donanım platformu · Taishanpai projesi](https://oshwhub.com/li-chuang-kai-fa-ban/li-chuang-tai-shan-pai-kai-fa-ban)
- [Doküman indirme merkezi](https://openkits-wiki.easyeda.com/zh-hans/tspi-rk3566/download-center.html)

---

## Üç · Kamera · IMX219 (MIPI CSI)

Kamera ana kartla **aynı baştadır, aynı gövdededir**; `setup-board.sh:748` içinde kullanılan overlay
`radxa-zero3-rpi-camera-v2`, `setup-rkaiq.sh:147` `SENSOR = imx219`.

> ⚠️ **180° ters montaj değil, 90° döndürülmüştür.** `mediad/src/main.rs:82`:
> «**90, because the head camera is mounted a quarter turn off**, and this is the one place
> that fact is written down.» `docs/project/media-bringup.md:472` içindeki 180°, **alpha makinenin** eskimiş verisidir.

| Mağaza | Fiyat | Satış | Link |
|---|---|---|---|
| DECXIN旗舰店 (DECXIN amiral mağaza) | ¥32,8 | 100+ | [tmall 775872575316](https://detail.tmall.com/item.htm?id=775872575316) |
| 德创信摄像头 (Dechuangxin kamera) | ¥32,8 | 27 | [taobao 771618094322](https://item.taobao.com/item.htm?id=771618094322) |
| 盛成威科技 (Shengchengwei Teknoloji, 11 yıllık mağaza) | ¥38 | 84 | [taobao 596521821696](https://item.taobao.com/item.htm?id=596521821696) |
| 亚博智能 (Yabo Akıllı, 14 yıllık mağaza, teknik dokümanlı) | ¥44 | 15 | [taobao 709927597121](https://item.taobao.com/item.htm?id=709927597121) |
| 树莓派零售商 (Raspberry Pi perakendecisi, ücretsiz kargo, 48 saatte gönderim) | ¥68 | 100+ | [taobao 760446989892](https://item.taobao.com/item.htm?id=760446989892) |
| findboard旗舰店 (Radxa resmi sürümü) | ¥129,99 | 9 | [tmall 874789708454](https://detail.tmall.com/item.htm?id=874789708454) |

### Flex kablo: 15 pin ⇄ 22 pin dönüşümü (gerekebilir, **en kısasını alın**)

⚠️ **Resmi el kitabı arayüz özelliklerini vermiyor.** `Radxa ZERO 3W Product Brief` Rev 1.10 §6.3 aslı yalnızca şu:

> "The Radxa ZERO 3W is equipped with a **1x4-lane MIPI CSI** connector for camera integration.
> This interface is designed to be backward-compatible with standard industrial camera peripherals."

Pin sayısı yok, aralık yok. Ancak Zero 3W bir Raspberry Pi Zero formundadır; CSI soketi Micro HDMI ile aynı kenardadır ve yerleşimi Pi Zero ile aynıdır,
**büyük olasılıkla dar 22 pin 0,5 mm**'dir; oysa genel IMX219 modüllerinin yanında verilen kablo **standart 15 pin 1,0 mm**'dir.

> 💡 **15 cm hatta daha kısası yeterlidir** — kamera ile ana kart aynı gövdededir, aralarında yaklaşık 13 mm vardır,
> flex kablo **boyundan geçmez**. 30 cm almayın.

| Mağaza | Açıklama | Uzunluk | Fiyat | Link |
|---|---|---|---|---|
| **汇博视捷科技工厂店 (Huibo Shijie Teknoloji fabrika mağazası)** | 15'ten 22 Pin'e altın parmaklı FPC, **4 cm kısa sürüm** | 4cm | **¥1,88** | [taobao 654755002992](https://item.taobao.com/item.htm?id=654755002992) |
| 摄像头生产厂家 (Kamera üreticisi, 11 yıllık mağaza) | Pi Zero Camera Cable | 16cm | ¥1,88 | [taobao 819560127110](https://item.taobao.com/item.htm?id=819560127110) |
| **Tytion (15 yıllık mağaza)** | Başlıkta açıkça **15P 1.0 → 22P 0.5** yazıyor | 15cm | ¥2,5 | [taobao 678057486394](https://item.taobao.com/item.htm?id=678057486394) |
| 树莓派精品销售商 (Raspberry Pi seçkin satıcı, 13 yıllık mağaza, ücretsiz kargo) | Resmi kablo, 135/200/300/500 mm seçenekli | Çoklu | ¥5,8 | [taobao 784739658496](https://item.taobao.com/item.htm?id=784739658496) |

---

## Dört · ToF Mesafe Ölçümü · VL53L5CX veya VL53L8CX (8×8 çok bölgeli)

**Yazılım yalnızca bu iki yongayı tanır, üçüncüsü yoktur.** `tof/src/sensor.rs` içinde tek bir match vardır, revision ID'ye göre ayrılır:

```rust
match revision_id {
    0x0C => L8cx,
    0x02 => L5cx,       // 官方注释：「大多数在用的鸭子装的就是这颗」
    _    => Unknown,    // 没有驱动，直接报错退出
}
```

(Kod yorumları: «0x02: resmi yorum — "kullanımdaki ördeklerin çoğunda takılı olan bu yongadır"»; «_ : sürücü yok, doğrudan hata verip çıkar».)

Tanınmadığında daemon'un asıl mesajı `… which is neither a VL53L5CX nor a VL53L8CX` olur ve çıkış yapar.
Yazılımda yalnızca iki ULD sürücü shim'i derlenmiştir (`Driver::L5` / `Driver::L8`), diğer yongaların sürücüsü yoktur, ID değiştirerek de kandırılamaz.

I²C adres adayları **`0x29` veya `0x52`**'dir (`tof/src/main.rs:107`; 0x52, resmi prototipte IMU'ya yer açmak için kaydırılan adrestir,
adresi kaydırılmış sensör gücü kesilse de 0x52'de kalır), i2c3 üzerinde @ 400 kHz bağlıdır. HAT üzerinde **JST SH 1,0 mm 4P** (Qwiic / Stemma QT) arayüzü J5–J8 ile bağlanır.

### Kart boyutu yüz kabuğuna sığıp sığmayacağını belirler

Aynı derecede kullanılabilir yongalarda bile modül kartı boyutu iki kattan fazla farklıdır. Yüz kabuğunun (`face_part`) ToF açıklığı belirli bir kart boyutuna göre yapılmıştır, kart boyutu değişirse çizimin değişmesi gerekir:

| Modül | Yonga | Kart boyutu | Ağırlık | Referans fiyat | Sonuç |
|---|---|---|---|---|---|
| **VL53L5X V2 modülü** | VL53L5CX | **15,8 × 10 mm** | 1,15 g | ¥44,5 (kapak camlı ¥49,5) | ✅ **İlk tercih**: yazılım tanır, kart en küçük, üstelik en ucuz |
| VL53L8CX modülü (Çin'de yaygın kart tipi) | VL53L8CX | 33,4 × 10,2 mm | 1,7 g | ¥75 | ⚠️ **Önerilmez**: yongada sorun yok, ancak bu kart 33,4 mm'dir, yüz kabuğuna sığmaz (2026-09-20 ölçümü). Daha kısa bir L8CX kartı bulamazsanız ya da kabuğu değiştirmeyi göze almazsanız |
| VL53L7CX modülü | VL53L7CX | 26 × 11,5 mm | 1,3 g | ¥75 | ❌ **Almayın**: yazılım doğrudan hata verip çıkar |

**Baskı parçasındaki delik aralığı 20 mm'dir, yalnızca L5CX kartı uyar** (meslektaş ölçümü 2026-09-20: baskı parçasında delik aralığı 20 mm,
elimizdeki L8CX kartında 28 mm, takılamadı). Delikler iki uçtaki kulakların merkezindedir, uçtan yaklaşık 2,3~2,4 mm uzaktadır,
bu nedenle `24.7 − 2×2.35 ≈ 20`, `33.4 − 2×2.7 ≈ 28`. Resmi yüz kabuğu zaten L5CX'e göre tasarlanmıştır,
bu da yazılım kaynak kodundaki şu yorumla örtüşür: «kullanımdaki ördeklerin çoğunda takılı olan L5CX yongasıdır».

**Seçim sırası: önce yongayı yazılım tanıyor mu bakın (yalnızca L5CX / L8CX), sonra delik aralığı uyuyor mu bakın (20 mm gerekir).**
Tersine önce boyuta bakarsanız bizim gibi, kısa olsun diye L7CX alıp iade edip baştan başlamak zorunda kalırsınız.

«Kapak camı» sensörün üstüne takılan siyah ışık siperidir (tek başına ¥5), çapraz karışmayı önler, takılıp takılmayacağı kabuk tasarımına bağlıdır.

| Mağaza | Model | Fiyat | Satış | Link |
|---|---|---|---|---|
| 森科源电子 (Senkeyuan Elektronik) | VL53L8CX | ¥70 | 1 | [taobao 1025775539663](https://item.taobao.com/item.htm?id=1025775539663) |
| 深圳市渱雯电子 (Shenzhen Zhuwen Elektronik) | VL53L8CX | ¥74,98 | 0 | [taobao 977907234039](https://item.taobao.com/item.htm?id=977907234039) |
| 都会明武电子 (Duhui Mingwu Elektronik, ücretsiz kargo, 20 bin müşteri geri dönüşü) | VL53L7CX / **L8CX** | ¥75 | 100+ | [taobao 942554129061](https://item.taobao.com/item.htm?id=942554129061) |
| 深圳优信电子 (Shenzhen Youxin Elektronik, teknik dokümanlı, ücretsiz kargo, kurumsal fatura) | VL53L8CX | ¥78,5 | 31 | [taobao 967946231167](https://item.taobao.com/item.htm?id=967946231167) |
| 勇泰发电子 (Yongtaifa Elektronik, 11 yıllık mağaza, ücretsiz kargo) | VL53L8CX | ¥84,8 | 14 | [taobao 939165242465](https://item.taobao.com/item.htm?id=939165242465) |
| 归吉星旗舰店 (Guijixing amiral mağaza) | ST resmi P-NUCLEO-53L8A1 değerlendirme kiti | ¥98 | 1 | [tmall 725486284128](https://detail.tmall.com/item.htm?id=725486284128) |

> ⚠️ **VL53L0X almayın.** «VL53L5CX» aramasında çıkanların büyük çoğunluğu **VL53L0X — tek noktalı mesafe ölçer**, yazılım tanımaz.
> `TOF050C / 200C / 400C` serisi de (¥2,79'dan başlayan) tek noktalı L0X / L1X'tir; ucuz ve kart küçük, ancak yazılım yine tanımaz.
>
> ⚠️ **VL53L7CX, L8CX'in kısa versiyonu değildir.** L7, 90° geniş görüş açılı başka bir yongadır, revision ID uymaz,
> yazılım doğrudan hata verip çıkar. 2026-09-20'de L8CX'in 33,4 mm'lik uzun kartından kaçınmak için L7CX alındı ve iade edilmek zorunda kaldı.
> Kısa ve kullanılabilir olan **L5CX**'tir (15,8 × 10 mm). Bazı ilanlar L5 / L7 / L8'i tek ilanda karıştırır, **SKU seçerken dikkatle bakın**.
>
> Başlığında aynı anda «79GHz radar sensörü» de yazan ¥8'lik bir «VL53L5CX» gördük — anahtar kelime doldurma tuzağı;
> ayrıca ¥5'lik bir «VL53L5X V2» gördük, içine girince **kapak camı** çıktı, modül değil.
>
> Gelince nasıl doğrulanır: kartı bağlayıp `tof` daemon'unun yazdığı modele bakın ya da doğrudan revision ID'yi okuyun; **yalnızca `0x02` (L5CX)
> ve `0x0C` (L8CX) doğrudur**.

---

## Beş · Güç

| Parça | Mağaza | Fiyat | Satış | Link |
|---|---|---|---|---|
| **NP-F pil yuvası (güç almak için)** | 腾壶旗舰店 (Tenghu amiral mağaza) | ¥17,8 | 99 | [tmall 658975825526](https://detail.tmall.com/item.htm?id=658975825526) |
| **NP-F güç taban kartı** (Type-C hızlı şarj) | 拓普赛旗舰店 (Tuopusai amiral mağaza) | ¥19 | 58 | [tmall 926961598924](https://detail.tmall.com/item.htm?id=926961598924) |
| NP-F550 pil gövdesi | 唯卓仕 (Viltrox; ulusal 3C standardı, şarj göstergeli) | ¥52,8 ilk sipariş | 900+ | «唯卓仕 NP-F550» aratın |

> 💡 **Bu iki kalem, resmi projede eksik olan halkayı tam olarak tamamlıyor.** Resmi proje yalnızca baskı parçası `power_support`'u (×2) veriyor,
> **kontak modeli yok**, güç alma çözümü kendiniz çözülmeliydi — hazır taban kartı almak yeterli.
>
> ⚠️ **F970 değil NP-F550.** Resmi mesh dosyasının adı `np_f970` yanıltıcıdır: ölçülen sınırlayıcı kutu
> **38,6 × 20,6 × 70,8 mm** F550'nin boyutudur (Sony resmi özellikleri: F550 = 38,4×20,6×70,8,
> F970 = 38,4×**60,0**×70,8). Kaynak kodunun tümünde grep yalnızca 2 yerde eşleşiyor, **ikisi de NP-F550**
> (`robotd-design.md:572`, `duck-control/src/model.rs:108` «NP-F550, 2S Li-ion»), F970 sıfır eşleşme.
>
> Pil **gövdenin arka alt kısmına dışarıdan takılır**, 71 mm uzunluğun yaklaşık 40 mm'si gövde kabuğunun alt kenarının dışında kalır, iki adet
> 83,5 mm uzunluğundaki `power_support` parçası tarafından dışarıdan sıkıştırılır.

### Düşürücü modül (HAT basılmadığında ana karta 5 V vermek için)

HAT üzerindeki `U9 AP63205`, ana karta 5 V üretir; [HAT basmamak](08-hat-olmadan-kurulum.md) halinde onun yerini tutacak hazır bir modül alınmalıdır.

| Parça | Özellik | Fiyat | Arama terimi | Link |
|---|---|---|---|---|
| **UBEC 5V/3A** (ilk tercih) | Giriş **6–8,4 V'u kapsamalı**, çıkış 5 V 3 A, ekranlı ve ferrit halkalı | ¥10–15 | «UBEC 5V 3A 2S» | *eklenecek* |
| MP1584EN modülü (alternatif) | Giriş 4,5–28 V, çıkış 5 V sabit veya ayarlanabilir, 3 A etiketli (soğutucusuz gerçekte ~2 A) | ¥3–5 | «MP1584EN 5V» | *eklenecek* |

**Satın almadan önce şu üç sayıya bakın, markaya bakmayın:**

1. **Giriş gerilimi alt sınırı ≤ 6 V** — 2S pil yük altında 6,6 V'a kadar düşebilir, servolar aynı anda kalkarken daha da düşer. Birçok UBEC «2–6S» etiketli olsa da gerçekte alt sınır 7 V yazar, **2S pil bitmek üzereyken önce regülasyondan çıkar ve ana kart yeniden başlar**. Ürün sayfasında «giriş gerilimi» satırını bulun, alt sınır ≤ 6 V olmalıdır
2. **Çıkış akımı ≥ 2 A sürekli** — Radxa Zero 3W, NPU + kamera + WiFi çalışırken tepede 1 A'nın biraz üzerine çıkar; resmi HAT'ta da 2 A'lik AP63205 kullanılır. 3 A etiketli küçük modüller soğutucusuz gerçekte 1,5–2 A verir, bu yüzden UBEC öncelikli
3. **Senkron düşürücü** — verim %90+. **LM2596 almayın**: 150 kHz asenkron, gerilim farkı 1,5 V'un üzerinde olmalı, 6 V girişten 5 V çıkış zaten sınırdadır, ayrıca ısınır

Giriş ucuna paralel bir **470 µF / 16 V** elektrolitik kondansatör bağlayın; 15 servo aynı anda kalkarken oluşan gerilim düşüşünü tamponlar — bkz. [HAT'sız kurulum · Adım 3](08-hat-olmadan-kurulum.md#adım-3--güç-her-bölümden-sonra-ölçün).

---

## Altı · İki PCB

### RPI Robot HAT — satın alınamaz, yalnızca numune üretimi yapılabilir; ama buna ihtiyacınız olmayabilir

**Resmi olarak tek başına satılmaz.** Pollen yalnızca komple Microduck satar, HAT için perakende sayfası yoktur. oshwhub'da da kimsenin replikasını yaptığı bulunamadı.

**① Aslına sadık numune üretimi** — Resmi taraf eksiksiz üretim dosyalarını verir (Gerber + BOM + yerleştirme koordinatları, Apache-2.0).
Ölçümle doğrulandı: **4 katmanlı kart** (`F_Cu / In1_Cu / In2_Cu / B_Cu`), kart çerçevesi **65,0 × 30,9 mm**, köşe yuvarlaması **R3,5**,
BOM **47 satır / 123 adet** (bunların 5 satırı, 9 adedi DNP), fiilen yerleştirilen **113 konum**. SMT maliyeti birkaç yüz yuandan başlar ve asgari sipariş miktarı vardır.

**② Hazır modüllerle değiştirmek — ¥50'nin altında**

HAT'ın gerçek işlevleri (şematiğe göre tek tek doğrulandı):

| İşlev | Hâlâ gerekli mi | Hazır alternatif |
|---|---|---|
| **Servo veri yolu yarı çift yönlü TTL** — U5 `74LVC1G08` + U6 `SN74LVC1G125` + U7 `SN74LVC1G126`,<br>`DynUART_Tx`/`DynUART_Rx`/`Dynamixel_dir` ile yön kontrolü | ✅ Şart | Aşağıdaki tabloya bakın |
| **Güç dağıtımı** — `+BATT` doğrudan servolara; U9 `AP63205` + L4 6,8µH → `+5V` 40 pine, ana karta;<br>U3 `XC6206P182` → `+1V8` codec'e | ✅ Şart | Hazır UBEC (5V/3A ve üzeri) |
| **Ses** — U2 `TLV320AIC3104` (i2c3 0x18 + i2s3_2ch), U1 `PAM8406D` amfi,<br>MK1 MEMS mikrofon, Wago klemensle 5W hoparlör ve harici mikrofon bağlantısı | ❓ İhtiyaca bağlı | **Kayıt ve hoparlör istemiyorsanız tamamen atlayın** |
| **Sensör genişletme** — J5–J8 JST SH 1mm 4P (Qwiic/Stemma) ile ToF bağlantısı | ✅ Gerekli | Doğrudan i2c3'e bağlanır, birkaç kablo |
| Kart üzerindeki U11 `BMI088` | ❌ **Yerleştirilmiş ama yazılım kullanmıyor** (`i2c3-pihat.dts:11` «dormant», `:31` «unused but still connected») | — |
| U4 `CAT24C32` EEPROM | ❌ **DNP, yerleştirilmiyor** — bu yüzden bu kart **kendini tanıtan bir HAT değildir** | — |

**Servo konektörleri**: J13 / J14 = **JST EH 3P** (TTL, TH1 100R termistör üzerinden `+BATT`'a);
J3 / J11 = **JST EH 4P** (RS-485, U8 `SIT3088E` ile sürülür, doğrudan `+BATT`), şematik yanındaki not **«3A max»**.

**Yarı çift yönlü veri yolu dönüştürücü kartlar** (Feetech yolunda doğrudan uyumlu):

| Mağaza | Açıklama | Fiyat | Link |
|---|---|---|---|
| Fashion脖子 (Fashion Boyun, 13 yıllık mağaza, 90 ödeme) | Seri veri yolu servo sürücü kartı, **ST/SC serisine uygun** | **¥22** | [taobao 1005305041207](https://item.taobao.com/item.htm?id=1005305041207) |
| 众灵科技企业店 (Zhongling Teknoloji kurumsal mağaza, 200+ ödeme) | ZLink USB/TTL hata ayıklama kartı + veri yolu servo dönüştürücü | ¥22,5 | [taobao 570100064201](https://item.taobao.com/item.htm?id=570100064201) |
| 芯板坊 (Xinbanfang, 7 yıllık mağaza) | Waveshare (微雪) seri veri yolu servo sürücü kartı, ST/SC'ye uygun | ¥24 | [taobao 954634564409](https://item.taobao.com/item.htm?id=954634564409) |
| 灵影智能企业店 (Lingying Akıllı kurumsal mağaza, 200+ ödeme) | ST/SC Feetech veri yolu servo TTL sürücü kartı `TTL_Adapter_(A)` | ¥26 | [taobao 983866781632](https://item.taobao.com/item.htm?id=983866781632) |

> 💡 **Feetech yolunu izliyorsanız bu madde özellikle düşünülmeye değer.** `imu_to_dxl` yeniden çizilecek, politika yeniden eğitilecek, aygıt ağacı da değişecek —
> HAT da aynı şekilde yeniden değerlendirilmelidir. ¥22'lik dönüştürücü kart + bir UBEC, «servo veri yolu» ve «güç dağıtımı» gibi iki şart işlevi karşılar.
> Bedeli kart üzerindeki sesi kaybetmektir.

### imu_to_dxl — kendiniz çizin

STM32G031F8P6 + LSM6DSV16X + yarı çift yönlü tampon; dışarıya veri yolu bağımlısı olarak görünür (Dynamixel tarafında ID 200).
Protokol ve yazmaç düzeni tamamen geri çözülmüştür, bkz. [Donanım çözümü tersine mühendisliği](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md).

- **Numune üretim maliyeti**: 2 katmanlı kart, JLCPCB'de yaklaşık ¥25–40 (SMT hariç)
- **Çift protokol**: Hem Feetech hem Dynamixel desteklenecekse **donanım değişmez, yazılım dallanır** —
  ikisinin fiziksel katmanı tamamen aynıdır (yarı çift yönlü tek hat TTL / 1 Mbps / 3 kablo), fark yalnızca paket biçimindedir
  (V2 paket başlığı `FF FF FD 00` + CRC-16; Feetech `FF FF` + `~sum`)
- ✅ **Arayüz ve pin sırası resmi şartnameyle doğrulandı** — Feetech «HL-2915-C002 Seri Şartnamesi» A/0 (2026-02-27)
  4. sayfa 6-7 maddeler: konektör **`AMP-3`**, **`1=GND / 2=Vcc / 3=Signal/TTL`**, Dynamixel ile aynı.
  `HD-1910-C001.stp` içindeki konektör parçası adı `AMP-3P`'dir ve bu montaj `HL-2915-C002_ASM` içerir, iki model aynı platformu paylaşır.
  <br>Aynı şartname ayrıca şunları doğrular: yarı çift yönlü asenkron, 8bit/1stop/eşlik yok, **fabrika varsayılanı 1 Mbps**, ID 0–253 (varsayılan 1),
  sinyal yüksek seviyesi **2–5 V** (bu kartın 74LVC çıkışı 3,3 V pencerenin içinde; girişi 5,5 V'a dayanıklıdır, servonun 5 V'una da dayanır)
  <br>⚠️ Bu şartname HL-2915-C002'ye (**12 V**) aittir, elektriksel parametreler HD-1910'a (5–8,4 V) uygulanamaz
  <br>⚠️ «Feetech = TTL tek hat» yalnızca STS/SCS/HL için geçerlidir — resmi el kitabı **SMS serisinin RS485 kullandığını, varsayılanın 115200 olduğunu** belirtir
- **Konektör gövdesi hâlâ gerçekte takılarak denenmelidir** — Feetech kabloları **5264 terminal** etiketli, resmi HAT **JST EH** kullanır,
  ikisinin de **aralığı 2,5 mm**'dir ancak farklı serilerdir, mandal ve gövde şekli farklıdır. Servo ve kablolar elinize geçince bir kez takıp deneyin,
  takılmazsa J1/J2'yi `B3B-EH-A` (`C160259`) yerine 5264-3P ile değiştirin.
  PR #12 sürümündeki çizimde JST PH 2,0 mm vardı, **aralık yanlış, düzeltilmeli**
- **C6 (LDO giriş kondansatörü) dayanım gerilimi 10 V → 25 V** — veri yolu dolu pilde 8,4 V'tur, 10 V payı yetersiz (MLCC'de ayrıca DC bias kaybı da var)
- **C5 100 nF değil 4,7 µF kullanın** — ST DS12992 Rev 3 Şekil 13, `VDD/VDDA` için
  `1 × 100 nF + 1 × 4.7 µF` ister, iki aynı 100 nF'ın paralel bağlanması işe yaramaz. JLCPCB temel kütüphanesinden `C19666` seçin
- **U1'in 2, 3 numaralı pinlerinde aktif kristal pedleri bırakın (yerleştirilmez)** — TSSOP20'de `OSC_OUT` çıkarılmamıştır, pasif kristal bağlanamaz;
  HSI16 doğruluğu en kötü durumda −%1,85/+%1,55'tir (Tablo 41), 1 Mbps için yeterli ama pay fazla değildir
- **DATA hattına TVS ekleyin** — servoyu enerjili takıp çıkarmak olağandır
- **Protokol yazılımla otomatik tanınır, DIP anahtar/jumper eklenmez** — iki üreticinin paket başlığı da `FF FF`'tir, Dynamixel V2'de arkasından `FD 00` gelir, Feetech'te `ID`+`LENGTH` gelir (LENGTH daima ≥ 2, dolayısıyla `FD 00` belirsizlik yaratmaz). İlk 3 paketle oy kullanılarak kilitlenir, sonrasında kilitlenen protokolle alınıp gönderilir. Yürüyen bir robotta DIP anahtar titreşimle arızalanma noktasıdır, üstelik bu kart ömrü boyunca yalnızca bir kez ayarlanır
- **J3 4P değil 6P olsun** — fazladan 4/5 numaralı pinler `USART1_TX/RX`'tir (U1 16/17 numaralı pinlerin yeniden eşlenmesi), 5 yuanlık bir USB-TTL takınca printf görülebilir. G031'de USB çevre birimi yoktur, USB portu eklemek bir köprü yongası daha gerektirir, değmez

---

## Yedi · Kablolar ve Aletler

| Parça | Mağaza | Açıklama | Fiyat | Link |
|---|---|---|---|---|
| **Servo veri yolu bağlantı kablosu** | 深圳飞特舵机工厂店 (Shenzhen Feetech servo fabrika mağazası) | Üç iğneli dört iğneli **5264 arayüzü** | **¥1,8** | [taobao 616460581906](https://item.taobao.com/item.htm?id=616460581906) |
| Servo kablo malzemesi | 鸿翊电子舵机工厂店 (Hongyi Elektronik servo fabrika mağazası) | Feetech seri veri yolu, 3 iğneli/4 iğneli 5264 terminal | ¥2,5 | [taobao 769633088382](https://item.taobao.com/item.htm?id=769633088382) |
| Servo bağlantı kablosu (çoklu uzunluk) | 松甲科技 (Songjia Teknoloji, 300+ ödeme) | Dişi-dişi **5264-3P**, 10/15/20/30/50/70 cm | ¥2 | [taobao 587191439333](https://item.taobao.com/item.htm?id=587191439333) |
| **FE-URT-1 hata ayıklama kartı** | 深圳飞特舵机工厂店 (resmi mağaza) | USB'den 485/TTL'e | **¥45** | [taobao 603181554943](https://item.taobao.com/item.htm?id=603181554943) |
| URT-2 hata ayıklama kartı | 深圳飞特舵机厂家 (Shenzhen Feetech servo üreticisi) | Benzeri | ¥45 | [taobao 575365901461](https://item.taobao.com/item.htm?id=575365901461) |
| URT hata ayıklama kartı (üçüncü taraf) | 云驱者科技企业店 (Yunqu Teknoloji kurumsal mağaza) | Benzeri | ¥40 | [taobao 712781832610](https://item.taobao.com/item.htm?id=712781832610) |

> **Hata ayıklama kartı zorunlu bir parçadır** — servolar geldiğinde yapılacak ilk iş veri yolu zamanlamasını ölçmektir.
>
> ⚠️ **Bu yalnızca Feetech'e özgü bir sorun değildir.** Resmi Dynamixel yolunda da aynı şekilde **cihaz başına bir yanıt gecikmesi** vardır —
> `duck-control/src/model.rs:84-86` XL330'un fabrika `return_delay_time = 250` olduğunu yazar,
> yani **cihaz başına 500 µs**, «Across **16 devices** that is **8 ms per tick — 40% of a 20 ms budget**»,
> resmi çözüm bu yazmacı 0 yazmaktır (`EXPECTED_REGISTERS` içinde).
> **Feetech tarafı araştırıldı**: STS/SCS'de `SYNC READ` (`0x82`) vardır ve Return Delay Time fabrikada zaten 0'dır —
> bkz. [Donanım çözümü tersine mühendisliği · Feetech STS/SCS protokol karşılaştırması](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/硬件方案逆向.md). Bu yüzden ölçmek daha da önemlidir, onun daha yavaş olduğunu varsaymayın.

---

## Sekiz · Tuzaklar

1. **Kamera flex kablosunu uzun almayın** — ana kart ve kamera aynı baştadır, aynı gövdededir, MIPI kablosu boyundan geçmez. 4–15 cm yeterlidir.
2. **Kamera 180° değil 90° döndürülmüştür** — yukarıya bakın.
3. **VL53L0X'in VL53L5CX gibi satılması** — aramada çıkanların çoğu tek noktalı L0X'tir, yazılım tanımaz; L7CX de L8CX değildir.
4. **Radxa çıplak karta fazla para vermeyin** — resmi kanalda 1G / eMMC'siz yaklaşık ¥130 (2026-09 anlık görüntüsü), küçük mağazalarda ¥690–1469 satılıyor. Yalnızca resmi kanalları kullanın; eMMC için de ek ödemeye gerek yok, bir microSD kart takmak yeter.
5. **Taishanpai sığmaz** — yalnızca pahalı olduğu için değil, başta 70×45'lik yer olmadığı için.
6. **¥8'lik Feetech STS3215 / ¥22'lik Taishanpai** — ikisi de SKU yemi, içine girince en düşük seçenek aksesuardır.
7. **Loctite 243 ¥15'in altındaysa sahte olabilir, dikkat** (bkz. [Mekanik satın alma listesi](05-mekanik-satin-alma.md)).

---

## Doğrulanmamış Maddeler

- Tüm fiyatlar, satış adetleri, mağaza bilgileri ve link geçerliliği (2026-09-04 anlık görüntüsü)
- Pollen'ın HAT'ı tek başına satıp satmadığı
- Zero 3W'nin CSI soketinin 15P mi 22P mi olduğu (resmi belgede verilmemiş, bu belgede «büyük olasılıkla 22P» olarak işaretlenmiştir)
- Taishanpai'nin özellikleri, fiyatı, açık kaynak proje içeriği

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
