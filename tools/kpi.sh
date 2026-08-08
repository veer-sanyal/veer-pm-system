#!/bin/bash
# Tripwire latency -- sunday.md:63 calls this "the system's core KPI" (the system exists to
# close loops). It was computed inside the monthly health check, inside /sunday, which ran 3
# times in 46 sessions and missed the Aug 2 first-Sunday entirely. So the KPI had never been
# computed while 22 sessions' worth of slugs sat in session-log.jsonl. This reads that data.
#
# Usage: tools/kpi.sh [days]   (default 30)
# Called by the session-start hook on the 1st of the month; runnable any time.
cd "$(dirname "$0")/.." || exit 1
days=${1:-30}
cutoff=$(date -v-"${days}"d '+%Y-%m-%d' 2>/dev/null || date -d "${days} days ago" '+%Y-%m-%d')

command -v jq >/dev/null || { echo "kpi: jq not installed"; exit 0; }

# One pass: every slug's first open date and first close date, then the deltas.
jq -rs --arg cutoff "$cutoff" '
  ( [ .[] | . as $s | ($s.ts[0:10]) as $d
      | ( ($s.tripwires_opened // [])[] | {slug:., opened:$d} ) ] | group_by(.slug)
      | map({key: .[0].slug, value: (min_by(.opened).opened)}) | from_entries ) as $open
  | ( [ .[] | . as $s | ($s.ts[0:10]) as $d
      | ( ($s.tripwires_closed // [])[] | {slug:., closed:$d} ) ] | group_by(.slug)
      | map({key: .[0].slug, value: (min_by(.closed).closed)}) | from_entries ) as $close
  | ( $open | to_entries | map(select(.value >= $cutoff)) ) as $recent
  | ( $recent | map(select($close[.key] != null)
        | { slug: .key,
            days: (((($close[.key] + "T00:00:00Z") | fromdate) - ((.value + "T00:00:00Z") | fromdate)) / 86400) } ) ) as $closed
  | ( $recent | map(select($close[.key] == null) | .key) ) as $open_now
  | if ($closed | length) == 0 then "tripwire latency: no slugs opened AND closed in the last \($cutoff | .[0:10])-to-now window"
    else
      "tripwire latency (opened since \($cutoff)): median \(($closed | map(.days) | sort | .[(length/2|floor)]))d over \($closed|length) closed | worst \(($closed | max_by(.days)).slug) at \(($closed | max_by(.days)).days)d"
    end
  , ( if ($open_now | length) > 0 then "still open: \($open_now | join(", "))" else empty end )
' session-log.jsonl 2>/dev/null || echo "kpi: could not parse session-log.jsonl"
