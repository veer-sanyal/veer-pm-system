#!/usr/bin/env python3
"""Build the Word reference document that styles both client audits.

Pandoc copies this file's styles into every .docx it generates, so all polish lives here
rather than in the converted output. That is the point: Izzy can restyle the entire
document by changing a style in Word, and a rebuild will not undo her edits to content.

Fonts are deliberately Calibri and Calibri Light — Word's own defaults. A prettier pairing
that is not installed on the client's machine silently substitutes into something worse.

Run:  python3 tools/make-audit-reference-docx.py
Out:  networking/audit-reference.docx
"""

import re
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "networking" / "audit-reference.docx"
TMP = ROOT / "build" / ".ref"

INK = "1F2A37"       # near-black, softer than pure black on paper
ACCENT = "1B4965"    # deep slate blue for headings
MUTED = "5A6572"     # captions and secondary text


def build():
    TMP.exists() and shutil.rmtree(TMP)
    TMP.mkdir(parents=True)
    base = TMP / "base.docx"
    with open(base, "wb") as f:
        subprocess.run(
            ["pandoc", "--print-default-data-file", "reference.docx"],
            stdout=f, check=True,
        )

    unpacked = TMP / "unpacked"
    with zipfile.ZipFile(base) as z:
        z.extractall(unpacked)

    styles_path = unpacked / "word" / "styles.xml"
    xml = styles_path.read_text(encoding="utf-8")

    # Body font everywhere, headings in Calibri Light.
    xml = xml.replace(
        '<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorEastAsia"'
        ' w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>',
        '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>',
    )

    def restyle(style_id, *, size=None, color=None, before=None, after=None,
                bold=None, italic=None, font=None):
        """Rewrite one style's rPr/pPr bits. Sizes are half-points, spacing in twentieths."""
        nonlocal xml
        m = re.search(
            r'(<w:style [^>]*w:styleId="%s".*?</w:style>)' % re.escape(style_id),
            xml, re.S,
        )
        if not m:
            return
        block = m.group(1)

        if size is not None:
            block = re.sub(r'<w:sz w:val="\d+"/>', "", block)
            block = re.sub(r'<w:szCs w:val="\d+"/>', "", block)
        if color is not None:
            block = re.sub(r'<w:color [^/]*/>', "", block)

        run_bits = ""
        if font:
            run_bits += f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
        if bold is not None:
            block = re.sub(r'<w:b/>|<w:b w:val="[^"]*"/>', "", block)
            run_bits += "<w:b/>" if bold else ""
        if italic:
            run_bits += "<w:i/>"
        if color is not None:
            run_bits += f'<w:color w:val="{color}"/>'
        if size is not None:
            run_bits += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'

        if run_bits:
            if "<w:rPr>" in block:
                block = block.replace("<w:rPr>", "<w:rPr>" + run_bits, 1)
            else:
                block = block.replace("</w:style>", f"<w:rPr>{run_bits}</w:rPr></w:style>")

        if before is not None or after is not None:
            block = re.sub(r'<w:spacing [^/]*/>', "", block)
            sp = "<w:spacing"
            if before is not None:
                sp += f' w:before="{before}"'
            if after is not None:
                sp += f' w:after="{after}"'
            sp += ' w:line="276" w:lineRule="auto"/>'
            if "<w:pPr>" in block:
                block = block.replace("<w:pPr>", "<w:pPr>" + sp, 1)
            else:
                block = block.replace("<w:rPr>", "<w:pPr>" + sp + "</w:pPr><w:rPr>", 1)

        xml = xml.replace(m.group(1), block)

    restyle("Title",    size=56, color=ACCENT, font="Calibri Light", bold=False, after=120)
    restyle("Heading1", size=32, color=ACCENT, font="Calibri Light", bold=False, before=400, after=140)
    restyle("Heading2", size=26, color=ACCENT, font="Calibri Light", bold=False, before=320, after=120)
    restyle("Heading3", size=23, color=INK,    font="Calibri",       bold=True,  before=260, after=100)
    restyle("BodyText", size=22, color=INK,                                       after=160)
    restyle("FirstParagraph", size=22, color=INK, after=160)
    restyle("Compact",  size=22, color=INK,                                       after=80)
    # Pandoc puts image captions in this style; ours are the italic lines under each shot.
    restyle("ImageCaption", size=19, color=MUTED, italic=True, after=240)
    restyle("Caption",      size=19, color=MUTED, italic=True, after=240)

    styles_path.write_text(xml, encoding="utf-8")

    # US Letter, 1in margins — stated explicitly. Pandoc's default reference carries no
    # page setup, so Word falls back to its own locale default (A4 in much of the world).
    # The screenshots are sized for Letter's 6.5in text column, so on A4 they would overrun.
    doc_path = unpacked / "word" / "document.xml"
    doc = doc_path.read_text(encoding="utf-8")
    sect = (
        '<w:sectPr>'
        '<w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"'
        ' w:header="720" w:footer="720" w:gutter="0"/>'
        '<w:cols w:space="720"/>'
        '<w:docGrid w:linePitch="360"/>'
        '</w:sectPr>'
    )
    if "<w:pgSz" in doc:
        doc = re.sub(r'<w:pgSz[^>]*>', '<w:pgSz w:w="12240" w:h="15840"/>', doc)
        doc = re.sub(
            r'<w:pgMar[^>]*>',
            '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"'
            ' w:header="720" w:footer="720" w:gutter="0"/>',
            doc,
        )
    else:
        doc = re.sub(r'<w:sectPr\b[^>]*/>', "", doc)          # drop an empty one if present
        doc = doc.replace("</w:body>", sect + "</w:body>")
    doc_path.write_text(doc, encoding="utf-8")

    OUT.exists() and OUT.unlink()
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(unpacked.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(unpacked).as_posix())

    shutil.rmtree(TMP)
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build()
