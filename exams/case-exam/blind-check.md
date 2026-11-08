# Blind check of the rubric (2026-11-08)

**Method.** Three sub-agents saw only the student pages of 5 cases each (15 answers over all 14 cases; ch06 twice). Each wrote answers in an assigned persona (strong 6, typical 4, fluent-but-wrong 5). A fourth sub-agent, who did not know the personas, scored all 15 with the case keys and README as a TA would. Intended level vs TA score:

| Persona | Cases (TA total) |
|---|---|
| Strong (target ~9) | ch00 10, ch04 10, ch06 10, ch11 10, ch13 9, ch09 8 |
| Typical (target ~6) | ch02 9, ch03 9, ch07 9, ch12 10 |
| Fluent-but-wrong (target ~3) | ch01 0, ch06 0, ch05 2, ch08 2, ch10 2 |

**Result.** The rubric separates good from weak clearly: no fluent-but-wrong answer scored above 2, and no strong answer below 8. Every wrong-problem answer missed the flaw and stayed under the cap. It did **not** separate strong from typical: the "typical" persona answers (written by a model) all named the flaw, the exact term and a usable check, so they scored 9 to 10. That is a limit of the test (model-written "typical" answers are too good), not proof the rubric is blind to vagueness; the hand-written typical samples on each page do score 6 under the key. Real student papers are needed to check the middle.

**What the blind scorer flagged, and what was changed.**
1. Wrong-problem answers: line definitions said 0, samples gave partial credit. Fixed in README: an off-target but sound request earns 1, never 2; Scope needs a plain, true Q4 that does not endorse the agent.
2. ch03 ablation of one feature: key said full evidence credit, sample gave 1. Fixed: ablation alone = 1; timestamp audit or temporal split = 2.
3. Naming the flaw then dismissing it (ch10): no rule. Added to README (Catches 1, cap applies); cap now triggers at Catches 0 or 1.
4. ch08 "hallucination": clarified Term 1 at most, Catches 1 only if the student still says the claim exceeds the check.
5. ch13 "structural blind spot" vs distribution shift headline: now full term if the student says more data cannot close the gap.
6. ch11 "was associated with": now acceptable as an observe-level verb.
7. Strong anchor of 9 is arguably low: a jargon-free probe 4 gives 10. README now says a 10 is possible.

**Not changed (judgement calls left to TAs, noted):** ch09 fix with human checkpoints but no acceptance criteria (1); ch12 fix that names a person and sanctions but no halt authority (lenient 2 accepted); ch01 "open-access sample is not representative" gets no credit (valid but secondary); ch07 "ground truth labels" with no source (evidence 2, fix 1).

**Still to do before use:** calibrate with real student answers (a pilot of 10 papers on 2 cases), because the middle band is untested. The cap rule never changed a score in this run; it is a safeguard for answers that earn partial Evidence and Fix credit while missing the flaw.
