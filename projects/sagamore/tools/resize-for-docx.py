#!/usr/bin/env python3
"""Resize retina captures for a Word page, respecting whether they are portrait or landscape.

Pandoc sizes an image from its pixel dimensions at the given --dpi. At 200dpi a US Letter
page with 1in margins gives a 6.5in column (1300px) and about 7.5in of usable height
(1500px). One rule cannot serve both shapes:

  * A landscape desktop capture wants to fill the column width.
  * A portrait phone capture (750x1624) scaled to column width becomes 14 inches tall and
    swallows two pages. It wants to be sized by height instead.

The earlier version used `sips -Z`, which constrains the LARGEST dimension. On a tall
screenshot that is the height, so phone captures came out as narrow unreadable slivers.
That is the bug this file exists to fix.

Usage: python3 resize-for-docx.py <src-dir> <out-dir>
"""

import sys
from pathlib import Path

from PIL import Image

COLUMN_PX = 1300   # 6.5in at 200dpi
HEIGHT_PX = 1500   # ~7.5in at 200dpi, leaves room for a caption
PORTRAIT_RATIO = 1.3


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)

    for f in sorted(src.glob("*.png")):
        im = Image.open(f).convert("RGB")
        ratio = im.height / im.width
        if ratio > PORTRAIT_RATIO:
            h = min(HEIGHT_PX, im.height)
            w = round(im.width * h / im.height)
            shape = "portrait"
        else:
            w = min(COLUMN_PX, im.width)
            h = round(im.height * w / im.width)
            shape = "landscape"
        im.resize((w, h), Image.LANCZOS).save(out / f"{f.stem}.jpg", "JPEG",
                                              quality=88, optimize=True)
        print(f"  {f.stem:<40} {shape:<9} {w}x{h}  ({w/200:.1f}in x {h/200:.1f}in)")


if __name__ == "__main__":
    main()
