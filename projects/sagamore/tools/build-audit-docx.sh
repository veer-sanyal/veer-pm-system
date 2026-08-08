#!/bin/bash
# Build editable Word versions of the two client audits, images embedded.
#
# Why Word: Izzy owns these audits and has to edit them, and Bryon may want to comment.
# Pandoc emits real Word styles (Heading 1/2/3, Body Text, Image Caption), so restyling the
# whole document is a style change rather than sixty manual edits. Upload to Google Drive
# and it opens as a Google Doc with the styles intact.
#
# Image sizing is the part that needed thought. Captures are retina (2x), and they come in
# two shapes that cannot share one rule:
#   * landscape desktop shots  -> fit the 6.5in text column
#   * portrait phone shots     -> fit the page HEIGHT, or a 750x1624 capture scaled to
#                                 column width becomes 14 inches tall and eats two pages
# resize-for-docx.py applies that rule, then pandoc renders everything at 200dpi.
#
# WHAT IS INSIDE: the social audit includes a Facebook capture showing a commenter's name.
# Redact before sending to a client. See MANUAL-SHOT-LIST.md.
#
# Usage:  bash projects/sagamore/tools/build-audit-docx.sh
# Output: projects/sagamore/build/

set -eu
DIR="$(cd "$(dirname "$0")/.." && pwd)"
BUILD="$DIR/build"
TMP="$BUILD/.tmp-docx"

command -v pandoc >/dev/null || { echo "pandoc not found (brew install pandoc)"; exit 1; }

rm -rf "$TMP"; mkdir -p "$TMP" "$BUILD"
python3 "$DIR/tools/resize-for-docx.py" "$DIR/audit-screenshots" "$TMP/audit-screenshots"

REF="$DIR/audit-reference.docx"
[ -f "$REF" ] || python3 "$DIR/tools/make-audit-reference-docx.py"

for name in CLIENT-sagamore-website-audit CLIENT-sagamore-social-audit; do
  sed 's|\(audit-screenshots/[A-Za-z0-9._-]*\)\.png|\1.jpg|g' "$DIR/$name.md" > "$TMP/$name.md"
  pandoc "$TMP/$name.md" -f gfm -t docx \
    --reference-doc="$REF" --resource-path="$TMP" --dpi=200 \
    --toc --toc-depth=2 \
    -o "$BUILD/$name.docx"
  echo "  $name.docx -> $(du -h "$BUILD/$name.docx" | cut -f1)"
done

# An em dash surviving into a client document is a standing rule violation, so fail loudly.
for name in CLIENT-sagamore-website-audit CLIENT-sagamore-social-audit; do
  n=$(grep -o '—' "$DIR/$name.md" | wc -l | tr -d ' ')
  [ "$n" = "0" ] || echo "  WARNING: $name.md still has $n em dash(es)"
done

rm -rf "$TMP"
echo "Done -> $BUILD"
