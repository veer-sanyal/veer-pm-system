#!/bin/bash
# Build the client posting-toolkit docx and fail loudly if any internal reference survives.
# Companion to make-client-copy.py: same send-protocol rule, different artifact.
# Usage: bash projects/sagamore/tools/build-toolkit-docx.sh
set -eu
DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$DIR/CLIENT-sagamore-posting-toolkit.md"
OUT="$DIR/build/CLIENT-sagamore-posting-toolkit.docx"

# Anything matching this in the source is a leak. Grep prints the hits, so the failure names itself.
if grep -nEi 'bryon|veer|prisha|izzy|jiada|\bv0\.[0-9]|\(team\)|TODO|tripwire|\bP[0-9]\b|—' "$SRC"; then
  echo "LEAK above: do not build, do not send." >&2
  exit 1
fi

mkdir -p "$DIR/build"
pandoc "$SRC" -f gfm -t docx --reference-doc="$DIR/audit-reference.docx" -o "$OUT"
echo "wrote $OUT"
