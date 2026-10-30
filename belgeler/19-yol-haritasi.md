# Yol Haritası — Sıfırdan Yürüyen Ördeğe

Zekaland Robot Ördek'i Türkiye'den parça toplayarak yapmanın önerilen sırası. Her adımın ayrıntısı bağlantılı belgede.

## 0. Hafta — Karar ve sipariş

- [ ] Servo sürümünü kesinleştirin: bu repo **Feetech HD-1910** içindir.
- [ ] [Alışveriş listesi](../ALISVERIS_LISTESI.md)'ni okuyun. Bütçe 350–600 $.
- [ ] **İlk sipariş:** 15 servo + FE-URT-2 programlama kartı. Teslim süresi en uzun olan bunlar.
- [ ] **İkinci sipariş:** Radxa ZERO 3W, IMX219 kamera, VL53L8CX sensör (AliExpress).
- [ ] **Üçüncü sipariş:** RPI Robot HAT + imu_to_dxl + pil kartı, tek JLCPCB siparişinde ([13-devre-kartlari.md](13-devre-kartlari.md)).
  HAT bastırmak istemiyorsanız: [08-hat-olmadan-kurulum.md](08-hat-olmadan-kurulum.md).
- [ ] Türkiye'den standart parçalar: rulman, vida, pil, Loctite.
- [ ] Önce [14-tuzaklar.md](14-tuzaklar.md) dosyasının "Satın alma" bölümünü okuyun.

## 1–2. Hafta — Baskı (siparişler yoldayken)

- [ ] [`modeller/feetech/zekaland-robot-ordek-feetech.3mf`](../modeller/feetech/zekaland-robot-ordek-feetech.3mf) projesini açın, yazıcınızı seçin.
- [ ] Önce tek bir servo yuvalı parçayla ölçü denemesi yapın ([12-baski-ve-cad.md](12-baski-ve-cad.md)).
- [ ] 6 tabla toplam ~411 g PLA, ~22 saat. TPU parçaları ayrı basın.
- [ ] İsteğe bağlı: ZEKALAND rozeti ve kaidesi ([`modeller/zekaland/`](../modeller/zekaland/)).

## 3. Hafta — Servolar

- [ ] Servolar geldiğinde, **montajdan önce** her birine ID atayın ve test edin. URT-2 kartıyla tek tek yapılır ([15-hata-ayiklama-kayitlari.md](15-hata-ayiklama-kayitlari.md), "15 servoya ID atama").
- [ ] Veri yolu: 1 Mbps, IMU kartı ID 200 ([04-donanim-ozellikleri.md](04-donanim-ozellikleri.md)).
- [ ] Servoları etiketleyin (ID numarasını küçük bir bantla üzerine yazın).

## 4. Hafta — Montaj

- [ ] [18-montaj-kilavuzu.md](18-montaj-kilavuzu.md): gövde → sol bacak → boyun ve kafa → sağ bacak.
- [ ] Vidalar: [07-vidalar-ve-baglanti.md](07-vidalar-ve-baglanti.md). Hareketli bağlantılarda Loctite 243.
- [ ] Kablolar gövdedeki deliklerden çıkar, sıkıştırılmaz.

## 5. Hafta — İlk açılış

- [ ] [20-ilk-acilis-kontrol-listesi.md](20-ilk-acilis-kontrol-listesi.md) dosyasındaki bütün maddeleri işaretleyin.
- [ ] İmajı SD karta yazın ([10-imaj-yazma-ve-ilk-kullanim.md](10-imaj-yazma-ve-ilk-kullanim.md)).
- [ ] Web panelinden sırasıyla servo sıfır konumu, IMU yönü, ana programa yazma.
- [ ] İlk ayağa kalkışta ördeği **elle tutun**.

## Sonrası

- Yürüme ayarı, gamepad ile kumanda, ses ve kamera: [11-radxa-imaj-kullanimi.md](11-radxa-imaj-kullanimi.md) ve [`software/`](../software/).
- Sorun çıkarsa önce [14-tuzaklar.md](14-tuzaklar.md), sonra [15-hata-ayiklama-kayitlari.md](15-hata-ayiklama-kayitlari.md).
- Yaptığınız ördeğin fotoğrafını ve videosunu bize gönderin: **bilgi@zekaland.com.tr**.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
