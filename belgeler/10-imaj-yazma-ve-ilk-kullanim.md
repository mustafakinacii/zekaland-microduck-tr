# Microduck replika imajı: imaj yazma ve ilk kullanım

> [20261027 imajı](https://github.com/fanhao375/microduck-replica/releases/tag/microduck-replica-image-20261027) yayımlandı ve Latest olarak işaretlendi; derleme, açma (salt okunur) ve yayın eklerinin doğrulaması tamamlandı; **bu sürümün yeni karttaki gerçek donanım kabulü ise henüz tamamlanmadı.** İmajda web üzerinden yazılım güncellemesi ve yerel R3 "otur / ayağa kalk" önceden kurulu gelir; asıl kalibrasyon/ayakta durma sürecini tamamladıktan sonra kullanın, bkz. [Yazılım güncellemesi ve ses](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/软件更新与语音使用说明-20261027.md). Mevcut kartlar ileride bileşen güncellemesiyle kendi verilerini korur; her web özelliği için kartı yeniden yazmak gerekmez.

Adımları sırayla izleyin; ördek ayağa kalkar ve yürür. Her şey tarayıcıdan yapılır; SSH ve komut yazmak gerekmez.

> **İmaj ücretsizdir, yalnızca kişisel öğrenme ve ticari olmayan replika için sunulur.** İçindeki yürüme ve hareket modelleri yazarın kişisel, ticari olmayan lisansı altındadır:
> HAT, tam robot, kit vb. ürünlerle birlikte önceden yüklenemez veya dağıtılamaz; yazılmış kart satılamaz, ücretli hizmetlerde kullanılamaz.
> Her bölümün lisansı imajın içindeki `/usr/share/doc/microduck/` altında, ayrıca yayın sayfasında aynı üç txt dosyası olarak bulunur.

## 1. Hazırlık

- Kurulumu bitmiş bir **Feetech HD-1910 sürümü** ördek: 15 servonun ID'leri ayarlanmış, HAT takılmış. Orijinal XL330'lu ördekte bu imajı kullanmayın.
  - Bizim denediğimiz donanım: Radxa Zero 3W (eMMC'siz) + 32 GB microSD kart, HAT C1 sürümü.
- Gövde IMU'su, ikisinden biri:
  - **IMU modülü** (BNO085 veya LSM6DSV16X): dört telle doğrudan ana karta bağlanır; HAT'ın J5'ine ya da 40 pinli başlığın 27 / 28. pinlerine takılır.
    HAT'ın D1 sürümünde kafanın içinde zaten bir LSM6DSV16X (adres 0x6A) vardır; gövdedeki modül **0x6B** adresine ayarlanmalıdır.
    LSM6DSV16X modülü için önerilen montaj: modülün x ekseni aşağı, z ekseni ördeğin önüne baksın (2 numaralı ördekte böyle takılı). Böyle takarsanız IMU adımı doğrudan atlanabilir.
  - Ya da servo veri yolundaki IMU küçük kartı (ID 200): modül bulunamazsa ana program veri yolunda bunu arar.
    20261023c sürümünden itibaren FT6, bu depodaki imu_to_dxl'in Feetech yazılımı (0.2.0'dan itibaren) ve 124/12 SFLP düzenini kullanan DXL 2.0 yazılımı otomatik tanınır.
    Her üreticinin her yazılımı uyumlu değildir: farklı register biçimi, ID veya baud hızı için uyarlama gerekir; IMU sayfası gerçekte neyin tanındığını gösterir.
    IMU'yu ya da montaj yönünü değiştirdikten sonra yön kalibrasyonunu yeniden yapın; eski Feetech yön onayı DXL2 kuvvet için doğrudan kullanılamaz.
  - **IMU, ilk açılıştan önce bağlanmış olmalıdır:** ilk açılışta ördek onu kendisi arayıp tanır.
- Bir microSD kart, 8 GB üstü, 32 GB önerilir; bir kart okuyucu.
- Bir bilgisayar (kartı yazmak için), bir telefon (ağ ayarı için).

## 2. İndirme, doğrulama, kartı yazma

1. `microduck-replica-tarih.img.xz` dosyasını ve aynı adlı `.sha256` dosyasını indirin (GitHub Releases veya bulut disk).
2. Dosyanın bozuk inmediğini doğrulayın (atlanabilir, ama tuhaf bir sorun çıkarsa önce bunu kontrol edin):
   - Windows: indirme klasöründe PowerShell açıp `Get-FileHash microduck-replica-tarih.img.xz` çalıştırın, çıkan diziyi `.sha256` dosyasındaki ile karşılaştırın (büyük/küçük harf önemli değil);
   - Mac / Linux: `shasum -a 256 -c microduck-replica-tarih.img.xz.sha256`.
3. Kartı [balenaEtcher](https://etcher.balena.io/) ile yazın: imaj dosyasını seçin (`.img.xz` açılmadan kullanılır) → SD kartı seçin → Flash.
   Raspberry Pi'nin resmi Raspberry Pi Imager'ı da olur: "İşletim sistemi" listesinin en altından "Özel imaj kullan" seçilir.
4. Yazma bittikten sonra Windows "biçimlendirmek gerekiyor" diye uyarabilir; **İptal**'e basın, biçimlendirmeyin.

## 3. İlk açılış

1. SD kartı ana karta takın, ördeği çalıştırın (servo gücünü de bağlayın).
2. **Yaklaşık 3 dakika** bekleyin. İlk açılışta üç iş yapılır: SD kartın kalan alanı genişletilir; ördeğe bir ad verilir (`duck-` ve 4 karakter, örn. `duck-c51b`); IMU modülü tanınır. Sonraki açılışlar daha hızlıdır.
3. Ördek hiçbir WiFi'ye bağlanamıyorsa (ilk açılışta mutlaka böyledir) kendi erişim noktasını (hotspot) açar:
   - Ad: `Microduck-` ve aynı 4 karakter, örn. `Microduck-c51b`;
   - Parola: `microduck`.

## 4. Telefonu ördeğe bağlama, evdeki WiFi'yi ayarlama

1. Telefonun WiFi listesinde `Microduck-xxxx` ağını bulun, `microduck` parolasıyla bağlanın.
   Telefon "bu ağ internete bağlı değil" derse **bağlı kal**'ı seçin.
2. Telefon tarayıcısında **http://10.42.0.1:8000/** adresini açın; Microduck Studio görünür.
   Açılmazsa önce telefonun **mobil verisini kapatıp** tekrar deneyin (bazı Android telefonlar internetsiz WiFi'yi atlar).
3. En üstte "WiFi'ye bağlan" kartı vardır: evinizdeki WiFi'ye dokunun, parolayı girin, "Bağlan"a basın, onay kutusundaki metni dikkatle okuyun, ardından "Bağlantıyı kes, «ev WiFi'niz»e bağlan"a basın.
   Her bağlanışta parola girilmelidir; "kayıtlı" ağlar için de böyledir.
4. Ördek hotspot'u kapatıp ev WiFi'nize bağlanır; **telefonun bağlantısı kopar, bu normaldir.**
5. Telefonu (veya bilgisayarı) ev WiFi'sine geri bağlayın, cihaza göre şu adreslerden birini açın (xxxx, hotspot adındaki 4 karakterdir):
   - **Windows bilgisayar:** **http://duck-xxxx:8000/** (`.local` olmadan; Clash gibi bir proxy açıkken de çalışır);
   - **iPhone, Mac:** **http://duck-xxxx.local:8000/**;
   - **Android telefon veya yukarıdakilerin hiçbiri açılmıyorsa:** yönlendiricinin yönetim sayfasında cihaz listesinde `duck-xxxx` kaydını bulun ve IP'siyle açın, örn. `http://192.168.1.23:8000/`.
   - Açıldıktan sonra "Daha fazla" sayfasında bu ördeğin tüm güncel adresleri listelenir; yer imi ekleyebilirsiniz.
6. Parola yanlış girilirse veya ördek bağlanamazsa hotspot kendiliğinden geri gelir (genellikle hemen, en geç 2 dakika kadar içinde). Tekrar `Microduck-xxxx`'e bağlanın; kartta son denemenin neden başarısız olduğu kırmızı yazıyla görünür, düzeltip yeniden deneyin.

Evdeki WiFi'ye bağlanmak istemezseniz de olur: ördeğin hotspot'una sürekli bağlı kalıp Studio'yu kullanabilirsiniz; tüm özellikler çalışır.

**Güvenlik uyarısı:** Hotspot parolasını herkes bilir, Studio'nun da varsayılan olarak giriş parolası yoktur; yani **yakındaki biri hotspot'a bağlanıp ördeği kontrol edebilir.**
Dışarıda gösteri yapmadan önce Studio'nun "Daha fazla" sayfasında bir giriş parolası belirleyin.

## 5. "Başlangıç listesi"ni izleyin

Genel bakış sayfasında bir "Başlangıç listesi" vardır; yukarıdan aşağıya yapılır. Her adımın üç düğmesi vardır: "Yap" sizi ilgili sayfaya götürür; daha önce yaptığınız adımlar için (örn. servo sıfır konumu çoktan kalibre edildiyse) "Tamamlandı"; şimdilik yapmak istemediğiniz için "Atla". Ana program o adımın henüz bitmediğini söylüyorsa, "Tamamlandı" veya "Atla"ya basarken sonucu hatırlatan bir uyarı çıkar; onaylarsanız adım sayılır.

1. **Servo sıfır konumu:** Servo sayfasına gidin, ördeği sıfır konumuna getirin (bacaklar düz, kafa dik, gaga kapalı), "Tek tuşla kalibrasyon"a basın.
2. **IMU yönü:** IMU sayfasına gidip kaba kalibrasyon yapın: ördeği iki elinizle kaldırın, dik tutun, kıpırdatmayın, ardından sayfadaki yönergeye göre öne doğru eğin.
   Sayfa yönü hesapladıktan sonra ana programa bir kez daha doğrulatılır: dik tutun, ardından **20 saniye içinde kafayı 15–30° öne eğin.**
   Ana program doğrularsa yön kaydedilmiş olur.
   - **Daha doğru yöntem: ayakta kalibrasyon.** IMU sayfasında "Duruş etkinleştir"e basın; 15 servo 3 saniye içinde birlikte duruş pozuna döner ve kilitlenir (kalibrasyon modunda da ayakta durabilir,
     yalnızca denge kurmaz; elle tutmak gerekir). Ayakta durunca "ayakta kalibrasyon"u yapın (hareketsiz, ön, arka, sol, sağ); bittiğinde "Devre dışı bırak"a veya üstteki "Gücü kes"e basıp ördeği elinizle tutun.
     Hesaplanan yön 3. adımda birlikte ana programa yazılır. Kaba kalibrasyon yapılmamış olsa da ayakta kalibrasyon yapılabilir.
   - **Daha önce kalibre ettiyseniz veya şimdilik atlamak isterseniz:** "Tamamlandı" ya da "Atla"ya basın; 3. adım IMU yönünü varsayılan montaja göre yazar:
     veri yolu IMU küçük kartı için resmi montaj; BNO085 için fork'un varsayılan montajı; LSM6DSV16X için replikanın önerdiği montaj (modül x ekseni aşağı, z ekseni ileri).
     Farklı monte edilmişse ördek ayağa kalktığında bir yana devrilir: yukarıdaki gibi bir kez ayakta kalibrasyon yapın, ana programa bir kez daha yazın.
3. **Ana programa yazma:** Yukarıdaki iki adımın sonucu tek seferde ana programa yazılır. Yazmadan önce ördeğin **oturur durumda veya yumuşakken** olmasını sağlayın (duruş etkinleştirmeyle ayakta duruyorsa önce "Devre dışı bırak"a basın); servo gücü açık olmalıdır.
   Yazma bitince ana program yeniden başlar (yaklaşık 20 saniye, yavaşsa bir dakika), kalibrasyon modundan hareket moduna geçilir; **ördeği elinizle tutun.**
   Ana program bu kalibrasyonu kabul etmezse otomatik olarak eskisine döner, sayfada nedeni yazar.
   Bundan sonra açılışta ördek doğrudan ayağa kalkıp yürüyebilir; web sayfasını açmak gerekmez.
4. **Gamepad eşleştirme:** Gamepad sayfasında sihirbazı izleyerek Bluetooth gamepad'i eşleştirin. İsterseniz önce web sayfasındaki gamepad'i de kullanabilirsiniz.
   Thunderobot G50 Pro gibi platform değiştirebilen gamepad'lerde arkadaki anahtarı **X konumuna (Xbox)** getirin: 20261021b sürümünde X konumu bir seferde bağlanır; S konumunda (Switch Pro) eşleşme başarılı olur ama ana program tuş girişini alamaz, gamepad bir süre sonra kendiliğinden kapanır (nedeni hâlâ araştırılıyor).
5. **Acil durdurma testi:** Gamepad'de Select'e **kısa** bir kez basın, ördeğin hemen gücünü kestiğini doğrulayın. (Select'e 2 saniye basılı tutmak: otur, gücü kes, **kapat**; acil durdurma testinde basılı tutmayın.)
6. **Ayağa kalkma, birkaç adım yürüme:** "Ayağa kalk"a, sonra "Yürümeye başla"ya basın, joystick'i itin.

İstediğiniz an ördeği hemen yumuşatmak için: sayfanın sağ üstündeki kırmızı "Gücü kes" düğmesine basın veya boşluk tuşuna basın.

## 6. Gamepad tuşları

Xbox gamepad'in konumlarına göre:

| Tuş | Ne yapar |
|---|---|
| Start | İlk basışta ayağa kalkar, sonraki basışta yürümeye başlar / durur |
| Sol joystick / Sağ joystick | Yürü / dön |
| Select kısa basış | Hemen gücü keser (acil durdurma) |
| Select 2 saniye basılı | Otur, gücü kes, kapat |
| Yön tuşu aşağı | Otur / ayağa kalk |
| Yön tuşu sağ | Tüm servoları yeniden başlat |
| A (alttaki) | Eğilip bir şey al |
| X (soldaki) | Öne takla |
| LB / RB | Sol ayakla / sağ ayakla tekme |
| Y / B | Kafa modu / gövde duruşu |
| Tetikler | Ağzı aç |
| Yön tuşu yukarı 3 saniye basılı | Yürüme ile paten arasında geçiş (pasif paten bileşeni takılmış olmalı; normal ördekte basmayın) |

Öne takla ve tekmeyi ilk denerken ördeğin çevresinde boşluk bırakın. Hangi hareketin hangi modele karşılık geldiği imajdaki `/usr/share/doc/microduck/模型说明.txt` dosyasında yazar.

## 7. Sorun çıkarsa

- **`Microduck-xxxx` hotspot'u görünmüyor:**
  - Ördek zaten ev WiFi'nize bağlıysa hotspot açılmaz; doğrudan `http://duck-xxxx.local:8000/` ya da yönlendiricideki IP ile açın;
  - İlk açılışta 2 dakika daha bekleyin; hâlâ yoksa gücü kesip yeniden açın.
- **Sayfa açılmıyor:** Telefonun ördeğin hotspot'una (veya ördekle aynı WiFi'ye) bağlı olduğunu, adresin sonunda `:8000` bulunduğunu doğrulayın; Android'de mobil veriyi kapatıp tekrar deneyin.
- **Bilgisayarda Clash gibi bir proxy açık:** `.local` adresleri proxy'ye gider ve açılmaz (502 hatası). Windows'ta `http://duck-xxxx:8000/` ya da IP kullanın;
  TUN modu açıkken de açılmıyorsa proxy yazılımında yerel ağı (192.168.0.0/16, 10.0.0.0/8) doğrudan bağlantıya (direct) alın ya da atlama (bypass) listesine `*.local` ekleyin.
- **IMU adımı "ana program hangi IMU'yu kullandığını henüz bildirmedi" diyor:** çoğunlukla ilk açılışta modülün tanınamamasından kaynaklanır. Kabloları ve adresi kontrol edin (HAT D1 sürümünde gövde modülü 0x6B olmalı),
  sonra SSH ile `sudo microduck-firstboot --detect-imu-only --force` çalıştırın ve ördeği yeniden başlatın.
- **Yardım:** Studio'nun "Daha fazla" sayfasında (bilgisayarda "Günlük" sayfasında da) "Tanılama paketini dışa aktar"a basın, dosyayı gruba gönderin ve hangi adımda takıldığınızı belirtin.
  Tanılama paketinde ördeğin seri numarası ve yerel ağ IP'si bulunur; sakıncalı buluyorsanız özel mesajla gönderin.

## 8. İleri düzey (gerekmez, ama kullanılabilir)

- **SSH ile uzaktan giriş** (sorun çıkarsa kartı yeniden yazmadan kendiniz girip düzeltin): Studio "Daha fazla" sayfasındaki "SSH uzaktan giriş".
  Önce yukarıdan web giriş parolasını belirleyin, ardından **kendiniz bir SSH parolası belirleyin** (en az 8 karakter, `microduck` olamaz), "SSH parola girişini aç"a basın.
  Kartta giriş komutu yazar, örn. `ssh radxa@duck-xxxx`: Windows'ta PowerShell'i, Mac'te Terminal'i açıp çalıştırın, az önce belirlediğiniz parolayı girin.
  Bu parola ördek üzerindeki `sudo` parolasıdır da. Kullanmayacaksanız "SSH parola girişini kapat"a basın; yalnızca anahtar kabul edilen duruma döner.
  Fabrika ayarında SSH yalnızca anahtar kabul eder, parola kabul etmez; imajda **kimsenin anahtarı yoktur**, uzaktan girilebilen varsayılan bir parola da yoktur.
- **Yerel giriş** (ekran ve klavye bağlayarak): kullanıcı adı `radxa`, varsayılan parola `microduck`; root ile giriş yapılamaz. Girdikten sonra `passwd` ile değiştirin.
- **SSH anahtarı kaydetme** (parolasız, daha güvenli): aynı "SSH uzaktan giriş" kartındaki "ikinci yöntem".
  Henüz anahtarınız yoksa Windows'ta PowerShell'de `ssh-keygen -t ed25519` çalıştırıp hepsine Enter'a basın;
  ardından `type $env:USERPROFILE\.ssh\id_ed25519.pub` (Mac: `cat ~/.ssh/id_ed25519.pub`) çalıştırın, çıkan satırın tamamını yapıştırıp "Bu anahtarı kaydet"e basın.
  **Yalnızca `.pub` uzantılı olanı yapıştırın;** diğeri özel anahtardır, kimseye vermeyin. Kaydedilmiş anahtarlar kartta listelenir ve silinebilir.
- **Studio giriş parolası:** "Daha fazla" sayfasında belirlenir. Ördekte radxa kullanıcısıyla `python3 -I /home/radxa/studio-dev/run.py set-password` da çalıştırılabilir; **sudo eklemeyin** (eklerseniz Studio parola dosyasını okuyamaz).
  Hiç parola belirlenmemişse Studio'yu açan herkes ilk parolayı belirleyebilir; bu yüzden dışarıda gösteri yapmadan önce kendiniz belirleyin.
- **Giriş parolasını unuttuysanız:** SSH ile ördeğe girin, parola dosyasını silin: `/var/lib/microduck-studio/password.json` veya `/home/radxa/studio-dev/state/password.json` (hangisi varsa), ardından `sudo systemctl restart microduck-studio` çalıştırın; parolasız duruma dönülür.
- **Kamera bağlandıysa:** İmaj varsayılan olarak test görüntüsü kullanır; kamerası olmayan ördekte hata vermez. Kamera bağlıysa `/etc/robot/robotd.toml` içindeki `[media]` bölümünde `source = "test"` değerini `source = "camera"` yapın, ardından `sudo systemctl restart mediad` çalıştırın.
- **Bilinmesi gereken iki varsayılan davranış:** Pil gerilimi düşünce **otomatik kapanma olmaz**, yalnızca sayfada uyarı verilir; uyarıyı görünce durup şarj edin, pili tamamen bitirmeyin;
  ördek düştükten sonra **gücü otomatik kesilmez**; kaldırmadan önce Select'e basın veya "Gücü kes"e dokunun.
- **İmajda neler var, lisanslar:** ördekteki `/usr/share/doc/microduck/` dizini veya [İmaj derleme notları](../software/image/README.md#镜像里有什么).

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
