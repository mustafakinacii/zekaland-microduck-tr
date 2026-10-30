"""Zekaland Robot Ördek — ZEKALAND imzalı aksesuar parçalarını üretir.

Üretilenler (mm cinsinden STL):
  - zekaland_rozet.stl : 52×14 mm sırt rozeti, kabartma yazı (gövde arkasına yapıştırılır)
  - zekaland_kaide.stl : 150×100 mm sergileme kaidesi, zeminde kabartma yazı

Ayak tabanlarındaki ZEKALAND yazısı için: araclar/zekaland_3mf.py

Kullanım:
  python araclar/zekaland_parcalar.py <cikti_klasoru>
Gerekenler: pip install trimesh manifold3d shapely matplotlib mapbox_earcut networkx
"""
import sys
from pathlib import Path

import numpy as np
import trimesh
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from shapely.geometry import Polygon
from shapely.ops import unary_union

FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
YAZI = "ZEKALAND"


def yazi_poligonu(metin: str, yukseklik_mm: float):
    """Metni, yüksekliği verilen mm olan ve (0,0) etrafında ortalanmış shapely poligonuna çevirir."""
    path = TextPath((0, 0), metin, size=10, prop=FontProperties(fname=FONT))
    halkalar = [Polygon(p) for p in path.to_polygons() if len(p) >= 3]
    # Dış konturlar ve delikler (A, D harflerinin içi) çift-tek kuralıyla birleştirilir
    halkalar.sort(key=lambda p: -abs(p.area))
    sonuc = Polygon()
    for h in halkalar:
        h = h.buffer(0)
        sonuc = sonuc.symmetric_difference(h)
    sonuc = unary_union(sonuc)
    minx, miny, maxx, maxy = sonuc.bounds
    olcek = yukseklik_mm / (maxy - miny)
    from shapely import affinity
    sonuc = affinity.translate(sonuc, -(minx + maxx) / 2, -(miny + maxy) / 2)
    return affinity.scale(sonuc, olcek, olcek, origin=(0, 0))


def yazi_govdesi(metin, yukseklik_mm, derinlik_mm):
    poly = yazi_poligonu(metin, yukseklik_mm)
    parcalar = [trimesh.creation.extrude_polygon(g, derinlik_mm)
                for g in getattr(poly, "geoms", [poly])]
    return trimesh.util.concatenate(parcalar)



def rozet() -> trimesh.Trimesh:
    plaka = trimesh.creation.extrude_polygon(
        Polygon([(-26, -7), (26, -7), (26, 7), (-26, 7)]).buffer(-2).buffer(2), 1.6)
    yazi = yazi_govdesi(YAZI, 6.0, 1.0)
    yazi.apply_translation([0, 0, 1.6])
    return plaka.union(yazi, engine="manifold")


def kaide() -> trimesh.Trimesh:
    # Oval taban + 3 mm kenar (ördeğin ayakları ortadaki düz alana basar)
    elips = Polygon([(75 * np.cos(t), 50 * np.sin(t)) for t in np.linspace(0, 2 * np.pi, 180, endpoint=False)])
    govde = trimesh.creation.extrude_polygon(elips, 8.0)
    oyuk = trimesh.creation.extrude_polygon(elips.buffer(-4), 4.0)
    oyuk.apply_translation([0, 0, 5.0])
    govde = govde.difference(oyuk, engine="manifold")
    # Zeminin ön kısmına kabartma yazı (ayaklar ortada durur)
    yazi = yazi_govdesi(YAZI, 8.0, 1.2)
    yazi.apply_translation([0, -35.0, 5.0])
    return govde.union(yazi, engine="manifold")


def main():
    cikti = Path(sys.argv[1])
    cikti.mkdir(parents=True, exist_ok=True)
    parcalar = {
        "zekaland_rozet.stl": rozet(),
        "zekaland_kaide.stl": kaide(),
    }
    for ad, m in parcalar.items():
        m.export(cikti / ad)
        print(f"{ad}: {len(m.faces)} üçgen, su geçirmez={m.is_watertight}, boyut mm={m.extents.round(1)}")


if __name__ == "__main__":
    main()
