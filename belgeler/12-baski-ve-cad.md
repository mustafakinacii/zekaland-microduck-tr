# Baskı ve CAD Dosyaları

Robotun bütün baskı dosyaları bu repoda, [`modeller/`](../modeller/) klasöründe.

| Klasör / dosya | Ne |
|---|---|
| [`modeller/feetech/zekaland-robot-ordek-feetech.3mf`](../modeller/feetech/zekaland-robot-ordek-feetech.3mf) | **Bambu Studio projesi.** 6 tabla, tüm parçalar dizili, ayarlar hazır. Ayak tabanlarında ZEKALAND yazısı var |
| [`modeller/feetech/stl/`](../modeller/feetech/stl/) | Aynı parçalar ayrı STL olarak (Cura, PrusaSlicer, OrcaSlicer için) |
| [`modeller/feetech/tabla-1.png` … `tabla-5.png`](../modeller/feetech/) | Tabla dizilim önizlemeleri |
| [`modeller/zekaland/`](../modeller/zekaland/) | Zekaland aksesuarları: sırt rozeti ve sergileme kaidesi |
| [`modeller/montaj-gorselleri/`](../modeller/montaj-gorselleri/) | Her alt grubun montaj ve patlatılmış görünüm resimleri |
| [`modeller/montaj-kilavuzu.pdf`](../modeller/montaj-kilavuzu.pdf) | Orijinal montaj kılavuzu (PDF). Türkçesi: [18-montaj-kilavuzu.md](18-montaj-kilavuzu.md) |

> ⚠️ Bu dosyalar **Feetech HD-1910** servolu sürüm içindir. Dynamixel XL330 servoların bağlantı parçaları farklıdır, iki sürüm karıştırılmaz.

## Bambu Studio projesi

Proje ayarları (dilimleyiciyle doğrulandı, 31 Ekim 2026):

| Ayar | Değer |
|---|---|
| Yazıcı profili | Bambu Lab P2S, 0,4 mm nozul |
| Katman yüksekliği | 0,20 mm (Standard) |
| Duvar sayısı | 6 |
| Doluluk | %15 |
| Destek | Açık |
| Filament | Bambu PLA Basic |

| Tabla | Filament | Süre (P2S tahmini) |
|---|---|---|
| 1 | 170 g | 9 sa 8 dk |
| 2 | 22 g | 1 sa 6 dk |
| 3 | 100 g | 5 sa 22 dk |
| 4 | 94 g | 4 sa 55 dk |
| 5 | 8 g | 29 dk |
| 6 | 16 g | 34 dk |
| **Toplam** | **~411 g** | **~21,6 saat** |

**A1 / A1 mini / X1 / P1S kullanıyorsanız:** Projeyi açın, sağ üstteki yazıcı seçiminden kendi yazıcınızı seçin ve "Ayarları koru" deyin. Parçalar tablaya sığmazsa "Otomatik yerleştir" (A tuşu) kullanın. A1'de süreler P2S'ten bir miktar uzun çıkar.

## Malzeme

| Parça | Malzeme |
|---|---|
| Neredeyse tüm parçalar | PLA |
| Yumuşak çene (`jaw_soft`), yumuşak ağız üstü (`soft_mouth_top`), birleşik tekerlekler (`combined_tire_TPU`) | **TPU 95A** önerilir |
| Ayak tabanları (`sole_left/right_ZEKALAND`) | PLA ya da daha iyi tutuş için TPU |
| Boyun, gövde tabanı, üst bacak takviye plakaları, rulman makarası | PLA yeterli; isteyen alüminyum CNC'ye de verebilir |

Projede bütün parçalar PLA olarak ayarlı. TPU basacağınız parçalara sağ tıklayıp filamenti TPU olarak değiştirin.

## ZEKALAND imzası

- **Ayak tabanları:** Alt yüzeye 0,6 mm derinlikte, 4 mm yüksekliğinde ZEKALAND yazısı kazılı. Ölçüler ve bağlantı noktaları orijinal tabanla aynı.
- **Sırt rozeti** (`zekaland_rozet.stl`, 52×14 mm): Gövdenin arkasına çift taraflı bantla ya da bir damla yapıştırıcıyla takılır. İki renk basmak için 1,6 mm'de filament değiştirin (Bambu'da katman kaydırıcısına sağ tık → "Filament değişimi ekle").
- **Sergileme kaidesi** (`zekaland_kaide.stl`, 150×100 mm): Robot sergilenirken üzerinde durur.

Bu dosyaları yeniden üretmek ya da yazıyı değiştirmek için: [`araclar/`](../araclar/).

## STL'den basarken dikkat

- STL'ler milimetre birimindedir.
- Destek, baskı yönü ve duvar sayısı yukarıdaki proje ayarlarıyla aynı tutulmalı. Servo yuvalarının ölçüsü duvar sayısından etkilenir.
- İlk olarak servo yuvası olan küçük bir parçayı (ör. `neck`) basıp servonun oturuşunu deneyin. Sıkıysa yatay genişleme (X-Y delik telafisi) ayarını -0,05 mm yapın.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
