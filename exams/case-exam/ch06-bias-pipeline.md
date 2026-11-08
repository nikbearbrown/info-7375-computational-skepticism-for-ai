# Chapter 6 case: Forty-eight thousand rows

**Chapter:** 6 Bias in the pipeline (observational data and controls) · **Seeded flaw:** a confounder "handled" by adding more rows · **Key terms:** confounder / confounding, self-selection, selection bias, exchangeability, randomization, matching / standardisation, sensitivity analysis, bias vs variance

---

# STUDENT PAGE

## 1. Scenario

Ms. Alvarez is the curriculum director for a school district. Last year, families could opt in to an AI math-tutoring app; some used it heavily and most did not. The school board will vote on funding the app for all 30 schools. She asked an AI analyst to estimate what the app does for end-of-year math scores.

## 2. The instruction given to the AI analyst

> "Estimate the effect of the tutoring app on end-of-year math scores and tell me whether the district should fund it for every school."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Effect of the tutoring app on math scores**
>
> **Data.** 48,200 students in grades 4-8. 9,100 used the app for 20 or more hours (users); 39,100 did not (non-users). Outcome: end-of-year math score (state test scale).
> **Raw comparison.** Mean score, users 71.9; non-users 60.5. Difference **+11.4 points** (standard error 0.4; 95% interval 10.6 to 12.2).
> **Possible confound.** Families opted in themselves, so motivated or better-resourced families may be over-represented among users and could raise scores independently of the app.
> **Handling.** The sample is very large (n = 48,200), so differences in motivation average out across the two groups and the estimate is unbiased. No further adjustment was applied.
> **Conclusion.** The app raises math scores by about 11 points (95% interval 10.6 to 12.2). I recommend district-wide funding.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's handling of the concern it raised itself? Name the problem with the exact term for it.
2. **(2 points)** Name one study design or analysis that would give better evidence about what the app does.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Ms. Alvarez whether the 11-point figure can be used to justify the funding. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** Families chose the app themselves (self-selection), so family motivation is a confounder; a bigger sample shrinks the random error (variance) but does nothing to the systematic error (bias), so the narrow interval around +11.4 is confidently measuring the wrong thing.

**Full-credit terms (2).** Confounder / confounding; self-selection or selection bias (when the student explains that users differ from non-users before the app); "more data reduces variance, not bias"; non-exchangeable groups.
**Half-credit near-misses (1).** "Correlation not causation" with no mechanism; "sampling bias"; "bias" alone; "lurking variable" or "hidden variable" (informal synonyms: full credit only if the student says it differs between the groups and affects the outcome; otherwise 1).
**No credit (0).** Overfitting; "need a significance test" (the interval is already narrow); "outliers".

**Acceptable evidence requests (2), either one.**
1. A randomised pilot: assign the app to some schools or classes by lottery and compare.
2. An adjusted comparison: control for prior-year scores (and other pre-app traits) with matching or standardisation, and add a sensitivity analysis for hidden confounders.
**Unacceptable (0).** "Get even more students", "run a t-test", "report a bootstrap interval" (all measure noise, not confounding).

**Fix or next step (2).** Instruction that drops "average out" language, includes pre-app scores and family traits as controls (matching or standardisation), asks for sensitivity analysis, and recommends a randomised pilot before district-wide funding. 1 point for only one of these.

**Scope and plain language (1).** Two sentences, no jargon: families who chose the app may already have been stronger students, so the 11 points mix the app's effect with who signed up; fund a small fair trial first.

**Traps.**
- The agent *itself* names the confounder, then dismisses it. Students who only repeat "motivation might confound" without saying why the handling fails get Catches 2 at most.
- "The sample is large, so the estimate is precise" is true; precision is not validity. Reward the students who separate the two.
- Do not give Catches to a student who attacks the 95% interval's calculation.

**CAP RULE.** If the student accepts that a large n handles the confounder, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. Self-selection creates confounding: motivated families chose the app and also have higher scores for other reasons. More rows reduce variance but not bias, so the narrow interval is precise and still wrong. The groups are not exchangeable.
2. A randomised pilot, or at least a comparison adjusted for prior-year scores with a sensitivity analysis.
3. "Compare users and non-users matched on prior-year score, grade, school and free-lunch status; report a sensitivity analysis for an unmeasured confounder; state that this is observational; and recommend a randomised pilot in several schools before any district-wide decision."
4. "The 11 points is confounded by self-selection, so it cannot justify funding until there is a randomised pilot."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 is in jargon (confounded, self-selection, randomised pilot), so the plain-language point is lost.*

**Typical (6/10).**
1. The agent says there's a lot of data so no problem, but there is still confounding because the families choose the app. Large data doesn't fix that.
2. Do an experiment.
3. "Control for motivation and re-run."
4. "The 11 points might just be because better students used the app."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (confounding named loosely without self-selection or variance/bias; "do an experiment" without randomisation or sampling; "control for motivation" is not measurable as stated). Q4 is correct but does not say the 11 points mixes the app with who signed up; no point.*

**Fluent but wrong (3/10).**
1. The agent should report an effect size and a power calculation. With 9,100 vs 39,100 the groups are unbalanced, and heteroskedasticity could make the standard error unreliable; use a Welch test with a bootstrap interval.
2. A Welch t-test and a bootstrap 95% interval.
3. "Re-run with a Welch t-test and a percentile bootstrap, and report Cohen's d."
4. "The statistical test used may not be right for different group sizes."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Correct statistics vocabulary pointed at noise. The interval is already narrow; none of the proposed analyses addresses who signed up. Cap rule applies.*
