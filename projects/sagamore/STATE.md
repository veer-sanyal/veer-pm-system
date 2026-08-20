# Sagamore / Scouting America — STATE

Live state for the Purdue Daniels Externship client engagement. **This file owns it.** `memory.md`
carries a pointer and the pillar-level read only, the same contract stick-dev has (point, never
mirror). Two copies means one of them is lying by Tuesday.

Static brief (client, team, plan params, locked decisions): `externship-scouting-america.md`.
Narrative and reasoning trail: `PROGRESS.md` on the dates named below.

**Last updated: 2026-08-19 (night)** — **ENGAGEMENT CLOSED. Veer sent the thank-you + full
deliverables package to Bryon (Cc Izzy, Prisha) the night of Aug 19.**

## Phase

**CLOSED.** The final closing call RAN Mon Aug 17, 1:00 PM PT (Teams: Veer + Bryon + Izzy +
Prisha). Went well: Bryon grateful, said the work will actually be used to make improvements and
that the team's input "would have a lasting impact." Bryon asked for a final consolidated package
of all deliverables; it went out Aug 19 as the recipient-checked OneDrive set (8 link attachments)
riding the thank-you email. Nothing further is owed to the client. Residue: the team group-chat
close message is still staged and unsent (`networking/sends-2026-08-17.md`); the two stale Aug-4
Bryon Gmail drafts still need Veer's manual delete. No reply expected or required from Bryon.

Call honesty notes (Veer's own debrief, 2026-08-17): he did NOT go deep on the two audits — he
mentioned they exist as documents; Izzy did not walk her markup either. So **the ZIP and its email
carry the audit depth the call skipped** — the email should explicitly point Bryon at the two audit
reports as the place the recommendations are argued with numbers.

## Owner actions (Veer)

1. **`sagamore-final-zip` — REDEFINED 2026-08-19: the "ZIP" is Veer's OneDrive folder
   "Scouting America Consulting Resources"** (Purdue account, assembled by Veer Mon Aug 17 after
   the call; Bryon can download the whole set in one go). Package state as of 2026-08-19:
   - **Every file recipient-checked** (browser preview read-throughs + local leak scans): both
     `CLIENT-*` audits CLEAN, calendar xlsx CLEAN (flag: filename + A1 still say "- Draft" —
     Veer's call, matches what Bryon already has on SharePoint), Templates on Canva.zip = 9
     client-appropriate Canva PDF exports (contents unverified, names clean), Izzy's markup PDF
     kept (judgment call, see below).
   - **Added this session:** the two Bulk Create CSVs (were only on the Mac) and
     `CLIENT-sagamore-posting-toolkit.docx` — a client-voiced rewrite of the internal toolkit
     (source: `CLIENT-sagamore-posting-toolkit.md` here; build + loud-fail leak check:
     `tools/build-toolkit-docx.sh`). The internal `sagamore-posting-toolkit-2026-08-04.md` is
     NOT sendable and stays internal.
   - **Removed from the folder:** `Website feedback.docx` (Izzy's raw first-person notes, "I
     will draw a picture") — moved to OneDrive My-files root, not deleted.
   - Folder is still unshared; access travels with the email's OneDrive-link attachments when
     Veer sends. Thank-you email final text in `networking/sends-2026-08-17.md`. **Veer presses
     send.** Remaining before his click: his call on (a) Izzy's OK for her markup PDF going to
     Bryon, (b) Jiada staying in the "on behalf of" line, (c) the "- Draft" filename.
2. **UNCONFIRMED from the call — still need Veer:** did the Eagle-photo consent flag actually get
   said? (The templates question is ANSWERED: 9 Canva template exports exist, dated Aug 17 —
   the email's toolkit bullet now claims exactly what the folder holds.)
3. ~~Send the two audits to Izzy~~ **DONE (2026-08-15).**

## Open queue

- **`sagamore-final-zip` is the only live item** — see owner action 1. Everything else below is
  residue to clear when convenient.
- **Closing call RAN 2026-08-17, 1:00 PM PT** (confirmed Aug 13 on thread `19fe6a87fd853589`;
  Bryon formally Accepted the Outlook invite Aug 16). Outcome in Phase above. Call-prep one-pager:
  `call-prep-2026-08-17.html` — historical now.
- **Team close message staged** in `networking/sends-2026-08-17.md` — Veer wanted to say "good
  job" live but everyone dropped off when Bryon did; the group-chat message is the substitute.
- **Two stale Bryon drafts still in Gmail Drafts** (`r-2984936810873573256`, `r1375487513162206080`,
  both Aug 4), superseded twice over. Kill both, send neither. (Auto-delete attempt 2026-08-19 was
  blocked by the permission layer — Veer deletes them by hand, 10 seconds in Gmail Drafts.)
- Retired with the call: the final-call agenda (delivered), the `sagamore-package-monday` guard,
  the keep-alive vs membership-moving labelling question (presented on the call as the mix
  recommendation).

## What is delivered

- **Promotional calendar** — sent Tue Aug 4 2:08 AM ET from Purdue Outlook to Bryon + Izzy + Prisha
  (SharePoint xlsx, describe-and-offer tone). Bryon's reply is above. Built by
  `tools/add-observance-layer.py` (month-long and single-day observances incl. Scout Sunday layered
  onto the v0.2 posting calendar, with a `Status` column so it reads as a menu to approve, not a
  commitment), then run through `tools/make-client-copy.py`.
- **Two audits, done Aug 4, verified Aug 7** — browser-driven vision passes with screenshots,
  read-only, sourced to named publications. Internal: `sagamore-website-audit-2026-08-04.md` ·
  `sagamore-social-audit-2026-08-04.md`. Client versions: the two `CLIENT-*.md`.
  - **Website:** the word "join" appears nowhere in the mobile homepage text; cost is stated on none
    of 34 pages; the mobile header's largest text reads "BOY SCOUTS OF AMERICA"; the good `/join/`
    page has zero inbound links.
  - **Social (the stronger one):** 11 accounts not 6; Facebook Reels are an abandoned reach machine
    (best 9,300 views vs 3,512 followers, worst 206 on a link-led Reel); named-human-no-link scored
    58/55/77 against 2/10 for link posts; six satellite pages returned four reactions from 2,863
    followers; the Linktree has no Join and no Donate link; **parents comment their children's names
    and nobody replies** — the FOS list identifying itself.
  - **Retired by the Aug 7 verification pass** (`audit-verification-pass-2026-08-07.md`): the join-link
    403 was a bot-block, and "a parent cannot find the join path" was false. Do not re-raise either.
- **Izzy's half, received Aug 7** — handwritten markup over dated screenshots: homepage hero
  redesign, an event grid of equal-sized click-through photo cards, move the trading-post block,
  center the uniform section, an FAQ page, "still says Boy Scouts", blurry logo, bold the pre-camp
  swim-check line, format the two Cub camps consistently. Does not collide with Veer's.

## Build

- `tools/build-audit-html.sh` — self-contained HTML with screenshots embedded → `build/`. This is
  what the client receives.
- `tools/build-audit-docx.sh` — editable Word, styled from `audit-reference.docx`.
- `tools/capture-audit-screenshots.sh` / `capture-facebook-screenshots.sh` → `audit-screenshots/`.
- `build/` is gitignored: the source is versioned, the deliverable is one command. Do not commit it,
  and do not leave the only copy on the Desktop.
- **Before sending anything from here, read it as the recipient** — the send protocol in the root
  `CLAUDE.md` exists because this project is where it failed on 2026-08-04.
