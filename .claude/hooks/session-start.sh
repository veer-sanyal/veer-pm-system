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
  echo "STALE: memory.md was last reconciled $stamp_date -> run /reconcile before substantive work."
fi

echo "--- live tripwires (headers from memory.md) ---"
awk '/^\*\*Live tripwires/{f=1;next} /^---/{f=0} f && /^[0-9]+\./' memory.md | cut -c1-140

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
