# INFO 7375 Computational Skepticism for AI: practice exam 04: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** Match each situation to a shift term. Check each statement that is true.  *(5 points)*

- [ ] A. A seasonal change in input features alone is concept drift.
- [ ] B. A disease becomes more common while its symptoms given the disease stay the same, which is label shift.
- [ ] C. A change in P(y | x) is called covariate shift.
- [ ] D. Fraudsters change tactics so the same transaction features now mean fraud, which is concept drift.
- [ ] E. Photos arrive from a new phone model under the same labelling rule, which is label shift.

**Key:** A=F B=T C=F D=T E=F  |  `MA-jargon.26`  |  *Jargon test: robustness and distribution shift*  |  source: Match the shift term

- A (false): Changes confined to inputs are covariate shift.
- B (true): The class prior changed.
- C (false): That change is concept drift.
- D (true): The input-to-target relationship changed.
- E (false): Only the input distribution changed, so it is covariate shift.

**2.** An audit finds similar error rates for women overall and for older people overall, but high error for older women. Check each statement that is true.  *(5 points)*

- [ ] A. Good results on each single attribute can hide poor results at the intersection.
- [ ] B. Reporting metrics by gender and by age separately is an intersectional analysis.
- [ ] C. Intersectional analysis examines subgroups defined by combinations of attributes.
- [ ] D. Intersectional means measuring fairness across different time periods.
- [ ] E. Intersectional subgroups can be small, so estimates there can be noisy.

**Key:** A=T B=F C=T D=F E=T  |  `MA-jargon.62`  |  *Jargon test: bias and fairness*  |  source: Intersectional analysis

- A (true): Averages over a single attribute can mask a small subgroup.
- B (false): Separate breakdowns miss the combined subgroups.
- C (true): Intersections like older women are the unit of analysis.
- D (false): It refers to overlapping group memberships, not time.
- E (true): Small groups give wide uncertainty.

**3.** An auditor reviews a model against the principle that similar individuals should be treated similarly. Check each statement that is true.  *(5 points)*

- [ ] A. It can be evaluated from per-group confusion matrices alone.
- [ ] B. The Lipschitz form bounds the difference in two people's outcomes by a distance between the people.
- [ ] C. This principle is called individual fairness.
- [ ] D. Applying it requires a similarity metric chosen for the task.
- [ ] E. Individual fairness implies demographic parity.

**Key:** A=F B=T C=T D=T E=F  |  `MA-ch07.20`  |  *None*  |  source: Individual fairness and the similarity metric

- A (false): Confusion matrices average over individuals and lose pairwise comparisons.
- B (true): Similar people must receive similar outcome distributions.
- C (true): It compares how individuals are treated rather than group averages.
- D (true): Someone must say which differences between people are relevant.
- E (false): Similar treatment of similar people can coexist with different group selection rates.

**4.** An analyst summarizes data with statistics and plots. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Pearson correlation measures linear association, so a perfect nonlinear relationship can have a correlation near 0.
- [ ] B. A Pearson correlation of 0.9 in observational data is a causal effect.
- [ ] C. A spike at exactly 0 in a measurement that should be continuous suggests a sentinel value such as a default or missing-value code.
- [ ] D. Datasets with identical summary statistics produce identical scatter plots.
- [ ] E. Pearson correlation is a robust statistic that one outlier barely changes.

**Key:** A=T B=F C=T D=F E=F  |  `MA-4.5`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Pearson correlation, sentinel value, Anscombe's quartet, correlation versus causation

- A (true): Y = X² on a symmetric range has correlation 0 with X.
- B (false): Correlation is association; confounding or reverse causation can produce it without causation.
- C (true): A sentinel value is a placeholder entered in place of a real measurement.
- D (false): Anscombe's quartet shows very different plots that share the same means, variances and correlation.
- E (false): One far point can move the correlation from near 0 to near 1.

**5.** A scorer assigns probabilities of being positive to nine cases, and an analyst compares AUC, calibration and log loss for it. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Cubing the scores leaves the AUC unchanged.
- [ ] B. A high AUC guarantees that the scores are well calibrated.
- [ ] C. Log loss treats a confident wrong prediction the same as an unsure wrong one.
- [ ] D. AUC is the probability that a randomly chosen positive is scored above a randomly chosen negative, so it measures discrimination (ranking).
- [ ] E. Calibration means that predicted probabilities match observed frequencies, such as 70% of cases scored 0.7 being positive.

**Key:** A=T B=F C=F D=T E=T  |  `MA-5.5`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: AUC, discrimination, calibration, log loss

- A (true): A monotonic transformation preserves the ranking, and AUC depends only on ranking.
- B (false): AUC measures ranking, so a well-ranked scorer can still have scores that do not match observed frequencies.
- C (false): Log loss grows steeply as the probability given to the true outcome approaches 0.
- D (true): AUC uses only the order of the scores.
- E (true): Calibration compares predicted probability with the actual rate.

**6.** An agent run makes 500 tool calls. Each call fails with probability 0.002, independently, and one failed call ruins the run. A manager calls 99.8% per-call reliability "basically perfect". Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. A Poisson distribution with mean n × p approximates this binomial when n is large and p is small.
- [ ] B. Small per-step failure probabilities compound across steps and lower end-to-end success.
- [ ] C. The number of failed calls per run is binomial with 500 trials and a per-trial failure probability of 0.002.
- [ ] D. Failures that share a cause, such as a down service, are positively correlated, so the independence-based figure for run success should be checked against observed runs.
- [ ] E. Per-call reliability and per-run (end-to-end) reliability are the same quantity.

**Key:** A=T B=T C=T D=T E=F  |  `MA-2.6`  |  *2. Random variables and distributions*  |  source: Binomial, Poisson approximation, compounding, end-to-end reliability

- A (true): The Poisson approximation to the binomial is the rare-event limit.
- B (true): The chance of no failure is (1 − p) raised to the number of steps.
- C (true): Fixed number of independent trials with equal failure probability gives a binomial count.
- D (true): Correlated failures violate the independence assumption behind the product rule.
- E (false): Per-run reliability is a product over steps and is much lower than the per-call figure.

**7.** Two automated checkers each miss a given defect with probability 0.10, and a reviewer asks whether the two misses are independent events. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. Independence means the two events do not occur together.
- [ ] B. If P(second misses | first misses) equals 1, the two misses are independent events.
- [ ] C. Two events are independent when the joint probability equals the product of the two marginal probabilities.
- [ ] D. Two checkers built with the same method that tend to miss the same defects have independent misses.
- [ ] E. Mutually exclusive events that each have positive probability are independent.

**Key:** A=F B=F C=T D=F E=F  |  `MA-1.3`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Independence and dependence of events

- A (false): Events that do not occur together are mutually exclusive, which is a different property from independence.
- B (false): Independence needs the conditional probability to equal the marginal 0.10; a value of 1 is extreme dependence.
- C (true): The product rule for joint probability is the definition of independence.
- D (false): Shared blind spots make the misses positively dependent, not independent.
- E (false): If one occurs the other has probability 0, so knowing one changes the other; they are dependent.

**8.** An analyst fits a depth-3 decision tree to imitate a black-box model and reads the tree to understand the black box. Check each statement that is true.  *(5 points)*

- [ ] A. High fidelity on held-out inputs is not proof that the black box uses the same internal logic.
- [ ] B. The tree is a surrogate model of the black box.
- [ ] C. A surrogate fitted near one input is called a global surrogate.
- [ ] D. Agreement of the tree with the true labels is the measure of surrogate fidelity.
- [ ] E. The tree is trained on the true labels so that it explains the black box.

**Key:** A=T B=T C=F D=F E=F  |  `MA-jargon.45`  |  *Jargon test: explainability*  |  source: Surrogate model

- A (true): Matching outputs does not show matching reasoning.
- B (true): A surrogate is a simpler model fitted to approximate a more complex one.
- C (false): A surrogate fitted near one input is a local surrogate.
- D (false): Fidelity is agreement with the black box's outputs.
- E (false): To explain the black box the surrogate is trained on the black box's own predictions.

**9.** A prompt to an AI tool says: "make the model more accurate so it's fair." Check each statement that is true.  *(5 points)*

- [ ] A. A model with 95 percent accuracy is fair.
- [ ] B. Fairness is a synonym for accuracy on the test set.
- [ ] C. A precise rewrite is: "Reduce the gap in true positive rates between groups (equal opportunity) and report overall accuracy."
- [ ] D. "Fair" needs a named criterion such as demographic parity or equalized odds.
- [ ] E. Accuracy measures the share of predictions that are correct, which differs from fairness.

**Key:** A=F B=F C=T D=T E=T  |  `MA-jargon.67`  |  *Jargon test: wrong word, right word*  |  source: Accuracy vs fairness

- A (false): High accuracy can coexist with large gaps between groups.
- B (false): Fairness compares outcomes or errors across groups.
- C (true): It names a specific fairness criterion and keeps accuracy as a separate quantity.
- D (true): The word alone does not say what is being equalised.
- E (true): Accuracy is overall correctness, not a group comparison.

**10.** A team runs 20 retrieval-quality trials, and the result is non-significant. Another analyst notes the sample was small. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Low power makes a non-significant result strong evidence that there is no effect.
- [ ] B. Statistical power is the probability of rejecting the null hypothesis when a true effect of a given size exists.
- [ ] C. A confidence interval that includes zero and also includes large benefits marks the study as inconclusive.
- [ ] D. An equivalence test is the tool for supporting the claim of "no meaningful effect".
- [ ] E. A non-significant result does not show the null hypothesis is true: absence of evidence differs from evidence of absence.

**Key:** A=F B=T C=T D=T E=T  |  `MA-3.8`  |  *3. Sampling, the central limit theorem and inference*  |  source: Absence of evidence, statistical power, equivalence test, inconclusive result

- A (false): With low power the test would likely miss a real effect, so the result is uninformative.
- B (true): Low power makes a non-significant result expected even if the effect is real.
- C (true): The data are compatible with both no effect and a sizable one.
- D (true): Equivalence testing sets a margin and tests that the effect lies within it.
- E (true): Failing to reject is not the same as confirming no effect.

**11.** Income is missing more often for people with high income, and a reviewer asks for the exact missingness type. Check each statement that is true.  *(5 points)*

- [ ] A. MCAR means the chance of a value being missing is unrelated to observed and unobserved values.
- [ ] B. MAR means missingness depends on observed variables but not on the missing value once they are accounted for.
- [ ] C. This pattern is MNAR, missing not at random.
- [ ] D. Older respondents skipping a question, with age recorded, is MNAR.
- [ ] E. Dropping incomplete rows is unbiased under MNAR.

**Key:** A=T B=T C=T D=F E=F  |  `MA-jargon.18`  |  *Jargon test: data validation and provenance*  |  source: MCAR vs MAR vs MNAR

- A (true): MCAR is missing completely at random.
- B (true): MAR is missing at random given recorded variables.
- C (true): Missingness depends on the unobserved value itself.
- D (false): It depends on an observed variable, so it is MAR.
- E (false): Under MNAR the remaining rows are a biased sample.

**12.** A model says it is 90% confident on a set of cases and is right on 65% of them. Check each statement that is true.  *(5 points)*

- [ ] A. A reliability diagram shows the gap between confidence and observed frequency.
- [ ] B. Overconfidence means stated confidence exceeds observed accuracy.
- [ ] C. Raising AUC repairs overconfidence.
- [ ] D. The model is underconfident.
- [ ] E. Expected calibration error is a ranking metric like AUC.

**Key:** A=T B=T C=F D=F E=F  |  `MA-jargon.10`  |  *Jargon test: probability and confidence*  |  source: Overconfidence

- A (true): It plots observed accuracy against stated confidence in bins.
- B (true): The model claims more certainty than it earns.
- C (false): AUC measures discrimination and does not fix the calibration gap.
- D (false): Underconfidence is the opposite gap.
- E (false): It averages the confidence-accuracy gap and is a calibration measure.

**13.** A model that was well calibrated on its validation set is deployed on shifted data. Check each statement that is true.  *(5 points)*

- [ ] A. Overconfidence under shift means accuracy exceeds stated confidence.
- [ ] B. Under distribution shift, calibration often degrades.
- [ ] C. A model calibrated on its validation set stays calibrated under shift.
- [ ] D. Calibration can be re-measured on a labelled sample of shifted data.
- [ ] E. Temperature scaling fitted on in-distribution data repairs calibration on shifted data.

**Key:** A=F B=T C=F D=T E=F  |  `MA-jargon.33`  |  *Jargon test: robustness and distribution shift*  |  source: Calibration under shift

- A (false): That is underconfidence.
- B (true): Stated probabilities stop matching observed frequencies.
- C (false): Calibration is tied to the distribution it was fitted on.
- D (true): A fresh reliability check shows the current gap.
- E (false): The fitted correction reflects the old distribution.

**14.** An analyst says: "the model has disparate treatment because the false negative rate is higher for group B, even though group is not an input." Check each statement that is true.  *(5 points)*

- [ ] A. Equalized odds would also ask for matching false positive rates.
- [ ] B. A higher false negative rate means a lower true positive rate for that group.
- [ ] C. Equal opportunity is the criterion that targets a gap in true positive rates.
- [ ] D. Disparate treatment fits because group is not an input.
- [ ] E. Unequal error rates with no group input are closer to disparate impact.

**Key:** A=T B=T C=T D=F E=T  |  `MA-jargon.63`  |  *Jargon test: bias and fairness*  |  source: Wrong word: disparate treatment

- A (true): Equalized odds covers both true and false positive rates.
- B (true): False negative rate plus true positive rate equal one.
- C (true): It requires matching true positive rates.
- D (false): Treatment concerns using the attribute, which did not happen here.
- E (true): The practice is neutral on its face but outcomes differ.

**15.** A model's Brier score is compared with that of a reference forecaster who predicts the base rate for every case. Check each statement that is true.  *(5 points)*

- [ ] A. The reference forecaster has a Brier score of 0 because it is calibrated.
- [ ] B. Brier scores from test sets with different base rates are directly comparable without a reference.
- [ ] C. The reference forecast is calibrated in aggregate and has no discrimination.
- [ ] D. A forecast of the base rate for each case is a climatological reference.
- [ ] E. A Brier skill score measures improvement relative to a reference forecast.

**Key:** A=F B=F C=T D=T E=T  |  `MA-ch02.29`  |  *None*  |  source: Brier skill score and reference forecast

- A (false): Calibration without discrimination still leaves a positive Brier score.
- B (false): The score of a trivial forecast depends on the base rate.
- C (true): A constant base-rate forecast matches overall frequency but ranks nothing.
- D (true): Such a constant forecast is the standard no-skill baseline.
- E (true): It is 1 minus the ratio of the model's score to the reference score.

**16.** A column has 10 rows; five values are observed and five are missing. An analyst fills each blank with the observed mean and treats the 10 rows as real data. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Mean imputation removes the bias when missingness is MNAR.
- [ ] B. Median imputation preserves the original variance.
- [ ] C. Mean imputation leaves the sample mean unchanged and shrinks the sample variance.
- [ ] D. Multiple imputation fills each blank once with the single best guess.
- [ ] E. Treating imputed values as observed data makes the standard error too small and overstates precision.

**Key:** A=F B=F C=T D=F E=T  |  `MA-4.2`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Mean imputation, multiple imputation, standard error

- A (false): If missingness depends on the missing value, filling with the observed mean keeps the bias.
- B (false): A single constant at the center lowers the variance, whether it is the mean or the median.
- C (true): Adding values equal to the mean adds no spread.
- D (false): Multiple imputation creates several completed datasets so the uncertainty about the imputed values is carried through.
- E (true): The invented values add rows without adding information.

**17.** A logistic regression predicts whether an account is flagged: log-odds of being flagged = −2.0 + 0.9 × x, where x is the number of prior incidents. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The coefficient 0.9 is the change in log-odds of being flagged for one more prior incident.
- [ ] B. The exponential of the coefficient, about 2.46, is an odds ratio per additional incident.
- [ ] C. Odds are the probability p divided by 1 minus p.
- [ ] D. Each additional prior incident multiplies the predicted probability of being flagged by 2.46.
- [ ] E. The effect of one more incident on the predicted probability is constant across the range of x.

**Key:** A=T B=T C=T D=F E=F  |  `MA-5.4`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Log-odds, odds, odds ratio, predicted probability

- A (true): Logistic regression is linear in the log-odds.
- B (true): Each added incident multiplies the odds by exp(0.9).
- C (true): Odds compare the chance of the event with the chance of its complement.
- D (false): The coefficient acts on the odds, not on the probability.
- E (false): The probability curve is S-shaped, so the change in probability depends on where you start.

**18.** A mail filter knows that 30% of messages are spam, that the word "urgent" appears in 60% of spam and in 10% of legitimate messages, and it wants the chance that a message containing "urgent" is spam. Which statements name the pieces correctly? Check each statement that is true.  *(5 points)*

- [ ] A. P("urgent" | spam) = 0.60 is a likelihood and is a different quantity from the posterior probability of spam.
- [ ] B. P(spam | "urgent") is the posterior probability.
- [ ] C. The likelihood ratio is the posterior probability divided by the prior probability.
- [ ] D. Posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] E. The 30% share of spam before looking at the word is the prior probability.

**Key:** A=T B=T C=F D=T E=T  |  `MA-1.5`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Prior, likelihood, posterior, likelihood ratio, odds

- A (true): A likelihood is the probability of the evidence given a hypothesis; the posterior is the probability of the hypothesis given the evidence.
- B (true): The posterior is the updated probability of the hypothesis after the evidence.
- C (false): The likelihood ratio compares the probability of the evidence under two hypotheses, here 0.60 divided by 0.10.
- D (true): This is the odds form of Bayes' rule.
- E (true): The prior is the probability assigned before the evidence is considered.

**19.** A language model writes step-by-step reasoning before giving an answer, and a user treats that reasoning as the explanation of the answer. Check each statement that is true.  *(5 points)*

- [ ] A. A chain-of-thought is a different thing from an attribution over the input features.
- [ ] B. A model's after-the-fact account of why it answered is a post-hoc rationale that may not reflect the computation.
- [ ] C. One faithfulness test is to add a hint to the input and check whether the answer changes while the reasoning does not mention the hint.
- [ ] D. A plausible chain-of-thought is evidence that it is faithful.
- [ ] E. Chain-of-thought is generated text, so it is not by itself a faithful account of the model's computation.

**Key:** A=T B=T C=T D=F E=T  |  `MA-jargon.50`  |  *Jargon test: explainability*  |  source: Chain-of-thought as explanation

- A (true): One is generated text and the other is a score assigned to inputs.
- B (true): Asking the model why afterwards yields a rationale, not a trace of the mechanism.
- C (true): An intervention that changes the answer but not the stated reasoning shows the reasoning is unfaithful.
- D (false): Plausibility and faithfulness are different properties.
- E (true): The text is an output and may not reflect the process that produced the answer.

**20.** A report says: "the test is 99 percent accurate at spotting the disease, so a positive result means a 99 percent chance of disease." Check each statement that is true.  *(5 points)*

- [ ] A. Precision, also called positive predictive value, is the share of positive results that are true cases.
- [ ] B. A sensitivity of 99 percent gives a precision of 99 percent.
- [ ] C. Specificity is the share of people without the disease whom the test clears.
- [ ] D. Sensitivity is the share of people with the disease whom the test flags.
- [ ] E. Precision depends on prevalence as well as on sensitivity and specificity.

**Key:** A=T B=F C=T D=T E=T  |  `MA-jargon.73`  |  *Jargon test: wrong word, right word*  |  source: Sensitivity, specificity, precision

- A (true): It answers what a positive result means.
- B (false): Precision also depends on how common the disease is.
- C (true): It is the true negative rate.
- D (true): It is the true positive rate.
- E (true): Rare conditions produce many false positives even with a strong test.
