# Chapter 2: Probability, uncertainty and the confidence illusion

## MA-ch02.1

A forecasting service publishes P(outage) = 0.70 and P(no outage) = 0.40 for the same day. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Coherence is judged on a set of probabilities taken together, not on one number alone.
- [ ] B. The figures violate normalization, because the probabilities of an event and its complement should sum to 1.
- [ ] C. The complement rule says P(no outage) should equal P(outage).
- [ ] D. A bettor treating the figures as fair prices could build a Dutch book, a set of bets that wins whichever outcome occurs.
- [ ] E. The figures are coherent, because each one lies between 0 and 1.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Probabilities are coherent when they satisfy the axioms jointly, such as normalization and additivity.
- B: Normalization and the complement rule require P(event) + P(not event) = 1, and here the sum is 1.10.
- C: The complement rule says P(not A) = 1 - P(A), which is different from equality.
- D: A Dutch book is a guaranteed-profit set of bets that exploits probabilities that are not coherent.
- E: Coherence is a property of the whole set of probabilities; each number being in range is not enough.

**Source:** Coherence, normalization and the Dutch book

## MA-ch02.2

An assistant is asked for P(rain or snow) given P(rain) and P(snow) for a day on which both can occur, and it simply adds the two numbers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The overlap term P(A and B) is called the marginal probability of A.
- [ ] B. Simple addition of the two probabilities is valid for mutually exclusive events.
- [ ] C. For events that can co-occur, P(A or B) = P(A) + P(B) - P(A and B), which is inclusion-exclusion.
- [ ] D. Rain and snow that can fall on the same day are mutually exclusive.
- [ ] E. Adding without subtracting the overlap double counts the outcomes where both events occur.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: P(A and B) is a joint probability; the marginal is P(A) on its own.
- B: Mutually exclusive events cannot co-occur, so there is no overlap to subtract.
- C: Inclusion-exclusion removes the overlap that addition counts twice.
- D: Mutually exclusive means the events cannot both happen; rain and snow here can.
- E: The overlap is included once in each term, so it appears twice in the sum.

**Source:** Addition rule and inclusion-exclusion

## MA-ch02.3

In a log of past cases, 70% carry an abnormal-lab flag, 40% are high-acuity, and 25% are both flagged and high-acuity. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 0.70 flag rate is a marginal probability.
- [ ] B. P(flag | high-acuity) is the same quantity as P(high-acuity | flag).
- [ ] C. P(high-acuity | flag) is found by dividing the marginal probability of the flag by the joint probability.
- [ ] D. The flag and high acuity are independent because the joint probability is smaller than each marginal.
- [ ] E. The 0.25 figure is a joint probability.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A marginal probability describes one variable without conditioning on another.
- B: Reversing the conditioning changes the denominator, so the two conditionals differ.
- C: A conditional probability divides the joint by the marginal of the conditioning event, not the other way round.
- D: Independence needs the joint to equal the product of the marginals, not merely to be smaller than each.
- E: A joint probability is the probability that both events occur together.

**Source:** Marginal, joint and conditional probability

## MA-ch02.4

For the same log, an analyst compares the joint probability 0.25 with the product of the two marginals, 0.70 x 0.40 = 0.28. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Independence means the joint probability equals the product of the marginal probabilities.
- [ ] B. Independent events and mutually exclusive events are the same thing.
- [ ] C. Since 0.25 differs from 0.28, the flag and high acuity are not independent.
- [ ] D. For independent events, conditioning on one leaves the probability of the other unchanged.
- [ ] E. A joint below each marginal shows the two events are mutually exclusive.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: That equality is the definition of independence for two events.
- B: Independent events can co-occur; mutually exclusive events cannot.
- C: A joint that does not match the product of the marginals signals dependence.
- D: If A and B are independent, P(A | B) = P(A).
- E: Mutually exclusive events have a joint of zero, which is a different condition.

**Source:** Independence

## MA-ch02.5

An agent completes three tool calls in sequence. An analyst estimates the chance that all three succeed by multiplying each call's success rate measured separately on fresh inputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The chain rule requires the steps to be independent.
- [ ] B. The chain rule multiplies P(first) by P(second | first) by P(third | first and second).
- [ ] C. If each step is more reliable after earlier steps succeed than on its own, the independence product overstates the chance that the whole task succeeds.
- [ ] D. Multiplying marginal success rates gives the joint probability when the calls are independent.
- [ ] E. The factors in the chain rule are the marginal probabilities of each step.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The chain rule is valid for dependent events; independence only lets the conditionals simplify.
- B: The chain rule builds a joint probability from conditionals on the earlier steps.
- C: That situation would make the independence product understate the joint probability.
- D: The product of marginals equals the joint exactly under independence.
- E: The factors are conditional probabilities given the earlier steps, not marginals.

**Source:** Chain rule and independence

## MA-ch02.6

A fraud-screening service routes each case to one of three model versions, each with its own error rate and share of traffic. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(version | error) comes from Bayes' theorem applied to the traffic shares and the version error rates.
- [ ] B. A version's share of the errors is its traffic share times its error rate, divided by the overall error rate.
- [ ] C. Changing the traffic mix changes the overall error rate even when no model changes.
- [ ] D. The overall error rate is the plain average of the three versions' error rates.
- [ ] E. The overall error rate is the sum over versions of traffic share times that version's error rate, by the law of total probability.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Bayes' theorem inverts P(error | version) into P(version | error) using the shares as priors.
- B: That is Bayes' theorem written with the law of total probability in the denominator.
- C: The overall rate is a weighted average, so its weights matter.
- D: The plain average ignores the weights; the correct combination weights each rate by its share.
- E: The law of total probability decomposes an overall probability into a weighted sum over cases.

**Source:** Law of total probability

## MA-ch02.7

A team updates its belief that a transaction is fraudulent after an alert fires. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The posterior is the probability of fraud before the alert is taken into account.
- [ ] B. The likelihood P(alert | fraud) is the same quantity as the posterior P(fraud | alert).
- [ ] C. The prior is the probability computed after the evidence has been included.
- [ ] D. The likelihood is P(alert | fraud).
- [ ] E. The prior is the probability of fraud before the alert is taken into account.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The posterior is the updated belief after the evidence; the quantity described is the prior.
- B: The two are conditionals in opposite directions and generally differ.
- C: That describes the posterior; a prior comes before the evidence.
- D: A likelihood is the probability of the observed evidence given a hypothesis.
- E: A prior is the belief held before seeing the evidence.

**Source:** Prior, likelihood and posterior

## MA-ch02.8

A vendor calls its fraud tool 98% accurate, meaning it flags 98% of fraudulent transactions and clears 98% of legitimate ones. Fraud is rare in the target market. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 98% of legitimate transactions cleared is the specificity.
- [ ] B. Precision depends on the prevalence of fraud as well as on sensitivity and specificity.
- [ ] C. The share of flagged transactions that are truly fraud is the precision, also called positive predictive value.
- [ ] D. The vendor's 98% figure is the precision of the tool.
- [ ] E. The 98% of fraudulent transactions flagged is the sensitivity, also called the true positive rate.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Specificity is P(clear | legitimate).
- B: A rarer condition gives more false flags relative to true flags, lowering precision.
- C: Precision is P(fraud | flag).
- D: The 98% describes behaviour given true status, so it is sensitivity and specificity, not precision.
- E: Sensitivity is P(flag | fraud).

**Source:** Sensitivity, specificity and precision

## MA-ch02.9

An analyst writes in a report: "The test is 99% accurate, so a positive result means a 99% probability of disease." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The quantity the sentence needs is the posterior P(disease | positive), which depends on the prevalence.
- [ ] B. Replacing the word accurate with the word calibrated fixes the sentence.
- [ ] C. A precise rewrite is: "The test has stated sensitivity and specificity; at this prevalence the positive predictive value is X."
- [ ] D. The sentence confuses sensitivity and specificity with positive predictive value.
- [ ] E. The figure 99% accurate names the posterior probability of disease.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The posterior combines the test's likelihood with the base rate through Bayes' theorem.
- B: Calibration is a different property, agreement of stated probabilities with frequencies, and does not repair the confusion.
- C: The rewrite uses the exact terms and states the base rate dependence.
- D: Accuracy-style figures condition on true status; the claim needs the probability of disease given a positive.
- E: It names behaviour given true status, which is a different conditional.

**Source:** Accuracy versus posterior probability

## MA-ch02.10

An expert testifies: "The chance an innocent person matches this DNA profile is 1 in 100,000, so the chance the defendant is innocent is 1 in 100,000." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The random-match probability and the probability of innocence given a match are equal when the same profile is involved.
- [ ] B. The quantity the court needs is P(innocent | match).
- [ ] C. Swapping P(A | B) for P(B | A) is called transposing the conditional, also known as the prosecutor's fallacy.
- [ ] D. The prior probability for the posterior calculation can come from the size of the pool of possible sources.
- [ ] E. The random-match probability is P(match | innocent).

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: They are different conditionals and are equal only by coincidence.
- B: The court conditions on the observed match and asks about innocence.
- C: The two conditionals are linked only through Bayes' theorem and the prior.
- D: A larger pool gives a smaller prior probability that any one person is the source.
- E: It conditions on innocence and asks about a match.

**Source:** Transposed conditional

## MA-ch02.11

A diagnostic test has a positive likelihood ratio computed from its sensitivity and specificity, and a user wants to update a prior to a posterior. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The positive likelihood ratio is sensitivity divided by (1 - specificity).
- [ ] B. Posterior odds equal prior odds times the likelihood ratio.
- [ ] C. Sensitivity divided by specificity is the positive likelihood ratio.
- [ ] D. Odds of 1 to 3 correspond to a probability of one third.
- [ ] E. Odds and probability are the same scale and take identical values.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It compares P(positive | condition) with P(positive | no condition).
- B: This is Bayes' theorem on the odds scale.
- C: The denominator is the false positive rate, 1 - specificity, not the specificity.
- D: Odds of 1 to 3 correspond to a probability of one in four.
- E: Odds are a ratio of chance to complement, so they differ from probability.

**Source:** Odds and likelihood ratio

## MA-ch02.12

A test is run twice on the same person and both results are positive. An analyst combines the two results. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Conditional independence means the two results are independent in the population without conditioning on true status.
- [ ] B. Reversing the order of two positive results changes the final posterior.
- [ ] C. If both positives come from the same specimen with the same interference, treating them as independent overstates the evidence.
- [ ] D. Multiplying likelihood ratios across the two results is valid when they are conditionally independent given true status.
- [ ] E. The posterior after the first positive result serves as the prior for the second update.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: The two results are usually dependent without conditioning because both depend on the true status.
- B: Odds updates multiply, and multiplication is commutative.
- C: Shared error sources break conditional independence, so the second result adds less.
- D: Conditional independence lets the likelihood of both results factor into a product.
- E: Sequential updating treats each posterior as the next prior.

**Source:** Sequential updating and conditional independence

## MA-ch02.13

A detector with fixed sensitivity and specificity is moved from a setting where 20% of cases are positive to one where 2% are positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A probability score calibrated at the old prevalence stays calibrated after the prior shift.
- [ ] B. Sensitivity and specificity stay the same under pure prior shift, since they condition on the true class.
- [ ] C. Precision of the flags falls, because precision depends on prevalence.
- [ ] D. The fall in precision shows the detector's discrimination between classes has worsened.
- [ ] E. A change in the prevalence of the target class, with class-conditional behaviour unchanged, is called prior shift (label shift).

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Calibration depends on the base rate, so the score is now too high.
- B: They are conditionals given class, so a change in class proportions does not move them.
- C: A lower base rate produces more false flags per true flag.
- D: Discrimination is unchanged by assumption; the base rate changed.
- E: Prior shift alters P(class) but leaves P(input | class) unchanged.

**Source:** Prior shift and precision

## MA-ch02.14

Four situations are described to a model-monitoring assistant, each to be named with the correct term for the type of shift. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The same inputs now lead to different outcomes because behaviour changed: concept drift.
- [ ] B. A change in the input distribution with the same input-outcome relationship is called concept drift.
- [ ] C. The share of fraud among transactions rises while each class looks the same as before: concept drift.
- [ ] D. Customers start sending longer messages than in the training data, while the rule linking message to outcome is unchanged: covariate shift.
- [ ] E. The share of positive cases falls while class-conditional inputs stay the same: covariate shift.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Concept drift is a change in the relationship between inputs and outcomes.
- B: That is covariate shift; concept drift changes the relationship.
- C: A change in class proportions alone is label (prior) shift.
- D: Covariate shift changes the distribution of inputs but not the input-outcome relationship.
- E: That pattern is label shift, a change in the prior, not in the input distribution.

**Source:** Covariate shift, concept drift and label shift

## MA-ch02.15

A classifier was found calibrated on data from an earlier year, and the user population has since changed in undocumented ways. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A calibration curve measured earlier remains valid after the population changes, provided the model weights are unchanged.
- [ ] B. Monitoring the distribution of inputs can flag covariate shift without waiting for labels.
- [ ] C. Unchanged overall accuracy implies unchanged calibration.
- [ ] D. Monitoring inputs alone is the most direct way to detect calibration decay.
- [ ] E. Concept drift can occur while the input distribution looks unchanged.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Calibration is a property of a model on a population, so it can go stale when the population shifts.
- B: Input drift is visible in features alone.
- C: Accuracy at a threshold ignores the size of the probability, so calibration can decay unseen.
- D: Calibration compares stated probabilities with realized outcomes, so it needs labels.
- E: The relationship between inputs and outcomes can change with the same inputs.

**Source:** Detecting shift and calibration decay

## MA-ch02.16

An evaluation team computes a 95% confidence interval for a model's accuracy on each of 100 independent test sets drawn from the same population. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 95% refers to the long-run coverage of the procedure over repeated samples.
- [ ] B. Using much larger test sets would raise the coverage of the intervals above 95%.
- [ ] C. Nominal coverage is guaranteed even when the independence assumption behind the interval fails.
- [ ] D. A single computed interval has a 95% probability of containing the true accuracy.
- [ ] E. A very narrow interval shows the test set is representative of the deployment population.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A confidence level describes how often the method captures the true value across repetitions.
- B: Larger samples narrow the intervals while coverage stays at the nominal level.
- C: Actual coverage can fall short of nominal when assumptions such as independence do not hold.
- D: For a fixed computed interval the true value is either inside or outside; the probability statement belongs to the procedure.
- E: Width reflects sampling noise, not bias or representativeness.

**Source:** Confidence interval and coverage

## MA-ch02.17

A team observes 19 correct answers out of 20 test items and computes both a confidence interval and a credible interval for the model's accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 95% confidence interval states a 95% probability that the parameter lies inside it, given the data.
- [ ] B. A credible interval depends on the prior, while a confidence interval has no prior.
- [ ] C. A confidence interval is a statement about the coverage of a procedure across repeated samples.
- [ ] D. A credible interval is a posterior probability statement about the parameter, given the model and the prior.
- [ ] E. A credible interval and a confidence interval are the same quantity and agree numerically in small samples.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: That reading belongs to a credible interval.
- B: The prior enters the posterior, so a different prior can change the credible interval.
- C: Its guarantee concerns the method, not one realised interval.
- D: A 95% credible interval holds 95% of the posterior probability.
- E: They answer different questions and can differ, especially with small samples or informative priors.

**Source:** Confidence interval versus credible interval

## MA-ch02.18

An engineer times 25 requests (mean 100 ms, standard deviation 15 ms) and writes: "The 95% interval is 93.8 to 106.2 ms, so there is a 95% chance the next request falls in that range." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The interval that answers the engineer's question about one new request is a prediction interval, and it is wider.
- [ ] B. The engineer's sentence is correct, because a confidence interval describes the spread of individual observations.
- [ ] C. The standard error of the mean shrinks as the sample grows, while the spread of individual requests does not.
- [ ] D. The standard error of the mean is the standard deviation of individual requests.
- [ ] E. The interval 93.8 to 106.2 ms is a confidence interval for the mean response time.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A prediction interval adds the variability of a single new observation to the uncertainty about the mean.
- B: A confidence interval describes the mean, not individual observations.
- C: Standard error is the standard deviation divided by the square root of n; the standard deviation itself is a property of the data.
- D: Standard error describes the sampling distribution of the mean, not the spread of individual values.
- E: It expresses uncertainty about the average, built from the standard error.

**Source:** Confidence interval, prediction interval and standard error

## MA-ch02.19

A test set of 400 items is in fact 40 distinct items, each reworded ten times, and an analyst computes an accuracy interval as if the 400 items were independent. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reworded copies of one item add independent information in the same way as new items.
- [ ] B. A confidence interval for accuracy accounts for sampling noise and for bias from an unrepresentative test set alike.
- [ ] C. Leakage of test items into training data is a non-sampling error that a confidence interval captures.
- [ ] D. An interval computed as if the 400 items were independent is too narrow.
- [ ] E. Near-duplicate items are correlated, so the effective sample size is smaller than the nominal sample size.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Rewordings of the same item are strongly dependent.
- B: An interval reflects sampling noise; a biased sample can still give a narrow interval around the wrong value.
- C: Leakage biases the estimate and the interval does not reflect it.
- D: Treating correlated items as independent understates the uncertainty.
- E: Correlated observations carry less independent information.

**Source:** Effective sample size and non-sampling error

## MA-ch02.20

Independent draws come from a heavy-tailed distribution, and an analyst reports a mean with a standard-error interval. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The standard error is the standard deviation of the sampling distribution of the mean.
- [ ] B. The standard error formula sigma / sqrt(n) does not apply when the variance is infinite.
- [ ] C. The central limit theorem for the sample mean needs finite variance, among other conditions.
- [ ] D. Strong positive correlation among observations makes sigma / sqrt(n) understate the variability of the mean.
- [ ] E. For heavy-tailed data the sample mean approaches a normal shape quickly.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: That is the definition of standard error.
- B: The formula presumes a finite standard deviation.
- C: Without finite variance the usual normal approximation does not hold.
- D: Correlated observations reduce the effective sample size.
- E: Rare large values can make convergence very slow or absent.

**Source:** Central limit theorem and heavy tails

## MA-ch02.21

A deployed model's mistakes cost 1 unit in most cases and a very large amount in rare cases. An audit sample contains no rare large mistake, and the report says the average cost has no variation and is therefore precise. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A zero-width interval from a sample with no variation reflects precise knowledge of the mean.
- [ ] B. The median is an adequate summary of the risk from rare large losses.
- [ ] C. Reporting the frequency and size of the largest losses, or high quantiles, alongside the mean is tail-aware reporting.
- [ ] D. A sample with no rare event shows that rare events are absent from the population.
- [ ] E. The mean, or expected value, weights rare large losses by their probability.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The zero width comes from the missing rare event, not from precise knowledge.
- B: The median ignores the tail, which can dominate the mean.
- C: Tail-aware reporting makes rare severe outcomes visible.
- D: Absence in a sample is not absence in the population; the zero-width interval is an artifact.
- E: Expected cost includes the tail through probability weighting.

**Source:** Tail risk and expected value

## MA-ch02.22

Model P gets 19 of 20 test items right and Model Q gets 940 of 1,000 right. Wilson intervals are computed for each. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An observed accuracy is a point estimate, and the interval expresses its sampling uncertainty.
- [ ] B. Overlapping intervals mean that the data do not establish that P is more accurate than Q.
- [ ] C. Halving an interval's width needs about double the number of items.
- [ ] D. Evaluating both models on the same items and analyzing the differences is a paired comparison.
- [ ] E. P's interval is wider than Q's because interval width scales roughly with one over the square root of n.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A point estimate is a single best guess with no stated uncertainty.
- B: A small gap in point estimates within sampling noise is not a demonstrated difference.
- C: Width scales with 1 / sqrt(n), so halving it needs about four times as many items.
- D: Pairing removes item-to-item variation from the comparison.
- E: Fewer items give a larger standard error.

**Source:** Interval width and paired comparison

## MA-ch02.23

A team compares two models by the difference in their accuracy and reports both a confidence interval for the difference and a p-value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The p-value is the probability of data at least as extreme as observed, assuming the null hypothesis.
- [ ] B. A posterior probability of a hypothesis requires a prior.
- [ ] C. A small p-value is the same thing as a large effect size.
- [ ] D. A 95% confidence interval for the difference that excludes zero corresponds to rejecting no difference in a two-sided test at the 5% level.
- [ ] E. The p-value is the probability that the null hypothesis is true given the data.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: That is the definition of a p-value.
- B: Bayes' theorem needs a prior to turn a likelihood into a posterior.
- C: A p-value reflects evidence against the null and depends on sample size, so it is not an effect size.
- D: Two-sided tests and confidence intervals are dual.
- E: A p-value conditions on the null; the probability of a hypothesis given the data is a posterior.

**Source:** p-value versus posterior probability

## MA-ch02.24

A reviewer says that accuracy, discrimination and calibration are three ways to say that a probabilistic classifier is good. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model that predicts the base rate for each case is calibrated in aggregate but has no discrimination.
- [ ] B. Calibration and discrimination are two names for the same property.
- [ ] C. Accuracy at a threshold ignores the size of the predicted probability.
- [ ] D. Calibration is agreement between stated probabilities and observed frequencies.
- [ ] E. Discrimination is the ability to rank positives above negatives, as summarized by AUC.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A constant forecast matches overall frequency and ranks nothing, so AUC is 0.5.
- B: A model can be calibrated without ranking cases or can rank perfectly with miscalibrated scores.
- C: Only the side of the threshold matters, not how far from it a probability lies.
- D: Among cases given probability p, about a fraction p should be positive.
- E: A discriminating model gives higher scores to positives than to negatives.

**Source:** Accuracy, discrimination and calibration

## MA-ch02.25

At 10% prevalence, model M1 outputs 0.10 for every patient, while model M2 ranks patients perfectly but outputs scores between 0.60 and 1.00. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For deciding which patients to examine first, calibration is the relevant property and discrimination is not.
- [ ] B. A strictly increasing recalibration map leaves M2's AUC unchanged.
- [ ] C. M1 has no discrimination, since its scores give no way to rank patients.
- [ ] D. M2 has excellent discrimination and poor calibration.
- [ ] E. M2's high AUC means its scores can be read as probabilities of disease.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Prioritizing needs a ranking, which is discrimination.
- B: Such a map preserves the order of scores.
- C: A constant score gives AUC 0.5.
- D: Perfect ranking is compatible with scores far above the actual frequency.
- E: AUC measures ranking, not agreement of scores with frequencies.

**Source:** Calibration without discrimination and the reverse

## MA-ch02.26

A data scientist reports an AUC for a classifier and describes how it is defined. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. AUC is the probability that a randomly chosen positive case scores higher than a randomly chosen negative case, with ties counted as half.
- [ ] B. Applying a strictly increasing transformation to the scores leaves the AUC unchanged.
- [ ] C. The expected AUC does not depend on the class proportions in the sample.
- [ ] D. AUC measures calibration of the predicted probabilities.
- [ ] E. An AUC of 0.875 means 87.5% accuracy at a 0.5 cutoff.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That is the ranking interpretation of AUC.
- B: AUC depends only on the order of scores.
- C: It compares the positive and negative score distributions.
- D: AUC measures discrimination, not calibration.
- E: AUC is a ranking measure and accuracy at a cutoff is a separate quantity.

**Source:** AUC

## MA-ch02.27

Two forecasters each assign a fixed probability to 10 events, 8 of which occur. Forecaster P says 0.8 for each event and forecaster Q says 0.99 for each event. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Brier score is the mean squared difference between the forecast probability and the outcome.
- [ ] B. The Brier score is an error rate at a cutoff.
- [ ] C. Forecaster Q is better, because it states higher confidence.
- [ ] D. Log loss caps the penalty for a confident miss at 1.
- [ ] E. The two forecasters have the same accuracy at a 0.5 cutoff.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It is a mean squared probability error.
- B: It averages squared probability error and does not use a cutoff.
- C: Q is overconfident; proper scores favour P, whose probabilities match the frequency.
- D: Log loss is unbounded as the probability given to the true outcome approaches 0.
- E: Both are on the correct side of 0.5 for the same events.

**Source:** Brier score, log loss and accuracy compared

## MA-ch02.28

A statistician discusses scoring rules that reward honest probability reports. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy at a cutoff is strictly proper.
- [ ] B. Brier score and log loss are strictly proper.
- [ ] C. A proper scoring rule has its expected score optimized by reporting one's true belief.
- [ ] D. Absolute error is proper because it penalizes the distance from the outcome.
- [ ] E. A strictly proper rule is one in which many different reports earn the same expected score.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Any report on the correct side of the cutoff earns the same expected score.
- B: Each is uniquely optimized by reporting the true probability.
- C: That is the definition of properness.
- D: Its expected value is minimized by reporting 0 or 1, so it rewards exaggeration.
- E: Strict properness means the true belief is the unique optimum.

**Source:** Proper and strictly proper scoring rules

## MA-ch02.29

A model's Brier score is compared with that of a reference forecaster who predicts the base rate for every case. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The reference forecaster has a Brier score of 0 because it is calibrated.
- [ ] B. Brier scores from test sets with different base rates are directly comparable without a reference.
- [ ] C. The reference forecast is calibrated in aggregate and has no discrimination.
- [ ] D. A forecast of the base rate for each case is a climatological reference.
- [ ] E. A Brier skill score measures improvement relative to a reference forecast.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Calibration without discrimination still leaves a positive Brier score.
- B: The score of a trivial forecast depends on the base rate.
- C: A constant base-rate forecast matches overall frequency but ranks nothing.
- D: Such a constant forecast is the standard no-skill baseline.
- E: It is 1 minus the ratio of the model's score to the reference score.

**Source:** Brier skill score and reference forecast

## MA-ch02.30

A classifier's probabilities are scored with log loss, defined as the mean negative natural logarithm of the probability given to the true class. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Log loss is unbounded above, while the Brier score for a binary outcome is bounded by 1.
- [ ] B. Log loss is computed from the labels alone and ignores the predicted probabilities.
- [ ] C. A confident miss costs more under the Brier score than under log loss.
- [ ] D. A forecast of exactly 0 for a case that turns out positive gives a large but finite penalty.
- [ ] E. Log loss averages the squared difference between forecast and outcome.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: The log penalty grows without limit as the probability given to the true class nears 0.
- B: It is computed from the probability assigned to the true class.
- C: Log loss punishes a confident miss more heavily because it has no upper bound.
- D: The negative log of zero is infinite, which is why implementations clip probabilities.
- E: That describes the Brier score.

**Source:** Log loss

## MA-ch02.31

A reliability diagram shows four bins as pairs (mean predicted probability, observed fraction of positives): (0.15, 0.22), (0.45, 0.47), (0.75, 0.62), (0.95, 0.80). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A reliability diagram plots observed frequency against mean predicted probability by bin.
- [ ] B. A point above the diagonal at low predicted probability shows the model understates risk in that bin.
- [ ] C. A curve that rises with predicted probability establishes that the model is calibrated.
- [ ] D. Points below the diagonal at high predicted probability indicate overconfidence.
- [ ] E. Small bins give noisy observed frequencies, so bin counts or intervals belong alongside the points.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A calibrated model lies near the diagonal.
- B: Events occur more often than predicted.
- C: A rising curve shows sensible ranking; calibration needs points near the diagonal.
- D: Stated probabilities exceed observed frequencies there.
- E: Sampling noise grows as the number of cases per bin falls.

**Source:** Reliability diagram and overconfidence

## MA-ch02.32

An evaluation reports a single expected calibration error (ECE) for a classifier, with predictions grouped into bins. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. ECE is the misclassification rate at a 0.5 cutoff.
- [ ] B. ECE is the count-weighted mean absolute gap between mean predicted probability and observed frequency across bins.
- [ ] C. A perfectly calibrated model has a measured ECE of zero on a finite test set.
- [ ] D. Maximum calibration error is the count-weighted average of the bin gaps.
- [ ] E. ECE does not depend on the number and placement of bins.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: ECE measures probability gaps, not classification errors.
- B: Weighting by bin count makes ECE an average over cases.
- C: Sampling noise gives a positive expected ECE even for a perfectly calibrated model.
- D: Maximum calibration error is the largest gap among the bins, not a weighted average.
- E: Different binning schemes give different ECE values.

**Source:** Expected and maximum calibration error

## MA-ch02.33

A classifier reports confidence 0.90 for every held-out case. Group X is 80% correct and group Y is 100% correct, in equal numbers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Pooled calibration implies each group is calibrated.
- [ ] B. A pooled calibration check suffices to show each group is calibrated.
- [ ] C. A single global rescaling fitted on the pooled data would find nothing to correct.
- [ ] D. Overconfidence means stated confidence is below observed accuracy.
- [ ] E. Pooled calibration at 0.90 coexists with overconfidence for group X and underconfidence for group Y.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The pooled average can be correct while each group is miscalibrated.
- B: Calibration should be checked within subgroups because offsetting errors hide in the aggregate.
- C: The pooled point already lies on the diagonal.
- D: Overconfidence is stated confidence above observed accuracy.
- E: Opposite gaps average out in the pool.

**Source:** Subgroup calibration

## MA-ch02.34

A team applies temperature scaling to a classifier that outputs sigma(z) from a logit z. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Temperature scaling changes the ordering of cases, so the AUC changes.
- [ ] B. Temperature scaling is a regularizer applied during training.
- [ ] C. Temperature scaling repairs a classifier whose ranking is poor.
- [ ] D. Temperature scaling divides the logit by a single parameter T fitted on held-out data.
- [ ] E. A T greater than 1 softens the probabilities toward 0.5.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Dividing by a positive T preserves order and AUC.
- B: It is fitted after training on held-out data, as a recalibration step.
- C: It rescales confidence without changing the ranking.
- D: It is a one-parameter post-hoc recalibration.
- E: Dividing the logit by a larger number moves the sigmoid output toward one half.

**Source:** Temperature scaling and recalibration

## MA-ch02.35

A language model answers factual questions and appends "Confidence: 95%" to each answer, and a team wants to treat the number as a probability of being correct. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Higher stated confidence tracking higher accuracy is discrimination, even when the stated levels are too high.
- [ ] B. Stated confidence is calibrated if, among answers stated at 95%, about 95% are correct.
- [ ] C. A precise stated figure shows the model computed that probability internally.
- [ ] D. Verbalized confidence is a number written in the model's text and is not necessarily an internally computed probability.
- [ ] E. Verbalized confidences are too unreliable to be recalibrated with labeled data.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Ranking information can remain when the levels are off.
- B: Calibration compares stated values with observed frequency.
- C: Precision of display is not evidence of how the number was produced.
- D: Fluent stated figures need not reflect a calculated probability.
- E: A recalibration map can be fitted on held-out labeled answers.

**Source:** Verbalized confidence

## MA-ch02.36

A clinic can follow up a flagged patient at a small cost, while a missed positive case is much more costly, and the model gives calibrated probabilities. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 0.5 cutoff minimizes expected cost because it minimizes the number of errors.
- [ ] B. A cost-derived threshold stays valid when the probabilities are miscalibrated.
- [ ] C. If the cost of a missed case falls, the cost-minimizing threshold rises.
- [ ] D. A threshold chosen from costs treats a false negative and a false positive as equally costly.
- [ ] E. With calibrated probabilities the cost-minimizing decision threshold comes from the costs of the two error types, not from 0.5.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Minimizing error count treats both mistakes as equally costly.
- B: The threshold assumes stated probabilities equal true frequencies.
- C: A smaller miss cost justifies following up only more probable cases.
- D: It is chosen precisely because the two errors have different costs.
- E: Following up pays when the probability of a positive times the miss cost exceeds the follow-up cost.

**Source:** Decision threshold and expected cost

## MA-ch02.37

A team checks whether the confidence scores of a deployed classifier can be read as probabilities and plans a fitting and evaluation procedure. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A calibration check done once stays valid as the population changes.
- [ ] B. A held-out set is data that were used to fit the model.
- [ ] C. Calibration is a property of a model on a population, so it is measured on data resembling the deployment population.
- [ ] D. A recalibration map judged on the same data used to fit it gives an honest estimate of calibration.
- [ ] E. The Brier score depends on the choice of bins.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Calibration can drift, so it is rechecked over time.
- B: A held-out set is data kept out of fitting.
- C: Scores calibrated on one population can be miscalibrated on another.
- D: A held-out set is needed because the fit data flatter the map.
- E: The Brier score is computed per case and does not use bins.

**Source:** Held-out data and evaluating calibration

## MA-ch02.38

A loan dashboard shows each decision with a score such as "87.3% likely to repay". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The number of displayed decimal places is a formatting choice and is not evidence of accuracy.
- [ ] B. The meaning of a score as a probability comes from the model's architecture rather than from observed outcomes.
- [ ] C. A high AUC ensures that an 87.3% score corresponds to an 87.3% repayment rate.
- [ ] D. False precision is reporting more digits than the underlying uncertainty supports.
- [ ] E. Labeling an output as a probability makes it a calibrated probability.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Digits shown say nothing about validity.
- B: A score means a probability when observed frequencies among similar scores match it, that is, when it is calibrated.
- C: AUC measures ranking and does not ensure calibration.
- D: Sampling and model error exceed the last displayed digit.
- E: The label is not evidence of agreement with frequencies.

**Source:** False precision and the meaning of a probability

## MA-ch02.39

An analyst writes: "The false positive rate is 5%, so 95% of the alerts are real." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The false positive rate and the false discovery rate are the same quantity.
- [ ] B. The false positive rate is P(flag | negative).
- [ ] C. Specificity equals 1 minus the false positive rate.
- [ ] D. Ignoring the prevalence when reading a positive result is called base rate neglect.
- [ ] E. The false discovery rate is the share of flags that are false, which is 1 minus precision.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: One conditions on true status and the other on the flag.
- B: It conditions on the true class being negative.
- C: Specificity is the true negative rate.
- D: The share of real alerts depends on how common the condition is.
- E: It is P(negative | flag).

**Source:** Base rate neglect, false positive rate and false discovery rate

## MA-ch02.40

A user asks an AI assistant: "Make the classifier's probabilities more accurate." The assistant asks which exact term the user means. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Reduce the Brier score" blends calibration and discrimination in one request.
- [ ] B. "Recalibrate the predicted probabilities on held-out labeled data" names a request about calibration.
- [ ] C. "Improve discrimination" asks for better ranking, which is a different goal from calibration.
- [ ] D. "Increase the confidence" is a precise request for calibration.
- [ ] E. The word accuracy is the correct term for matching probabilities to observed frequencies.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The Brier score reflects both the calibration and the ranking quality of probabilities.
- B: Calibration is agreement between stated probabilities and observed frequencies.
- C: Discrimination is measured by a ranking statistic such as AUC.
- D: Raising stated confidence can worsen calibration.
- E: Accuracy at a threshold is the fraction correct; matching frequencies is calibration.

**Source:** Choosing the exact term in a prompt

## MA-ch02.41

A user asks an AI assistant for "the error bar" on latency, and the assistant asks which interval is meant. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For the average latency, ask for a confidence interval for the mean.
- [ ] B. For one future request, ask for a prediction interval.
- [ ] C. The standard error describes the spread of individual latencies.
- [ ] D. A credible interval needs a stated prior and model.
- [ ] E. A credible interval is a request for a frequentist coverage guarantee.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It expresses uncertainty about the population mean.
- B: It covers the variability of a single new observation.
- C: Standard error describes the spread of the sample mean.
- D: The posterior depends on both.
- E: A credible interval is a posterior probability statement given a prior.

**Source:** Choosing the exact interval

## MA-ch02.42

An agent ends each task by reporting "complete". It does so on 98% of the tasks that succeed and on 60% of the tasks that fail. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The posterior probability of success after the report equals 98%.
- [ ] B. The likelihood ratio of about 1.6 makes the report weak evidence of success.
- [ ] C. The 98% is the sensitivity of the report and the 60% is its false positive rate.
- [ ] D. A report written on both successful and failed tasks is highly discriminating.
- [ ] E. The probability that a task succeeded, given the report, depends on the base rate of success.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: 98% is P(report | success), a different conditional from P(success | report).
- B: A ratio near 1 moves belief only slightly.
- C: They are P(report | success) and P(report | failure).
- D: A report given at similar rates for both outcomes separates them poorly.
- E: The posterior combines the likelihood ratio with the prior.

**Source:** Likelihood ratio and base rate for an agent's report
