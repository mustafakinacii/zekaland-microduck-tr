"""Bambu Studio projesindeki ayak tabanlarına ZEKALAND yazısı kazır, diğer her şeyi aynı bırakır.

Ayrıca her parçayı, slicer'ı Bambu olmayanlar için ayrı STL olarak dışa aktarır.

Kullanım:
  python araclar/zekaland_3mf.py <girdi.3mf> <cikti.3mf> <stl_klasoru>
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

import numpy as np
import trimesh

sys.path.insert(0, str(Path(__file__).parent))
from zekaland_parcalar import YAZI, yazi_govdesi  # noqa: E402

NS = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"


def mesh_oku(model_xml: str, obj_id: str):
    blok = re.search(rf'<object id="{obj_id}"[^>]*>(.*?)</object>', model_xml, re.S).group(1)
    v = np.array(re.findall(r'<vertex x="([^"]+)" y="([^"]+)" z="([^"]+)"', blok), dtype=float)
    f = np.array(re.findall(r'<triangle v1="(\d+)" v2="(\d+)" v3="(\d+)"', blok), dtype=int)
    return trimesh.Trimesh(v, f, process=True)


def mesh_yaz(model_xml: str, obj_id: str, m: trimesh.Trimesh) -> str:
    verts = "\n".join(f'     <vertex x="{x:.6f}" y="{y:.6f}" z="{z:.6f}"/>' for x, y, z in m.vertices)
    tris = "\n".join(f'     <triangle v1="{a}" v2="{b}" v3="{c}"/>' for a, b, c in m.faces)
    yeni = f"<mesh>\n    <vertices>\n{verts}\n    </vertices>\n    <triangles>\n{tris}\n    </triangles>\n   </mesh>"
    desen = re.compile(rf'(<object id="{obj_id}"[^>]*>.*?)<mesh>.*?</mesh>', re.S)
    return desen.sub(lambda mt: mt.group(1) + yeni, model_xml, count=1)


def taban_kazi(m: trimesh.Trimesh) -> trimesh.Trimesh:
    """Dış taban yüzünü bulur, ZEKALAND'i dışarıdan okunacak şekilde 0,6 mm kazır."""
    v = m.vertices
    secim = None
    for i in np.argsort(m.facets_area)[::-1][:8]:
        n = m.facets_normal[i]
        p = v[m.faces[m.facets[i][0]][0]]
        disarida = np.mean((v - p) @ n > 0.3)  # yüzün önünde kalan köşe oranı
        # Dış yüz: parçanın neredeyse tamamı arkada kalır; ayrıca yüzün merkezi malzeme üstünde olmalı
        merkez = v[np.unique(m.faces[m.facets[i]])].mean(axis=0)
        if disarida < 0.01 and m.nearest.on_surface([merkez])[1][0] < 0.05:
            secim = i
            break
    n = m.facets_normal[secim]
    nokta = v[np.unique(m.faces[m.facets[secim]])]
    merkez = nokta.mean(axis=0)
    # Yazı yüzün uzun ekseni boyunca uzansın
    yerel = nokta - merkez
    yerel -= np.outer(yerel @ n, n)
    _, _, vt = np.linalg.svd(yerel, full_matrices=False)
    u = vt[0] - (vt[0] @ n) * n
    u /= np.linalg.norm(u)
    w = np.cross(n, u)
    genislik = np.ptp(yerel @ u)
    yazi = yazi_govdesi(YAZI, 1.0, 1.2)
    olcek = min(4.0, 0.65 * genislik / yazi.extents[0])  # yüzün %65'i, en fazla 4 mm yazı boyu
    yazi = yazi_govdesi(YAZI, olcek, 1.2)
    yazi.apply_translation([0, 0, -0.6])
    T = np.eye(4)
    T[:3, :3] = np.column_stack([u, w, n])  # dışarıdan bakınca soldan sağa okunur
    T[:3, 3] = merkez
    yazi.apply_transform(T)
    return m.difference(yazi, engine="manifold")


def main():
    girdi, cikti, stl_klasor = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    stl_klasor.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(girdi) as z:
        z.extractall(tmp)
    ayar = (tmp / "Metadata/model_settings.config").read_text()
    ana = (tmp / "3D/3dmodel.model").read_text()

    adlar = {}
    for oid, govde in re.findall(r'<object id="(\d+)">(.*?)</object>', ayar, re.S):
        ad = re.search(r'key="name" value="([^"]*)"', govde).group(1)
        kaynak = re.search(r'key="source_file" value="([^"]*)"', govde)
        if (len(ad) <= 2 or not re.search(r"[a-z]", ad)) and kaynak:
            ad = kaynak.group(1)  # isimsiz nesnede kaynak dosya adını kullan
        adlar[oid] = ad
    kullanilan = {}

    for oid, ad in adlar.items():
        govde = re.search(rf'<object id="{oid}"[^>]*>(.*?)</object>', ana, re.S).group(1)
        temiz = re.sub(r"[^\x00-\x7f]+", "", ad.replace("合体轮胎", "combined_tire_TPU"))
        temiz = re.sub(r"\.(stl|STEP|step|stp)$", "", temiz)
        temiz = re.sub(r"^\d+-", "", temiz)
        temiz = re.sub(r"_+", "_", temiz).replace("_-", "-").strip("_- ")
        kullanilan[temiz] = kullanilan.get(temiz, 0) + 1
        if kullanilan[temiz] > 1:
            temiz = f"{temiz}_{kullanilan[temiz]}"
        parcalar = []
        for yol, alt_id, tr in re.findall(r'p:path="([^"]+)" objectid="(\d+)"[^>]*transform="([^"]+)"', govde):
            dosya = tmp / yol.lstrip("/")
            xml = dosya.read_text()
            m = mesh_oku(xml, alt_id)
            if "sole_" in ad:
                m2 = taban_kazi(m)
                dosya.write_text(mesh_yaz(xml, alt_id, m2))
                # Bambu'nun tuttuğu yüz sayısını güncelle (onarım uyarısı çıkmasın)
                ayar = re.sub(rf'(<object id="{oid}">.*?)face_count="\d+"',
                              lambda mt: mt.group(1) + f'face_count="{len(m2.faces)}"', ayar, count=1, flags=re.S)
                ayar = re.sub(rf'(<object id="{oid}">.*?<mesh_stat )face_count="\d+"',
                              lambda mt: mt.group(1) + f'face_count="{len(m2.faces)}"', ayar, count=1, flags=re.S)
                print(f"{temiz}: ZEKALAND kazındı ({len(m.faces)} → {len(m2.faces)} üçgen, su geçirmez={m2.is_watertight})")
                m = m2
            t = np.array(tr.split(), dtype=float).reshape(4, 3)
            M = np.eye(4)
            M[:3, :3] = t[:3].T
            M[:3, 3] = t[3]
            parcalar.append(m.copy().apply_transform(M))
        if parcalar:
            tam = trimesh.util.concatenate(parcalar)
            tam.apply_translation(-tam.bounds[0] * [1, 1, 1])  # tablaya otur
            tam.export(stl_klasor / f"{temiz}.stl")
            if "sole_" in ad:
                (stl_klasor / f"{temiz}.stl").rename(stl_klasor / f"{temiz}_ZEKALAND.stl")

    # Proje başlığı
    ana = ana.replace('<metadata name="Title"></metadata>',
                      '<metadata name="Title">Zekaland Robot Ördek — Feetech HD-1910</metadata>')
    (tmp / "3D/3dmodel.model").write_text(ana)
    (tmp / "Metadata/model_settings.config").write_text(ayar)

    cikti.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(girdi) as zin, zipfile.ZipFile(cikti, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            zout.write(tmp / info.filename, info.filename)
    shutil.rmtree(tmp)
    print("yazıldı:", cikti)


if __name__ == "__main__":
    main()
