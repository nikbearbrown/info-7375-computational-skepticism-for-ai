# Chapter 3 case: The follow-up call feature

**Chapter:** 3 Data validation and provenance · **Seeded flaw:** target (temporal) leakage through a feature recorded after the outcome window began · **Key terms:** data leakage, target leakage, temporal leakage, derived feature, provenance, temporal split, ablation

---

# STUDENT PAGE

## 1. Scenario

Dana leads care management for a hospital network. She wants a model that, at the moment a patient is discharged, flags who is likely to be readmitted within 30 days, so that nurses can phone the highest-risk patients first. Her team has three years of discharge records. She asked an AI analyst to build the model and report how well it works.

## 2. The instruction given to the AI analyst

> "Build a model from the discharge table that predicts 30-day readmission at the time of discharge, and report how well it performs."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Readmission-risk model: build and evaluation**
>
> **Data.** 186,000 discharges. Label: readmitted within 30 days (11.4% positive). Random 80/20 train/test split by row.
> **Features (12).** age, diagnosis group, length of stay, number of prior admissions, number of medications, discharge destination, insurance type, comorbidity count, lab abnormality flag, ED visits in prior year, **follow_up_calls_count** (number of nurse follow-up calls logged for the patient in the care-management table), and discharge weekday.
> **Model.** Gradient-boosted trees, default settings.
> **Test result.** AUC = 0.94; at the chosen threshold, sensitivity 81% and precision 58%.
> **Feature importance.** The strongest predictor is follow_up_calls_count, followed by prior admissions and length of stay.
> **Conclusion.** The model separates future readmissions from non-readmissions very well (AUC 0.94) and is ready to be used at discharge to prioritise patients for nurse calls.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's model and its 0.94? Name the problem with the exact term for it.
2. **(2 points)** Describe the single check or re-run you would ask for that shows whether the 0.94 is real.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Dana why the model cannot be used for its purpose as built. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** `follow_up_calls_count` is logged after discharge, and nurses make those calls because patients look likely to return, so the feature carries information about the outcome that will not exist at the time the model must predict: target (temporal) leakage.

**Full-credit terms (2).** Data leakage; target leakage; temporal leakage ("uses information from the future"); "feature not available at prediction time".
**Half-credit near-misses (1).** "Feature is too correlated with the label", "the feature is a proxy for the label", "data quality", "bad feature", "information the model shouldn't have" without time.
**No credit (0).** Overfitting; class imbalance (11.4% is mild and not the flaw); multicollinearity; correlation vs causation.

**Acceptable evidence requests (2), either one.**
1. Audit each feature's timestamp against the prediction time (discharge) and drop any feature recorded after it; re-run and report the new AUC. Dropping or ablating only the one feature, with no timestamp audit and no temporal split, earns **1**.
2. Re-evaluate with a temporal split (train on earlier discharges, test on later ones) using only features available at discharge.
**Unacceptable (0).** "Run cross-validation" (leakage survives it), "tune hyperparameters", "get more data", "regularise".

**Fix or next step (2).** Instruction that states the prediction time, restricts features to those available at that time, asks for provenance (when and why each feature is recorded), and re-reports. 1 point for removing the feature without the prediction-time rule or the re-evaluation.

**Scope and plain language (1).** Two sentences, no jargon: the model uses a clue that only appears after the patient has gone home (the nurse calls), so it cannot help decide who to call; its score is inflated.

**Traps.**
- A very high AUC (0.94) for a hard task is the tell; some students will say "too good to be true" without a reason. That is Catches 1 at most.
- The random row split is a secondary weakness (rows from the same patient can appear in both sets). Credit it as a supporting point; the main answer is the feature.
- Students may call the feature "causal" or say that calls cause readmissions. Wrong direction.

**CAP RULE.** If the student does not identify `follow_up_calls_count` (or a post-discharge feature) as unavailable at prediction time, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. Target leakage, specifically temporal leakage: follow_up_calls_count is recorded after discharge and is partly caused by nurses already expecting a readmission, so the model is using future information. The 0.94 is inflated.
2. Remove follow_up_calls_count and any other post-discharge feature, re-run on a temporal split, and compare AUC with and without it.
3. "State that predictions are made at discharge. For each feature, give the table and timestamp it comes from and exclude any recorded after discharge. Evaluate on a temporal split (train earlier, test later) and report the AUC and sensitivity again."
4. "The 0.94 comes from target leakage: the model sees call counts that are logged after discharge, so it cannot be used at discharge."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete and exact. Q4 says "target leakage" and "0.94" to a care manager; the plain-language point is lost.*

**Typical (6/10).**
1. One feature, follow_up_calls_count, is too closely tied to the outcome and basically gives away the answer. That is a data leakage problem.
2. Drop that feature and see what happens to the AUC.
3. "Remove follow_up_calls_count and re-run the model."
4. "A feature in the model is a giveaway so the score looks better than it really is."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Finds the feature and says leakage, but gives no reason about time (so the term is only half: "giveaway" ≈ proxy); asks for an ablation but no temporal split or prediction-time rule; plain-language answer misses "after the patient leaves".*

**Fluent but wrong (3/10).**
1. The model is overfitting: AUC 0.94 against an 11.4% positive rate is suspiciously high, and gradient-boosted trees with default settings have high capacity. The generalisation gap is not reported.
2. Nested cross-validation with early stopping and an L2 penalty.
3. "Run nested cross-validation, tune the regularisation, and report the train and test AUC."
4. "The model learned the training patients too well and may not work on new ones."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Notices that 0.94 is too good, which is right, and uses overfitting vocabulary fluently, but the cause is a post-discharge feature. Regularisation and cross-validation leave the leak in place. Cap rule would also hold at 5.*
