# Microduck Replika

**Basitleştirilmiş Çince (asıl kaynak)** · [English](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/README.en.md)

[Pollen Robotics Microduck](https://pollen-robotics.com/microduck/) tabanlı, üçüncü taraf komple robot replika projesi; satın almadan, baskıya, montajdan kalibrasyona, kontrole ve eğitime kadar malzemeleri sunar.

**Feetech HD-1910 sürümü gerçek robotta uçtan uca doğrulandı: ayakta durma, yürüme, öne takla sonrası kalkma çalışıyor.** Ana hat **15 adet Feetech HD-1910 servo** kullanır; yazılabilir **replika imajı** ve **Microduck Studio web kontrol paneli** sunar; ağ yapılandırması, kalibrasyon ve uzaktan kumanda telefon veya bilgisayar tarayıcısından yapılır.

**İlk kullanım akışı gerçek robotta çalıştırıldı:** imaj yazma → hotspot ile ağ yapılandırması → servo ve IMU kalibrasyonu → gamepad eşleştirme, acil durdurma testi → ayakta durma ve yürüme. [Gerçek robot doğrulama kaydına bak](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/历史更新.md#最近更新)

## Ördeğin şu anki hali

**2026-10-24 · Gerçek robotta hareket doğrulaması geçti**: Aşağıdaki iki gerçek çekim video, öne takla sonrası kalkmayı ve masa üstünde yürümeyi gösteriyor.

<table>
<tr>
<th align="center">Öne takla ve kalkma</th>
<th align="center">Masa üstünde yürüme</th>
</tr>
<tr>
<td align="center" valign="middle"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-roll-and-rise.mp4"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-roll-and-rise.gif" alt="Gerçek robot öne takla attıktan sonra yeniden ayağa kalkıyor" width="260"></a></td>
<td align="center" valign="middle"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-walking.mp4"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-walking.gif" alt="Feetech sürümü ördek masa üstünde adım atarak yürüyor" width="400"></a></td>
</tr>
<tr>
<td align="center"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-roll-and-rise.mp4">Tam MP4 · yaklaşık 8 sn</a></td>
<td align="center"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/demos/2026-10-24-walking.mp4">Tam MP4 · yaklaşık 6 sn</a></td>
</tr>
</table>

Hareketli görseller sessiz önizlemedir; MP4 tam görüntüyü ve sesi korur.

**[İmajı indir](https://github.com/fanhao375/microduck-replica/releases/latest)** · **[İlk kullanım rehberi (PDF / web)](17-baslangic-rehberi.md)** · **[CAD ve baskı parçaları](https://github.com/fanhao375/microduck-replica-cad)** · **[Montaj eğitimi](#-montaj-video-eğitimi)** · **[BOM satın alma listesi](02-malzeme-listesi-bom.md)** · **[Donanım projeleri](13-devre-kartlari.md)**

---

### Geçerli sürümler

- **Feetech HD-1910 + Radxa Zero 3W**: Bu depodaki replika imajı ve Studio web kontrol paneli kullanılır.
- **Dynamixel XL330**: İlgili CAD ve montaj malzemeleri sunulur; uyumlu çalışma yazılımı gerekir.

[Baskı parçalarını ve satın alma listesini seç](#baskı-parçaları-ve-satın-alma-listesi) · [Servo ayrıntılı karşılaştırmasına bak](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/执行器选型.md)

---

## Sohbet grubu

Aynı işi yapan insanlar var; replika ilerlemesini, yaşanmış sorunları (tuzakları) ve parça tedarikini tartışmak için bir WeChat grubu kuruldu.

Aşağıda **Ördek Replika Grubu 13**'ün karekodu var (WeChat grubu 200 kişiye ulaşınca karekodla katılım mümkün olmaz).

<div align="center">
  <img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/wechat-group-13.png" alt="Ördek Replika Grubu 13 WeChat karekodu" width="280">
  <br>
  <sub><b>Ördek Replika Grubu 13 · Karekod 2026-11-04'e kadar geçerli</b> (WeChat grup karekodları 7 gün sonra otomatik geçersiz olur)<br>
  Süresi dolmuşsa bir <a href="https://github.com/fanhao375/microduck-replica/issues">issue</a> açıp haber verin, yenisini koyacağım</sub>
</div>

---

## 📺 Montaj Video Eğitimi

**[Bilibili serisi "MicroDuck Sıfırdan Kurulum Eğitimi"](https://space.bilibili.com/312747174/lists/9279084?type=season)** — CAD çizimlerinin ve montaj BOM'unun yazarı **机械行者Robo** tarafından çekildi; parça listesinden başlar, her bölümde bir bileşen monte edilir. Toplam 8 bölüm; 2026-10-12 itibarıyla 6 bölüm yayımlandı:

Bölüm listesinin sağındakiler yazarın hesaplarıdır; sırasıyla **Bilibili, Xiaohongshu, Douyin**. Karekodu tarayarak veya görsele tıklayarak ulaşabilirsiniz.

<table>
<thead>
<tr><th>Bölüm</th><th>İçerik</th><th nowrap>Süre</th><th>Bilibili</th><th>Xiaohongshu</th><th>Douyin</th></tr>
</thead>
<tbody>
<tr>
<td nowrap><a href="https://www.bilibili.com/video/BV1RoHX68EFV/">Bölüm 1</a></td><td width="260"><a href="https://www.bilibili.com/video/BV1RoHX68EFV/">Parça ve aksesuar listesi</a></td><td nowrap>1:32</td>
<td rowspan="6" align="center" valign="middle" width="210"><a href="https://space.bilibili.com/312747174"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/social/bilibili-qr.jpg" alt="Bilibili: 机械行者Robo" width="200"></a><br><sub><b>机械行者Robo</b><br>UID 312747174</sub></td>
<td rowspan="6" align="center" valign="middle" width="210"><a href="https://www.xiaohongshu.com/user/profile/5ad950114eacab046016f038"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/social/xiaohongshu-qr.jpg" alt="Xiaohongshu: 机械行者" width="200"></a><br><sub><b>机械行者</b><br>Xiaohongshu no. 270594280</sub></td>
<td rowspan="6" align="center" valign="middle" width="210"><a href="https://www.douyin.com/user/MS4wLjABAAAArLa_6yE3GE-AoRURoQnIHdbbI7yM-GHhzlgLZ-XbeYE"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/social/douyin-qr.jpg" alt="Douyin: 机械行者Robo" width="200"></a><br><sub><b>机械行者Robo</b><br>Douyin no. 1852366168</sub></td>
</tr>
<tr><td nowrap><a href="https://www.bilibili.com/video/BV1Xppb6tECr/">Bölüm 2</a></td><td><a href="https://www.bilibili.com/video/BV1Xppb6tECr/">Alt bacak (baldır) montajı</a></td><td nowrap>2:21</td></tr>
<tr><td nowrap><a href="https://www.bilibili.com/video/BV1ycpb6yEwB/">Bölüm 3</a></td><td><a href="https://www.bilibili.com/video/BV1ycpb6yEwB/">Üst bacak (uyluk) montajı</a></td><td nowrap>5:13</td></tr>
<tr><td nowrap><a href="https://www.bilibili.com/video/BV1Kwpg6wE9G/">Bölüm 4</a></td><td><a href="https://www.bilibili.com/video/BV1Kwpg6wE9G/">Gövde grubu montajı</a></td><td nowrap>2:29</td></tr>
<tr><td nowrap><a href="https://www.bilibili.com/video/BV1EEpg6nEkD/">Bölüm 5</a></td><td><a href="https://www.bilibili.com/video/BV1EEpg6nEkD/">Boyun montajı</a></td><td nowrap>0:40</td></tr>
<tr><td nowrap><a href="https://www.bilibili.com/video/BV1aKpE6hEzj/">Bölüm 6</a></td><td><a href="https://www.bilibili.com/video/BV1aKpE6hEzj/">Kafa montajı</a></td><td nowrap>5:50</td></tr>
</tbody>
</table>

### Baskı Parçaları ve Satın Alma Listesi

Önce servo sürümüne göre baskı malzemesini seçin, sonra buna uygun satın alınan parçaları hazırlayın.

| Malzeme | Geçerli sürüm | Giriş |
|---|---|---|
| **Baskı parçaları ve CAD** | **Feetech HD-1910** | [Feetech bölümüne git](https://github.com/fanhao375/microduck-replica-cad#飞特-hd-1910-打印资料): baskı projesi, CAD kaynak dosyaları ve güncelleme notları |
| **Baskı parçaları ve CAD** | **Dynamixel XL330** | [XL330 bölümüne git](https://github.com/fanhao375/microduck-replica-cad#dynamixel-xl330-打印资料): ilgili sürümün CAD kaynak dosyaları ve baskı açıklamaları |
| **Montaj satın alma listesi** | **Feetech HD-1910** | **[Çevrimiçi önizleme](02-malzeme-listesi-bom.md)** · **[Excel indir](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/BOM/装配BOM-机械行者Robo-2026-10-23-带采购链接.xlsx)**: 机械行者Robo tarafından derlendi, 2026-10-23 sürümü; adet, malzeme ve satın alma bağlantılarını içerir |

İki servo türünün uyum parçaları karıştırılamaz. Baskı dosyalarının tam sürümü ve güncelleme tarihi CAD deposunun ilgili bölümünde tutulur; bu satın alma listesi Feetech çözümüne göre derlenmiştir, XL330'un servoları ve ilgili elektroniği ayrıca kontrol edilmelidir.

---

## Şu an nerede

**2026-10-25** itibarıyla **Feetech sürümü komple replika, ilk kullanım ve gerçek robotta hareket zinciri çalışır durumda**. Aşağıda her bölümün çıktıları ve sonraki geliştirme projeleri tanıtılıyor; test kapsamı ve geçmiş süreç için [güncelleme kayıtlarına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/历史更新.md) bakın.

---

## 💻 Yazılım · Replika İmajı ve Microduck Studio

**2026-10-31 · Yazılım paketi güncellemesi: gamepad yeniden eşleme, kamerada yerinde yakınlaştırma ve SSH yönergesi**: 27 sürümü güncelleme girişi bulunan cihazlarda yalnızca yazılım paketini kurmak yeterlidir, imajı yeniden yazmaya gerek yoktur. Gamepad düğmelerini, çubuklarını ve tetiklerini öğrettikten sonra yapılandırma kaydedilir; sürücü, sayfadaki yönergelere göre ayrıca onaylanarak kurulmalıdır, yalnızca web sayfasını güncellemek yetmez. Orijinal 27 sürüm yükseltici, Linux eşlemesi ve servis izni kontrolleri geçti; yeni gamepad sürücüsünün gerçek kurulumu ve çeşitli gamepad modellerinin doğrulaması hâlâ beklemede. [Yazılım paketi ve ilk kurulum ekleri](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.31) · [İşlem adımları ve doğrulama kapsamı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/功能软件升级-20261030.md)

**2026-10-30 · Yazılım paketi güncellemesi: yalnızca IMU bağlıyken de bağımsız tanılama**: Veri yolu IMU'su artık servo başlangıç kontrolü tarafından engellenmez. Hiç servo olmadığında veya yalnızca bir kısmı bağlıyken, genel bakış ve IMU sayfası kartın yanıtını, tanımasını ve örnek durumunu göstermeye devam eder; süresi dolmuş, bağlantısı kopmuş veya yapılandırma değişmiş sonuçlar eski sonuçla devam ettirilmez. Tanılama, hareket veya kalibrasyon yazmasına izin vermez. Önce web arayüzünü yükseltin, sonra ana programın `.47` / API 42'ye güncellenmesini açıkça onaylayın. [Yazılım paketi ve kurulum ekleri](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.30) · [Güncelleme adımları ve kullanım açıklaması](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/仅接IMU的独立诊断与软件更新-20261030.md)

**2026-10-29 · Yazılım paketi güncellemesi: IMU ve servo durumu ayrı gösterilir**: Ana program IMU'yu beklerken, genel bakış ve servo sayfası alınan servo yanıt paketlerini, ham konumu, gerilimi ve sıcaklığı göstermeye devam eder; eksik, bilinmeyen ve süresi dolmuş veriyi birbirinden ayırır. Önce web arayüzünü yükseltin, sonra ana programın `.46`'ya güncellenmesini açıkça onaylayın; mevcut kartlar yazılım güncellemesiyle kurar. [Yazılım paketi ve kurulum ekleri](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.29) · [Güncelleme adımları ve doğrulama kapsamı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/软件更新与独立设备状态说明-20261029.md)

**2026-10-28 · Yazılım paketi güncellemesi (SD kartı yeniden yazmadan)**: Ayarlar sayfasında yükseltme girişi bulunan kullanıcılar önce `2026.10.28` web / ses paketini kursun; yeniden bağlandıktan sonra robotu destekleyip servo torkunu bırakabilir (servoları gevşetebilir) ve ana programın güncellenmesini açıkça onaylayabilir, ardından IMU sayfasında `Qinmo · Feetech` seçip yönü doğrulayabilir. Ana programın otomatik güncellemesi yalnızca bilinen 20261027 temel sürümünü destekler; mevcut kartlar varsayılan olarak otomatik tanımayı sürdürür. Qinmo'nun gerçek donanım ve bu sürümün komple robot yükseltmesi hâlâ doğrulanmayı bekliyor; müziğe uyumlu hareket ve serbest AI sesli sohbet hâlâ çözülmedi. [Yazılım paketi ve kurulum ekleri](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.28) · [Mevcut kullanıcılar için güncelleme adımları](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/软件更新与Qinmo使用说明-20261028.md) · [Qinmo web kullanımı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/Qinmo-IMU-网页使用.md)

**Replika imajı 20261027: web yazılım yükseltmesi ve yerel otur/kalk sesi.** Ayarlar sayfasından imzalı yazılım paketi kontrol edilebilir, indirilebilir veya yüklenebilir; kurulum başarısız olursa geri alınır. R3 tek tıkla dinlemeyi açıp kapatır, "otur / ayağa kalk" komutlarını tanır; Çince model dahildir, bulut hesabı gerekmez. Web üzerinden kayıt ve oynatma, "灵动" (canlı hareket) ve model yönetimi korunmuştur. Mevcut kartlar SSH ile bir kez yükseltme girişini kurar; sonrasında günlük yazılım güncellemeleri için yeniden imaj yazmak gerekmez.

Bu sürüm, 20261023c'nin ana programını, yürüyüş modelini ve veri yolu ID 200 IMU otomatik tanımasını korur. Yazılım, imzalı işlem, tarayıcı ve imajın salt okunur doğrulaması geçti; bu sürümde yeni kartın ilk kullanımı, eski kart yükseltme/geri alma ve gerçek insan sesiyle akustik doğrulama hâlâ gerçek donanımda onay bekliyor. Müziğe uyumlu kafa-gövde hareketi hâlâ düzeltilmeyi bekliyor, serbest AI sesli sohbet henüz bağlanmadı. [İmaj ve sağlama değerleri](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-replica-image-20261027) · [Yazılım yükseltme paketi](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-software-v2026.10.27) · [Güncelleme ve ses kullanımı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/软件更新与语音使用说明-20261027.md) · [Doğrulama kapsamı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/superpowers/verification/2026-10-27-web-updates.md)

<p align="center"><a href="https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/software/studio/README.md"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/studio-overview-20261025-demo.jpg" alt="Microduck Studio'nun güncel arayüz demosu, cihaz okumaları simülasyon verisidir" width="920"></a><br><sub>Studio arayüz demosu, cihaz okumaları simülasyon verisidir</sub></p>

**[İmajı indir](https://github.com/fanhao375/microduck-replica/releases/latest)** · **[İlk kullanım rehberi](17-baslangic-rehberi.md)** · **[Studio açıklaması](../software/studio/README.md)**

İmaj ücretsizdir ve yalnızca kişisel, ticari olmayan replika içindir; her bölümün lisansı için yayın sayfasına bakın. Kamera varsayılan olarak test kaynağıdır; gerçek kamera ve ToF'un doğrulama kapsamı bu sürümün açıklamasında yer alır.

---

## 🔧 Mekanik · Tek Duraktan Baskı ve Montaj

**机械行者Robo, Feetech HD-1910 ve Dynamixel XL330 olmak üzere iki malzeme setini sürekli bakımda tutuyor.** Modeller, baskı projeleri ve güncelleme notları CAD deposunda toplanmıştır; kendi servo sürümünüze göre seçin.

| Neye ihtiyaç var | Giriş |
|---|---|
| **Tek duraktan baskı** | **[Bambu Lab MakerWorld (Feetech sürümü)](https://makerworld.com.cn/zh/models/2963569-microduck#profileId-3478428)** · [Bambu Studio 3MF projesi](https://github.com/fanhao375/microduck-replica-cad#打印) |
| **Modeller ve baskı malzemeleri** | **[Feetech HD-1910 bölümü](https://github.com/fanhao375/microduck-replica-cad#飞特-hd-1910-打印资料)** · **[XL330 bölümü](https://github.com/fanhao375/microduck-replica-cad#dynamixel-xl330-打印资料)** |
| **Montaj eğitimi** | **[Montaj kılavuzu PDF](https://github.com/fanhao375/microduck-replica-cad/blob/master/安装说明书/microduck装配安装说明书.pdf)** · **[Bölüm bölüm videolar](#-montaj-video-eğitimi)**; iki sürüm, ilgili yapısal parçalara göre monte edilir |
| **Satın alma listesi** | **[BOM çevrimiçi önizleme](02-malzeme-listesi-bom.md)** · **[Excel indir](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/BOM/装配BOM-机械行者Robo-2026-10-23-带采购链接.xlsx)**: 2026-10-23 Feetech sürümü; XL330'un servoları ve ilgili elektroniği ayrıca kontrol edilmelidir |

[CAD deposu ve son yayınlar](https://github.com/fanhao375/microduck-replica-cad/releases) · [Yapım günlüğü](16-yapim-gunlugu.md)

---

## 🔌 Elektrik · Beş Devre Kartı

Bu depo; veri yolu IMU kartı, servo veri yolu HUB'ı ve batarya arayüz kartı için proje malzemelerini sunar; ana kart olarak Radxa **ZERO 3W**, genişletme kartı olarak da Pollen Robotics'in resmî açık kaynak **RPI Robot HAT**'i kullanılır.

<table>
<tr>
<th>Veri yolu IMU kartı</th>
<th>Servo veri yolu HUB'ı</th>
<th>Batarya arayüz kartı</th>
<th>Radxa ana kart<br>ZERO 3W</th>
<th>Resmî HAT<br>RPI Robot HAT</th>
</tr>
<tr>
<td align="center" valign="middle" width="170"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/imu-to-dxl-1v0a-3d.png"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/imu-to-dxl-1v0a-3d.png" alt="Veri yolu IMU kartı 3B tasarım önizlemesi" width="160"></a></td>
<td align="center" valign="middle" width="170"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/wire-hub-1v0a-3d.png"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/wire-hub-1v0a-3d.png" alt="Servo veri yolu HUB'ı 3B tasarım önizlemesi" width="160"></a></td>
<td align="center" valign="middle" width="170"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/pogo-pin-1v0a-3d.png"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/pogo-pin-1v0a-3d.png" alt="Batarya arayüz kartı 3B tasarım önizlemesi" width="160"></a></td>
<td align="center" valign="middle" width="170"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/radxa-zero3w-official.webp"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/radxa-zero3w-official.webp" alt="Radxa resmî ZERO 3W kart görseli" width="160"></a></td>
<td align="center" valign="middle" width="170"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/rpi-robot-hat-official.png"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/rpi-robot-hat-official.png" alt="Pollen Robotics resmî RPI Robot HAT tasarım görseli" width="160"></a></td>
</tr>
<tr>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/imu-to-dxl-1v0a-pcb.png">PCB önizleme</a><br><a href="https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/imu_to_dxl_1V0A/">Proje dosyaları</a></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/wire-hub-1v0a-pcb.png">PCB önizleme</a><br><a href="https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/wire_hub_1V0A/">Proje dosyaları</a></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/pogo-pin-1v0a-pcb.png">PCB önizleme</a><br><a href="https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/新版/POGO_PIN_1V0A/">Proje dosyaları</a></td>
<td align="center" valign="top"><a href="https://item.taobao.com/item.htm?id=763812025816">Satın al (Taobao)</a><br><a href="https://docs.radxa.com/en/zero/zero3">Resmî dokümanlar</a> · <a href="https://docs.radxa.com/en/zero/zero3/download#hardware-design">Tasarım dosyaları</a></td>
<td align="center" valign="top"><a href="https://github.com/pollen-robotics/elec_RPI_Robot_HAT">KiCad projesi</a><br><a href="https://github.com/pollen-robotics/elec_RPI_Robot_HAT/tree/main/production">Üretim/prototip dosyaları</a></td>
</tr>
</table>

İlk üç görsel özel yapım kartların 3B tasarım önizlemeleridir; Radxa ve HAT görselleri resmî dokümanlardan alınmıştır. Orijinal görseli görmek için resme tıklayın, [görsel kaynakları](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/official-board-images.md). Radxa tasarım malzemeleri şema, 2B ölçüler ve 3B model içerir; üç özel kartın JLCPCB EDA (EasyEDA) projeleri, STEP dosyaları ve gerçek ölçüm ilerlemesi ilgili proje açıklamalarındadır.

[Tüm donanım projeleri](13-devre-kartlari.md) · [Üç kartın açıklaması](13-devre-kartlari.md#2-yeni-sürüm-donanım-2026-10-kaynak-hardware新版readmemd) · [Veri yolu IMU firmware'i](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/README.md)

---

## 🧠 Algoritma · Feetech Resmî BAM

[**Feetech resmî HD-1910 BAM**](https://gitee.com/ftservo/ftservo-bam), servo dinamiği modeli ve tanımlama (identification) parametrelerini sağlar; simülasyon eğitimi için referanstır. Bu depo açık kaynak [eğitim projesini](../software/training/README.md) ve [web eğitim çalışma alanını](../software/training-studio/README.md) sunar; belirli model yapılandırması ve parametre kaynakları için [parametre açıklamasına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD-1910-M6参数来源.md) bakın.

---

## 🖥️ Açık Kaynak Eğitim Platformu · Microduck Training Studio

Ayrıca **Microduck Training Studio**'yu da yaptık: Bilgisayarda web üzerinden eğitim deneyi oluşturabilir, eğrileri görüntüleyebilir, duraklatıp devam ettirebilir, kontrol noktalarını (checkpoint) değerlendirebilir ve ONNX modeli dışa aktarabilirsiniz. Eğitim çalışma alanı, ördeğin üzerindeki Studio'dan bağımsız iki ayrı servistir.

<p align="center"><a href="https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/software/training-studio/README.md"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/training-studio-20261025-demo.jpg" alt="Microduck Training Studio gerçek arayüzü: 3B model, eğitim kontrolleri ve sentetik demo eğrileri" width="920"></a><br><sub>Eğitim platformu demo arayüzü: 3B model önizlemedir, eğriler sentetik demo verisidir</sub></p>

Gerçek GPU ile kısa deneme eğitimi, değerlendirme oynatma ve model dışa aktarma zinciri doğrulandı; uzun eğitim ve kendi eğittiğiniz politikanın gerçek robotta doğrulanması henüz tamamlanmadı.

**[Eğitim platformu ve kullanım açıklaması](../software/training-studio/README.md)** · **[Hareket laboratuvarı rehberi](../software/training-studio/web/custom-actions.md)** · **[Eğitim projesi](../software/training/README.md)** · [Doğrulama kaydı](../software/training-studio/docs/verification.md)

---

## 🧰 Araçlar · Kart Yazma, Hata Ayıklama ve Malzemeler

Sık kullanılan yazılım ve geliştirme araçları [araç gezgininde](../tools/README.md) toplanmıştır; yapmak istediğiniz işe göre seçin.

| Ne yapılacak | Araç ve giriş |
|---|---|
| İmaj yazma | **[Rufus taşınabilir EXE](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/tools/rufus/rufus-4.15p.exe)** · [Kart yazma açıklaması](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/tools/rufus/README.md) |
| Seri port ve servo hata ayıklama | **[Feetech FD ve seri port yardımcısı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/tools/飞特/README.md)** · [3B web hata ayıklama paneli](../tools/servo-web/README.md) |
| Feetech malzemeleri, SDK entegrasyonu | **[Resmî kılavuzlar, model veri sayfaları ve SDK](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/飞特资料/README.md)**; resmî site sürümü ve çevrimdışı kopya tarihi belirtilmiştir |
| Servo testi, sorun analizi | [HD1910M test aracı](../tools/FeeTech_HD1910M_Servo/README.md) · [STS3215 test aracı](../tools/sts3215Servo_testtool/README.md) · [Yürüyüş (gait) analizi](../tools/gait-analysis/README.md) |

---

## 🦆 Ördek Meraklılarının Katkıları

Bu depo tek kişinin eseri değil. Birleştirilen kodlar ve gerçek robotta doğrulanmış sonuçlar buraya kaydedilir.

| Kim | Ne katkıda bulundu |
|---|---|
| [@yoyojacky](https://github.com/yoyojacky) | **Rust ile yazılmış Feetech servo test aracı** ([PR #27](https://github.com/fanhao375/microduck-replica/pull/27), birleştirildi). Kendi yazdığı asgari STS/SCS protokolü (çerçeve paketleme, sağlama toplamı (checksum), ping, register okuma/yazma, durum ayrıştırma); komut satırından veri yolunu tarayabilir (ilerleme çubuğuyla), durum okuyabilir, belirli bir konuma döndürebilir, tekil ve toplu test yapabilir, konum sapmasını, tepe akımı, tepe yükü, gerilim ve sıcaklığı çıktı olarak verip PASS/FAIL kararı verir. Test tezgâhında kabul testi tek komutla özet tablo üretir → [`tools/sts3215Servo_testtool/`](../tools/sts3215Servo_testtool/) |
| [@Abo1ish](https://github.com/Abo1ish) | **IMU kartı firmware'i + hata ayıklama panelinde duruş gösterimi** ([PR #32](https://github.com/fanhao375/microduck-replica/pull/32), birleştirildi). Resmî olarak açık kaynak yapılmamış imu_to_dxl kartı için STM32G031 firmware temeli yazdı; gerçek kartta doğrulandı, host tarafı testleri ve sınırları net yazılmış bir [`VALIDATION.md`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/firmware/VALIDATION.md) ile birlikte → [`hardware/imu_to_dxl/firmware/`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/firmware/); ardından J-Link ile IMU duruşunu gerçek zamanlı okuyup web hata ayıklama paneline ekledi, 3B ördeğin gövdesi gerçek kartla birlikte dönüyor (`--imu-jlink`; kart yoksa önce `--imu-demo` ile etkiyi görebilirsiniz) → [`tools/servo-web/`](../tools/servo-web/) |
| WeChat grubundaki ördek meraklıları | **Radxa Zero 3W V1.12J için önyükleme (boot) çözümü.** Bu partideki kartlarda (WiFi AIC8800DS2 ile değiştirilmiş) yalnızca Radxa bootloader'ını değiştirmek yetmedi, cihaz ağacının (DTB) da Radxa B1'inkiyle değiştirilmesi gerektiğini denemeyle buldu: **B1 bootloader + B1 DTB + Armbian 6.1.115 çekirdeği + Trixie sistemi** ile çalıştırıldı → [tuzaklar kaydına](14-tuzaklar.md) ve [imaj kullanım açıklamasına](11-radxa-imaj-kullanimi.md) yazıldı |

---

## Ördek Meraklılarının Projeleri

Bazı ördek meraklıları kendi depolarını ayrı açtı; bu depoda yer almıyor ama ördekle doğrudan ilgili ve iyi yapılmış olanları buradan tanıtıyoruz:

| Proje | Yazar | Ne işe yarar |
|---|---|---|
| [microduck-color-studio](https://github.com/LathamZ/microduck-color-studio) ([çevrimiçi dene](https://lathamz.github.io/microduck-color-studio/)) | [@LathamZ](https://github.com/LathamZ) | **Ördeğin 3B renk stüdyosu; baskıdan önce renkleri web üzerinde belirleyin.** 70 parçayı tek tek boyayın, malzeme (PLA / mat / PETG / metalik / karbon fiber / TPU) ve ışık seçerek etkisini görün; elinizde hangi filamentlerin olduğunu girin, stoğa göre renk önerir (yalnızca mevcutlar / bir renk ekle / akrilik vurgu). Kendi 3MF dosyanızı da (örneğin Feetech sürümü) içe aktarabilir, **renkli çok plakalı 3MF** ve parça parça ayrılmış STL dışa aktarabilirsiniz; Bambu P1S / A1 mini / H2D için hazır ayarlar var. Çince/İngilizce arayüz, telefonda da görüntülenebilir |
| [MICDUCK_FTHD1901_REBUILD](https://github.com/fengj4780-sudo/MICDUCK_FTHD1901_REBUILD) | [@fengj4780-sudo](https://github.com/fengj4780-sudo) | **Feetech sürümü yapısal iyileştirme + isteğe bağlı CNC takviye parçaları.** Bizim [düzenlenebilir SolidWorks çizimlerimiz](https://github.com/fanhao375/microduck-replica-cad) üzerine devam edildi: Feetech servoya uyarlandı (deposunda HD1901 olarak yazılmış, parça dosyaları ise HD-1910-C001 kullanıyor), zayıf parçalar güçlendirildi, montaj çakışmaları ve birkaç bozuk model düzeltildi. Bacaktaki **5 parça CNC parçayla değiştirilebilir**, böylece yük daha uygun taşınır (hâlâ prototip testi aşamasında, 5 parçanın kargo dahil yaklaşık 45 yuan olacağını tahmin ediyor); CNC yapmayıp doğrudan basmak da mümkün, mukavemet yine orijinalinden iyi. Tek tıkla baskı için 3MF (Bambu H2D, 0.4 mm, 5 plaka) ve düzeltilmiş SolidWorks çizimleri ekli |
| [Microduck-kissqy](https://github.com/kissqy/Microduck-kissqy) | [@kissqy](https://github.com/kissqy) | **Feetech HD1910 için eğitim süreci ve kontrol uygulaması referansı.** Eğitim kontrol paneli, eğitim ortamı hazırlama ve görev yönetimi açıklamaları, ONNX model dışa aktarma ile robot kontrol paneli, firmware ve demo videoları sunar; algoritma kısmındaki ayrıntılı eğitim süreci için bu proje önerilir |

Ördekle ilgili bir proje yaptıysanız (araç, eğitim, modifikasyon, politika…), bir issue açıp bağlantısını bırakın, ekleyelim.

Katılmak için: doğrudan bir [issue](https://github.com/fanhao375/microduck-replica/issues) açın veya PR gönderin.
Donanım, firmware, algoritma, doküman, gerçek ölçüm verisi hepsi sayılır — **gerçek ölçüm verileri özellikle makbul**; bu deponun kuralı, sonuçların olumlu da olsa olumsuz da olsa olduğu gibi kaydedilmesidir.

---

## Malzeme Dizini

Yollar bu deponun köküne göredir; mekanik CAD ayrı bir depoda tutulur.

| Konu | Depodaki yer | Açıklama ve giriş |
|---|---|---|
| Kullanım ve montaj | [CAD deposu](https://github.com/fanhao375/microduck-replica-cad) · [BOM/](02-malzeme-listesi-bom.md) | [İlk kullanım rehberi](17-baslangic-rehberi.md) · [Satın alma listesi](02-malzeme-listesi-bom.md) · [Montaj videoları](#-montaj-video-eğitimi) |
| Yazılım ve imaj | [software/](../software/README.md) | [Studio kontrol paneli](../software/studio/README.md) · [İmaj derleme](../software/image/README.md) |
| Eğitim platformu ve proje | [software/training-studio/](../software/training-studio/README.md)<br>[software/training/](../software/training/README.md) | Web eğitim çalışma alanı, simülasyon ortamı ve model dışa aktarma |
| Elektrik ve firmware | [hardware/](13-devre-kartlari.md) | [Devre kartı projeleri](13-devre-kartlari.md) · [IMU firmware'i](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/README.md) |
| Hata ayıklama ve analiz araçları | [tools/](../tools/README.md) | [Araç gezgini](../tools/README.md) · kart yazma, seri port hata ayıklama, Feetech malzemeleri ve analiz betikleri |
| Dokümanlar ve kayıtlar | [docs/](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/README.md) | [Tam doküman dizini](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/README.md) · [Tuzaklar](14-tuzaklar.md) · [Hata ayıklama](15-hata-ayiklama-kayitlari.md) · [Yapım](16-yapim-gunlugu.md) |
| Geçmiş ve topluluk | [docs/](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/README.md#深入研究与归档) | [Resmî güncelleme takibi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/官方更新跟踪.md) · [Geçmiş güncellemeler](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/历史更新.md) · [Topluluk katkıları](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/社区贡献.md) |

---

## Lisans ve Kaynaklar

Kod, simülasyon materyalleri ve imaj içindeki modeller kendi lisanslarına tabidir; ayrıntılar için bkz. [lisans ve atıf](00-orijinal-lisans-ve-atif.md) ve [model kullanım koşulları](../software/image/overlay/usr/share/doc/microduck/模型说明.txt). **Replika imajı yalnızca kişisel, ticari olmayan replika içindir; ücretli ürünlerle birlikte dağıtılamaz.**

Bu proje Pollen Robotics ile bağlantılı değildir ve onun tarafından onaylanmamıştır.

### ❤️ Yazara Destek

Montajdan hata ayıklamaya, yazılımdan dokümana kadar bu proje defalarca denenerek birikti. Bu malzemeler ve araçlar size yardımcı olduysa Star ⭐ vermeniz, sorun bildirmeniz veya replika deneyiminizi paylaşmanız çok makbule geçer; ayrıca isteğe bağlı bağış yaparak yazara bir kahve ısmarlayıp projenin bakımına destek olabilirsiniz. Her ördek meraklısına teşekkürler.

<p align="center"><a href="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/alipay-support.jpg"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/alipay-support.jpg" alt="Alipay bağış karekodu, orijinal görseli görmek için tıklayın" width="240"></a><br><sub>Alipay ile karekod tarayarak destek · Orijinal görseli görmek için resme tıklayın</sub></p>

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
