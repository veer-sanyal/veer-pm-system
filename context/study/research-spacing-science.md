> Compressed 2026-06-14 from files/study/research-spacing-science.md (full original).

# Spacing Science: Compressed Research Report
*Run B, 2026-06-14. 23 sources, 101 claims, 21/25 verified, 4 refuted.*

---

## Verified Findings

### (a) Optimal Spacing Gap

Gap is sub-linear fraction of retention interval (RI). Cepeda 2006/2008 (primary, 3-0): at RI=7d, optimal ISI ~1d (~14%); at RI=35d, ~7d (~20%); at RI=70d, ~14-21d (~20-30%); at RI=350d, ~20-35d (~5-10%). Recall gains from spacing vs. massing: 10%, 59%, 111%, 77% at 7/35/70/350-day RIs. Spacing approximately doubles long-term retention. Sub-linear means linear scaling of gap formula overshoots at long horizons -- use fixed bands instead.
Sources: Cepeda 2008 https://laplab.ucsd.edu/articles/Cepeda%20et%20al%202008_psychsci.pdf; Cepeda 2006 https://augmentingcognition.com/assets/Cepeda2006.pdf; https://www.yorku.ca/ncepeda/publications/CPVWR2006.html; https://files.eric.ed.gov/fulltext/ED505660.pdf; https://pubmed.ncbi.nlm.nih.gov/24744260/.

For 4-16 month horizon with no fixed exam: banded intervals (7 / 14 / 28 days keyed to mastery) sit within Cepeda's optimal range at week-to-year scale without continuous re-computation.

### (b) Expanding vs. Uniform Spacing

Expanding not superior to uniform for long-term retention. Karpicke 2007 (3-0): at 2-day delay, equal spacing = 45% recall, expanding = 33%. Kang 2014 (2-1): critical factor is delaying first retrieval, not the shape of the schedule. Avoid massing at the start; then uniform bands retain as well as or better than expanding over long horizons. Do not engineer expanding schedules -- promote the band when mastery rises.
Sources: Karpicke & Roediger 2007 https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JEPLMC.pdf; Kang 2014 https://pubmed.ncbi.nlm.nih.gov/24744260/.

### (c) Interleaving vs. Blocking

Interleaving beats blocking: d=1.34, can double test scores at 1-week delay (Rohrer & Taylor 2007, 3-0). Benefit holds in math (Taylor 2010) and concept learning (Kornell & Bjork 2008). 78% of participants performed better with spaced/interleaved practice (Foster 2019, 3-0). Mechanism: discriminative contrast -- learners must identify which procedure to apply, not just execute it. Interleaving hurts during practice (desirable difficulty) -- must be enforced, not left to learner preference.
Sources: Rohrer & Taylor 2007 http://uweb.cas.usf.edu/~drohrer/pdfs/Rohrer&Taylor2007IS.pdf; Taylor & Rohrer 2010 https://onlinelibrary.wiley.com/doi/abs/10.1002/acp.1598; Foster 2019 https://link.springer.com/article/10.3758/s13421-019-00918-4; Kornell & Bjork 2008 https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02127.x; Rohrer 2014 https://gwern.net/doc/psychology/spaced-repetition/2014-rohrer.pdf.

### (d) Calibration and Metacognition

Learners misjudge value of spacing/interleaving: 78% performed better spaced yet 78% believed massing was as good or better (Kornell & Bjork 2008, 3-0). In-session fluency under blocking misleads. Confidence: medium (single source for 78/78 statistic). Structural fix: require confidence prediction (0-100) before every answer; track mean overconfidence (mean confidence minus mean accuracy). Keeps calibration visible without relying on learner self-correction.
Sources: Kornell & Bjork 2008 https://journals.sagepub.com/doi/abs/10.1111/j.1467-9280.2008.02127.x; calibration meta-analysis https://www.researchgate.net/publication/349179781_Calibrating_Calibration_A_Meta-Analysis_of_Learning_Strategy_Instruction_Interventions_to_Improve_Metacognitive_Monitoring_Accuracy.

---

## Refuted (do not encode)

- "Space as widely as possible; over-spacing decrement is minor": 1-2 refuted. Sub-linear curve shows over-spacing does hurt.
- "Equal spacing = 45% recall vs. expanding = 33% at 2-day delay, therefore equal is cleanly superior": 1-2 refuted. Actual lesson: delay first retrieval; neither schedule dominates across all conditions.
- "Interleaving benefit driven by distributed practice not discriminative contrast (remote interleaving did not beat standard interleaving)": 0-3 refuted.
- "Remote-interleaved outperformed remote-blocked, supporting distributed-practice hypothesis": 0-3 refuted.

---

## Uncovered (budget-dropped from final verification)

- Minimum review frequency to prevent skill decay: not quantified. 30-day hard cap is a heuristic, not a verified number.
- Many-topics-at-limited-hours allocation rules: no verified heuristics for ~6-8 hrs/week across many topics. Due-first ordering is reasoned, not verified.
- Confidence prediction effect on calibration accuracy: intervention efficacy not directly verified (78/78 statistic supports the diagnosis, not the fix).

---

## Scheduling Rules (parameterizable)

Bands keyed to mastery, hard-capped at 30 days:

| Band | Condition | Interval |
|---|---|---|
| new | never practiced, or red weakness flag | 1-3 days |
| short | mastery < 0.5 | ~7 days |
| medium | mastery 0.5-0.8 | 14 days |
| long | mastery >= 0.8 | 28 days |

Interleaving: after every 3-4 items on one topic, insert one item from a different topic (prefer overdue or weak). Never block a full session to one topic even if the learner requests it.
Confidence prediction: 0-100 before every answer; track mean overconfidence per topic.
Going cold: surface any topic with last_practiced >30 days as overdue, regardless of band.
First retrieval: always delay -- never practice a topic immediately after first study.
