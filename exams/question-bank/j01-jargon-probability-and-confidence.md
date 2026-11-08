# Jargon test: probability and confidence

## MA-jargon.1

A classifier says 0.8 and is right about 80% of the time at that score, but it ranks positive cases above negative cases poorly. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The model is well calibrated.
- [ ] B. Calibration describes agreement between predicted probabilities and observed frequencies.
- [ ] C. Discrimination is the ability to rank positives above negatives, often summarised by AUC.
- [ ] D. The model has high discrimination.
- [ ] E. Accuracy is the same quantity as calibration.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Calibration means predicted probabilities match observed frequencies.
- B: That agreement is the definition of calibration.
- C: AUC measures how well scores separate the classes.
- D: Discrimination is ranking ability, which is poor here.
- E: Accuracy is the share of correct predictions; calibration is about probability values.

**Source:** Calibration vs accuracy vs discrimination

## MA-jargon.2

A prompt asks an analyst for "the likelihood that the coin is fair given 8 heads in 10 flips." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A likelihood function is a probability distribution over the parameter that sums to one.
- [ ] B. The probability that the coin is fair given the data is called a likelihood.
- [ ] C. Likelihood is the probability of the observed data viewed as a function of the parameter.
- [ ] D. Likelihood and posterior probability answer the same question.
- [ ] E. P(data | hypothesis) and P(hypothesis | data) are the same quantity.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A likelihood is not normalised over the parameter.
- B: That quantity is a posterior probability.
- C: Likelihood treats the data as fixed and varies the parameter.
- D: Likelihood is about the data given the parameter; the posterior is about the parameter given the data.
- E: They are different conditional probabilities.

**Source:** Probability vs likelihood

## MA-jargon.3

A report gives a 95% interval for a mean and a second report gives a 95% interval from a Bayesian model. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Confidence interval and credible interval are two names for the same thing.
- [ ] B. A 95% credible interval says that, given the model and prior, the parameter lies in the interval with probability 0.95.
- [ ] C. A confidence interval is a posterior probability statement about the parameter in the one interval computed.
- [ ] D. A 95% confidence interval comes from a procedure that captures the true parameter in about 95% of repeated samples.
- [ ] E. A credible interval needs a prior distribution.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: They have different meanings and different assumptions.
- B: A credible interval is a posterior probability statement.
- C: That reading belongs to a credible interval.
- D: Confidence refers to the long-run behaviour of the procedure.
- E: The posterior, and so the interval, combines prior and likelihood.

**Source:** Confidence interval vs credible interval

## MA-jargon.4

A report says "p = 0.03, so there is a 3% chance the null hypothesis is true." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A posterior probability of the null needs no prior.
- [ ] B. The p-value is the probability of data at least this extreme if the null hypothesis is true.
- [ ] C. The p-value is the posterior probability of the null hypothesis.
- [ ] D. A small p-value gives the probability that the alternative hypothesis is true.
- [ ] E. The report confuses P(data | null) with P(null | data).

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A posterior comes from combining a prior with the likelihood.
- B: That is the definition of a p-value.
- C: A posterior probability is P(null | data), a different quantity.
- D: It does not give a probability for either hypothesis.
- E: The p-value is the first; the quoted sentence claims the second.

**Source:** p-value vs posterior

## MA-jargon.5

A reviewer asks for exact terms for a screening test. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Precision is the share of positive predictions that are truly positive.
- [ ] B. Specificity is the share of actual negatives classified as negative.
- [ ] C. Recall is another name for sensitivity.
- [ ] D. Precision is the share of actual positives that the test catches.
- [ ] E. Specificity is also called the true negative rate.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Precision is also called positive predictive value.
- B: That is the true negative rate.
- C: Both are the true positive rate.
- D: That describes recall; precision concerns the positive predictions.
- E: It measures how well negatives are cleared.

**Source:** Sensitivity, specificity, precision, recall

## MA-jargon.6

A fraud model flags 100 transactions and 40 are fraud. Of 80 fraudulent transactions in total, it flagged those 40, so 40/100 is 0.4 and 40/80 is 0.5. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 0.5 figure is the specificity.
- [ ] B. The 0.4 figure is the precision.
- [ ] C. The 0.4 figure is the recall.
- [ ] D. Legitimate transactions that were flagged are false positives.
- [ ] E. The 0.5 figure is the recall, also called sensitivity.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Specificity concerns actual negatives.
- B: Of the flagged cases, 40 percent are truly fraud.
- C: Recall divides by the actual positives, not the flagged ones.
- D: A false positive is a negative case predicted positive.
- E: Of the actual frauds, half were found.

**Source:** Match the metric to the situation

## MA-jargon.7

A vendor says a rare-disease test is "99% accurate", so a positive result means the patient is almost surely ill. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Positive predictive value is unaffected by the base rate.
- [ ] B. Sensitivity and specificity are defined by prevalence.
- [ ] C. Ignoring the base rate is called overfitting.
- [ ] D. With a low base rate, many positive results can be false positives even for a sensitive test.
- [ ] E. The base rate is the prevalence of the condition in the population tested.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Positive predictive value falls as prevalence falls.
- B: They are properties of the test given the condition and do not depend on prevalence.
- C: Ignoring the base rate is the base rate fallacy.
- D: Few true cases means false positives from the large healthy group can dominate.
- E: Base rate means how common the condition is before testing.

**Source:** Base rate

## MA-jargon.8

An engineer writes P(A and B) in a prompt but means the probability of A once B is known to have occurred. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(A | B) equals P(A and B) divided by P(B) when P(B) is positive.
- [ ] B. P(A | B) is the probability of A given that B has occurred.
- [ ] C. P(A and B) is called the marginal probability of A.
- [ ] D. P(A | B) and P(B | A) are the same quantity.
- [ ] E. A joint probability can exceed the marginal probability of one of its events.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: That is the definition of conditional probability.
- B: The bar means conditioning on B.
- C: P(A and B) is the joint probability.
- D: They condition on different events and generally differ.
- E: The joint is bounded above by each marginal.

**Source:** Conditional vs joint probability

## MA-jargon.9

A dashboard shows "churn will be 12%" with no range, and a reviewer asks for an interval estimate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An interval estimate gives a range that expresses uncertainty.
- [ ] B. A point estimate carries a measure of its own uncertainty.
- [ ] C. A point estimate is a single value reported as the best guess.
- [ ] D. Raising the confidence level from 90% to 99% widens the interval, other things equal.
- [ ] E. A wider interval at the same confidence level signals more uncertainty.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The range reflects sampling or model uncertainty.
- B: A bare point estimate is silent about uncertainty.
- C: It gives one number with no spread.
- D: A higher level needs a wider range to capture the parameter as often.
- E: Width is a direct reading of the uncertainty.

**Source:** Point estimate vs interval

## MA-jargon.10

A model says it is 90% confident on a set of cases and is right on 65% of them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A reliability diagram shows the gap between confidence and observed frequency.
- [ ] B. Overconfidence means stated confidence exceeds observed accuracy.
- [ ] C. Raising AUC repairs overconfidence.
- [ ] D. The model is underconfident.
- [ ] E. Expected calibration error is a ranking metric like AUC.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It plots observed accuracy against stated confidence in bins.
- B: The model claims more certainty than it earns.
- C: AUC measures discrimination and does not fix the calibration gap.
- D: Underconfidence is the opposite gap.
- E: It averages the confidence-accuracy gap and is a calibration measure.

**Source:** Overconfidence

## MA-jargon.11

A user asks a language model "how sure are you?" and it answers "95% confident." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Token probabilities are a different signal from verbalized confidence.
- [ ] B. A stated 95% is a calibrated probability by construction.
- [ ] C. Agreement across repeated samples is another way to estimate confidence.
- [ ] D. Verbalized confidence is a probability the model states in words.
- [ ] E. Verbalized confidence can be checked by comparing stated values with observed correctness.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Logprobs come from the output distribution, not from the text.
- B: Stated values need to be checked against outcomes.
- C: Self-consistency is a sampling-based confidence signal.
- D: It is the self-reported number in the text output.
- E: That comparison is a calibration check.

**Source:** Verbalized confidence

## MA-jargon.12

An analyst prompts: "Tell me how accurate and how confident the model's 70% scores are." Choose the rewrites that use exact terms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Report discrimination as AUC and calibration as expected calibration error, as separate quantities.
- [ ] B. Use the word accuracy for the share of predictions that are correct.
- [ ] C. Report AUC to show the scores are calibrated.
- [ ] D. Call the bootstrap interval for accuracy a posterior.
- [ ] E. Report calibration of the predicted probabilities with a reliability diagram.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The two properties are distinct and need distinct metrics.
- B: Accuracy is the proportion correct.
- C: AUC is discrimination, not calibration.
- D: A bootstrap interval is a confidence interval, not a posterior.
- E: That names the property of probability values the prompt is after.

**Source:** Rewrite a vague probability prompt
