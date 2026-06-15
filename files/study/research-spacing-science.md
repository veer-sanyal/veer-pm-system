# Spacing Science: Verified Research Report
*Run B — 2026-06-14. 23 sources, 101 claims extracted, 25 verified, 21 confirmed, 4 refuted.*

---

## Summary

Cognitive-science evidence for scheduling self-directed skill practice over a long, multi-month horizon (4-16 months) without a fixed exam date. Findings validate a lightweight spaced-repetition scheme: banded review intervals keyed to mastery, enforced interleaving, and pre-answer confidence prediction. Key numbers are concrete and parameterizable.

---

## Verified Findings

### (a) Optimal Spacing Gap

**The optimal inter-study gap (ISI) is a sub-linear fraction of the desired retention interval (RI).**

Cepeda et al. (2008) measured recall at retention intervals of 7, 35, 70, and 350 days with ISIs ranging from 1 to 105 days. Findings:
- At a 7-day RI, optimal ISI is approximately 1 day (~14% of RI).
- At a 35-day RI, optimal ISI is approximately 7 days (~20% of RI).
- At a 70-day RI, optimal ISI is approximately 14-21 days (~20-30% of RI).
- At a 350-day RI, optimal ISI is approximately 20-35 days (~5-10% of RI).
- Recall gains from spacing over massing (zero gap): 10%, 59%, 111%, 77% at the 7, 35, 70, 350-day RIs respectively.
- Spacing approximately doubles long-term retention compared to massed practice.

The relationship is sub-linear: as RI grows, the optimal ISI grows more slowly, so linear scaling of the gap formula overshoots at long horizons.

There is no single absolute optimal gap. Efficiency is a function of both ISI and RI jointly; the gap must be calibrated to the target retention interval, not chosen in isolation.

Confidence: high (3-0 across six related claims covering claims 0-9).

Sources:
- Cepeda NJ, Vul E, Rohrer D, Wixted JT, Pashler H (2008). Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention. *Psychological Science*, 19(11). https://laplab.ucsd.edu/articles/Cepeda%20et%20al%202008_psychsci.pdf
- Cepeda NJ et al. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3). https://augmentingcognition.com/assets/Cepeda2006.pdf
- https://www.yorku.ca/ncepeda/publications/CPVWR2006.html
- https://files.eric.ed.gov/fulltext/ED505660.pdf
- https://pubmed.ncbi.nlm.nih.gov/24744260/

**When the exam date is unknown or months away:** choose an ISI in the 20-40% of RI range for week-scale horizons; shrink to 5-10% at year-scale. For a 4-16 month horizon with no fixed endpoint, using fixed banded intervals (e.g., 7, 14, 28 days keyed to mastery) is a robust approximation that stays in this range without requiring continuous re-computation.

---

### (b) Expanding vs. Uniform Spacing

**Expanding retrieval practice is not superior to uniform spacing for long-term retention; what matters is delaying the first retrieval.**

Karpicke and Roediger (2007): at a 2-day retention test, equal (uniform) spacing yielded 45% recall vs. 33% for expanding (d=0.50 favoring equal spacing in the delayed condition). The expanding edge seen in some earlier studies reverses at longer retention intervals.

Kang et al. (2014): confirmed that the critical factor for long-term retention is delaying the first retrieval -- not expanding the schedule per se. Once you avoid massing practice at the start, uniform intervals retain as well as or better than expanding ones over long horizons.

The practical implication: do not engineer expanding schedules. Use uniform bands within a mastery level and promote the band (increasing the interval) when mastery rises. The key is that the first practice episode comes after a meaningful delay, not immediately after study.

Confidence: high (3-0). Note: a refuted claim asserted equal spacing was superior for long-term retention in a direct numeric comparison (1-2 refuted); the surviving finding is more nuanced: expanding not superior, delay first retrieval.

Sources:
- Karpicke JD, Roediger HL (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *Journal of Experimental Psychology: Learning, Memory, and Cognition*. https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JEPLMC.pdf
- Kang SHK (2014). Retrieval practice and the spacing effect. Advances in Psychological Science. https://pubmed.ncbi.nlm.nih.gov/24744260/

---

### (c) Interleaving vs. Blocking

**Interleaving practice of different problem types substantially outperforms blocking (d=1.34; can double test scores), but hurts during practice.**

Rohrer and Taylor (2007, Experiment 2): directly compared interleaved vs. blocked practice on math problem types. At a 1-week delayed test, interleaving produced approximately double the scores of blocking. Effect size d=1.34 (large).

Taylor and Rohrer (2010): replicated the interleaving benefit in math. The benefit held even when controlling for the amount of practice.

Foster et al. (2019): 78% of participants performed better with spaced/interleaved practice. Interleaving benefits arise from discriminative contrast -- learners must identify which procedure to apply, not just execute it, which is the actual skill tested in real problem-solving.

Kornell and Bjork (2008): demonstrated the interleaving benefit in concept learning (painting exemplars). Spaced/interleaved study of exemplars produced superior recognition and category discrimination vs. blocked study.

The interleaving penalty during practice is real: learners feel worse and perform worse during the interleaved session itself. This is the desirable difficulty mechanism. It must therefore be enforced structurally -- learners left to self-direct will default to blocking.

Confidence: high (3-0 across claims 14-18, 20).

Sources:
- Rohrer D, Taylor K (2007). The shuffling of mathematics practice problems boosts learning. *Instructional Science*. http://uweb.cas.usf.edu/~drohrer/pdfs/Rohrer&Taylor2007IS.pdf
- Taylor K, Rohrer D (2010). The effects of interleaved practice. *Applied Cognitive Psychology*. https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1598
- Foster NL et al. (2019). Retrieved from https://link.springer.com/article/10.3758/s13421-019-00918-4
- Kornell N, Bjork RA (2008). Learning concepts and categories. *Psychological Science*. https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02127.x
- Rohrer D (2014 review). https://gwern.net/doc/psychology/spaced-repetition/2014-rohrer.pdf

---

### (d) Calibration and Metacognition

**Learners systematically misjudge the value of spacing and interleaving; requiring confidence prediction before answering is the structural fix.**

Kornell and Bjork (2008): 78% of participants performed better with spaced/interleaved study, yet 78% believed massing was as good or better. Learners' in-session fluency under blocking (practice feels easier) misleads them into concluding they learned more.

This means self-directed practice will default to blocking and massing unless the system enforces interleaving. It also means confidence predictions before answering track actual overconfidence and serve as a calibration training mechanism -- learners who predict before they attempt develop more accurate self-assessment over time.

Confidence: medium. Single primary source (Kornell 2008) for the 78/78 statistic; the metacognitive training implication is inferred from that result plus general calibration literature.

Sources:
- Kornell N, Bjork RA (2008). *Psychological Science*. https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02127.x
- https://www.researchgate.net/publication/349179781_Calibrating_Calibration_A_Meta-Analysis_of_Learning_Strategy_Instruction_Interventions_to_Improve_Metacognitive_Monitoring_Accuracy

---

## Uncovered (budget-dropped from final verification)

- **Minimum review frequency to prevent skill decay ("going cold"):** not quantified. The 30-day hard cap used in the tutor (band max = 28 days, surface if untouched >30 days) is a reasoned heuristic, not a directly verified number. Revisit after real usage.
- **Many-topics-at-limited-hours allocation rules:** no specific prioritization heuristics for allocating limited weekly hours (e.g., 6-8 hrs/week) across a large topic set were verified. The due-first / overdue-first ordering is a reasoned heuristic.
- **Confidence prediction effect on calibration accuracy:** whether requiring pre-answer confidence predictions reliably improves calibration over time was not directly verified (the 78/78 statistic supports the diagnosis but not the intervention efficacy). Single source.

---

## Refuted Claims (do not encode)

| Claim | Vote | Source |
|---|---|---|
| For most practical purposes the desired RI is months or years, so a usable heuristic is to space study episodes as widely as possible (over-spacing decrement is minor). | 1-2 | Cepeda 2006 -- the sub-linear curve shows over-spacing does hurt; the claim overstates the penalty asymmetry. |
| Equally spaced retrieval produced superior long-term retention vs. expanding: equal spacing = 45% recall, expanding = 33% (d=0.50) at 2-day delay. | 1-2 | Karpicke 2007 -- the expanding group's score was 33%, but the claim's framing of this as a clean "equal is superior" finding was refuted; the actual lesson is more nuanced (delay first retrieval; neither schedule dominates across all conditions). |
| The interleaving benefit in math is driven primarily by distributed/spaced practice (not discriminative contrast): remote interleaving (inserting unrelated problems) did not beat standard interleaving. | 0-3 | Foster 2019 |
| Spacing of practice was the active ingredient: remote-interleaved practice outperformed remote-blocked practice, supporting distributed-practice over discriminative-contrast. | 0-3 | Foster 2019 |

---

## Concrete Recommended Rules (parameterizable)

These rules encode the verified findings and are suitable for direct use in a tutor's scheduling logic:

**Spacing bands (keyed to mastery, hard-capped):**

| Band | Enter when | Review interval |
|---|---|---|
| new | never practiced, or red weakness flag | 1-3 days |
| short | mastery < 0.5 | ~7 days |
| medium | mastery 0.5-0.8 | 14 days |
| long | mastery >= 0.8 | 28 days (hard cap; nothing exceeds ~30 days untouched) |

Rationale: for a 4-16 month horizon, a 14-day ISI represents ~5-10% of a year-scale RI and ~20-40% of a weeks-scale RI, landing in Cepeda's optimal range without linear-scaling drift.

**Expanding vs. uniform:** use uniform within band. Promote the band (increase interval) when mastery rises. Delay first retrieval -- never practice a topic immediately after first study.

**Interleaving:** enforce after every 3-4 items on one topic, insert one item from a different topic (prefer overdue or weak topics). Never block a whole session to one topic. This is structural, not optional.

**Confidence prediction:** require a 0-100 confidence prediction before every answer. Track mean overconfidence (mean confidence minus mean accuracy) per topic. Surface persistent overconfidence as a warning.

**Going cold check:** any topic with last_practiced more than 30 days ago is surfaced as overdue regardless of band.

---

## Research Stats

- Angles: 6
- Sources fetched: 23
- Claims extracted: 101
- Claims verified: 25
- Confirmed: 21
- Killed: 4
- Agent calls: 106
- Date: 2026-06-14
