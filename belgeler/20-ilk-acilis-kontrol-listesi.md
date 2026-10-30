# İlk Açılış Kontrol Listesi

Pili ilk kez takmadan önce bu listeyi baştan sona işaretleyin. Bu adımlardaki hatalar servo, kart ya da pil kaybına yol açabilir.

## Güç

- [ ] Pil **NP-F550** (2S, 7,4 V nominal). Dolu pilde veri yolu **8,4 V**'a çıkar.
- [ ] Pil kartındaki **artı ve eksi kutuplar multimetreyle doğrulandı.** Kutup ters bağlanırsa kartlar yanar.
- [ ] Ana kart ilk testte USB'den beslenir. Servo gücü ilk testte bağlı değil.
- [ ] HAT kullanılmıyorsa: pilin ham gerilimi servo veri yoluna, düşürücü modülün 5 V çıkışı ana karta gider. Pil eksisi, modül çıkış eksisi, ana kart GND'si ve veri yolu GND'si ortaktır. Pil gerilimi **URT-2'nin V1 ucuna verilmez** ([08-hat-olmadan-kurulum.md](08-hat-olmadan-kurulum.md)).
- [ ] HAT'ta pil şarj devresi yok. Pil dışarıda, kendi şarj aletiyle şarj edilir.

## Servolar ve veri yolu

- [ ] 15 servonun her biri **ayrı ayrı** ID atandı ve test edildi. Aynı ID'ye sahip iki servo veri yolunda çakışır.
- [ ] Bütün servolar 1 Mbps hızda.
- [ ] IMU kartı veri yolunda ve **ID 200** ile yanıt veriyor. IMU ilk açılıştan önce bağlı olmalı; ana program onu ilk açılışta arar.
- [ ] Servo kablolarının hiçbiri eklem dönerken gerilmiyor ya da sıkışmıyor. Bacakları elle tam açıda oynatıp kontrol edin.

## Mekanik

- [ ] Bütün eklemler güç yokken elle rahat dönüyor; takılma yok.
- [ ] Servo kolları (horn) **sıfır konumunda** takıldı: bacaklar düz, kafa dik, gaga kapalı.
- [ ] Hareketli bağlantılardaki vidalarda Loctite 243 var.
- [ ] Ayak tabanları yerinde, kaymaz pedler yapıştırılmış.

## Yazılım

- [ ] SD karta güncel imaj yazıldı ([10-imaj-yazma-ve-ilk-kullanim.md](10-imaj-yazma-ve-ilk-kullanim.md)).
- [ ] İlk açılışta ördek kendi WiFi erişim noktasını açar. Telefonla bağlanıp web paneline girin.
- [ ] Panelde "Başlangıç listesi" yukarıdan aşağıya yapılır:
  1. Servo sıfır konumu → "Tek tuşla kalibrasyon"
  2. IMU yönü → kaba kalibrasyon ya da ayakta kalibrasyon
  3. Ana programa yazma (yaklaşık 20 saniye yeniden başlar)

## Kapatma

- [ ] Ördek her zaman **önce yazılımdan kapatılır, sonra güç kesilir.** Ani güç kesilmesi SD kartı bozabilir.

## İlk ayağa kalkış

- [ ] Ördeği **iki elinizle tutun**. Kalibrasyon modundan hareket moduna geçerken hemen hareket eder.
- [ ] Ördek bir yana devriliyorsa: IMU montaj yönü farklıdır, ayakta kalibrasyonu tekrar yapın.
- [ ] Servolardan biri ısınıyor ya da tıklıyorsa: hemen gücü kesin, o eklemin kolunu ve kablosunu kontrol edin ([14-tuzaklar.md](14-tuzaklar.md), "Servo / Kalibrasyon").

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
