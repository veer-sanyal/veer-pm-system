#!/usr/bin/env python3
"""Crop the tall page captures into sections a document can actually use.

A full-page mobile capture is 375x6000 CSS pixels. Placed in a Word column it becomes a
16:1 sliver about half an inch wide - technically present, completely unreadable. The
finding it carries (how far down the Donate button sits) is better served by a crop of
that region plus a stated measurement.

Captures come in at 2x device scale, so all offsets below are CSS pixels and get doubled.

Run:  python3 projects/sagamore/tools/crop-sections.py
"""

from pathlib import Path

from PIL import Image

DIR = Path(__file__).resolve().parent.parent / "audit-screenshots"
SCALE = 2  # --force-device-scale-factor=2

# (output name, source, top in CSS px, height in CSS px, caption of what should be visible)
CROPS = [
    ("v2-web-mobile-donate-position", "RAW-mobile-homepage-full", 4100, 800,
     "the Donate button, 4,384px down a 5,599px page"),
    ("v2-web-desktop-footer", "RAW-desktop-homepage-full", 4500, 700,
     "the footer trademark line"),
]


def main():
    for name, src, top, height, expect in CROPS:
        src_path = DIR / f"{src}.png"
        if not src_path.exists():
            print(f"  SKIP {name}: {src}.png not found - run the capture script first")
            continue
        im = Image.open(src_path)
        t, h = top * SCALE, height * SCALE
        if t >= im.height:
            print(f"  SKIP {name}: crop starts at {t}px but image is only {im.height}px tall")
            continue
        box = (0, t, im.width, min(t + h, im.height))
        out = DIR / f"{name}.png"
        im.crop(box).save(out)
        w, hh = Image.open(out).size
        print(f"  ok   {name}.png  {w}x{hh}  (expect: {expect})")

    print("\nLOOK AT THESE before using them. A crop at the wrong offset is a picture of nothing.")


if __name__ == "__main__":
    main()
