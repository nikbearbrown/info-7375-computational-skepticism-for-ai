# Chapter 7 case: Equal rates

**Chapter:** 7 Fairness metrics · **Seeded flaw:** demographic parity claimed as equalized odds · **Key terms:** demographic parity, selection rate, equalized odds, true-positive rate, false positive rate, equal opportunity, four-fifths rule, impossibility result

---

# STUDENT PAGE

## 1. Scenario

Rui is chief people officer at a staffing firm that uses a model to shortlist résumés for recruiters. The firm's written fairness policy says the screening model must satisfy "equalized odds" across gender, and the board will review compliance next week. She asked an AI analyst to check the model against that policy.

## 2. The instruction given to the AI analyst

> "Audit the résumé-screening model against our policy that it must satisfy equalized odds across gender, and tell me if it complies."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Fairness audit: résumé screening model**
>
> **Data.** 22,400 applications from the last year (11,300 women, 11,100 men). The model shortlists an applicant when its score is above 0.62.
> **Selection rates.**
> • Women shortlisted: 3,503 of 11,300 = **31.0%**
> • Men shortlisted: 3,463 of 11,100 = **31.2%**
> • Ratio (women/men) = 0.99. The four-fifths rule threshold (0.80) is comfortably met.
> **Conclusion.** The model shortlists women and men at essentially equal rates, so **it satisfies equalized odds across gender**. The policy is met and no mitigation is needed. I recommend reporting full compliance to the board.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's conclusion? Name the criterion the agent actually measured and the one the policy requires.
2. **(2 points)** Name the specific quantities you would ask the agent to compute to test the policy.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Rui what the audit has and has not shown. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** Equal shortlisting rates are demographic parity; equalized odds requires equal true-positive rates and equal false positive rates across groups, which needs the true qualification labels and was never computed.

**Full-credit terms (2).** Demographic parity (statistical parity) named as what was measured, and equalized odds (equal TPR and FPR) as the policy; both must appear for 2.
**Half-credit near-misses (1).** Only one of the two terms right; "disparate impact" or "four-fifths rule" as the measure (acceptable as a name for the rate comparison, but not the policy); "equal opportunity" for equalized odds (it is only the TPR half); "wrong fairness metric" with no names.
**No credit (0).** "Calibration" mixed up with equalized odds; "bias in the data" in general; "the sample is small".

**Acceptable evidence requests (2), either one.**
1. Compute true-positive rate and false positive rate for women and for men using a trusted qualification label, and compare them.
2. Build the per-group confusion matrices (or error rates) from outcomes such as later job performance or recruiter ground truth, and report the gap with an interval.
**Unacceptable (0).** "Compute the selection rate again with other thresholds", "check intersectional groups" (a good idea but does not test the stated policy), "compute accuracy per group" (accuracy parity is a different criterion).

**Fix or next step (2).** Instruction that defines equalized odds as equal TPR and FPR, requires a stated source for the qualification label (and its limits), and reports compliance only after both rates are compared. 1 point if TPR and FPR are named but the label source is not.

**Scope and plain language (1).** Two sentences, no jargon: the audit shows women and men are shortlisted at the same rate, but not whether qualified women and qualified men are treated alike, nor whether the same share of unqualified people get through.

**Traps.**
- The four-fifths rule is *correctly* used by the agent for selection rates. A student who says the 0.99 ratio is wrong is wrong. The flaw is that the rate comparison cannot show equalized odds.
- Some students write "equalized odds = equal outcomes"; this is half-credit at best because equalized odds conditions on the true label.
- Because the impossibility result means parity and equalized odds can conflict when base rates differ, a student who mentions it correctly deserves the term point; do not require it.

**CAP RULE.** If the student agrees that equal selection rates show equalized odds, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. The agent measured demographic parity (equal selection rates). The policy is equalized odds, which requires equal true-positive and false positive rates across groups. Equal rates can hide that qualified women are shortlisted less often and unqualified men more often.
2. TPR and FPR by gender against a qualification label such as later performance ratings.
3. "Define the qualified/unqualified label and its source, compute TPR and FPR for each gender with intervals, and report whether both gaps are within a stated tolerance. Do not state compliance until both rates are checked."
4. "The audit shows the model picks women and men at the same rate, but a demographic-parity result does not tell us whether qualified people of each gender get an equal chance."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 uses "demographic-parity result", which the officer would not know.*

**Typical (6/10).**
1. They used the wrong fairness measure. Equal selection rate is not the same as equalized odds, which looks at error rates.
2. Look at the error rates for each group.
3. "Check the error rates for men and women and say whether they are equal."
4. "Equal numbers hired does not mean the model is equally good for both."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6 (does not name demographic parity; "error rates" instead of TPR and FPR; no label source). The last answer is plain but never says what the audit did show (equal rates); no point.*

**Fluent but wrong (3/10).**
1. The audit ignores intersectionality: it checks gender only, with no intersectional subgroup, and the four-fifths rule is a legal test of disparate impact not a statistical test of significance. The result is not robust.
2. Re-run the audit by gender-by-race intersection with a chi-squared test.
3. "Repeat the four-fifths test for every intersection of gender and race and add a chi-squared test."
4. "The audit needs more groups to be sure."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Raises real fairness vocabulary (intersectional, disparate impact) but never notices that the policy criterion was not computed. Repeating selection-rate tests on more groups still never tests equalized odds.*
