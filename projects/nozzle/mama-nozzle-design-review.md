# Design review — Adult External-Sealing Enema Nozzle v0.3
**For Dr. Maneesh Sinha (Head of Urology, NU Hospitals Bangalore). Reviewed 2026-07-24.**
Reframed: personal clinical side-project, self-funded (the VC money is a different venture). So this review is about DESIGN + MATERIAL + how to get a prototype made locally. Regulatory and patent findings are parked in `mama-enema-nozzle-call-prep.md` and are not blockers at this stage.

Sources: two adversarially-verified research runs (174 + 170 agents) + first-order physics done here. Anything below marked **[calc]** is my own estimate from the spec's own numbers, not a cited source — check the arithmetic before quoting it.

---

## Verdict

**The concept is sound and worth prototyping. The material choice is right. Two geometry decisions are wrong and should change before you spend money on parts.**

The single best piece of news: **the external-hold, non-inserting approach is already clinically validated.** Commercial cone-tip transanal irrigation devices deliberately use a manually-held external seal rather than an internal balloon, specifically because the external hold is less likely to provoke the reflex rectal contractions that balloon inflation triggers (Coloplast best-practice TAI paper; *Spinal Cord* 2013). You are not proposing something exotic. You are proposing a better-engineered version of a thing that already works.

---

## 1. Material: your choice is correct

**Platinum-cured (addition-cure) silicone is the right chemistry.** Verified: it meets USP Class VI and ISO 10993-5 cytotoxicity, leaves essentially no cure byproducts (peroxide-cure leaves acids/ketones/VOCs requiring a post-cure bake), and is fully autoclave-stable at 121-134°C with at most slight discolouration. Keep it.

**Shore A 10-20 is the right softness band** for perianal contact — and see §3, where I argue you should go softer than A20 for the baseline, not harder.

One trap worth naming: **every "skin-safe" / "medical-grade" marketing claim tested in the research was refuted except Spectroplast's.** Vendor web copy is not documentation. Before any material touches a patient, read the *named grade's* actual TDS/SDS and its ISO 10993 test report. This applies to the hobby-casting silicones in §5 too.

Biocompatibility you would eventually need for patient contact (short-duration skin + mucosal surface device): ISO 10993-5 (cytotoxicity), -10 (irritation/sensitisation), and increasingly -23 for irritation. Bench work on a model needs none of this.

## 2. Two geometry problems — fix these first

### 2a. The 4 mm outlet is a jet nozzle, and it is fighting your own bench check
Your spec sets a 6 mm internal lumen narrowing to a **4 mm outlet**, with the rationale "gentle gravity-fed stream." The physics goes the other way. Narrowing the exit *accelerates* the stream exactly where it meets mucosa:

- Torricelli at a 1 m head: exit velocity ≈ **4.4 m/s** **[calc]**
- The 6→4 mm step alone multiplies velocity by (6/4)² = **2.25×** **[calc]**
- Flow through a 4 mm orifice at that velocity ≈ 55 mL/s, so ~500 mL in about 9 seconds **[calc]**

So flow *rate* is not your problem — velocity is. Your own acceptance criterion ("continuous central flow without a fine high-velocity jet") is contradicted by the geometry that produces it. A directed 4.4 m/s stream a few millimetres from rectal mucosa is the kind of thing that causes mucosal injury, and it is avoidable.

**Fix:** make the outlet the *largest* opening in the flow path, not the smallest — a diffusing exit (outlet ≥ lumen, e.g. 6-8 mm, flared), and/or several radial ports instead of one axial hole, and/or a small baffle so flow disperses rather than firing straight up the canal. I have already set `outlet_dia = 6.0` as the default in the CAD (§6) with a comment explaining why, and left 4.0 available so you can print both and compare.

### 2b. A flat-ish 50 mm disc cannot seal across the natal cleft
This is the biggest anatomical risk and it is not addressed anywhere in v0.3. The perianal region is not a plane — it sits in the gluteal cleft. A shallow 4 mm dish on a 50 mm circular flange will contact well at 3 and 9 o'clock and **bridge at 12 and 6 o'clock**, which is precisely where the leak path opens. Research independently confirms leakage past the seal is a *common, expected* failure mode in existing TAI practice, with a standard troubleshooting protocol for it, and names leakage among the top reasons patients abandon these devices. My cleft argument is the mechanism behind that statistic.

**Fixes, cheapest first:**
1. **Go softer.** A20 is too firm to conform into a cleft under gentle hand pressure. Make **A10 the baseline**, not the fallback variant. Softness is doing more work here than diameter is.
2. **Deepen and thin the skirt.** A 4 mm dish with a 2 mm lip is a stiff shallow saucer. A taller, thinner, more compliant conforming skirt drapes into the cleft; a shallow rigid dish spans it.
3. **Consider an oval flange** with the long axis oriented along the cleft (anterior-posterior). Cheap to test — it is one number in the CAD.
4. Test P2 (55 mm) knowing that **more diameter on a stiff flange can make cleft bridging worse, not better.** Bigger is not automatically better sealing.

## 3. Missing from the spec — the numbers that decide whether it works

Your acceptance checks in §9 are all qualitative ("no leakage", "no fine jet", "conforms to a soft anatomical model"). None of them can pass or fail objectively. Add these:

| Add this | Why | First-order estimate |
|---|---|---|
| **Hold force** to maintain seal | This is the whole usability question and it is unmeasured | ≈ **16 N (1.7 kgf)** continuous on a 50 mm flange at 1 m head; ≈ 20 N (2 kgf) on the 55 mm **[calc]** |
| **Leakage volume** (mL leaked / mL delivered) | Makes "reduce leakage" testable | target a number, e.g. <5% |
| **Exit velocity** or outlet area ratio | Turns "no fine jet" into a spec | outlet area ≥ lumen area |
| **Delivery time** for the intended volume | Clinically useless if too slow | ~9 s per 500 mL is fine **[calc]** |
| **Water temperature** in the IFU | Cold water causes cramping | body temperature |
| **Peel-off / suction release** | You forbid suction but no feature guarantees it | add a small non-contact pull tab so it peels from one edge instead of being yanked |

On hold force: ~1.7 kgf sustained is feasible for a caregiver for a minute or two, but it is *work*, and it is the number that decides whether frail or self-administering patients can use this at all. Measure it early — a kitchen scale and the printed part will tell you.

**And the honest physiological limit:** a 0-5 mm nose can only engage the **distal external anal sphincter** — the voluntary, cough-guarding muscle — not the internal sphincter that supplies most resting tone. So retention assistance is real but modest, and any cough or Valsalva will spike rectal pressure well past the 1 m head and break the seal **[calc]**. Keep the claim as your spec already words it: *brief* assisted retention. Do not let it drift toward "retention device."

## 4. Single-use and biodegradable — direct answers

**Can it be single-use? Yes, and it probably should be — but not in silicone.**
- Reprocessing a reusable version is the weak point: a 6 mm lumen ~55 mm long plus a blind socket that grips the spout is an occluded space that cannot be reliably brush-cleaned or visually inspected. Silicone autoclaves fine, but autoclaving does not substitute for cleaning, and narrow-lumen bioburden is the classic reprocessing failure. Repeated cycles will also relax the push-fit interference and start leaking.
- The industry has already answered this: commercial single-use enema/rectal tips are **moulded PVC, EO-sterilised, explicitly labelled no-reuse.** A granted enema-nozzle patent names **polyurethane as preferred**, with silicone/SEBS/TPS as alternatives.
- **Useful distinction to hold onto: "single-use" vs "single-patient use."** Hospital *shared* use pushes hard to disposable. A home user reusing their own device is a different and much easier risk case. You may want both: a disposable hospital SKU and a durable single-patient home SKU.
- For a disposable, the realistic material is a **moulded TPE/SEBS or medical PVC**, not silicone — silicone at single-use unit cost is off-pattern.

**Can it be biodegradable? Not yet — this one is aspirational, and I'd park it.**
No candidate is simultaneously soft (~Shore A 10-20), documented as biocompatible for skin+mucosal contact, and mouldable:
- **PLA and PLA blends** — rigid engineering plastics. Even a toughened 70/20/10 PLA/PHBV/PCL blend has Young's modulus ≈ 949 MPa, roughly 1,000-9,000× stiffer than A10-20 silicone (~0.1-1 MPa). Improved ductility is not softness.
- **PHA/PHB/PHBV** — characterised on Shore **D**, semicrystalline and stiff; moulded (unoriented) parts are brittle.
- **PCL** — softer, but degrades over 2-4 years in vivo, which defeats the flushable/compostable rationale.
- **The one genuinely soft biodegradable elastomer found** (photo-crosslinked PLA-PEG-PLA) is a UV thermoset — not injection-mouldable — with only in-vitro cytocompatibility and no ISO 10993 mucosal testing.
- **"Flushable" is self-defeating here** on two counts: a water-dispersible polymer in a water-delivery device is a contradiction, and flushing soft polymer parts is bad for sewer systems.

Note the verdict rests on *absence of qualifying data*, not proof of unsafety. **Better interim answer for his eco goal:** a recyclable **mono-material** TPE disposable, or a durable single-patient silicone device with a take-back scheme. Both are honest sustainability stories that don't require unproven materials against mucosa.

## 5. Getting it made — Bangalore reality

Three research attempts could not confirm **a single Bangalore silicone-part moulder** (platinum-cure, medical grade, 1-5 pieces). Both IndiaMART-sourced Bengaluru leads were refuted. Important caveat: that trade is phone-and-visit driven with little web presence, so this is a limit of web verification, not proof none exists — a Peenya/Bommasandra walk-around may well find one.

What Bangalore *verifiably* offers is **the first half of the job**: printing the rigid master.

| Option | Where | What's confirmed | Use it for |
|---|---|---|---|
| **Criador Labs** | HRBR Layout | ISO 13485 medical-device product-innovation studio; SLA/SLS printing. No silicone confirmed | Best local *design partner*. Face-to-face, speaks medical device |
| **iamRapid** | HSR Layout, +91 8629044664 | Working SLA resin printing bureau. No silicone | Cheap fast masters |
| **IISc CPDMED** | Raman Building, IISc; 080-22933687, incubator.dm@iisc.ac.in | MedTech incubator, rolling admissions, eligibility explicitly includes industry professionals | Institutional route, and your best local network into medtech fabrication |
| ~~C-CAMP MedTech µFab~~ | Bellary Rd | **Checked directly — it is a microfluidics µFab for diagnostic chips.** Not soft-part moulding | Dead end for this part (though they do PDMS work, so they'll know local silicone suppliers) |
| ~~BBC / 3D Paradise~~ | — | BBC is incubation-gated, not a fab shop; 3D Paradise's "Bangalore" page has only a Delhi address | Skip |

**The recommended split route:**
1. **Now, for geometry:** print rigid masters locally (iamRapid or Criador) from the STEP files in §6 and hold them against an anatomical model. Rigid parts cannot test sealing, but they *will* test fit to the steel handpiece, flange diameter feel, and cleft geometry — for a few thousand rupees, in person, in days. **Do this before ordering any silicone.**
2. **For the real soft part:** **Spectroplast (Zurich)** is the only confirmed source of a finished soft platinum-grade silicone part at this quantity — direct silicone 3D printing, no tooling, **TrueSil A20 at Shore 20A**, orders from 1 unit, instant online quote from an uploaded file, and its A20 passed three ISO 10993 tests. Ships internationally. Ask them about a sub-20A grade for the soft variant.
3. **The face-to-face path he prefers, as a two-step build:** local SLA master → hand-cast platinum-cure silicone into it. Material: **Smooth-On Dragon Skin 15 or 20** hits the A15-20 target exactly (Ecoflex goes softer). Sourcing: no confirmed Bangalore distributor; **Gaurav Impex (Mumbai)** is an authorised Dongjue LSR importer shipping pan-India. **Read the actual TDS before any patient contact** — see §1.
4. **Drop these:** Protolabs (medical LSR only at A52 — far too hard), Viking Extrusions (India shipping unconfirmed), RapidMade (no true silicone), Karkhana.io (electronics EMS, not silicone at all).

## 6. The CAD file problem — solved, files are ready

He needs a STEP file to hand a vendor. The part is a solid of revolution with every dimension already in his spec, so it did not need hand-modelling in CAD software — it is generated from code.

**Built and verified: `projects/nozzle/nozzle-cad/nozzle.py`** (Python + CadQuery). Generates all four spec variants:

| File | Flange | Nose projection | Verified |
|---|---|---|---|
| `nozzle_P1.step` | 50 mm | 3.00 mm | ✓ |
| `nozzle_P2.step` | 55 mm | 3.00 mm | ✓ |
| `nozzle_P3.step` | 50 mm | 0.00 mm (flush) | ✓ |
| `nozzle_P4.step` | 50 mm | 5.00 mm | ✓ |

Every dimension is a named variable at the top — change a number, re-run, get new STEP + STL. Verified three ways, not assumed: flange OD and nose projection asserted against the parameters (the script fails loudly if geometry drifts), the flow lumen probed to confirm it is open end-to-end on all four, and rendered to confirm it matches his Figure 1. Two real bugs were caught this way — an inverted dish cut that hollowed the part, and a nose whose projection came out 1.35 mm instead of 3 mm because the outlet bore ate the dome tip, which would have silently invalidated the whole P1/P3/P4 comparison.

To run: `pip3 install cadquery` then `python3 nozzle.py`.

Note for the vendor: these are **design-intent** models. A production mould needs draft angles, parting-line and shrinkage work, which the moulder does in their own CAD — that is expected and is what his spec §7 already asks them for.

If he prefers a GUI, FreeCAD is free and there are Claude/MCP integrations for both FreeCAD and OpenSCAD. But for a parametric part like this, the script *is* the better tool — it makes variants trivial and the dimensions self-documenting.

---

## Recommended sequence

1. **Fix the outlet** (diffusing, ≥ lumen) and **make A10 the baseline** durometer. Both are free changes now, expensive later.
2. **Add the missing quantitative acceptance criteria** — hold force, leakage %, delivery time. Measure hold force on a printed part with a kitchen scale.
3. **Measure the steel handpiece spout** and set `socket_bore` in the CAD. This is still the true critical path — nothing can be finalised without it.
4. **Print rigid masters locally this week** (Criador or iamRapid) and check fit + cleft geometry in person.
5. **Then** order soft parts (Spectroplast, or local cast from Dragon Skin) once geometry is settled.
6. **Park single-use material choice and biodegradability** until the geometry is proven. Prove it works in silicone first; optimise for manufacture second. Deciding disposable material now, before the shape is validated, is optimising the wrong end.
7. Bench and anatomical-model testing only. Nothing about this changes the "not for clinical use" framing in v0.3, which is correctly stated.

## Still open
- No confirmed Bangalore silicone-part moulder — worth a physical Peenya/Bommasandra visit, or asking C-CAMP's microfluidics team who casts PDMS for them locally.
- Whether an external flange can hold irrigant against distal-EAS pressure in practice: needs his bench leak test, not more literature.
- Whether a TPE/SEBS or medical PVC at a comfortable durometer hits the disposable cost target.
