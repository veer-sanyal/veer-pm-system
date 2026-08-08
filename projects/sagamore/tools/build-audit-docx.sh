#!/bin/bash
# Build editable Word versions of the two client audits, images embedded.
#
# Why Word and not HTML: Izzy owns these audits and has to be able to edit them, and the
# client may want to comment. Pandoc emits real Word styles (Heading 1/2/3, Body Text,
# Table Grid), so restyling the whole document is a style change rather than 60 manual
# edits. Upload to Google Drive and it opens as a Google Doc with the styles intact.
#
# Image sizing: pandoc sizes images from pixel dimensions at --dpi. Captures are resized
# to 1100px wide and rendered at 170dpi, giving ~6.5in — exactly the text width of US
# Letter with 1in margins, so nothing overflows the page.
#
# WHAT IS INSIDE: the social audit's screenshots include a commenter's name and photo, and
# posts containing children. REDACT BEFORE SENDING TO A CLIENT — see MANUAL-SHOT-LIST.md.
#
# Usage:  bash tools/build-audit-docx.sh
# Output: build/  (gitignored)

set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT"
BUILD="$ROOT/build"
TMP="$BUILD/.tmp-docx"

command -v pandoc >/dev/null || { echo "pandoc not found (brew install pandoc)"; exit 1; }

rm -rf "$TMP"; mkdir -p "$TMP/audit-screenshots" "$BUILD"

echo "Resizing screenshots to 1100px..."
for f in "$SRC/audit-screenshots"/*.png; do
  sips -s format jpeg -s formatOptions 60 -Z 1100 "$f" \
       --out "$TMP/audit-screenshots/$(basename "${f%.png}").jpg" >/dev/null 2>&1
done
echo "  $(ls "$TMP/audit-screenshots" | wc -l | tr -d ' ') images, $(du -sh "$TMP/audit-screenshots" | cut -f1)"

# Reference doc carries the styles. Generate once, then reuse if the repo has a tuned one.
REF="$SRC/audit-reference.docx"
if [ ! -f "$REF" ]; then
  pandoc --print-default-data-file reference.docx > "$REF"
  echo "  created $REF (default styles; edit its styles in Word to restyle every build)"
fi

for name in CLIENT-sagamore-website-audit CLIENT-sagamore-social-audit; do
  sed 's|\(audit-screenshots/[A-Za-z0-9._-]*\)\.png|\1.jpg|g' "$SRC/$name.md" > "$TMP/$name.md"
  pandoc "$TMP/$name.md" -f gfm -t docx \
    --reference-doc="$REF" \
    --resource-path="$TMP" \
    --dpi=170 \
    --toc --toc-depth=2 \
    -o "$BUILD/$name.docx"
  echo "  $name.docx -> $(du -h "$BUILD/$name.docx" | cut -f1)"
done

rm -rf "$TMP"
echo "Done -> $BUILD"
