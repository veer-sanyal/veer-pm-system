# AUDIT.md — /cairn:audit trail

Diagnostic of this system against the cairn level-zero doctrine (P-refs into the plugin's
`docs/PRINCIPLES.md`). This file is the record for the next audit's anti-re-litigation rule: a
finding rejected here only resurfaces on evidence newer than its rejection.

Note: this repo is NOT a cairn instance (no `manifest.json`) and there is no migration, so any
refresh-by dates created here (in `context/knowledge-freshness.md`) are swept by the `/sunday`
freshness pass added by F1 — not by a cairn governor. Re-audit remains manual.

---

## Run 1 — 2026-07-24

**North star (P14, user-authored, unchanged):** land a Summer 2027 PM internship (Google APM or
equiv); the system's job is to drive action over insight. It IS measured — telemetry
(`session-log.jsonl`) + the SessionStart hook's STICK `app/`-vs-prose commit ratio (a
non-gameable git read, P16). Rare for an audited system; treated as the asset to protect.

**Strengths (verified, left untouched):** SessionStart hook as deterministic enforcement (P9) —
staleness surfacing, git auto-push, telemetry-gap detection, external metric; single-owner
ownership map (P2/P4); Gmail-draft-only / Calendar-write blast-radius split (P19); stick-dev as
self-owned single-writer subsystem (P20).

### Findings (blast-ordered) and decisions

| # | Principle | Evidence | Decision | Status |
|---|---|---|---|---|
| F1 | P22 | ~10 `context/` research docs mtime-frozen 2026-06-15, no verified-as-of / refresh trigger; recruiting timing is load-bearing (git log: "Salesforce deadline ~1hr — likely closed"). | BUILD — tier LIVING/STATIC in a freshness ledger + weekly sweep. | **APPLIED** |
| F2 | Data-path (Stage 2) / P16 | Hook literally prints "iMessage/WhatsApp still blind"; real state (Trice/Naveen WhatsApp, team iMessage, family thread) sits at ladder rung 5; `/reconcile` only annotated the blindness. | BUILD — add an active manual-capture ask to `/reconcile`. | **APPLIED** |
| F3 | P5 / P2 | `PROGRESS.md` 145,615 B spanning Jun 9→now; `PROGRESS-archive.md` 5,536 B, last entry Jun 4 — the documented monthly roll (CLAUDE.md, sunday.md) unrun ~7 weeks. | BUILD — roll June into archive. | **APPLIED** (145,615→78,037 B) |
| F4 | P1 / P4 | `memory.md` self-caps "~1,500 words", measured 16,471 B ≈ ~2,500 words (~65% over); protocol-mandated read every session. | BUILD — compress to pointers. | **APPLIED** (→1,370 words; hook parse verified) |
| F5 | P18 | STICK commit-ratio is surfaced as *the* signal and is a gameable proxy (pad `app/` with trivial commits); currently working as a diagnostic (low ratio reveals the true problem). | PARK — prospective, watch-item; add a guardrail note only if the ratio is ever chased. | Noted, no change |

### What was applied (files)

- **F1:** created `context/knowledge-freshness.md`; added a "Knowledge freshness" sweep to
  `.claude/commands/sunday.md`; added a routing pointer in `CLAUDE.md`; indexed in `file-index.md`.
- **F2:** rewrote step 4 of `.claude/commands/reconcile.md` (iMessage + WhatsApp → active ask).
- **F3:** moved June entries `PROGRESS.md` → `PROGRESS-archive.md`.
- **F4:** rewrote `memory.md` (reasoning trails → pointers; all live tripwires + facts preserved).

Every fix executes discipline the system already documented but wasn't running; no new subsystem.
