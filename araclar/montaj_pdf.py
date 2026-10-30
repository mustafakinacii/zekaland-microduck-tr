"""belgeler/18-montaj-kilavuzu.md dosyasından Türkçe montaj kılavuzu PDF'i üretir.

Kullanım:
  python araclar/montaj_pdf.py            # modeller/montaj-kilavuzu.pdf yazar
Gerekenler: pip install markdown · Google Chrome (başsız yazdırma için)
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

KOK = Path(__file__).resolve().parent.parent
KAYNAK = KOK / "belgeler/18-montaj-kilavuzu.md"
CIKTI = KOK / "modeller/montaj-kilavuzu.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm;
  @bottom-left { content: "Zekaland Robot Ördek · Montaj Kılavuzu"; font: 8pt 'Helvetica Neue', Arial, sans-serif; color: #8a94a6; }
  @bottom-right { content: counter(page) " / " counter(pages); font: 8pt 'Helvetica Neue', Arial, sans-serif; color: #8a94a6; } }
@page :first { margin: 0; @bottom-left { content: none; } @bottom-right { content: none; } }
* { box-sizing: border-box; }
body { font: 10.5pt/1.55 'Helvetica Neue', Arial, sans-serif; color: #1d2433; margin: 0; }
.kapak { height: 297mm; padding: 28mm 22mm; display: flex; flex-direction: column;
  background: linear-gradient(160deg, #0f2a4a 0%, #16457a 60%, #1f6fb2 100%); color: #fff; page-break-after: always; }
.kapak .marka { font-size: 13pt; letter-spacing: .35em; font-weight: 700; opacity: .9; }
.kapak h1 { font-size: 34pt; line-height: 1.1; margin: 18mm 0 4mm; border: 0; color: #fff; }
.kapak .alt { font-size: 14pt; opacity: .9; }
.kapak img { margin: 14mm auto 0; max-height: 120mm; max-width: 100%; background: #fff; border-radius: 6mm; padding: 6mm; }
.kapak .bilgi { margin-top: auto; font-size: 10pt; opacity: .85; line-height: 1.7; }
h1 { font-size: 20pt; color: #0f2a4a; }
h2 { font-size: 16pt; color: #0f2a4a; border-bottom: 2px solid #1f6fb2; padding-bottom: 2mm; margin-top: 8mm; page-break-after: avoid; }
h3 { font-size: 13.5pt; color: #fff; background: #16457a; padding: 2.5mm 4mm; border-radius: 2mm; margin: 0 0 4mm; page-break-after: avoid; }
section.bilesen { page-break-before: always; }
h4, p strong:only-child { color: #16457a; }
table { width: 100%; border-collapse: collapse; font-size: 9pt; margin: 3mm 0 5mm; page-break-inside: auto; }
th { background: #eaf1f9; color: #0f2a4a; text-align: left; }
th, td { border: 1px solid #d5deea; padding: 1.8mm 2.4mm; vertical-align: top; }
tr { page-break-inside: avoid; }
figure { margin: 3mm 0 5mm; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 105mm; object-fit: contain; }
figcaption { font-size: 8.5pt; color: #5b6578; margin-top: 1.5mm; font-style: italic; }
ul, ol { padding-left: 6mm; }
li { margin: 1mm 0; }
blockquote { margin: 3mm 0; padding: 2.5mm 4mm; background: #fff6e5; border-left: 3px solid #f0a500; }
hr { display: none; }
code { font: 9pt Menlo, monospace; background: #f2f4f8; padding: 0 1mm; border-radius: 1mm; }
"""


def html_uret(md_metin: str) -> str:
    # Repo içi gezinme satırlarını ve dipnotu PDF'ten çıkar
    md_metin = re.sub(r"^# .*\n", "", md_metin, count=1)
    md_metin = re.sub(r"^Görseller `modeller/.*\n", "", md_metin, flags=re.M)
    md_metin = re.sub(r"\n---\n\*Zekaland Robot Ördek belgeleri.*$", "\n", md_metin, flags=re.S)
    # Görseller → başlıklı figure, mutlak dosya yolu
    gorsel_klasor = KOK / "modeller/montaj-gorselleri"

    def figur(m):
        alt, yol = m.group(1), m.group(2)
        dosya = (KAYNAK.parent / yol).resolve()
        return f'\n<figure><img src="{dosya.as_uri()}"><figcaption>{alt}</figcaption></figure>\n'

    md_metin = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", figur, md_metin)
    govde = markdown.markdown(md_metin, extensions=["tables", "sane_lists"])
    # Her bileşen (h3) yeni sayfada başlasın
    parcalar = re.split(r"(?=<h3>)", govde)
    govde = parcalar[0] + "".join(f'<section class="bilesen">{p}</section>' for p in parcalar[1:])
    kapak_gorsel = (gorsel_klasor / "00-tam-montaj.png").as_uri()
    kapak = f"""
<div class="kapak">
  <div class="marka">ZEKALAND</div>
  <h1>Robot Ördek<br>Montaj Kılavuzu</h1>
  <div class="alt">Feetech HD-1910 sürümü · 15 alt grup</div>
  <img src="{kapak_gorsel}">
  <div class="bilgi">
    zekaland.com.tr · bilgi@zekaland.com.tr · Alanya<br>
    Belgeler ve modeller CC BY-NC-SA 4.0 · Katkıda bulunanlar: ATIF.md<br>
    github.com/mustafakinacii/zekaland-microduck-tr
  </div>
</div>"""
    return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Zekaland Robot Ördek — Montaj Kılavuzu</title><style>{CSS}</style></head><body>{kapak}{govde}</body></html>'


def main():
    html = html_uret(KAYNAK.read_text())
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        gecici = f.name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--allow-file-access-from-files", f"--print-to-pdf={CIKTI}", Path(gecici).as_uri()],
                   check=True, capture_output=True)
    print("yazıldı:", CIKTI)


if __name__ == "__main__":
    sys.exit(main())
