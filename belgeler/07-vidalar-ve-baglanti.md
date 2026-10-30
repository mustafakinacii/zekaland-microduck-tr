# Bağlantı elemanlarının geri çıkarımı

> 🛒 Vida setleri, ısıl ankrajlar (heat-set insert) ve bastırma uçları, vida sabitleyici için satın alma linkleri: [Mekanik satın alma listesi](05-mekanik-satin-alma.md).

**Basitleştirilmiş Çince** · [English](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/fastener-reconstruction.en.md)

Resmi tarafta mekanik BOM ve vida listesi yoktur (HAT kartının elektronik BOM'u var ama yapısal parçaları içermez). Bu belge **47 STL ağının geometrik özelliklerinden geri çıkarılmış** sonuçtur.

## Yöntem

`scripts/analyze_holes.py`:

1. Yinelenen köşe noktaları birleştirilir, yüzey komşuluk grafiği kurulur
2. 35° dihedral açıdan kesilerek region-grow ile «düzgün yüzey parçaları» çıkarılır (keskin kenarda kopar)
3. Her parçaya silindir uydurulur — silindir yüzeyinin normalleri eksene diktir, dolayısıyla **eksen = normal kovaryans matrisinin en küçük özvektörüdür**
4. Köşe noktaları eksene dik düzleme izdüşürülür, Kåsa cebirsel daire uydurmasıyla çap bulunur, göreli artığı >%3 olanlar atılır
5. Normali eksen merkezine bakıyorsa = **delik**; merkezden uzaklaşıyorsa = mil/çıkıntı, hariç tutulur
6. Sarma açısı hesaplanır, yalnızca ≥300° olan tam daire delikler tutulur

47 parçanın hepsi taranmıştır, süre 2,5 saniye.

## Sonuç: Makine bir M2 vida sistemidir

Yapısal parçalardaki tam daire deliklerin çap dağılımı:

| Çap | Adet | Yorum |
|---|---|---|
| **Ø2,2** | **77** | **M2 geçiş deliği** (standart M2 boşluk 2,2–2,4) |
| **Ø4,4** | **28** | **M2 havşa/alıştırma deliği** (M2 alyan silindirik başı Ø3,8, alıştırma 4,0–4,5) |
| **Ø1,6** | **20** | **M2 diş açma ön deliği** (M2 standart ön delik tam olarak 1,6) |
| Ø2,4 | 22 | M2 gevşek geçmeli geçiş deliği |
| Ø2,0 | 12 | M2 sıkı geçmeli geçiş deliği |
| Ø2,7 / Ø2,8 | 20 | M2.5 geçiş deliği (az sayıda) |
| Ø4,8 | 10 | M2 alıştırma deliği (başka bir alıştırma derinliği) |
| Ø5,4 / Ø6,0 | 16 | Mil deliği / rulman yuvası, vida değil |

**Ø2,2 ile Ø4,4 çift olarak görülür**: `yaw2roll`, `leg`, `ankle_left`, `neck_pitch`, `yaw_roll_motion` üzerinde —
bu tipik bir **geçiş deliği + alıştırma deliği** kombinasyonudur, **M2 alyan başlı silindirik vida** kullanıldığını doğrular.

Çapraz doğrulama: `xl330.stl`'in kendisinde **Ø2,0×4 + Ø1,6×8** vardır, bu da Dynamixel XL330'un M2 montaj delikleriyle uyumludur.

## Parça parça delik istatistiği

Her ağın makinedeki gerçek referans sayısıyla ağırlıklandırılmıştır:

| Ağ | Makinedeki adet | M2 geçiş deliği | M2 ön delik | Alıştırma deliği |
|---|---|---|---|---|
| `xl330` | **×15** | 4 | 8 | — |
| `hip_l` | ×2 | 9 | — | 6 |
| `yaw2roll` | ×2 | 8 | — | 6 |
| `leg` | ×2 | 6 | — | 6 |
| `neck_pitch` | ×1 | 12 | — | 4 |
| `face_part` | ×1 | 10 | 4 | — |
| `ankle_left` / `ankle_right` | her biri ×1 | 5 | — | 5 |
| `yaw_roll_motion` | ×1 | 4 | — | 6 |
| `power_support` | ×1 | — | 8 | — |
| `left_shell` / `right_shell` | her biri ×1 | 7 / 6 | — / 1 | — |
| `bearing_roll` | ×2 | 4 | — | — |
| `neck` | ×2 | 4 | — | — |
| `upper_leg_rigidity_plate` | ×2 | 4 | — | — |
| `jaw` | ×1 | 5 | — | — |
| `trunk_base` | ×1 | 4 | — | — |
| `bottom_head_shell` / `top_head_shell` | her biri ×1 | 4 / 3 | — | — |
| `m12_lens_holder` | ×1 | 3 | — | — |

> **`xl330` 15 kez görünüyor** — makinede 15 servo var, 14 değil.
> 14'ü politika tarafından kontrol edilir, 15.'si gagayı/çeneyi sürer (`passive_*` bağlantılarında, eylem uzayına girmez).
> Bu, resmi README'deki "15 servos" ile uyumludur.

## Satın alma tahmini

- Tüm makinedeki M2 sınıfı delikler (Ø1,9–2,5 mm, sarma açısı ≥300°) **montaj kullanımına göre ağırlıklandırılınca toplam 237**,
  bunlardan 60'ı servo gövdesinde (15×4), 21'i rulman/PCB/pil gibi standart parçalarda, yapısal parçalarda yaklaşık 156

  > ⚠️ **Düzeltme (2026-09-04)**: Daha önce yazılan «213» yeniden hesaplanınca çıkmıyordu. Fark iki kaynaktan geliyor:
  > erken istatistik **montaj kullanımına göre ağırlıklandırılmamıştı** (`leg` aslında ×4, `hip_l`/`yaw2roll` vb. ×2),
  > ve **hiçbir MJCF'nin referans etmediği ağlar** da karışmıştı. Aşağıdaki delik çapı ve derinlik dağılım tabloları **ağırlıksız** esasa göredir
  > (her STL bir kez sayılır), iki tablo doğrudan toplanamaz.
- Servolar ve satın alınan parçalar (rulman/PCB/pil) düşülünce **yapısal parçalardaki geçiş deliği yaklaşık 146**

**Önerilen satın alma miktarı** (fire ve deneme montajı dahil):

| Ölçü | Önerilen adet | Kullanım |
|---|---|---|
| M2×4 alyan başlı silindirik | 60 | İnce duvarlı yerler (delik derinliği 0–3mm olanlar 79'dan 51'i) |
| M2×6 alyan başlı silindirik | 80 | Ana ölçü |
| M2×8 alyan başlı silindirik | 40 | Delik derinliği 3–5mm olan yerler (24/79) |
| M2×12 alyan başlı silindirik | 15 | Az sayıda derin delik (8–12mm, 4 yer) |
| M2 somun | 50 | Diş açılmayan yerler |
| M2 ısıl ankraj (heat-set insert) | 60 | Baskı parçalarında doğrudan diş açmanın yerine önerilir |
| M2.5×6 | 20 | Az sayıda Ø2,7 delik konumu |

Vida uzunlukları Ø2,2 deliklerin ölçülen derinlik dağılımından çıkarılmıştır: 0–3mm toplam 51, 3–5mm toplam 24, 8–12mm toplam 4.

## Rulmanlar

| Kaynak dosya | Ölçülen boyut |
|---|---|
| `seeed_bearing__configuration__22x16x4` | **dış çap 22 × iç çap 16 × kalınlık 4 mm** |
| `seeed_bearing__configuration_default` | dış çap 15 × iç çap ~10 × kalınlık 3 mm (makinede ×3 kullanılır) |

## ⚠️ Sınırlamalar

1. **Bu, simülasyon ağlarından geri çıkarılmıştır, mühendislik çizimi değildir.** Simülasyon ağları yalnızca dış şekli ve atalet değerlerini
   garanti eder; geçme toleransını ve diş ayrıntılarının eksiksizliğini garanti etmez.
2. **Baskı büzülmesi gerçek delik çapını değiştirir.** Ø2,2 tasarım deliği FDM'de genellikle 0,1–0,3mm küçük çıkar,
   gerçek montajdan önce mutlaka bir deneme parçası basıp doğrulayın.
3. **Alıştırma delikleri ile geçiş delikleri çift sayılmış olabilir** (aynı vidanın iki özelliği),
   vida adedi «geçiş deliği»ne göre alınır, alıştırma delikleri ayrıca sayılmaz.
4. **Tanınmayan özellikler**: dairesel olmayan delikler (oblong delik, özel şekilli yuva), sarma açısı <300° olan kısmi yaylar,
   çapı >14mm olan büyük açıklıklar istatistiğe dahil değildir.
5. Vida **uzunluğu** delik derinliğinden çıkarılmış bir aralıktır, ölçülmüş değer değildir.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
