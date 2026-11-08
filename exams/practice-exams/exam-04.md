# INFO 7375 Computational Skepticism for AI: practice exam 04

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** Match each situation to a shift term. Check each statement that is true.  *(5 points)*

- [ ] A. A seasonal change in input features alone is concept drift.
- [ ] B. A disease becomes more common while its symptoms given the disease stay the same, which is label shift.
- [ ] C. A change in P(y | x) is called covariate shift.
- [ ] D. Fraudsters change tactics so the same transaction features now mean fraud, which is concept drift.
- [ ] E. Photos arrive from a new phone model under the same labelling rule, which is label shift.

**2.** An audit finds similar error rates for women overall and for older people overall, but high error for older women. Check each statement that is true.  *(5 points)*

- [ ] A. Good results on each single attribute can hide poor results at the intersection.
- [ ] B. Reporting metrics by gender and by age separately is an intersectional analysis.
- [ ] C. Intersectional analysis examines subgroups defined by combinations of attributes.
- [ ] D. Intersectional means measuring fairness across different time periods.
- [ ] E. Intersectional subgroups can be small, so estimates there can be noisy.

**3.** An auditor reviews a model against the principle that similar individuals should be treated similarly. Check each statement that is true.  *(5 points)*

- [ ] A. It can be evaluated from per-group confusion matrices alone.
- [ ] B. The Lipschitz form bounds the difference in two people's outcomes by a distance between the people.
- [ ] C. This principle is called individual fairness.
- [ ] D. Applying it requires a similarity metric chosen for the task.
- [ ] E. Individual fairness implies demographic parity.

**4.** An analyst summarizes data with statistics and plots. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Pearson correlation measures linear association, so a perfect nonlinear relationship can have a correlation near 0.
- [ ] B. A Pearson correlation of 0.9 in observational data is a causal effect.
- [ ] C. A spike at exactly 0 in a measurement that should be continuous suggests a sentinel value such as a default or missing-value code.
- [ ] D. Datasets with identical summary statistics produce identical scatter plots.
- [ ] E. Pearson correlation is a robust statistic that one outlier barely changes.

**5.** A scorer assigns probabilities of being positive to nine cases, and an analyst compares AUC, calibration and log loss for it. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Cubing the scores leaves the AUC unchanged.
- [ ] B. A high AUC guarantees that the scores are well calibrated.
- [ ] C. Log loss treats a confident wrong prediction the same as an unsure wrong one.
- [ ] D. AUC is the probability that a randomly chosen positive is scored above a randomly chosen negative, so it measures discrimination (ranking).
- [ ] E. Calibration means that predicted probabilities match observed frequencies, such as 70% of cases scored 0.7 being positive.

**6.** An agent run makes 500 tool calls. Each call fails with probability 0.002, independently, and one failed call ruins the run. A manager calls 99.8% per-call reliability "basically perfect". Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. A Poisson distribution with mean n × p approximates this binomial when n is large and p is small.
- [ ] B. Small per-step failure probabilities compound across steps and lower end-to-end success.
- [ ] C. The number of failed calls per run is binomial with 500 trials and a per-trial failure probability of 0.002.
- [ ] D. Failures that share a cause, such as a down service, are positively correlated, so the independence-based figure for run success should be checked against observed runs.
- [ ] E. Per-call reliability and per-run (end-to-end) reliability are the same quantity.

**7.** Two automated checkers each miss a given defect with probability 0.10, and a reviewer asks whether the two misses are independent events. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. Independence means the two events do not occur together.
- [ ] B. If P(second misses | first misses) equals 1, the two misses are independent events.
- [ ] C. Two events are independent when the joint probability equals the product of the two marginal probabilities.
- [ ] D. Two checkers built with the same method that tend to miss the same defects have independent misses.
- [ ] E. Mutually exclusive events that each have positive probability are independent.

**8.** An analyst fits a depth-3 decision tree to imitate a black-box model and reads the tree to understand the black box. Check each statement that is true.  *(5 points)*

- [ ] A. High fidelity on held-out inputs is not proof that the black box uses the same internal logic.
- [ ] B. The tree is a surrogate model of the black box.
- [ ] C. A surrogate fitted near one input is called a global surrogate.
- [ ] D. Agreement of the tree with the true labels is the measure of surrogate fidelity.
- [ ] E. The tree is trained on the true labels so that it explains the black box.

**9.** A prompt to an AI tool says: "make the model more accurate so it's fair." Check each statement that is true.  *(5 points)*

- [ ] A. A model with 95 percent accuracy is fair.
- [ ] B. Fairness is a synonym for accuracy on the test set.
- [ ] C. A precise rewrite is: "Reduce the gap in true positive rates between groups (equal opportunity) and report overall accuracy."
- [ ] D. "Fair" needs a named criterion such as demographic parity or equalized odds.
- [ ] E. Accuracy measures the share of predictions that are correct, which differs from fairness.

**10.** A team runs 20 retrieval-quality trials, and the result is non-significant. Another analyst notes the sample was small. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Low power makes a non-significant result strong evidence that there is no effect.
- [ ] B. Statistical power is the probability of rejecting the null hypothesis when a true effect of a given size exists.
- [ ] C. A confidence interval that includes zero and also includes large benefits marks the study as inconclusive.
- [ ] D. An equivalence test is the tool for supporting the claim of "no meaningful effect".
- [ ] E. A non-significant result does not show the null hypothesis is true: absence of evidence differs from evidence of absence.

**11.** Income is missing more often for people with high income, and a reviewer asks for the exact missingness type. Check each statement that is true.  *(5 points)*

- [ ] A. MCAR means the chance of a value being missing is unrelated to observed and unobserved values.
- [ ] B. MAR means missingness depends on observed variables but not on the missing value once they are accounted for.
- [ ] C. This pattern is MNAR, missing not at random.
- [ ] D. Older respondents skipping a question, with age recorded, is MNAR.
- [ ] E. Dropping incomplete rows is unbiased under MNAR.

**12.** A model says it is 90% confident on a set of cases and is right on 65% of them. Check each statement that is true.  *(5 points)*

- [ ] A. A reliability diagram shows the gap between confidence and observed frequency.
- [ ] B. Overconfidence means stated confidence exceeds observed accuracy.
- [ ] C. Raising AUC repairs overconfidence.
- [ ] D. The model is underconfident.
- [ ] E. Expected calibration error is a ranking metric like AUC.

**13.** A model that was well calibrated on its validation set is deployed on shifted data. Check each statement that is true.  *(5 points)*

- [ ] A. Overconfidence under shift means accuracy exceeds stated confidence.
- [ ] B. Under distribution shift, calibration often degrades.
- [ ] C. A model calibrated on its validation set stays calibrated under shift.
- [ ] D. Calibration can be re-measured on a labelled sample of shifted data.
- [ ] E. Temperature scaling fitted on in-distribution data repairs calibration on shifted data.

**14.** An analyst says: "the model has disparate treatment because the false negative rate is higher for group B, even though group is not an input." Check each statement that is true.  *(5 points)*

- [ ] A. Equalized odds would also ask for matching false positive rates.
- [ ] B. A higher false negative rate means a lower true positive rate for that group.
- [ ] C. Equal opportunity is the criterion that targets a gap in true positive rates.
- [ ] D. Disparate treatment fits because group is not an input.
- [ ] E. Unequal error rates with no group input are closer to disparate impact.

**15.** A model's Brier score is compared with that of a reference forecaster who predicts the base rate for every case. Check each statement that is true.  *(5 points)*

- [ ] A. The reference forecaster has a Brier score of 0 because it is calibrated.
- [ ] B. Brier scores from test sets with different base rates are directly comparable without a reference.
- [ ] C. The reference forecast is calibrated in aggregate and has no discrimination.
- [ ] D. A forecast of the base rate for each case is a climatological reference.
- [ ] E. A Brier skill score measures improvement relative to a reference forecast.

**16.** A column has 10 rows; five values are observed and five are missing. An analyst fills each blank with the observed mean and treats the 10 rows as real data. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Mean imputation removes the bias when missingness is MNAR.
- [ ] B. Median imputation preserves the original variance.
- [ ] C. Mean imputation leaves the sample mean unchanged and shrinks the sample variance.
- [ ] D. Multiple imputation fills each blank once with the single best guess.
- [ ] E. Treating imputed values as observed data makes the standard error too small and overstates precision.

**17.** A logistic regression predicts whether an account is flagged: log-odds of being flagged = −2.0 + 0.9 × x, where x is the number of prior incidents. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The coefficient 0.9 is the change in log-odds of being flagged for one more prior incident.
- [ ] B. The exponential of the coefficient, about 2.46, is an odds ratio per additional incident.
- [ ] C. Odds are the probability p divided by 1 minus p.
- [ ] D. Each additional prior incident multiplies the predicted probability of being flagged by 2.46.
- [ ] E. The effect of one more incident on the predicted probability is constant across the range of x.

**18.** A mail filter knows that 30% of messages are spam, that the word "urgent" appears in 60% of spam and in 10% of legitimate messages, and it wants the chance that a message containing "urgent" is spam. Which statements name the pieces correctly? Check each statement that is true.  *(5 points)*

- [ ] A. P("urgent" | spam) = 0.60 is a likelihood and is a different quantity from the posterior probability of spam.
- [ ] B. P(spam | "urgent") is the posterior probability.
- [ ] C. The likelihood ratio is the posterior probability divided by the prior probability.
- [ ] D. Posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] E. The 30% share of spam before looking at the word is the prior probability.

**19.** A language model writes step-by-step reasoning before giving an answer, and a user treats that reasoning as the explanation of the answer. Check each statement that is true.  *(5 points)*

- [ ] A. A chain-of-thought is a different thing from an attribution over the input features.
- [ ] B. A model's after-the-fact account of why it answered is a post-hoc rationale that may not reflect the computation.
- [ ] C. One faithfulness test is to add a hint to the input and check whether the answer changes while the reasoning does not mention the hint.
- [ ] D. A plausible chain-of-thought is evidence that it is faithful.
- [ ] E. Chain-of-thought is generated text, so it is not by itself a faithful account of the model's computation.

**20.** A report says: "the test is 99 percent accurate at spotting the disease, so a positive result means a 99 percent chance of disease." Check each statement that is true.  *(5 points)*

- [ ] A. Precision, also called positive predictive value, is the share of positive results that are true cases.
- [ ] B. A sensitivity of 99 percent gives a precision of 99 percent.
- [ ] C. Specificity is the share of people without the disease whom the test clears.
- [ ] D. Sensitivity is the share of people with the disease whom the test flags.
- [ ] E. Precision depends on prevalence as well as on sensitivity and specificity.
