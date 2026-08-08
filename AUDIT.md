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

---

## Run 2 — 2026-08-07

**Why this run reads differently:** it audited Run 1 as much as the system. Run 1's five findings
were all correct and all fixed by hand. **Every one of the three size fixes regressed within 14
days, all to worse than the state that raised the finding.** That is the run's headline, and it
reframes Run 1's error as one of *placement*, not diagnosis.

| File | State that raised the finding | After Run 1 (Jul 24) | Run 2 (Aug 7) |
|---|---|---|---|
| `memory.md` (F4) | 16,471 B | ~1,370 words | **52,735 B / 8,450 words** |
| `PROGRESS.md` (F3) | 145,615 B | 78,037 B | **175,627 B** |
| `PROGRESS-archive.md` (F3) | — | 73,189 B | **73,189 B, byte-identical** |

**Root cause (P8):** the size budgets live in a table in `sunday.md`, and `/sunday` fired **3 times
in 46 logged sessions** (missing Jul 12 and Aug 2). `/reconcile` fires ~15x more often, writes
memory.md every time, and its prune instruction (`reconcile.md:62`) is prose with no number. The
invariant was placed in the least-run flow while the growth happened in the most-run one.

**System map (7 flows).** Deliberately recorded HERE and not in `docs/SYSTEM-MAP.md`: this system's
cardinal rule is one owner per fact, point never restate (CLAUDE.md ownership map). A standalone
map would be a second copy of the routing table and the commands' own contracts, and it would be
the next thing to rot. AUDIT.md is dated and historical by nature, which is the honest home for a
point-in-time map. This is a knowing deviation from the cairn audit skill's Stage 1.

Corroborated after the fact: a map already exists at `specs/system-map.tex` / `.pdf`, written
2026-07-15 and frozen since — it predates the founder-primary restatement, so it states the retired
goal. Built as a document rather than a maintained file, it rotted in 23 days. A third copy would
have rotted the same way.

| id | Trigger | Writes | Verification | Boundary | Fires |
|---|---|---|---|---|---|
| `session-start` | every session | `git push` | staleness · git-dirty · telemetry-gap · **(new) size budgets** | act | 46/46 |
| `reconcile` | daily / stale stamp | memory.md, PROGRESS.md, patterns.md, session-log | none | act | 15/46 |
| `sunday` | weekly | + ledgers, key-dates, **Google Calendar** | none | act | 3/46 (3 of 5 due) |
| `debrief` | post-call | alumni-tracker, ledgers, PROGRESS | none | act | 5/46 |
| `apply` | on demand | applications/ | Step 0 profile self-heal | act | 2/46 |
| `initialize` | wake | calendar, memory | none | act | 2/46 |
| `tutor` | on demand | study/state.json, ledgers | none | act | 2/46 |

### Findings (blast-ordered) and decisions

| # | Principle | Evidence | Decision | Status |
|---|---|---|---|---|
| G1 | P8/P9 | Table above. Budgets in `sunday.md:32-41` (3/46 fires) vs growth in `/reconcile` (15/46). | BUILD — move the memory.md + PROGRESS.md budgets into `session-start.sh`, same `ACTION REQUIRED` shape as the git-dirty check. | **APPLIED** |
| G2 | P14 | `CLAUDE.md:3` stated "landing a Summer 2027 PM internship" as the system's purpose; `direction.md:13` says "**Terminal: build a company**" (Veer, 2026-07-25; direction.md rewritten, CLAUDE.md never was). The router booted the retired goal for 13 days. | BUILD — rewrite the goal line, name direction.md as sole owner. | **APPLIED** |
| G3 | P2/P5 | memory.md append-only in practice: line 72 still asserted direction.md was wrong, 13 days after it was fixed. 6 "tripwires" = 21,426 of 52,735 B, written as narrative logs. Aug 5/6 reconcile text duplicated verbatim from `PROGRESS.md:543-591`. | BUILD — tripwires to `slug · state · next physical action · pointer`; drop duplication (PROGRESS.md + git hold it). | **APPLIED** (52,735 → 11,577 B; 8,450 → 1,756 words) |
| G4 | P1/P4 | `session-start.sh:9` echoed the `Last reconciled:` grep verbatim; that "line" had grown to **10,459 B** (three nested reconciles), i.e. 89% of the hook's 11,781 B output. memory.md was delivered twice per session. | BUILD — truncate the echo to 400 chars. | **APPLIED** (hook 11,781 → 2,253 B) |
| G5 | P16/P10 | Confirmed by targeted search, not absence of evidence: only `SessionStart` registered in `settings.json`; `size budget` appears in exactly one file, as prose; no `.github/workflows`, no tests, no validator. 7 of 7 flows `Verification: none` — collapsed to one system finding. The only non-gameable external signal (STICK `app/` ratio) measures a **different repo**. | PARK — G1 adds the first real post-condition; broader verification is a bigger change than the evidence warrants. Revisit if a second invariant regresses. | Noted |
| G6 | P18 | `sunday.md:63` names tripwire latency "the system's core KPI"; it was computed inside the monthly health check inside `/sunday`. First-Sunday-of-August (Aug 2) skipped ⇒ **never computed**, while 22 session-log lines carried the slugs. | BUILD — `tools/kpi.sh`, ungated. | **APPLIED** |
| G7 | P13 | `/sunday` is a 74-line ritual with a 40% skip rate (3 of 5 due), and the size budgets, the KPI, the freshness sweep, the profile sweep and the architecture watch were all placed inside it. Upkeep burden is the dominant abandonment cause. | BUILD (partial) — G1 and G6 move two load-bearing items out. The rest stays; do not respond to a skipped ritual by running it harder. | **PARTIAL** |
| G8 | P16 | Edge case, top 1 of 6 generated (5 suppressed as unreachable or low-blast). `session-start.sh:9-14` **failed open**: the stamp format is specified in prose only (`reconcile.md:62`), so one typo ⇒ empty grep ⇒ empty `stamp_date` ⇒ no staleness signal. | BUILD — fail closed: empty stamp now prints STALE. | **APPLIED** |
| G9 | P19 | `session-start.sh` auto-`git push` is `Boundary: act` on an outward-facing write with no gate. Blast radius low (private repo, own commits, existing commits only — never auto-commits). | PARK — log it, do not gate it. | Noted, no change |
| G10 | P14/P25 | `/tutor` fired 2/46 and `/initialize` 2/46, against memory.md's own record of **23+ days of zero study** and `study/state.json` untouched since Jul 3. This is an **uncovered objective**, not an orphan flow — deleting the flow does not fix Pillar 2. | PARK — a Sunday call on whether Pillar 2 is real, not an audit call. | Noted |
| F5 (Run 1) | P18 | Gameable STICK commit ratio. No new evidence; the ratio has since risen to ~31% with the gate still shut, i.e. still diagnosing honestly rather than being chased. | PARK (unchanged) | Noted |

**Rejected:** migration to a cairn instance — the architecture is sound and the defect was
enforcement placement; migration is far larger than the finding warrants.

**Reversed in-run:** `tripwires.json` was drafted as a REJECT ("`sunday.md:70` arms it with a
trigger and the trigger hasn't fired"). The first `tools/kpi.sh` run falsified that within minutes:
three live slugs for one thread. The armed trigger **has** fired and is now recorded at
`sunday.md:70`. Noted because it is the run's own evidence that measurement beats reading.

**Also produced by G6's first run, and worth carrying to the next audit:** median close latency is
1 day over 15 closed slugs, but 22 remain open including `stick-first-user-shown` across the whole
window. The median measures only loops that close. Do not report it alone.

### What was applied (files)

- **G2:** `CLAUDE.md:3` — founder-primary / PM-instrumental, direction.md named sole owner.
- **G1 + G8:** `.claude/hooks/session-start.sh` — memory.md word budget + PROGRESS.md byte budget
  with `ACTION REQUIRED`; fail-closed staleness.
- **G4:** same file — stamp echo truncated to 400 chars.
- **G3:** `memory.md` rewritten. Live-fact preservation spot-checked against the pre-edit file; the
  Aug 5/6 narrative is not lost (PROGRESS.md:543-591 + git).
- **G6:** `tools/kpi.sh` (new); `sunday.md:63` now calls it and warns against the median alone.
- **G1/G7:** `sunday.md:30` — the first two budgets explicitly delegated to the hook.
- Reversal: `sunday.md:70` — `tripwires.json` trigger marked FIRED.

**No `docs/RESEARCH.md` was produced:** no finding cleared the four-clause research bar (every one
resolved to measured local evidence). So there are no Refresh-by dates from this run, and the
caveat in the header about un-swept dates does not apply to Run 2.

**Suppressed:** 5 of 6 generated edge cases, as unreachable or low-blast.

**The test of this run is not the diff, it is Aug 21.** Run 1 looked identically successful on the
day it was applied. If `memory.md` is over 1,800 words two weeks from now, the hook is being
dismissed and the finding is a P19 rubber-stamp problem, not a size problem.
