#!/bin/bash
# Capture evidence screenshots for the Sagamore Council website + social audits.
#
# Why this exists: the Aug 4 audit's screenshots were taken with ad-hoc headless Chrome
# commands that were never saved, so re-running the capture meant reconstructing them.
# There will be a v2 of these audits the moment Bryon answers anything, so the capture
# is a script now.
#
# Scope and its one hard limit: this captures PUBLIC pages only. Facebook's logged-out
# wall means Reels view counts, comment threads and page follower counts cannot be shot
# here — those are listed in MANUAL-SHOT-LIST.md for Veer to take from his own session.
# Do not "fix" that by loading a browser profile; cookie stores are credentials.
#
# Second limit worth knowing: Google and DuckDuckGo serve bot challenges to headless
# Chrome. Search-result screenshots are attempted and will simply produce a challenge
# page if blocked — check them before using. This is exactly the failure that put four
# false findings into the Aug 4 audit.
#
# Usage:  bash tools/capture-audit-screenshots.sh
# Output: networking/audit-screenshots/

set -u

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT="$(cd "$(dirname "$0")/.." && pwd)/networking/audit-screenshots"
mkdir -p "$OUT"

[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME"; exit 1; }

# shot <name> <width> <height> <url>
shot() {
  local name="$1" w="$2" h="$3" url="$4"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --window-size="${w},${h}" \
    --virtual-time-budget=8000 \
    --screenshot="$OUT/$name.png" "$url" >/dev/null 2>&1
  if [ -s "$OUT/$name.png" ]; then
    printf '  ok   %-42s %sx%s  %s\n' "$name.png" "$w" "$h" "$(du -h "$OUT/$name.png" | cut -f1)"
  else
    printf '  FAIL %-42s %s\n' "$name.png" "$url"
  fi
}

# The homepage answers at the bare domain, but every interior page is served from
# /htdocs/wordpress/ — sagamorebsa.org/join/ is a hard 404. This is the web-root
# misconfiguration the audit notes, and it bit this script on the first run.
SITE="https://sagamorebsa.org"
APP="https://sagamorebsa.org/htdocs/wordpress"

echo "== website: mobile 375x812 (the device the priority audience uses) =="
shot v2-web-mobile-homepage-fold      375 812  "$SITE/"
shot v2-web-mobile-header             375 400  "$SITE/"
shot v2-web-mobile-join-page          375 812  "$APP/join/"

echo "== website: full-page mobile (tall viewport, shows where Donate falls) =="
shot v2-web-mobile-homepage-full      375 6000 "$SITE/"
shot v2-web-mobile-join-full          375 4000 "$APP/join/"

echo "== website: desktop =="
shot v2-web-desktop-homepage          1440 900  "$SITE/"
shot v2-web-desktop-join-page         1440 1400 "$APP/join/"
shot v2-web-desktop-cubscouts-price   1440 2400 "$APP/cub-scouts/"

echo "== website: the join target actually resolves (kills the Aug-4 403 claim) =="
shot v2-web-beascout-resolves         1440 900  "https://www.beascout.org/"

echo "== social: public profiles =="
shot v2-soc-linktree                  414 1200 "https://linktr.ee/sagamore.scouting"
shot v2-soc-x-profile                 1440 900  "https://x.com/SagamoreCouncil"
shot v2-soc-x-footer-link-404         1440 900  "https://twitter.com/SagamoreBSA"
shot v2-soc-instagram-profile         1440 1200 "https://www.instagram.com/sagamorebsa/"

echo "== search: EXPECT BOT CHALLENGES. Inspect before trusting. =="
shot v2-search-cost-question          1440 1600 "https://duckduckgo.com/?q=how+much+does+scouting+cost"
shot v2-search-sagamore-join          1440 1600 "https://duckduckgo.com/?q=sagamore+council+join"

echo
echo "Done. Files in $OUT"
echo "REVIEW EVERY SEARCH SHOT BY EYE before citing it — a challenge page is not a result page."
