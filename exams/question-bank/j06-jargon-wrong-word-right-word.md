# Jargon test: wrong word, right word

## MA-jargon.67

A prompt to an AI tool says: "make the model more accurate so it's fair." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model with 95 percent accuracy is fair.
- [ ] B. Fairness is a synonym for accuracy on the test set.
- [ ] C. A precise rewrite is: "Reduce the gap in true positive rates between groups (equal opportunity) and report overall accuracy."
- [ ] D. "Fair" needs a named criterion such as demographic parity or equalized odds.
- [ ] E. Accuracy measures the share of predictions that are correct, which differs from fairness.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: High accuracy can coexist with large gaps between groups.
- B: Fairness compares outcomes or errors across groups.
- C: It names a specific fairness criterion and keeps accuracy as a separate quantity.
- D: The word alone does not say what is being equalised.
- E: Accuracy is overall correctness, not a group comparison.

**Source:** Accuracy vs fairness

## MA-jargon.68

A prompt to an analyst says: "check the data is clean." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Data validation checks that data meet stated rules, such as types, ranges and missing values.
- [ ] B. A precise rewrite names the checks, such as schema validation, missingness, duplicates and outliers.
- [ ] C. Cleaning the data removes sampling bias.
- [ ] D. Provenance is the record of where data came from and how it was changed.
- [ ] E. A dataset that passes validation checks is guaranteed to be accurate.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Validation is rule-based checking of data against a schema or expectations.
- B: "Clean" is vague, while named checks are testable.
- C: Cleaning fixes errors; it does not change who is in the sample.
- D: Provenance documents origin and custody.
- E: Validation checks stated rules, which do not prove the values are true.

**Source:** Clean vs validated

## MA-jargon.69

A report says: "the model is 90 percent confident, so it is 90 percent accurate." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy is the fraction of predictions that are correct.
- [ ] B. Confidence and accuracy are the same quantity.
- [ ] C. Confidence is the probability the model assigns to its prediction.
- [ ] D. Calibration is the match between stated confidence and the observed frequency of being correct.
- [ ] E. If 90 percent confident predictions are right 70 percent of the time, the model is well calibrated.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Accuracy is an observed rate.
- B: One is a stated probability and the other an observed rate.
- C: Confidence is the model's stated probability.
- D: A calibrated 90 percent confidence is right about 90 percent of the time.
- E: That model is overconfident, so it is poorly calibrated.

**Source:** Confidence vs accuracy vs calibration

## MA-jargon.70

An analyst writes: "this 95 percent confidence interval means there is a 95 percent probability the true effect lies inside it." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The terms credible interval and confidence interval are interchangeable.
- [ ] B. A p-value is the posterior probability that the null hypothesis is true.
- [ ] C. A credible interval is a range built from repeated sampling in the long run.
- [ ] D. The 95 percent in a confidence interval refers to the long-run share of such intervals that cover the true value.
- [ ] E. The analyst's sentence describes a credible interval, not a confidence interval.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: They rest on different definitions of probability.
- B: A p-value is computed assuming the null hypothesis, and it is not a posterior probability.
- C: That describes a confidence interval; a credible interval is a Bayesian posterior range.
- D: The coverage is a property of the procedure over repeated samples.
- E: A direct probability statement about the parameter is Bayesian.

**Source:** Confidence interval vs credible interval

## MA-jargon.71

A message says: "the model degraded because of drift. The mix of inputs shifted, but the relationship between inputs and outcome is the same." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The word "drift" alone states which distribution changed.
- [ ] B. Label shift means the distribution of outcomes changes while the input distribution given the outcome stays the same.
- [ ] C. Covariate shift means the distribution of inputs changes while the relationship between inputs and outcome stays the same.
- [ ] D. Concept drift means the relationship between inputs and outcome changes over time.
- [ ] E. The case in the message is covariate shift.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: "Drift" is vague; covariate shift, concept drift and label shift name the change.
- B: It changes P(y) and leaves P(x given y) alone.
- C: It changes P(x) and leaves P(y given x) alone.
- D: The conditional distribution of the outcome given the inputs moves.
- E: Inputs changed and the input-to-outcome relationship did not.

**Source:** Covariate shift, concept drift, label shift

## MA-jargon.72

A manager says: "verify the model works for patients" and wants evidence the model serves its purpose on real patients. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Checking the model against its written specification in a test is verification.
- [ ] B. Validation asks whether the right system was built, meaning it serves its real purpose.
- [ ] C. Verification asks whether the system was built right, meaning it meets its specification.
- [ ] D. Evidence on real patients is validation.
- [ ] E. A unit test that the code computes a specified formula is validation.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Verification confirms the build meets its spec.
- B: Validation checks fit to the real need.
- C: Verification checks against the specification.
- D: It tests the purpose in the real setting.
- E: That is verification against a specification.

**Source:** Verification vs validation

## MA-jargon.73

A report says: "the test is 99 percent accurate at spotting the disease, so a positive result means a 99 percent chance of disease." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Precision, also called positive predictive value, is the share of positive results that are true cases.
- [ ] B. A sensitivity of 99 percent gives a precision of 99 percent.
- [ ] C. Specificity is the share of people without the disease whom the test clears.
- [ ] D. Sensitivity is the share of people with the disease whom the test flags.
- [ ] E. Precision depends on prevalence as well as on sensitivity and specificity.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It answers what a positive result means.
- B: Precision also depends on how common the disease is.
- C: It is the true negative rate.
- D: It is the true positive rate.
- E: Rare conditions produce many false positives even with a strong test.

**Source:** Sensitivity, specificity, precision

## MA-jargon.74

A report says: "the p-value is 0.03, so there is a 97 percent chance the effect is real." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A p-value is computed by assuming the null hypothesis.
- [ ] B. A p-value is the probability of data at least this extreme if the null hypothesis were true.
- [ ] C. A p-value is the probability that the null hypothesis is true.
- [ ] D. A p-value of 0.03 means a 97 percent probability that the effect is real.
- [ ] E. A posterior probability is the probability of a hypothesis given the data, in the Bayesian sense.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The null defines the reference distribution.
- B: It is a probability of data given the null.
- C: It assumes the null, so it cannot be the probability of the null.
- D: The p-value is not a probability that the effect is real.
- E: It conditions on the data.

**Source:** p-value vs posterior probability

## MA-jargon.75

A prompt says: "make the model robust against attacks and against new data." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Distribution shift means test inputs come from a different distribution than the training data.
- [ ] B. Robustness to distribution shift is tested with adversarial examples.
- [ ] C. Adversarial robustness is measured on held-out data from the same distribution.
- [ ] D. Adversarial robustness concerns small deliberate input perturbations designed to cause errors.
- [ ] E. An adversarial example is naturally occurring noise in the data.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: It is a change in the data-generating distribution.
- B: It is tested with data from a shifted distribution.
- C: Same-distribution held-out data tests ordinary generalization.
- D: Adversarial examples are crafted to fool the model.
- E: It is a deliberate perturbation.

**Source:** Adversarial robustness vs distribution shift

## MA-jargon.76

An analyst asks an AI for "the data lineage" but wants to know who collected the dataset and under what licence. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Joins and aggregations applied to a table belong to provenance rather than lineage.
- [ ] B. Lineage tracks transformations from a source to a derived table or feature.
- [ ] C. The question as asked is about lineage.
- [ ] D. Who collected the data and under what licence is a question about lineage.
- [ ] E. Provenance records origin and custody: who collected the data, when, how, and under what terms.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Processing steps are lineage.
- B: Lineage follows the chain of processing.
- C: It asks about origin and terms, which is provenance.
- D: That is provenance.
- E: Provenance answers where the data came from.

**Source:** Provenance vs lineage

## MA-jargon.77

A student says: "the model memorised the training set, so it has high bias." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Overfitting is the result of high bias.
- [ ] B. High bias means the model is flexible enough to memorise noise.
- [ ] C. High variance means the model is too simple to capture the pattern.
- [ ] D. Overfitting means low error on training data and high error on held-out data.
- [ ] E. Bias in the bias-variance sense is the same as demographic bias.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Overfitting is typically associated with high variance.
- B: High bias means the model is too simple, which is underfitting.
- C: High variance means sensitivity to the particular training sample.
- D: The model fits noise in the training set.
- E: The statistical bias-variance sense is about systematic error of the model's predictions, not about groups.

**Source:** Overfitting, bias, variance

## MA-jargon.78

An analyst writes: "I tuned the hyperparameters on the test set, then reported the best test score." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tuning on the test set is the same as cross-validation.
- [ ] B. Data leakage is information from outside the training data, such as test labels, influencing the training.
- [ ] C. A validation set is used to tune hyperparameters and choose between models.
- [ ] D. A test set is held back for the final estimate of generalization.
- [ ] E. Tuning on the test set leaks information, so the reported score is optimistic.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Cross-validation tunes on folds of the training data, not on the held-back test set.
- B: Leakage breaks the separation between fitting and evaluation.
- C: It guides model selection.
- D: It is used once the choices are made.
- E: The test data influenced the choices, so it no longer measures unseen performance.

**Source:** Validation set, test set, leakage

## MA-jargon.79

A prompt says: "collect more data to reduce the model's uncertainty about the noisy sensor readings." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Epistemic uncertainty comes from limited knowledge or data and can shrink with more data.
- [ ] B. More data reduces aleatoric uncertainty.
- [ ] C. Uncertainty about a parameter from a small sample is aleatoric.
- [ ] D. Aleatoric uncertainty is noise inherent in the data.
- [ ] E. The word "uncertainty" alone does not say which kind, so a rewrite should name aleatoric or epistemic.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: More data informs the model.
- B: Inherent noise stays the same.
- C: That is epistemic.
- D: It remains however much data is collected.
- E: The two kinds respond differently to more data.

**Source:** Aleatoric vs epistemic uncertainty

## MA-jargon.80

A report says: "ads and sales are correlated, so ad spend is a confounder of sales", and also treats the correlation as proof that ads drive sales. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The correlation coefficient measures how well a nonlinear curve fits the data.
- [ ] B. A strong correlation shows that one variable causes the other.
- [ ] C. A spurious correlation is an association not due to a causal link between the variables.
- [ ] D. A confounder is a common cause of both the exposure and the outcome.
- [ ] E. A correlation of zero shows the variables are independent.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The standard correlation coefficient measures linear association.
- B: Association alone does not establish a causal direction.
- C: It can arise from chance or a confounder.
- D: It creates association without a direct causal link.
- E: Zero linear correlation leaves room for a nonlinear relationship.

**Source:** Correlation, confounder, spurious correlation
