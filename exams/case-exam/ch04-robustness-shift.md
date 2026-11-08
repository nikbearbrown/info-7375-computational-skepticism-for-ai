# Chapter 4 case: Worse since the suburbs

**Chapter:** 4 Robustness and distribution shift · **Seeded flaw:** covariate shift diagnosed as concept drift · **Key terms:** covariate shift, concept drift (concept shift), data drift, distribution shift, slice-based evaluation, importance weighting, support overlap, population stability index (PSI)

---

# STUDENT PAGE

## 1. Scenario

Priya is operations director at a delivery company. Its model predicts how many minutes each delivery will take, and the app shows that estimate to customers. Since the company began serving suburban neighbourhoods in January, customers complain that estimates are badly wrong. Priya wants to know why, and what to do, before the next quarter.

## 2. The instruction given to the AI analyst

> "Diagnose why our delivery-time predictions have got worse since January and recommend a fix."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Diagnosis: delivery-time model degradation**
>
> **Symptom.** Mean absolute error rose from 6.1 minutes (previous six months) to 11.8 minutes (since January).
> **What I checked.**
> • Share of orders from the new suburban zones rose from 8% to 41%.
> • Suburban orders have longer distances (median 9.4 km vs 3.1 km) and fewer stops per route.
> • Error in the original urban zones is **unchanged at 6.2 minutes**.
> • Error in the suburban zones is 19.7 minutes. The model was trained almost entirely on urban orders (suburban rows were under 3% of training data).
> **Diagnosis.** The relationship between delivery conditions and delivery time has changed since January. **This is concept drift.**
> **Recommendation.** Relabel the last 90 days of orders to reflect the new delivery behaviour and retrain the entire model from scratch every week. Alert when overall MAE exceeds 9 minutes.

## 4. Questions (10 points)

1. **(5 points)** The agent names the cause "concept drift". Using the agent's own numbers, say what is wrong with that diagnosis and give the exact term for what actually happened.
2. **(2 points)** Name one check or analysis that would tell the two causes apart.
3. **(2 points)** Write the corrected instruction (diagnosis and fix) you would send to the agent.
4. **(1 point)** In two sentences, explain to Priya what went wrong with the estimates. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** The input mix changed (many more long-distance suburban orders) while the model's accuracy on the old kind of order did not (urban error is unchanged at 6.2), which is covariate shift (the inputs moved), not concept drift (the rule linking inputs to outcome changed).

**Full-credit terms (2).** Covariate shift; "input distribution shifted while P(y|x) is unchanged"; "population/subpopulation mix changed with limited support overlap" (accept if the student also says concept drift is the wrong label).
**Half-credit near-misses (1).** Data drift; distribution shift (true but unspecific); label shift (wrong type); "out-of-distribution"; "sampling bias in the training data"; "population mismatch".
**No credit (0).** Overfitting; data leakage; "the model is just bad"; accepting concept drift.

**Acceptable evidence requests (2), either one.**
1. Slice-based evaluation: report error separately by zone (urban vs suburban) and by distance band, and compare with the training distribution (PSI or a domain classifier on the inputs).
2. Test whether the input-to-outcome relationship is stable: compare the error of urban orders over time, or compare suburban orders against similar urban orders matched on distance and stops.
**Unacceptable (0).** "Retrain on all the new data and see if it improves" (no diagnosis); "check overall MAE weekly"; "run cross-validation".

**Fix or next step (2).** Collect and label suburban deliveries (the model has almost none), evaluate by slice, apply importance weighting or reweighting toward the new mix, and monitor input drift. Full marks need at least one of the data-collection / reweighting ideas and a per-slice metric. 1 point for "retrain with more suburban data" alone.

**Scope and plain language (1).** Two sentences, no jargon: the model learned from short city trips and is now being asked about long suburban trips it has hardly seen; for the city trips it is still fine.

**Traps.**
- The agent's own bullets contain the refutation (urban error unchanged). Students who ignore it and accept "concept drift" get Catches 0.
- Weekly retraining from scratch and relabelling are treatments for concept drift; a student who points this out has understood. Do not penalise a student who also notes that relabelling labels that are not wrong wastes effort.
- Near-misses: "label shift" (the outcome rate changed) is a different shift; give 1 only if the student's description matches the case (inputs moved).

**CAP RULE.** If the student accepts concept drift or cannot say that the inputs shifted while the rule stayed the same, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. Concept drift means the outcome for the same inputs changed. But urban error is unchanged at 6.2, so P(outcome | inputs) held; what changed is the mix of inputs, with far more suburban orders. That is covariate shift, with little support overlap since the training data had under 3% suburban rows.
2. Slice-based evaluation by zone and distance band, plus a PSI on distance and stops between the training and current periods.
3. "Report error by zone and distance band, compute PSI for each input against the training period, collect labelled suburban deliveries, and test importance weighting toward the current mix. Do not relabel old data unless a stable-input check shows the outcome rule changed."
4. "Covariate shift: the suburban orders are outside the model's training distribution, so it needs retraining on them."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete and exact. Q4 is written in jargon, so the plain-language point is lost.*

**Typical (6/10).**
1. The agent is wrong: it's not concept drift because the urban error didn't change. It is data drift, the data changed when suburbs were added.
2. Look at the error for suburban and urban separately.
3. "Check the error by zone and add more suburban data to the training."
4. "We added suburbs and the model hasn't seen enough of them."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Uses the agent's number to refute the label (catch). "Data drift" is the half-credit near-miss. Slice check is named but not with a compare-to-training measure; fix has data but not weighting or monitoring. Q4 is plain, but it blames the added suburbs without saying the model has seen few of them; no point.*

**Fluent but wrong (3/10).**
1. The agent is right that the model is stale, but the real issue is label shift: the share of long deliveries (a higher base rate of late orders) went up, so the class prior moved. The cause is prior probability shift.
2. A Kolmogorov-Smirnov test on the label distribution.
3. "Recompute the label priors and rescale the predicted probabilities by the new priors, then retrain."
4. "The mix of outcomes has changed so the model's guesses are off."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses correct shift vocabulary but picks label shift; the case is about the inputs moving, and prior-rescaling would not fix suburban errors. The KS test is a legitimate tool but on the wrong variable.*
