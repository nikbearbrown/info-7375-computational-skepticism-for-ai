# Chapter 2 case: The one segment that worked

**Chapter:** 2 Probability, uncertainty and confidence · **Seeded flaw:** a "significant" result found by testing many segments with no correction (multiple comparisons) · **Key terms:** multiple comparisons problem, family-wise error rate, false discovery rate, Bonferroni / Holm / Benjamini-Hochberg, p-hacking, exploratory vs confirmatory, preregistration

---

# STUDENT PAGE

## 1. Scenario

Jun is the product lead at a language-learning app. His team tested a new onboarding flow in an A/B test and he must decide whether to roll it out to everyone, to one group of users, or not at all. He asked an AI analyst to find out whether the new flow helps and which users benefit. The company has about 60,000 users in the test.

## 2. The instruction given to the AI analyst

> "Test whether the new onboarding flow improves 30-day retention, and find which user segments benefit from it."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **A/B test analysis: new onboarding flow**
>
> **Overall result.** 30-day retention was 41.8% (control) and 42.2% (new flow). Difference +0.4 points, two-sided p = 0.41. Not significant.
> **Segment analysis.** To find who benefits, I split users into 24 segments (device, country group, age band, referral source, plan type, and combinations of these) and ran a two-sided test of retention difference in each, at the standard 0.05 level.
> **Finding.** One segment shows a significant lift: *Android users aged 55 and over referred by podcasts* (n = 1,140). Retention rose from 38.2% to 44.3% (**+6.1 points, p = 0.03**).
> **Interpretation.** The new flow is effective for older podcast-referred Android users, likely because the larger buttons suit them. The other 23 segments showed no significant difference and are not discussed further.
> **Recommendation.** Roll the new flow out to this segment and build a podcast marketing campaign around it.

## 4. Questions (10 points)

1. **(5 points)** What is the statistical problem with the agent's finding? Name it with the exact term.
2. **(2 points)** Name two specific things you would ask the agent to do (a calculation or a new test) to find out whether the segment result is real.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, explain to Jun why he should not build a campaign yet. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** The agent ran 24 tests at 0.05 and reported the one that crossed the line, which is expected by chance (about 1.2 false positives from 24 tests; roughly a 70% chance of at least one), so p = 0.03 is not evidence of a real effect.

**Full-credit terms (2).** Multiple comparisons problem (multiple testing); family-wise error rate or false discovery rate (naming either with the problem); p-hacking / data dredging / forking paths; "exploratory finding presented as confirmatory".
**Half-credit near-misses (1).** "Type I error" or "false positive" without the many-tests reasoning; "cherry-picking"; "significance level was too lax"; "spurious result".
**No credit (0).** "Small sample size" as the main point; "p-value is wrong"; overfitting; "effect size is small" (6.1 points is not small).

**Acceptable evidence requests (2), either one.**
1. Report adjusted p-values for all 24 tests (Bonferroni or Holm for family-wise error; Benjamini-Hochberg for false discovery rate) and say whether the segment survives.
2. Treat the segment as a hypothesis and run a fresh, preregistered confirmatory test on new users in that segment (or a held-out part of the data).
**Unacceptable (0).** "Lower the cutoff to 0.01 for that segment" (chosen after seeing the result); "collect more data on everyone" with no confirmatory design; "report the confidence interval of the segment" alone (it is still selected after the search).

**Fix or next step (2).** Instruction that names the number of tests, applies a correction, labels the result exploratory, and proposes a confirmatory test. 1 point for any one of correction or confirmatory test without the other.

**Scope and plain language (1).** Two sentences, no jargon: if you slice the users 24 ways one slice will look good by luck alone, so wait for a repeat test before spending money.

**Traps.**
- The first line (overall result not significant) is correct and not the flaw. A student who says "the overall result should have been significant" is wrong.
- "Larger buttons suit older users" is a story told after the result. Students may note this as HARKing; accept as a supporting point for the term (1) but not as a replacement for multiple comparisons.
- Check that a student who suggests Bonferroni does so over all 24 tests, not just "the segment".

**CAP RULE.** If the student does not recognise that testing many segments makes one false hit likely, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. This is the multiple comparisons problem. With 24 segment tests at 0.05, about one false positive is expected by chance (roughly a 70% chance of at least one), so a single p = 0.03 is not trustworthy. It is also p-hacking in effect, because the segment was picked after looking.
2. Holm or Benjamini-Hochberg adjusted p-values across all 24 tests; and a preregistered retest on new Android 55+ podcast users.
3. "Report all 24 segment results, apply a Holm correction across them, label any survivor as exploratory, and propose a confirmatory test with the segment, outcome and sample size fixed in advance. Do not recommend a rollout from an uncorrected segment."
4. "The segment result is exploratory and uncorrected for 24 comparisons, so it should be confirmed with a preregistered test before any campaign."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Everything is right and complete; Q4 is written in jargon (exploratory, uncorrected, preregistered) so the plain-language point is lost.*

**Typical (6/10).**
1. They did too many tests and got a false positive. This is a Type I error.
2. Use a stricter cutoff and test it again.
3. "Redo the analysis with a stricter significance level and retest the segment."
4. "The result may be a coincidence because so many groups were checked."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Understands the cause but gives only "Type I error"; "stricter cutoff" has no named correction or number of tests; "retest" is not specified as preregistered. Stakeholder line is almost right (a TA could give the point; keep the 6 as the calibration answer).*

**Fluent but wrong (3/10).**
1. The sample for the segment is only 1,140, so the estimate has high variance and low statistical power. The finding is unreliable because of the small sample.
2. A power analysis and a confidence interval for the segment.
3. "Compute the power and a 95% confidence interval for the segment and double the sample."
4. "The group is too small to be sure about."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses power and confidence-interval vocabulary correctly but blames sample size; n = 1,140 is ample for a 6-point difference. Never notices the 24 tests. An interval on a selected segment inherits the same bias.*
