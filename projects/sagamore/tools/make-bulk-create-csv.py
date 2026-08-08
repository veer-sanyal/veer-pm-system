#!/usr/bin/env python3
"""Turn the Posting Schedule tab into Canva Bulk Create data files.

Canva Bulk Create takes a CSV and generates one design per row, auto-matching CSV column names to
named text fields in the template. So the column names here are the contract: rename a column and
you have to rename the field in the Canva template to match.

Only the rows that actually need a graphic are exported. The `Real photo, no graphic` and
`Phone camera` rows are deliberately left out - those are the posts that carry the engagement, and
running them through a template would be a downgrade.

    python3 projects/sagamore/tools/make-bulk-create-csv.py ~/Downloads/"Sagamore Council Promotional Calendar - Draft.xlsx" ~/Downloads

Re-run after Bryon answers the open questions and the calendar changes.
"""
import csv
import os
import re
import sys

import openpyxl

# "Make it with" value -> (output filename, KICKER to use when the row has no prefix of its own)
TEMPLATES = {
    "Canva event template": ("sagamore-bulk-event-posts.csv", "COMING UP"),
    "Canva education template": ("sagamore-bulk-education-posts.csv", "DID YOU KNOW"),
}

# Prefixes the calendar generator writes, mapped to the urgency band shown on the design.
KICKERS = {
    "Push + last call": "LAST CALL",
    "Weekly ramp": "COMING UP",
    "Announce": "SAVE THE DATE",
    "Details + registration": "REGISTRATION OPEN",
    "Thanks + recap": "THANK YOU",
}

FIELDS = ["DATE", "KICKER", "HEADLINE", "STORY_ANGLE", "OBSERVANCE", "NOTE"]
ANGLE = re.compile(r"\s*\(story angle:\s*(.+?)\)\s*$")


def parse(row, default_kicker):
    date, _day, _slot, _bucket, post, _make, observance = row[:7]
    body, _, note = post.partition("|")
    prefix, sep, rest = body.partition(":")
    kicker = KICKERS.get(prefix.strip(), prefix.strip().upper()) if sep else default_kicker
    headline = (rest or body).strip()
    match = ANGLE.search(headline)
    return [
        date,
        kicker,
        ANGLE.sub("", headline).strip(),
        match.group(1).strip() if match else "",
        observance or "",
        note.strip(),
    ]


def main(workbook, outdir):
    rows = list(openpyxl.load_workbook(workbook)["Posting Schedule"].iter_rows(values_only=True))[1:]
    total = 0
    for make_with, (filename, default_kicker) in TEMPLATES.items():
        selected = [parse(r, default_kicker) for r in rows if r[5] == make_with]
        path = os.path.join(outdir, filename)
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)
            writer.writerows(selected)
        print(f"{path}: {len(selected)} rows")
        total += len(selected)
    skipped = len(rows) - total
    print(f"{skipped} rows skipped on purpose (real photo / phone camera - no template)")
    if total > 300:
        print("WARNING: Canva Bulk Create caps at 300 rows per run; split the file by month.")


def demo():
    """Self-check on the row shapes the calendar actually produces."""
    cases = [
        (("Aug 03, 2026", "Monday", "Event promo", "Event promotions",
          "Push + last call: Membership | Signals goes out", "Canva event template", None),
         ["Aug 03, 2026", "LAST CALL", "Membership", "", "", "Signals goes out"]),
        (("Aug 24, 2026", "Monday", "Event promo", "Event promotions",
          "Weekly ramp: Welcome to Scouting (story angle: last year's photos)",
          "Canva event template", None),
         ["Aug 24, 2026", "COMING UP", "Welcome to Scouting", "last year's photos", "", ""]),
        (("Aug 14, 2026", "Friday", "Community education", "Educating the community",
          "What Scouting teaches kids", "Canva education template", "Flag Day"),
         ["Aug 14, 2026", "DID YOU KNOW", "What Scouting teaches kids", "", "Flag Day", ""]),
    ]
    for row, expected in cases:
        default = TEMPLATES[row[5]][1]
        got = parse(row, default)
        assert got == expected, f"\n got {got}\nwant {expected}"
    print("demo ok")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--demo":
        demo()
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        sys.exit(__doc__)
