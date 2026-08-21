#!/bin/sh
# Mechanical resume gate: dash rules + page count + ATS text extraction.
# Usage: tools/resume-check.sh <file.tex>   (expects the compiled .pdf beside it)
# Judgment checks (tense, bullet length, match-map coverage) belong to the reviewer agent.
set -e
tex="$1"; pdf="${tex%.tex}.pdf"; dir=$(dirname "$0")
fail=0
"$dir/no-emdash-check.sh" "$tex" || fail=1
pages=$(pdftotext "$pdf" - 2>/dev/null | grep -c $'\f' || true)
[ "$pages" -le 1 ] || { echo "PAGE CHECK FAILED: $((pages)) page breaks (must be 1-page)"; fail=1; }
txt=$(pdftotext "$pdf" - 2>/dev/null)
echo "$txt" | grep -q "@" || { echo "EXTRACTION FAILED: no email in extracted text"; fail=1; }
echo "$txt" | grep -qE "[0-9]{3}-[0-9]{3,4}" || { echo "EXTRACTION FAILED: no phone in extracted text"; fail=1; }
echo "$txt" | grep -qi "cid:" && { echo "EXTRACTION FAILED: cid: glyph garbage (font encoding broke ATS text)"; fail=1; }
[ $fail -eq 0 ] && echo "resume-check clean: dashes, 1 page, ATS extraction"
exit $fail
