# Mekanik satın alma listesi (Çin içi / Taobao)

> **Depoda dört liste ve bir baskı açıklaması var, her biri ayrı konuyu kapsar:**
>
> | Belge | Ne kapsar | Ne kapsamaz |
> |---|---|---|
> | [BOM](02-malzeme-listesi-bom.md) | **Ana tablo**: tüm malzemeler, adetler (MJCF'deki geom referanslarından sayılmıştır), maliyet mertebesi, henüz çözülmemiş boşluklar | Tam olarak nereden alınacağı, nasıl basılacağı |
> | [Elektronik satın alma listesi](06-elektronik-satin-alma.md) | Elektronik parçaların **nereden alınacağı**: ana kart / kamera / ToF / güç / iki PCB / kablolar, Taobao gerçek linkleri + kaçınılacak tuzaklar | Adet dayanağı, mekanik parçalar |
> | **Mekanik satın alma listesi** (bu belge) | Mekanik parçaların **nereden alınacağı**: rulman / bağlantı elemanları / sarf malzemeleri, Taobao gerçek linkleri | Elektronik parçalar |
> | [Donanım özellikleri hızlı başvuru](04-donanim-ozellikleri.md) | **Parametreler**: arayüzler, gerilim, protokol, yazılım tarafında uyulması gereken değerler | Fiyat ve mağaza |
> | [Baskı ve CAD](12-baski-ve-cad.md) | **Baskı girişi**: CAD deposunda sürüm, malzeme ve adet seçimi | Satın alma |
>
> Montajda kullanılan parça numaraları ve vida eşleşmeleri [CAD deposunda](https://github.com/fanhao375/microduck-replica-cad#装配-bom) bulunur.


> **Anlık görüntü tarihi: 2026-09-04.** Fiyatlar ve satış adetleri değişir, linkler geçersiz kalabilir; sipariş vermeden önce fiyatı kendiniz kontrol edin.
> Elektrik-elektronik parçalar (ana kart / kamera / ToF / güç / PCB / kablolar) için bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md).
> Fiyatlar ¥ (Çin yuanı) cinsindendir.
>
> Adetler MJCF `robot_walk.xml` içindeki mesh örnek sayımından ve delik özelliklerinden geri çıkarılmıştır, **bunlar çıkarım değerleridir, resmi çizim değildir**.

---

## 1. Rulmanlar (toplam 14 adet, iki ölçü)

Adetler doğrudan `robot_walk.xml` içindeki mesh referansları sayılarak bulunmuştur; altı MJCF varyantında sayım tamamen aynıdır.
**Ölçüler dosya adına bakılarak değil, ağ geometrisi ölçülerek bulunmuştur**:

| Ölçü | Adet | Ölçülen (dış çap / iç delik / genişlik) | Ağ |
|---|---|---|---|
| **Ø22 × 16 × 4** | **11** | 22,0 / **16,0** / 4,0 mm | `seeed_bearing__configuration__22x16x4` |
| **Ø15 × 10 × 3** | **3** | 15,0 / **10,0** / 3,0 mm | `seeed_bearing__configuration_default` |

| Mağaza | Açıklama | Fiyat | Link |
|---|---|---|---|
| **NBZH 永天轴承** (16 yıllık mağaza) | Paslanmaz çelik ultra ince duvarlı `ET2216ZZ` / `MR16224` / `SET2216` / `DDA2216`, 16×22×4 | **¥2,2** | [taobao 539024647147](https://item.taobao.com/item.htm?id=539024647147) |
| **鑫燚轴承** (7 yıllık mağaza) | NSK mikro rulman, **aynı linkte hem 10×15×3 hem 16×22×4 var** | **¥5** | [taobao 670727787832](https://item.taobao.com/item.htm?id=670727787832) |

> 💡 鑫燚'deki ilan tek linkten iki ölçüyü birden almayı sağlar, kolaylık sunar.

**机械行者Robo'nun Feetech sürümünü kurarken gerçekte aldıkları** (2026-09-16, çalıştı): 10×15×3 [Taobao 963037239628](https://item.taobao.com/item.htm?id=963037239628&skuId=6069280211062), 16×22×4 [Tmall 978199812185](https://detail.tmall.com/item.htm?id=978199812185&skuId=6245616343131). Çizim deposundaki [montaj BOM'unda](https://github.com/fanhao375/microduck-replica-cad#装配-bom) da var.

> ⚠️ **`bearing_roll` rulman değildir, satın alınan parça da değildir.** MJCF'de 2 kez geçen bir de
> `bearing_roll` adlı ağ var; ölçüldüğünde **23 × 3 × 40 mm, Ø≈18 merkez delikli düz bir plaka** (hacim 625 mm³, doluluk %23)
> ve `trunk_base` / `yaw2roll` / dış kabukla **aynı Onshape Part Studio'dan** geliyor
> (elementId `d6fcdccc8b25aaa256e7e213`); iki gerçek rulman ise yapılandırma dizgili başka bir standart parça kütüphanesinde.
> Bu, hip_roll mili üzerindeki Ø22 rulmanın **baskı kapağıdır (压盖)**, **basılır, satın alınmaz**. Bkz. [Baskı parçaları](#4-baskı-parçaları).

---

## 2. Bağlantı elemanları (M2 sistemi, yaklaşık 325 adet)

Tüm makinedeki M2 sınıfı delikler (Ø1,9–2,5 mm, sarma açısı ≥300°) **montaj kullanımına göre ağırlıklandırılınca toplam 237**:
60'ı servo gövdesinde (15 × 4), 21'i rulman/PCB/pil gibi standart parçalarda, yapısal parçalarda yaklaşık 156.
Aşağıda 325 adet verilmiştir; 237 delik konumuna göre **1,37×** pay vardır.

| Ölçü | Önerilen adet | Kullanım |
|---|---|---|
| M2×4 alyan başlı silindirik | 60 | İnce duvarlı yerler |
| **M2×6 alyan başlı silindirik** | **80** (ana ölçü) | |
| M2×8 alyan başlı silindirik | 40 | Delik derinliği 3–5 mm |
| M2×12 alyan başlı silindirik | 15 | Az sayıda derin delik |
| M2 somun | 50 | Diş açılmayan yerler |
| **M2 ısıl ankraj (heat-set insert)** | **60** | Baskı parçaları için önerilir, doğrudan diş açmaktan çok daha sağlamdır |
| M2.5×6 | 20 | Az sayıda Ø2,7 delik konumu |

Çıkarım süreci için bkz. [Vidalar ve bağlantı elemanları](07-vidalar-ve-baglanti.md).

### Vida setleri

| Mağaza | Açıklama | Fiyat | Satış | Link |
|---|---|---|---|---|
| **广州信邦电子** (10 yıllık mağaza, ücretsiz kargo) | **600 adet** kutulu paslanmaz çelik havşa/düz başlı alyan **M2/M2.5/M3** karışık set, **anahtar hediye** | **¥26,8** | 42 | [taobao 842110292995](https://item.taobao.com/item.htm?id=842110292995) |
| 宏顺通五金工厂店 (8 yıllık mağaza) | 600 adet M2/M2.5/M3 havşa başlı alyan + somun + hediye alet | ¥23 | 2 | [taobao 842400332284](https://item.taobao.com/item.htm?id=842400332284) |
| 广州信邦电子 (10 yıllık mağaza, ücretsiz kargo) | 304 paslanmaz çelik M2–M8 tava başlı alyan + somun + pul seti | ¥19,8 | 71 | [taobao 888186264852](https://item.taobao.com/item.htm?id=888186264852) |

**机械行者Robo'nun gerçekte aldığı** (2026-09-16): M2×5 / M2×6 / M2.5×6 hepsi [Tmall 637524754721](https://detail.tmall.com/item.htm?id=637524754721) üzerinden SKU seçilerek.

> 💡 **M2 içerdiği açıkça yazan setleri tercih edin.** Birçok «M2M3M4M5M6M8 komple set» başlığında M2 geçer, ama gerçekte en küçüğü M3'tür —
> sipariş vermeden önce SKU'ya dikkatle bakın. Bu projede **M2 mutlak ana ölçüdür**, M3 neredeyse hiç kullanılmaz.

### Isıl ankraj (heat-set insert) + bastırma ucu

| Mağaza | Açıklama | Fiyat | Satış | Link |
|---|---|---|---|---|
| **深圳市榕誉微电子** (6 yıllık mağaza) | **400 ADET M2 + M3** ısıl pirinç somun, çift kanallı tırtıllı | **¥22** | 200+ | [taobao 1000673642588](https://item.taobao.com/item.htm?id=1000673642588) |
| 深圳市榕誉微电子 (6 yıllık mağaza) | 80/220 ADET M2–M6 ısıl pirinç somun | ¥18 | 1000+ | [taobao 922318148975](https://item.taobao.com/item.htm?id=922318148975) |
| 天卓五金官方旗舰店 (ücretsiz kargo) | 土八 ısıl somun M1–M8, ölçüye göre tek tek alınır | ¥0,77'den | 40 bin+ | [tmall 809364062256](https://detail.tmall.com/item.htm?id=809364062256) |

> ⚠️ **Bastırma ucunu unutmayın.** Isıl ankrajlar **özel havya ucuyla** bastırılmalıdır; sıradan havya ucu düzgün bastıramaz, eğri oturtur.

| Mağaza | Açıklama | Fiyat | Satış | Link |
|---|---|---|---|---|
| **烙铁工具** (7 yıllık mağaza) | 3D ısıl ankraj bastırma ucu seti M2–M8, **936 / T12 / T65** havyalara uygun | **¥13** | 800+ | [taobao 902798112263](https://item.taobao.com/item.htm?id=902798112263) |
| 外茂优品 (ücretsiz kargo) | Benzer M2–M8 bastırma ucu seti | ¥11,5 | 200+ | [taobao 966212633086](https://item.taobao.com/item.htm?id=966212633086) |

### Vida sabitleyici (metal-metal vida noktalarında gevşemeyi önlemek için)

Servo çıkış mili ve metal parça birleşim yerlerinde orta mukavemetli vida sabitleyici önerilir.

| Mağaza | Açıklama | Fiyat | Satış | Link |
|---|---|---|---|---|
| **LOCTITE 乐泰旗舰店** (Loctite resmi mağaza) | Henkel Loctite **243** orta mukavemetli sökülebilir vida sabitleyici | **¥19,11** | 10 bin+ | [tmall 653848839737](https://detail.tmall.com/item.htm?id=653848839737) |
| LOCTITE 乐泰企业店 (Loctite kurumsal mağaza) | 243 / 263 vida sabitleyici | ¥18,4 | 700+ | [taobao 663963768247](https://item.taobao.com/item.htm?id=663963768247) |
| 工业胶厂家直销 (endüstriyel yapıştırıcı üretici doğrudan satış, ücretsiz kargo) | Loctite 243 / 242 / 263 | ¥16,8 | 600+ | [taobao 925965306702](https://item.taobao.com/item.htm?id=925965306702) |

> ⚠️ **¥15'in altındakilere dikkat.** Arama sonuçlarında ¥8, ¥10'luk «Loctite 243» ilanları var, orijinal ürün bu fiyata gelmez.
> Yalnızca LOCTITE resmi mağazasını veya yetkili bayiyi tercih edin.

---

## 3. Sarf malzemeleri

| Malzeme | Miktar | Nerede kullanılır |
|---|---|---|
| **PLA / PETG** | yaklaşık 300–500 g | Yapısal parçaların büyük kısmı |
| **TPU** | az miktar | `jaw_soft_软下巴` (yumuşak çene), `soft_mouth_top_软嘴顶部` (yumuşak ağız üstü) — adlandırma ve kullanım amacına bakılarak yumuşak malzeme önerilir |

> Baskı yöntemi ve tolerans değerlendirmesi henüz yapılmadı, bkz. [PROGRESS.md](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/PROGRESS.md) risk listesi.
> **Simülasyon STL'si ≠ basılabilir mühendislik parçası** — yalnızca dış şekli ve atalet değerlerini garanti eder, geçme toleransı, vida delikleri, ısıl ankraj yuvaları yoktur.

---

## 4. Baskı parçaları

**En güncel model, malzeme ve baskı adetleri için [CAD deposuna](https://github.com/fanhao375/microduck-replica-cad#装配-bom) bakın; resmi simülasyon referans sayılarına göre sipariş/baskı yapmayın.** İki servo modelinin eşleşen parçaları farklıdır, ayrıntı için bkz. [baskı girişi](12-baski-ve-cad.md).

<details>
<summary>Resmi modelin geçmiş sayımları ve adlandırma düzeltmeleri (yalnızca analiz içindir, güncel baskı listesi değildir)</summary>


**30 çeşit / 41 adet.**

**Eski modelde 9 ağ çeşidi birden fazla kez referans edilmiş:**

| Parça | Eski modelde referans sayısı |
|---|---|
| `leg_腿部` (bacak) | **×4** |
| `hip_l_髋部左` (sol kalça) | ×2 |
| `neck_颈部` (boyun) | ×2 |
| `power_support_电源支架` (güç desteği) | ×2 |
| `sole_left_左脚底` (sol taban) | ×2 |
| `sole_right_右脚底` (sağ taban) | ×2 |
| `upper_leg_rigidity_plate_上腿加固板` (üst bacak güçlendirme plakası) | ×2 |
| `yaw2roll_偏航转横滚` (yaw'dan roll'a) | ×2 |
| **`bearing_roll_横滚轴承压盖`** (roll rulman kapağı) | **×2** ← aşağıdaki düzeltmeye bakın |
| Diğer 21 çeşit | her biri ×1 |

> ⚠️ **Düzeltme (2026-09-04)**: `bearing_roll` bu depoda daha önce «standart parça — basılmaz» sınıfına konmuştu, **bu yanlıştı**.
> Ölçütler: ① ölçülen 23×3×40 mm düz plaka, Ø≈18 merkez delikli; hiçbir standart rulmanın şekli değil (gerçek rulman dönel gövdedir);
> ② `trunk_base` / `yaw2roll` / dış kabukla aynı Onshape Part Studio'dan geliyor;
> ③ montajda `yaw2roll` ile aynı body'de, aynı konumda, yan yüzüne yapışan bir kapak plakası.
> Çinceden «轴承滚轮» (rulman makarası) olarak çevrilmesi de yanlıştı — ne rulman ne makaradır, adı «roll rulman kapağı (横滚轴承压盖)» olarak düzeltildi.
> Baskı parçası sayımı bu nedenle 29 çeşit / 39 adetten **30 çeşit / 41 adede** düzeltildi.

⚠️ **Sol-sağı karıştırmayın**: `upper_leg_left` ile `upper_leg_right` ayna parçalardır
(kütle merkezi **±0,006766 m ＝ ±6,77 mm**), ikisi de basılmalıdır;
`ankle_left`/`ankle_right`, `sole_left`/`sole_right`, `foot_left`/`foot_right` için de aynısı geçerlidir.

---

</details>

## 5. Satın alınmayacaklar (resmi modelde olup başka kategoriye girenler)

| Ağ | Nedir | Ne yapılır |
|---|---|---|
| `xl330` ×15 | Servo | Bkz. [Aktüatör seçimi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/执行器选型.md) |
| `np_f970` | NP-F pil (**aslında F550**) | Bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «Güç» bölümü |
| `elec_rpi_robot_hat_pcb` | HAT devre kartı | Ürettirilir, bkz. [Elektronik satın alma listesi](06-elektronik-satin-alma.md) belgesinin «İki PCB» bölümü |
| `pcb__raspberry_pi_zero_2_w` | Ana kart yer tutucusu | Radxa Zero 3W alın |
| `lens` / `m12_lens_holder` | Lens ve lens tutucusu | ⚠️ İkisi aynı Onshape Part Studio'dan geliyor,<br>bu depo `lens`'i standart parça, `m12_lens_holder`'ı baskı parçası saymış, **bu ayrım şüpheli**, gerçek parçayla yeniden doğrulanmayı bekliyor |
| `speaker` | Hoparlör | 5W, HAT'in Wago klemensine bağlanır |

---

## Doğrulanmamış maddeler

- Tüm fiyatlar, satış adetleri, mağaza bilgileri ve link geçerliliği (2026-09-04 anlık görüntüsü)
- Vida uzunlukları delik derinliğine göre hesaplanmıştır, **aralıktır, ölçülmüş değer değildir**; FDM baskı büzülmesi de gerçek delik çapını değiştirir
  (Ø2,2 genellikle 0,1–0,3 mm küçük çıkar)
- TPU parçalar için karar adlandırma ve kullanım amacından çıkarılmıştır, resmi taraf malzemeyi belirtmemiştir
- `lens` / `m12_lens_holder` için satın alma/baskı aidiyeti

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
