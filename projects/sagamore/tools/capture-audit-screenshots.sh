#!/bin/bash
# Capture evidence screenshots for the Sagamore website + social audits.
#
# Three things this gets right that the first version did not:
#
# 1. RETINA. --force-device-scale-factor=2 captures at 2x, so text stays sharp when the
#    image is scaled to a 6.5in column in Word. The first pass captured at 1x and then
#    compressed hard, which is why everything looked pixelated.
# 2. SENSIBLE ASPECT RATIOS. A full-page mobile capture is 375x6000 - a 16:1 sliver that is
#    useless in a document. Tall pages are captured whole and then CROPPED to the region
#    that carries the finding (see crop-sections.py).
# 3. NO SEARCH SHOTS. Google and DuckDuckGo serve this a bot challenge, and the machine
#    geolocates outside Indiana, so local results would be wrong even if it passed.
#
# It captures PUBLIC pages only. Facebook behind its login wall is a separate script.
#
# Usage:  bash projects/sagamore/tools/capture-audit-screenshots.sh
# Output: projects/sagamore/audit-screenshots/

set -u

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$DIR/audit-screenshots"
mkdir -p "$OUT"
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME"; exit 1; }

# The homepage answers at the bare domain, but every interior page is served from
# /htdocs/wordpress/ - sagamorebsa.org/join/ is a hard 404. That is the web-root
# misconfiguration the audit reports, and it broke this script on its first run.
SITE="https://sagamorebsa.org"
APP="https://sagamorebsa.org/htdocs/wordpress"

shot() {
  local name="$1" w="$2" h="$3" url="$4"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=2 \
    --window-size="${w},${h}" --virtual-time-budget=12000 \
    --screenshot="$OUT/$name.png" "$url" >/dev/null 2>&1
  if [ -s "$OUT/$name.png" ]; then
    local dim
    dim=$(sips -g pixelWidth -g pixelHeight "$OUT/$name.png" 2>/dev/null \
          | awk '/pixelWidth/{w=$2}/pixelHeight/{h=$2}END{print w"x"h}')
    printf '  ok   %-40s %-12s %s\n' "$name.png" "$dim" "$(du -h "$OUT/$name.png" | cut -f1)"
  else
    printf '  FAIL %-40s %s\n' "$name.png" "$url"
  fi
}

echo "== mobile 375px (the device the priority audience uses) =="
shot v2-web-mobile-homepage-fold  375 812  "$SITE/"
shot v2-web-mobile-header         375 300  "$SITE/"
shot v2-web-mobile-join-page      375 812  "$APP/join/"

echo "== tall captures (cropped afterwards by crop-sections.py) =="
shot RAW-mobile-homepage-full     375 6000 "$SITE/"
shot RAW-desktop-homepage-full    1440 5200 "$SITE/"

echo "== desktop =="
shot v2-web-desktop-homepage      1440 900  "$SITE/"
shot v2-web-desktop-join-page     1440 1400 "$APP/join/"
shot v2-web-desktop-cubscouts-price 1440 1800 "$APP/cub-scouts/"
shot v2-web-recharter             1440 1200 "$APP/recharter-information/"
shot v2-web-contact-us            1440 1600 "$APP/contact-us/"
shot v2-web-friends-of-scouting   1440 1800 "$APP/friends-of-scouting/"

echo "== the join target resolves (kills the Aug-4 403 claim) =="
shot v2-web-beascout-resolves     1440 900  "https://www.beascout.org/"

echo "== the dead link =="
shot v2-web-deadlink-campbuffalo  1200 600  "http://www.new.campbuffalo.com/"

echo "== social, public =="
shot v2-soc-linktree              500 1100 "https://linktr.ee/sagamore.scouting"
shot v2-soc-x-profile             1440 900  "https://x.com/SagamoreCouncil"
shot v2-soc-x-footer-link-404     1440 700  "https://twitter.com/SagamoreBSA"
shot soc-03-youtube-channel       1440 900  "https://www.youtube.com/@sagamore162"

echo
echo "Now run: python3 $(dirname "$0")/crop-sections.py"
echo "REVIEW EVERY IMAGE BY EYE. An error page or a login wall is not evidence."
