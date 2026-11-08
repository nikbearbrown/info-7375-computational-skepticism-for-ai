# Foundations case: The 98% fraud detector

**Chapter:** Foundations (probability and statistics) · **Seeded flaw:** accuracy reported as reliability on imbalanced data · **Key terms:** class imbalance, majority-class baseline, sensitivity (recall), positive predictive value (precision), confusion matrix, threshold

---

# STUDENT PAGE

## 1. Scenario

Marisol runs payments risk at a regional credit union with 1.2 million cardholders. A vendor has sold her a card-fraud model and she must decide whether to switch it on for every cardholder. A false alarm freezes a customer's card; a missed fraud costs the credit union money. She asked an AI analyst to evaluate the model on a month of transactions the model had never seen.

## 2. The instruction given to the AI analyst

> "Evaluate the fraud model on the held-out month of transactions and tell me whether it is reliable enough to deploy to all cardholders."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Evaluation summary: card-fraud model v2**
>
> **Data.** Held-out month: 500,000 transactions, of which 10,000 are confirmed fraud. Model never trained on these rows.
> **Method.** Scored every transaction with the model at its default cutoff of 0.5. Compared the predicted label with the confirmed label.
> **Result.** 490,500 of 500,000 transactions classified correctly. **Accuracy = 98.1%.**
> **Stability.** Accuracy on the first and second half of the month: 98.1% and 98.1%.
> **Checks passed.** No missing values. No duplicate transaction IDs. No test rows found in the training data.
> **Conclusion.** With 98.1% accuracy on unseen data, the model is reliable. **I recommend deploying it to all 1.2 million cardholders.**

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's conclusion? Name the problem with the exact term for it.
2. **(2 points)** Write the one number, comparison or table you would ask the agent to produce that turns "98.1% accuracy" from a headline into evidence.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, explain to Marisol why the 98.1% figure does not yet tell her whether to deploy. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1. Score by criterion; credit counts wherever it appears in the answer sheet.

## Case key

**The flaw in one sentence.** Fraud is 10,000 of 500,000 transactions (2.0%), so a model that flags nothing scores 98.0% accuracy; 98.1% therefore says almost nothing about whether the model finds fraud.

**Full-credit terms (2).** Class imbalance; majority-class baseline; base rate / prevalence (used for this point); "accuracy is misleading when classes are imbalanced".
**Half-credit near-misses (1).** "Accuracy is the wrong metric" with no reason; "need precision/recall" with no imbalance named; "accuracy paradox" with no explanation; "metric problem".
**No credit (0).** Overfitting; data leakage; sampling error; "bias"; "needs more data".

**Acceptable evidence requests (2), either one.**
1. A confusion matrix with sensitivity (recall) and positive predictive value (precision) for the fraud class at a stated threshold (an interval on each is a bonus).
2. A comparison against the majority-class baseline ("flag nothing" = 98.0%) or against the credit union's existing rules.
**Unacceptable (0).** "Run cross-validation", "test on a bigger sample", "check for overfitting" (none of these changes what accuracy measures). "Report F1" alone earns 1 only if the student says why.

**Fix or next step (2).** Re-ask for per-class metrics (sensitivity, PPV, false positive rate) and a baseline comparison; ask for a threshold chosen by the cost of a missed fraud versus a frozen card. 1 point if the instruction names a better metric but not the baseline or cost. AUC alone earns 1.

**Scope and plain language (1).** Two sentences, no jargon, saying that because almost all transactions are honest, a model that never flags anything would also score about 98%, so the figure does not show it catches fraud.

**Traps.**
- A student who writes "98.1% is impressive, but check for overfitting" has accepted the flaw. Catches = 0.
- Students may praise the data hygiene checks (no duplicates, no leakage). Those are fine and are not the flaw.
- "Reliable" in the output is the overreach. A student who objects to the word "reliable" and names imbalance gets full credit; one who objects only to the word gets Catches 1 at most.
- Do not reward a long list of extra metrics. Look for the baseline or per-class idea.

**CAP RULE.** If the student does not identify that accuracy is uninformative here because fraud is rare (Catches = 0), the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. The agent reports accuracy as if it proved reliability, but fraud is only 2% of transactions. This is class imbalance: a model that never flags anything gets 98% accuracy, the majority-class baseline.
2. A confusion matrix with sensitivity and precision on the fraud class, next to the 98.0% flag-nothing baseline.
3. "Re-evaluate and report the confusion matrix, sensitivity, precision and false positive rate at threshold 0.5, compare to a model that flags nothing, and recommend a threshold using the cost of a missed fraud versus a frozen card."
4. "The 98.1% is dominated by the majority class: almost all transactions are honest, so we need the sensitivity on the fraud cases before deciding."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Everything is right; Q4 uses "majority class" and "sensitivity", which a credit-union manager would not know, so the plain-language point is lost.*

**Typical (6/10).**
1. Accuracy is a bad metric here because the data is skewed and the fraud class is small. It can look high even if the model is bad at fraud.
2. Precision and recall.
3. "Re-run the evaluation and use precision and recall instead of accuracy."
4. "The number is high but it can be misleading because fraud is rare."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Understands the problem but says "skewed" and "bad metric" without class imbalance or baseline; asks for metrics but not for a comparison or threshold; no plain-language contrast.*

**Fluent but wrong (3/10).**
1. The model may be overfitting to the held-out month. A 98.1% score with identical halves suggests memorisation, and the dataset's variance across seeds was not reported.
2. Five-fold cross-validation with confidence intervals on the accuracy.
3. "Please run cross-validation, report the generalisation gap and regularise if needed."
4. "We should be careful because the model might be too tuned to this month of data."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses correct vocabulary (generalisation gap, regularise) for the wrong problem; never notices fraud is 2%. Cross-validation does not fix a misleading metric. Cap rule would also hold the case at 5.*
