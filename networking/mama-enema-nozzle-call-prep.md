# Call prep — Mama (Bangalore), external-sealing enema nozzle prototype

**Context:** Mama (doctor, Bangalore, VC-funded) sent a 5-page prototype spec Tue Jul 21 (WhatsApp): "Adult External-Sealing Enema Nozzle v0.3" — soft platinum-cured silicone (Shore A 20), seals externally against perianal surface (max 5 mm projection), push-fit onto steel enema faucet, gravity-fed max 1 m head. Veer promised a reply "kal" Tue 11:56pm; reply owed. Research: run 1 Jul 23 (119 agents, 24/30 claims confirmed) + run 2 Jul 23 (145 agents, vendor shortlist + regulatory gaps closed) + direct patent-status check.

## The one-line verdict on his spec
The spec is genuinely good for a v0.3 (dimensioned variants P1-P4, bench acceptance checks, safety limits, correct proof-of-concept framing). The help he needs is AFTER the document: vendor, regulatory route, and the patent question below.

## THE HEADLINE FOR THE CALL: the patent
**US9227006B2 "Non-penetrating nozzle" (STERILAB Inc, Florida; filed 2011, granted Jan 2016) is ACTIVE per Google Patents, expiring 2032-08-27** — and its independent claim 1 covers the generic mechanism, not just a specific shape: base + top face with discharge opening + interior passageway + radially projecting rim + continuous side wall that the orifice tissue conforms to, sealing externally during fluid delivery. Claim 14 (method): "pressing the nozzle against the orifice without penetrating the orifice... to create a leaktight seal." The spec's own language calls it a "flow-through enema nozzle that does not penetrate the anus."
- This is both direct prior art (limits what HE can patent) and a potential infringement problem for US sales until Aug 2032. **India: CONFIRMED CLEAR at family level (checked Jul 23)** — no Indian filing in the family, PCT WO2011150349A1 "Ceased", EP withdrawn; only the US grant is active (CN application shows stale "pending"). India national-phase window closed years ago. Making/selling in India is unblocked; IP counsel to double-check divisionals.
- Status caveat: Google Patents status is one source; his IP counsel should confirm maintenance-fee history in USPTO Patent Center (5-minute check) and whether STERILAB still exists / ever shipped a product (no commercialization was found).
- Call question: does his geometry (concave flange + sealing lip + 0-5mm nose) differ from claim 1's elements enough to design around, and who is his IP advisor?

## Vendor shortlist (verified against vendor sites, run 2)

| Vendor | Where | What's verified | Caveats / ask them |
|---|---|---|---|
| **Spectroplast** (spectroplast.com) | Zurich, ships internationally | **Best spec match.** 3D-prints final parts in true 100% silicone, TrueSil **A20** = exactly Shore A 20; platinum-catalyzed chemistry; no mould needed at all; no MOQ (1+ parts); express 5-7 days | A20 is their softest grade — ask if sub-20 possible for the P2 variant (Shore A 15-20). Self-reported lead times |
| **iMake** (imake.in) | Hyderabad | Final silicone parts (seals, gaskets, skin-contact components); medical + food-grade silicone; molds built from customer CAD/drawing/sample; 3D-printed tooling in 3-5 working days; from 1 piece | Shore range NOT verified (their "A 20-90" claim was refuted); ISO 9001 only, no 13485; no visible medical portfolio — RFQ must pin material grade + durometer |
| **Ami Polymer** (amipolymer.com) | Mumbai | ISO 13485:2016, cleanroom, US FDA DMF 26201; custom compression-molded silicone parts confirmed (diaphragms, gaskets, washers); platinum-cured medical grade cited on the diaphragm line | Platinum-cured claim is product-line-specific — ask directly: will you mold a custom Shore A 15-20 platinum-cured part from supplied tooling? |
| Protolabs (protolabs.com) | US/global | True-silicone 3D printing service — but it's a **channel for Spectroplast's process** (parts printed in Switzerland). Not an independent option | If quoting via Protolabs, confirm 20A availability (unverified) |

Recommended play: **Spectroplast for the first P1-P4 set** (no mould, exact durometer, days not weeks — and it kills the 3D-printed-mould step entirely for round one), **Ami Polymer RFQ in parallel** for the India-local, ISO 13485 path once the geometry converges. Design Roots (Bangalore) remains only a mould-maker option, not a silicone caster.

## India regulatory (CDSCO, MDR 2017) — now complete
- **Bench prototyping on his own bench: nothing required.** CDSCO FAQ 2024 (Q59): prototypes for feasibility/verification/validation testing "may obtain" a **test license — Form MD-12 application → Form MD-13 license** (Rule 31), issued by the CENTRAL Licensing Authority for all classes, Rs 500 per device, valid 3 years, ~1.5-2 months processing (consultancy-sourced). Needed once he manufactures batches for formal V&V/demo/clinical work — never for sale.
- Commercial manufacture later: likely **Class A** ("Gravity enema set", "Enema tip, reusable") → State Licensing Authority, Form MD-3 → MD-5. "Manual enema device" = Class B; gravity-vs-manual is the pivot.
- **If the classification is ambiguous** (novel external-sealing design), the mechanism exists: written request to the Central Licensing Authority with label + IFU + foreign regulatory status → CDSCO issues a classification ruling and updates the public list.
- Refuted, do not repeat: "ISO 13485 required for MD-5" (0-3); "any manufacture including bench work needs a test license" (0-3).

## US FDA — comparison, if the VC story includes the US
- Enema kit = 21 CFR 876.5210, code FCE, Class I, 510(k)-exempt — but defined verbatim as a nozzle "inserted into the rectum."
- Run 2 searched the 510(k) database: **no cleared external-sealing/non-inserting enema nozzle precedent exists.** K051344 turned out to be an inserting colonic nozzle (code KPL, Class II under 876.5220) — not a helpful precedent either way.
- The formal way to settle it: a **513(g) Request for Information** to FDA (mechanics/fee not verified this run — standard practice, ~60-day statutory clock). Not urgent unless US entry is a funded milestone.

## Differentiation + users (run 1, unchanged)
- All dominant transanal-irrigation products insert (Peristeen/Peristeen Plus balloon catheters, CP362, even the anal plug). External-sealing is differentiated at the product level; NOT novel at the concept level (see patent).
- Populations (all currently served by inserting systems — demand for non-inserting is inferred by adjacency, not demonstrated): anal fissures 240-342k new US cases/yr, 7.8% lifetime risk; neurogenic bowel dysfunction 23-80% prevalence (SCI/MS/spina bifida/Parkinson's); LARS up to 80% post rectal-cancer surgery.
- **Founder identified (Jul 23): Dr. Maneesh Sinha, Head of Urology, NU Hospitals Bangalore** (MCh Urology CMC Vellore, ~30 yrs). His clinical base — nephro-urology, incl. neurogenic bladder/bowel patients — maps directly to the NBD population above; likely he's seeing the first users in his own OPD. Ask on the call: is the origin a specific patient cohort he treats? That's the evidence story a VC already bought and the strongest anchor for question 4. Outreach drafts (his voice): `networking/mama-nozzle-outreach-drafts.md`.

## Questions to ask on the call
1. What exactly did the VC fund — what milestone, what deadline?
2. Has the steel handpiece (or measurements) gone to any manufacturer? (Spec says CAD can't freeze without it.) Note: Spectroplast prints direct from CAD, so the connector measurement is the only remaining physical blocker.
3. Does he know about US9227006B2? Who's his IP advisor? Is there an Indian family member of the patent? (Likely not — check.)
4. First user in his head: fissure patients self-administering, or caregivers/assisted care? Home or clinic?
5. CDSCO: does he agree the gravity/tip Class A bucket fits, or should he seek a classification ruling early?
6. What does he want from Veer? (Offer: vendor RFQs — Spectroplast + Ami Polymer + iMake, drafted this week; the section-11 manufacturer packet; competitor/patent one-pager.)

## Still open after two runs
- USPTO Patent Center confirmation of the maintenance-fee history (Google Patents says Active; single source).
- Whether other prior art / off-label products (colostomy irrigation cones, stoma cones) anticipate the design or could serve as an FDA predicate.
- 513(g) mechanics (fee, format).
- Whether any vendor delivers below Shore A 20 (needed for the P2 soft variant) — RFQ question.

## Status
- [ ] WhatsApp reply to Mama (overdue since Wed) — draft in session Jul 23
- [ ] Call scheduled (propose Fri/Sat evening IST = Veer morning PT)
