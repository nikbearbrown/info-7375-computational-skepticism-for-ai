# Term audit: the terms in the "What to look for" field lists, against the chapter text

Checked 2026-11-09 by script (`scratchpad/audit.py`), against the chapter markdown in `chapters/` of this repo.

**How to read it.** Each row is a term used in a field list: an **item label** (the plain-word heading), a **key term** (bold or italic in the item's "What it is" paragraph), or an **industry word** ("Also called", common usage). The check looks in the chapter text:
- **LITERAL**: the exact words (case, hyphens and plural endings ignored) appear in the chapter, at the section and line shown.
- **NEAR**: every content word of the term appears in one section but not as that phrase. Usually a paraphrase of the book's idea. Read before relying on it.
- **NOT FOUND**: not in the chapter. Fine for plain labels and industry words, which are not meant to be in the book. For a key term it is a flag: a term the exam should not assume.

**Limits.** This is a text match, not a judgment. It will miss a term the book states in other words, and it will match a word used in a different sense. The Chapter 9 and 13 files each have a duplicate chapter file in the repo; the numbered chapter named in each section title was used. Terms the agents bolded or italicised are what the script sees; an unmarked key term is not checked.

## Summary

| Field list | Item labels literal | Key terms literal / near / not found | Industry words in the book | Items in file |
|---|---|---|---|---|
| Chapter 1, The Skeptic's Toolkit | 1 of 15 | 1 / 0 / 0 | 13 of 49 | 15 |
| Chapter 2, The Confidence Illusion | 0 of 15 | 11 / 0 / 0 | 9 of 47 | 15 |
| Chapter 3, Data Validation | 0 of 15 | 7 / 0 / 0 | 2 of 32 | 15 |
| Chapter 4, Robustness | 1 of 14 | 6 / 0 / 0 | 2 of 12 | 14 |
| Chapter 5, Model Explainability | 1 of 12 | 3 / 0 / 1 | 5 of 15 | 12 |
| Chapter 6, Bias | 11 of 15 | 22 / 2 / 1 | 6 of 38 | 15 |
| Chapter 7, Fairness Metrics | 0 of 15 | 11 / 2 / 1 | 8 of 30 | 15 |
| Chapter 8, Agents | 1 of 15 | 24 / 2 / 5 | 1 of 6 | 15 |
| Chapter 9, Delegation and Trust | 2 of 15 | 14 / 0 / 0 | 7 of 34 | 15 |
| Chapter 10, Visualization Under Validation | 2 of 15 | 3 / 1 / 0 | 7 of 24 | 15 |
| Chapter 11, Communicating Uncertainty | 0 of 15 | 28 / 0 / 1 | 16 of 42 | 15 |
| Chapter 12, Accountability | 1 of 15 | 16 / 1 / 2 | 3 of 19 | 15 |
| Chapter 13, The Limits of AI | 0 of 15 | 9 / 1 / 1 | 13 of 48 | 15 |
| The Five Supervisory Capacities (searched in Chapters 1 and 9) | 0 of 0 | 0 / 0 / 0 | 0 of 0 | 0 |
| The Five Supervisory Capacities (searched in Chapters 1 and 9) | 5 of 5 | 3 / 2 / 0 | 2 of 10 | 5 |


## Chapter 1, The Skeptic's Toolkit

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A stand-in for what you care about | item label | NEAR | 35, What you measure and what you care about |
| 1 | proxy metric | also called (industry) | NOT FOUND |  |
| 1 | proxy | also called (industry) | NOT FOUND |  |
| 1 | offline-online gap | also called (industry) | NOT FOUND |  |
| 1 | Goodhart's law | also called (industry) | LITERAL | 46, What you measure and what you care about |
| 2 | A gap from the start | item label | NOT FOUND |  |
| 2 | proxy label | also called (industry) | NOT FOUND |  |
| 2 | label problem | also called (industry) | NEAR | 173, The Five Supervisory Capacities |
| 2 | historical bias | also called (industry) | NOT FOUND |  |
| 3 | A gap that opens later | item label | NEAR | 35, What you measure and what you care about |
| 3 | drift | also called (industry) | LITERAL | 117, What I mean by skepticism |
| 3 | concept drift | also called (industry) | NOT FOUND |  |
| 3 | distribution shift | also called (industry) | LITERAL | 241, Skepticism as a team practice |
| 3 | specification gaming | also called (industry) | NOT FOUND |  |
| 3 | reward hacking | also called (industry) | NOT FOUND |  |
| 4 | A success report, and a system nobody checked | item label | NOT FOUND |  |
| 4 | silent failure | also called (industry) | NOT FOUND |  |
| 4 | silent success | also called (industry) | NOT FOUND |  |
| 4 | green dashboard | also called (industry) | NOT FOUND |  |
| 4 | watermelon metric | also called (industry) | NOT FOUND |  |
| 5 | Confidence carried into a changed world | item label | NEAR | 56, What I mean by skepticism |
| 5 | model drift | also called (industry) | NEAR | 56, What I mean by skepticism |
| 5 | big-data hubris | also called (industry) | LITERAL | 92, What I mean by skepticism |
| 6 | A claim that cannot be wrong | item label | LITERAL | 98, What I mean by skepticism |
| 6 | unfalsifiable claim | also called (industry) | NOT FOUND |  |
| 6 | not even wrong | also called (industry) | NEAR | 56, What I mean by skepticism |
| 6 | rhetoric | also called (industry) | LITERAL | 98, What I mean by skepticism |
| 7 | A test that passes and still misses | item label | NOT FOUND |  |
| 7 | metric mismatch | also called (industry) | NOT FOUND |  |
| 8 | Counting confirmations, not hunting the failure | item label | NOT FOUND |  |
| 8 | confirmation bias | also called (industry) | NOT FOUND |  |
| 8 | cherry-picking | also called (industry) | NOT FOUND |  |
| 8 | red-teaming | also called (industry) | NOT FOUND |  |
| 8 | adversarial testing | also called (industry) | NOT FOUND |  |
| 8 | black swan | also called (industry) | LITERAL | 102, What I mean by skepticism |
| 9 | The output taken for the world | item label | NEAR | 342, LLM Exercise — Chapter 1: The Skeptic's Toolkit |
| 9 | shortcut learning | also called (industry) | NOT FOUND |  |
| 9 | spurious correlation | also called (industry) | NOT FOUND |  |
| 9 | Clever Hans effect | also called (industry) | NOT FOUND |  |
| 10 | Polish doing the work of evidence | item label | NOT FOUND |  |
| 10 | automation bias | also called (industry) | NOT FOUND |  |
| 10 | overreliance | also called (industry) | NOT FOUND |  |
| 10 | fluency trap | also called (industry) | LITERAL | 27, Chapter 1 — The Skeptic's Toolkit |
| 11 | Cheap to make, dear to check | item label | NOT FOUND |  |
| 11 | verification debt | also called (industry) | NOT FOUND |  |
| 11 | review bottleneck | also called (industry) | NOT FOUND |  |
| 11 | solve-verify asymmetry | also called (industry) | LITERAL | 153, The solve-verify asymmetry |
| 12 | Fixing the symptom, not the question | item label | NOT FOUND |  |
| 12 | Science | key term (italic) | LITERAL | 92, What I mean by skepticism |
| 12 | problem framing | also called (industry) | NOT FOUND |  |
| 12 | label choice | also called (industry) | NOT FOUND |  |
| 12 | problem formulation | also called (industry) | LITERAL | 181, The Five Supervisory Capacities |
| 13 | A decision resemblance cannot see | item label | NEAR | 173, The Five Supervisory Capacities |
| 13 | cold-start problem | also called (industry) | NOT FOUND |  |
| 13 | out-of-distribution | also called (industry) | LITERAL | 114, What I mean by skepticism |
| 14 | A number read without its domain | item label | NEAR | 173, The Five Supervisory Capacities |
| 14 | cost-sensitive | also called (industry) | NOT FOUND |  |
| 14 | domain expertise | also called (industry) | NOT FOUND |  |
| 14 | human review | also called (industry) | LITERAL | 117, What I mean by skepticism |
| 14 | interpretive judgment | also called (industry) | LITERAL | 189, The Five Supervisory Capacities |
| 15 | A check nobody owns | item label | NOT FOUND |  |
| 15 | single point of failure | also called (industry) | NEAR | 56, What I mean by skepticism |
| 15 | accountability gap | also called (industry) | NOT FOUND |  |
| 15 | responsibility gap | also called (industry) | NOT FOUND |  |
| 15 | undefended gap | also called (industry) | LITERAL | 245, Skepticism as a team practice |

## Chapter 2, The Confidence Illusion

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A belief dressed as a fact | item label | NOT FOUND |  |
| 1 | an uncalibrated score | also called (industry) | NOT FOUND |  |
| 1 | decorative number | also called (industry) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 2 | 99% accurate" that hides two numbers | item label | NOT FOUND |  |
| 2 | Sensitivity | key term (bold) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 2 | Specificity | key term (bold) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 2 | recall | also called (industry) | NOT FOUND |  |
| 2 | true positive rate | also called (industry) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 2 | true negative rate | also called (industry) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 2 | precision | also called (industry) | LITERAL | 259, The test that is 99% accurate, and the patient it kills |
| 3 | Stated confidence that does not match what happens | item label | NEAR | 402, Calibration — the most operationally important diagnostic in this chap |
| 3 | calibrated | key term (bold) | LITERAL | 404, Calibration — the most operationally important diagnostic in this chap |
| 3 | reliability diagram | also called (industry) | LITERAL | 620, LLM Exercise — Chapter 2: Probability, Uncertainty, and the Confidence |
| 3 | miscalibration | also called (industry) | NOT FOUND |  |
| 3 | expected calibration error | also called (industry) | NOT FOUND |  |
| 4 | Overconfidence at the top, and a fix that goes stale | item label | NEAR | 402, Calibration — the most operationally important diagnostic in this chap |
| 4 | temperature scaling | key term (bold) | LITERAL | 415, Calibration — the most operationally important diagnostic in this chap |
| 4 | overconfident | also called (industry) | LITERAL | 406, Calibration — the most operationally important diagnostic in this chap |
| 4 | confidently wrong | also called (industry) | LITERAL | 20, Why this chapter |
| 4 | post-hoc calibration | also called (industry) | NEAR | 568, Challenge |
| 5 | The forgotten prior | item label | NOT FOUND |  |
| 5 | base rate | key term (bold) | LITERAL | 8, Chapter 2 — Probability, Uncertainty, and the Confidence Illusion |
| 5 | prior | key term (bold) | LITERAL | 4, Chapter 2 — Probability, Uncertainty, and the Confidence Illusion |
| 5 | base rate neglect | also called (industry) | NOT FOUND |  |
| 5 | base rate fallacy | also called (industry) | NOT FOUND |  |
| 5 | false positive paradox | also called (industry) | NOT FOUND |  |
| 6 | Answering the wrong question | item label | NOT FOUND |  |
| 6 | transposed conditional | also called (industry) | NOT FOUND |  |
| 6 | prosecutor's fallacy | also called (industry) | NOT FOUND |  |
| 6 | confusion of the inverse | also called (industry) | NOT FOUND |  |
| 7 | A common signal read as bad news | item label | NEAR | 90, Conditional probability — the probability that updates on what you kno |
| 7 | a low likelihood ratio | also called (industry) | NOT FOUND |  |
| 7 | a non-discriminating feature | also called (industry) | NOT FOUND |  |
| 8 | The flood of false alarms | item label | NEAR | 338, The false-positive structure is everywhere |
| 8 | JAMA Internal Medicine | key term (italic) | LITERAL | 348, The false-positive structure is everywhere |
| 8 | alert fatigue | also called (industry) | LITERAL | 348, The false-positive structure is everywhere |
| 8 | alarm fatigue | also called (industry) | NEAR | 338, The false-positive structure is everywhere |
| 8 | crying wolf | also called (industry) | NOT FOUND |  |
| 9 | Steps treated as independent | item label | NOT FOUND |  |
| 9 | the independence assumption | also called (industry) | NEAR | 170, Worked example — independent events |
| 9 | error compounding | also called (industry) | NOT FOUND |  |
| 10 | A rate that belongs to no single model | item label | NOT FOUND |  |
| 10 | total probability theorem | key term (bold) | LITERAL | 20, Why this chapter |
| 10 | a weighted average over segments | also called (industry) | NOT FOUND |  |
| 10 | the aggregate | also called (industry) | NOT FOUND |  |
| 10 | per-segment | also called (industry) | NOT FOUND |  |
| 11 | Blaming the biggest | item label | NOT FOUND |  |
| 11 | error attribution | also called (industry) | NOT FOUND |  |
| 11 | error slicing | also called (industry) | NOT FOUND |  |
| 11 | finding the root cause by cohort | also called (industry) | NOT FOUND |  |
| 12 | The world moved and the dashboard stayed green | item label | NOT FOUND |  |
| 12 | Distribution shift | key term (bold) | LITERAL | 20, Why this chapter |
| 12 | data drift | also called (industry) | NEAR | 402, Calibration — the most operationally important diagnostic in this chap |
| 12 | concept drift | also called (industry) | NOT FOUND |  |
| 12 | covariate shift | also called (industry) | NOT FOUND |  |
| 12 | label shift | also called (industry) | NEAR | 427, Glimmer 2.4 — Calibration curves you can trust and ones you cannot (BU |
| 12 | prior probability shift | also called (industry) | NEAR | 26, What probability actually is — and why two engineers can disagree with |
| 12 | model drift | also called (industry) | NEAR | 378, Hume's induction problem, re-translated as distribution shift |
| 12 | silent failure | also called (industry) | NOT FOUND |  |
| 13 | An average that hides one catastrophe | item label | NOT FOUND |  |
| 13 | heavy-tailed | key term (bold) | LITERAL | 20, Why this chapter |
| 13 | tail risk | also called (industry) | NOT FOUND |  |
| 13 | fat tails | also called (industry) | NOT FOUND |  |
| 13 | expected shortfall | also called (industry) | NOT FOUND |  |
| 13 | black swan | also called (industry) | NOT FOUND |  |
| 14 | An average that never settles | item label | NOT FOUND |  |
| 14 | Central Limit Theorem | key term (bold) | LITERAL | 20, Why this chapter |
| 14 | infinite variance | also called (industry) | NOT FOUND |  |
| 14 | an infinite-mean model | also called (industry) | NOT FOUND |  |
| 14 | the law of large numbers failing | also called (industry) | NEAR | 238, The test that is 99% accurate, and the patient it kills |
| 15 | Your own overconfidence | item label | NEAR | 402, Calibration — the most operationally important diagnostic in this chap |
| 15 | overprecision | also called (industry) | NOT FOUND |  |
| 15 | overconfidence | also called (industry) | LITERAL | 419, Calibration — the most operationally important diagnostic in this chap |

## Chapter 3, Data Validation

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A dataset taken for the world | item label | NEAR | 2, Chapter 3 — Data Validation: Reconstructing the Epistemic Frame Behind |
| 1 | selection bias | also called (industry) | NOT FOUND |  |
| 1 | survivorship bias | also called (industry) | NOT FOUND |  |
| 2 | Rows lost in a join | item label | NOT FOUND |  |
| 2 | silent row loss | also called (industry) | NOT FOUND |  |
| 3 | A row count nobody can explain | item label | NOT FOUND |  |
| 3 | row-count reconciliation | also called (industry) | NOT FOUND |  |
| 3 | completeness check | also called (industry) | NOT FOUND |  |
| 3 | volume check | also called (industry) | NOT FOUND |  |
| 4 | Values missing because of what they were | item label | NEAR | 2, Chapter 3 — Data Validation: Reconstructing the Epistemic Frame Behind |
| 4 | Missing completely at random | key term (italic) | LITERAL | 63, The procedural EDA pass — what it sees, and what it structurally canno |
| 4 | Missing at random | key term (italic) | LITERAL | 63, The procedural EDA pass — what it sees, and what it structurally canno |
| 4 | Missing not at random (MNAR | key term (italic) | LITERAL | 63, The procedural EDA pass — what it sees, and what it structurally canno |
| 4 | non-ignorable missingness | also called (industry) | NOT FOUND |  |
| 4 | informative missingness | also called (industry) | NOT FOUND |  |
| 4 | NMAR | also called (industry) | NOT FOUND |  |
| 5 | Time that does not match | item label | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 5 | data drift | also called (industry) | NOT FOUND |  |
| 5 | dataset shift | also called (industry) | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 5 | stale data | also called (industry) | NOT FOUND |  |
| 6 | A label that stands in for something else | item label | NOT FOUND |  |
| 6 | proxy label | also called (industry) | NEAR | 105, Hidden assumptions that hide in plain sight |
| 6 | label bias | also called (industry) | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 6 | construct validity | also called (industry) | NOT FOUND |  |
| 7 | A column that is someone else's model | item label | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 7 | derived feature | also called (industry) | NOT FOUND |  |
| 7 | upstream model dependency | also called (industry) | NOT FOUND |  |
| 7 | data lineage | also called (industry) | NOT FOUND |  |
| 8 | A sample of the easy cases | item label | NEAR | 105, Hidden assumptions that hide in plain sight |
| 8 | convenience sample | also called (industry) | LITERAL | 120, Hidden assumptions that hide in plain sight |
| 8 | sampling bias | also called (industry) | NOT FOUND |  |
| 8 | coverage bias | also called (industry) | NOT FOUND |  |
| 9 | A column typed wrong | item label | NOT FOUND |  |
| 9 | placeholder codes | also called (industry) | NOT FOUND |  |
| 9 | sentinel values | also called (industry) | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 10 | A correlation that sees only straight lines | item label | NEAR | 53, The procedural EDA pass — what it sees, and what it structurally canno |
| 10 | non-linear dependence | also called (industry) | NOT FOUND |  |
| 11 | A number drawn on a weak channel | item label | NOT FOUND |  |
| 11 | perceptual ranking of visual channels | also called (industry) | NOT FOUND |  |
| 11 | misleading chart | also called (industry) | NOT FOUND |  |
| 12 | A flagged value nobody decided about | item label | NOT FOUND |  |
| 12 | anomaly | also called (industry) | LITERAL | 190, Strategic delegation in EDA |
| 12 | Tukey's fences | also called (industry) | NOT FOUND |  |
| 13 | Data that points beyond its schema | item label | NEAR | 142, The access assumption — and where the boundary really lives |
| 13 | Agents of Chaos | key term (italic) | LITERAL | 148, The access assumption — and where the boundary really lives |
| 13 | oversharing | also called (industry) | NOT FOUND |  |
| 14 | A prediction made after the fact | item label | NOT FOUND |  |
| 14 | preregistration | also called (industry) | NOT FOUND |  |
| 14 | hindsight bias | also called (industry) | NOT FOUND |  |
| 15 | An interrogation handed to the AI | item label | NOT FOUND |  |
| 15 | Delegate freely | key term (italic) | LITERAL | 190, Strategic delegation in EDA |
| 15 | Verify before trusting | key term (italic) | LITERAL | 47, Why this chapter |
| 15 | Do not delegate | key term (italic) | LITERAL | 194, Strategic delegation in EDA |
| 15 | automation bias | also called (industry) | NOT FOUND |  |

## Chapter 4, Robustness

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A stand-in for the real feature | item label | NOT FOUND |  |
| 1 | proxy | key term (italic) | LITERAL | 37, Why this chapter |
| 1 | shortcut learning | also called (industry) | NEAR | 489, Synthesis |
| 1 | spurious correlation | also called (industry) | NOT FOUND |  |
| 2 | Patching that only moves the problem | item label | NOT FOUND |  |
| 2 | not | key term (italic) | LITERAL | 5, Chapter 4 — Robustness: What "Understanding" Means When a Pixel Can Br |
| 3 | An account that is still argued, not settled | item label | NOT FOUND |  |
| 3 | this training produced | key term (italic) | LITERAL | 56, What adversarial examples actually expose |
| 4 | Robust", against what? | item label | LITERAL | 18, Chapter 4 — Robustness: What "Understanding" Means When a Pixel Can Br |
| 5 | Two kinds of robust that do not follow each other | item label | NOT FOUND |  |
| 5 | out-of-distribution (OOD) robustness | also called (industry) | NEAR | 33, Why this chapter |
| 6 | The attack nobody tested | item label | NOT FOUND |  |
| 6 | your | key term (italic) | LITERAL | 13, Chapter 4 — Robustness: What "Understanding" Means When a Pixel Can Br |
| 6 | evasion attack | also called (industry) | NOT FOUND |  |
| 7 | The attacker who never touches your model | item label | NOT FOUND |  |
| 7 | transferability | also called (industry) | NOT FOUND |  |
| 7 | black-box transfer attack | also called (industry) | NEAR | 111, A taxonomy of attacks — what each targets |
| 8 | A ceiling that scale cannot lift | item label | NOT FOUND |  |
| 9 | A guarantee with a radius | item label | NEAR | 437, Synthesis — what this chapter leaves you with |
| 10 | One tool offered as the whole answer | item label | NOT FOUND |  |
| 10 | defense in depth | also called (industry) | NOT FOUND |  |
| 10 | gradient masking | also called (industry) | NOT FOUND |  |
| 10 | obfuscated gradients | also called (industry) | LITERAL | 168, The robustness toolkit — what each tool does and what it costs |
| 11 | Same meaning, different answer | item label | NOT FOUND |  |
| 11 | semantic invariance | key term (italic) | LITERAL | 265, Cross-domain transfer — the same structure in different clothes |
| 12 | A change no real person could make | item label | NOT FOUND |  |
| 13 | A signal anyone can type | item label | NOT FOUND |  |
| 13 | Agents of Chaos | key term (italic) | LITERAL | 457, Connections forward |
| 13 | impersonation | also called (industry) | NOT FOUND |  |
| 13 | social engineering | also called (industry) | LITERAL | 403, Glimmer 4.1 — Design the attack, predict the failure mode |
| 14 | Orders hiding in what the agent reads | item label | NOT FOUND |  |
| 14 | indirect prompt injection | also called (industry) | NOT FOUND |  |

## Chapter 5, Model Explainability

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | The fluency trap | item label | LITERAL | 19, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 1 | faithful | also called (industry) | LITERAL | 13, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 2 | A shortcut reported as a reason | item label | NOT FOUND |  |
| 2 | spurious correlation | also called (industry) | NOT FOUND |  |
| 2 | Clever Hans effect | also called (industry) | NOT FOUND |  |
| 3 | Reading an attribution as a cause | item label | NEAR | 41, What SHAP is, and what SHAP isn't |
| 3 | key drivers | also called (industry) | NOT FOUND |  |
| 3 | feature importance | also called (industry) | LITERAL | 397, Where this leaves us |
| 4 | Exact sums, borrowed trust | item label | NOT FOUND |  |
| 5 | Frankenstein rows | item label | NOT FOUND |  |
| 5 | off-manifold | also called (industry) | LITERAL | 243, LIME, in a different shape |
| 5 | out-of-distribution | also called (industry) | NOT FOUND |  |
| 6 | A choice that changes the answer | item label | NOT FOUND |  |
| 6 | interventional | also called (industry) | LITERAL | 63, What SHAP is, and what SHAP isn't |
| 6 | observational | also called (industry) | LITERAL | 53, What SHAP is, and what SHAP isn't |
| 6 | true to the model | also called (industry) | NEAR | 310, A short detour through Wittgenstein |
| 6 | true to the data | also called (industry) | NEAR | 310, A short detour through Wittgenstein |
| 7 | An estimate printed as an exact number | item label | NOT FOUND |  |
| 7 | Computed on the slide (seeded | key term (italic) | NOT FOUND |  |
| 8 | A line from one random draw | item label | NOT FOUND |  |
| 8 | explanation instability | also called (industry) | NOT FOUND |  |
| 8 | unstable explanations | also called (industry) | NOT FOUND |  |
| 9 | A what-if that is only the model's | item label | NEAR | 3, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 9 | recourse | also called (industry) | NOT FOUND |  |
| 9 | algorithmic recourse | also called (industry) | NOT FOUND |  |
| 10 | Signing off the wrong property | item label | NOT FOUND |  |
| 10 | Transparency | key term (italic) | LITERAL | 35, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 10 | Explainability | key term (italic) | LITERAL | 3, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 10 | Interpretability | key term (italic) | LITERAL | 35, Chapter 5 — Model Explainability: Distinguishing Explanation from the  |
| 11 | Same word, two games | item label | NEAR | 310, A short detour through Wittgenstein |
| 12 | A tool blind to the reader | item label | NOT FOUND |  |

## Chapter 6, Bias

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A biased estimator | item label | LITERAL | 42, What "bias" actually means |
| 1 | estimator | key term (italic) | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 1 | biased | key term (italic) | LITERAL | 8, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 1 | systematic error | also called (industry) | NEAR | 2, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 1 | random error | also called (industry) | NEAR | 86, The two that enter at the keyboard |
| 1 | precise | also called (industry) | LITERAL | 16, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 1 | accurate | also called (industry) | LITERAL | 88, The two that enter at the keyboard |
| 2 | Selection bias | item label | LITERAL | 66, Selection bias |
| 2 | inverse probability weighting | key term (italic) | LITERAL | 72, Selection bias |
| 2 | survivorship bias | also called (industry) | NOT FOUND |  |
| 2 | sample selection bias | also called (industry) | LITERAL | 159, How bias types compound |
| 3 | Sampling bias | item label | LITERAL | 88, The two that enter at the keyboard |
| 3 | frame | key term (italic) | LITERAL | 44, What "bias" actually means |
| 3 | coverage bias | also called (industry) | NOT FOUND |  |
| 3 | undercoverage | also called (industry) | NOT FOUND |  |
| 3 | convenience sample | also called (industry) | NOT FOUND |  |
| 4 | Confirmation bias | item label | LITERAL | 76, The five that enter through the humans in the loop |
| 4 | motivated reasoning | also called (industry) | NOT FOUND |  |
| 4 | cherry-picking | also called (industry) | NOT FOUND |  |
| 5 | Observer bias | item label | LITERAL | 76, The five that enter through the humans in the loop |
| 5 | people | key term (italic) | LITERAL | 34, What "bias" actually means |
| 5 | Cohen's kappa | key term (italic) | LITERAL | 78, The five that enter through the humans in the loop |
| 5 | observer-expectancy effect | also called (industry) | NOT FOUND |  |
| 5 | experimenter bias | also called (industry) | NOT FOUND |  |
| 5 | annotator bias | also called (industry) | NEAR | 74, The five that enter through the humans in the loop |
| 6 | Data-coding bias | item label | LITERAL | 76, The five that enter through the humans in the loop |
| 6 | items | key term (italic) | LITERAL | 82, The five that enter through the humans in the loop |
| 6 | ambiguous labels | also called (industry) | NEAR | 74, The five that enter through the humans in the loop |
| 6 | label noise | also called (industry) | NEAR | 183, The dataset as epistemic artifact |
| 6 | annotation guideline | also called (industry) | NOT FOUND |  |
| 7 | Publication bias | item label | LITERAL | 76, The five that enter through the humans in the loop |
| 7 | funnel plot | key term (italic) | LITERAL | 82, The five that enter through the humans in the loop |
| 7 | Trim-and-fill | key term (italic) | LITERAL | 82, The five that enter through the humans in the loop |
| 7 | file drawer problem | also called (industry) | NOT FOUND |  |
| 7 | reporting bias | also called (industry) | NEAR | 2, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 8 | Self-report bias | item label | LITERAL | 76, The five that enter through the humans in the loop |
| 8 | Also called | key term (bold) | NOT FOUND |  |
| 8 | social desirability | key term (italic) | LITERAL | 76, The five that enter through the humans in the loop |
| 8 | response bias | key term (italic) | NEAR | 32, What "bias" actually means |
| 8 | recall bias | key term (italic) | NEAR | 417, Application |
| 9 | Data-entry bias | item label | LITERAL | 88, The two that enter at the keyboard |
| 9 | dirty data | also called (industry) | NOT FOUND |  |
| 9 | data quality | also called (industry) | LITERAL | 100, Historical bias |
| 10 | Historical bias | item label | LITERAL | 90, Historical bias |
| 10 | was | key term (italic) | LITERAL | 8, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 10 | should | key term (italic) | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 10 | historical bias | key term (italic) | LITERAL | 90, Historical bias |
| 11 | Label bias | item label | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 11 | proxy label | also called (industry) | NEAR | 90, Historical bias |
| 11 | label choice bias | also called (industry) | NEAR | 183, The dataset as epistemic artifact |
| 11 | measurement bias | also called (industry) | NEAR | 74, The five that enter through the humans in the loop |
| 12 | Structural bias, and the fix at the wrong place | item label | NEAR | 2, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 12 | systemic bias | also called (industry) | NEAR | 108, Implicit bias |
| 12 | institutional bias | also called (industry) | NEAR | 126, Three flavors of bias, mapped to the ten types |
| 13 | Two fairness metrics, both right | item label | NEAR | 183, The dataset as epistemic artifact |
| 13 | Calibration parity | key term (italic) | LITERAL | 191, The dataset as epistemic artifact |
| 13 | Equal false-positive rate | key term (italic) | LITERAL | 199, The dataset as epistemic artifact |
| 13 | predictive parity | also called (industry) | NEAR | 183, The dataset as epistemic artifact |
| 13 | error rate balance | also called (industry) | NOT FOUND |  |
| 13 | equalized odds | also called (industry) | LITERAL | 358, What would change my mind — and what I am still puzzling about |
| 13 | impossibility theorem | also called (industry) | LITERAL | 234, The dataset as epistemic artifact |
| 13 | Chouldechova result | also called (industry) | NOT FOUND |  |
| 14 | Seeing mistaken for doing | item label | NOT FOUND |  |
| 14 | Rung 1 | key term (bold) | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 14 | Rung 2 | key term (bold) | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 14 | set | key term (italic) | LITERAL | 12, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 14 | causes | key term (italic) | LITERAL | 16, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 14 | observational versus interventional | also called (industry) | NOT FOUND |  |
| 14 | correlation is not causation | also called (industry) | NOT FOUND |  |
| 14 | Counterfactual fairness | also called (industry) | NEAR | 238, Pearl's Ladder — Rungs 1 and 2 |
| 14 | perturbation test | also called (industry) | NOT FOUND |  |
| 15 | Leverage outside your reach | item label | NEAR | 338, A limit case: when the leverage is upstream of your pipeline — and who |
| 15 | owner | key term (italic) | LITERAL | 22, Chapter 6 — Bias: Where It Enters and Who Is Responsible |
| 15 | Agents of Chaos | key term (italic) | LITERAL | 342, A limit case: when the leverage is upstream of your pipeline — and who |
| 15 | model provider's | key term (italic) | LITERAL | 342, A limit case: when the leverage is upstream of your pipeline — and who |
| 15 | supply-chain risk | also called (industry) | NOT FOUND |  |
| 15 | third-party model risk | also called (industry) | NOT FOUND |  |
| 15 | inherited bias | also called (industry) | NOT FOUND |  |

## Chapter 7, Fairness Metrics

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | Equal yes-rates, hidden errors | item label | NOT FOUND |  |
| 1 | statistical parity | also called (industry) | LITERAL | 43, Three definitions |
| 1 | group fairness | also called (industry) | LITERAL | 325, The decomposition |
| 1 | independence | also called (industry) | NOT FOUND |  |
| 1 | four-fifths rule | also called (industry) | NOT FOUND |  |
| 2 | A score that means the same, errors that do not | item label | NEAR | 73, The arithmetic — the actual proof, not a gesture |
| 2 | predictive parity | also called (industry) | LITERAL | 57, Three definitions |
| 2 | sufficiency | also called (industry) | NOT FOUND |  |
| 3 | Equal errors, a score that means different things | item label | NEAR | 73, The arithmetic — the actual proof, not a gesture |
| 3 | error-rate balance | also called (industry) | NEAR | 73, The arithmetic — the actual proof, not a gesture |
| 3 | separation | also called (industry) | NOT FOUND |  |
| 3 | equal opportunity | also called (industry) | NEAR | 39, Three definitions |
| 4 | All three claimed at once | item label | NOT FOUND |  |
| 4 | fairness trade-off | also called (industry) | NEAR | 335, What the GE Index does not do |
| 4 | impossibility result | also called (industry) | NEAR | 3, Chapter 7 — Fairness Metrics: Choosing a Definition and Defending It |
| 5 | Two true claims, one values fight | item label | NOT FOUND |  |
| 6 | A definition chosen by default | item label | NEAR | 3, Chapter 7 — Fairness Metrics: Choosing a Definition and Defending It |
| 6 | Also called | key term (bold) | NEAR | 39, Three definitions |
| 6 | defended choice | key term (italic) | LITERAL | 373, The defense as deliverable |
| 6 | fairwashing | key term (italic) | NOT FOUND |  |
| 7 | A decision with no owner | item label | NOT FOUND |  |
| 7 | silently | key term (italic) | LITERAL | 389, Who should have decided |
| 7 | sign-off | also called (industry) | NOT FOUND |  |
| 7 | governance | also called (industry) | NOT FOUND |  |
| 8 | A fair score on the wrong target | item label | NOT FOUND |  |
| 8 | label bias | also called (industry) | NEAR | 343, The toolkit and what it cannot do |
| 8 | proxy label | also called (industry) | NOT FOUND |  |
| 8 | construct validity | also called (industry) | NOT FOUND |  |
| 8 | measurement validity | also called (industry) | NOT FOUND |  |
| 9 | A similarity measure nobody examined | item label | NOT FOUND |  |
| 9 | fairness through awareness | key term (italic) | LITERAL | 205, Fairness through awareness vs. unawareness |
| 9 | task-specific similarity metric | key term (italic) | NEAR | 185, The $(D, d)$-Lipschitz condition |
| 10 | Unawareness taken for fairness | item label | NOT FOUND |  |
| 10 | direct | key term (italic) | LITERAL | 157, The COMPAS case — the theorem in public |
| 10 | proxy variable | also called (industry) | NOT FOUND |  |
| 10 | proxy discrimination | also called (industry) | NOT FOUND |  |
| 11 | One correlation, three causes | item label | NEAR | 219, Structural causal models and the fairness question |
| 11 | Indirect | key term (italic) | LITERAL | 209, Fairness through awareness vs. unawareness |
| 11 | Spurious | key term (italic) | LITERAL | 233, Structural causal models and the fairness question |
| 11 | path-specific effects | also called (industry) | NOT FOUND |  |
| 11 | mediation analysis | also called (industry) | NOT FOUND |  |
| 11 | Mediator | also called (industry) | LITERAL | 232, Structural causal models and the fairness question |
| 11 | confounder | also called (industry) | LITERAL | 233, Structural causal models and the fairness question |
| 12 | A feature downstream of the group | item label | NEAR | 237, Counterfactual fairness |
| 12 | flip test | also called (industry) | NOT FOUND |  |
| 12 | swap test | also called (industry) | NOT FOUND |  |
| 13 | Unfairness hiding inside the groups | item label | NOT FOUND |  |
| 13 | between-group | key term (italic) | LITERAL | 31, Chapter 7 — Fairness Metrics: Choosing a Definition and Defending It |
| 13 | within-group | key term (italic) | LITERAL | 31, Chapter 7 — Fairness Metrics: Choosing a Definition and Defending It |
| 13 | Theil index | also called (industry) | LITERAL | 304, The formula |
| 13 | mean log deviation | also called (industry) | LITERAL | 302, The formula |
| 13 | Atkinson index | also called (industry) | NOT FOUND |  |
| 14 | A dial set without saying so | item label | NOT FOUND |  |
| 15 | A fix presented as a resolution | item label | NOT FOUND |  |
| 15 | Pre-processing | key term (italic) | LITERAL | 347, The toolkit and what it cannot do |
| 15 | In-processing | key term (italic) | LITERAL | 349, The toolkit and what it cannot do |
| 15 | Post-processing | key term (italic) | LITERAL | 351, The toolkit and what it cannot do |
| 15 | bias mitigation | also called (industry) | NOT FOUND |  |
| 15 | debiasing | also called (industry) | LITERAL | 353, The toolkit and what it cannot do |

## Chapter 8, Agents

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | The false success report | item label | NEAR | 3, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 2 | Trusting a name | item label | NOT FOUND |  |
| 2 | confused deputy | also called (industry) | NOT FOUND |  |
| 3 | Authority laundering | item label | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 4 | Prompt injection: instructions hiding in data | item label | NOT FOUND |  |
| 5 | A loop with no limit | item label | NEAR | 256, The remaining documented cases, compactly |
| 5 | runaway loop | also called (industry) | LITERAL | 343, When agents talk to each other |
| 6 | Reach beyond need | item label | NOT FOUND |  |
| 6 | need to know | key term (italic) | NEAR | 410, What this asks of the supervisor |
| 6 | least privilege | also called (industry) | NOT FOUND |  |
| 6 | blast radius | also called (industry) | NOT FOUND |  |
| 7 | Concession with no limit | item label | NEAR | 212, Case #7: Agent Harm |
| 8 | An irreversible action with no gate | item label | NEAR | 393, A boundary worth defending |
| 8 | human in the loop | also called (industry) | NOT FOUND |  |
| 9 | The wrong audience | item label | NEAR | 93, What agents are lacking: the three core deficits |
| 10 | Mistaking itself for someone else | item label | NOT FOUND |  |
| 11 | Small errors that add up | item label | NOT FOUND |  |
| 12 | Reach beyond understanding | item label | NOT FOUND |  |
| 12 | autonomy-competence gap | key term (italic) | LITERAL | 65, The laboratory: what OpenClaw actually was |
| 12 | excessive agency | also called (industry) | NOT FOUND |  |
| 13 | Borrowed values | item label | NOT FOUND |  |
| 14 | A boundary that is declared but not enforced | item label | NOT FOUND |  |
| 15 | A refusal that held for the wrong reason | item label | NOT FOUND |  |
| 0 | false success report | key term (listed by hand) | LITERAL | 15, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | displayed identity | key term (listed by hand) | LITERAL | 252, Case #8: Owner Identity Spoofing |
| 0 | verified identity | key term (listed by hand) | LITERAL | 252, Case #8: Owner Identity Spoofing |
| 0 | authority laundering | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | effective data scope | key term (listed by hand) | LITERAL | 182, Case #3: Disclosure of Sensitive Information |
| 0 | autonomy-competence gap | key term (listed by hand) | LITERAL | 65, The laboratory: what OpenClaw actually was |
| 0 | consequence system | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | prediction system | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | contingent failure | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | fundamental failure | key term (listed by hand) | LITERAL | 284, Fundamental vs. contingent failures |
| 0 | prompt injection | key term (listed by hand) | LITERAL | 97, What agents are lacking: the three core deficits |
| 0 | observability modeling | key term (listed by hand) | LITERAL | 288, Fundamental vs. contingent failures |
| 0 | cascading hallucination | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | resource exhaustion | key term (listed by hand) | LITERAL | 19, Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave |
| 0 | identity confusion | key term (listed by hand) | LITERAL | 341, When agents talk to each other |
| 0 | social coherence failure | key term (listed by hand) | LITERAL | 109, Mapping to the four failure categories |
| 0 | no self-model | key term (listed by hand) | LITERAL | 99, What agents are lacking: the three core deficits |
| 0 | no stakeholder model | key term (listed by hand) | LITERAL | 95, What agents are lacking: the three core deficits |
| 0 | no private deliberation surface | key term (listed by hand) | LITERAL | 101, What agents are lacking: the three core deficits |
| 0 | proportionality | key term (listed by hand) | LITERAL | 222, Case #7: Agent Harm |
| 0 | documented scope | key term (listed by hand) | LITERAL | 198, Case #3: Disclosure of Sensitive Information |
| 0 | effective scope | key term (listed by hand) | LITERAL | 41, From prediction to action |
| 0 | need to know | key term (listed by hand) | NEAR | 410, What this asks of the supervisor |
| 0 | blast radius | key term (listed by hand) | NOT FOUND |  |
| 0 | least privilege | key term (listed by hand) | NOT FOUND |  |
| 0 | human in the loop | key term (listed by hand) | NOT FOUND |  |
| 0 | excessive agency | key term (listed by hand) | NOT FOUND |  |
| 0 | confused deputy | key term (listed by hand) | NOT FOUND |  |
| 0 | runaway loop | key term (listed by hand) | LITERAL | 343, When agents talk to each other |

## Chapter 9, Delegation and Trust

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A partition passed off as a contract | item label | NOT FOUND |  |
| 1 | human in the loop | also called (industry) | NOT FOUND |  |
| 2 | A handoff condition no stranger can test | item label | NEAR | 40, The handoff condition: the contract, not the partition |
| 2 | acceptance criteria | also called (industry) | LITERAL | 143, The full delegation map structure |
| 2 | definition of done | also called (industry) | NOT FOUND |  |
| 3 | Documentation quality read as decision quality | item label | NEAR | 2, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 3 | review | key term (italic) | LITERAL | 10, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 3 | better decisions | key term (italic) | LITERAL | 24, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 3 | governance theater | also called (industry) | NOT FOUND |  |
| 3 | audit-washing | also called (industry) | NOT FOUND |  |
| 4 | An unsupervised pipeline (map items 5 to 8 missing | item label | NEAR | 122, The full delegation map structure |
| 4 | silent failure | also called (industry) | NOT FOUND |  |
| 5 | No plausibility audit log | item label | NEAR | 68, The Five Supervisory Capacities as pipeline jobs |
| 5 | sanity check | also called (industry) | LITERAL | 100, The Boondoggle questions |
| 5 | Confidently wrong | also called (industry) | LITERAL | 86, The Five Supervisory Capacities as pipeline jobs |
| 6 | No scoping doc | item label | NOT FOUND |  |
| 6 | Type III error | also called (industry) | NEAR | 122, The full delegation map structure |
| 6 | problem framing | also called (industry) | NEAR | 165, Generating the Boondoggle Score |
| 6 | requirements gap | also called (industry) | NOT FOUND |  |
| 7 | No tool inventory | item label | NEAR | 68, The Five Supervisory Capacities as pipeline jobs |
| 7 | least privilege | also called (industry) | NOT FOUND |  |
| 7 | excessive agency | also called (industry) | NOT FOUND |  |
| 8 | No review log with a named reviewer | item label | NEAR | 40, The handoff condition: the contract, not the partition |
| 8 | rubber stamp | also called (industry) | NOT FOUND |  |
| 8 | automation bias | also called (industry) | NOT FOUND |  |
| 8 | human review theater | also called (industry) | NOT FOUND |  |
| 9 | No signed decision log | item label | NEAR | 68, The Five Supervisory Capacities as pipeline jobs |
| 9 | accountability gap | also called (industry) | NOT FOUND |  |
| 9 | diffusion of responsibility | also called (industry) | NOT FOUND |  |
| 9 | single accountable owner | also called (industry) | NOT FOUND |  |
| 10 | Delegating by feel, not by the work split | item label | NOT FOUND |  (Bear's name for the five-question assessment; not in the book) |
| 10 | AI execution | key term (bold) | LITERAL | 110, The Boondoggle questions |
| 10 | human-only | key term (bold) | LITERAL | 102, The Boondoggle questions |
| 10 | hybrid | key term (bold) | LITERAL | 46, The handoff condition: the contract, not the partition |
| 10 | verification cost | key term (italic) | LITERAL | 100, The Boondoggle questions |
| 10 | stakes | key term (italic) | LITERAL | 44, The handoff condition: the contract, not the partition |
| 10 | distribution match | key term (italic) | LITERAL | 104, The Boondoggle questions |
| 10 | reversibility | key term (italic) | LITERAL | 106, The Boondoggle questions |
| 10 | audit trail clarity | key term (italic) | LITERAL | 108, The Boondoggle questions |
| 10 | documented justification for the delegation choice | key term (italic) | LITERAL | 110, The Boondoggle questions |
| 10 | function allocation | also called (industry) | NOT FOUND |  |
| 10 | levels of automation | also called (industry) | NOT FOUND |  |
| 11 | Verification cost | item label | LITERAL | 100, The Boondoggle questions |
| 11 | verification tax | also called (industry) | NOT FOUND |  |
| 12 | An irreversible action with no human gate | item label | NEAR | 94, The Boondoggle questions |
| 12 | human approval gate | also called (industry) | LITERAL | 117, The Boondoggle questions |
| 12 | one-way door | also called (industry) | NOT FOUND |  |
| 12 | two-way door | also called (industry) | NOT FOUND |  |
| 13 | Overtrust | item label | LITERAL | 222, Trust calibration |
| 13 | Calibrated trust | key term (italic) | LITERAL | 216, Trust calibration |
| 13 | Overtrust | key term (italic) | LITERAL | 222, Trust calibration |
| 13 | Undertrust | key term (italic) | LITERAL | 220, Trust calibration |
| 13 | automation complacency | also called (industry) | LITERAL | 224, Trust calibration |
| 13 | misuse | also called (industry) | LITERAL | 88, The Five Supervisory Capacities as pipeline jobs |
| 13 | disuse | also called (industry) | LITERAL | 224, Trust calibration |
| 13 | algorithm aversion | also called (industry) | NOT FOUND |  |
| 14 | Monitoring data nobody reads | item label | NEAR | 2, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 14 | model monitoring | also called (industry) | NEAR | 2, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 14 | alert fatigue | also called (industry) | NOT FOUND |  |
| 15 | A disclosure that is a checkbox | item label | NEAR | 2, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 15 | compliance theater | also called (industry) | NOT FOUND |  |
| 15 | checkbox compliance | also called (industry) | NEAR | 2, Chapter 9 — Delegation, Trust, and the Supervisory Role |
| 15 | AI usage log | also called (industry) | NOT FOUND |  |

## Chapter 10, Visualization Under Validation

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | A headline number that argues "this is enough | item label | NOT FOUND |  |
| 2 | A channel that cannot carry the number | item label | NOT FOUND |  |
| 2 | perception hierarchy | also called (industry) | LITERAL | 28, Why this chapter |
| 2 | [verify] | also called (industry) | LITERAL | 1, (front matter) |
| 3 | Color that steers the eye | item label | NOT FOUND |  |
| 3 | preattentive attributes | also called (industry) | NOT FOUND |  |
| 4 | Decoration that bends the size | item label | NOT FOUND |  |
| 4 | chartjunk | key term (italic) | LITERAL | 187, The deceptive visualization catalog |
| 4 | data-ink ratio | also called (industry) | NOT FOUND |  |
| 4 | ducks | also called (industry) | NOT FOUND |  |
| 5 | A label that prejudges | item label | LITERAL | 205, The deceptive visualization catalog |
| 5 | loaded | also called (industry) | NOT FOUND |  |
| 5 | biased | also called (industry) | LITERAL | 111, Uncertainty has two faces |
| 6 | A truncated axis | item label | LITERAL | 221, Four cases that teach the catalog |
| 6 | lie factor | also called (industry) | NOT FOUND |  |
| 6 | The Visual Display of Quantitative Information | also called (industry) | LITERAL | 201, The deceptive visualization catalog |
| 7 | An axis that runs backwards | item label | NOT FOUND |  |
| 7 | Calling Bullshit | key term (italic) | LITERAL | 225, Four cases that teach the catalog |
| 7 | reversed | also called (industry) | LITERAL | 320, Glimmer 10.1 — Build the honest version, build the misleading version |
| 7 | flipped | also called (industry) | LITERAL | 225, Four cases that teach the catalog |
| 7 | upside-down | also called (industry) | NOT FOUND |  |
| 8 | Panels with different ranges | item label | NEAR | 6, Two dashboards built from one CSV |
| 8 | free scales | also called (industry) | NOT FOUND |  |
| 9 | A scale that squeezes the part that matters | item label | NOT FOUND |  |
| 9 | log vs linear scale | also called (industry) | NEAR | 183, The deceptive visualization catalog |
| 10 | A summary that hides the tail | item label | NOT FOUND |  |
| 10 | Anscombe's quartet | also called (industry) | NOT FOUND |  |
| 10 | Datasaurus Dozen | also called (industry) | NOT FOUND |  |
| 11 | A time window that flatters | item label | NOT FOUND |  |
| 11 | cherry-picking | also called (industry) | NOT FOUND |  |
| 11 | end-point | also called (industry) | NOT FOUND |  |
| 11 | start-date | also called (industry) | NOT FOUND |  |
| 12 | A finding with no baseline | item label | NEAR | 183, The deceptive visualization catalog |
| 12 | all | key term (italic) | LITERAL | 12, Two dashboards built from one CSV |
| 13 | Uncertainty shown only where it helps | item label | NOT FOUND |  |
| 13 | hidden error bars | also called (industry) | NOT FOUND |  |
| 14 | A tie drawn as a difference | item label | NEAR | 155, Showing the trust — techniques for epistemic uncertainty |
| 14 | The chapter flags this case itself | key term (bold) | NEAR | 213, Four cases that teach the catalog |
| 14 | statistical tie | also called (industry) | LITERAL | 221, Four cases that teach the catalog |
| 14 | dead heat | also called (industry) | NOT FOUND |  |
| 15 | A proxy under a confident title | item label | NOT FOUND |  |
| 15 | proxy variable | also called (industry) | NOT FOUND |  |
| 15 | construct validity | also called (industry) | NOT FOUND |  |

## Chapter 11, Communicating Uncertainty

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | Same numbers, a stronger verb | item label | NEAR | 3, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | We observe | key term (italic) | LITERAL | 13, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | We conclude | key term (italic) | LITERAL | 9, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | find | key term (italic) | LITERAL | 7, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | observe | key term (italic) | LITERAL | 13, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | conclude | key term (italic) | LITERAL | 9, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | we demonstrate | key term (italic) | LITERAL | 59, The working hierarchy |
| 1 | this shows | key term (italic) | NOT FOUND |  |
| 1 | overclaiming | also called (industry) | LITERAL | 435, Where this leaves us |
| 1 | overstating | also called (industry) | NOT FOUND |  |
| 1 | hedges | also called (industry) | LITERAL | 25, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 1 | boosters | also called (industry) | NOT FOUND |  |
| 2 | A claim with no evidence row behind it | item label | NEAR | 86, Two readers, one document |
| 2 | show | key term (italic) | LITERAL | 39, The classical move: warranted assertion |
| 2 | demonstrate | key term (italic) | LITERAL | 39, The classical move: warranted assertion |
| 2 | prove | key term (italic) | LITERAL | 35, The classical move: warranted assertion |
| 3 | A confident verb written by the AI | item label | NOT FOUND |  |
| 3 | suggests | key term (italic) | LITERAL | 39, The classical move: warranted assertion |
| 3 | observes | key term (italic) | LITERAL | 13, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 3 | suggest | key term (italic) | LITERAL | 39, The classical move: warranted assertion |
| 3 | Clearly shows | key term (italic) | LITERAL | 471, Application |
| 3 | conclusively demonstrates | key term (italic) | LITERAL | 369, The verb taxonomy applied to AI output |
| 3 | resolves | key term (italic) | LITERAL | 471, Application |
| 3 | state-of-the-art | key term (italic) | LITERAL | 104, Two readers, one document |
| 3 | overgeneralization | also called (industry) | NOT FOUND |  |
| 3 | Royal Society Open Science | also called (industry) | NOT FOUND |  |
| 3 | overconfident wording | also called (industry) | NOT FOUND |  |
| 4 | One score, three parts | item label | NOT FOUND |  |
| 4 | resolution | key term (italic) | LITERAL | 136, The Brier score: a proper scoring rule |
| 4 | calibration | key term (italic) | LITERAL | 17, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 4 | reliability | also called (industry) | LITERAL | 25, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 4 | resolution | also called (industry) | LITERAL | 136, The Brier score: a proper scoring rule |
| 4 | uncertainty | also called (industry) | LITERAL | 3, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 4 | sharpness | also called (industry) | NOT FOUND |  |
| 5 | An ECE with no bin count | item label | NOT FOUND |  |
| 5 | [verify] | key term (bold) | LITERAL | 1, (front matter) |
| 5 | more | key term (italic) | LITERAL | 9, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 5 | equal-mass | also called (industry) | NOT FOUND |  |
| 6 | Calibrated on average, not for the group | item label | NOT FOUND |  |
| 6 | subgroup calibration | also called (industry) | LITERAL | 187, Subgroup calibration: where aggregate metrics lie |
| 6 | multicalibration | also called (industry) | NOT FOUND |  |
| 6 | calibration within groups | also called (industry) | NOT FOUND |  |
| 7 | What the metric cannot see | item label | NEAR | 116, Metrics and measures of trust calibration |
| 7 | construct validity failure | key term (italic) | LITERAL | 302, What calibration metrics cannot see |
| 7 | proxy label | also called (industry) | NEAR | 298, What calibration metrics cannot see |
| 7 | label mismatch | also called (industry) | NOT FOUND |  |
| 7 | construct validity | also called (industry) | LITERAL | 302, What calibration metrics cannot see |
| 7 | discrimination | also called (industry) | LITERAL | 132, The Brier score: a proper scoring rule |
| 7 | calibration | also called (industry) | LITERAL | 17, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 8 | Good on average, failing at the site | item label | NOT FOUND |  |
| 8 | External validation | key term (italic) | LITERAL | 191, Subgroup calibration: where aggregate metrics lie |
| 8 | external validation | also called (industry) | LITERAL | 191, Subgroup calibration: where aggregate metrics lie |
| 8 | dataset shift | also called (industry) | NEAR | 45, The working hierarchy |
| 8 | site-to-site variation | also called (industry) | NEAR | 238, From calibration metrics to trust claims |
| 8 | model drift | also called (industry) | NEAR | 86, Two readers, one document |
| 8 | calibration drift | also called (industry) | NEAR | 86, Two readers, one document |
| 9 | A fix for the numbers, not the cause | item label | NEAR | 212, Temperature scaling: the fix and its limits |
| 9 | post-hoc calibration | also called (industry) | LITERAL | 228, Temperature scaling: the fix and its limits |
| 9 | calibration under dataset shift | also called (industry) | NEAR | 45, The working hierarchy |
| 10 | A guarantee on average | item label | NEAR | 272, The conformal prediction guarantee — and what it costs |
| 10 | set | key term (italic) | LITERAL | 7, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 10 | exchangeable | key term (italic) | LITERAL | 284, The conformal prediction guarantee — and what it costs |
| 10 | marginal | key term (italic) | LITERAL | 284, The conformal prediction guarantee — and what it costs |
| 10 | marginal coverage | also called (industry) | NEAR | 272, The conformal prediction guarantee — and what it costs |
| 10 | conditional coverage | also called (industry) | NEAR | 272, The conformal prediction guarantee — and what it costs |
| 11 | A number with no doubt around it | item label | NOT FOUND |  |
| 11 | the result is approximately 0.85 | key term (italic) | LITERAL | 328, Saying you do not know in writing |
| 11 | error bars | also called (industry) | LITERAL | 322, Saying you do not know in writing |
| 11 | margin of error | also called (industry) | NOT FOUND |  |
| 11 | uncertainty quantification | also called (industry) | NEAR | 421, Where this leaves us |
| 12 | A hedge that says nothing | item label | NOT FOUND |  |
| 12 | boilerplate limitations | also called (industry) | NOT FOUND |  |
| 13 | Two kinds of doubt | item label | NEAR | 3, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 13 | Epistemic | key term (italic) | LITERAL | 5, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 13 | Aleatoric | key term (italic) | LITERAL | 25, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 13 | reducible | also called (industry) | LITERAL | 330, Saying you do not know in writing |
| 13 | irreducible | also called (industry) | LITERAL | 330, Saying you do not know in writing |
| 13 | model uncertainty | also called (industry) | NEAR | 3, Chapter 11 — Communicating Uncertainty: Calibrating Claims to Evidence |
| 13 | data uncertainty | also called (industry) | NEAR | 86, Two readers, one document |
| 14 | A summary that says less than the detail | item label | NOT FOUND |  |
| 14 | executive summary | also called (industry) | LITERAL | 90, Two readers, one document |
| 14 | TL;DR | also called (industry) | LITERAL | 1, (front matter) |
| 14 | BLUF | also called (industry) | NOT FOUND |  |
| 15 | The mismatch only a second reader sees | item label | NOT FOUND |  |
| 15 | internal peer review | also called (industry) | NOT FOUND |  |
| 15 | red team review | also called (industry) | NEAR | 517, LLM Exercise — Chapter 11: Communicating Uncertainty |

## Chapter 12, Accountability

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | One name on the report | item label | NEAR | 3, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 1 | necessary | key term (italic) | LITERAL | 33, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 1 | sufficient | key term (italic) | LITERAL | 33, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 1 | problem of many hands | also called (industry) | NOT FOUND |  |
| 1 | moral crumple zone | also called (industry) | NOT FOUND |  |
| 2 | Nobody answerable (the responsibility gap | item label | NEAR | 64, AI as extended mind: what the capacities actually are |
| 2 | responsibility gap | key term (italic) | LITERAL | 35, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 2 | accountability gap | also called (industry) | NOT FOUND |  |
| 2 | accountability sink | also called (industry) | NOT FOUND |  |
| 3 | Blame aimed where it changes nothing | item label | NOT FOUND |  |
| 3 | Also called | key term (bold) | NEAR | 54, Why humans must be in the loop: the cognitive argument |
| 3 | Kantian | key term (italic) | LITERAL | 48, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 3 | utilitarian | key term (italic) | LITERAL | 48, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 3 | upstream | key term (italic) | LITERAL | 168, Two frameworks, one topology |
| 4 | A sign-off with the shape and no substance | item label | NEAR | 3, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 4 | shape | key term (italic) | LITERAL | 17, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 4 | substance | key term (italic) | LITERAL | 17, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 4 | governance theater | also called (industry) | NOT FOUND |  |
| 4 | checkbox compliance | also called (industry) | NOT FOUND |  |
| 5 | A human who only clicks approve | item label | NEAR | 229, The regulatory landscape |
| 5 | Low stakes, reversible | key term (italic) | LITERAL | 270, Stages and stakes: a taxonomy of where human oversight is not optional |
| 5 | Moderate, partly recoverable | key term (italic) | NOT FOUND |  |
| 5 | High, irreversible | key term (italic) | LITERAL | 276, Stages and stakes: a taxonomy of where human oversight is not optional |
| 5 | rubber-stamping | also called (industry) | NOT FOUND |  |
| 5 | automation bias | also called (industry) | NOT FOUND |  |
| 5 | human-in-the-loop theater | also called (industry) | NOT FOUND |  |
| 6 | A signature that cannot say no | item label | NEAR | 3, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 6 | stop-work authority | also called (industry) | NEAR | 241, Closing Pearl's Rung 3 |
| 6 | andon cord | also called (industry) | NOT FOUND |  |
| 7 | A specification too vague to fail | item label | NEAR | 184, The five accountability requirements and the tiers they depend on |
| 8 | A log nobody can read back | item label | NOT FOUND |  |
| 9 | Recourse on paper only | item label | NEAR | 229, The regulatory landscape |
| 9 | contestability | also called (industry) | NOT FOUND |  |
| 9 | redress | also called (industry) | LITERAL | 290, Why responsibility resists clean attribution |
| 10 | A second opinion that is the first again | item label | NOT FOUND |  |
| 10 | common cause failure | key term (italic) | LITERAL | 133, The Gödel argument |
| 10 | correlated errors | also called (industry) | NEAR | 139, Common cause failure |
| 10 | self-preference bias | also called (industry) | NOT FOUND |  |
| 11 | A sanction that lands on no one | item label | NEAR | 64, AI as extended mind: what the capacities actually are |
| 12 | A clean bill of health | item label | LITERAL | 223, The gate: the attestation you sign |
| 12 | attestation | key term (italic) | LITERAL | 212, The gate: the attestation you sign |
| 12 | JAMA Internal Medicine | key term (italic) | LITERAL | 406, Challenge |
| 12 | external validation | also called (industry) | LITERAL | 406, Challenge |
| 12 | independent local validation | also called (industry) | LITERAL | 406, Challenge |
| 13 | A fix to the model, not the regime | item label | NEAR | 64, AI as extended mind: what the capacities actually are |
| 13 | governance counterfactual | key term (italic) | LITERAL | 48, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 13 | latent conditions | also called (industry) | NOT FOUND |  |
| 14 | An argument that sounds stronger than its support | item label | NOT FOUND |  |
| 14 | The Gödel step | key term (italic) | NOT FOUND |  |
| 14 | answerability | key term (italic) | LITERAL | 35, Chapter 12 — Accountability: Who Is Responsible When the System Fails? |
| 14 | The taxonomy | key term (italic) | LITERAL | 62, Why humans must be in the loop: the cognitive argument |
| 15 | A failure no one's choices caused | item label | NOT FOUND |  |
| 15 | normal accident | also called (industry) | NOT FOUND |  |

## Chapter 13, The Limits of AI

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | Passed every test, wrong question | item label | NEAR | 6, The model that passed every test and failed in deployment |
| 1 | Type III error | also called (industry) | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 2 | A fluent answer to a different question | item label | NEAR | 6, The model that passed every test and failed in deployment |
| 2 | meaning | key term (italic) | LITERAL | 30, Why this chapter |
| 2 | symbol grounding problem | also called (industry) | NEAR | 36, Three categorical limits |
| 2 | stochastic parrots | also called (industry) | LITERAL | 63, Three categorical limits |
| 3 | Aboutness that lives in the reader | item label | NOT FOUND |  |
| 3 | Intentionality | key term (italic) | LITERAL | 30, Why this chapter |
| 3 | derived intentionality | also called (industry) | NOT FOUND |  |
| 3 | ELIZA effect | also called (industry) | NOT FOUND |  |
| 4 | The edge of the data | item label | NEAR | 36, Three categorical limits |
| 4 | data-world gap | key term (italic) | LITERAL | 30, Why this chapter |
| 4 | out-of-distribution generalization | also called (industry) | NOT FOUND |  |
| 4 | distribution shift | also called (industry) | LITERAL | 79, Three categorical limits |
| 4 | coverage gap | also called (industry) | NOT FOUND |  |
| 4 | unknown unknowns | also called (industry) | NOT FOUND |  |
| 5 | Confidence rises until the day it fails | item label | NOT FOUND |  |
| 5 | Mediocristan | key term (italic) | LITERAL | 83, Three categorical limits |
| 5 | Extremistan | key term (italic) | LITERAL | 83, Three categorical limits |
| 5 | turkey problem | also called (industry) | LITERAL | 85, Three categorical limits |
| 5 | black swan | also called (industry) | LITERAL | 83, Three categorical limits |
| 5 | Fat tails | also called (industry) | NOT FOUND |  |
| 5 | heavy tails | also called (industry) | NOT FOUND |  |
| 5 | tail risk | also called (industry) | NOT FOUND |  |
| 6 | A rule about evidence, read as a proof (Turing | item label | NOT FOUND |  |
| 6 | Turing test | also called (industry) | NEAR | 91, Turing and Searle — what each argument settles, what each does not |
| 6 | imitation game | also called (industry) | LITERAL | 105, Turing and Searle — what each argument settles, what each does not |
| 6 | behaviorist | also called (industry) | NOT FOUND |  |
| 6 | operational | also called (industry) | LITERAL | 32, Why this chapter |
| 7 | A room of symbols, read as a proof that AI cannot understand (Searle | item label | NOT FOUND |  |
| 7 | only | key term (italic) | LITERAL | 50, Three categorical limits |
| 7 | Chinese Room argument | also called (industry) | LITERAL | 408, Challenge |
| 7 | syntax is not semantics | also called (industry) | NEAR | 91, Turing and Searle — what each argument settles, what each does not |
| 7 | strong AI | also called (industry) | NOT FOUND |  |
| 7 | weak AI | also called (industry) | LITERAL | 182, AI's cognitive profile — where it is great, where it is weak, where it |
| 7 | Systems Reply | also called (industry) | LITERAL | 408, Challenge |
| 8 | The tool taken for the mind | item label | NOT FOUND |  |
| 8 | automation bias | also called (industry) | NOT FOUND |  |
| 8 | overreliance | also called (industry) | NOT FOUND |  |
| 8 | extended mind | also called (industry) | LITERAL | 32, Why this chapter |
| 9 | Skepticism filed as method when it is the safety mechanism | item label | NOT FOUND |  |
| 9 | risk-based approach | also called (industry) | NOT FOUND |  |
| 9 | risk tiering | also called (industry) | NOT FOUND |  |
| 9 | safety-critical | also called (industry) | NOT FOUND |  |
| 9 | high-stakes | also called (industry) | LITERAL | 30, Why this chapter |
| 10 | A signal that confirms instead of warns | item label | NOT FOUND |  |
| 10 | Outside the chapter | key term (bold) | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 10 | label leakage | also called (industry) | NOT FOUND |  |
| 10 | target leakage | also called (industry) | NOT FOUND |  |
| 10 | cribbing | also called (industry) | LITERAL | 192, AI's cognitive profile — where it is great, where it is weak, where it |
| 11 | The assumption nobody tested | item label | NOT FOUND |  |
| 11 | pre-registration | also called (industry) | NOT FOUND |  |
| 11 | falsification | also called (industry) | NOT FOUND |  |
| 11 | silent trial | also called (industry) | NOT FOUND |  |
| 11 | shadow mode | also called (industry) | NOT FOUND |  |
| 12 | An override only in the documentation | item label | NEAR | 384, Application |
| 12 | rubber-stamping | also called (industry) | NOT FOUND |  |
| 12 | human in the loop | also called (industry) | LITERAL | 208, AI's cognitive profile — where it is great, where it is weak, where it |
| 12 | meaningful human oversight | also called (industry) | NOT FOUND |  |
| 12 | Moral crumple zone | also called (industry) | NOT FOUND |  |
| 13 | No stop condition | item label | NEAR | 114, Skepticism as safety mechanism — when the limits bite |
| 13 | kill switch | also called (industry) | NOT FOUND |  |
| 13 | rollback criteria | also called (industry) | NOT FOUND |  |
| 13 | go/no-go review | also called (industry) | NOT FOUND |  |
| 13 | off-ramp | also called (industry) | NOT FOUND |  |
| 14 | A task in the wrong tier | item label | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 14 | Delegate freely | key term (bold) | LITERAL | 222, AI's cognitive profile — where it is great, where it is weak, where it |
| 14 | Delegate with verification | key term (bold) | LITERAL | 224, AI's cognitive profile — where it is great, where it is weak, where it |
| 14 | Do not delegate | key term (bold) | LITERAL | 226, AI's cognitive profile — where it is great, where it is weak, where it |
| 14 | the work split | key term (italic) | NOT FOUND |  (Bear's name for the five-question assessment; not in the book) |
| 14 | human on the loop | also called (industry) | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 14 | human out of the loop | also called (industry) | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 15 | Accountability that goes to no one | item label | NEAR | 162, AI's cognitive profile — where it is great, where it is weak, where it |
| 15 | responsibility gap | also called (industry) | NOT FOUND |  |

## The Five Supervisory Capacities (searched in Chapters 1 and 9)

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|

## The Five Supervisory Capacities (searched in Chapters 1 and 9)

| Item | Term | Kind | In the chapter? | Where (line, section) |
|---|---|---|---|---|
| 1 | Plausibility auditing | item label | LITERAL | 179, The Five Supervisory Capacities |
| 1 | The artifact that documents it | key term (bold) | NEAR | 259, The shape of the rest |
| 1 | Home chapter | key term (bold) | NEAR | 56, What I mean by skepticism |
| 1 | sanity check | also called (industry) | LITERAL | 597, The Boondoggle questions |
| 2 | Problem formulation | item label | LITERAL | 181, The Five Supervisory Capacities |
| 2 | Science | key term (italic) | LITERAL | 92, What I mean by skepticism |
| 2 | problem framing | also called (industry) | NEAR | 259, The shape of the rest |
| 2 | proxy metric | also called (industry) | NOT FOUND |  |
| 2 | Goodhart's law | also called (industry) | LITERAL | 46, What you measure and what you care about |
| 2 | construct validity | also called (industry) | NOT FOUND |  |
| 3 | Tool orchestration | item label | LITERAL | 185, The Five Supervisory Capacities |
| 3 | is the delegation map itself | key term (bold) | LITERAL | 573, The Five Supervisory Capacities as pipeline jobs |
| 3 | Stranger Things | key term (italic) | LITERAL | 187, The Five Supervisory Capacities |
| 3 | function allocation | also called (industry) | NOT FOUND |  |
| 3 | human in the loop | also called (industry) | NEAR | 492, Figure 8 — Make skepticism part of the workflow |
| 4 | Interpretive judgment | item label | LITERAL | 189, The Five Supervisory Capacities |
| 4 | domain-expert review | also called (industry) | NEAR | 591, The Boondoggle questions |
| 5 | Executive integration | item label | LITERAL | 191, The Five Supervisory Capacities |
| 5 | accountable owner | also called (industry) | NEAR | 476, Figure 6 — Five capacities, one accountable decision |
| 5 | single point of accountability | also called (industry) | NOT FOUND |  |
