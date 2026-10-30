# Yapım Günlüğü

**Basitleştirilmiş Çince (özgün dil)** · [İngilizce](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/BUILD-LOG.en.md)

> **Güncel durum: Feetech HD-1910 sürümünün tam montajı tamamlandı**
> Mekanik montaj kaydı: 2026-09-13; elektrik ilerleme dizini güncellemesi: 2026-09-28　|　Gerçek fotoğraflar aşağıda ↓

Bu depo, açık MJCF ve kaynak koddan geometriyi, montaj ilişkisini ve elektronik çözümü tersine çıkarır, aynı zamanda gerçek parça doğrulamalarını da sürekli kaydeder.
Bu günlük onu **gerçekten yapma** sürecini kaydeder: ne basıldı, ne takıldı, nerede sorun çıktı.

Elektrikteki son gelişmeler: HAT geldi, kamera flat kablosu ayarlandıktan sonra resmi B1'de görüntü alındı, proje imajına dönülerek yeniden test edilmeye hazırlanıyor; ağız servosu geçici olarak ID 21 olarak kullanılıyor. Ayrıntılar için [Hata ayıklama kayıtları](15-hata-ayiklama-kayitlari.md); bağlantı hatırlatmaları için [Tuzaklar](14-tuzaklar.md) (Ana kart / HAT / kamera bölümü).

> ⚠️ Bu depo şu yargıyı defalarca vurgulamıştır: **Simülasyon STL'si baskıya hazır bir mühendislik parçası değildir** —
> simülasyon yalnızca dış şekli ve ataleti garanti eder; geçme toleransını, dişleri, gömme parça yuvasını ve kablo geçiş alanını garanti etmez.
> **Bu günlük, bu cümlenin gerçekten doğru olup olmadığını doğrular.** Sonuç, olumlu ya da olumsuz, olduğu gibi buraya yazılacaktır.

---

## İlerleme

| Tarih | Aşama | Durum | Not |
|---|---|---|---|
| 2026-09-01 | İlk parti parça baskısı | 🔨 Sürüyor | Kafa kabuğu, gövde kabuğu, bacak yapı parçaları, ayaklar |
| 2026-09-02 | Bacak parçalarının deneme montajı | ✅ Tamamlandı | **M2 vidalar takıldı, delik konumları kullanılabilir** |
| 2026-09-12 | Feetech sürümü yapı parçalarının yeniden modellenip basılması | ✅ Tamamlandı | **HD-1910 servo kolu dışbükey, XL330 servo kolu içbükey**, 8 geçme parçası değiştirildi |
| 2026-09-13 | Tam makine montajı | ✅ Tamamlandı | 15 HD-1910 ID'leriyle birlikte takıldı, aşağıya bakın |

Gösterge: 📋 planlandı · 🔨 sürüyor · ✅ tamamlandı · ⚠️ sorun çıktı · ❌ bu yol çıkmaz

---

## Baskı kayıtları

| Parça | Malzeme | Katman yüksekliği | Dolgu | Süre | Sonuç |
|---|---|---|---|---|---|
| *(doldurulacak)* | | | | | |

**Yazıcı / dilimleme yazılımı**: *(doldurulacak)*

---

## Yaşanan tuzaklar

> Bu bölüm tüm günlüğün en değerli kısmıdır — **başkaları aynı tuzağa düşmeyebilir.**
> Her madde "belirti → neden → çözüm" biçiminde yazılır; çözülmemişse "çözülmedi" yazılır.

### (doldurulacak)

**Belirti**:
**Neden**:
**Çözüm**:

---

## Boyut ve geçme doğrulaması

Tersine çıkarılan verilerin gerçek parçada doğru olup olmadığı:

| Madde | Tersine çıkarılan değer | Ölçülen değer | Uyuşuyor mu |
|---|---|---|---|
| Tüm makinenin dış ölçüleri | 144 × 141 × 264 mm | *(ölçülecek)* | |
| M2 geçiş deliği | Ø2.2 mm | *(ölçülecek)* | |
| M2 havşa deliği | Ø4.4 mm | *(ölçülecek)* | |
| M2 diş açma ön deliği | Ø1.6 mm | *(ölçülecek)* | |
| Rulman yuvası | Ø22 × 16 × 4 mm | *(ölçülecek)* | |

> FDM baskı genellikle delik çapını 0.1–0.3 mm küçültür; bu sütundaki ölçüm verileri sonradan gelenler için çok değerlidir.

---

## Çözülecekler

- [ ] *(doldurulacak)*

---

## Fotoğraflar

### 2026-09-02 · İlk baskı parçaları

![İlk baskı parçaları](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/build-log/photos/2026-09-02-首批打印件.jpg)

Basılıp kısmen monte edilmiş parçalar:

- **Kafa grubu** — çok renkli baskı (beyaz / siyah / kırmızı), kamera halka yuvası ve gösterge ışığı açıklığı dahil, yüzey kalitesi iyi
- **Boyun** — siyah, kafaya bağlanmış
- **Gövde kabuğu** — beyaz
- **Bacak yapı parçaları** — siyah, **M2 vidalar takılmış**
- **Ayaklar** — kırmızı / sarı iki renk, iki adet

> 📌 **İlk gerçek parça doğrulama noktası**: Siyah bacak parçalarındaki **M2 vidalar takılmış durumda**.
> Bu, [Vidalar ve bağlantı (tersine çıkarım)](07-vidalar-ve-baglanti.md) belgesinin vardığı "tüm makine M2 vida sistemidir" sonucunun
> gerçek parçada geçerli olduğunu gösteriyor — en azından bu birkaç delik konumu için.
>
> Kesin delik çapı ölçüm verileri henüz eklenmedi, yukarıdaki "Boyut ve geçme doğrulaması" tablosuna bakın.

---

## 2026-09-13 · Feetech HD-1910 sürümü monte edildi

<table><tr>
<td width="50%"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/build-log/photos/2026-09-13-飞特版装机-正面.jpg" alt="Ön"></td>
<td width="50%"><img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/build-log/photos/2026-09-13-飞特版装机-手持.jpg" alt="Elde"></td>
</tr></table>

**15 HD-1910'un tamamına ID atandı ve gövdeye takıldı.** Kafa, boyun, iki bacak, ayaklar, eksiksiz.

**Fark edilen sorun**: HD-1910 ile XL330'un dış şekli yakın (34×20×23 ve 20×34×26), ama **servo kolları farklı — HD-1910'unki dışbükey, XL330'unki içbükey**.
Orijinal yapı parçaları içbükey servo koluna göre tasarlanmış, olduğu gibi takılamıyor. Çalışma arkadaşı servo koluyla geçme yapan tüm parçaları değiştirdi:

```
left_upper_leg / right_upper_leg   Uyluk          Kalça pitch ve diz servo kolu konumu
leg                                Baldır         Diz ve ayak bileği servo kolu konumu
trunk_base                         Gövde tabanı   Kalça yaw servo konumu
yaw2roll                           Yaw'dan roll'e Kalça yaw servo kolu → kalça roll
bearing_roll                       Rulmanlı makara Kalça roll rulman yuvası
01-upper_leg_rigidity_plate        Uyluk takviye plakası
99-yaw_roll_motion                 Kafa yaw/roll  İki varyant
```

O zaman değiştirilen SolidWorks çizimleri (`-FT` son ekli) ve 9 STEP dosyası
[CAD deposu v2.0](https://github.com/fanhao375/microduck-replica-cad/releases/tag/v2.0) ile eşleşiyor. **Şimdi model indirirken ya da baskı projesi hazırlarken lütfen hepsini [microduck-replica-cad](https://github.com/fanhao375/microduck-replica-cad) deposundan ilgili sürümü seçerek yapın**; bu geçmiş kaydı en güncel baskı kılavuzu olarak almayın.

**Sıradaki adım**: Tezgâhta veri yolu (bus) bağlantısı (URT-2 → Radxa), bkz. [Hata ayıklama kayıtları](15-hata-ayiklama-kayitlari.md).

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
