# Zekaland Araçları

| Betik | Ne yapar |
|---|---|
| `zekaland_3mf.py` | Bambu Studio projesindeki ayak tabanlarına ZEKALAND yazısı kazır, diğer her şeyi aynı bırakır; tüm parçaları ayrıca STL olarak dışa aktarır |
| `zekaland_parcalar.py` | Sırt rozeti ve sergileme kaidesini üretir |
| `montaj_pdf.py` | `belgeler/18-montaj-kilavuzu.md` dosyasından Türkçe PDF kılavuzu üretir (Google Chrome gerekir) |

Kurulum:

```bash
python3 -m venv .venv && .venv/bin/pip install trimesh manifold3d shapely matplotlib mapbox_earcut networkx scipy
```

Yazıyı değiştirmek için iki betiğin de kullandığı `YAZI` sabitini (`zekaland_parcalar.py`) düzenleyin. Yazı tipi macOS'taki Arial Rounded Bold'dur; başka sistemde `FONT` yolunu değiştirin.
