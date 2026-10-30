# Feetech Sürümü Montaj Satın Alma Listesi

**Hazırlayan: 机械行者Robo · 2026-10-23 sürümü**

**[Tam Excel dosyasını indir](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/BOM/装配BOM-机械行者Robo-2026-10-23-带采购链接.xlsx)** · [Baskı parçaları ve CAD](https://github.com/fanhao375/microduck-replica-cad) · [Ana depo](https://github.com/fanhao375/microduck-replica)

Bu sayfa, aynı sürümün Excel dosyasından derlenmiştir; **33 baskı parçası ve 23 satın alınan parça** içerir. Adetler, malzemeler, notlar, fiyatlar ve satın alma bağlantıları orijinal tablodaki gibi korunmuştur.

**Geçerli sürüm: Feetech HD-1910 yapısı.** Liste, Feetech servoları ve URT2 programlama/test kartını içerir; XL330 sürümü için servolar ve ilgili elektronik ayrıca kontrol edilmelidir. Excel'in orijinal dosyası değiştirilmemiştir.

[Baskı parçalarına git](#1-baskı-parçaları-33-kalem) · [Satın alınan parçalara git](#2-satın-alınan-parçalar-23-kalem) · [Orijinal tablo notları ve doğrulanacak noktalar](#3-orijinal-tablo-notları-ve-doğrulanacak-noktalar)

## 1. Baskı parçaları (33 kalem)

Baskı modellerini [CAD deposundan](https://github.com/fanhao375/microduck-replica-cad) kendi servo sürümünüze uygun olarak seçin. Malzemeyi ayrıca o sürümün baskı açıklamasıyla karşılaştırın; aşağıdaki tabloda Excel'deki orijinal metin gösterilmektedir. (Dosya adlarındaki Çince bölümler orijinaldir ve değiştirilmemiştir.)

**Tüm baskı parçaları seti için fiyat kaydı: 139 yuan** (¥ = Çin yuanı), orijinal tablodaki birleştirilmiş I3:I35 alanına karşılık gelir; [satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?from=cart&id=1083122166800&mi_id=0000ywbZ5efl4VxxIGb0KHx-3C8BOS37n90MGBh_xmncHd4&skuId=6306393642451&spm=a1z0d.6639537%2F202410.item.d1083122166800.70527484LqKlHG&upStreamPrice=13900>).

| No | Ad | Orijinal dosya adı | Malzeme (orijinal tablo) | Adet | Not (orijinal tablo) |
|---|---|---|---|---:|---|
| 1 | Kafa üst kabuk | top_head_shell_头部上壳.stp | PLA | 1 |  |
| 2 | Kafa alt kabuk | bottom_head_shell_头部下壳.stp | PLA | 1 |  |
| 3 | Yüz parçası | face_part_面部零件.stp | PLA | 1 |  |
| 4 | Çene | jaw_下巴.stp | PLA | 1 |  |
| 5 | Yumuşak çene | jaw_soft_软下巴.stp | PLA | 1 | TPU esnek filament önerilir |
| 6 | Yumuşak gaga üstü | soft_mouth_top_软嘴顶部.stp | PLA | 1 | TPU esnek filament önerilir |
| 7 | Gözler | noenoeil_眼睛.stp | PLA | 1 |  |
| 8 | Boyun | neck_颈部.stp | PLA | 2 | Alüminyum alaşım önerilir |
| 9 | Boyun eğim (pitch) | neck_pitch_颈部俯仰.stp | PLA | 1 |  |
| 10 | Gövde tabanı | trunk_base_躯干底座.stp | PLA | 1 | Alüminyum alaşım önerilir |
| 11 | Sol kabuk | left_shell_左壳.stp | PLA | 1 |  |
| 12 | Sağ kabuk | right_shell_右壳.stp | PLA | 1 |  |
| 13 | Kalça sol | hip_l_髋部左.stp | PLA | 2 |  |
| 14 | Yaw'dan roll'a dönüşüm | yaw2roll_偏航转横滚.stp | PLA | 1 |  |
| 15 | Yaw-roll hareketi | yaw_roll_motion_偏航横滚运动.stp | PLA | 1 |  |
| 16 | Bacak | leg_腿部.stp | PLA | 2 |  |
| 17 | Sol üst bacak | left_upper_leg_左上腿.stp | PLA | 1 |  |
| 18 | Sağ üst bacak | right_upper_leg_右上腿.stp | PLA | 1 |  |
| 19 | Üst bacak takviye plakası | upper_leg_rigidity_plate_上腿加固板.stp | PLA | 2 | Alüminyum alaşım önerilir |
| 20 | Sol ayak | foot_left_左脚.stp | PLA | 1 |  |
| 21 | Sağ ayak | foot_right_右脚.stp | PLA | 1 |  |
| 22 | Sol taban | sole_left_左脚底.stp | PLA | 1 |  |
| 23 | Sağ taban | sole_right_右脚底.stp | PLA | 1 |  |
| 24 | Bilek sol | ankle_left_脚踝左.stp | PLA | 1 |  |
| 25 | Bilek sağ | ankle_right_脚踝右.stp | PLA | 1 |  |
| 26 | Bilek sol (V1 alternatif) | ankle_l_v1_脚踝左V1.stp | PLA | 1 |  |
| 27 | Bilek sağ (V1 alternatif) | ankle_r_v1_脚踝右V1.stp | PLA | 1 |  |
| 28 | Birleşik lastik | 合体轮胎.stp | PLA | 4 |  |
| 29 | Tekerlek kanadı | roller_blade_滚轮叶片.stp | PLA | 2 |  |
| 30 | Motor desteği | motor_support_电机支架.stp | PLA | 1 |  |
| 31 | Güç (batarya) desteği | power_support_电源支架.stp | PLA | 1 |  |
| 32 | Muz biçimli PCB kilidi | banana_pcb_locker_香蕉形PCB锁扣.stp | PLA | 1 |  |
| 33 | Rulmanlı tekerlek | bearing_roll_轴承滚轮.stp | PLA | 2 | Alüminyum alaşım önerilir |

## 2. Satın alınan parçalar (23 kalem)

Fiyat birimi yuandır (¥); değerler orijinal tabloda kayıtlı sayılar olarak gösterilmiştir. Satın alma bağlantılarına doğrudan tıklanabilir; Excel'de adres girilmemiş kalemler "Orijinal tabloda girilmemiş" olarak işaretlenmiştir.

| No | Ad | Kategori | Adet | Birim fiyat | Toplam fiyat (orijinal tablo) | Not (orijinal tablo) | Satın alma girişi |
|---|---|---|---:|---:|---:|---|---|
| 1 | Radxa Zero 3W ana kart | Elektronik parça | 1 | 309 | 309 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?id=763812025816&last_time=1790655696&mi_id=0000M9KvAKZdKHX6irXd93nZ9S8044VLMp9XHfosSxlXgV0&scm=1007.13982.82927.0&spm=tbpc.mytb_footmark.item.goods&upStreamPrice=88800>) |
| 2 | 64GB TF (microSD) kart | Elektronik parça | 1 | 60 | 60 |  | Orijinal tabloda girilmemiş |
| 3 | Raspberry Pi robot HAT devre kartı | Elektronik parça | 1 | 120 | 120 | Ortak (grup) sipariş mümkün, GitHub | [Proje girişi (GitHub)](<https://github.com/fanhao375/microduck-replica>) |
| 4 | imu_to_dxl devre kartı | Elektronik parça | 1 | 80 | 80 | Ortak (grup) sipariş mümkün, GitHub | [Proje girişi (GitHub)](<https://github.com/fanhao375/microduck-replica>) |
| 5 | Feetech HD1901M servo | Elektronik parça | 15 | 95 | 1425 | Ortak (grup) sipariş mümkün, GitHub | [Proje girişi (GitHub)](<https://github.com/fanhao375/microduck-replica>) |
| 6 | Feetech servo URT2 programlama/test kartı | Elektronik parça | 1 | 45 | 45 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?spm=a1z0d.6639537%2F202410.item.d575365901461.511774843C6ViG&id=575365901461&xxc=shop&from=cart&skuId=5435424470243&mi_id=0000xzcmwFVCRAh37nhTBqqPxAc4BB-aXBAZs9-SHZnxT_s>) |
| 7 | NP-F550 batarya | Elektronik parça | 1 | 17 | 47 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?adType=orgqzt&from=cart&id=769425140324&mi_id=00009VN3uJH9Mvl1nh6sR6uszyaiYL6FFhvjGBj6PAaJbUg&skuId=5445604550341&spm=a1z0d.6639537%2F202410.item.d769425140324.5a377484k96nZS&upStreamPrice=5500&xxc=qzt_taobaoSearch>) |
| 8 | AMP2.0 çift uçlu dönüşüm kablosu, microduck servo kablosu | Elektronik parça | 1 | 2 | 2 | Hata ayıklama için | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?id=1089647066599&mi_id=0000KqIW0wThzcfg1FqUc6VdYVF2XtZv0Ep94yoyuJ-fYl8&pvid=a7a9bbc1-3e60-439d-90a4-0d4fdd081d6d&scm=1007.54964.509742.0&skuId=6146736860515&spm=pc_detail.30350276.201876.d4.18bd7dd6DvXX58&utparam=%7B%22x_object_type%22%3A%22item%22%2C%22matchType%22%3A%22MAIN_SWING_I2I%22%2C%22item_price%22%3A%222%22%2C%22umpCalled%22%3Atrue%2C%22pc_scene%22%3A%2220001%22%2C%22userId%22%3A1038948925%2C%22ab_info%22%3A%2244964%23509742%23-1%23%22%2C%22tpp_buckets%22%3A%2244964%23509742%23-1%23%22%2C%22aplus_abtest%22%3A%22fe88f406097dbf1addeadb9550070432%22%2C%22isLogin%22%3Atrue%2C%22abid%22%3A%220%22%2C%22pc_pvid%22%3A%22a7a9bbc1-3e60-439d-90a4-0d4fdd081d6d%22%2C%22isWeekLogin%22%3Afalse%2C%22rn%22%3A3%2C%22item_ecpm%22%3A0%2C%22ump_price%22%3A%222%22%2C%22isXClose%22%3Afalse%2C%22x_object_id%22%3A1089647066599%7D&xxc=home_recommend>) |
| 9 | 2.5mm muz (banana) fişi, PCB tipi, altın kaplama bakır | Elektronik parça | 2 | 1.6 | 3.2 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?from=cart&id=1066300439603&mi_id=0000idrzZ0iZmNePV-H8uLJ0q--7Nuk50iH4KmlQjt7l16Q&skuId=6116801109787&spm=a1z0d.6639537%2F202410.item.d1066300439603.20807484wDo29i&upStreamPrice=160>) |
| 10 | banana PCB | Elektronik parça | 1 | 20 | 20 |  | JLCPCB |
| 11 | IMX219 kamera modülü | Optik parça | 1 | 46.8 | 46.8 |  | [Satın alma bağlantısı (Tmall)](<https://detail.tmall.com/item.htm?id=775872575316>) |
| 12 | VL53L8CX ToF modülü | Elektronik parça | 1 | 49.5 | 49.5 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?from=cart&id=737603917521&mi_id=0000svFiYCCRNyTplS2syupd6wPqm_3g253yiYEiJIUzYWg&skuId=5090650052053&spm=a1z0d.6639537%2F202410.item.d737603917521.12a97484LeTNU7&upStreamPrice=4950>) |
| 13 | Hoparlör | Elektronik parça | 1 | 3.8 | 3.8 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?ali_refid=a3_430673_1006%3A1300920180%3AH%3AXe0d%2B%2ByvvuheeXXsNbtAzA%3D%3D%3A1fb351596f290624d1f838f6933a4bf9&ali_trackid=318_1fb351596f290624d1f838f6933a4bf9&id=902489608878&loginBonus=1&mi_id=00004qd77Ss-NI_QwEGJk3oQMSCKLeGBjvYFB1womY2KPUQ&mm_sceneid=0_0_1169600180_0_0&priceTId=2100c91217905892639744554e0a2f&skuId=5925223242747&spm=a21n57.sem.item.52&utparam=%7B%22aplus_abtest%22%3A%221116d3394ed69d4d6ae8676cf27ec828%22%7D&xxc=ad_ztc>) |
| 14 | Rulman 10×15×3 | Standart parça | 3 | 2.8 | 8.4 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?id=670727787832>) |
| 15 | Rulman 16×22×4 | Standart parça | 11 | 3.5 | 38.5 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?id=539024647147&skuId=5716548727712>) |
| 16 | Rulman 6×12×3 | Standart parça | 4 | 0.88 | 3.52 | Paten rulmanı | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?abbucket=2&id=963037239628&loginBonus=1&mi_id=00009MRQFjdPW6cwLc4VvA6iVYQgy2Qaevxz6dOGm9D1myw&ns=1&priceTId=213e0a2917895687271465994e0fd6&skuId=6068333830994&spm=a21n57.sem.item.1.40ad3903YwCCZ2&utparam=%7B%22aplus_abtest%22%3A%22633f8c365e71a9c062ec49e542a73279%22%7D&xxc=taobaoSearch>) |
| 17 | Sac vidası, düz başlı M2×5 | Standart parça | 1 paket | 3.05 | 3.05 |  | [Satın alma bağlantısı (Tmall)](<https://detail.tmall.com/item.htm?id=534923831046&mi_id=0000lLHxCRqtZ8_pqc3QGIagm4EgOL8KYhEEg_ZEZdQEaCI&spm=tbpc.boughtlist.suborder_itemtitle.1.c3892e8dY9OLZg>) |
| 18 | Sac vidası, düz başlı M2×6 | Standart parça | 1 paket | 4.05 | 4.05 |  | [Satın alma bağlantısı (Tmall)](<https://detail.tmall.com/item.htm?id=534923831046&mi_id=0000lLHxCRqtZ8_pqc3QGIagm4EgOL8KYhEEg_ZEZdQEaCI&spm=tbpc.boughtlist.suborder_itemtitle.1.c3892e8dY9OLZg>) |
| 19 | Sac vidası, düz başlı M2×8 | Standart parça | 1 paket | 4.05 | 4.05 |  | [Satın alma bağlantısı (Tmall)](<https://detail.tmall.com/item.htm?id=534923831046&mi_id=0000lLHxCRqtZ8_pqc3QGIagm4EgOL8KYhEEg_ZEZdQEaCI&spm=tbpc.boughtlist.suborder_itemtitle.1.c3892e8dY9OLZg>) |
| 20 | Sac vidası, düz başlı M2.5×6 | Standart parça | 1 paket | 3.93 | 3.93 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?spm=a1z0d.6639537%2F202410.item.d534923831046.10db74840oHq5F&id=534923831046&from=cart&skuId=5947341310639&mi_id=0000RGt64BzUSirBb2ZGiESDHLYHZCCldpvt2pjiQe6DwTE&upStreamPrice=700>) |
| 21 | Sac vidası, düz başlı M2.5×8 | Standart parça | 1 paket | 2.08 | 2.08 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?spm=a1z0d.6639537%2F202410.item.d534923831046.10db74840oHq5F&id=534923831046&from=cart&skuId=5947341310640&mi_id=0000RGt64BzUSirBb2ZGiESDHLYHZCCldpvt2pjiQe6DwTE&upStreamPrice=700>) |
| 22 | Loctite 243 vida sabitleyici | Standart parça | 1 | 9 | 9 |  | [Satın alma bağlantısı (Taobao)](<https://item.taobao.com/item.htm?adType=orgqzt&from=cart&id=1056442610986&mi_id=0000wOojFoJyiP5dQudTpjmjzfZLEEq7GLdMEB8DaDqMa7Y&skuId=6099342537028&spm=a1z0d.6639537%2F202410.item.d1056442610986.44d57484Ny8pKV&upStreamPrice=900&xxc=qzt_taobaoSearch>) |
| 23 | Ayakkabı tabanı kaymaz ped | Standart parça | 1 | 16 | 16 |  | [Satın alma bağlantısı (Tmall)](<https://detail.tmall.com/item.htm?id=888852278057&mi_id=0000Bug6nFYlEVkT2CGWMwXKqUSbi-0G_VP4pnfiGwBOnrU&spm=tbpc.boughtlist.suborder_itemtitle.1.c3892e8dY9OLZg&skuId=5902232407790>) |

## 3. Orijinal tablo notları ve doğrulanacak noktalar

**Orijinal tablo toplamı: 2426.88 yuan.** Excel'in orijinal dosyası değiştirilmemiştir; aşağıdaki iki noktanın kontrol edilmesi gerekir:

- Toplam formülü `SUM(I3:I58)` olup son kalem olan "ayakkabı tabanı kaymaz ped"i (I59, 16 yuan) içermemektedir.
- "NP-F550 batarya" satırında adet 1, birim fiyat 17 yuan, toplam fiyat 47 yuandır; birim fiyat ile toplam fiyat tutarsızdır.

<details>
<summary>Yazarın Excel'e eklediği orijinal açıklamayı göster</summary>

Açıklama:
🦆 Herkes kendi MicroDuck'ına sahip olabilir!

💰 Proje maliyeti açıklaması
15 servo, HAT kartı ve IMU kartı dışındaki donanımın maliyeti yaklaşık 828 yuandır.
15 servo, HAT kartı ve IMU kartı için GitHub projesi üzerinden ortak (grup) siparişe katılabilir veya ihtiyaca göre JLCPCB, Taobao gibi platformlardan kendiniz satın alabilirsiniz.
İlerleyen dönemde, herkesin MicroDuck'ı daha kolay monte edip hata ayıklayabilmesi için montaj eğitimi ve hata ayıklama eğitimi de açık kaynak olarak yayımlanacaktır.
🤖 Neden açık kaynak?

Daha fazla insanın düşük maliyetle somutlaşmış zekâ (embodied AI), robot kontrolü ve pekiştirmeli öğrenme ile tanışıp öğrenebilmesini istiyoruz.

Herkesin kendi ördeği olsun.

Açık kaynak sayesinde, daha fazla insanın uygulamalı çalışıp sıfırdan somutlaşmış zekâyı keşfedebileceği daha açık ve dostane bir öğrenme ortamını birlikte kurmayı hedefliyoruz.

Bu proje size yardımcı olduysa beğeni bırakmak bize verebileceğiniz en büyük destektir ❤️

GitHub hesabımızı takip edip bir Star ⭐ vermeniz de çok makbule geçer!

🔗 GitHub:
https://github.com/fanhao375/microduck-replica

📕 Xiaohongshu: 机械行者
🎵 Douyin: 机械行者Robo
Bilibili: 机械行者Robo

</details>

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
