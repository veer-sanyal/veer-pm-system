#!/bin/bash
# Build single-file, self-contained HTML versions of the two client audits, with every
# screenshot compressed and embedded as a data URI. The output opens anywhere, needs no
# image folder beside it, and never leaves this machine.
#
# Why: the audits are markdown with relative image paths. Emailed on their own, or dropped
# into SharePoint, every image breaks. This produces one file per audit that cannot break
# that way.
#
# WHAT IS INSIDE THESE FILES: the social audit's screenshots include a commenter's name and
# photo, and posts containing children. REDACT BEFORE SENDING TO A CLIENT — see
# MANUAL-SHOT-LIST.md.
#
# Usage:  bash tools/build-audit-html.sh
# Output: build/  (gitignored)

set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/networking"
BUILD="$ROOT/build"
TMP="$BUILD/.tmp"

command -v pandoc >/dev/null || { echo "pandoc not found (brew install pandoc)"; exit 1; }

rm -rf "$TMP"; mkdir -p "$TMP/audit-screenshots" "$BUILD"

echo "Compressing screenshots (max 1100px wide, JPEG q55)..."
for f in "$SRC/audit-screenshots"/*.png; do
  sips -s format jpeg -s formatOptions 55 -Z 1100 "$f" \
       --out "$TMP/audit-screenshots/$(basename "${f%.png}").jpg" >/dev/null 2>&1
done
echo "  $(ls "$TMP/audit-screenshots" | wc -l | tr -d ' ') images, $(du -sh "$TMP/audit-screenshots" | cut -f1)"

cat > "$TMP/style.css" <<'CSS'
body{max-width:56em;margin:2.5rem auto;padding:0 1.5rem;
 font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:#1a1a1a}
h1{font-size:2rem;border-bottom:2px solid #333;padding-bottom:.4rem}
h2{font-size:1.4rem;margin-top:2.5rem;border-bottom:1px solid #ddd;padding-bottom:.3rem}
h3{font-size:1.15rem;margin-top:1.8rem}
img{max-width:100%;height:auto;border:1px solid #d0d0d0;border-radius:4px;margin:1rem 0;display:block}
em{color:#555}
p>em:only-child{display:block;font-size:.9rem;background:#f7f7f7;border-left:3px solid #bbb;
 padding:.6rem .9rem;margin:-.5rem 0 1.5rem}
table{border-collapse:collapse;width:100%;margin:1.2rem 0;font-size:.94rem}
th,td{border:1px solid #ddd;padding:.5rem .7rem;text-align:left;vertical-align:top}
th{background:#f2f2f2}
code{background:#f2f2f2;padding:.12rem .35rem;border-radius:3px;font-size:.88em}
pre{background:#f7f7f7;padding:.8rem;border-radius:4px;overflow-x:auto;border:1px solid #e5e5e5}
pre code{background:none;padding:0}
blockquote{border-left:3px solid #ccc;margin-left:0;padding-left:1rem;color:#444}
hr{border:0;border-top:1px solid #e0e0e0;margin:2.5rem 0}
@media print{body{max-width:none}img{page-break-inside:avoid}}
CSS

for name in CLIENT-sagamore-website-audit CLIENT-sagamore-social-audit; do
  # Point the markdown at the compressed .jpg copies
  sed 's|\(audit-screenshots/[A-Za-z0-9._-]*\)\.png|\1.jpg|g' "$SRC/$name.md" > "$TMP/$name.md"
  pandoc "$TMP/$name.md" -f gfm -t html5 --standalone --embed-resources \
    --resource-path="$TMP" --css "$TMP/style.css" \
    --metadata title="Sagamore Council — ${name#CLIENT-sagamore-}" \
    -o "$BUILD/$name.html"
  echo "  $name.html -> $(du -h "$BUILD/$name.html" | cut -f1)"
done

rm -rf "$TMP"
echo "Done -> $BUILD"
