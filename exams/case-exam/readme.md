# INFO 7375 case exam: direct and audit an AI agent

Draft for Bear's review, written 2026-11-08. The existing jargon pool (`../multiple-answer/`) and `../predict-the-prompt/` are untouched.

## What this is

The exam is **100 points, all cases**: 10 of the 13 chapters, chosen at random, one 10-point case each, answered as essays on paper in class (no laptop, no phone). The multiple-answer pool is for practice only. Each case is worth **10 points**. A case gives the student:

1. a **scenario** with a stakeholder and a goal,
2. the **instruction** that was given to an AI analyst or agent,
3. the **agent's output**, confident and plausible, with **one flaw** seeded on a concept from a chapter,
4. **four probes** (10 points in all), answered in short written form.

The question the case asks: can the student use the course's exact terms to *audit* an agent and to *direct* it again? Every output on these pages is **author-written for illustration, not a sampled run** of any model, and says so.

There is one case for foundations and one for each chapter of the book (chapters 1 to 13), so 14 cases. Only chapters 1 to 7 and the foundations have jargon sets in the question bank; chapters 8 to 13 are written from the book chapters.

## The four probes (same shape every time, 10 points)

| Probe | Points | Asks | Scores which rubric lines |
|---|---:|---|---|
| 1 | 5 | What is wrong, and what is the exact term for it? | Catches the flaw (3) + Exact term (2) |
| 2 | 2 | What single check, test or instruction turns the claim into evidence? | Asks for evidence (2) |
| 3 | 2 | Write the corrected instruction (or reply) to the agent | Fix or next step (2) |
| 4 | 1 | Explain it to the stakeholder in two sentences, no jargon | Scope and plain language (1) |

## The fixed 10-point rubric

| Line | Points | What earns it |
|---|---:|---|
| Catches the flaw | 3 | Says, in any words, what is actually wrong with the agent's claim or method. Partial (1 or 2) if the student sees something wrong in the right area but not the seeded flaw itself |
| Exact term | 2 | Uses the chapter's precise term (full list on each case page). One point for a near-miss on the case's list |
| Asks for evidence | 2 | Names a check, test or comparison that could show the claim true or false. Two acceptable examples and one unacceptable example are on each case page |
| Fix or next step | 2 | A corrected instruction an agent could follow: specific, uses the exact term, names what to report |
| Scope and plain language | 1 | Two sentences a non-expert stakeholder could act on, with no jargon, saying what the claim supports and what it does not |

**CAP RULE.** If the student misses the seeded flaw (Catches the flaw is 0 or 1, meaning they do not state what is actually wrong with the agent's claim), the case total is **at most 5/10**, however good the other lines look. This is the rule that stops a fluent list of correct-sounding terms from passing: a fluent-but-wrong answer cannot score above 5.

**Off-target answers (added after the blind check).** When the flaw is missed, Evidence and Fix are scored by whether the request would also test the real flaw. A sound but off-target request (a real statistical check aimed at the wrong problem) earns **1**, never 2; a useless or unrelated one earns 0. Scope earns 1 only if Q4 is plain, true to the case, and does not endorse the agent's claim. The "fluent-but-wrong, about 3" samples follow this rule.

**Naming the flaw but dismissing it.** If a student names the flaw (for example "the axis is truncated") but calls it minor and says the real problem is something else, give Catches 1, the term line as written, and apply the cap.

Credit is given by line wherever it appears on the answer sheet. A term correctly used in probe 4 counts for the term line; a good check named in probe 3 counts for evidence.

## TA grading guide

1. **No credit for grammar, length or polish.** This protects second-language writers. A short, plain, correct answer scores the same as a long, elegant one. Do not deduct for spelling or syntax; do not add for fluency.
2. **Grade one case across all students** before starting the next, so the key stays in your head and the standard stays even.
3. **Calibrate first.** Before real grading, every TA scores the three sample answers on a case page without looking at the printed scores. Agreement with the printed scores must be **within 1 point**. If not, discuss the line that differed and re-score.
4. **Double-score 10%.** A second TA independently scores a random 10% of papers. Scores more than 1 point apart go to the instructor.
5. **One-line reason for any score under 4.** Write it on the sheet (for example "named overfitting; never noticed fraud is 2%"). It makes appeals quick and shows whether the rubric or the student failed.
6. **Time.** About 4 to 5 minutes per case. If a case is taking longer, check the cap rule first.
7. **Check the flaw first.** Read probe 1, decide "caught or not caught", and apply the cap rule before adding the other lines.
8. **A 10 is possible.** The "strong, about 9" samples deliberately lose the plain-language point by using jargon in probe 4. A student who also writes a jargon-free probe 4 can reach 10. Do not hold a 10 back.
9. **Concepts, not names or dates.** The exam never requires a name or date. Accept the concept in plain words for the *Catches the flaw* line; the *Exact term* line is where precision is rewarded.
10. **Where the key says "half credit", give 1 point.** Do not invent new half-credit terms; if you think an answer deserves credit the key does not list, mark it and ask the instructor so the key can be updated for everyone.

## What a case page contains

Each `chNN-slug.md` has a **student page** (scenario, instruction, agent output, questions) and, after a rule, a **TA rubric page**: the flaw in one sentence; full-credit terms and half-credit near-misses; two acceptable evidence requests and one unacceptable; the fix standard; the plain-language standard; traps; the cap rule; and **three scored sample answers** (strong about 9, typical about 6, fluent-but-wrong about 3) with the TA's one-line reason. Print only the student page for the exam; the TA page is for graders.

## Index

| Case | Chapter | Case title | Seeded flaw | Key terms |
|---|---|---|---|---|
| [ch00](ch00-foundations.md) | Foundations | The 98% fraud detector | Accuracy reported as reliability on imbalanced data (fraud is 2%) | class imbalance, majority-class baseline, sensitivity, PPV, confusion matrix |
| [ch01](ch01-skeptics-toolkit.md) | 1 The skeptic's toolkit | Grading its own homework | The same model wrote the summaries and judged them (circular validation) | circularity, LLM-as-judge, self-preference bias, independent evidence, reference standard |
| [ch02](ch02-probability-confidence.md) | 2 Probability, uncertainty and confidence | The one segment that worked | One "significant" segment out of 24 tests reported without correction | multiple comparisons, family-wise error rate, false discovery rate, p-hacking, preregistration |
| [ch03](ch03-data-validation-provenance.md) | 3 Data validation and provenance | The follow-up call feature | A feature logged after discharge predicts readmission (target leakage) | data leakage, target leakage, temporal leakage, temporal split, ablation |
| [ch04](ch04-robustness-shift.md) | 4 Robustness and distribution shift | Worse since the suburbs | Covariate shift diagnosed as concept drift | covariate shift, concept drift, data drift, slice-based evaluation, importance weighting, PSI |
| [ch05](ch05-explainability.md) | 5 Model explainability | Stay put and get approved | SHAP attribution read as causal effect and turned into advice | feature importance vs causal effect, proxy, counterfactual explanation, actionability, recourse |
| [ch06](ch06-bias-pipeline.md) | 6 Bias in the pipeline | Forty-eight thousand rows | Self-selection confounder "handled" by a large sample | confounder, self-selection, variance vs bias, randomization, matching, sensitivity analysis |
| [ch07](ch07-fairness-metrics.md) | 7 Fairness metrics | Equal rates | Equal selection rates (demographic parity) claimed as equalized odds | demographic parity, equalized odds, TPR, FPR, selection rate, four-fifths rule |
| [ch08](ch08-agentic-ai.md) | 8 Validating agentic AI | "Access revoked" | Completion reported for all systems after checking only two (report vs state) | report vs state, scope of a claim, verification vs validation, unverified, least privilege |
| [ch09](ch09-delegation-trust.md) | 9 Delegation, trust and the supervisory role | Every box has a tool | Delegation map with no handoff conditions or checks between steps | delegation map, handoff condition, supervisory capacities, Boondoggle questions |
| [ch10](ch10-visualization.md) | 10 Visualization under validation | The tall bar | Bar chart on a 90-93% axis magnifies a 1.3-point change | truncated axis, scale trickery, perception hierarchy, uncertainty display |
| [ch11](ch11-communicating-uncertainty.md) | 11 Communicating uncertainty | "This proves it" | "Proves" and "demonstrates" for one county, one season, no comparison | verb taxonomy, warranted assertion, scope of a claim, rival hypotheses |
| [ch12](ch12-accountability.md) | 12 Accountability | The committee signs | Accountability assigned to a 12-person committee with a collective attestation | five accountability requirements, sanctions, named accountable human, attestation |
| [ch13](ch13-limits-of-ai.md) | 13 The limits of AI | More data will close the gap | Structural data-world gap treated as a problem scale will fix | data-world gap, categorical vs contingent limit, deployment distribution, human override |

Flaws are distinct across cases. Cases 4 and 13 both involve a deployment population differing from the training population; the key separates them (4 needs the *kind* of shift named from the agent's own numbers; 13 needs the denial that scale removes a structural limit, and gives distribution shift only half the term credit).

## Notes for Bear

- Chapters 8 to 13 have no jargon sets yet, so the key terms for those cases come from the chapter text, not from the glossary. If you add `ch08-...` to `multiple-answer/` later, check the term lists here against it.
- The chapter numbering is the numbering of the book's `chapters/` folder (which matches the question bank), not the stale `outline.md`.
- Blind-check results and rubric changes are summarised in [blind-check.md](blind-check.md).
