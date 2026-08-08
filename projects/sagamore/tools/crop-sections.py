#!/usr/bin/env python3
"""Crop tall captures to the region that carries the finding, and redact private identities.

Two jobs, both learned the hard way.

CROPPING. The full Facebook page capture is 1440x4000. Dropped into a Word column whole it
renders 2.7in wide and nothing is legible. An earlier attempt cropped the tall *website*
captures by measured pixel offset and landed on the wrong region twice, because a tall
viewport reflows the page. So: only crop captures whose layout you have actually looked at,
and look at the result before using it.

REDACTION. The Facebook crop shows a real parent's name and profile photo under a public
post. The evidence is that a parent asked an unanswered question, not who she is. For a
youth-serving organisation's audit, publishing her identity would be the same class of
mistake the audit itself flags about the Eagle Scout photo.

Run:  python3 projects/sagamore/tools/crop-sections.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

DIR = Path(__file__).resolve().parent.parent / "audit-screenshots"

# name, source, (left, top, right, bottom) in source pixels, redaction boxes, what to expect
JOBS = [
    (
        "v3-soc-fb-link-penalty",
        "v3-soc-fb-page-full",
        (620, 780, 1340, 2000),
        # The commenter's avatar and display name, in coordinates of the CROPPED image.
        [(20, 465 - 780 + 780 - 780 + 0, 0, 0)],  # placeholder replaced below
        "membership post 31/19/27 above the Buffalo Stampede video post at 1 reaction",
    ),
]

# Redaction boxes are fiddly to express relative to a crop, so state them explicitly here in
# SOURCE coordinates and let the code translate.
REDACT_IN_SOURCE = {
    # This crop ends above the comment thread, so it contains no private identity and needs
    # no redaction. An earlier box here landed on the council's own event graphic and
    # defaced it, which is the argument for looking at the output every time.
    # If the crop is ever extended downward to include the comments, the commenter's avatar
    # and display name must be blurred before it goes anywhere.
}


def main():
    for name, src, box, _unused, expect in JOBS:
        src_path = DIR / f"{src}.png"
        if not src_path.exists():
            print(f"  SKIP {name}: {src}.png not found")
            continue

        im = Image.open(src_path).convert("RGB")
        left, top, right, bottom = box
        right = min(right, im.width)
        bottom = min(bottom, im.height)
        if left >= right or top >= bottom:
            print(f"  SKIP {name}: crop box outside the {im.width}x{im.height} image")
            continue

        # Redact in source space first, so the numbers stay readable and checkable.
        draw_target = im.copy()
        for (rx1, ry1, rx2, ry2) in REDACT_IN_SOURCE.get(name, []):
            rx2, ry2 = min(rx2, im.width), min(ry2, im.height)
            if rx1 >= rx2 or ry1 >= ry2:
                continue
            region = draw_target.crop((rx1, ry1, rx2, ry2)).filter(ImageFilter.GaussianBlur(14))
            draw_target.paste(region, (rx1, ry1))
            d = ImageDraw.Draw(draw_target)
            d.rectangle([rx1, ry1, rx2 - 1, ry2 - 1], outline=(150, 150, 150), width=1)

        out = DIR / f"{name}.png"
        draw_target.crop((left, top, right, bottom)).save(out)
        w, h = Image.open(out).size
        print(f"  ok   {name}.png  {w}x{h}   expect: {expect}")

    print("\nLOOK AT THESE. Check the crop is the right region AND that the redaction covers"
          "\nthe name and face completely before any of it reaches a client.")


if __name__ == "__main__":
    main()
