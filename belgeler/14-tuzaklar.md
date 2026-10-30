# Tuzaklar ve Yaşanmış Sorunlar

Replika yapımı sırasında gerçekten yaşanmış sorunlar; **her maddede üç cümle: belirti, neden, ne yapılmalı**. Aşamalara göre ayrılmıştır, işe başlamadan önce bir göz gezdirin.

Analiz ve kanıtlar başka belgelerde, burada yalnızca sonuçlar yer alıyor. Yeni bir tuzakla karşılaşırsanız ilgili aşamanın altına ekleyin, düz ve anlaşılır yazın.

> Mekanik süreç [yapım günlüğünde](16-yapim-gunlugu.md), elektrik ve yazılım süreci [hata ayıklama kayıtlarında](15-hata-ayiklama-kayitlari.md). Son eklemeler: 2026-10-20～21, replika imajının gerçek robotta kabulü: fork kalibrasyon modu sürekli "başlatılıyor" diyor, Clash açıkken `.local` açılmıyor, imajda SSH ana makine anahtarı oluşmamış, hepsini atla deyince hareket moduna geçilemiyor, kalibrasyon modunda robot ayağa kalkamıyor (hold-home eklendi), hotspot geç çıkıyor; araçlara GitHub yayını ve ana sayfa kartı için iki madde eklendi; 2026-10-15 akşamı, "iki üç adım atınca düşme" sorununun kök nedeni BNO085'in kendi duruş (attitude) verisinin zıplamasıydı, jiroskop integrasyonuyla düzeltildi; inceleme önce verinin kendi içinde tutarlı olup olmadığına bakmalı; sıçrama tespitinde kullanılan ölçü gecikmeyle hizalanmalı; dönüş zayıf (henüz çözülmedi); tüm sistemin yeniden başlaması ve G50 eşleşmesi için birer madde eklendi; 2026-10-14 akşamı, kissqy V167 artık yükleme sırasında D=0 ve tork 1000 yazıyor (IMU modülü kullananlar doğrudan yükseltmesin); 2026-10-14 gün içi, servo parametreleri RAM'de yazılı (güç uygulanmışken robotd yeniden başlatılırsa kalıntı kalır), iki ayağın sol-sağ yönde aynı düzlemde olmaması iki kalça roll ekleminin dışa açılmasından kaynaklanıyor (vücut ağırlığının bastırdığı tahmin ediliyor), ağız servosu çok ısınıyor, yeni sürümdeki "gamepad bağlantısını onar" yalnızca GameSir (盖世小鸡) (盖世小鸡) modelini tanıyor, "Firmware yükle / yükselt" a tıklamayın, ayak tabanı TPU 95A fazla sert, simülasyon karşılaştırmasında önce ölçek ve filtre ağırlıklarını hizalayın; 2026-10-13 gecesi～10-14, servo D değeri yürürken titreme yapıyor, V164 D ve tork sınırı yazmıyor, yürürken tüm sistemin gücünün kesilmesi besleme kaynaklı, yeni kartta G50 Pro eşleşir eşleşmez kopuyor, kart değişince gamepad yeniden eşleştirilmeli, sabit IP başka cihazca kullanılıyor, Armbian günlükleri güç kesilince kayboluyor, birleşik modelin ölçek filtresi robotd.toml'da değil, yerde sürtünmeyi önce hesaplayıp sonra ayarlayın; 2026-10-13, kissqy kurulum paketi `packaging/padd.service` kullanıyor, padd'ı çapraz derlemek için arm64 libudev gerekiyor, resmi ve kissqy arayüz sürüm numaraları ayrı ayrı artıyor, Feetech AMP2.0 kart tarafı soket modeli; 2026-10-12 gecesi, IMU'nun 8,5° eğik takılması modelin devralır devralmaz fırlamasının kök nedeni (sıfır noktası kalibrasyon yöntemiyle birlikte), web gamepad'inde dört katmanlı neden, SSH karşılama betiği, ToF yeniden bağlanma, Bluetooth gamepad eşleştirme, IMU kablosunda temassızlık, diz çökmesi, güç bankasının 5 V'a geri dönmesi, TPU ayak tabanı; 2026-10-12 öğleden sonra, kissqy tek tıkla imaj R1'in incelenmesi (V1.12 açılmıyor, yalnızca veri yolu IMU kartını tanıyor, önceden yüklenmiş prototip kalibrasyonu), Radxa önyüklemesinde armbianEnv değişikliği etkisiz kalıyor, HAT J5'e IMU modülü bağlarken adresler, Windows'ta Python'la dosya değiştirince CRLF oluşması; 2026-10-12, kissqy'nin tüm setine geçiş (resmi install.sh 0.15.1'e sabitli, ses kartı etkin değilse ses ayarında takılıyor, R17 prototip kalibrasyonunu kopyalıyor, mediad/tofd ana kartı ısıtıyor, delik ve hava kanalı, R17 kurulumu servo gücünü keser, IMU yönü önce ayakta durarak ölçülmeli, başka bir program güç verdikten sonra HOME reddediliyor, `service.sh init` HOME gönderemiyor, aşırı ısınma web joystick'ini devre dışı bırakıyor); 2026-10-11, kissqy yürüme modelinin gerçek robotta denenmesi (elle tutarak yürüyüş görülmez, düşük gerilim koruması ve tüm gövdede güç kesme, besleme payı, yumuşak başlatma, ana kart aşırı ısınıp frekans düşürüyor, Clash TUN ana kartı engelliyor, açılıştan sonra kilitlenme); 2026-09-28, HAT beslemesi, USB portu, kamera şerit kablosu ve resmi imaj karşılaştırması.

---

## Satın alma

**Pil NP-F970 değil, NP-F550 alınmalı**
Upstream'deki mesh dosyasının adı `np_f970.stl`, ama ölçüldüğünde 39 × 21 × 71 mm çıkıyor; bu F550'nin boyutudur. Gerçek F970 yaklaşık 60 mm kalınlığında olduğundan **sığmaz**, ayrıca 300 g ile tüm robotun ağırlık bütçesinin üçte birini yer.
→ NP-F550 alın (2S, 6,6–8,4 V). Ayrıntılar için [malzeme listesine (BOM)](02-malzeme-listesi-bom.md) bakın.

**Feetech HD-1910'un kablosu 2,0 mm, Feetech programlama kartının soketi ise değil — ID atamak için kablo bağlamak gerekir**
HD-1910'un orijinal kablosu AMP2.0-3P (2,0 mm aralık). FE-URT-2 programlama kartının TTL soketi bundan büyük olduğundan **takılmaz**, kartta da 2,0 mm'lik bir soket yok.
→ ID'yi aynı gün atamanız gerekiyorsa **bir servo kablosunu kesin** (15 kablodan biri feda edilir), üç çıplak teli şöyle bağlayın:

```
Servo kablosu            FE-URT-2
Pin 1  Signal    →   S    Kartın arkasındaki beyaz soketin S pininin lehim noktasına lehimleyin (geçici olarak kalaylayıp doğrudan S deliğine de sokabilirsiniz)
Pin 2  Vcc       →   V1   Mavi klemens
Pin 3  GND       →   G    Mavi klemens
```

**Ortadaki tel mutlaka V'dir** (Feetech ve Dynamixel bu konuda aynıdır). S ile G'nin ters bağlanması yakmaz, yalnızca iletişim kurulamaz; yerlerini değiştirmek yeter.
**Yanan şey V'nin yanlış bağlanmasıdır.** ID atama yüksüz yapılır, USB 5 V yeterlidir (HD-1910 4 V'tan itibaren çalışır) — önce multimetreyle mavi klemensteki G–V1 arasında 5 V olup olmadığını ölçün, yoksa o anahtarı çevirin.
→ Resmi çözüm: "PH2.0 3P klemens kablosu" ile karttaki türden klemens kablosundan birkaçını alıp birbirine lehimleyerek adaptör kablosu yapmaktır. Satın almadan önce servo kutusuna bakın, bazen bir tane ekliyorlar.
→ Bunu doğrudan Feetech'e iletmeye değer: resmi sürümde adaptör kablosu verilecek mi?

**Feetech'in pin sırası Dynamixel'in tam tersidir**
Feetech HD-1910: `1=Signal 2=Vcc 3=GND`. Dynamixel XL330: `1=GND 2=Vcc 3=Signal`.
→ Neyse ki iki tür farklı aralıkta (2,0 vs 2,5 mm) olduğundan birbirine takılmaz. Geriye yalnızca "kendi sıkıştırdığınız kabloyu ters sıkıştırma" olasılığı kalıyor — sıkıştırdıktan sonra önce multimetreyle bir kez çalıştırarak her pini yoklayın.

**HL-2915'i referans almayın**
Feetech HL-2915-C002 9–14 V'luk bir servodur; 2S pil (en fazla 8,4 V) onu **süremez**, üstelik pin sırası da HD-1910'un tersidir.
→ Bu tasarım yalnızca HD-1910-C001'i kabul eder.

**Dolu pilin 8,4 V'u, HD-1910'un gerilim üst sınırına eşittir**
HD-1910 çalışma aralığı 4–8,4 V. NP-F550 dolu iken 8,4 V'tur, yani **hiç pay yok**. Yük altında gerilim 6,6–8,2 V'a düşünce güvenli bölgeye gelir.
→ Yeni şarj edilmiş pille doğrudan sıkışma (stall) testi yapmayın. Uzun süre saklarken hücre başına 3,8 V'ta saklayın. Montajdan önce servolardaki aşırı gerilim korumasını açın.

**Radxa Zero 3W'nin düşük konfigürasyonlu sürümü çıplak karttır**
2 GB, eMMC'siz sürümde **pin başlığı lehimli değildir, depolama yoktur**; yalnızca microSD'den açılır.
→ 2×20 pin başlığı (2,54 mm, dik; renkli olanı alın, pinleri saymak kolay olur) ve **yüksek dayanıklılıkta** microSD kartı (SanDisk High Endurance / Hikvision PLUS, 32 veya 64 GB; iki tane alın, biri yedek olsun) kendiniz almalısınız.

**URT-2'nin V1 klemensine harici güç vermeyin**
Kart üzerindeki DIP anahtar TTL seviye seçimidir (3,3 / 5 V), güç anahtarı **değildir**. USB takılınca V1'de 5 V vardır; USB ile nasıl bağlandığı net değil, doğrudan geçiş olabilir. V1'e 7,4 V vermek bilgisayara veya Radxa'ya geri besleme riski taşır.
→ Harici güç doğrudan servoların V ve G'sine verilir, URT-2'nin G'si de ortak toprak için eksi kutba bağlanır, V1 boş bırakılır. URT-2 yalnızca sinyali yönetir.

**Feetech servoların fabrika ID'si hep 1'dir**
15 servoyu birden bağlarsanız hepsi yanıt verir, kimin kim olduğu ayırt edilemez.
→ **ID atarken her seferinde yalnızca bir servo bağlayın.** Değiştirdikten sonra etiket yapıştırın (eklem adı + ID), çıkarın, sonraki servoya geçin. Adımlar ve ID tablosu için [hata ayıklama kayıtlarındaki Servo yapılandırması bölümüne](15-hata-ayiklama-kayitlari.md) bakın.

---

**ToF modülü: L8CX kartı yüz kabuğuna sığmıyor, L7CX'i ise firmware tanımıyor**
Belirti: önce VL53L8CX alındı; Çin'de yaygın olan o kart **33,4 × 10,2 mm** olup yüz kabuğuna (`face_part`) sığmıyor;
kısa olsun diye L7CX (26 mm) alındı, firmware açılışta hata verip çıkıyor. İkisi de boşa gitti.
Neden: L7CX, 90° geniş görüş alanlı **başka bir çiptir**, revision ID uyuşmuyor. Resmi `tof` firmware'i yalnızca `0x02` (L5CX)
ve `0x0C` (L8CX) değerlerini tanır; diğerlerinde doğrudan `neither a VL53L5CX nor a VL53L8CX` hatasıyla çıkar —
firmware'e yalnızca bu iki ULD sürücüsü derlenmiştir, bir ID'yi değiştirerek aşılacak bir durum değildir.
→ **VL53L5CX (VL53L5X V2 modülü)** alın: firmware tanır, **delik aralığı 20 mm baskı parçasıyla tam uyuşur** (meslektaşın ölçtüğü baskı parçası delik aralığı 20 mm,
L8CX kartında 28 mm olduğundan hiç takılamaz), kart da en küçüğüdür (**15,8 × 10 mm** kart gövdesi / 24,7 mm montaj kulaklarıyla),
üstelik 25 yuan daha ucuz. **Seçim sırası: önce çipi firmware'in tanıyıp tanımadığına bakın (yalnızca L5CX / L8CX), sonra kartın sığıp sığmadığına** —
tersini yapıp önce boyuta bakmak bu seferki sonucu doğurdu. L8CX çipinin kendisinde sorun yok, sorun o kartın fazla uzun olması;
kısa kartlı bir L8CX bulunursa o da kullanılabilir, delik aralığı ve mercek konumu gerçek parçadan ölçülmeli.
Üç kart tipinin boyut karşılaştırması için [elektronik satın alma listesine](06-elektronik-satin-alma.md) bakın (bölüm 4: ToF mesafe ölçümü — VL53L5CX veya VL53L8CX, 8×8 çok bölgeli).

## Çizim / PCB üretimi

**JLCPCB sipariş sayfasındaki "Değiştir" projeye geri yazılmaz**
Sipariş sayfasında "Değiştir"e basarak parça numarasını değiştirmek yalnızca o siparişi etkiler. EasyEDA projesindeki komponent eski numarada kalır, **bir sonraki BOM dışa aktarmada yine eskisine döner** ve tekrar "özel kütüphane 0" uyarısı çıkar.
→ Komponenti EasyEDA projesinde değiştirin (silip aynı koordinata yeniden yerleştirin), yalnızca sipariş sayfasında değiştirmeyin.

**Aktif osilatör ile pasif kristal 3225 dört pinli kılıfta tıpatıp aynı görünür**
Pasif kristalin 2. ve 4. pini aynı metal kapaktır, içeride kısa devredir. Bu kartta X1 aktif olarak çizilmiş (2=GND, 4=VDD); pasif olanı lehimlerseniz **güç verir vermez 3,3 V toprağa kısa devre olur**. JLCPCB'de "3225" aratınca çıkanların çoğu pasiftir, temel kütüphanede (parça değiştirme ücretsiz) bulunan `C13738` yanlışlıkla en kolay seçilenidir.
→ Yalnızca etiketinde "aktif osilatör / OSC" yazanı kabul edin. Bu kart `C5917307` kullanır.

**Xingtong Shipin (星通时频) C387369 JLCPCB SMT yedek stoğunda yok**
Sipariş sırasında "özel stok kullanan komponentler" kategorisine alındı, özel stok 0.
→ `C5917307` ile değiştirin (Yajingxin (雅晶鑫), 5 mA, aynı kılıf).

**Komponent ekledikten sonra Gerber / BOM / koordinat dosyalarının tümü yeniden dışa aktarılmalı**
Şemayı değiştirdikten sonra (örneğin J4/J5 eklenince) üç dosya da değişir. Eski Gerber'le üretim yaptırırsanız kartta o iki soketin delikleri olmaz.
→ Her değişiklikten sonra tüm seti dışa aktarın, dosya adına zaman damgası ekleyin ve en yenisini kullanın.

**J4/J5 için seçilen PH2.0 soketlerinde aralık doğru, ancak gövde Feetech kablosunun fişine uymuyor, takılamıyor**
Feetech HD-1910 kablosu AMP2.0-3P fişidir, 2,0 mm aralık doğru, ama fişin dış şekli JST PH soketin gövdesine (`B3B-PH-K-S`) uymuyor. Değerlendirme sırasında "kart tarafındaki soket gerçek parçayla doğrulanmadı" uyarısı yapılmıştı, nitekim öyle çıktı.
→ İlk kart: soketin gövdesini kesip yalnızca pinleri bırakın, takılır ve çalışır. v2: soketi Feetech kablosunun gerçek haliyle eşleştirin (Feetech'ten kart tarafı soket modelini isteyin ya da birkaç farklı 2,0 mm 3P soket alıp deneyin), **kartı üretime vermeden önce gerçek parçayı bir kez takın**.
→ Ek (2026-10-13): Feetech'in şartnamesi yalnızca kablo ucunu `AMP2.0-3P` olarak belirtiyor, kart tarafı modeli yayımlanmamış, internette de doğrulanmış bir yatık (yan takılan) parça numarası bulunamadı; diğer replika projeleri doğrudan "PH2.0" yazıyor, onlar da gerçek parçayla denememiş. Ancak Feetech'in boyut çiziminde **servonun gövde tabanında aynı tür iki soket zaten var**, yani eşleşen kart tarafı soketi Feetech'in kendisi kullanıyor — en hızlısı doğrudan Feetech'e model numarasını, tek tek satın alınıp alınamayacağını ve yatık (yan) versiyonu olup olmadığını sormak.

**GitHub Release eklerinin adındaki Çince karakterler temizleniyor**
`SolidWorks图纸.zip` yüklendi, `SolidWorks.zip` olarak kaydedildi. README'deki indirme bağlantısı uyuşmuyor.
→ Release eklerinde doğrudan İngilizce ad kullanın.

---

## Jumper kablo (HAT basılmadığında)

> Tam bağlantı şeması [HAT olmadan kurulum](08-hat-olmadan-kurulum.md) belgesinde, burada yalnızca ısıran noktalar listelenmiştir.

**Dönüştürücü kartın mantık beslemesi yalnızca 3,3 V'tan alınabilir**
Yarım dubleks dönüştürücü kartın MCU tarafında bir VCC vardır. 5 V'tan alınırsa TX'i ana kontrolcünün 3,3 V'luk RX pinine 5 V seviyesinde vurur.
→ 40 pinli konnektörün pin 1'inden (3,3 V) alın. ToF pin 17'den alınır, ikisi birbirini engellemez.

**40 pine verilen 5 V korumasızdır**
Pin 2/4'ten 5 V beslemek kartın kendi USB giriş korumasını atlar. **Ters bağlarsanız kart anında yanar.**
→ Takmadan önce düşürücü modülün çıkış kutbunu ve gerilimini ölçün.

**Servo ana hattında Dupont kablo kullanmayın**
15 servo tepe değerde birkaç amper çeker; 24–28 AWG Dupont kablo yalnızca yaklaşık 1 A taşır, ısınır, hatta yalıtımı erir.
→ Ana hat için 18–20 AWG silikon kablo kullanın.

**Pilden servolara giden hatta sigorta ve anahtar seri bağlanmalı**
Lityum pilin kısa devresi ateş püskürtür. Resmi HAT'ın o hattında termal koruma + "3A max" işareti vardır, uçuş kablolu çözümde doğrudan bağlanınca hiçbir koruma yoktur.
→ 5 A sigorta + güç anahtarı seri bağlayın.

**Kapanma algılama sinyali yok**
HAT üzerindeki LM5050-1 ana kontrolcüye bir kapanma sinyali verir, uçuş kablolu çözümde bu yoktur. Her güç kesmede sert çekme olur, **microSD'ye en çok zarar veren budur**.
→ Önce `make shutdown` veya gamepad kapatma hareketini kullanın, sistem tamamen kapanana kadar bekleyip sonra gücü kesin.


---

## Servo / Kalibrasyon

**Feetech FD hata ayıklama yazılımı: önce sürücüyü kurun, en yeni sürümü kullanın, baud hızını 1 Mbps seçin**
Üçlü belirti: URT-2'yi takınca tek bir servo bile taranamıyor; sürücüyü kurunca bağlanılıyor ama servo modeli `unknown` olarak okunuyor; veya bağlanıyor ama tarama sonuç vermiyor.
Neden: ① URT-2'nin USB-seri çipi sürücü gerektirir, aygıt yöneticisinde COM portu yoksa sürücü kurulmamıştır; ② FD sürümü eskidir, model tablosunda HD-1910 gibi özel modeller yoktur, tanıyamayınca unknown gösterir, **ancak register okuma/yazma tamamen normal çalışır**; ③ HD-1910'un fabrika baud hızı 1 Mbps'tir (register 6 = 0), FD'de baud hızı 1000000 seçilmezse taranamaz.
→ Sıra: sürücüyü kur → aygıt yöneticisinde COM portunu doğrula → FD'de baud hızını 1000000 seç → [Feetech resmi sitesinden](http://doc.feetech.cn/) en yeni FD'yi kullan. Model unknown görünüyorsa umursamayın, servonun bozuk olduğunu sanmayın.

**HD-1910'un konum sayma yönü resmi XL330'un tersidir, 15 servonun hepsi ters**
Belirti: kaydırıcıyı sürüklerken 3D model gerçekten ters yönde hareket ediyor; resmi duruş açılarını gönderince bacaklar ters yöne bükülüyor.
Neden: HD-1910'da değer artış yönü XL330'un tersidir, mekanik montaj ise resmi tasarımdan aynen alındığından her eklem bir kez tersine dönmüştür — bu bütünüyle ters olmaktır, birkaç servonun yanlış takılmış olması değildir.
→ 15 servonun yönünün tamamını −1 yapın: [`tools/servo-web/directions.json`](../tools/servo-web/directions.json), robotd'de ise `[bus.feetech] directions`. Web sayfasındaki her servonun yanındaki ± düğmeleri tek tek doğrulanmıştır.

**HD-1910 "tork anahtarına 128 yaz" türü orta nokta kalibrasyonunu tanımıyor**
Belirti: bellek tablosunda açıkça "128 yaz: mevcut herhangi bir konumu 2048 olarak düzelt" yazıyor, buna uyunca servo "başarılı" yanıtı veriyor ama ofset register'ı (31) hiç değişmiyor. Kod devamında hedef konumu 2048 yazarsa eklem eski sıfıra geri çekiliyor. 2026-09-20'de 15 servonun 4 turluk ölçümünde, kilit açık ve tork kapalıyken de aynısı görüldü.
Neden: firmware 3.46 bunu desteklemiyor. Protokol kılavuzu 4.9'daki destek tablosunda şöyle yazıyor: SMS ≤2.54 ve STS ≥3.10 128 yazmayı destekler, **HLS ≥3.43 desteklemez**, yalnızca 0x0B'yi destekler — HD-1910'un davranışı HLS satırıyla aynıdır.
→ **0x0B konum kalibrasyon komutunu** kullanın (parametresiz = 2048'e kalibre eder, parametreli = belirtilen okumaya kalibre eder). Kalibrasyondan sonra mutlaka konumu ve ofseti geri okuyup doğrulayın, yanıttaki "başarılı"ya güvenmeyin: Feetech'in desteklemediği birçok işleme de yine başarılı yanıtı verir.

**Kalibrasyon sırasında torku kapalı bekletmeyin**
Belirti: tork kapatıldıktan sonra onlarca milisaniye bekleyip konumu okuyunca boyun (30) okuması 80 adım (7°) düştü, kalibre edilen sıfır eğri çıktı.
Neden: tork kapanır kapanmaz eklem yerçekimiyle aşağı bastırılır, ne kadar beklenirse o kadar düşer.
→ Torkun kapatılmasından kalibrasyonun tamamlanmasına kadar araya sleep koymayın, birkaç milisaniye yeter; kalibrasyondan hemen sonra hedef konumu yeni okumaya yazıp torku açın.


**Servonun D'si (türev, sönümleme) yürürken titremeyle ilişkili**
Belirti: 2026-10-13'te R17 varsayılanı P5/D20 ile yürürken gövde sallanmasının yarısı 4 Hz üzeri titreme (%51), adım ritmi bozuk. Yeni kart V164 fabrika D=40'ı kullanıyor.
Neden: eğitimde kullanılan BAM servo modelinin (parametreleri Luwu'nun (陆吾) yayımladığı 1910 M6'dır, `kp_fw=5` yani firmware P=5) donanım D terimi yoktur, oysa gerçek robotta D vardır. D 0 yapılınca (aynı anda tork 1000→850) titreme %4～8'e düştü. D'nin neden titreme yaptığı konusunda "sönümlemenin düzeltme hareketini yemesi" yalnızca bir varsayım, izleme verisi bunu doğrulamadı.
→ Önce D'yi 0 yaparak titremeyi giderin. Ancak D=0 olunca yere basan diz daha zor düzleşiyor, ayrıca gövde ileri geri başını sallıyor ve sol ayak ucu aşağı bakıyor (D=20'de yoktu); D=5～10 ara değerleri denemeye değer. D=0 iken P büyüdükçe daha çok sallanıyor: P5 56°/s, P4 44°/s, P3 30°/s (simülasyonda 31°/s). Şu an P3 / D0 / tork 700 kullanıyoruz, bedeli ayağı daha az kaldırmak. Veriler için bkz. [10-13 gecesi gerçek robot kaydı §5](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-夜-掉电-舵机D与蹭地.md).

**kissqy V164 (tek tıkla imaj) D ve tork sınırını yazmıyor, kontrol merkezindeki P/D/tork kutularını değiştirmek işe yaramıyor**
Belirti: yeni kartta kontrol merkezinin "gelişmiş parametreler" bölümünde P, D, tork sınırı değiştiriliyor, güç verildikten sonra servo register'ları değişmiyor.
Neden: V164 yalnızca model paketinde kararlaştırılan P'yi yazar (5, kissqy buna "dağıtım sözleşmesi" diyor); 51 numaralı D ve 48 numaralı tork sınırı servonun fabrika değerinde (D=40, 1000) bırakılır, bu kasıtlı bir tasarımdır (tasarım belgesinde "cihazın mevcut değerini koru" yazıyor); R17'deki "test parametreleri" yolu silinmiştir. HD-1910 fabrika EEPROM'u P32 / D40 / I0'dır.
→ Ayarlamak için R17'yi kullanın; veya robotd durdurulup 15 servonun gücü alındıktan sonra servo RAM'ine yazın (güç kesilince eski haline döner, gamepad D-pad sağ "servoları yeniden başlat" da eski haline getirir); veya EEPROM'daki D'yi 0 yapın (bir kez yapılır; yalnızca D yazmayan V164 için geçerli, R17 güç verirken kendi D'sini yazdığından test parametrelerindeki kd ile birlikte ayarlanmalı). Güç verilmeden önce servodaki özgün değer `robot.busStatus` → `native.hd1910.registers_before_arm` altında görülür.
**Ek (10-14)**: V164 ile gelen kontrol merkezi 1.0.164'te bu üç kutu (P / D / tork) zaten yok (bu üç kutu R17'nin eski kontrol merkezi 1.0.146'da vardı; eski merkez V164 kartına bağlansa da değiştirilen değerler işe yaramıyor). Biz yerelde V164'ün bu kalemlerini açtık (gerçek robotta denenmedi, yayımlanmadı), bkz. [10-14 gün içi kayıt §8](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md).
**Ek (10-14 akşamı)**: kissqy 10-14'te V167 / control.43'ü (kontrol merkezi 1.0.167) yayımladı, açıklaması "ördek gövde titremesini düzeltir": her HOME güç verilişinde 15 servonun RAM'indeki D'yi 0, tork sınırını 1000 yazıyor, P yine modeldeki 5; bu iki değer sabit, kontrol merkezinden ayarlanamıyor; güç alınırken yalnızca P geri yükleniyor, D servo gücü kesilene kadar 0'da kalıyor. Bu, bizim 10-13 gecesi sonucumuzla uyuşuyor (aynı masa, D20'de titreme %51, D0 ile %4～8). Dikkat: IMU modülü (BNO085 vb.) kullanan ördekler, onun kontrol merkezindeki "Kur / Firmware yükselt" düğmesine doğrudan basmasın: kurulum paketi kendi robotd'sini getiriyor, IMU modülünü tanımıyor, yükseltmeden sonra IMU okunamıyor ve güç verilemiyor (bkz. "Yazılım" bölümündeki "Kendi değiştirdiğiniz robotd'yi kurduysanız kissqy kontrol merkezinde 'Kur / Firmware yükselt'e tıklamayın" maddesi).

**Servonun P / D / tork sınırı RAM'e yazılır: her güç verişte yazılır, güç alınırken geri yüklenir, enerji kesilince fabrika değerine döner**
Belirti: 2026-10-14'te kullanıcı sordu: kontrol merkezinde ayarlanan P / D / tork hep geçerli mi, yoksa her seferinde yeniden mi yazılmalı? Servoya bir kez güç kesilince veya gamepad D-pad sağ (servoları yeniden başlat) basılınca register okununca yine fabrika değerleri D40 / 1000 görülüyor.
Neden: R17 ve bizim V164 üzerinde yaptığımız ayarlanabilir sürüm, her HOME güç verilişinde tork sınırı, P, D'yi servonun **RAM**'ine (48～51 numaralı register'lar) yazar, yazmadan önce özgün değeri not eder, güç alınırken geri yazar; V164 orijinali yalnızca RAM'e P'yi (50 numara) yazar. EEPROM'a hiçbiri dokunmaz. Servonun gücü kesilince RAM, EEPROM'dan yeniden yüklenir (HD-1910 fabrika P32 / D40 / I0, tork sınırı 1000). Ayarlanan değerler kart üzerindeki bir dosyada (`/etc/robot/feetech-ft5/servo-test-parameters.json`) saklanır, bir sonraki güç verişte otomatik yeniden yazılır, yani bir kez ayarlamak yeter, her seferinde yeniden ayarlamak gerekmez.
→ Geçerli olup olmadığını `robot.busStatus` → `native.hd1910.servo_parameters` (robotd'nin yüklediği değerler) ve `temporary_gains_applied: true` (yazıldı ve geri okuyarak doğrulandı) ile kontrol edin; `registers_before_arm` güç verilmeden önce okunan özgün değerlerdir, ayarladığınız değerler değildir. Bir tuzak var: **güç verilmişken robotd yeniden başlatılırsa** (çökme, elle restart, güç verilmişken program kurma), not edilen özgün değer kaybolur. V164 ve ayarlanabilir sürümde robotd başlar başlamaz tüm servoların gücünü keser (ördek o an yığılır, tutun), bir sonraki HOME'da servoda kalan test değerlerini özgün değer sanıp not eder; R17 başlarken güç kesmez, yalnızca değerlerin dosyayla uyuşup uyuşmadığını kontrol eder (uyuşmuyorsa HOME'u reddeder, aşağıdaki "başka bir programla güç verip sonra kissqy'ye geçmek" maddesine bakın). Her iki durumda da test değerleri RAM'de kalıcı olarak kalır. Bu parametre setini kullanmaya devam etmek sorun değil; ancak yalnızca P yazan orijinal davranışa döndükten sonra (parametre dosyasını silmek veya kontrol merkezinde "varsayılana dön"), D ve tork test değerlerinde takılı kalır. Bu durumda servoların gücünü bir kez kesin. Ayrıntılar için [10-14 gün içi kayıt §8.3, §8.4](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md).

**HOME'da iki ayağın sol-sağ yönü aynı düzlemde değil: iki kalça roll'u dışa açılıyor, her seferinde farklı (vücut ağırlığının bastırdığı tahmin ediliyor)**
Belirti: servo okumalarından ileri kinematik hesaplandığında, HOME'da (veya yürüyüş bitince durulduğunda) iki ayak tabanı sol-sağ yönde aynı düzlemde değil. 2026-10-14'te 14 segmentin tamamı hesaplandı, HOME'a göre fark 0,6°～13°, her segmentte farklı. İlk başta kalça roll sıfırının kaydığından şüphelenildi.
Neden: eklem eklem ayrıştırıldığında ([`tools/gait-analysis/home_roll.py`](../tools/gait-analysis/home_roll.py)), farkın tamamı sol ve sağ kalça roll'unun HOME hedefine ulaşamamasından kaynaklanıyor; yön her seferinde sol +, sağ − (bacak dışa açılıyor), büyüklük her seferinde farklı (0,2°～6,9°). Simülasyon geometrisine göre, yerin ayağı desteklediği kuvvet kalça roll ekseninin yaklaşık 23 mm dışına düşüyor ve bacağı dışa doğru iter, vücut ağırlığının bastırması gibi (tahmin; ne kadar sapacağının P ile ilişkisi veriden görülemiyor). Simülasyondaki politika da dururken aynı yönde sapma yapıyor (sol +1,6°, sağ −1,8°), gerçek robotta çoğunlukla aynı büyüklük mertebesinde.
→ Her seferinde değişen kısım sıfır konumu değildir, bunun için sıfırı değiştirmeyin. Ancak şunu bilin: bu yöntem "okuma − hedef"i karşılaştırır, ikisi aynı sıfır noktasındandır, **sıfır konumunun kendisinin kayık olup olmadığını göstermez**. Simülasyon modelinde HOME'da iki ayak zaten dış kenarlarından yaklaşık 2,3 mm alçaktır, biraz dışa açılma düzleştirir, fazla açılma iç kenarın alçak kalmasına yol açar; gerçek ördekte hangi tarafın kalktığına HOME'da tam önden masa yüzeyine yakın bakıp ışığın geçişine göre karar verin, gerçek parça esastır. 10-14 sabahı sözlü olarak "dış kenar kalkıyor" dedik, 14 segmentin 12'sinde tam tersi çıktı, bu maddedeki doğru kabul edilsin. Ayrıntılar için [10-14 gün içi kayıt §7](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md).

**Ağız servosu çok ısınıyor: sürekli kapalı konuma doğru bastırıyor, ayrıca ana karta yakın (kissqy'nin açıklaması)**
Belirti: ağız servosu elle tutulunca yakıyor. 2026-10-12 gecesi ölçümümüze göre ördek ayaktayken ağız servosu 60～70°C.
Neden: kissqy grupta şöyle açıkladı: ağzın konumu −5°'ye (kapalı konum) ayarlı, kapandıktan sonra hâlâ güç uygulamaya devam ediyor, sürekli tork veriyor; ağız ana karta en yakın yerde olduğundan ana kartın ısısıyla da ısınıyor. "Sürekli kapalı kalsa da 40 küsur derece olur" dedi, servo bozuk değil. Onun söylediği sıcaklık bizim ölçtüğümüzden düşük, nedeni araştırılmadı.
→ Servoyu hemen değiştirmeyin. Ana kart soğutması için aşağıdaki "Ana kartın gövde içinde hava kanalı yok" maddesine bakın. Ağzın kapalı konumunun biraz geriye alınıp sonuna kadar bastırılmaması gerekip gerekmediğini henüz denemedik.

**kissqy'nin R17'sini kurmak, onun prototipinin sıfır noktalarını sizin kalibrasyonunuz sanır**
Belirti: 2026-10-12'de R17 ilk kez kurulduğunda bu makinede kalibrasyon dosyası yoktu, kurulumdan sonra `hd1910-calibration.toml` içinde 15 eklemin hepsi "kalibre edildi" idi ve durum "hareket hazır" gösteriyordu. Oysa sıfırlar 1372'den 2176'ya kadar değişiyor, yönler hem pozitif hem negatif (baş ID 33'ün sıfırı 1599), bizim makineyle uyuşmuyor: biz servo-web ile kalibre ettik, sıfırlar hep 2048, yönler hep −1.
Neden: onun kurulum betiği, bu makinede kalibrasyon yoksa paketteki prototipin kalibrasyonuyla tamamlıyor ve kalibre edildi olarak işaretliyor. Açıklamasında "paket içindeki kalibrasyon prototip referansıdır, her makinede kontrol edilmelidir" de yazıyor, ancak kurulum sırasında bir uyarı yapmıyor.
→ Kurulumdan sonra önce `/etc/robot/feetech-ft5/hd1910-calibration.toml` dosyasını açıp kendi sıfırlarınız ve yönlerinizle değiştirin, ardından `açı = (okuma − sıfır) × yön × 2π/4096` (servo-web ile aynı formül) ile her eklemin açısını hesaplayıp gerçek duruşla eşleştiğini doğrulamadan güç vermeyin. Eşleşene kadar HOME'a basmayın.

**kissqy'nin tek tıkla imajı R1 de prototipinin kalibrasyonunu önceden yüklüyor, üstelik IMU "onaylandı" olarak işaretli**
Belirti: 2026-10-12'de imaj incelendi, `hd1910-calibration.toml` içindeki sıfırlar onun ördeğinin değerleri (2281, 2176……), yönlerin hepsi −1, `imu_mount_verified = true`; yalnızca `motion_enabled = false` engelliyor.
Neden: imaj onun prototipinden çıkarılmıştır. IMU "onaylandı" ifadesi onun veri yolu kartındaki montaj yönü içindir, başka bir ördek veya başka tür IMU için geçerli değildir.
→ Yazdıktan sonra önce bir önceki maddeye göre kendi sıfırlarınızı ve yönlerinizi koyun, IMU montaj yönünü yeniden onaylayın, ancak sonra HOME'a ve hareket anahtarına dokunun. Ayrıntılar için [kissqy imaj R1 analizi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy镜像R1分析.md).

---

## Ana kart / HAT / Kamera

**Kamera şerit kablosunda iki ucun da temas yüzeylerini kontrol edin, takılmış olması doğru takılmış demek değildir**
Belirti: Radxa Camera 8M219 (IMX219), Armbian'da da resmi B1'de de çip okunamıyor, `Reading register 100 from 10 failed`, `Error -5` hatası veriyor; 2026-09-28'de kullanıcı şerit kablonun ön-arka yüzünün ters olabileceğini fark etti, düzeltince `Model ID 0x0219` okundu ve 1920×1080'lik 40 kare başarıyla alındı.
Neden: kablo yönü/teması ayarlandıktan sonra arıza kayboldu; fişin takılmış olması veya kablonun rengi bakılarak temasın sağlandığı anlaşılamaz.
→ **Normal şekilde kapatın, tüm gücü kesin, sonra iki ucun açıkta kalan metal temas noktalarının sokettekilerle hizalandığını kontrol edin, düz takıp kilitleyin.** ZERO 3W ile Radxa 8M219 için **22 pin / 0,5 mm → 15 pin / 1,0 mm, aynı yüzlü temas** şerit kablosu kullanılır; "aynı yüz" ifadesi, düz serildiğinde iki ucun açıkta kalan temas bölgelerinin aynı tarafta olması demektir, filmin altından görünen bakır hat değildir.

<p align="center"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/radxa-camera-cable-reference-20260928.png" alt="Kullanıcının sağladığı kamera şerit kablosu bağlantı referansı: solda mercek yüzü, sağda ana kartın arka yüzü, şerit kablo U şeklinde" width="380"></p>

*Kullanıcının sağladığı bağlantı referans görseli: solda mercek görünüyor, sağda ana kartın arka yüzündeki Radxa / UKCA işaretleri görünüyor. Genel göreli yönü kontrol ettikten sonra her soketin içindeki temaslara da bakın; farklı modüllerde yalnızca mercek yönüne veya kablonun yazı yüzüne göre takmayın. Bu görsel bağlantı hatırlatması içindir, bu seferki alınan görüntü değildir.*

**`/dev/video0`'ı görmek kameranın tanındığı anlamına gelmez**
Belirti: kamera yanıt vermese de kartta `/dev/media0` ve `/dev/video0..9` hâlâ mevcut.
Neden: bunlar yalnızca Rockchip ISP alıcı uç düğümleri olabilir, sensör bağlanmamıştır.
→ Sırayla çip ID'sini, `imx219` sürücü bağlanmasını, `media-ctl -p` çıktısında sensör varlığını doğrulayın, son olarak gerçekten kare yakalayın; [bu seferki tam komutlar ve sonuçlar](../tools/radxa/摄像头调试记录-20260928.md).

**İki Type-C portunu "biri güç, biri bilgisayar" diye tahmin etmeyin**
Belirti: bilgisayar USB 3.0 Host portuna bağlanıp ana kartın USB seri portunun görünmesi bekleniyor.
Neden: `5V IN / USB_OTG` hem güç hem USB 2.0 gadget portudur, USB 3.0 Host ise URT-2, USB bellek gibi çevre birimlerinin bağlandığı porttur; COM'un görünüp görünmeyeceği ayrıca sistemde gadget seri portunun yapılandırılıp yapılandırılmadığına bağlıdır.
→ **HAT beslenmişken Wi-Fi + SSH ile hata ayıklayın**; V1.12'nin 40 pinli 5V'u ile OTG VBUS aynı ağdadır, sıradan USB veri kablosuyla bilgisayardan ikinci bir 5V sokulmamalıdır. USB beslemesine geçmek gerekirse önce kapatın ve HAT girişini çıkarın. 7,4V yalnızca HAT'ın ilgili girişine verilebilir, doğrudan ana kartın 5V'una veya USB-C'ye verilemez; bkz. [imaj kullanım kılavuzu](11-radxa-imaj-kullanimi.md) (bölüm 3: İlk açılış).

**Yeşil ışığın çift yanıp sönmesi normal kalp atışı olabilir, ayrı bir arıza kodu değildir**
Belirti: bu seferki resmi B1'de yeşil ışık çift yanıp sönüyor, ancak Wi-Fi, SSH ve kamera normal.
Neden: LED yapılandırması `heartbeat`'tir; daha önce açılış başarısız olduğunda da çift yanıp sönme görülmüştü, o zamanki eşlik eden belirti genel bir tanı olarak alınamaz.
→ Sistemin açılıp açılmadığına ağ, SSH, açılış günlüğüne bakarak karar verin, yalnızca ışık efektine bakıp kartı yeniden yazmayın.

**Karşılaştırma için resmi imaja geçildiğinde bağlantı da değiştiyse, yalnızca imaja bağlamayın**
Belirti: resmi B1 de başta kamerayı okuyamadı, şerit kablo ayarlandıktan sonra görüntü geldi.
Neden: imaj ve bağlantı aynı koşullarda tam olarak yeniden test edilmedi; bu seferki yalnızca resmi yapılandırmada kamera tanıma ve kısa süreli alımın geçtiği doğrulanabildi.
→ Başarılı olan bağlantıyı koruyun, gerekirse özgün Armbian'ı yeniden test edin; hemen "özgün imaj bozuk" demeyin, 40 karelik kısa testi de 30 fps, uzun süreli kararlılık veya HAT'ın tüm işlevlerinin kabulü sayma.


**Ana kart aşırı ısınıp frekans düşürüyor: web servisi sürekli bir çekirdeği dolduruyor, kontrol ritmi yavaşlıyor**
Belirti: 2026-10-11'de politika çalıştırılırken kontrol periyodu 20 ms'den 25 ms'ye çıktı, sensör okuması en yavaş 20 ms; ana kart CPU'su 84–87°C, `scaling_max_freq` en düşük kademe olan 408 MHz'e bastırılmış (en yüksek 1800).
Neden: `servo-web/server.py` sürekli çalışırken top'ta bir çekirdeği dolduruyor (%100), ana kart gövdenin içinde olduğundan ısı atamıyor; RK3566 85°C'de frekans düşürür.
→ Politikayı çalıştırmadan önce web servisini durdurun (`systemctl stop microduck-servo-web`), ana kartı açın veya fan ekleyin; çalıştırmadan önce `/sys/class/thermal/thermal_zone0/temp` ve `/sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq` dosyalarına bakın. Web sayfasının neden CPU'yu doldurduğu henüz araştırılmadı.

**Ana kart açıldıktan bir iki dakika sonra kilitleniyor, yeşil ışık yanıp sönmeden sürekli yanıyor**
Belirti: 2026-10-11'de güç verildikten sonra SSH bağlanabiliyor, yaklaşık 2 dakika sonra ağdan kayboluyor, router'da da bulunamıyor, yeşil ışık yanıp sönmeden sürekli yanmaya geçiyor. Güç kesip yeniden başlatınca normale dönüyor, sonrasında bütün gece tekrar etmedi.
Neden: belirsiz. Yeşil ışığın sürekli yanması çekirdek kalp atışının durduğunu (kilitlenme) gösterir, Wi-Fi kopması değildir. O açılışın günlüğü karta yazılmadığından bakılamıyor. O sırada ayarlanabilir 7,4 V güç kaynağı kullanılıyordu.
→ Tekrar ortaya çıkarsa önce güç kaynağının ekranındaki gerilim ve akımı not edin, sonra güç kesip yeniden başlatın; tekrar tekrar güç vermeyin.

**Kamera ve ToF bağlı değilken resmi mediad ve tofd sürekli yeniden başlayıp ana kartı ısıtıyor**
Belirti: 2026-10-12'de resmi 0.15.1 kurulduktan sonra ana kart 89–90°C, CPU en düşük kademe olan 408 MHz'e kilitli. top'ta mediad'ın `gst-plugin-scanner` işlemi bir çekirdeği dolduruyor (%99,5), tofd da sürekli yeniden başlıyor.
Neden: kamera bağlı olmadığından kamera servisi başlar başlamaz çöküyor, systemd onu sürekli yeniden başlatıyor, her seferinde GStreamer eklentilerini baştan tarıyor; tofd mesafe sensörünü bulamayınca aynı şekilde davranıyor. Gruptaki kullanıcılar da kullanılmayan servisleri kapatınca sıcaklığın düştüğünü söylemişti.
→ Bu ikisi bağlı değilse `sudo systemctl disable --now mediad tofd` çalıştırın, sonra bağlayınca `enable --now` yapın. Kapattıktan 2 dakika sonra 85°C'ye indi, ancak frekans düşürme sınırında kalmaya devam ediyor, ek soğutma gerekli (bir sonraki maddeye bakın).

**Ana kartın gövde içinde hava kanalı yok, servisleri kapatsanız bile 92°C'ye çıkar**
Belirti: mediad ve tofd kapatıldıktan sonra yalnızca robotd çalışırken ve ördek ayaktayken sıcaklık yavaş yavaş 92,5°C'ye çıktı, CPU hep 408 MHz'de. Güç verme geri okuma zaman aşımı CPU'nun çok yavaş olmasından kaynaklanıyor; web joystick'inin tepkisiz kalması da bundan daha da kötüleşiyor (kök neden yalnızca aşırı ısınma değil, bkz. [Yazılım](14-tuzaklar.md) bölümü). 2026-10-12 gecesi tüm servisler kapalı ve SSH yeniden bağlanması da kaldırıldıktan sonra, model çalıştırılınca yaklaşık 10 dakikada CPU yine 85°C'ye ulaştı, 408～600 MHz'e düştü (robotd modeli çalıştırırken bir çekirdeğin %30～46'sını kullanıyor).
Neden: ana kartın gövde içinde soğutucu yok, hava giriş-çıkış yolu da yok. RK3566 85°C'de frekansı düşürür, en düşük kademeye inince tüm programlar yavaşlar.
→ Önce kafa kabuğunda veya gövdede birkaç delik açın, en basit çözümdür, ısının bir kısmını atar. Gerçekten ısıyı atmak için önemli olan **hava kanalıdır**: hava girişi ve çıkışı olması gerekir, fanın ana karta yapışık olması şart değil. Gerçek robotta denemeden önce `/sys/class/thermal/thermal_zone0/temp` ve `/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq` dosyalarına bakın, frekans 408000 ise frekans düşürüyor demektir.

**Yürürken veya ayağa kalkarken tüm sistem güç kaybedip yeniden başlıyor: sorun beslemede, yazılımda değil**
Belirti: 2026-10-13'te yeni kart da eski kart da yürürken veya ayağa kalkarken ani güç kaybıyla yeniden başladı, kayıt ve sistem günlükleri aynı anda kesildi, kapanma süreci yok. Yeni kart (D=40) model devralınca 13 saniyede düştü, son anda servo yaklaşık 3,9 V okudu; eski kart (D=20) devralınca 42 saniye dayandı, arada bir kez düşüp kalktı, kalktıktan yaklaşık 11 saniye sonra güç kesildi, güç kesildiğinde joystick 0'dı.
Neden: on küsur servonun birlikte güç uygulamasının akım şoku, güç kaynağı ve kablolar kaldıramıyor, ana kartın 5 V'u HAT'ın aynı hattan düşürdüğü gerilim olduğundan o da düşüyor. D büyüdükçe modelin düzeltmesi daha sık oluyor, şok daha çok olabilir (yeni kartta ses de açıktı, bire bir karşılaştırma ile sonuca varılamıyor). robotd'nin bildirdiği gerilim 0,5～1 saniyede bir nokta, onlarca milisaniyelik düşüşler görülemiyor.
→ Pil veya yüksek akımlı güç kaynağı (10 A) kullanın, kablo 16～18 AWG olsun, mümkün olduğunca kısa tutun, XT30/XT60 konnektörler kullanın, girişe 1000～2200 µF kondansatör paralel bağlayın. Ana güç kaynağından mı, yoksa HAT'ın ana karta verdiği hattan mı olduğunu ayırt etmek için: ana kartın USB-C'sine ayrıca güç bankasıyla ayrı besleme verip öyle yürütün. kissqy deposunda bir zamanlar "LM5050 payı yetersiz olduğundan yeniden başlıyor" yazıyordu, 10-12'de sildi (yazar düzeltti), atıf yapmayın. Ayrıntılar için [10-13 gecesi gerçek robot kaydı §2](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-夜-掉电-舵机D与蹭地.md).
**Ek (10-15 akşamı)**: yeni kart bir kez daha tüm sistem yeniden başladı (19:31:42), bu sefer ördek walk modunda yerinde duruyordu, joystick'e dokunulmamıştı, bir an önce pil 7,59 V, CPU 78°C, kayıt dosyasının sonu bir dizi boş bayt. Büyük bir harekette düşmediğinden "yalnızca güç şoku" açıklaması geçerli olmayabilir, neden henüz belli değil; 10 A güç kaynağı gelince karşılaştırma yapılacak. Bkz. [10-15 kaydı §6.2](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261015-IMU乱跳根因与陀螺融合上机.md).

**HAT'ın J5'ine harici IMU modülü bağlarken, önce kartta hangi çiplerin adresleri zaten kullandığına bakın**
Belirti: J5 (40 pin 3/5. pinler, I2C3) hattında kartın üzerindeki çipler zaten bağlı: iki sürümde de ses aic3104 (0x18); C1 sürümünde (elimizdeki kart) ayrıca BMI088, ivmeölçer 0x19, jiroskop 0x68; D1 sürümünde (resmi en yeni) LSM6DSV16X, 0x6A.
Neden: I²C aygıtları adresle ayırt eder, iki çip aynı adresi kullanırsa birbirine karışır, hiçbiri doğru okunamaz. Harici BNO085 (0x4A/0x4B) iki sürümde de çakışmaz; harici LSM6DSV16X, D1'de de 0x6A kullanırsa kart üzerindekiyle çakışır.
→ Bağlamadan önce `i2cdetect -y 3` ile kullanılan adreslere bakın; D1'de harici LSM6DSV16X için 0x6B kullanın (SA0 yüksek), robotd'de açıkça `i2c_address = 0x6B` yazın. Kart üzerindeki IMU kafanın içindedir, yalnızca kafa IMU'su olarak kullanılabilir, harici modül gövdeye takılmalıdır. J5'i meşgul etmek istemezseniz J6'yı I2C4 yapabilirsiniz (R18/R19'u sökün, R16/R17'yi kısa devre edin). C1/D1 pad pad karşılaştırması için [kissqy imaj R1 analizi §9](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy镜像R1分析.md)'na bakın.

**IMU modülünde temassızlık: robotd IMU'yu bayat sayıyor, ördek doğrudan gücünü kesiyor**
Belirti: 2026-10-12 gecesi ördek aniden yumuşadı (çöktü), Start'a basınca `nothing to bring up state=Limp` döndü, `robotctl health` `orientation frozen` gösterdi, robotd günlüğünde `trunk IMU reader fault … No such device or address (os error 6)`.
Neden: BNO085 I²C üzerinde yanıt vermiyor (adrese kimse cevap vermiyor). 77 kopma anında da servo gerilimi 7,3～7,5 V idi, yani besleme değil; çoğu yürürken sallanırken, birkaçı da tamamen hareketsizken oldu, bu bir noktanın zaten gevşemiş olduğunu gösterir. robotd IMU'nun güncellenmemesini okuma hatası sayıyor, art arda hata olunca korumak için gücü kesiyor, bu doğru bir davranış; IMU düzelince sürücü kendiliğinden yeniden tanıyor.
→ Kabloyu sağlam lehimleyin veya kilitli konnektör kullanın, iki ucu sıcak silikonla sabitleyin, boynun geçtiği yerde pay bırakın; lehimledikten sonra aşağıdaki sıfır noktası kalibrasyonuyla bir kez daha kontrol edin. [`imu_fault_ctx.py`](../tools/radxa/onboard-analysis/) her kopmayı o anda ne yapıldığı ve gerilimin kaç olduğuyla eşleştirebilir.


---

## Yazılım

**Bilgisayarda Clash'in TUN modu açıkken ana karta ping, SSH ve web erişimi çalışmıyor**
Belirti: 2026-10-11'de ana kart çevrimiçiydi (port taramasında 22 açıktı), ancak bilgisayardan ping gitmiyor, SSH `Error reading SSH protocol banner` hatası veriyor, tarayıcıda `http://192.168.0.102:8080` açılırken 502 alınıyordu.
Neden: Clash Verge'in TUN sanal ağ kartı (Meta), yerel ağ dahil tüm yönlendirmeyi devralıyor (`Find-NetRoute` çıktısı Meta üzerinden gidildiğini gösteriyor); ana karta giden bağlantılar bunun tarafından yakalanıyor.
→ TUN'u geçici olarak kapatın ya da Clash'te `192.168.0.0/16` aralığını doğrudan (direct) bağlantıya alın. Clash'e dokunmak istenmiyorsa, programda bağlantıyı kablolu ağ kartının yerel adresine bağlamak (Python'da `socket.bind(('192.168.0.100', 0))` ile bağlanıp ardından ana karta bağlanmak) bu engeli aşar; web arayüzü için bilgisayarda bir port yönlendirmesi kurulabilir ya da telefondan açılabilir.

**kissqy tek tıkla imajında G50 Pro eşleşiyor ama birkaç saniye sonra bağlantı kopuyor**
Belirti: 2026-10-13'te yeni kartta (kissqy R1 imajı), gamepad S konumundayken `bluetoothctl pair` başarılı görünüyor, hemen ardından bağlantı kopuyor ve padd gamepad'i okuyamıyor. Eski kartta aynı gamepad sorunsuz çalışıyordu.
Neden: Bu kartta Bluetooth açılışta "bağlanabilir/bonding yapılabilir" değil (nedeni araştırılmadı); eşleşme No Bonding ile dönüyor, anahtar saklanamıyor. BlueZ'in varsayılanı `ClassicBondedOnly=true` yalnızca daha önce bond edilmiş HID cihazlarını kabul ettiği için reddediyor. Resmi setup-board, `/etc/bluetooth/input.conf` içindeki `UserspaceHID` değerini bilerek false yapar (gamepad çekirdek üzerinden çalışır, bir çekirdekte yaklaşık %16 CPU tasarrufu sağlar; resmi kartta eşleşme sorunsuzdur); bunun burada etkisi olup olmadığı doğrulanmadı.
→ Eşleşmeden önce `btmgmt bondable on` verin, ardından `pair` → `trust` → hemen `connect` yapın; başarılı olunca `Nintendo Switch Pro Controller` ve `hid_nintendo` görünür. Biz o sırada ayrıca `input.conf` dosyasını `UserspaceHID=true`, `ClassicBondedOnly=false` olarak değiştirdik; birkaç ayar birlikte değiştiği için **yalnızca bir kez başarılı olduk, sonraki iki denemede eşleşme olmadı**. `UserspaceHID=true` daha fazla CPU yer; bir dahaki sefere önce yalnızca bondable'ı deneyin.
**Ek (10-15 akşamı, aynı kart)**: `pair`, `trust`, `connect` üç ayrı komut olarak girildiğinde eşleşme başarılı oldu ama gamepad bağlantıyı reddetti (`control_connect_cb() … Permission denied (13)`); gamepad'de HOME'a basıp geri bağlanmasını sağlayınca 10 saniye bağlı kalıp koptu, sistemde gamepad de görünmedi. Önce `btmgmt bondable on` ve `btmgmt connectable on` verin, `bluetoothctl remove <gamepad adresi>` ile eski kaydı silin, sonra **aynı** `bluetoothctl` oturumunda hepsini art arda yapın (`agent NoInputNoOutput` → `default-agent` → `scan on` → gamepad görünene kadar bekleyin → `pair` → `trust` → hemen `connect`): bu kez çalıştı, padd günlüğünde `pad connected — driving pad=Nintendo Switch Pro Controller` yazdı ve WiFi de kopmadı. Bu denemede `input.conf` hâlâ 10-13'te değiştirilmiş hâldeydi (`UserspaceHID=true`, `ClassicBondedOnly=false`); hangisinin şart olduğu ayrı ayrı doğrulanmadı.

**G50 Pro yalnızca en son eşleştiği kartı hatırlıyor, kart değişince yeniden eşleştirmek gerekiyor**
Belirti: Gamepad yeni kartla eşleştirildikten sonra eski karta geri dönüldüğünde gamepad eski karta bağlanmıyor.
Neden: Gamepad yalnızca son eşleşmenin anahtarını saklar; eski kartta kayıtlı anahtar bir öncekidir ve uyuşmaz.
→ Kart her değiştiğinde, o anki kartta gamepad'i yeniden eşleştirin (bir önceki maddedeki akış).

**Ördeğe verilen sabit IP, yerel ağdaki başka bir cihaz tarafından kullanılıyor; bilgisayar zaman zaman bağlanıp zaman zaman bağlanamıyor**
Belirti: 2026-10-13'te eski kart statik 192.168.0.102 kullanıyordu; aynı anda yerel ağdaki başka bir cihaz da (ağ kartı adresine göre telefon gibi görünüyor) .102 aldı ve bilgisayarın ördeğe bağlantısı kâh çalıştı kâh çalışmadı.
Neden: Yönlendiricinin DHCP'si ördeğin bu adresi elle aldığını bilmiyor ve adresi başkasına da dağıttı.
→ Yönlendiricide ördek için "statik adres atama" (MAC'e bağlama) yapın ya da ördeğin sabit IP'sini DHCP aralığının dışında seçin. Geçici çözüm: adresi kapmış cihazın WiFi'sini kapatın ya da bilgisayarda yönetici olarak bu IP'yi ördeğin MAC'ine statik bağlayın (`netsh interface ip add neighbors`; bilgisayar yeniden başlayınca geçersiz olur).

**Tüm sistem güç kaybedince hiçbir günlük kalmıyor: Armbian günlükleri bellekte tutuyor**
Belirti: Güç kesilip yeniden başladıktan sonra `journalctl`'e bakıldığında yalnızca bu açılışa ait kayıtlar var; kendi kaydımızın son birkaç saniyesi de karta yazılmamış. Ana kartta RTC yok, saat her açılışta geri sarıyor, bu yüzden zamana göre hangi dosyanın aranacağı da bulunamıyor.
Neden: Armbian günlükleri varsayılan olarak zram'da (bellekte) tutar, diske yazmaması SD kartı korumak için bilinçli bir tercihtir; Python'un dosya tamponu ise birkaç saniyede bir yazar.
→ Kayıt ve sistem günlüğü için ayrı birer servis açın, **her saniye fsync yapsın**, dosya adında açılış kimliği olsun (`/proc/sys/kernel/random/boot_id` değerinin ilk 6 hanesi). Betikler: [`tools/radxa/onboard-analysis/`](../tools/radxa/onboard-analysis/) altındaki `duck_rec.py`, `duck_journal.py` ve iki service dosyası. zram'ı kapatmayın (aşağıdaki "armbian-zram-config'i kapatmayın" maddesine bakın).

**Armbian'ın varsayılan `overlay_prefix=rk35xx` değeri yanlış; RK3566 overlay'leri `rk3568-*` adını taşır**
Önek yanlış olduğunda yükleyici hiçbir şey bulamaz ve sessizce başarısız olur; kart normal açılır, **ama `/dev/ttyS2` yoktur**. Bağlantıyı yanlış yaptığınızı sanırsınız. `apt upgrade` ile çekirdek değişince eski hâle dönebilir.
→ `/boot/armbianEnv.txt` içinde `overlay_prefix=rk3568` yapın, `overlays=uart2-m0` ekleyin ve yeniden başlatın. Resmi `setup-board.sh` tam olarak bunu yapar.

**Çekirdek konsolu da varsayılan olarak ttyS2 üzerinde**
UART2, RK3566'nın hata ayıklama seri portudur; Armbian çekirdek günlüğünü oraya, yani servo veri yoluna basar.
→ `/boot/armbianEnv.txt` dosyasındaki `extraargs` satırından `console=ttyS2,1500000` ifadesini çıkarın.

**Armbian varsayılan olarak UART2'de bir giriş konsolu çalıştırır**
`agetty`, `/dev/ttyS2`'yi tutar ve servolar bir türlü haberleşmez. Bağlantı doğru olsa bile haberleşme olmuyorsa büyük olasılıkla bunun sebebidir.
→ `systemctl mask serial-getty@ttyS2` komutunu verin, ardından `fuser -v /dev/ttyS2` ile başka bir sürecin tutmadığını doğrulayın.

**armbian-zram-config'i kapatmayın**
Armbian, günlükleri varsayılan olarak zram'da (bellekte) tutar ve diske yazmaz; bu, SD kartı korumak içindir. Bazıları günlükleri kolay izlemek için bunu kapatıyor ve yazma miktarı birkaç kat artıyor.
→ Açık bırakın. Resmi `deploy/README.md`'nin ifadesiyle: diske yazılmaması "bilinçli bir düzenleme"dir, kapatmak ise "her kartın kendi kararıdır, varsayılan değildir".

**i2c3'ü pin 3/5 üzerinde kullanınca USB-C PD pazarlığı kaybolur**
RK3566'nın i2c3'ü fabrika ayarında M1 pinmux'ta FUSB302'ye (USB-C PD) hizmet eder. Resmi overlay bunu M0'a (pin 3/5) taşır ve fusb302'yi devre dışı bırakır.
→ Bu bedel kabul edilir: USB-C yine 5 V verir, yalnızca pazarlık yapılmaz. Robotun gücü bataryadan geldiği için bunun etkisi yoktur.

---

**`wsl --mount` USB kart okuyucuyu bağlayamaz; imaj yazılmış karta dosya yazmayı bununla denemeyin**
Armbian'ın ilk açılış ön ayarı olan `.not_logged_in_yet` dosyasını WSL2 ile karttaki ext4 kök bölümüne yazmak için `wsl --mount \\.\PHYSICALDRIVE2 --partition 1` denendiğinde doğrudan `Wsl/Service/AttachDisk/MountDisk/HCS/ERROR_FILE_NOT_FOUND` hatası alınır. Bu, WSL'in USB çıkarılabilir disklere getirdiği bir kısıttır; kartın düzgün yazılıp yazılmamasıyla ilgisi yoktur.
→ Tersini yapın: dosyayı önce imajın içine koyun, sonra yazın. WSL'de `.img.xz` dosyasını yerel diske açın (`/mnt/` altına olmaz, loop bağlanamaz), `mount -o loop,offset=$((32768*512))` ile kök bölümü bağlayıp dosyayı yazın, sonra oluşan `.img`'i karta yazın. Betikler [`tools/radxa/`](../tools/radxa/) altında.

**Daha önce denenen Armbian imajı Zero 3W V1.12'de (AIC8800 WiFi sürümü) açılışta takılıyor: günlük ve sistem diskine bakarak teşhis edilmeli**
2024-11'den sonra çıkan Zero 3W, V1.12'dir; Armbian 26.2.1 / 26.8.1 vendor imajı yazıldığında LED kalp atışı gibi çift yanıp sönüyor (çekirdek başlıyor) ama initramfs'e hiç ulaşılmıyor, sistem diskine tek bayt dokunulmuyor ve yerel ağda kart hiçbir zaman bulunamıyor.
Radxa'nın resmi imajı aynı kartta, aynı kartla bir seferde açılıyor. Tek tek eleme sonrasında (kart, SDR104 yüksek hız modu, güç, aygıt ağacı aynı) fark yalnızca önyükleyiciye kalıyor:
Armbian, zero3 için ana hat U-Boot 2025.10 + 2024-01 tarihli bellek başlatma yazılımı v1.21 kullanıyor; Radxa'nın kendisi ise rk U-Boot 2017.09 + DDR v1.23 (2024-09) + BL31 v1.45 kullanıyor.
→ Radxa'nın `u-boot-rk2410` paketindeki `idbloader.img` / `u-boot.itb` dosyalarını kartın 64 / 16384 numaralı sektörlerine yazın, ardından Armbian için bir `/boot/extlinux/extlinux.conf` hazırlayın (Radxa U-Boot'u extlinux kullanır, boot.scr okumaz); çekirdeğe ve sisteme hiç dokunmadan hemen açılır.
Betikler [`tools/radxa/`](../tools/radxa/) altında, tek komutla kart hazırlar. Seri port olmadan bu tür sorunları bulma yöntemi: kartı okuyup kök bölümün yazılıp yazılmadığına bakmak, initramfs içine LED sinyali ve kara kutu günlüğü eklemek.

**V1.12J'de (2026-09 partisi) yalnızca önyükleyiciyi değiştirmek yetmez, aygıt ağacı da değişmeli**
Belirti: Önceki maddedeki gibi Radxa önyükleyicisi kullanıldı, Armbian yine açılmadı; Radxa'nın resmi B1 imajı ise açılıyor. Bazıları ayrıca soğuk açılışta HDMI takılıyken kartın hiç açılmadığını gördü.
Neden: Bu partideki kartların WiFi'si AIC8800DS2'ye değişmiş; Armbian'ın kendi `rk3566-radxa-zero3.dtb` dosyası bunu tanımıyor, Radxa B1 imajındaki sürüm tanıyor.
→ Önyükleyiciyi ve **DTB'yi B1 imajından alın**, extlinux'taki `fdt` satırını kopyalanan dosyaya yöneltin, çekirdek ve kök dosya sistemi Armbian'dan kalsın
(ikisi de 6.1 vendor çekirdeği olduğundan karışabilir). Grup üyeleri 2026-09-20'de gerçek kartta denedi ve çalıştı. DTB değiştirildikten sonra `/dev/ttyS2` ve USB seri portunun hâlâ var olup olmadığını doğrulayın; overlay'ler Armbian'a ait olduğundan düğümler uyuşmayabilir. Komutlar için [imaj kullanım kılavuzuna](11-radxa-imaj-kullanimi.md#6-kartınız-bu-seriden-değilse) bakın.

**Radxa önyükleyicisine geçildikten sonra `armbianEnv.txt` değişiklikleri işlemiyor**
Belirti: `/boot/armbianEnv.txt` içindeki `overlays=` satırına bir overlay eklendi (örneğin `i2c3-pihat`), yeniden başlatmadan sonra `/dev/i2c-3` hâlâ yok; resmi `setup-board.sh` ile değiştirmek de aynı sonucu veriyor, betiğin kendi kontrolü ise her şeyin yapılandırıldığını söylüyor.
Neden: Radxa U-Boot yalnızca `/boot/extlinux/extlinux.conf` dosyasını okur, Armbian'ın `boot.scr` betiğini çalıştırmaz; `armbianEnv.txt` dosyasını okuyan ise tam olarak `boot.scr`'dir.
→ Overlay'i `extlinux.conf` içindeki `fdtoverlays` satırına, dtbo dosyasının tam yoluyla (`/boot/dtb/rockchip/overlay/rk3568-xxx.dtbo`) yazın; yeniden başlatmadan önce dosyanın var olduğunu doğrulayın.

**AIC8800 GCMP-256'yı desteklemiyor; yönlendiricide WPA3 karma modu açıksa bağlanamıyor**
Zero 3W V1.12'deki AIC8800D80/DS2 yalnızca CCMP-128 destekler. Ev tipi yönlendiriciler (TP-LINK gibi) varsayılan olarak WPA2/WPA3 karma moddadır, WPA3 yarısı GCMP-256 kullanır ve el sıkışma başarısız olur.
→ wpa_supplicant'ta `key_mgmt=WPA-PSK`, `pairwise=CCMP`, `ieee80211w=0` değerlerini zorlayın (kart hazırlama betiğinde zaten var) ya da yönlendiriciyi yalnızca WPA2'ye alın. 5 GHz ve 2.4 GHz'in ikisi de bağlanır.

**Kart bilgisayara takılınca USB seri port yok: `dwc3-peripheral` overlay'i gerekir**
Zero 3W'nin OTG portunun aygıt ağacında `dr_mode = otg` yazılıdır; Armbian vendor çekirdeğinde bilgisayara takıldığında kendiliğinden aygıt moduna geçmez, `g_serial` yüklense bile bilgisayar bunu görmez.
→ extlinux'ta `rk3568-dwc3-peripheral.dtbo` (Armbian ile birlikte gelir) overlay'ini bağlayın, ardından `g_serial` + `serial-getty@ttyGS0` kurun; bilgisayara takınca ekstra bir COM portu görünür, doğrudan root olarak girilir; acil durum kurtarıcısıdır. Kart hazırlama betiğinde zaten var.

**Kart üzerinde resmi betikleri çalıştırırken GitHub'dan indirme yapılamıyor**
`setup-board.sh` / `install.sh` ikisi de raw.githubusercontent.com, api.github.com ve objects.githubusercontent.com'dan dosya indirir; Çin'den doğrudan bağlantı neredeyse tamamen takılır (IPv6 öncelikli olunca daha da kötüdür).
→ Bilgisayardaki Clash'te "yerel ağa izin ver" seçeneğini açın, kartta `/etc/environment` dosyasına `http_proxy=http://bilgisayar IP'si:7890` yazın (kart hazırlama betiğinin `card.conf` dosyasındaki `HTTP_PROXY=` alanına yazmak yeterli). apt, Debian deposunu kullandığı için vekile ihtiyaç duymaz.
Dikkat: Resmi kurulum, kurulum kancalarını updaterd üzerinden çağırır; kancadaki curl `/etc/environment` dosyasını okumaz. 2026-10-12'de ONNX Runtime indirilirken doğrudan bağlantı 90 saniyede zaman aşımına uğradı; root için `/root/.curlrc` dosyasına (tek satır: `proxy = "http://bilgisayar IP'si:7890"`) yazınca iki saniyede indi; kurulum bitince silmeyi unutmayın.

**Resmi install.sh yalnızca en son sürümü kuruyor, kissqy'nin R17'si ise 0.15.1 gerektiriyor**
Belirti: kissqy'nin R17'si resmi `daemon-v0.15.1` üzerine bindirilmiştir; resmi taraf 10-07'de 0.16.1'e çıkmıştır, `install.sh` her zaman en sonuncuyu kurar, sürüm belirtme seçeneği yoktur.
Neden: Betik, updaterd'nin GitHub'da latest'i kendisinin bulmasına bırakıyor.
→ `daemon-v0.15.1` yayın dosyalarını önce yerel olarak indirin, `install.sh` dosyasının bir kopyasında yayın etiketini `daemon-v0.15.1` olarak sabitleyin ve `updaterd install` komutuna `--from <yerel dizin>` ekleyin. İmza doğrulaması yine de yapılır. Düzeltilmiş betik `Radxa-Zero3W/official-daemon-v0.15.1/scripts/install-local.sh` yolundadır. Kurulumdan sonra `/etc/robot/updater.toml` içindeki `auto_apply` değerini `"off"` yapın ki kendiliğinden yükseltmesin.

**Ses kullanılmayacaksa resmi setup-board.sh'nin ses kısmını çalıştırmayın; uzaktan da migrate-network.sh çalıştırmayın**
Belirti: `setup-board.sh`'nin ses adımı apt ile Armbian vendor çekirdeğini kurar ve `/boot/Image`, `dtb`, `uInitrd` dosyalarını yeni çekirdeğe yönlendirir; `migrate-network.sh` ise WiFi'yi netplan'dan NetworkManager'a taşır.
Neden: V1.12 kart, Radxa'nın U-Boot'u ve `extlinux.conf` dosyasıyla açılır; uzaktan çekirdek değiştirmek kartın açılmaması riskini taşır. Bu adım yalnızca HAT üzerindeki ses çipini etkinleştirmek içindir, yürümek için ses gerekmez; HAT takılı değilse hiç gerekmez. Ağ geçişi sırasında WiFi koparsa uzaktan geri bağlanılamaz.
→ Ses istenmiyorsa ikisini de çalıştırmayın: servo seri port overlay'i ve seri konsolun devreden çıkarılması kart hazırlanırken zaten yapılmıştır. Yürüme için yalnızca resmi `install.sh`'nin kurduğu servisler yeterlidir.

**kissqy'nin R17'sini kurarken sistemde aic3104 ses kartı yoksa ses ayarında takılıyor**
Belirti: `service.sh upgrade`, `alsactl store aic3104` adımında 19 çıkış koduyla duruyor ve "kurulum tamamlanmadı; aşama: audio-setup" mesajı veriyor.
Neden: Onun kurulum betiği bu ses kartının her zaman var olduğunu varsayar. HAT takılı değilse ya da HAT takılı olsa bile resmi `setup-board.sh`'nin ses adımı çalıştırılmadıysa (2026-10-12'de ilk kart böyleydi), sistemde yalnızca HDMI ses kartı bulunur.
→ Bizim dalda düzeltildi (bu ses kartı yoksa ses ayarı atlanır, yürümeyi etkilemez). Onun orijinal paketi kullanılacaksa, önce paketteki `voice-setup.py` dosyasını düzenleyin, sonra `SHA256SUMS` dosyasını yeniden hesaplayın.

**kissqy'nin tek tıkla imajı R1, Armbian'ın orijinal önyükleyicisini kullanıyor; V1.12 kart açılmayabilir**
Belirti: 2026-10-12'de onun R1 imajı incelendi: önyükleme alanı Armbian ana hat U-Boot 2025.10 + bellek başlatma yazılımı v1.21, `boot.scr` ile çalışıyor; ilk kartımız (V1.12, AIC8800) Eylül'de tam bu kombinasyonda takılmıştı.
Neden: Onun kartı açılıyorsa, o partisi bu önyükleme düzeniyle uyumludur; V1.12'nin hepsinin açılamayacağı genelleştirilemez, ama bizim bu kartta kesin açılmadığı görülmüştür.
→ [`tools/radxa/kissqy-r1-v112.sh`](../tools/radxa/kissqy-r1-v112.sh) ile onun imajında Radxa önyükleyicisi değiştirilir ve extlinux yazılır (onun overlay'leri olduğu gibi taşınır), gerisine dokunulmaz. Çevrimdışı doğrulandı: önyükleme alanı Radxa paketiyle bayt bayt aynı, bölüm tablosu değişmedi, kök bölümde yalnızca beklenen birkaç yer değişti. **Gerçek robotta henüz denenmedi**; önce boş bir kartla deneyin, kullanımdaki kartı yazmayın. V1.12J için bir önceki maddedeki gibi aygıt ağacının da değiştirilmesi gerekebilir.

**kissqy'nin tek tıkla imajı R1 yalnızca veri yolundaki IMU küçük kartını tanıyor, IMU modülü kullanılamıyor**
Belirti: İmajdaki robotd (control.40) yalnızca ID 200'ü okuyan koda sahip ve küçük kartın kimliğinin `06 00 00 00 F2` olmasını bekliyor (onun FT6 yazılımı); I²C IMU okuma kodu yok, açılış yapılandırmasında da I2C4 açık değil. BNO085 ya da LSM6DSV16X modülü olan ördeklere yüklenirse "Feetech ID 200 yanıt vermiyor" hatasında takılıyor.
Neden: Onun tüm seti kendi donanımına göre yapılmış. Bizim robotd'ye eklediğimiz I²C IMU desteği (dal `hd1910-trunk-imu-i2c`) v146 kaynağı üzerine yazıldı; onun V164 kaynağı henüz açık değil.
→ IMU modülü kullananlar şimdilik kendi kurduğumuz v146 + I²C IMU düzeniyle devam etsin ([10-12 gerçek robot kaydına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy整套上机.md) bakın); V164 kaynağı açıldığında yama taşınabilir ya da ondan imaja eklemesi istenebilir.

**`service.sh init`, robotd çalışırken HOME komutunu gönderemiyor**
Belirti: Hareket modunda `sudo bash service.sh init` komutu `cannot claim robot IPC socket … another robotd owns this socket` hatası veriyor.
Neden: `robotd init` alt komutu robotd'nin kilidini tek başına almak ister, yalnızca robotd çalışmıyorken kullanılabilir. Onun kontrol uygulaması `/run/robotd.sock` üzerinden JSON-RPC gönderir (her satırda bir komut, `{"jsonrpc":"2.0","id":1,"method":"robot.init","params":{}}`).
→ Kontrol uygulamasının HOME düğmesini kullanın ya da sokete kendiniz `robot.init` gönderin. Politikayı başlatıp durdurmak için `robot.enable` (`{"on":true}` / `{"on":false}`), gücü kesmek için `robot.relax` kullanılır.

**Web joystick'i tuşa basılınca tepki vermiyor: dört katman üst üste biniyor, yalnızca aşırı ısınma değil**
Belirti: 2026-10-12'de kissqy kontrol uygulaması (R17 v1.0.146) bağlandı, veriler normaldi, web gamepad'inde HOME ve Start'a basınca tepki olmadı. Kontrol uygulaması günlüğünde "girdi süresi doldu, gönderilmedi" ya da "timed out" yazıyordu, padd arada `Failed to open "/dev/input/event4"` hatası veriyordu.
Neden: Her tuşa basışta yeni bir SSH bağlantısı açılıyor, webpad isteğe bağlı olarak başlatılıyor, sanal bir gamepad oluşturuluyor ve padd'in onu tanıması bekleniyor; dört katman da yavaş. ① Armbian her SSH girişinde 3,8 saniyelik karşılama betiğini boşuna çalıştırıyor; ② kontrol uygulaması kanalı 0,4 saniyede açamazsa isteği geçersiz sayıyor; ③ webpad'in soğuk açılışı ile padd'in gamepad'i tanıması 1–2 saniye sürüyor, tuşa tıklayıp bırakınca basış kayboluyor; ④ padd, sistem yeni aygıtı kaydetmeden onu açmaya çalışıyor, başarısız olunca tekrar denemiyor (padd'i root ile çalıştırmak da değiştirmedi, yetki sorunu değil). Gece yarısı bunun yalnızca aşırı ısınma olduğunu sandık; aşırı ısınma her katmanı biraz daha yavaşlatmıştı.
→ Fiziksel Bluetooth gamepad kullanın (sonraki madde), bu yolun tamamı atlanır. Web gamepad'i yine de kullanılacaksa önce SSH karşılama betiğini kapatın (ondan sonraki madde), tuşu 1–2 saniye basılı tutup bırakın. kissqy V164'te web gamepad'ini doğrudan robotd üzerinden çalışacak şekilde değiştirdi. Katman katman ölçümler için [10-12 gecesi gerçek robot kaydına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-夜-IMU校准与首次迈步.md#1-网页手柄按了没反应四层原因叠在一起) bakın.

**Thunder G50 Pro'yu fiziksel gamepad olarak kullanma: arkadaki düğmeyi S konumuna alın, Bluetooth ile doğrudan ördeğe eşleyin**
Belirti: Gamepad'in 2.4G alıcısı bilgisayara takılı olduğunda ördek için işe yaramıyor: kontrol web arayüzü bilgisayardaki gamepad'i okumuyor; alıcıyı da kafadaki ana karta takmak mümkün değil.
Neden: Hem resmi tasarım hem kissqy'nin tasarımı, Bluetooth gamepad'in doğrudan ana kartla eşleşip padd'in onu okumasına dayanır. G50 Pro'nun arkasındaki X / S / T / D platform seçimidir, kablolu/kablosuz seçimi değildir; S konumu Switch Pro gamepad olarak tanıtır, ana kartın çekirdeğinde sürücüsü vardır ve resmi eşleştirme aracı da destekler.
→ Bilgisayardaki alıcıyı çıkarın, arkadaki düğmeyi S'ye alın, kapalıyken HOME'a ışık hızlı yanıp sönene kadar basılı tutun; ana kartta `sudo systemctl start configd`, ardından `sudo robotctl pad pair` çalıştırın. Bulunamazsa `bluetoothctl` ile `Pro Controller` adresini tarayıp `robotctl pad pair <adres>` yapın. Eşleştikten sonra otomatik yeniden bağlanır. "≡" Start'tır (ilk basış HOME, ikinci basış modelin devralması), "⧉" Select'tir (güç kesme). Ana kart yapılandırmasında X, öne takla'ya bağlıdır; harf tuşlarına gelişigüzel basmayın.
**Ek (10-21, replika imajı 20261021b, üçüncü ördek): Bizim imajda X konumuna alınmalı, S konumu çalışmıyor.** S konumunda Studio'nun gamepad sayfasından eşleştirme yapılırken: yardımcı uygulama (resmi `robotctl pad pair`) eşleştiğini bildirdi, ancak çekirdekte gamepad'in girdi aygıtı hiç görünmedi, padd onu bekleyip bulamadı, gamepad birkaç on saniye sonra kendiliğinden kapandı; X konumuna (Xbox) alınca hemen bağlandı, acil durdurma ve yürüme normal çalıştı. Neden henüz araştırılmadı: o sırada ördeğin Bluetooth'u "bağlanabilir değil, bond edilemez" durumdaydı, `/var/lib/bluetooth` içinde de eşleşme kaydı kalmamıştı (ancak arada iki kez "unut"a basıldı, kaydın silinmesi bundan olabilir). Bir sonraki S konumu eşleştirmesinde `btmon` ile paket yakalayıp inceleyin.

**Armbian her SSH girişinde 3,8 saniyelik karşılama betiğini boşuna çalıştırıyor**
Belirti: SSH girişi yavaş; SSH'i sık açan araçlar (kissqy kontrol uygulamasının gamepad'i, ToF kanalı) kullanır kullanmaz zaman aşımına uğruyor, ana kartın CPU'su da sürekli meşgul kalıyor.
Neden: `/etc/pam.d/sshd` içindeki `pam_motd.so motd=/run/motd.dynamic` satırı her girişte `/etc/update-motd.d/` dizinini baştan çalıştırır; bunların içinden yalnızca `20-ip-info` 2,9 saniye, toplam 3,8 saniye tutar.
→ Önce yedek alın, ardından bu satırı yorum satırı yapın (`pam_motd.so noupdate` satırı kalsın). Değişiklikten sonra SSH üzerinden bir soru-yanıt döngüsü 3–4 saniyeden 0,7 saniyeye düştü.

**ToF takılı değilken kissqy kontrol uygulaması her 5 saniyede bir SSH'i yeniden bağlıyor**
Belirti: 10 dakika içinde ana karta 112 kez SSH ile giriş yapılmış, her seferinde bir önceki maddedeki karşılama betiği de çalışmış.
Neden: tofd kapalı (ToF takılı değil), kontrol uygulaması ToF aboneliği başarısız olunca sonsuza dek yeniden deniyor ve her deneme tam bir SSH girişi.
→ ToF takılı değilse kontrol uygulamasının ona abone olmasına izin vermeyin; bizim daldaki kontrol uygulamasına `--tofd-socket ""` eklendi.

**Gamepad'de Start'a iki kez basmak gerekiyor: ilk basış HOME, ikinci basış modelin devralması**
Belirti: Kalktıktan sonra joystick'i itince tepki yok, günlükte `the policy is not driving — press Start on the pad`; bazen ikinci basışta yeniden bir HOME yapıldı.
Neden: İlk basış yalnızca eklemleri duruş konumuna kilitler, model açılmaz; model ancak ikinci basışta devralır ve joystick o zaman çalışır. Devralmadan önce robotd duruşu da kontrol eder: her eklem HOME'dan en fazla 5° uzakta, gövde eğimi en fazla 10° olmalı ve bu 3 kare üst üste sürmeli; geçilemezse yeniden HOME yapılır.
→ Kalktıktan sonra elinizi çekin, kendiliğinden dengelenmesini bekleyip ikinci basışı yapın. Reddedilirse hangi koşulun geçilemediğine bakın: diz çöktü mü, IMU kaydı mı, gövde mi eğildi.

**Armbian ilk açılış ön ayarında iki değişken eksikse komut isteminde klavye bekleyerek duruyor**
`/root/.not_logged_in_yet` içinde `PRESET_DEFAULT_REALNAME` yazılmazsa "Please provide your real name" isteminde takılır; `PRESET_CONNECT_WIRELESS` yazılmazsa ve ağ yoksa "Connect via wireless? [Y/n]" isteminde takılır. Ekransız kart bu şekilde kilitlenir ve parola da fabrika değeri olan root / 1234 olarak kalır.
→ İkisini de yazın (kart hazırlama betiğinde zaten var).

**kissqy'nin kaynağında iki ayrı `padd.service` var, kurulum paketi `packaging/` altındakini kuruyor**
padd'in systemd ayarlarını değiştirirken (örneğin UDP gamepad için `AF_INET` izni vermek) yalnızca `padd/systemd/padd.service` dosyasını düzenlemek gerçek robotta etkili olmaz. kissqy'nin kurulum betiği (`packaging/gamepad.py`) `/etc/systemd/system/` altına `packaging/padd.service` dosyasını kopyalar; `padd/systemd/` altındaki, resmi proje geliştirmesi için kullanılan dosyadır.
→ İkisini birlikte değiştirin, sonra `packaging/SHA256SUMS` içindeki ilgili satırı da güncelleyin. Kurulu kartlarda yeniden kurulum yapmadan drop-in ile tamamlayın: `/etc/systemd/system/padd.service.d/` altına bir `.conf` koyun.

**padd çapraz derlenirken `libudev-sys` derleme hatası veriyor**
padd'in gamepad okumak için kullandığı gilrs, libudev'e bağlanmak ister; `cargo board` çapraz derlemesinde aarch64 libudev bulunamaz (robotd ve robotctl buna bağımlı olmadığı için daha önce karşılaşılmadı).
→ Depodaki `scripts/cross-sysroot.sh` betiğini kullanın; Debian'dan arm64 paketlerini indirip sysroot olarak açar. Çin'de `DUCK_DEBIAN_MIRROR=https://mirrors.ustc.edu.cn/debian` ayarlayın; betik bittikten sonra verdiği birkaç `export` satırını aynen geçerli kabuğa yapıştırın, ardından `cargo board -p padd` çalıştırın.

**Resmi yeni sürümde ve kissqy sürümünde arayüz sürüm numaraları ayrı ayrı artıyor, aynı sayı farklı anlama geliyor**
Resmi yeni sürümden kissqy tabanına özellik taşırken "sürüm numaraları yakınsa uyumludur" sanılabilir. kissqy resmi 0.15.1'deki 37'den kendisi 40'a çıkarmış, resmi taraf 37'den 0.17.1'deki 41'e çıkmış; iki tarafın eklediği arayüzler farklı.
→ Özellik taşırken çağrılacak her arayüzün kissqy'nin robotd'sinde bulunup bulunmadığını tek tek kontrol edin (bu seferki `sit_toggle`, `robot.policies.sitting` ve iki tür ses çıkarma kontrol edildi); resmi istemci kodunun tamamını olduğu gibi giydirmeyin.

**kissqy'nin yeni kontrol uygulamasındaki "gamepad bağlantısını onar" yalnızca GameSir Nova 2 Lite'ı tanıyor, G50 Pro için işe yaramıyor**
Belirti: 2026-10-13 akşamı kissqy'nin yeni sürümüne geçildi (kontrol uygulaması R17 V164 1.0.164), Thunder G50 Pro bağlanamadı; kissqy kontrol uygulamasındaki "gamepad bağlantısını onar" düğmesine basılmasını önerdi.
Neden: Bu özellik (`console/gamepad_repair.py`) özellikle GameSir Nova 2 Lite için yazılmıştır: gamepad adı kodda sabittir; onarım sırasında bu bağlantıyı temizler, yeniden eşleştirir ve gamesir-xboxd üzerinden sanal bir Xbox gamepad'ine dönüştürür (kissqy'nin açıklaması: resmi düzen yalnızca Xbox gamepad'lerini tanır, diğer gamepad'ler Bluetooth ile bağlansa da kimlik doğrulamadan geçemez ve orada takılır). Başka bir gamepad ile karşılaşırsa doğrudan reddeder, G50 Pro'nun eşleşmesini silmez, dolayısıyla G50 Pro için işe yaramaz. G50 Pro'nun yeni kartta bağlanamamasının bulduğumuz nedeni başkadır: Bluetooth'un "bond edilemez" olması, eşleşmenin No Bonding ile dönmesi (yukarıdaki "kissqy tek tıkla imajında G50 Pro eşleşiyor ama birkaç saniye sonra bağlantı kopuyor" maddesine bakın).
→ G50 Pro'yu [10-13 gecesi §1.2](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-夜-掉电-舵机D与蹭地.md#12-g50-pro-配对上又被断开) uyarınca elle eşleştirin (`btmgmt bondable on` → `pair` → `trust` → hemen `connect`) ya da yeni sürümün web gamepad'ini kullanın (kissqy, SSH'in sürekli bağlı kalacak şekilde değiştirildiğini söylüyor). Onun "onar" özelliği isteniyorsa, birlikte çalıştığı Nova 2 Lite satın alınmalı.

**Kendi değiştirdiğiniz robotd'yi kurduysanız, kissqy kontrol uygulamasında "firmware kur / yükselt"e basmayın**
Belirti: Bu düğme karttaki robotd'yi değiştirir. robotd'ye eklediğimiz I²C IMU desteği ve yerel olarak ayarlanabilir sürümde yapılan P / D / tork ayarları silinir (koddan çıkarım, gerçekten basılmadı).
Neden: Geri yüklenen, kissqy kurulum paketinin içindeki robotd'dir; kurulum betiği ayrıca `servo-test-parameters.json` dosyasını siler (bilerek, eski sürümün elle girilmiş parametrelerini temizlemek için).
→ Bizim yerel kontrol uygulamamız, ayarlanabilir sürümümüzün olduğu karta bağlıyken bu düğmeyi engeller; ancak kissqy'nin orijinal kontrol uygulamasıyla bağlanıldığında ya da eski kartta (R17 + I²C IMU yaması) eski kontrol uygulamasıyla bağlanıldığında kimse engellemez, basmayın. Gerçekten orijinaline dönülecekse kissqy'nin orijinal kontrol uygulamasıyla kurun ve sonrasında servolara bir kez güç kesip verin ("servonun P / D / tork sınırı RAM'de tutulur" maddesine bakın).

**Fork'un kalibrasyon modunda Studio sürekli "ana program başlıyor" gösteriyor**
Belirti: 2026-10-20'de yeni kartta ana program kalibrasyon modunda çalışıyor (`--commissioning`), servolar ve IMU okunuyor ama Studio sürekli "ana program başlıyor" yazıyor, hiçbir değer göstermiyor, başlangıç kontrol listesinin ilk iki adımı yapılamıyor.
Neden: `robot.busStatus` başlangıç aşamasında açılış raporu döndürür (`phase: configuring_bus`). Hareket modunda ilk başarılı okumadan sonra bu temizlenir, kalibrasyon modunda hiç temizlenmez, bu yüzden hep `configuring_bus` döner ve gerçek zamanlı anlık görüntü (`ready`, `last_sample`) hiç verilmez. Bilgisayarda yakalanmamasının nedeni, sahte ana programımızın "sanılan davranışa" göre yazılması ve kalibrasyon modu başlar başlamaz anlık görüntüyü döndürmesiydi.
→ fork `341b68f`: kalibrasyon modunda da ilk başarılı okumadan sonra temizlenir. Eski fork'ta belirti `phase` değerinin sürekli `configuring_bus` kalması, `total_success` değerinin ise artmasıdır. Sahte ana program ve test verisi, gerçek robotta kaydedilen yanıtlar aynen taklit edilerek yazılmalı.

**Bilgisayarda Clash açıkken (sistem vekili) `http://duck-xxxx.local:8000` 502 veriyor**
Belirti: 2026-10-21'de ördek evdeki WiFi'ye bağlandı, tarayıcıda `duck-0de6.local:8000` 502 verdi, IP ve `duck-0de6:8000` ile ise normal açıldı.
Neden: Clash sistem vekilinin atlama listesi `localhost;127.*;192.168.*;10.*;172.16-31.*;<local>`. `<local>` yalnızca noktasız adlar için geçerlidir; `.local` noktalıdır, dış alan adı sayılıp vekile gönderilir.
→ Windows'ta `.local` olmayan `http://duck-xxxx:8000/` adresini kullanın (LLMNR üzerinden gider, atlama listesindedir) ya da doğrudan IP girin; Apple cihazlarda `.local` kullanın; TUN modu açık olanlar vekil yazılımında yerel ağı doğrudan bağlantıya alsın. Studio ve kılavuz adresleri cihaza göre veriyor.

**Kendi hazırladığımız imajda SSH 22 portu reddediyor: hiçbir ana makine anahtarı üretilmemiş**
Belirti: 2026-10-21'de doğrulama kartının 2. sürümünde ördek ping'e yanıt veriyor, web açılıyor, ama SSH 22 portu doğrudan bağlantıyı reddediyor.
Neden: Debian'ın `sshd-keygen` servisi yalnızca "ilk açılışta" çalışır (`ConditionFirstBoot`). İmaj hazırlanırken `/etc/machine-id` boş dosyaya çevrildi, systemd bunu ilk açılış saymıyor, anahtarlar üretilmiyor, `sshd -t` başarısız oluyor ve ssh başlamıyor.
→ `ssh.service` için bir drop-in ekleyin: her başlatmadan önce `ssh-keygen -A` (mevcut olanlara dokunmaz) ve ardından `sshd -t` çalışsın. İmaj hazırlarken "ilk açılışta" bir işin kendiliğinden yapılmasına güvenmeyin, yapılacak işi servise kendiniz yazın.

**Başlangıç kontrol listesinde 1. ve 2. adım atlanınca, ana programa yazıldıktan sonra yine kalibrasyon modunda kalıyor**
Belirti: 2026-10-21'de yeni kartta servo sıfır konumu daha önce kalibre edilmişti, IMU'yu da yeniden kalibre etmek istenmedi; ilk iki adım atlandı, 3. adımda yazıldıktan sonra ana program başladı ama hareket moduna geçmedi.
Neden: Fork'un hareket moduna geçmesi için "kullanılan IMU'nun yönünün onaylanmış" olması gerekir. 2. adım atlanınca yön hiç onaylanmaz.
→ Studio 3. adım: 2. adım tamamlandı ya da atlandı olarak işaretlenmişse ve yön onaylanmamışsa, varsayılan montaj yönüyle yazılıp onaylanmış olarak işaretlenir (veri yolu küçük kartı için resmi montaj, BNO085 için fork varsayılanı, LSM6DSV16X modülü için x aşağı, z ileri). Farklı monte edilenler, ayakta bir kez kalibre ettikten sonra yazsın.

**Kalibrasyon modunda ördek ayağa kalkamıyor, yalnızca tek servo dönüyor ve dönünce gücü kesiyor**
Belirti: Önce ayakta IMU kalibre edilip sonra ana programa yazılmak istendi. Studio'daki "duruş etkinleştir" kalibrasyon modunda gri; ancak önce IMU'yu varsayılan montaja göre bir kalibrasyonla yazıp hareket moduna geçerek ayağa kalkılabiliyor.
Neden: Fork'un kalibrasyon modunda yalnızca tek servo hareketi (konuma gidince güç kesilir), merkeze alma ve sıfır konumu kaydetme var; "tüm gövdeyi ayakta tutma" yok.
→ fork `f4bbe53` ile `hold-home` eklendi: 15 servo birlikte 3 saniyede HOME'a döner, kilitlenir, IMU normal okunur, acil durdurma normal çalışır. Studio'da kalibrasyon modunda "duruş etkinleştir" doğrudan bunu çağırır. Yalnızca dengelemez, destek verilmelidir. 10-21'de yazıldı, gerçek robotta henüz denenmedi.

**Yeni kartta güç verince ördeğin erişim noktasının çıkması yaklaşık 2 dakika sürüyor** (20261021b'de düzeltildi)
Belirti: 2026-10-21'de imaj yazıldıktan sonraki ilk açılışta, telefonda `Microduck-xxxx` ağı iki dakika aranınca görünebildi.
Neden: İlk açılışın kendisi bölüm genişletme, adlandırma ve IMU tanıma yapar; ağ yapılandırma programı da erişim noktasını açmadan önce "hiçbir WiFi'ye bağlanılamadığını" tam 45 saniye doğrular. Yeni kartta kayıtlı hiçbir WiFi olmadığı için bu 45 saniye boşuna beklenir.
→ 20261021b'den itibaren: kayıtlı hiç WiFi yoksa, ağ koptuğu anda erişim noktası hemen açılır; kayıtlı WiFi bilgisi belirlenemiyorsa eskisi gibi 45 saniye beklenir. Eski imajda biraz daha beklenmelidir.

## Politika eğitimi ve gerçek robota aktarım

**Çalıştırma programını mümkünse mevcut olanın üzerinde değiştirin, kendi başınıza yeni bir tane yazmayın**
Belirti: Eylül sonunda önce servo ve IMU'yu denemek için bir Python çalıştırıcı yazıldı, zamanla politika çalıştırıcısına dönüştü; 10-11'de kissqy'nin modelini bununla çalıştırmak istenince ritim, voltaj, yön, servo parametreleri elendikten sonra da yürümedi, geriye kalan fark tamamen çalıştırma katmanındaydı ve ilerleyen araştırma tıkandı.
Neden: Politika çalıştırma tarafına çok duyarlıdır: kontrol periyodu, eylem filtresi, eklem hızının bir kare gecikip gecikmediği, IMU ile servonun aynı anda okunup okunmadığı hepsinin eğitimle ve özgün yazarın çalıştırma tarafıyla uyumlu olması gerekir. Ayrı bir tane yazmak, her ayrıntıyı görünmeyen bir değişkene çevirir. Resmi robotd o sırada yalnızca Dynamixel'i destekliyordu; 9-18'de Feetech uyarlaması için fork yaptık, IMU'yu bağlayamadan takıldık ve Python yazmaya geçtik.
→ Çalışan bir çalıştırma tarafı varsa (resmi robotd, kissqy'nin R17'si), onun üzerinde değişiklik yapın, eksik olanı ekleyin (örneğin robotd'ye I²C IMU eklemek). Kendi yazdığınız küçük araçlar yalnızca donanımı test etmek içindir (servo muayenesi, yön doğrulaması, tek eklem hareketi), politika çalıştırmak için kullanılmaz.

**Yürüme modelini test ederken gövdeyi elle taşımayın**
Belirti: 2026-10-11'de kissqy'nin walk modelinde, gövde elde tutulurken 0 / 0,05 / 0,15 m/s verildiğinde yalnızca duruş değişti ve sonraki birkaç saniye hareket olmadı; yere konup desteksiz bırakılınca 0,4 saniye içinde iki bacak dönüşümlü bükülüp esnemeye başladı.
Neden: Bu tür modellerin girdisinde "ritim" yoktur; adım atma gövde sallanması ve ağırlık aktarımından doğar, IMU ve eklem geri bildirimiyle devam eder. Gövde elle taşınınca sallanma olmaz, çıktı kısa sürede hareketsiz bir duruşta kalır.
→ Yere koyun, ellerinizi iki yanda 2–3 cm mesafede tutun, devrilirse yakalayın. Hız 0 zaten "ayakta durma" demektir; yürüyüp yürümeyeceğini buna bakarak anlayamazsınız.

**Yürümeye başlar başlamaz tüm gövdenin gücü kesiliyor: önce modele değil çalıştırıcının korumalarına bakın**
Belirti: Ördek adım atmaya başlar başlamaz duruyor, ardından tüm servolar birlikte gücünü kesiyor ve ördek çöküyor.
Neden: Çalıştırıcının iki koruması tezgâhtaki küçük hareketlere göre ayarlanmıştı. Birincisi, herhangi bir servonun voltajı 6,6 V'un altına düşerse durdurur; yürürken akım büyür, 7,4 V besleme servo ucunda 6,5 V'a düşünce tetiklenir. İkincisi, durduktan sonra yerinde tutarken konum sapmasının ≤ 1° olduğunu doğrular; hareket hâlindeki ya da P5 altında çökmekte olan bir ördek bunu sağlayamaz ve sonuç "tümünün gücünü kesme" olur.
→ Düzeltildi: tutma ve toparlanma aşamasında düşük voltaj artık güç kesmez, tutma ölçütü 5°'ye gevşetildi, ayağa dönüş için hâlâ 1° geçerli. Güç kaynağı yaklaşık 8,0 V'a ayarlanarak pay bırakıldı (HD-1910 üst sınırı 8,4 V); 7. denemede 10 saniyelik koşunun en düşük voltajı 7,6 V oldu.

**Kazancı bir anda çok artırmayın, akım güç kaynağını çökertir**
Belirti: P5'te bacak hedefe yetişemedi (6–7° fark), P10'a geçilince 0,24 saniye içinde servo akım okumalarının toplamı yaklaşık 26 A oldu, 14 servonun voltajı birlikte 5,4–5,8 V'a düştü ve koruma durdurdu.
Neden: P büyüdükçe aynı hatada servo daha fazla güç uygular, on küsur servo birlikte zorlanınca ayarlanabilir güç kaynağı yetmez. Ayrıca eğitimde BAM'de P5 kullanıldı, P'yi artırmak başlı başına eğitim koşullarından sapmadır.
→ Artırılacaksa önce 6–8 deneyin, voltajı izleyin; büyük hareketler yapılacaksa 2S lityum batarya gibi anlık onlarca amper verebilen bir kaynak kullanın.

**Kalkış anında voltaj çöküyor: harekete yumuşak başlangıç ekleyin**
Belirti: Eğitimdeki gibi (ölçeksiz, filtresiz) çalıştırıldığında 0,3 saniye içinde 14 servonun voltajı birlikte 4,6–5,2 V'a düştü ve koruma durdurdu.
Neden: İlk kare doğrudan modelin istediği duruşa atlıyor, on küsur servo aynı anda sert kuvvet uyguluyor, kalkış anındaki akım tepesi en büyük ve ayarlanabilir güç kaynağı ile kablolar yetişemiyor.
→ Çalıştırıcıya yumuşak başlangıç eklendi: ilk 1 saniyede hareket genliği 0'dan %100'e doğrusal artar (kissqy yapılandırmasında varsayılan olarak açık, `--ramp` ile değiştirilebilir). Eklendikten sonra aynı parametrelerle 10 saniye tamamlandı, en düşük voltaj 7,5 V oldu. Yumuşak başlangıç yalnızca kalkışı kapsar; hareket tam genliğe ulaştıktan sonra ayarlanabilir güç kaynağı yine çökebilir, uzun vadede batarya gerekir.

**kissqy'nin 0,9 / 0,5 / 0,7 değerleri eğitim parametresi değil**
Belirti: Onun dağıtım paketinde iki ayrı sayı kümesi var: `deployment-profile.toml` ölçek 1,0, filtresiz yazıyor; `deployment-execution.json` ise ölçek 0,9, baş filtresi 0,5, bacak filtresi 0,7 yazıyor.
Neden: Model eğitimde 1 / 1 / 1 ile eğitildi; 0,9 / 0,5 / 0,7, onun resmi ördek çalıştırma programından (Dynamixel için ayarlanmış) aldığı varsayılanlardır; onun robotd'si ikincisini tercih eder ve ayrıca voltaj telafisi 7,4/V ile çarpar.
→ İkisini de deneyin: çalıştırıcı varsayılan olarak onun çalışma değerlerini kullanır, `--training-mapping` eklenirse eğitimdeki gibi çalışır. Her parametrenin işlevi için [2026-10-11 kissqy gerçek robot ölçümlerine](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261011-kissqy-walk上机实测.md#3-运行参数每个是干什么的为什么有两套) bakın.

**R17 kurulurken ve hata ayıklama moduna geçerken servolar önce gücünü kesiyor, ördek çöküyor**
Belirti: 2026-10-12'de R17 kurulurken gücü açık duran ördek aniden gevşedi; hata ayıklama (commissioning) modundaki robotd her başlatılışında 15 servonun hepsinin gücünü keser.
Neden: Onun tasarımı "açılışta gücü kes"tir: kurulumun ilk adımında eski servis gücü keser, hata ayıklama modu başlarken de önce güç keser. Hareket modu başlarken kendiliğinden güç kesmez.
→ R17 kurmadan, "kalibrasyon moduna geç"e basmadan, hata ayıklama modunu yeniden başlatmadan önce ördeği tutun ya da yatırın.

**IMU yönünü doğrularken yumuşak ördeği elle tutmayın: önce HOME'a ayağa kaldırıp sonra ölçün**
Belirti: IMU montaj yönü onaylanırken gövdenin dikey olması ve dikeyden en fazla 5° sapması isteniyor. Güç verilmemiş ördeğin bacakları yumuşaktır, elle tutulduğunda ilk okuma 15,2° çıktı ve geçilemedi.
Neden: Elle tutulan duruş zaten eğridir (bu seferki yaklaşık 13° öne eğik, yaklaşık 8° sola yatık) ve yumuşak ördek hafif sallanınca değişir.
→ Önce ördeğe güç verip HOME'da ayağa kaldırın (servo-web'deki "duruş" ile resmi HOME aynı açı kümesidir), kendi kendine dururken 4,95° okundu; ardından tüm ördeği 15–30° öne eğip değişimin tam öne doğru olup olmadığına bakın. robotd'nin `verify-imu` komutu şimdilik yalnızca hata ayıklama modunda kullanılabiliyor ve hata ayıklama modu başlar başlamaz güç kestiği için 2026-10-12'de servo-web okumalarıyla aynı ölçüt elle yazıldı; ayrıntılar için [o geceki kayda](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy整套上机.md) bakın.
**Düzeltme (2026-10-12 gecesi)**: O seferki 4,95° değerinin büyük kısmı IMU'nun eğik monte edilmesinden kaynaklanan sapmaydı, ördeğin gerçek duruşu değildi. Yönü doğru yapmak yetmez, sıfır noktasını da kalibre etmek gerekir; aşağıdaki "IMU 8,5° eğik monte edilmiş" maddesine bakın.

**Başka bir programla güç verildikten sonra kissqy'ye geçilirse HOME reddediliyor**
Belirti: Ördek servo-web ile ayakta duruyordu, R17 hareket moduna geçilip HOME gönderildiğinde 4 kez `ID 20: temporary P/D readback mismatch; torque-on refused` hatası alındı.
Neden: Onun programı servonun zaten güçlü olduğunu görünce bunu kendisinin daha önce verdiği güç sanar, yalnızca P/D değerlerinin kendi istediği P5/D20 olup olmadığını denetler, yeniden yazmaz. servo-web'deki güç P32/D40 kullandığı için denetim tabii ki geçmez.
→ Önce güç kesin (`robot.relax`, ördeği tutun), sonra HOME yapın (`robot.init`). P5/D20 yazılır, geri okunarak doğrulanır, güç verilir ve 2 saniye içinde HOME'a dönülür. HOME sırasında gövde dikeyden en fazla 10° sapmalı.

**IMU 8,5° eğik monte edilmiş: model devralır devralmaz geriye doğru fırlıyor**
Belirti: 2026-10-12 gecesi model devralınca hızlısı 0,6 saniyede, yavaşı 21 saniyede geriye doğru düştü, bacak hedefleri ±90°～±100°'ye dayandı; devralmadan önce gövde okuması ne kadar öne eğikse kontrol kaybı o kadar hızlı oldu. IMU eksen yönü, jiroskop ve eklem hızı işaretleri kontrol edildi, hepsi doğruydu.
Neden: Model eğitilirken ördek HOME'da, ayaklar düz basarak duruyor, gövde yataydı (resmi MJCF'in `STAND` anahtar karesi, IMU 0° okur). Bizim BNO085 modülümüz yaklaşık 8,5° öne ve 1,75° sağa eğik monte edilmişti: ördek dik dururken IMU "8,5° öne eğik" diyor ve model sürekli geriye doğru kurtarmaya çalışıyor. Resmi eğitim kodundaki yorum da gerçek robottaki sabit eğim sapmasının çalışma zamanında giderilmesi gerektiğini, eğitimin bununla ilgilenmediğini yazıyor.
→ HOME'da durun, gerçek robotun o anki eklem açılarını simülasyona koyup gövdenin "olması gereken" eğimini hesaplayın, IMU okumasından çıkarın; fark sapmadır, bunu IMU montaj kuaterniyonuna ekleyin (M′ = C ⊗ M). Adımlar ve betik için [`tools/radxa/onboard-analysis/`](../tools/radxa/onboard-analysis/) dizinine bakın. Kalibrasyondan sonra model 70 saniye devralınca düşmedi, ortalama eğim 0,2° oldu, joystick itilince dönüşümlü adım atmaya başladı. Tam araştırma için [10-12 gecesi gerçek robot kaydına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-夜-IMU校准与首次迈步.md#4-一接管就猛冲怎么一步步找到-imu-偏差) bakın.

**IMU okumaları kayar: düşme ya da IMU'ya çarpma sonrası sıfır noktasını yeniden kontrol edin**
Belirti: HOME'da duran, eklem açıları neredeyse aynı olan ördekte IMU'nun öne eğim okuması önce 5,2°, sonra 8,6° oldu.
Neden: IMU modülü kımıldamış (arada birkaç kez düşüldü, IMU'nun kablosuna da basıldı); baskı parçalarının yük altında bükülmesi ve servo kolunun gevşekliği de bir iki derecelik fark yaratabilir.
→ Modülü sağlam sabitleyin (biz ortakla vida ile sabitlemeyi konuştuk; sabitledikten sonra sıfır noktasını yeniden kalibre edin). Sert düşme, IMU'ya çarpma ya da kablo değişimi sonrasında bir önceki maddeye göre bir kez daha kontrol edin; sapma 1°～2°'yi aşıyorsa yeniden kalibre edin.

**HOME'da dururken dizler eziliyor, gövde gerçekten öne eğiliyor**
Belirti: Aynı şekilde HOME'a basıldığında bazen iki diz yerine oturuyor, bazen 5°～9° eziliyor ve gövde 17° öne eğiliyor, ikinci Start basışı reddediliyor.
Neden: HOME eğitimdeki P5 kazancını kullanır, biraz yumuşaktır, dizler en büyük yükü taşır; ayağa kalkış biçimine göre durulan yer de değişir.
→ Düz zemine koyun, elinizi çekin, dengelenmesini bekleyip ikinci basışı yapın. Bunun için kazancı artırmayın: eğitim koşullarından sapar ve akım güç kaynağını çökertir (yukarıdaki "Kazancı bir anda çok artırmayın" maddesine bakın).

**Powerbank servoları kaldıramıyor: akım artınca 5 V'a geri düşüyor**
Belirti: Çökmüş duruştan HOME'a dönülürken voltaj 5 V'a düşüyor; yerine ulaşılamıyor, ikinci Start basışı reddediliyor, yeniden HOME yapılıyor ve döngü sürüyor.
Neden: PD hızlı şarj powerbank'ı ve tetikleme kablosu, aşırı akımda protokol koruması nedeniyle 5 V'a geri düşer. Servolar 5 V'ta tork ve hızlarının yüzde otuz–kırk kadarını yitirir; 5 V ayrıca HAT'ın ana kartı beslemek için düşürdüğü voltajın alt sınırına da değer, ana kart yeniden başlayabilir.
→ NP-F550 batarya ya da ayarlanabilir güç kaynağı kullanın (8,0 V, akım sınırı maksimum). Ayarlanabilir kaynağın kabloları kısa ve kalın olmalı: 8 V'ta bile servo ucunda gerilim yaklaşık 7,0 V'a düştü, kablo üzerinde 1 V kayıp fazla.

**Ayak tabanı TPU'sunun da yumuşak ve sert türleri var: 95A sert kalıyor; taban çok kaygansa model küçük adımlarla koşturur (simülasyonda böyle, gerçek robotta doğrulanacak)**
Belirti: 2026-10-12 gecesi ile 10-13 arasında, ördek masa üzerinde joystick itilince iki bacakla dönüşümlü adım attı, ama adımlar küçük ve parçalıydı, ileri gitme azdı; kullanıcı fare altlığına koyunca biraz daha iyi hissetti (his, veri yok).
Neden: kissqy ayak tabanının TPU olması gerektiğini hatırlatmıştı, bizim tabanımız zaten TPU, ama **95A**, yani sert. kissqy, kendi 90A'sının iki günde sertleşip kaymaya başladığını, sonra 85A'ya geçtiğini söyledi. Bu modelin eğitiminde ayak sürtünmesi yalnızca 0,7～1,3 arasında rastgele değiştirildi, daha kaygan bir zemin görmedi; simülasyonda yalnızca sürtünme değiştirildiğinde 0,5 neredeyse etkisizdi, 0,3'te 4,5 Hz'lik parçalı adımlara ve neredeyse tamamen yüksek frekanslı titremeye dönüştü, ayak yalnızca 7 mm kalktı, 0,2'de yürüyemedi. Ancak D 0 yapıldıktan sonra gerçek robot aynı masada titremeyi bıraktı, simülasyon bunu açıklayamıyor; bu yüzden "çok kaygan" yalnızca elenemeyen bir şüpheli. Gerçek sürtünmeyi henüz ölçmedik.
→ Yumuşak taban ucuzdur, denemeye değer: 85A TPU ya da PLA ayak tabanına 1～2 mm silikon / kauçuk kaymaz parça yapıştırmak (iki ayakta aynı kalınlık, düz ve tam yapıştırılmış, ayak ucu pahlı, ayak tabanından taşmayacak; 机械行者Robo montaj videosunun 1. bölümündeki parça listesinde ayak tabanı grubunda "ayak tabanı / kaymaz ped" de var); kalın sünger ve EVA kullanmayın. Sürtünmeyi eğik tahta ile ölçün: sürtünme katsayısı = tan (kaymaya başladığı açı), 35° ≈ 0,7 eğitimin alt sınırıdır; tüm ördek üstüne konunca önce devrilir, aynı malzemeden alçak bir numune kullanın. En kolay doğrulama: aynı parametreler, aynı masa, taban değişiminden önce ve sonra birer koşu yapıp titreme ile yerden kalkmayı karşılaştırmak. Ayrıntılar için [10-14 gündüz kaydı §6](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md#6-脚底摩擦和鞋底).

**Simülasyonu gerçek robotla karşılaştırmadan önce koşulları eşitleyin: hareket ölçeği, filtre, ağırlık, hız**
Belirti: 2026-10-14 sabahı simülasyonla gerçek robot karşılaştırıldı; simülasyonda destek dizi düzleşebiliyor ve ayak 12 mm kalkıyordu, gerçek robotta düzleşmiyor ve yalnızca 5 mm kalkıyordu; bunun üzerine servo parametrelerinden, ağırlıktan ve ayak tabanından şüphelenildi.
Neden: Simülasyon ile gerçek robotun koşulları farklıydı, sabah eşitlenmemişti. Gerçek robotta, eski kartta birleşik modelin fiili hareket ölçeği yaklaşık 0,83 (0,9 × voltaj telafisi 7,4 / voltaj), bacak filtresi 0,7, baş 0,5 idi; simülasyonda 1,0 ve filtresizdi. kissqy'nin eğitimde kullandığı model 820 g (model paketindeki `deployment-contract.json` içindeki parça kütleleri toplamı), bizim simülasyonda kullandığımız resmi model 737 g. Eşitledikten sonra (ağırlık kissqy'nin eğitim modeli 820 g olarak tahmin edildi) simülasyondaki destek dizi +3,5° / +6,5°'den −3,4° / −3,5°'ye geldi, gerçek robottaki −4,5° / −2,6°'ye yaklaştı; yalnızca hareket ölçeği 0,83 farkın büyük kısmını açıkladı.
→ Simülasyonla karşılaştırmadan önce gerçek robotta fiilen kullanılan değerleri listeleyip tek tek eşitleyin: hareket ölçeği (`robot.busStatus` → `loaded_models.walk.runtime_execution_profile` bölümüne bakın, sonra voltaj telafisiyle çarpın), baş ve bacak filtreleri, tüm ördeğin ağırlığı (tartın), P / D / tork, servo voltajı, joystick hızı (tam itme). Eşitledikten sonra bile simülasyonda gerçek robotta olmayan yüksek frekanslı titreme görülüyor, nedeni araştırılmadı; bu yüzden simülasyon sayılarını yalnızca yön olarak alın. Ayrıntılar için [10-14 gündüz kaydı §1, §2](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md#1-仿真怎么做的跟真机差在哪).

**Birleşik modelin ölçek ve filtresi `robotd.toml` içinde değil, toml'u değiştirmek işe yaramaz**
Belirti: 2026-10-13'te `robotd.toml` içinde `action_scale` (1,0, 0,8) ve baş-bacak filtreleri değiştirilip birkaç karşılaştırma yapıldı, sonuçların hepsi daha sonra geçersiz sayıldı.
Neden: kissqy'nin birleşik modeli (`scale_use = joint_uniform`), model paketinin kendi `deployment-execution.json` dosyasını kullanır (R17'de kurulan sürümde ölçek 0,9, baş 0,5, bacak 0,7; V164'te aynı model için ölçek 1,0 yazıyor), robotd bunu ayrıca voltaj telafisiyle (yaklaşık 7,4/voltaj) çarpar; toml'daki değerler yalnızca diğer modeller için geçerlidir.
→ Değiştirmeden önce parametrenin nerede etkili olduğunu doğrulayın: `robot.busStatus` → `loaded_models.walk.runtime_execution_profile` robotd'nin fiilen kullandığı değerleri gösterir. Birleşik modeli değiştirmek için paketindeki `deployment-execution.json` dosyasını düzenleyin, gücü kesip robotd'yi yeniden başlatın.

**Yerde sürtme: önce hangi ayağın hangi bölümünün alçak olduğunu hesaplayın, sıfır konumunu kalibre etmeye ya da sağ-sol bacakları ayrı ayarlamaya acele etmeyin**
Belirti: 2026-10-14'te ördek yürürken yere sürtüyordu, özellikle sol ayak belirgindi. Önce gövdenin sola eğik olduğu, IMU'nun yanlış olduğu ya da sıfır konumunun doğru olmadığı sanılıp sağ-sol bacakları ayrı ayarlamak istendi.
Neden: Gövde IMU'ya göre düzeltildikten sonra zemin boşluğu hesaplandı (`tools/gait-analysis/foot_clear.py`), **iki ayak da simülasyonun yalnızca yarısı kadar kalkıyor** (3～6 mm, simülasyonda 11～12 mm): destek sırasında model dizin düzleşmesini istiyor, gerçek robot sürekli bükülü tutuyor (servo parametreleri aynı 1910 modeli; fark P, tork sınırı ve ağırlık gibi koşullarda, hâlâ ayrıştırılıyor). Sol ayağın daha çok sürtmesinin nedeni, adım atarken ayak ucunun aşağı bakması (sağ ayakta ve simülasyonda en alçak nokta topuk) ve sağ bacak destekteyken gövdenin 1,5° daha fazla öne düşmesi; ikisi de D 0 yapıldıktan sonra ortaya çıktı. IMU yatış düzeltmesi yapıldı; eklem sıfır konumları ön-arka yönde sol ve sağda aynı, sol-sağ yönde iki ayak için hesaplanan fark yaklaşık 1,6°～2,6°, henüz araştırılmadı.
→ Parametrelere dokunmadan önce betikle "hangi ayak, uç mu topuk mu, hangi eklem, gövde nasıl hareket ediyor" netleştirin. D ile ilgiliyse önce başka bir D kümesi deneyin; servo okumalarında görünmeyenleri (ayağın düz basmaması, mekanik gevşeklik) yandan ağır çekim ve elle yoklama ile inceleyin. Dikkat: IMU sıfır noktasının 1° kayması hesaplamada iki ayak arasında yaklaşık 2 mm fark yaratır, önce IMU'yu kalibre edip sonra sol-sağ karşılaştırmasını yapın. Ayrıntılar için [10-13 gecesi gerçek robot kaydı §7](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-夜-掉电-舵机D与蹭地.md#7-蹭地两只脚都只抬了仿真的一半).
**Ek (10-14 gündüz)**: Simülasyon gerçek robotun hareket ölçeğine (yaklaşık 0,83), baş-bacak filtrelerine ve kissqy'nin eğitim ağırlığına (820 g) eşitlendikten sonra destek dizi gerçek robota yaklaştı; simülasyonda "dizin düzleşmemesi" büyük ölçüde bu koşullarla açıklanabiliyor (yukarıdaki "Simülasyonu gerçek robotla karşılaştırmadan önce koşulları eşitleyin" maddesine bakın); simülasyonda ölçeği 0,83'ten 1,0'a çıkarmak ayağı yaklaşık 3 mm daha kaldırıyor, gerçek robotta birleşik ölçeği 1,0 yapıp voltaj telafisiyle çarpmak yalnızca %11 artış getiriyor (simülasyonda %20), doğrusal tahminle etki simülasyonun yaklaşık yarısı kadar olur, yine de denemeye değer. Sol-sağ yönde iki ayağın aynı düzlemde olmaması da incelendi: iki kalça yatış ekseni dışa açılıyor, her seferinde farklı, vücut ağırlığıyla bastırılıyor gibi görünüyor (tahmin; "Servo / kalibrasyon" bölümüne bakın). Ayrıntılar için [10-14 gündüz kaydı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md).

**BNO085'in yürürken kendi hesapladığı duruş rastgele sıçrıyor: "iki üç adımda düşme"nin kök nedeni**
Belirti: 2026-10-12 ile 10-14 arasında, model devraldıktan sonra duruş sağlamdı, ama joystick itilince iki üç adım atıp öne devriliyordu; ayak tabanını, servo D değerini, filtreyi ve ölçeği değiştirmek işe yaramadı. Ayak yere ne kadar iyi tutunursa (koli bandı → silikon) ve servo ne kadar sert olursa o kadar hızlı düşüyordu.
Neden: BNO085 çipinin kendi birleştirdiği duruş (oyun dönme vektörü) yürürken (nöbet başlangıcı yaklaşık yarı yarıya ayağın basışının öncesi-sonrası) 20 ms içinde 20～60° sıçrıyor, aynı anda çipin jiroskobu yalnızca 1～2° dönmüş oluyor. Modelin gördüğü yerçekimi yönü de onunla birlikte sıçrıyor, model kendisinin devrildiğini sanıp düzeltince gerçekten devriliyor. Joystick itilerek yürünen karelerde rastgele sıçrama oranı %1,9 (koli bandı) ile %23～32 (silikon, P5) arasında; kalkıştan sonra ilk nöbetin ortanca zamanı 1,8 s, yani tam "iki üç adım"; yürürken düşmelerin yaklaşık sekizde yedisinde düşmeden önceki 1,5 s içinde sıçrama var (taban çizgisi yok, yalnızca referans). Jiroskobun kendisi güvenilir: kuaterniyon türevinden hesaplanan açısal hızla korelasyonu 0,97～0,99, bacağın düz kinematiği de jiroskobun yanında. Kuaterniyon ham değerlerinin uzunluğu normal, I²C okuma hatası değil. Çipin içinde neden sıçradığını göremiyoruz, tahminimiz ayak basış darbesinin ivmeölçer düzeltmesini bozması.
→ Çipin duruşuna güvenmeyin, çipin jiroskobunu kendiniz entegre edin: robotd'nin `[trunk_imu] bno08x_fusion = "gyro"` ayarı (bizim fork'umuzdaki [`hd1910-v167-gyro-fusion`](https://github.com/fanhao375/Microduck-kissqy/tree/hd1910-v167-gyro-fusion) dalı, varsayılan hâlâ `chip`, kendiniz değiştirmelisiniz; nasıl yapılacağı oradaki IMU-MODULE.md 4.4'te, **nano ile ya da sed ile elle anahtar eklemeyin**). 10-15 akşamı gerçek ölçümler: chip modunda joystick ile 9 s'de 2 düşme; gyro modunda joystick ile 60 s'de hiç düşme olmadı, walk modunda 10 dakikadan fazla kalındı (joystick'li 60 s) yalnızca 1 düşme oldu, çip yine 745 kez sıçradı, modelin gördüğü yol onunla birlikte sıçramadı. Tam bir sıralı karşılaştırma yapılmadı, kullanıcı sahada izleyip doğrudan gyro kullanmaya karar verdi. Tam süreç için [10-15 kaydına](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261015-IMU乱跳根因与陀螺融合上机.md) bakın.

**Üç gün parametre ayarlamak yerine önce verinin kendi içinde tutarlı olup olmadığına bakın; çalıştırabilen biriyle farkları tek tek karşılaştırın**
Belirti: 10-12 ile 10-14 arasında ayak tabanı, servo D, filtre, ölçek ayarlandı, simülasyonla karşılaştırıldı; her seferinde "biraz daha iyi gibi, ama değil gibi" oldu ve model yeniden eğitilmeye hazırlanıldı.
Neden: Sorun bu parametrelerde değildi. Grupta aynı servolar, aynı kissqy modeliyle "P5 D0, geri kalan her şey varsayılan" ayarlarıyla çalıştırabilen biri vardı; bu da servo ve modelin sağlam olduğunu, sorunun bizimle onun farklarında (IMU çipi, güç, ağırlık, ayak tabanı, mekanik) olduğunu gösteriyordu. Gerçek ipucu "fiziksel olarak imkânsız" bir olguydu: jiroskop pek dönmediğini söylerken duruş onlarca derece sıçrıyordu.
→ Önce çalışan kişiyle aranızdaki farkları listeleyin ve tek tek eleyin (ağırlık 806 g, eğitim 820 g, elendi; parametreler onunkiyle aynı yapıldı, yine düştü; geriye en çok şüphe IMU'ya kaldı). Sonra "önceki kare yerçekimi + bu kare jiroskobuyla 20 ms ileri tahmin, bu karenin yerçekimiyle farkı > 5°" gibi tutarlılık kontrolüyle yalan söyleyen sensörü bulun. Yeni algoritmayı önce gölge modda çalıştırın (yalnızca eşlik eder, yayınlamaz), gerçek robot verisiyle sorun olmadığı doğrulanınca geçin. Ölçüt ve parça parça istatistik betikleri: [`tools/radxa/onboard-analysis/`](../tools/radxa/onboard-analysis/) altındaki `judge_block.py`, `ab_blocks.py`.

**Sıçrama ölçütü de yanıltabilir: kayıttaki jiroskop üçlü medyandan geçtiği için duruştan bir kare geç**
Belirti: 10-15 akşamı chip gölge bölümünde, jiroskop birleştirme yolu eski ölçüyle 5 kez "5° üzeri sıçradı" dedi; 4'ü düşmeden önceki yarım saniye içinde, 1'i joystick yeni bırakılmış ve gövde şiddetle sallanırken oldu. gyro modunun yayın yoluyla simüle edildiğinde 0 kez, ama en büyüğü 3,75° idi, payı yalnızca 1,25°; "1 kez olunca chip'e dön" kuralı, düşmenin kendisi tarafından her an tetiklenebilir.
Neden: Kayıttaki `imu.gyro` üçlü medyandan geçmiş, gerçekte bir kare geç; `imu.fusion.fused` ise medyandan geçmemiş. Bir kare geç gelen açısal hızla ileri tahmin yapıldığında, vücut saniyede 130～640° dönerken 5° fark çıkıyor. O 5 karede birleştirme çipi "reddediyordu" (yalnızca jiroskop entegrasyonu, adımla sıçrama imkânsız), birleştirilmiş kuaterniyonun iki kare arasındaki dönüşü 100 Hz ham jiroskop entegrasyonuyla uyuşuyor (bildirilen hizalama farkı içinde). İleri tahmin için bir sonraki karenin jiroskobu kullanılınca 0 kez oldu.
→ İleri tahmindeki açısal hız, duruşun gecikmesiyle hizalanmalı: modelin gördüğü yol (`safety.gravity`, o da medyandan geçmiş) bu karenin jiroskobuyla, birleştirme ham değeri bir sonraki karenin jiroskobuyla eşleşmeli. Durdurma kuralı birleştirme hükmüne göre ayrılır: sıçrama öncesi-sonrası ±2 karede `realign_long`, `realign_gap`, `fallback`, `follow` varsa 1 kez bile chip'e dönülür; yalnızca kabul, ret ve hız sınırlı takip olanlarda, düşmeden önceki 1 s içindeki ya da önceki karede eğimi ≥30° olanlar sayılmaz, geri kalan her bölümde ≥3 kez olursa chip'e dönülür. IMU okuması takılıp (birkaç kare güncellenmeme, toparlanınca bir karede yakalama) da yumuşak basamak sayılabilir, tek tek bakılmalı. Bkz. [10-15 kaydı §5.5](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261015-IMU乱跳根因与陀螺融合上机.md#55-停止规则判跳变的尺子在摔倒时会误报).

**IMU düzeltildikten sonra dönüş çok zayıf: eklemler hedefin yalnızca yarısına ulaşıyor** (henüz çözülmedi)
Belirti: 10-15 akşamı gyro modu kararlı yürüyebildikten sonra sağ joystick ile dönüş: yerinde dönüş komutun dörtte biri kadar (58°/s komutta yalnızca 15°/s), yürürken dönüş neredeyse hiç dönmüyor (61～79°/s komutta yalnızca −4～11°/s, bir seferinde ters döndü).
Neden: Model hedefi ile servo gerçeği karşılaştırıldığında: kalça sapması %57～95, kalça yatışı %31～56, diz %48～55, kalça eğimi %45～67 oranında takip ediyor. Bacak yalnızca yarısı kadar sallanıyor, ayak kalkamıyor, havada ayağı döndüremiyor; tamamen silikon taban yere yapışınca da burulmuyor (tahmin). Dönüş yalnızca gyro modunda ölçüldü; koda göre dönüşte kullanılan açısal hız her iki modda da çipin ham jiroskobu olduğundan IMU değişikliğiyle ilgisi olmadığı çıkarılıyor; ayrıca bunun daha önce söylenen "dizler yalnızca yarısı kadar sallanıyor" olduğu, daha önce IMU sıçramalarının bunu örttüğü çıkarılıyor.
→ Her seferinde tek şeyi değiştirin: önce çalıştırabilen kişiye dönüşün nasıl olduğunu ve tabanın hangi malzeme olduğunu sorun; sonra hareket ölçeğini 0,9 → 1,0 deneyin; sonra servo P 5 → 6, 7; 10 A güç kaynağıyla yeniden karşılaştırın. Her seferinde aynı yöntemle ölçün: yerinde sola ve sağa 3'er saniye dönüş, yürürken birkaç dönüş, gerçek dönüş hızı ile eklem takip oranını karşılaştırın.

## Araçlar

**STM32G0 boş çipte ilk programlamadan sonra program çalışmıyor, ST'nin kendi Bootloader'ında kalıyor**
Belirti: CubeProgrammer ile yazma ve geri okuma doğrulaması tamam, sıfırlamadan sonra program hiç tepki vermiyor: RAM'de hâlâ açılıştaki rastgele değerler duruyor, CPU durdurulunca PC = `0x1FFF…` (sistem belleğindeki Bootloader; R6/R7 yazmaçları USART1/I²C1, arayüzleri tarayarak biri programlasın diye bekliyor). Neden: G0, güç verildiğinde Flash'ın ilk kelimesinin boş olup olmadığına bakar, sonucu `FLASH_ACR.EMPTY` içinde tutar, bu **yalnızca güç açılışında (seçenek baytları yüklenirken) güncellenir**; boş çip güç alınca EMPTY=1 olur, yazmadan sonraki yazılım sıfırlaması yeniden kontrol etmez, çip hâlâ boş olduğunu sanır.
→ **Boş çipe ilk yazmadan sonra gücü kesip yeniden verin**. Sıfırlama düğmesi (NRST) de yeniden kontrol yaptırmaz, işe yaramaz. Sonraki yazmalarda (Flash boş değilken) bu sorun olmaz (2026-09-22, imu_to_dxl ilk kart).

**ST-LINK/V2'nin 20 pinli konnektörü her üreticide aynı değil, GND yalnızca 12/18/20 numaralı pinlerde güvenilir**
ST'nin resmi tanımında 4/6/8/10 numaralı pinler de GND'dir, ancak bazı sürümlerde (örneğin UART/SWIM'li olanlarda) 4/6/8/10/14 numaralı pinler hata ayıklayıcı tarafında UART-RX, UART-TX, BOOT0, SWIM, SWIM-RST'dir. Resmi tabloya göre GND'yi 4. pine bağlamak, hedef kartın toprağını hata ayıklayıcının seri portuna bağlamak demektir. Ayrıca **1. pin TVCC yalnızca voltajı ölçer, güç vermez**; bazı sürümlerde **19. pin VDD dışarı 3,3 V verir**.
→ SWD için yalnızca dört kablo bağlayın: **1 TVCC, 7 SWDIO, 9 SWCLK, 20 GND**; kart kendi gücünü veri yolundan alıyorsa 19. pini bağlamayın, iki güç yolunu paralel yapmayın. Bağlandıktan sonra ST-Link tekrar tekrar kopuyorsa (Aygıt Yöneticisi'nde "aygıt tanımlayıcı isteği başarısız") büyük olasılıkla bağlantı onun gücünü çökertiyordur: önce ST-Link'i tek başına takıp sağlam olduğunu doğrulayın, sonra karta bağlayın.

**Keil çok eski, CMSIS 6 projesini derleyemiyor: `cmsis_clang.h` bulunamıyor**
MDK 5.24, Arm Compiler 6.7 ile gelir; CMSIS 6'nın `cmsis_compiler.h` dosyası `__ARMCC_VERSION >= 6100100` (6.10.1) gerektirir, sürüm yetmeyince sıradan clang sanılır ve hiç var olmayan bir `cmsis_clang.h` aranır.
→ MDK 5.4x kurun (5.41, 6.22 ile gelir; lisanssız 32 KB sınırlı Lite sürümü, bu yazılım 10 KB olduğundan yeterli). `Keil.STM32G0xx_DFP` aygıt paketi eski Keil'de de ayrıca kurulmalı.

**URT-2'de önce servolara güç verip sonra USB takılırsa veri yolu çalışmıyor**
Belirti: 15 servonun hepsi yanıtsız, yalnızca yayın ping'inde birkaç bayt hep sıfır geliyor; multimetreyle veri yolu S–G boşta yalnızca 2,1 V ölçülüyor (normali 4,5 V civarı); USB takılı değilken kartın 5 V pin başlığında nedensiz 2,1 V var. Kart servolar çıkarılıp yüksüz bırakılınca S–G yine 4,5 V ile iyi. Sebep, kartın mantık gücünün yalnızca USB'den gelmesi; servo tarafı veri yolunu önce 5 V'a çekiyor, kartta henüz güç yokken akım S pininden kartın 5 V rayına geri akıyor, USB sonradan takılınca seviye çevirme kısmı yarı ölü bir durumda takılı kalıyor ve veri yolunu 2,1 V'da tutuyor.
→ **Sıra: önce USB'yi takın, sonra servolara güç verin**. Ters yapıldıysa iki tarafı da çıkarıp baştan başlayın. S/G ters takıldı ya da kart bozuk diye acele etmeyin (2026-09-17'de bunun için bir saat harcandı).

**VS Code'un Markdown Editor eklentisi HTML görsellerini göstermiyor**
README'de `<table><img>` ile yapılmış iki sütunlu kartlarda, bu eklenti çıplak HTML içindeki göreli yolları çözmez, görseller boş kalır. GitHub'da sorun yok.
→ VS Code'un kendi önizlemesini kullanın (`Ctrl+Shift+V`).

**Windows'ta `core.autocrlf=true` ikili dosyaları bozar**
PDF başlıkları çoğunlukla ASCII'dir, git otomatik algılamada yanlışlıkla metin sanar, checkout sırasında LF→CRLF dönüşümü yapar ve dosya doğrudan bozulur.
→ `.gitattributes` dosyasında `*.pdf *.stl *.step *.png` vb. hepsini `binary` olarak bildirin.

**GitHub'da Release yayınlarken `--target` için kısa commit numarası verilirse başarısız oluyor; ek dosya adında Çince kullanmayın**
Belirti: 2026-10-20'de `gh release create … --target 36854c7` komutu `Release.target_commitish is invalid` hatası verdi; Çince dosya adlı ekler yüklendikten sonra adları değiştirildi.
Neden: API yalnızca 40 haneli tam commit numarasını veya dal adını kabul eder; ek adlarında yalnızca ASCII korunur.
→ `--target $(git rev-parse HEAD)` kullanın; ekleri İngilizce adlandırın (`microduck-replica-tarih-licenses.txt`), Çince açıklamayı yayın sayfasının gövdesine yazın.

**Ana sayfadaki iki sütunlu kartın içine Markdown tablosu koyunca tüm sütun bozuluyor**
Belirti: 2026-10-20'de README'deki elektrik kartına bir kart karşılaştırma tablosu eklendi, itildikten sonra mekanik ve algoritma sütunları kayboldu.
Neden: Kartlar `<table><td>` ile yapıldı, içine bir de Markdown tablosu koymak GitHub'ın işlemesinde iç içe tabloyu dış tabloyu bozacak hâle getiriyor.
→ Kartların içinde yalnızca liste kullanın; ana sayfayı değiştirmeden önce `gh api markdown` ile işleyip tarayıcıda ekran görüntüsüne bakın, sonra itin.

**Windows'ta Python ile metin düzenlenince satır sonları sessizce CRLF'ye dönüşüyor**
Belirti: 2026-10-12'de Windows'ta Python'un `Path.write_text` ile kissqy dalındaki `voice-setup.py` dosyasında 3 satırlık yorum değiştirildi, commit sonrası `git diff --stat` dosyanın 150'den fazla satırının tamamının değiştiğini gösterdi.
Neden: `write_text` Windows'ta varsayılan olarak `\n`'yi `\r\n` yazar; o deponun `.gitattributes` dosyası `-text` olduğundan git satır sonu dönüşümü yapmaz ve CRLF olduğu gibi commit'e girer. `core.autocrlf=true` olan depolarda commit sırasında LF'ye geri çevrilir, fark edilmez, ama çalışma dizinindeki dosya yine de değişmiş olur.
→ Python ile dosya değiştirirken `open(p, 'w', newline='')` yazın ya da bayt olarak okuyup yazın; commit'ten önce `git diff --stat` satır sayısının gerçekte değiştirilenle uyuşup uyuşmadığına bakın, `file dosya_adı` CRLF olup olmadığını gösterir. O seferki durum `d1dcfa6` commit'iyle LF'ye geri çevrildi.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
