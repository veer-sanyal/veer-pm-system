#!/bin/sh
# Fails loudly if an outbound artifact contains em dashes or prose en dashes.
# Allowed: en dashes in date/number ranges ("Jun. 2025 -- Aug. 2025", "3--5").
# Usage: tools/no-emdash-check.sh <file...>   (run on .tex/.md/.txt before compiling/sending)
fail=0
for f in "$@"; do
  # U+2014 anywhere; LaTeX --- and prose " -- " between letters, outside comment lines
  bad=$(grep -nE '^[^%]*—' "$f"; grep -nE '^[^%]*---' "$f"; grep -nE '^[^%]*[A-Za-z] -- [a-z]' "$f")
  if [ -n "$bad" ]; then
    echo "EM-DASH CHECK FAILED: $f"; echo "$bad"; fail=1
  fi
done
[ $fail -eq 0 ] && echo "clean: no em dashes / prose en dashes"
exit $fail
