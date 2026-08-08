#!/usr/bin/env python3
"""Inline screenshots into an artifact HTML file as data URIs.

Artifacts run under a strict CSP that blocks every external host, so an <img src="file.png">
silently shows nothing. Each {{IMG:name}} token in the source is replaced with a base64
JPEG. Captures are 2x retina, so they are downscaled here: full resolution would push the
page past the 16MB artifact ceiling for no visible gain at the sizes they are displayed.

Usage:  python3 tools/build-artifact.py <source.html> <output.html> [max_width]
"""

import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image

DIR = Path(__file__).resolve().parent.parent
SHOTS = DIR / "audit-screenshots"


def encode(name, max_width):
    path = SHOTS / f"{name}.png"
    if not path.exists():
        print(f"  MISSING {name}.png", file=sys.stderr)
        return ""
    im = Image.open(path).convert("RGB")
    if im.width > max_width:
        im = im.resize((max_width, round(im.height * max_width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    data = base64.b64encode(buf.getvalue()).decode()
    print(f"  {name}: {im.width}x{im.height}, {len(data)//1024}KB b64", file=sys.stderr)
    return f"data:image/jpeg;base64,{data}"


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    max_width = int(sys.argv[3]) if len(sys.argv) > 3 else 1400

    html = src.read_text(encoding="utf-8")
    names = sorted(set(re.findall(r"\{\{IMG:([A-Za-z0-9._-]+)\}\}", html)))
    print(f"inlining {len(names)} images…", file=sys.stderr)
    for n in names:
        html = html.replace(f"{{{{IMG:{n}}}}}", encode(n, max_width))

    left = re.findall(r"\{\{IMG:[^}]+\}\}", html)
    if left:
        print(f"  WARNING unresolved tokens: {set(left)}", file=sys.stderr)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    mb = out.stat().st_size / 1_048_576
    print(f"wrote {out} ({mb:.1f} MB)", file=sys.stderr)
    if mb > 15:
        print("  OVER BUDGET: artifact limit is 16MB. Lower max_width.", file=sys.stderr)


if __name__ == "__main__":
    main()
