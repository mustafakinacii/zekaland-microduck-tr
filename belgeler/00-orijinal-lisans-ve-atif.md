# Atıf ve Kaynaklar / Attribution

Bu depo, **Microduck'ın üçüncü taraf replika araştırmasıdır**; Pollen Robotics ile bağlantısı yoktur ve onun tarafından onaylanmamıştır.

## Üst akım (upstream) kaynakları

| Kaynak | Yazar | Lisans |
|---|---|---|
| [pollen-robotics/microduck_rl](https://github.com/pollen-robotics/microduck_rl) | Pollen Robotics | Kod Apache-2.0; **3B modeller CC BY-NC-SA** (resmi README'de "BY-SA-NC" yazılmış) |
| [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) | Pollen Robotics | Apache-2.0 |
| [LuwuDynamics/xgoduck_rl](https://github.com/LuwuDynamics/xgoduck_rl) deposundan 1910 M6 parametreleri ve ilgili yapılandırma referansı | LuwuDynamics | Apache-2.0 |
| [Rhoban/BAM](https://github.com/Rhoban/bam) aktüatör modeli ve tanımlama (identification) kütüphanesi (eğitim bağımlılığı) | Rhoban | Apache-2.0 |

Microduck, Pollen Robotics'in ticari bir ürünüdür; donanımı **kısmen açık kaynaklıdır**:

- **RPI Robot HAT kartı resmî olarak tamamen açık kaynak yapılmıştır** ([`elec_RPI_Robot_HAT`](https://github.com/pollen-robotics/elec_RPI_Robot_HAT), Apache-2.0, KiCad projesi ve üretim dosyalarını içerir)
- **`imu_to_dxl` kartı, mekanik parçaların düzenlenebilir CAD'i, komple BOM ve montaj dokümanları** ise yayımlanmamıştır

Bu depodaki tüm geometri bilgisi, upstream `microduck_rl` deposunda herkese açık olarak yayımlanan
**MJCF simülasyon modeli ve STL ağlarından (mesh)** gelir; elektronik sonuçlar `microduck` deposunun kaynak kodu, cihaz ağacı (device tree) ve yapılandırma dosyalarından çıkarılmıştır.

> Düzeltme (2026-09-03): Bu dosyada daha önce "donanımı açık kaynak değildir" denmişti; bu ifade yanlıştı — HAT kartı açık kaynaktır.

## Bu depodaki türetilmiş içerik

Aşağıdaki içerik, bu proje tarafından upstream'in herkese açık MJCF + STL dosyalarından üretilmiş veya derlenmiştir; **CC BY-NC-SA'nın türev eseridir**
ve bu nedenle aynı lisansla yayımlanır:

| Yol | İçerik | Upstream ile ilişkisi |
|---|---|---|
| `assembly-drawings/` | Tüm render görselleri ve patlatılmış (exploded) görünümler | Upstream MJCF + STL'den render alınarak üretildi |
| `software/training/` içindeki 3B ağlar | Eğitimde kullanılan simülasyon geometrisi | Upstream modelin kaynağı ve lisansı korunur, gerçek baskı dosyası değildir |
| `tools/servo-web/model/` | Web hata ayıklama panelinin görüntüleme modeli | Upstream MJCF / STL'den dönüştürüldü, en güncel gerçek CAD değildir |
| `software/studio/web/model/` | Studio web arayüzündeki 3B ördek | Upstream simülasyon modelinden dönüştürüldü, yalnızca dış şekil kaldı, en güncel gerçek CAD değildir |
| `docs/hole_analysis.json` | Delik konumu geometri analiz verisi | Upstream STL'den hesaplandı |

> **Model indirmelerinin taşınması (2026-09-28):** `print/` ve `cad/` artık [CAD deposuna](https://github.com/fanhao375/microduck-replica-cad) yönlendiren giriş açıklamalarına dönüştürüldü; eski tekil STL'ler, montaj STL'leri ve karşılaştırma tabloları, en güncel baskı parçası sanılmasın diye mevcut sürümden kaldırıldı. Git geçmişindeki eski modeller, upstream STL'lerin yeniden adlandırılmış, sınıflandırılmış veya montaj dönüşümü uygulanmış türev eserleri olmaya devam eder ve CC BY-NC-SA'ya tabidir; indirme kopyalarının kaldırılması geçmiş dosyaların yazarını ve lisansını değiştirmez.

**Bu projenin özgün içeriği:**

| Yol | İçerik | Lisans |
|---|---|---|
| `scripts/` | Render, dışa aktarma, delik konumu analizi vb. betikler | **Apache-2.0** |
| `tools/stl_viewer.html` | Bağımlılıksız WebGL STL görüntüleyici | **Apache-2.0** |
| `software/studio/` kodu | Microduck Studio web kontrol paneli (`web/vendor/`, `deps/`, `web/model/` hariç) | **Apache-2.0** |
| `software/image/` | Replika imajının derleme betikleri, ilk açılış ve ağ yapılandırma betikleri | **Apache-2.0** |
| `software/updater/` | İmzalı bileşen paketi derleme, özgün güncelleme motoru uyarlaması, web üzerinden yükseltme koordinasyonu ve ilk kurulum aracı | **Apache-2.0**; özgün updaterd Pollen Robotics'ten, kaynak 1fa8438 |
| `software/duck-echo/` kodu | Yerel R3 ses, kayıt ve müzikle etkileşim; derleme makinesinin özel anahtarlarını veya kullanıcı kayıtlarını içermez | **Apache-2.0**; harici Vosk modeli ve ARM64 bağımlılıkları kendi lisanslarına tabidir, listede kaynak ve hash korunur |
| `docs/*.md`, `*.md` | Tüm dokümanlar ve tersine mühendislik analiz metinleri | **CC BY-NC-SA 4.0** |
| `build-log/` fotoğrafları | Gerçek yapım fotoğrafları | **CC BY-NC-SA 4.0**, projeye katılanlar tarafından çekildi ve lisanslandı |
| `assets/` içindeki projeye özgü materyaller | Kapak, grup karekodu ve proje önizleme görselleri; aşağıdaki resmî kart görsellerini içermez | Aynısı |

## Resmî kart görselleri

Aşağıdaki iki görsel olduğu gibi alıntılanmıştır; kendi yazarlarını ve özgün lisanslarını korurlar, bu projenin dokümanlarına veya özgün materyallerine uygulanan CC BY-NC-SA lisansının kapsamında değildir:

| Yol | Kaynak ve yazar | Lisans |
|---|---|---|
| `assets/hw/radxa-zero3w-official.webp` | [Radxa ZERO 3 resmî dokümanı](https://docs.radxa.com/en/zero/zero3), Radxa Computer (Shenzhen) Co., Ltd. | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `assets/hw/rpi-robot-hat-official.png` | [Pollen Robotics resmî HAT deposu](https://github.com/pollen-robotics/elec_RPI_Robot_HAT), Pollen Robotics | [Apache-2.0](https://github.com/pollen-robotics/elec_RPI_Robot_HAT/blob/main/LICENSE) |

Özgün görsel adresi, sabitlenmiş sürüm ve sağlama değerleri [görsel kaynak kaydında](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/official-board-images.md) yer alır.

## Dahili eğitim projesi

[`software/training/`](../software/training/) eğitim projesini bütünüyle içerir; böylece replika yapan kişi tek indirmede
kodu, parametreleri ve simülasyon modellerini edinebilir. İçe aktarılan sabit sürüm ve değişiklik kapsamı için bkz. [UPSTREAM.md](../software/training/UPSTREAM.md).

- Pollen Robotics'in eğitim kodu, araçları ve özgün dokümanları **Apache-2.0** olarak kalır; bu dizine eklenen HD1910
  görevi, başlatma uyarlaması, testler ve açıklamalar da Apache-2.0'dır. Lisansın tam metni
  [`software/training/LICENSE`](../software/training/LICENSE) içindedir.
- Eğitim dizinindeki **3B modeller ve ağlar upstream'in CC BY-NC-SA beyanını korur**, kodun Apache lisansı bunları kapsamaz.
- LuwuDynamics'in `1910_m6.json` dosyası olduğu gibi korunmuştur; sabit kaynak, sağlama değerleri ve lisans kopyası
  [`software/training/src/mjlab_microduck/robot/hd1910/`](../software/training/src/mjlab_microduck/robot/hd1910/) altındadır.
  Bu proje bu parametreleri kendisi tanımlamadı (identification yapmadı); ileride bunlarla politika eğitilse de parametre referansı korunur.
- Rhoban/BAM, sürümü kilitlenmiş bağımlılık olarak kurulur; kaynağı ve lisansı korunur.

Yukarıdaki tabloda bu projenin dokümanlarına uygulanan CC BY-NC-SA lisansı, eğitim dizinindeki Apache dokümanlarını kapsamaz.

## Diğer üçüncü taraf yazılımlar

**Olduğu gibi dağıtılan üçüncü taraf yazılımlar:**

| Yol | İçerik | Kaynak | Lisans |
|---|---|---|---|
| `tools/飞特/` | Feetech FD hata ayıklama yazılımı 1.9.8.5 + CH340 sürücüsü | [gitee.com/ftservo/fddebug](https://gitee.com/ftservo/fddebug), 2026-09-11'de kopyalandı | **MIT** (FTServo 2024, LICENSE aynı dizinde) |
| `tools/rufus/` | Rufus 4.15 Windows x64 taşınabilir sürüm ve aynı sürümün kaynak kodu | [pbatard/rufus v4.15](https://github.com/pbatard/rufus/releases/tag/v4.15), 2026-10-25'te olduğu gibi indirildi | **GPL-3.0-or-later**; lisans, kaynak arşivi, sağlama değerleri ve kaynak kaydı o dizinde |
| `software/studio/web/vendor/` | Studio ön yüz kütüphaneleri: Preact, htm 3.1.1, three.js 0.160.0 | Her birinin resmî sürümü | Preact, three.js **MIT**, htm **Apache-2.0** (lisanslar `web/vendor/licenses/` içinde) |
| `software/studio/deps/` | Studio'nun Python bağımlılıkları (anyio, click, h11, idna, pyserial, sniffio, starlette, typing_extensions, uvicorn, wsproto) | pypi.org'dan orijinal wheel'ler; sürümler ve sağlama değerleri `deps/VERSIONS.txt` içinde | MIT / BSD-3-Clause / PSF-2.0 vb., her paketin lisansı kendi `*.dist-info` dizininde |

> Dokümanlarda alıntılanan upstream kaynak kodu parçaları (yorumlar, sabitler, register tanımları)
> `pollen-robotics/microduck` deposundandır ve **Apache-2.0** lisansına tabidir; alıntı yerlerinde dosya yolu belirtilmiştir.

## Tamamlayıcı depo: SolidWorks 3B çizimleri

[**fanhao375/microduck-replica-cad**](https://github.com/fanhao375/microduck-replica-cad)
düzenlenebilir SolidWorks / STEP dosyalarını, baskı dosyalarını ve 21 sayfalık montaj kılavuzunu tek yerden yönetir. Feetech ve XL330 sürümleri ayrı sunulur; dosya listesi o deponun ilgili yayınına göre belirlenir; ana depoda ayrı bir baskı modeli kopyası tutulmaz.

| İçerik | Yazar | Lisans |
|---|---|---|
| SolidWorks çizimleri, montaj kılavuzu, bileşen resimleri | **机械行者Robo** (Xiaohongshu 270594280 / Douyin 1852366168) | **CC BY-NC-SA 4.0** |

Bu çizimler, **upstream'in herkese açık STL ağlarına dayanılarak yeniden oluşturulmuş düzenlenebilir parametrik modellerdir**; CC BY-NC-SA'nın türev eseridir
ve bu nedenle aynı lisansla yayımlanır. **Telif hakkı yazarın kendisine aittir**, yeniden yayınlarda ve ikincil dağıtımda atıf korunmalıdır.
Çizimlerin bu depoya katılmayıp ayrı bir depoda tutulmasının nedeni, SolidWorks kaynak dosyalarının açılmış halde yaklaşık 340 MB tutmasıdır;
katılsalar bu depoyu her klonlayan bu boyutu taşımak zorunda kalırdı.

## Lisans adı hakkında not

Kurallı ad **CC BY-NC-SA 4.0**'dır (Atıf - Gayriticari - Benzer Paylaşım).
Upstream README'de "BY-SA-NC" yazılmıştır; bu depo o yazımı kullandığında aynı lisansı kasteder.

> Belirtmek gerekir ki: upstream `microduck_rl` deposunun `LICENSE` dosyasında yalnızca Apache-2.0 vardır;
> **CC koşulları yalnızca README'sindeki tek bir satırda geçer**. Bu deponun 3B modeller için daha katı olan CC BY-NC-SA'yı seçmesi
> temkinli bir yaklaşımdır — upstream saf Apache-2.0 olduğunu netleştirirse bu depo da buna göre gevşetilecektir.

## Uyumluluk beyanı

Bu depodaki tüm sonuçlar şunlardan elde edilmiştir:

- Pollen Robotics'in herkese açık yayımladığı **kaynak kodu ve cihaz ağacı** (`pollen-robotics/microduck`, Apache-2.0)
- Herkese açık **simülasyon modeli ve ağlar** (`pollen-robotics/microduck_rl`)
- Herkese açık **KiCad projesi** (`pollen-robotics/elec_RPI_Robot_HAT`, Apache-2.0)
- LuwuDynamics'in herkese açık yayımladığı **1910 M6 parametreleri ve ilgili yapılandırma** (`LuwuDynamics/xgoduck_rl`, Apache-2.0)
- Üreticilerin herkese açık komponent kılavuzları ve özellik sayfaları

**Hiçbir gizli/herkese açık olmayan malzeme kullanılmamış, gerçek ürün sökülmemiş, yayımlanmamış hiçbir tasarım dosyasına erişilmemiştir.**
`imu_to_dxl` kartının yazılımı (firmware) hiçbir açık kaynak depoda yer almaz; bu depo yalnızca onun veri yolu (bus) tarafında gözlemlenebilir davranışını yeniden oluşturmuştur.

## Ticari kullanım yasağı beyanı

Upstream 3B modeller **CC BY-NC-SA** ile lisanslıdır; bunların türev eserleri **ticari amaçla kullanılamaz**.
Bu depo yalnızca öğrenme, araştırma ve kişisel replika kullanımı içindir.

## Nasıl atıf yapılır

> Pollen Robotics'in Microduck modeline dayanır (CC BY-NC-SA)
> https://github.com/pollen-robotics/microduck_rl

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
