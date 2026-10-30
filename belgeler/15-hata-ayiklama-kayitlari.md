# Hata Ayıklama Kayıtları

**Basitleştirilmiş Çince (özgün dil)**

> **Güncel durum: HAT geldi ve ana kartla birleştirildi; şu an Radxa resmi B1 sistemi çalışıyor, Wi-Fi / SSH normal, kamera flat kablosu ayarlandıktan sonra 1920×1080 görüntü alındı.**
> Son güncelleme: 2026-09-28. Resmi sistem şu an yalnızca kamera karşılaştırması için kullanılıyor; proje çalışma ortamı henüz geri yüklenmedi. Orijinal Armbian, doğru kablo bağlantısıyla henüz yeniden denenmedi.

[Yapım günlüğü](16-yapim-gunlugu.md) **mekanik** tarafı kaydeder: baskı, deneme montajı, toleranslar.
Bu belge ise **elektrik ve yazılım** tarafını kaydeder: önce **adım adım bir kullanım kılavuzu** (parçalar gelince nasıl yapılandırılır, nasıl bağlanır, nasıl test edilir), aşağıda ise **tarihe göre süreç** (ne yapıldı, ne görüldü, sıradaki adım ne) yer alır.

Sonuç niteliğindeki tuzaklar ayrıca [Tuzaklar](14-tuzaklar.md) belgesinde derlenmiştir. Kartların ve çiplerin ne olduğu, neden seçildikleri [Donanım başlangıç rehberi](03-donanim-baslangic.md) belgesindedir.

---

## İlerleme

| Tarih | Aşama | Durum | Not |
|---|---|---|---|
| 2026-09-10 | Servolar + programlama/test kartı geldi | ⚠️ Sorun çıktı | Test kartının TTL portu servonun 2.0 mm kablosuyla uyuşmuyor |
| 2026-09-12 | Ana kart, ToF, pil, pil yuvası, SD kart, pin başlık, kamera tamam | ✅ Tamamlandı | Pin başlık Radxa'ya lehimlendi |
| 2026-09-12 | Servoların mekanik parçalara takılması | ✅ Tamamlandı | **HD-1910 ile XL330 arasında yapısal fark var**; parçalar değiştirilip yeniden basılınca uyum sağlandı |
| 2026-09-13 | 15 servoya ID atama | ✅ Tamamlandı | Kesilmiş servo kablosu URT-2'ye havadan bağlanarak tek tek yapıldı |
| 2026-09-13 | Tezgâhta veri yolu (bus) bağlantısı (URT-2 ↔ Radxa) | 🔨 Sürüyor | 7.4V URT-2'ye, USB Radxa host portuna |
| 2026-09-16 | Ana kart çıplak halde güç verme | ✅ Tamamlandı | Sorun yok |
| 2026-09-16 | Ana karta imaj yazma (2G kart / microSD) | ❌→✅ | Armbian resmi imajı V1.12 kartta açılmadı (önyükleyici); Radxa önyükleyicisine geçilince 09-17'de açıldı, aşağıya bakın |
| 2026-09-17 | Resmi betikler setup-board / migrate-network / install | ✅ Tamamlandı | ttyS2, NetworkManager, ONNX Runtime, daemon 0.13.0 |
| 2026-09-17 | 15 servonun tamamı veri yolunda (URT-2 ↔ bilgisayar) | ✅ Tamamlandı | 0 zaman aşımı, 0 sağlama hatası, 15 servo senkron okuma 4.8 ms; bir saat kaybettiren şey URT-2'nin güç verme sırasıydı |
| 2026-09-17 | Web hata ayıklama paneli `tools/servo-web/` | ✅ Tamamlandı | Kaydırıcılar, duruşlar, diziler, 3D takip, ağırlık merkezi gösterimi, register dışa aktarımı |
| 2026-09-18 | Sıfır kalibrasyonu, ayakta duruş, "büzül ↔ ayağa kalk" dizisi | 🔨 Sürüyor | Kendi başına kalkıp oturabiliyor ([video](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/首次上电-2026-09-18.mp4)); 4 servonun sıfırı yeniden kalibre edilecek, yönü ters olan 4 servo panelden ± ile çevriliyor |
| 2026-09-17 | `imu_to_dxl` kartı geldi, güç verildi | ✅ Tamamlandı | 3.3 V normal. J4/J5 soketlerinin aralığı doğru ama **gövdesi Feetech kablosuna uymuyor**; gövde kesilince takılıyor, v2'de soket değişecek |
| 2026-09-22 | `imu_to_dxl` Feetech protokollü yazılım (firmware) 0.2.0 | ✅ Masa başı doğrulandı / ⚠️ Gerçek veri yolunda test bekliyor | Geliştirme kartına yazıldı, IMU çalışıyor; kabul sınırları [firmware açıklamasında](https://github.com/fanhao375/microduck-replica/tree/789ef5e45b6102d7e71fecefbf58606520147cfa/hardware/imu_to_dxl/firmware/) |
| 2026-09-28 | HAT geldi, ana karta takıldı ve ana kartta güç verme hata ayıklaması | 🔨 Sürüyor | Ana kart → kamera sırasıyla madde madde kontrol; HAT ses, servo veri yolu ve yük kabulü DEĞİLDİR |
| 2026-09-28 | Bozuk ID 21'in değiştirilmesi ve orta konum kalibrasyonu | ✅ Kullanıcı onayladı | Eski ağız ID 34 servosu ID 21 yapıldı, kullanıcı FD ile 2048 kalibrasyonunun başarılı olduğunu doğruladı; ağız şimdilik yok |
| 2026-09-28 | Resmi B1 imajıyla karşılaştırma | ✅ Tamamlandı | Wi-Fi / SSH gerçekten test edildi, Radxa Camera 8M overlay'i etkinleştirildi |
| 2026-09-28 | Kameranın tanınması ve görüntü alınması | ✅ Kısa süreli yakalama geçti | Flat kablo ayarlandıktan sonra `0x0219` okundu, 40 kare 1920×1080; kalıcı kare hızı ve proje entegrasyonu test bekliyor |
| — | HAT basmadan ana karta jumper kabloyla bağlantı | 📋 Yedek plan | Şimdilik gelen HAT kullanılıyor, jumper kablo belgesi saklanıyor |

Gösterge: 📋 planlandı · 🔨 sürüyor · ✅ tamamlandı · ⚠️ sorun çıktı · ❌ bu yol çıkmaz

---

## Elde olanlar

| Parça | Adet | Durum |
|---|---|---|
| Feetech HD-1910-C001 | İlk alınan 15 | Orijinal ID 21 bozuldu, ağız ID 34 servosu ID 21 yapıldı; şu an ağız yok, "15 servonun tamamı çevrimiçi" ifadesi mevcut durum olarak kullanılamaz |
| Feetech FE-URT-2 test kartı | 1 | ✅ 2026-09-10'da geldi |
| Radxa Zero 3W 2 GB (çıplak kart, eMMC yok) | 1 | ✅ 2026-09-12'de geldi, **pin başlık lehimli** |
| Radxa Zero 3W 8 GB + 64 GB eMMC | 1 | 📦 Ay sonu |
| NP-F550 pil + pil yuvası | — | ✅ 2026-09-12'de geldi |
| VL53L8CX ToF | 1 | ✅ 2026-09-12'de geldi |
| Radxa Camera 8M219 (IMX219) | 1 | ✅ Resmi B1'de tanındı ve görüntü verdi, 2026-09-28 |
| RPI Robot HAT | 1 | ✅ Geldi, takıldı; çevre birimlerinin işlevleri tek tek hata ayıklanıyor |
| Yüksek dayanıklılıklı microSD | — | ✅ 2026-09-12'de geldi |
| 2×20 pin başlık | — | ✅ Geldi ve lehimlendi |
| `imu_to_dxl` PCB + SMT | 5 | ✅ 2026-09-17'de geldi, ¥629.72 (¥ = Çin yuanı); güç verilince 3.3 V normal, konnektör ayak izinde (footprint) sorun var |
| Kart okuyucu, 5 V düşürücü modül | — | ✅ 2026-09-16'da geldi |
| Dönüştürücü kablo, yarım dubleks dönüştürücü kart | — | 📋 Alınacak (tezgâhta şimdilik URT-2 idare ediyor) |

---

## Feetech kaynakları nerede

Yerel `飞特-HD1910/` klasöründe yalnızca teknik şartname PDF'i, DWG ve STP var. **Yazılım ve kılavuzlar Gitee'de, resmi sitede değil:**

| Ne gerekiyor | Nerede |
|---|---|
| **FD hata ayıklama yazılımı** + **CH340 sürücüsü** | **Depoda mevcut: [`tools/飞特/`](https://github.com/fanhao375/microduck-replica/tree/789ef5e45b6102d7e71fecefbf58606520147cfa/tools/飞特/)** (FD 1.9.8.5 + sürücü, MIT, sha256'lı). Özgün kaynak [gitee.com/ftservo/fddebug](https://gitee.com/ftservo/fddebug) |
| Örnekler / haberleşme protokolü / bellek tablosu | [gitee.com/ftservo](https://gitee.com/ftservo) altındaki depolar |
| Resmi site yazılım sayfası (yedek) | [feetech.cn/software.html](https://www.feetech.cn/software.html) |
| Başlangıç kılavuzu PDF | [先看这里-入手教程 (Önce buraya bakın — başlangıç kılavuzu)](https://www.feetech.cn/Data/feetechrc/upload/file/20220618/%E5%85%88%E7%9C%8B%E8%BF%99%E9%87%8C-%E5%85%A5%E6%89%8B%E6%95%99%E7%A8%8B2-1.pdf) |

---

## Servo yapılandırması · Parçalar gelince adım adım

**Hedef**: 15 HD-1910'un her birine ID atamak, korumaları açmak ve etiket yapıştırmak; böylece montaj sırasında elinize alınan servonun hangi eklem olduğu hemen bilinsin.

### Gerekenler

| Parça | Açıklama |
|---|---|
| HD-1910-C001 × 15 | Fabrika ID'si **hepsinde 1** |
| FE-URT-2 test kartı + USB-C kablo | Soldaki iki beyaz 3 pinli port kullanılır (serigrafi `TTL-Bus`, `G V1 S`). Sağdaki 4 pinli port RS485'tir, kullanılmaz |
| Kesilmiş bir servo kablosu | Test kartının portu servonun 2.0 mm kablosuna **takılmaz**, havadan bağlanması gerekir. 15 kablodan biri feda edilir |
| Güç | Üç seçenek var, 3. adıma bakın. **Yalnızca ID atamak için USB yeterlidir** |
| Yazılım | [`tools/飞特/`](https://github.com/fanhao375/microduck-replica/tree/789ef5e45b6102d7e71fecefbf58606520147cfa/tools/飞特/): FD 1.9.8.5 + CH340 sürücüsü, Windows |
| Multimetre | Gerilim ölçmek, kablo sırasını kontrol etmek için |
| Etiket kâğıdı + kalem | 7. adımda kullanılır |

### Adım 1 · Yazılımı kurma

```
1  URT-2'yi takın → Aygıt Yöneticisi'nde "Bağlantı Noktaları" altında USB-Enhanced-SERIAL CH343 (COMx) görünür, numarayı not edin
   URT-2'de CH343 var, Win10/11'in kendi sürücüsü yeterli, kurulum gerekmez. Görünmezse tools/飞特/CH340_URT.rar kurulur (eski URT-1 için)
2  tools/飞特/FD1.9.8.5(250729).7z dosyasını açın → doğrudan çalıştırılır, kurulum gerekmez
```

### Adım 2 · Havadan kablo bağlantısı

Bir servo kablosunu kesin; bir ucu 2.0 soket, diğer ucu üç çıplak tel kalsın. **Renge değil, pin numarasına bakın**:

```
Servo kablosu                URT-2
Pin 1  Signal / TTL    →    S     kartın arkasında beyaz portun S pininin lehim noktasına lehimlenir (geçici: tel ucu kalaylanıp beyaz portun S deliğine sokulur)
Pin 2  Vcc             →    V1    mavi bağlantı terminali
Pin 3  GND             →    G     mavi bağlantı terminali
```

- **Ortadaki tel mutlaka V'dir**; bu noktada Feetech ile Dynamixel aynıdır — V yanlış bağlanırsa servo yanar
- S ile G ters bağlanırsa **yanmaz**, yalnızca servo bulunamaz; yer değiştirmek yeterlidir
- Pin 1, sokette küçük bir üçgen ya da çentikle işaretlidir; servo gövdesinde soketin yanındaki serigrafiden de bakılabilir

### Adım 3 · Güç verme

**URT-2 üzerindeki DIP anahtar TTL sinyal seviyesi (3.3 / 5 V) seçicisidir, güç kaynağı değiştirici değildir.** 5 V'a alın (HD-1910 2–5 V kabul eder, pay geniştir).
USB takılıyken V1 terminalinde 5 V vardır (2026-09-12'de ölçüldü). 2026-09-17'de üretici belgelerine bakıldı: URT-2'de iki bağlantı terminali var; **V1, TTL veri yolunun harici güç girişidir, nominal DC 4.8–12 V**; V2 RS485 içindir, DC 12–24 V. URT-1 kılavuzundaki bağlantı fotoğrafında USB ve harici güç aynı anda bağlıdır. Spesifikasyon V1'e 12 V girmeye izin verdiğine göre V1 ile USB 5 V arasında doğrudan bağlantı olamaz, diyotla ayrılmış olmalı; yalnızca USB takılıyken 5 V, V1'e verilir. Dolayısıyla iki bağlantı şekli de olur:

| Ne kullanılır | Nasıl bağlanır | Ne zaman kullanılır |
|---|---|---|
| **USB 5 V** | Hiçbir şey bağlanmaz, V1'de kendiliğinden 5 V vardır | **ID atama, parametre değiştirme**. HD-1910 4 V'tan itibaren çalışır, yüksüz yeterlidir |
| Ayarlı anahtarlamalı güç kaynağı / pil → **V1 terminali** | + V1'e, − G'ye, servo kablosu doğrudan TTL-Bus portuna takılır. Üreticinin standart bağlantısı | 15 servo birlikte, tezgâh |
| Ayarlı anahtarlamalı güç kaynağı / pil → servo | + doğrudan servo V'ye, − servo G'ye **ve** URT-2'nin G'sine (ortak toprak), V1 boş bırakılır | Akımın URT-2'nin terminali ve izlerinden geçmesi istenmiyorsa (15 servo sıkışınca (stall) on küsur amper çekebilir, terminal 6 A olarak işaretli) |

⚠️ 8.4 V'u geçmeyin; bu HD-1910'un üst sınırıdır, URT-2'nin değil.

⚠️ **Güç verme sırası: önce USB'yi takın, sonra servoya güç verin.** Tersi olursa veri yolu 2.1 V'ta ezilir ve tek servo bile yanıt vermez; bkz. [Tuzaklar · Araçlar](14-tuzaklar.md).

**Tam dolu 8.4 V'luk pille sıkışma (stall) testi yapmayın** — bu HD-1910'un gerilim üst sınırıdır, sıfır paydır.

### Adım 4 · Servoyu arama

```
1  FD'de 1. adımda not edilen COM portunu seçin
2  Baud hızı 1000000
3  "Aç"a tıklayın
4  Yalnızca bir servo bağlayın (jumper kabloyla bağlanan)
5  "Ara"ya tıklayın → listede ID 1, model HD-1910 görünür
```

Bulunamazsa sırayla kontrol edin: sürücü kurulu mu → COM portu doğru mu → baud hızı 1000000 mü → S hattının teması iyi mi (geçici delik en şüphelisi) → S/G ters mi.

### Adım 5 · Parametreleri değiştirme

"Programlama" sayfasına (EPROM) geçin. **Her servoda yalnızca şu maddeler değiştirilir, diğerlerine dokunulmaz:**

| Parametre | Fabrika | Yeni değer | Neden |
|---|---|---|---|
| **ID** | 1 | **Aşağıdaki tabloya göre** | Resmi çalışma zamanı (runtime) eklemleri bu ID'ye göre bulur |
| **Aşırı akım koruması** | Kapalı | **Açık** | Montaj sonrası sıkışma (stall) sıradan bir şeydir, açılmazsa servo yanar |
| **Aşırı gerilim koruması** | Kapalı | **Açık** | 8.4 V tam dolu pil 4–10 V penceresinin içinde kalır, yanlış tetiklenmez |
| Aşırı ısınma koruması | Açık (80 ℃) | Dokunulmaz | — |
| Baud hızı | 1 Mbps | Dokunulmaz | Fabrika değeri resmi projenin istediğidir |
| Çalışma modu | Mod 4 saf konum PD | Dokunulmaz | Pekiştirmeli öğrenmenin sahaya aktarımında tam olarak gereken budur |
| Return delay | 0 | Dokunulmaz | STS serisinde bu madde etkisizdir |
| Orta konum | — | **Montajda kalibre edilir** | Makine tamamen monte edildikten sonra hata ayıklama paneliyle resmi katlama pozuna göre kalibre edilir (9. adımdan önceki "Büzülmüş durum kalibrasyon referansı olabilir mi" bölümüne bakın). FD'nin "orta konum kalibrasyonu" yalnızca mevcut konumu 2048 yapar, sadece bacaklar düzken kullanılabilir |

Değiştirdikten sonra "Kaydet"e tıklayın.

**ID eşleme tablosu** — yukarı akıştaki `duck-control/src/model.rs` dosyasından; yorumda değerlerin "donanım üzerinde ölçülerek bulunduğu" yazıyor:

| ID | Eklem | ID | Eklem | ID | Eklem |
|---|---|---|---|---|---|
| **10** | Sağ kalça yaw | **20** | Sol kalça yaw | **30** | Boyun pitch |
| **11** | Sağ kalça roll | **21** | Sol kalça roll | **31** | Kafa pitch |
| **12** | Sağ kalça pitch | **22** | Sol kalça pitch | **32** | Kafa yaw |
| **13** | Sağ diz | **23** | Sol diz | **33** | Kafa roll |
| **14** | Sağ ayak bileği | **24** | Sol ayak bileği | **34** | Ağız |

**Hatırlama yöntemi**: onlar basamağı = bölge (1 sağ bacak · 2 sol bacak · 3 boyun-kafa), birler basamağı = gövdeden uca sıra (0 kalça yaw → 4 ayak bileği).
ID 200, `imu_to_dxl` kartıdır, firmware içinde sabit yazılıdır, burada yapılandırılmaz.

> Bu makinenin geçici durumu (2026-09-28): eski ağız ID 34 servosu ID 21 yapıldı, kullanıcı FD'de orta konum kalibrasyonunun 2048'e yapıldığını onayladı; ağız konumu şimdilik boş. Yukarıdaki tablo hâlâ tasarım ID dağılımıdır; veri yolu yeniden devreye alınmadan önce gerçekte çevrimiçi olan ID'ler kontrol edilmeli, geçmişteki "15 servonun tamamı çevrimiçi" varsayımıyla doğrudan hareket başlatılmamalıdır.

### Adım 6 · Doğrulama

```
1  Gücü kesin (USB'yi çekin ya da güç kaynağını kapatın)
2  Yeniden güç verin
3  Yeniden "Ara"ya tıklayın → yeni ID görünürse yazılmış demektir
```

Bu adım atlanmasın; EPROM parametreleri ancak güç kesilip yeniden başlatılınca kesinleşir.

### Adım 7 · Etiket yapıştırma, sıradaki servo

Etikete **eklem adı + ID** yazın (ör. "sol diz 23"), yalnızca sayı yazmayın. 15 servo birbirinin aynısıdır.
Servoyu çıkarın, sonrakini takın, 4. adıma dönün. Bir servo yaklaşık iki dakika sürer.

### Adım 8 · Dönüşünü izleme (isteğe bağlı)

Servo bulunduktan sonra ana sayfada ona tıklayın, konum kaydırıcısını çekince servo da döner. USB 5 V ile yüksüz döner ama güçsüzdür; gerçek çalışma koşulu 7.4 V bağlandığında olur.

### 2026-09-17 · Veri yoluna ilk tam bağlantı, bir "büzülmüş" duruş kaydı

URT-2 + web hata ayıklama paneli (`tools/servo-web/`) ile monte edilmiş ördeğin 15 servosu ilk kez eksiksiz okundu: 0 zaman aşımı, 0 sağlama hatası, 7.2 V, 30–40 °C. Sıfır kalibrasyonundan sonra tork tamamen kapatıldı, ördek yatırıldı ve eklemlerin kendi ağırlığıyla sonuna kadar sarkması sağlandı; okunan değerler onun "büzülmüş" duruşudur ve `tools/servo-web/poses/缩起来-2026-09-17.json` dosyasına kaydedildi:

| ID | Eklem | Servo değeri | Sıfıra göre |
|---|---|---|---|
| 20 | left_hip_yaw | 2084 | +3.2° |
| 21 | left_hip_roll | 1997 | -4.5° |
| 22 | left_hip_pitch | 772 | -112.1° |
| 23 | left_knee | 1058 | -87.0° |
| 24 | left_ankle | 2247 | +17.5° |
| 30 | neck_pitch | 1473 | -50.5° |
| 31 | head_pitch | 1094 | -83.8° |
| 32 | head_yaw | 2059 | +1.0° |
| 33 | head_roll | 2012 | -3.2° |
| 34 | mouth | 2047 | -0.1° |
| 10 | right_hip_yaw | 2018 | -2.6° |
| 11 | right_hip_roll | 2109 | +5.4° |
| 12 | right_hip_pitch | 3195 | +100.8° |
| 13 | right_knee | 3032 | +86.5° |
| 14 | right_ankle | 1782 | -23.4° |

İki şey görülüyor: sol ve sağ bacağın kalça pitch ve dizleri birbirinin aynasıdır (sol −112° / −87°, sağ +101° / +87°), bu MJCF'teki sol-sağ bacak pozitif yön zıtlığı kuralıyla uyumludur; boyun −50°, kafa −84° ise başın göğse düştüğünü gösterir. Bu veri seti ileride "toplanma duruşu" olarak doğrudan gönderilebilir.

### 2026-09-18 · Büzülmüşten ayakta duruşa nasıl hareket edilir (resmi modelin ileri kinematiği)

`tools/servo-web/model/model.json` (ince ayarlı resmi MJCF) ile ileri kinematik hesaplandı; koşullar: taban ön-arka eğilmez, taban noktasının ön-arka konumu resmi ayakta duruşla aynıdır. Sonuç bir doğru: **kalça = −26° + diz/2, ayak bileği = +26° + diz/2** (sol bacak; sağ bacakta hepsinin işareti ters, model kuralı). Bacaklar çok kısa (uyluk 42 mm, baldır 49 mm); diz +60° bükülse bile gövde yalnızca 3 cm alçalır.

| Diz (model kuralı) | Kalça | Ayak bileği | Gövde ayakta duruşa göre |
|---|---|---|---|
| −60° | −56° | −4° | 10 mm yüksek |
| 0° | −26° | +26° | 0 (resmi ayakta duruş) |
| +30° | −10° | +40° | 16 mm alçak |
| +60° | +6° | +54° | 33 mm alçak |

**Ağırlık merkezi (resmi robot_walk.xml kütleleri ile)**: tüm makine 744 g; ayak tabanı, ayak site'ından ileri 34 mm, geri 20 mm. Ayakta duruşta ağırlık merkezinin izdüşümü ayak parmak ucuna 34 mm, topuğa 20 mm uzaklıkta; yarım çömelmeden (diz +60) ayakta duruşa kadar tüm yolda pay 17 mm'nin üzerinde; kafa ve boyun her 10° için ağırlık merkezini yalnızca 2.4 mm kaydırır; kalça her 5° daha fazla öne eğildiğinde (ayak düz kalsın diye ayak bileği ters yönde 5°) ayak öne kayar, parmak ucu payı +5 mm artar. Modele göre yavaş kalkışta öne devrilmemesi gerekir; gerçek makine devrilirse önce sıfır sapmalarına (sağ kalça 27°, sol ayak bileği 28°) ve pilin takılıp takılmadığına bakılmalı. Sayfadaki 3D görünümde artık ağırlık merkezi izdüşümü (yeşil nokta + kesikli çizgi) ve iki ayağın destek bölgesi gerçek zamanlı çiziliyor; destek bölgesinden çıkınca kırmızıya dönüyor, sağ alt köşe dört yöndeki payı bildiriyor.

**Gerçek makinede yönü modelden farklı olan eklemler sayfadaki ± ile çevrilmelidir**: 2026-09-18'de büzülmüş duruş fotoğrafıyla karşılaştırıldı; diz (23, 13), boyun pitch (30), kafa pitch (31) ters çıktı, ayak bileği doğrulanacak. Dizi dosyasında model kuralındaki göreli açılar yazılıdır, sayfa göndermeden önce ± ile dönüştürür.

Büzülmüşten (kalça −112 / diz −87 / ayak bileği +17) ayağa kalkma sırası, sayfada "ayağa kalk" dizisi (`poses/站起来-序列.json`) olarak hazırlandı:

1. Kafayı kaldır 1 s: boyun, kafa pitch +20°'ye. Kafa tüm makinenin ağırlığının üçte biridir; gövde henüz masada otururken ayakta duruş konumuna getirilir.
2. Bacakları aç, ayakları düzle 3 s: gerçek makinenin ayakta duruşu referans alınarak diz +60 / kalça +30 / ayak bileği +30 (model kuralı, sol bacak; sağ bacak ters işaret). Ayak arkadan gövdenin altına dönüp masaya basar, gövde yaklaşık 9 cm yukarı itilir; en kritik adım budur, ilk seferde elle destekleyin.
3. Dikleş 2 s: ayak düz çizgisi boyunca resmi ayakta duruşa gidilir. Üç açı aynı anda doğrusal değişir, ayak boyunca düz kalır, boy yalnızca 10 mm artar.

Sayfaya "geçiş süresi" eklendi: tüm duruşlar, ayakta duruş ve sıfıra dönüş mevcut gerçek konumdan doğrusal geçişle yapılır, 20 Hz senkron yazma ile gönderilir, artık bir anda sıçranmaz. Ön koşul servo yönlerinin modelle aynı olmasıdır (madde 8 doğrulanacak); önce tek servoda deneyin: 22 numaralı servo negatif yönde dönünce uyluk öne kalkıyor mu.

### 2026-09-22 · Büzülmüş duruş kalibrasyon referansı olabilir mi (resmi modelde kesin örgü kesişimi)

Gruptaki tartışma: resmi sıfır bacakların düz olduğu konumdur, havada elle ayarlarken referans noktası olmadığı için bir iki derece sapmayla ördek düşer; büzülmüş duruş referans yapılabilir mi? Resmi model kullanılarak her bacak eklemi katlanma yönünde parçalar çarpışana kadar döndürüldü (fcl kesin örgü, dışbükey zarf kullanılmadı, [`tools/fold_contact`](../tools/fold_contact/)):

- Eklemi durduran **hep ayak ve ayak bileğidir**, eklemin kendi sınırı değil; yani nerede durduğu diğer eklemlere bağlıdır: diz, kalça 0° iken 70.7°'de, kalça 90° iken 89.6°'de çarpışır
- **Ayak bileği büzülmüş durumda sabitlenmiyor**, diz ve kalça sonuna kadar katlandıktan sonra hâlâ yaklaşık 20° oynayabiliyor; büzülmüş durumda ayak bileği kalibre edilemez
- Resmi FOLD'un (kalça, diz ±90°) dizi neredeyse temas noktasıdır; 1.57 rad (89.95°) ayak bileğinin uyluk servosuna yaklaşık 0.36° girmesine neden olur (temas 89.59°'de); 9/20'de kaydedilen "büzülmüş" sol diz dönüşümü yaklaşık 88°, bu temas noktasıyla örtüşüyor
- FOLD'un boyun / kafa pitch değeri 57°'dir, **temas noktası değildir**: bacaklar katlandıktan sonra boyun servosunun gövde kabuğuna değmesi için boynun 66.6°'ye dönmesi gerekir, 57° öncesi ve sonrası boşluk vardır
- Bu XL330 orijinal geometrisidir, Feetech sürümünde 8 parça değiştirildi; Feetech sürümü modelle yeniden hesaplanmalı ya da SolidWorks'te ölçülmelidir

Analiz sonucu: büzülmüş duruş yalnızca kalça ve diz için referans olabilir ve duruş biçimi sabit yazılmalıdır. Sıfır noktası hâlâ resmi 2048'dir, resmi kod ve politika için telafi eklemeye gerek yoktur — büzülmüş duruş yalnızca referans noktasıdır, yeni sıfır değildir.

**Sonunda karara bağlanan yöntem** (hata ayıklama paneli 0.14.0'dan itibaren "resmi katlama (kafa-boyun düzeltilmiş)" referansı, 0.15.0'da incelemeye göre düzeltildi):

- Bacaklar resmi FOLD'a göre konumlanır: diz, ayak bileği uyluk servosuna yeni değecek kadar katlanır (parçalar dayanır, her seferinde aynıdır), kalça pitch gönye (dik açı cetveli) ile gövdeye dik konumlanır, kalça yaw / roll, ayak bileği 0°
- Kafa-boyun resmi FOLD'un 57°'sine göre konumlandırılmaz (temas noktası değil, gözle ayarlanamaz); düzeltilmiş konumlandırılır: boyun dik, kafa karşıya bakar, ağız kapalı
- **15 servo birlikte kalibre edilir**, tork kapalıyken elle konumlandırılır. Hedef: ± hepsi −1 iken 22 / 23 = 1025, 12 / 13 = 3071, geri kalanı 2048; servonun EEPROM'una yazılır (0x0B'ye hedef değerle = "mevcut konum bu okumadır"), sıfır noktası yine resmi 2048'dir
- Diz resmi 1.57 rad'a göre hesaplanır, gerçekte temas noktası olan 89.59°'ye konumlanır, sıfır farkı yaklaşık 0.36° (4 adım), göz ardı edilir
- Onay kutusu servo servo "şimdi → yazılacak, kaç derece fark" listeler; fark 30°'nin üzerindeyse bir kez daha onay ister, ama **engellemez**: servo kolu takılırken yarım tur dönmüşse 180° fark olur, kalibrasyon bunu tam düzeltir; yön ± ters ayarlıysa da yaklaşık 180° fark çıkar ve o zaman kalibre etmek yanlış olur, önce elle oynatıp 3D'de dönüş yönüne bakarak ± doğrulanmalı
- Kalibrasyondan sonra tork yine kapalı kalır, elle açıp sonra tork açmak sıçratmaz (0.15.0'dan itibaren tork açmadan önce hedef mevcut konuma hizalanır)

### Adım 9 · Montaj, sıfırlama, hareket aralığı denemesi

**Sıfır noktası nedir**: robotun **dik ayakta** durduğu duruştur — bacaklar düz sütun, ayaklar yatay, boyun dik, kafa karşıya bakıyor. MJCF'teki tüm eklemlerin = 0 olduğu konumdur ve servo **2048**'e karşılık gelir.

**Ayakta duruş sıfır noktası değildir.** Resmi ayakta duruş (`DEFAULT_POSITION`) sıfır noktasına eklenen ofsettir: kalça pitch ±26°, ayak bileği ∓26°, boyun ve kafa pitch +20°. Bu yazılımın işidir, **ayakta duruşu 2048 olarak kalibre etmeyin**.

**Her eklem için yöntem**:

```
1  Servoyu önce FD'de 2048'e çevirin, sonra servo kolunu takın (kolun diş konumu tam oturmazsa en yakınını alın, hata sonraki adıma kalır)
2  Eklemi "düz" konuma getirin, elle destekleyin
3  FD programlama sayfası → "orta konum kalibrasyonu" → mevcut konum 2048 olarak tanımlanır (ya da `tools/servo-web/` web hata ayıklama panelindeki "orta konum kalibrasyonu" düğmesi; monte edildikten sonra elle düzleştirip tıklanır, aynı komuttur)
4  Vidayı sıkın
5  FD'de 2048'den aşağıdaki tablonun alt ve üst sınırlarına yavaşça çekin, yapı parçalarının çarpıp çarpmadığına, kabloların gerilip gerilmediğine bakın
6  Çarparsa o servonun gerçek açısını not edin — yazılım sınırından küçük olması normaldir, bu makinenin gerçek hareket aralığı odur
```

**Hareket aralığı tablosu** — MJCF `robot_walk.xml` içindeki `range` değerlerinden; bunlar **yazılım sınırlarıdır**, mekanik olarak ulaşılıp ulaşılamayacağı denenmelidir. HD-1910 4096 adım / 360°'dir, 1° ≈ 11.4 adım:

| ID | Eklem | Aralık | Servo değeri (2048 sıfır) |
|---|---|---|---|
| 10 / 20 | Kalça yaw | Sağ −30 ~ +25°　Sol −25 ~ +30° | Sağ 1707 ~ 2332　Sol 1764 ~ 2389 |
| 11 / 21 | Kalça roll | ±22° | 1798 ~ 2298 |
| 12 / 22 | Kalça pitch | ±90° | 1024 ~ 3072 |
| 13 / 23 | Diz | ±90° | 1024 ~ 3072 |
| 14 / 24 | Ayak bileği | ±90° | 1024 ~ 3072 |
| 30 | Boyun pitch | −90 ~ +60° | 1024 ~ 2731 |
| 31 | Kafa pitch | ±90° | 1024 ~ 3072 |
| 32 | Kafa yaw | ±170° | 114 ~ 3982 |
| 33 | Kafa roll | ±25° | 1764 ~ 2332 |
| 34 | Ağız | −5° (kapalı) ~ +30° (açık) | 1991 ~ 2389 |

Kalça yaw'ın sol-sağ asimetrisi aynalamadır — iki bacak dışa 30°, içe 25° döner. Ağız MJCF'te yoktur (politika onu kontrol etmez), aralığı `model.rs` içindeki `MOUTH_CLOSED / MOUTH_OPEN` değerlerinden gelir.

⚠️ **Artı ve eksi yönün hangi tarafa olduğu servonun takılma yönüne bağlıdır**; resmi çalışma zamanında her servonun bir yönü ve ofseti vardır (`motor.rs`, yorumda "donanım üzerinde ölçülerek bulundu" yazıyor). Girişimi (çarpmayı) denerken iki yönü de sonuna kadar çekmek yeterlidir, işaretle ilgilenmeye gerek yok.

---

---

## HAT basmadan · Ana karta jumper kabloyla bağlantı

**Ayrı bir belge oldu → [HAT basmadan kurulum](08-hat-olmadan-kurulum.md)**. Birçok kişi HAT'ın baskı (prototip üretim) maliyetini çok pahalı buluyor; o belge alternatif çözümdür: ¥70'lik modül, adım adım bağlantı, hangi adımda bir şeyin yanabileceği.
Burada yalnızca uygulama sırasında olanlar kaydedilir.

---

## 2026-09-10 · Servolar ve test kartı geldi

**Ne geldi**: 15 HD-1910-C001, bir FE-URT-2 test kartı (USB-C, hem TTL hem RS485 portu var).

**İlk sorun**: Servoların orijinal kablosu **2.0 mm 3P** (şartnamede AMP2.0-3P yazıyor); test kartının solundaki iki beyaz TTL portu **bundan büyük, takılmıyor**. Kartta 2.0'lik port verilmemiş.

**Ne yapılır**: "Servo dönüştürücü kablo 2.0'dan 2.5 3P'ye" satın alınır. Kablo beklenirken iş görmek için iki kablo kesilip uç uca lehimlenir.
`imu_to_dxl` kartının J4/J5'i PH 2.0 mm'dir, servo kablosuyla uyumludur, **etkilenmez** — yalnızca bu test kartının portu uyumsuzdur.

**Sıradaki adım**: Dönüştürücü kablo gelince tek tek ID atanır. **Bir seferde yalnızca bir servo bağlanır** (fabrika ID'leri hep 1), değiştirildikten sonra etiket yapıştırılır.
Bu arada her servonun aşırı akım ve aşırı gerilim korumaları açılır (fabrika varsayılanı kapalı). Baud hızı ve çalışma modu fabrikadan doğru gelir, dokunulmaz.
Adımlar ve ID tablosu yukarıdaki [Servo yapılandırması · Parçalar gelince adım adım](#servo-yapılandırması--parçalar-gelince-adım-adım) bölümünde.

---

## 2026-09-12 · Parçalar tamam, ana kartın pin başlığı lehimlendi, servolar mekanik parçalara takılmaya başlandı

**Ne geldi**: Radxa Zero 3W (2 GB çıplak kart), ToF, pil, pil yuvası, microSD, pin başlık, kamera. 09-10'daki servo ve test kartıyla birlikte, **`imu_to_dxl` kartı (JLCPCB hâlâ üretiyor) ve havadan kablo modülleri (düşürücü, dönüştürücü kart, dönüştürücü kablo) dışında her şey tamam**.

**Neler yapıldı**:
- 2×20 pin başlık Radxa'ya lehimlendi
- Feetech HD-1910'ları mekanik parçalara takmaya başlandı

**Fark edilen sorun**: **HD-1910 orijinal XL330'dan yapısal olarak farklı** (bacağı bastıran bir noktada). Çalışma arkadaşı yapı parçalarını değiştirip yeniden bastı, değişiklikten sonra takılabiliyor.
Hangi parça, neresi, ne kadar değişti — *eklenecek* (fotoğraf çekilip ölçülerek [Yapım günlüğü](16-yapim-gunlugu.md)'ne yazılacak; ayrıca [Aktüatör seçimi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/执行器选型.md) belgesindeki HD-1910 bölümüne "mekanik olarak doğrudan yedek değildir, parça değişikliği gerekir" notu eklenecek).

**Algoritma tarafı eğitim öncesi veri toplama listesi gönderdi** → doldurulmuş hali [docs/HD-1910训练前数据清单.md](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD-1910训练前数据清单.md) içinde; depoda bulunanların hepsi dolduruldu, tezgâh kalemlerinde nasıl ölçüleceği işaretlendi.

**Sıradaki adımlar**:
- Servoların takılmasına devam, bir bacak bitince hareket aralığını bir kez ölç
- ID atama — dönüştürücü kablo henüz gelmedi, önce [yukarıdaki 2. adıma](#adım-2--havadan-kablo-bağlantısı) göre bir servo kablosu kesilip havadan bağlanır. **Bugün bunu yapın**
  - ✅ Kablo havadan bağlandı, DIP anahtar USB tarafına alındı, G–V1 arasında 5 V ölçüldü
  - ✅ Bilgisayara takılınca **COM5** çıktı, çip **CH343** (CH340 değil), Win'in kendi sürücüsü doğrudan tanıyor — kılavuzda 1. adım düzeltildi
- Ana karta imaj yazma — **kart okuyucu yok, yapılamaz**. Kart microSD, kartın kendisi okuyucu olarak kullanılamaz; dizüstünde SD yuvası yoksa bir tane (USB 3.0) alınmalı. Gelince [HAT basmadan · 1. adım](08-hat-olmadan-kurulum.md) uyarınca ilk güç verilir

---

## 2026-09-13 · 15 servonun tamamı ID aldı, hepsi takıldı, tezgâh çalışması başlıyor

**Neler yapıldı**: 15 HD-1910'un tamamına ID atandı, aşırı akım ve aşırı gerilim korumaları açıldı, gövdeye takıldı.

**Tezgâh bağlantısı** (düşürücü modül kullanılmadı, Radxa için şarj adaptörü):
- Ayarlı güç kaynağı 7.4 V, 2 A sınırlı → **doğrudan servo veri yolu V/G'ye**, URT-2'nin G'si de güç kaynağının eksi ucuna ortak toprak olarak bağlı, **V1 terminali boş**
- URT-2 DIP anahtarı = sinyal seviyesi, 5 V'a alındı (önceden yazılan "harici taraf" yanlıştı, o kartta güç değiştirme yok)
- URT-2 USB-C → Radxa **host** portu (güç portu değil)
- Radxa güç portu → 5V/2A şarj adaptörü (**bilgisayarın USB'sini kullanmayın, 500 mA yetmez**)

**Sıradaki adım**: `dmesg` ile CH343'ün `ttyACM0` verip vermediğine bak → Python ile ID 10–34'ü tara → 15 servo da yanıt veriyor → resmi çalışma zamanı.

---

## 2026-09-16 · Ana kart güç aldı, kart yazıldı

**Neler yapıldı**:
- Radxa Zero 3W çıplak kart güç aldı, normal. Pin başlık 2.54 mm, DXF'teki delik aralığıyla örtüşüyor (iki sıra y = 25.41 / 27.95 mm).
- Kart okuyucu ve 5 V düşürücü modül geldi.
- Armbian 26.8.1 trixie minimal yazıldı (sha256 doğrulandı). Rufus taşınabilir sürüm, `.img.xz` tanıyor, 2 dakikada yazıldı. Ekran görüntüleri [`assets/flash/`](https://github.com/fanhao375/microduck-replica/tree/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/flash/) içinde, adımlar [HAT basmadan · 1. adım](08-hat-olmadan-kurulum.md) bölümüne yazıldı.

**Karşılaşılan tuzak**: `wsl --mount` ile yazılmış karta `.not_logged_in_yet` dosyasını koymaya çalışıldı, `ERROR_FILE_NOT_FOUND` hatası verdi, WSL USB kart okuyucuyu bağlayamıyor. **Önce ön ayarı imaja koyup sonra yazma** yöntemine geçildi, betik [`tools/radxa/`](../tools/radxa/) içinde, yönetici hakkı gerekmiyor. [Tuzaklar](14-tuzaklar.md) belgesine kaydedildi.

**Radxa kaynakları**: Şema / ürün özeti / 2D DXF / 3D STP / bileşen yerleşim şeması indirildi, yerelde `Radxa-Zero3W/`. **PCB kaynak dosyası yok**, yerleşim şemasında ve DXF'te pin 1 işaretlenmemiş. Pin 1'i tanımak için multimetre kullanılır: OTG portundan güç verilince pin başlığın dört köşesi ölçülür, 3.3 V olan pin 1'dir, yanındaki 5 V olan pin 2'dir.

**Sıradaki adım**: Kartı takıp aç → yönlendiricide `radxa-zero3`'ü bul → `ssh duck@IP` → URT-2'yi takıp `dmesg`'e bak.

---

## 2026-09-16 ～ 17 · Ana kart açıldı, dokuz kart

**Sonuç**: Armbian 26.2.1 vendor kartta çalıştı, WiFi otomatik bağlandı, ssh girilebiliyor, `/dev/ttyS2` çıktı, bilgisayara takılınca bir USB seri port daha görünüyor, Pollen'in resmi üç betiği çalıştı, daemon 0.13.0 kuruldu. Kart hazırlamanın tek komuta indirilmiş hali [`tools/radxa/`](../tools/radxa/) içinde.

**Süreç** (zamana göre):
- 09-16 akşam: Rufus ile Armbian 26.8.1 yazıldı, WiFi ön ayarı imaja konuldu. Açılışta LED çift yanıp sönüyor, yerel ağda görünmüyor. WiFi sanıldı: yönlendirici WPA3 karma, AIC8800 GCMP-256'yı desteklemiyor, 5G bandı, iki sürücü birbirine giriyor; sürüm sürüm değiştirildi, dört kez yazıldı, hiçbiri olmadı.
- USB seri yolu da denendi: `g_serial` + `dwc3-peripheral`, bilgisayar aygıtı görmüyor.
- Kart okuma: kartın kök bölümü kopyalanıp bağlanarak bakıldı, **kök bölümüne tek bayt bile yazılmamış**, ilk açılış işareti hâlâ duruyor, bölüm genişletilmemiş. Yani çekirdek kalp atışını başlatmış ama sistem diskini hiç bağlamamış. Daha önceki WiFi için yapılan dört sürüm boşunaymış, sorun çok daha öncesindeymiş.
- Taban 26.2.1'e (resmi belirtilen sürüm) alındı, SDR104 kaldırıldı, olmadı. "Kara kutu" initramfs yapıldı (initramfs'ye girince LED söner, disk bulunursa sürekli yanar, başarısızsa hızlı yanıp söner, çekirdek günlüğü kartın bölüm dışı alanına yazılır); sonuç LED hep çift yanıp sönüyor, initramfs'ye bile girilemiyor.
- 09-17 gece yarısı: Radxa resmi imajı (b1, 2025-07) yazıldı, aynı kart aynı ana kart, iki dakikada WiFi'ye bağlandı. ssh ile girip bakıldı: SD kart SDR104 ile normal çalışıyor, WiFi AIC8800D80/DS2, aygıt ağacı Armbian'ınkiyle madde madde karşılaştırıldı, neredeyse aynı. Kart, SD kart, güç, aygıt ağacı hepsi elendi.
- Önyükleyiciler karşılaştırıldı: Armbian ana hat U-Boot 2025.10 + DDR firmware v1.21 (2024-01) kullanıyor, Radxa rk U-Boot 2017.09-51 + DDR v1.23 (2024-09) + BL31 v1.45. Kart 2024-11 tarihli V1.12.
- Radxa imajının 64～32767 sektörleri (idbloader + u-boot.itb) Armbian kartının üzerine yazıldı ve bir `/boot/extlinux/extlinux.conf` eklendi, **dokuzuncu kart açıldı**. LED: çift yanıp sönme → söner → sürekli yanar, yerel ağda `192.168.0.102`, bilgisayarda COM5 göründü.
- Sonra resmi `install-by-hand.md`'ye göre: extlinux'a `uart2-m0` + `dwc3-peripheral` takıldı, konsol tty1'e bırakıldı, ttyS2/ttyFIQ0 getty'leri mask edildi; WiFi Armbian'ın standart netplan yazımına çevrildi; `setup-board.sh` (aic3x codec DKMS, ONNX Runtime 1.28, ToF udev kuralı) → `migrate-network.sh` (NetworkManager) → yeniden başlatma → her biri bir kez daha → `install.sh` (daemon 0.13.0). Ana kart GitHub'ı bilgisayarın Clash vekil sunucusu üzerinden indirdi.

**Karşılaşılan tuzaklar** [Tuzaklar](14-tuzaklar.md) belgesine girdi: önyükleyici, GCMP-256, dwc3-peripheral, GitHub vekil sunucusu, ilk açılış ön ayarında eksik değişken.

**Sıradaki adım**: 4. adım, servo veri yolunu ana karta bağlama (URT-2 USB üzerinden ya da pin 8/10'a jumper kabloyla `/dev/ttyS2` kullanılır), `robotctl health` ile 15 servoya bak.

**Gövde IMU için iki yol** (2026-09-17'de belirlendi ve paralel yürütülüyor):

| | A · `imu_to_dxl` küçük kart | B · GY-BNO085 modülü doğrudan ana karta |
|---|---|---|
| Donanım | Kendi çizimimiz, geldi, 3.3 V normal, konnektör ayak izi düzeltilecek | ¥66 hazır modül, I2C ile 40 pin'in pin 3/5'ine (ToF ile aynı i2c3 hattı), 3.3 V pin 1'den |
| Yazılım tarafında yapılacak | STM32 firmware: ID 200 register protokolü + IMU füzyonu, **şu an açık firmware yok, sıfırdan yazılacak** | robotd'ye bir I2C IMU kaynağı (Rust) eklenecek, BNO085 çip üzerinde füzyon yapıp doğrudan kuaterniyon verir |
| Resmi çalışma zamanına göre | Protokol uyumlu, robotd değişmez | robotd'nin IMU arka ucu (backend) değişir |
| Ortak yapılacak | Feetech servo protokolü portu (robotd Dynamixel konuşuyor) | Aynı |

Prototip dönemi (Raspberry Pi Zero 2 W sürümü) I2C ile BNO055 kullanıyordu, B yolunun öncüsü var. Önce bir tane alın, `i2cdetect -y 3` ile 0x4A görünür ve Python'la kuaterniyon okunursa tamamdır.

---

## 2026-09-28 · HAT geldi, ID 21 değiştirildi, kamera sonunda görüntü verdi

**Servo**: Kullanıcı eski ağız ID 34 servosunu ID 21 yaptı, bozuk eski 21'in yerine koydu ve FD ile 2048 orta konum kalibrasyonunu tamamladı. Bu kalem kullanıcı onayına dayanır; bu turdaki ana kart/kamera kontrollerinde servo register'ları yeniden okunmadı ve herhangi bir hareket çalıştırılmadı. Ağız şimdilik yok, tasarım ID tablosu değişmedi.

**Ana kart ve güç**: HAT ana karta takıldı, kullanıcı ayarlı güç kaynağından HAT'a 7.4V verdi ve madde madde kontrole başladı. HAT'ın düşürücü çıkışı ana karta 5V verir; ana kart ağa bağlandıktan sonra Wi-Fi / SSH ile hata ayıklanır. Ana kartın `5V IN / USB_OTG` girişi hem güç hem gadget işlevi görür, USB 3.0 Host'tur; HAT güç verirken ikinci bir 5V yolu getirmemek için bilgisayara sıradan USB veri kablosu aynı anda bağlanmamalıdır. Burada bağlantı şekli ve hata ayıklama ilerlemesi kaydedilmiştir; yük, gerilim dalgalanması (ripple), ses ya da servo veri yolunun kabul edildiği anlamına gelmez.

**Kamera süreci**:

1. Orijinal Armbian'da kamera yanıt vermedi, IMX219 register okuması hata verdi, medya topolojisinde sensör varlığı (entity) yoktu.
2. Karşılaştırma için Radxa resmi Bookworm KDE B1 yazıldı; imaja yalnızca bu makinenin Wi-Fi / SSH ayarı önceden konuldu, çekirdek, sürücü ve sistem içeriği orijinal bırakıldı. Açıldıktan sonra resmi `rsetup` ile `radxa-zero3-radxa-camera-8m.dtbo` etkinleştirilip yeniden başlatıldı.
3. Resmi sistemde başlangıçta yine `Error -5` yeniden üretildi; yalnızca `/dev/video0` var diye kameranın normal olduğuna hükmedilemez. Yeşil ışığın çift yanıp sönmesi bu sistemdeki `heartbeat`'tir, açılış başarısızlığı kanıtı değildir.
4. Kullanıcı flat kablonun ön-arka yüzünü kontrol edip ayarladı ve yeniden güç verdi; `Model ID 0x0219` başarıyla okundu, `imx219` sürücüsü bağlandı, medya zinciri eksiksiz.
5. GStreamer ile sınırlı 40 kare yakalandı, yaklaşık 4.05 saniye sonra normal EOS, çıkış kodu 0; son kare gerçekten incelendi, 1920×1080 JPEG içinde tavan, lamba ve monitör görülüyor.

Bağlantı referans görseli, eksiksiz yeniden test komutları, sürümler ve kanıtlar için **[Kamera hata ayıklama kaydı](../tools/radxa/摄像头调试记录-20260928.md)**; kısa hatırlatma için **[Tuzaklar](14-tuzaklar.md)** (Ana kart / HAT / kamera bölümü).

**Sonraki sıra**: Kullanıcı orijinal proje Armbian'ına dönmeye karar verdi; başarılı bağlantı şekli korunarak önce tanıma ve kare yakalama yeniden denenecek, sonra proje çalışma ortamı geri yüklenecek, kalıcı video test edilecek, ardından HAT çevre birimleri ve servo veri yolu tek tek doğrulanacak. Daha önceki Wi-Fi'li 09-20 temel imajı salt okunur dosya sistemi kontrolünden geçti; bu turun sonunda normal kapatma yapıldı, gücün kesilip kartın alınarak yazılması bekleniyor. Bu imaj resmi kartı yazmadan önceki tam çalışır kart yedeği değildir; kamera etkinleştirmesi ve proje yazılımı geri yüklenmelidir. Orijinal Armbian doğru bağlantıyla yeniden denenmedi; kameranın görüntü vermesi tüm makinenin, HAT güç yolunun ya da yürümenin kabul edildiği anlamına gelmez. Daha önce önerilen "HAT'ı sök, ana kartı yalnızca USB ile besle" işleminin gerçekten yapılıp yapılmadığı doğrulanmadı, tamamlanmış test sayılmaz.

## 2026-10-11 · kissqy'nin walk modelini kendi çalıştırıcımla (runner) koşturmak

**Neden böyle yapıldı**: kissqy'nin R17 dağıtım paketi resmi 0.15.1 sisteminin üzerine biniyor, yalnızca servo veri yoluna bağlı IMU'yu tanıyor (ID 200, kimlik `06 00 00 00 F2`), kodda I²C yolu yok; bizim makine BNO085'i ana kartın I²C'sine bağlı kullanıyor, kartta resmi çalıştırma programı da yok. Bu yüzden model onunki, çalıştırma programı ise 10-04'te Luwu'yu koşturan program; yeni bir `kissqy_walk` yapılandırması eklendi, yürütme parametreleri onun robotd uygulamasına göre.

**Sonuç**: Gövde elle taşınırken yalnızca poz değişiyor, adım atılmıyor; yere bırakılıp desteksiz bırakıldığında 0.4 saniye içinde iki bacak dönüşümlü hareket etmeye başlıyor. Birkaç kez ortada durdu, tüm vücut gücü kesildi; hepsi çalıştırıcının korumasından kaynaklandı (6.6 V düşük gerilim hattı, durduktan sonra 1° tutma kararı), düzeltildi. Güç kaynağı yaklaşık 8.0 V'a ayarlandıktan sonra 0.15 m/s, P5 tam 10 saniye koştu ve normal biçimde ayakta duruşa döndü: ilk 3 saniye ileri geri sallanma, sonra yarım çömelmiş halde hareketsiz, kesintisiz bir yürüyüş (gait) henüz elde edilemedi. P10'da akım çok büyük oldu, ayarlı güç kaynağı gerilimi 5.4 V'a çöktü.

**İkinci yarı**: Ana kartın aşırı ısınıp frekans düşürdüğü fark edildi (84–87°C, CPU 408 MHz'e kilitli, web hizmeti kalıcı olarak bir çekirdeği dolduruyor), kontrol periyodu 25 ms'ye uzadı; web hizmeti durdurulunca 20 ms'ye döndü. Tempo doğru, hareket tam olduğunda ayarlı güç kaynağı yine 4.6 V'a çekildi, yumuşak başlangıç eklendi. Eklem yönleri tek tek kontrol edildi, hepsi doğru, 15 servonun parametreleri tutarlı. En iyi koşul (20 ms, 1.8 GHz, en düşük 7.6 V) bile yalnızca poz değiştirdi, kesintisiz adım atmadı. **kissqy'nin Rust çalıştırma programına geçmeye karar verildi**; ona "IMU ana kartın I²C'sine bağlı" bağlantı şekli (B planı) eklenecek, yerleşik veri yolu küçük kartı (A planı) korunuyor.

**Aynı gece karşılaşılanlar**: Bilgisayarda Clash TUN açıkken ana karta bağlanılamadı; ana kart açıldıktan iki dakika sonra bir kez kilitlendi (yeşil ışık sürekli yanık), sebebi belirlenemedi.

Tur tur veriler, her parametrenin anlamı, kendi başına nasıl koşturulacağı için bkz. **[2026-10-11 kissqy gerçek robot deneyi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261011-kissqy-walk上机实测.md)**; sonuç [Tuzaklar](14-tuzaklar.md) belgesinin "Politika eğitimi ve gerçek robota aktarım" bölümüne eklendi.

## 2026-10-12 · İlk makine kissqy'nin tam setine geçti: resmi 0.15.1 + R17 + I²C IMU

**Neden böyle yapıldı**: 10-11'de kendi Python çalıştırıcımla yapılan eleme sonunda geriye kalan fark tamamen çalışma katmanındaydı. kissqy grupta kendi tam setiyle çok akıcı yürüdüğünü gösterdi; karar verildikten sonra robotta kendi setimiz kurulmayacak, doğrudan onunki kullanılacak, yalnızca onda eksik olan "IMU ana kartın I²C'sine bağlı" kısmı eklenecek (yerel dal `hd1910-trunk-imu-i2c`).

**Neler yapıldı**: Eski kart yeniden yazılmadı (resmi program hiç kurulmamıştı, IMU'nun kullandığı `i2c4-m0` overlay'i zaten vardı), `/home/duck` yedeklenip uzaktan kurulum yapıldı. Resmi `install.sh` yalnızca en son sürümü (0.16.1) kuruyor; yerel dosya kullanılarak `daemon-v0.15.1` sabitlendi ve otomatik yükseltme kapatıldı. `setup-board.sh`'nin ses kısmı (çekirdeği değiştirir) ve `migrate-network.sh` çalıştırılmadı. Önce kissqy'nin orijinal R17'si temel olarak kuruldu: `alsactl store aic3104` adımında takıldı (HAT üzerindeki ses çipi etkinleştirilmemiş, sistemde bu ses kartı yok, dal düzeltti), kurulduktan sonra "ID 200 yanıt vermiyor" hatası verdi (yalnızca veri yolu IMU'sunu tanıyor), ayrıca onun örnek makinesinin sıfır konumlarını bu makinenin kalibrasyonu olarak kopyaladı. Sonra bizim paket konuldu, `[trunk_imu] source = "bno08x"` ayarlandı.

**Sonuç**: BNO085 gerçek robotta okundu (firmware 2.6.6), 15 servo 50 Hz'de tamamen yanıt verdi, yaklaşık %1.7 periyotta IMU verisi eskimiş (tek kare, kontrol döngüsü bir önceki kareyi kullanabiliyor). Kalibrasyon bizim sıfır 2048, yön −1 olarak değiştirildi. Ördek servo-web ile HOME'a kaldırıldıktan sonra IMU ölçüldü: ayakta dikeyden 4.95°, öne eğim 16.2°, yön tam öne göre 3.9° sapmış, varsayılan montaj yönü doğru. Hareket moduna geçildikten sonra önce güç kesilip sonra HOME, 2 saniyede resmi ayakta duruşa kalkıldı; model devralıp yerinde 10 saniye tuttu, gövde eğimi 6.6°'den 3.3°'ye indi, hata yok.

**Takıldığımız yer**: Ana kart aşırı ısınması. Kamera bağlı değilken mediad sürekli çöküp yeniden başlıyor, GStreamer taraması bir çekirdeği dolduruyor, ana kart 89°C. mediad ve tofd kapatıldıktan sonra bile 85–92°C, CPU hep 408 MHz'e kilitli. Merkezi web joystick'inde Start'a basınca tepki yok: web gamepad hizmetinin başlaması 1.7 saniye sürüyor, padd'in onayı beklediği 0.6 saniyeyi aşıyor. Kullanıcı soğuması için kapattı, sonraki adım önce soğutma eklemek (delik açmak, hava kanalı yapmak), sonra web joystick'i ve yürümeyi denemek.

Her adımın komutları, sayıları ve nedenleri için bkz. **[2026-10-12 kissqy tam set gerçek robot](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy整套上机.md)**; sonuç [Tuzaklar](14-tuzaklar.md) belgesine eklendi.

## 2026-10-12 öğleden sonra · kissqy imajı R1'i açıp V1.12'nin açılabildiği bir kart çıkarmak

**Neden**: kissqy 10-12'de tam kart imajı "tek tıkla sistem imajı R1"i yayınladı (resmi 0.15.1 + onun firmware V164 / control.40, ilk açılışta hotspot ile ağ yapılandırması). Üç şeyin netleştirilmesi gerekiyordu: bizim türden kartlar açılabiliyor mu, IMU modülü tanınıyor mu, önceden kurulu şeylerin hangileri yeni başlayanları tuzağa düşürür. Olmayan yerler onun imajı üzerinde değiştirilecek, ayrı yeni bir iş çıkarılmayacak.

**Neler yapıldı**:

- `microduck-zero3w-0.15.1-R1.img.xz` indirildi, sha256 onun yayımladığı `75da978b…a7bce5` ile aynı.
- WSL'de yalnızca okuma modunda bağlanıp parçalandı, hiçbir program çalıştırılmadı: önyükleme bölgesi, açılış yapılandırması, açılışta otomatik başlayan hizmetler, firmware içindeki dizgiler, kalibrasyon, hesaplar incelendi, belirteç (token) ve özel anahtar imzalarına göre tarandı.
- V164'ün kurulum betiği ve güncelleme notları kopyalanıp v146 ile dosya dosya karşılaştırıldı.
- HAT'ın iki sürümüne (C1 üretim Gerber ve BOM, D1 KiCad projesi) bakılıp J5～J8 pin sırası ve J5 hattındaki çip adresleri kontrol edildi.
- [`tools/radxa/kissqy-r1-v112.sh`](../tools/radxa/kissqy-r1-v112.sh) yazıldı: onun imajında Radxa önyükleyicisini değiştirir, extlinux yazar (onun overlay'leri olduğu gibi taşınır), isteğe bağlı olarak mediad / tofd'yi kapatır ve overlay ekler.

**Sonuç**:

- Gizlilik çok temiz ele alınmış: belirteç, özel anahtar ve WiFi yok, hesap kilitli, SSH ana makine anahtarları ilk açılışta üretiliyor.
- Bizim donanımla uyuşmayan üç nokta var: önyükleme Armbian ana hat U-Boot 2025.10 + DDR v1.21 (bizim V1.12 kartın açılamadığı kombinasyon tam bu); yalnızca veri yolu IMU küçük kartını (ID 200) tanıyor; onun örnek makinesinin kalibrasyonu önceden kurulu, IMU de "onaylanmış" işaretli. Ayrıca kamera ve mesafe hizmetleri varsayılan olarak açık.
- V164 web gamepad'i webpad yerine doğrudan robotd'nin IPC'sine bağlamış, 10-12 sabahı joystick'in tepkisiz kalmasına yol açan yol değişmiş; ama merkezi kontrolden model içe aktarma da kaldırılmış.
- Betikle `--no-tof --overlay i2c4-m0` içeren bir kart yapılıp çevrimdışı doğrulandı: önyükleme bölgesi Radxa resmi paketiyle bayt bayt aynı; 0～63. sektörler (bölüm tablosu) dokunulmadı; kök bölümü orijinaliyle dosya dosya karşılaştırıldığında yalnızca beklenen 5 yer değişmiş (yeni `extlinux.conf` ve açıklama dosyası eklenmiş, `armbianEnv.txt` değişmiş, tofd otomatik başlatması kaldırılmış).
- C1 sürümü HAT'ın J5 hattında zaten ses (0x18) ve BMI088 (0x19 / 0x68) var, D1 sürümü LSM6DSV16X (0x6A) yapmış. J6'da R18/R19 sökülüp R16/R17 kısa devre edilirse I2C4'e çevrilebilir.

**Sıradaki adım**: Boş bir kart alıp değiştirilmiş imajı yaz, ilk makinede açılışı, hotspot ile ağ yapılandırmasını, SSH'yi dene (şimdiki karta dokunma); kissqy'ye V164 kaynağını ne zaman açacağını sor, böylece I²C IMU yamasını oraya taşıyalım.

Tüm dayanaklar için bkz. **[kissqy imajı R1 analizi](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-kissqy镜像R1分析.md)**; sonuç [Tuzaklar](14-tuzaklar.md) belgesine eklendi.

## 2026-10-12 gece · IMU 8.5° yamuk takılmış: kalibrasyondan sonra 70 saniye dengede kaldı, dönüşümlü adım atmaya başladı

**Tek cümleyle**: Model devralır devralmaz geriye doğru şiddetle atıldı; kök neden BNO085 modülünün yaklaşık 8.5° öne eğim, 1.75° sağa eğimle yamuk takılmış olmasıydı. Modelin eğitimde HOME'da gövde yataydı, ama IMU sürekli "öne 8.5° eğim" diyordu, model de çaresizce geriye doğru kurtarmaya çalışıyordu. Gerçek makinenin eklem açıları simülasyona konup "olması gereken eğim" hesaplandı, sapma çıkarılıp IMU montaj kuaterniyonuna eklendikten sonra model 70 saniye devralınca düşmedi (eğim ortalaması +0.2°), joystick 0.14～0.21 m/s itilince iki bacak ritimli dönüşümlü adım atmaya başladı. Ne kadar ileri gidildiği henüz ölçülmedi.

**Yol boyunca çözülenler**:
- Web gamepad'e basınca tepki yok: dört katmanlı neden (SSH girişinde 3.8 saniye boşa giden karşılama betiği, merkezi kontrolün 0.4 saniyede süresi dolmuş sayması, sanal gamepad'in soğuk başlangıcı, padd'in yeni aygıtı açma sırası), sonunda Thor G50 Pro Bluetooth doğrudan bağlantısına geçildi (arkadan S konumuna alınır);
- Taşınabilir güç kaynağı aşırı akımda 5 V'a düştü, servolar güçsüz, ayakta duruş tamamlanmadı; ayarlı güç kaynağı 8 V'a geçildi;
- BNO085'in kablosu zayıf temas ediyordu, I²C yanıt vermiyor, robotd IMU'yu eskimiş sayıp gücü kesiyordu; yeniden sağlam lehimlenip bağlanınca bir daha kopmadı.

**Ana karttaki değişiklikler**: SSH karşılama betiği kapatıldı (yedek var), IMU montaj kuaterniyonu `[0.454164155, 0.544101455, 0.527409117, 0.468538313]` yapıldı (yedek var), açılışta otomatik başlayan kayıt hizmeti `duck-rec` kuruldu, Bluetooth gamepad eşleştirildi. Nasıl geri alınacağı gerçek robot kaydının §9 bölümünde listelenmiş.

**Hâlâ çözülmeyenler**: Soğutma (model 10 dakika çalışınca CPU 85°C'ye çıkıp frekans düşürüyor), ağız servosu ayakta dururken 60～70°C, filtre 1/1/1 ve 0.9/0.5/0.7 henüz karşılaştırılmadı, TPU taban ve ilerleme mesafesi.

Her adımın verisi, nedeni, başkalarının nasıl takip edeceği: **[2026-10-12 gece gerçek robot kaydı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261012-夜-IMU校准与首次迈步.md)**; analiz betikleri ve IMU sıfır noktası kalibrasyon adımları: [`tools/radxa/onboard-analysis/`](../tools/radxa/onboard-analysis/).

## 2026-10-13 · Resmi 0.17'yi takip: UDP gamepad ve gamepad kopunca otomatik oturma (kod tamam, gerçek robotta denenmedi)

**Tek cümleyle**: Resmi taraf 10-12'de robotd 0.16.2～0.17.1'i art arda yayınladı, ana değişiklik "UDP gamepad": bilgisayara gamepad takılıp yerel ağ üzerinden ördek kontrol ediliyor. Bizim taban kissqy'nin 0.15.1'i; resmi 0.17.1'e kadar yirmi bin küsur satır değişmiş, iki tarafın arayüz sürüm numaraları da kendi yönünde artıp birbirini tutmuyor, bu yüzden bütünüyle yükseltilmiyor, yalnızca UDP gamepad ve "gamepad kopunca 1 saniyede otomatik oturma" kissqy'nin padd'ine taşındı. Yöntem padd'e ikinci bir giriş kaynağı eklemek, tuşlar kissqy'nin eşlemesini kullanıyor; kablo protokolü resmi olanla bayt bayt aynı, bilgisayar tarafı doğrudan resmi `uvx duckctl@0.17.1 udp-pad <IP>`'yi kullanabiliyor.

**İnceleme**: Değişiklikten sonra subagent ile bağımsız inceleme açıldı, toplam 6 tur, son turda mutlaka düzeltilmesi gereken sorun kalmadı. Düzeltilen sorunlar arasında: kurulum paketinin fiilen kullandığı unit dosyasında AF_INET'in serbest bırakılmaması; yeniden bağlanırken basılı tutulan Select'in acil durdurma sayılması (24 seferin 8'inde); robotd'nin geç yanıtının gamepad kopması sanılması; takılmadan sonra eski joystick ve eski uzun basışın hâlâ geçerli olması (kısa bir mesafe yürüme, yanlışlıkla kapanma); aynı turda bırakılıp tekrar basılan Select'in kapatmaya dönüşmesi. Hepsi betikle yeniden üretildi, düzeltildikten sonra yeniden testte 0.

**Sonuç**: padd birim testleri 79/79, uçtan uca 14 madde tamamen geçti, resmi 0.17.1'in kod çözücüsü bizim gönderdiğimiz her paketi açabiliyor. Ana kartta kullanılacak padd ve dağıtım betiği hazır (önce orijinali yedekler, tek komutla geri alınır). **Henüz gerçek robotta denenmedi**: gerçek robotta önce Bluetooth gamepad ile gerilemenin olmadığı doğrulanır, sonra D-pad aşağı ile oturma elle denenir, sonra kopunca oturma test edilir, en sonda UDP gamepad.

Neden böyle yapıldığı, nasıl kullanılacağı, incelemenin her maddesinin belirtisi ve nedeni: **[2026-10-13 resmi güncelleme ve UDP gamepad](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-官方更新与UDP手柄.md)**.

## 2026-10-13 gece ～ 10-14 sabaha karşı · Yeni kart gerçek robotta, tüm makinede güç kesilmesi, servo D ve titreme, sürtünme analizi

**Tek cümleyle**: kissqy'nin tek tıkla imajı (V164 + bizim IMU yamamız) yeni karta konuldu; açılış, ağ yapılandırması, Bluetooth gamepad hepsi çalıştı, ama yeni ve eski kart yürürken **tüm makinede güç kesiliyor** (yeni kartta servo ucunda son okunan yaklaşık 3.9 V), bu bir güç besleme sorunu, yazılım değil. Yürürken titreme **servonun D'si (donanım sönümleme)** ile ilgili: eğitimde kullanılan servo modelinde D yok, gerçek robot D=20/40 ile gidiyor. D=0 yapılınca titreme %51'den %4～8'e düştü; P3'te gövde sallanması simülasyonla aynı. Şu an eski kartta **P3 / D0 / tork 700** kullanılıyor.

**Yol boyunca çözülenler**:
- Yeni kartta G50 Pro eşleşir eşleşmez bağlantı kesiliyor: bu kartta açılışta Bluetooth bağlanabilir değil (No Bonding), `ClassicBondedOnly` bağlanmamış HID'leri reddediyor (birkaç madde birlikte değiştirilince bir kez eşleşti, yeniden doğrulanmalı);
- `robotd.toml` içinde ölçek ve filtre için yapılan birkaç karşılaştırma boşunaydı: birleşik model kendi paketindeki `deployment-execution.json` dosyasını kullanıyor;
- Yeni kartta merkezi kontroldeki P/D/tork kutuları işlemiyor: V164 yalnızca P yazıyor, D fabrika değeri 40'ta kalıyor;
- IMU roll sıfır noktası yaklaşık 1.1° eksikti, 1.14° geri eklendi;
- Kayıt hizmeti her saniye diske yazacak şekilde değiştirildi, dosya adına açılış numarası eklendi, sistem günlüğünün gerçek zamanlı kopyası eklendi, güç kesilince son saniye görülebiliyor.

**Hâlâ çözülmeyenler**:
- **Sürtünme (yere sürtme)**: İki ayağın yerden yüksekliği yalnızca 3～6 mm, simülasyonda 11～12 mm. Destek verirken diz düzleşemiyor, model uzatmak istiyor ama gerçek robot sürekli bükük kalıyor. Sol ayak daha çok sürtünüyor gibi görünüyor, çünkü adım atarken sol ayak parmağı aşağı bakıyor ve sağ bacak destek verirken gövde yaklaşık 1.5° daha fazla öne düşüyor; bu iki durum da D=0 yapıldıktan sonra ortaya çıktı (D=20'de yoktu), sıradaki adım D=5～10'u denemek. Ayrıca servo okumalarına göre iki ayak sağ-sol yönde (roll) yaklaşık 1.6°～2.6° fark gösteriyor, bakılmadı (10-14 gündüz bakıldı, bir sonraki bölüme bakın);
- **Güç**: 10 A güç kaynağı 10-16'da gelecek.

Her adımın verisi, nedeni, nasıl geri alınacağı: **[2026-10-13 gece gerçek robot kaydı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261013-夜-掉电-舵机D与蹭地.md)**; yürüyüş (gait) analiz betikleri: [`tools/gait-analysis/`](../tools/gait-analysis/); kayıt hizmeti: [`tools/radxa/onboard-analysis/`](../tools/radxa/onboard-analysis/).

## 2026-10-14 gündüz · Simülasyon karşılaştırmasıyla sürtünme nedenini bulma, taban, yeni sürümde P / D / tork serbest bırakıldı (gerçek robotta denenmedi)

**Tek cümleyle**: Gündüz ördek çevrimdışıydı, yalnızca bilgisayarda analiz ve kod yapıldı. kissqy'nin yürüme modeli simülasyonda gerçek robotla karşılaştırıldı; sabahki simülasyon koşullarının gerçek robotla hizalanmadığı görüldü: gerçek robotun birleşik modelinin hareket ölçeği aslında yaklaşık 0.83, kafa-bacak filtreli, kissqy'nin eğitimde kullandığı model 820 g; simülasyonda ise ölçek 1.0, filtresiz, 737 g. Hizalandıktan sonra (ağırlık kissqy'nin eğitim modelinin 820 g'ına göre tahmin edildi) simülasyondaki destek dizi gerçek robota yaklaştı, simülasyonda "diz düzleşemiyor" durumunun büyük kısmı bu koşullarla açıklanabiliyor; ama o simülasyon grubunda gerçek robotta olmayan yüksek frekanslı titreme (%96) çıkıyor, nedeni araştırılmadı. Ayrıca kissqy yeni V164 sürümünde P / D / tork sınırı ve kafa-bacak filtresi serbest bırakıldı (yerel, gerçek robotta denenmedi, yayınlanmaz).

**Yol boyunca netleşenler**:
- Simülasyon karşılaştırmasında önce ölçek, filtre, ağırlık, hızın hizalanması gerekiyor; ölçek 0.83'ten 1.0'a çıkarılınca simülasyonda yaklaşık 3 mm daha fazla kalkıyor; gerçek robotta birleşik ölçek 1.0 yapılıp gerilim telafisi çarpılınca yalnızca %11 ekliyor, doğrusal tahminle etki simülasyonun yaklaşık yarısı kadar, yine de denemeye değer;
- Simülasyonda %70 tork sınırı konup konmaması sonucu neredeyse hiç değiştirmiyor; hız farkın nedeni değil;
- Taban çok kaygan olursa simülasyonda küçük adımlar ve titremeye dönüşüyor, ama gerçek robotun D0 davranışıyla örtüşmüyor; bizim tabanımız TPU 95A, 85A'ya geçmek ya da kaymaz parça denemeye değer;
- HOME'da iki ayak sağ-sol düzlemde eş düzlemli değil: iki kalça roll'ü dışa açılıyor, her seferinde farklı, vücut ağırlığı bastırıyor gibi (tahmin); sıfır konumunun kayık olup olmadığı bu yöntemle görülemiyor; sabah sözlü söylenen "dış kenar kalkıyor" 14 kesitin 12'sinde ters çıktı;
- Servo parametrelerinin hepsi güç verilince RAM'e yazılıyor, güç kesilince geri alınıyor; güç verilmişken robotd yeniden başlatıldıysa parametreler serovda kalır, orijinal davranışa (yalnızca P yazma) dönmeden önce servoya bir kez güç kesilmeli (V164'te robotd yeniden başlatılınca ördek anında yığılır);
- kissqy yeni sürümündeki "gamepad bağlantısını onar" yalnızca Gamesir Nova 2 Lite'ı tanıyor, G50 Pro'ya faydası yok.

**Henüz yapılmadı**: Yeni karta ayarlanabilir sürüm kurmak, iki ayağın hangi tarafından ışık geçtiğine bakmak, tartmak, taban değiştirmek, ölçek 1.0'ı denemek; güç (10 A güç kaynağı 10-16'da gelecek).

Her adımın verisi ve nedeni: **[2026-10-14 gündüz kaydı](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/HD1910-20261014-白天-仿真找原因与新版放开参数.md)**; yeni betik [`tools/gait-analysis/home_roll.py`](../tools/gait-analysis/home_roll.py).

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
