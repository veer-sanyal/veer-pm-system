#!/bin/bash
# Capture the logged-in Facebook evidence for the Sagamore social audit.
#
# WHY YOU ARE RUNNING THIS AND NOT CLAUDE:
# Claude's sandbox blocks it from copying or reading a Chrome profile directory,
# because such a directory holds live session cookies and that counts as credential
# handling. The restriction is on the agent, not on you. This script does nothing
# clever — it points headless Chrome at a profile you logged into yourself and takes
# screenshots. Read it before running it; it is short on purpose.
#
# PREREQUISITE: the throwaway Chrome window Claude opened, which you logged into.
# Its profile lives at the path in PROFILE below. CLOSE THAT WINDOW FIRST — Chrome
# will not let two instances share one profile, and closing it also flushes cookies
# to disk.
#
# Usage:  bash tools/capture-facebook-screenshots.sh
# Output: networking/audit-screenshots/v3-*.png
#
# AFTERWARDS: delete the profile. It contains a live Facebook session.
#   rm -rf "<PROFILE path printed at the end>"

set -u

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROFILE="/private/tmp/claude-501/-Users-veersanyal-Desktop-veer-pm-project/2bda583d-5c64-4f3b-a703-eabffe47de39/scratchpad/fbprofile"
OUT="$(cd "$(dirname "$0")/.." && pwd)/networking/audit-screenshots"
PAGE="https://www.facebook.com/141862791402"   # Sagamore Council page ID

mkdir -p "$OUT"
[ -d "$PROFILE" ] || { echo "Profile not found: $PROFILE"; exit 1; }

if pgrep -f "user-data-dir=$PROFILE" >/dev/null; then
  echo "That Chrome window is still open. Close it first, then re-run."
  exit 1
fi
rm -f "$PROFILE/Singleton"*

shot() {
  local name="$1" w="$2" h="$3" url="$4"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --user-data-dir="$PROFILE" --window-size="${w},${h}" \
    --virtual-time-budget=20000 \
    --screenshot="$OUT/$name.png" "$url" >/dev/null 2>&1
  if [ -s "$OUT/$name.png" ]; then
    printf '  ok   %-40s %s\n' "$name.png" "$(du -h "$OUT/$name.png" | cut -f1)"
  else
    printf '  FAIL %-40s %s\n' "$name.png" "$url"
  fi
}

echo "== council page =="
shot v3-soc-fb-page-header    1440 900  "$PAGE"
shot v3-soc-fb-reels-grid     1440 1600 "$PAGE/reels"
shot v3-soc-fb-page-full      1440 4000 "$PAGE"

echo "== satellite pages =="
shot v3-soc-fb-takachsin      1440 900  "https://www.facebook.com/TakachsinLodge"
shot v3-soc-fb-campbuffalo    1440 900  "https://www.facebook.com/CampBuffaloSagamore"
shot v3-soc-fb-wabashvalley   1440 900  "https://www.facebook.com/WabashValleyDistrict"

echo
echo "Done -> $OUT"
echo
echo "CHECK EVERY IMAGE BY EYE. A Facebook login wall or an empty skeleton is not evidence."
echo "Satellite page URLs above are guesses; any that FAIL or land on a 'page not found'"
echo "just need the real URL substituted."
echo
echo "THEN DELETE THE SESSION PROFILE:"
echo "  rm -rf \"$PROFILE\""
