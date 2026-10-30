# Lisans ve Katkıda Bulunanlar

Zekaland Robot Ördek, açık kaynak projelerin üzerine kuruludur. Bu dosya, lisansların gerektirdiği atıfları ve Zekaland'in yaptığı değişiklikleri listeler.

## Üzerine kurulduğu projeler

| Eser | Sahibi | Lisans | Bu repoda |
|---|---|---|---|
| [Microduck](https://github.com/pollen-robotics/microduck): robot tasarımı, yazılım | Pollen Robotics / Hugging Face | Kod Apache-2.0, 3D modeller CC BY-NC-SA | Robotun temel tasarımı |
| [microduck-replica](https://github.com/fanhao375/microduck-replica): Feetech HD-1910 uyarlaması, dokümanlar, yazılım | fanhao375 ve katkıda bulunanlar | Dokümanlar CC BY-NC-SA 4.0, kod Apache-2.0 | `belgeler/` (Türkçe çeviri), `software/`, `tools/`, `scripts/` (commit `789ef5e`, 30 Ekim 2026) |
| [microduck-replica-cad](https://github.com/fanhao375/microduck-replica-cad): CAD çizimleri, baskı projesi, montaj kılavuzu | 机械行者Robo | CC BY-NC-SA 4.0 | `modeller/feetech/`, `modeller/montaj-gorselleri/`, `modeller/montaj-kilavuzu.pdf` (commit `a3ac692`) |
| [elec_RPI_Robot_HAT](https://github.com/pollen-robotics/elec_RPI_Robot_HAT): HAT devre kartı | Pollen Robotics | Apache-2.0 | Yalnızca bağlantı |

Yazılımın içindeki üçüncü taraf kütüphaneler (`software/studio/web/vendor/`, `software/studio/deps/`) kendi lisanslarıyla, kendi klasörlerinde durur.

## Zekaland'in değişiklikleri

- `belgeler/00–17`: Özgün dokümanların Türkçe çevirisi. Bağlantılar bu repodaki dosyalara yönlendirildi.
- `belgeler/12`: Baskı ve CAD belgesi bu repoya göre yeniden yazıldı.
- `belgeler/18`: Montaj kılavuzunun (PDF) Türkçe, görselli sürümü.
- `belgeler/19–20`, `ALISVERIS_LISTESI.md`, `ZEKALAND.md`, `README.md`: Zekaland'in özgün içeriği.
- `modeller/feetech/zekaland-robot-ordek-feetech.3mf`: Özgün baskı projesi. Ayak tabanlarına (`sole_left`, `sole_right`) 0,6 mm derinlikte ZEKALAND yazısı kazındı ve proje başlığı değişti. Diğer bütün parçalar ve baskı ayarları aynı.
- `modeller/feetech/stl/`: Aynı projeden dışa aktarılmış STL'ler.
- `modeller/montaj-gorselleri/`: Görsellerin dosya adları Türkçeleştirildi.
- `modeller/zekaland/`, `araclar/`: Zekaland'in özgün tasarımları ve araçları.
- `software/`, `tools/`, `scripts/`: Kod değiştirilmedi. Üçüncü taraf ikili dosyalar (Windows sürücüleri, Rufus) ve üretici veri sayfaları (PDF) dahil edilmedi.

## Lisanslar

- Belgeler, 3D modeller ve Zekaland'in özgün içeriği: **CC BY-NC-SA 4.0** ([LICENSE](LICENSE)). Ticari kullanım yasak, paylaşırken atıf ve aynı lisans zorunlu.
- Yazılım: **Apache 2.0** ([LICENSE-APACHE](LICENSE-APACHE), [NOTICE](NOTICE)).
- Sistem imajıyla gelen yürüme modelleri bu repoda yok; yazarlarının kişisel, ticari olmayan lisansıyla dağıtılıyor.

Özgün lisans metninin tam çevirisi: [belgeler/00-orijinal-lisans-ve-atif.md](belgeler/00-orijinal-lisans-ve-atif.md).
