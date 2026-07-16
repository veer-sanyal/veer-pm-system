#!/bin/bash
# SessionStart hook: print system state into context so no session starts blind.
# Surfacing layer only; memory.md stays authoritative. Auto-pushes existing
# commits; never auto-commits (commits need a real message, written in-session).
cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || cd "$(dirname "$0")/../.." || exit 0

echo "=== veer-pm-system status ($(date '+%Y-%m-%d %H:%M %Z')) ==="

stamp_line=$(grep -m1 "Last reconciled:" memory.md)
echo "$stamp_line"
stamp_date=$(echo "$stamp_line" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}' | head -1)
if [ "$stamp_date" != "$(date '+%Y-%m-%d')" ]; then
  echo "STALE: memory.md was last reconciled $stamp_date -> auto-run /reconcile as the first action (CLAUDE.md session-start rule), then answer."
fi

echo "--- live tripwires (headers from memory.md) ---"
awk '/^\*\*Live tripwires/{f=1;next} /^---/{f=0} f && /^[0-9]+\./' memory.md | cut -c1-140

# Makes silently-unpersisted study sessions visible (the Jun 23 / Jul 7 ambiguity).
[ -f context/study/state.json ] && echo "study state.json last write: $(date -r context/study/state.json '+%Y-%m-%d %H:%M')"

# Pillar 1 = STICK. Its failure mode is not idleness, it is effort routing to prose instead of the app.
# One number makes that visible without an audit. Baseline 2026-07-16: 1 of 250 commits touched app/.
stick="$HOME/Desktop/stick-dev"
if [ -d "$stick/.git" ]; then
  s_all=$(git -C "$stick" rev-list --count HEAD 2>/dev/null)
  s_app=$(git -C "$stick" rev-list --count HEAD -- app/ 2>/dev/null)
  s_all14=$(git -C "$stick" rev-list --count --since=14.days HEAD 2>/dev/null)
  s_app14=$(git -C "$stick" rev-list --count --since=14.days HEAD -- app/ 2>/dev/null)
  echo "STICK (Pillar 1): app/ commits ${s_app:-?}/${s_all:-?} all-time | ${s_app14:-?}/${s_all14:-?} last 14d | HEAD $(git -C "$stick" log -1 --format='%cs %s' 2>/dev/null | cut -c1-70)"
  # Fires on a pathological RATIO, not only on zero: 1-of-238 is the case this exists to catch.
  if [ "${s_all14:-0}" -gt 0 ] 2>/dev/null && [ $(( ${s_app14:-0} * 10 )) -lt "${s_all14:-0}" ] 2>/dev/null; then
    echo "  ^ only ${s_app14}/${s_all14} commits in 14d touched product code (<10%). Effort is routing to prose. That is the pattern running, not a quiet week -- name it, do not re-list it."
  fi
fi

if [ -n "$(git status --porcelain)" ]; then
  echo "GIT: uncommitted changes left by a previous session:"
  git status --porcelain | head -20
  echo "ACTION REQUIRED: first move this session = read this diff, fold it into a proper commit (real message), push. Before any other work."
fi

ahead=$(git rev-list --count @{u}..HEAD 2>/dev/null)
if [ "${ahead:-0}" -gt 0 ] 2>/dev/null; then
  if git push -q 2>/dev/null; then
    echo "GIT: auto-pushed $ahead commit(s) a previous session left unpushed."
  else
    echo "GIT: $ahead unpushed commit(s); auto-push failed (offline or auth) -- push manually this session."
  fi
fi

last_ts=$(tail -1 session-log.jsonl | sed -E 's/.*"ts": *"([^"]+)".*/\1/')
echo "Last telemetry line: ${last_ts:-none}"
last_commit_date=$(git log -1 --format=%cs 2>/dev/null)
if [ -n "$last_commit_date" ] && [ "${last_ts:0:10}" \< "$last_commit_date" ]; then
  echo "TELEMETRY GAP: last commit ($last_commit_date) is newer than the last telemetry line -- a session likely ended without its session-log.jsonl line; backfill one line noting it is a reconstruction."
fi
