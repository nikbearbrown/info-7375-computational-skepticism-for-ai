# Foundations (probability and statistics for skeptics)

Vocabulary questions on the terms used to check a claim about an AI system: probability, distributions, sampling and inference, data quality and missing data, and the basics of fitting and evaluating a model. Each section keeps its own heading below.

# 1. Probability, conditional probability and Bayes' theorem

## MA-1.1

A fraud team says its transaction classifier "catches 90% of fraud" and "wrongly flags 4% of legitimate transactions". Which statements name these quantities correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For a fixed sensitivity and false positive rate, the prevalence (base rate) of fraud leaves the positive predictive value unchanged.
- [ ] B. "Catches 90% of fraud" is the sensitivity of the classifier, also called recall or the true positive rate.
- [ ] C. Sensitivity and positive predictive value are two names for one quantity.
- [ ] D. "Wrongly flags 4% of legitimate transactions" is the false positive rate, which equals 1 minus the specificity.
- [ ] E. The probability that a flagged transaction is fraudulent is the sensitivity.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: The positive predictive value rises with prevalence even when the two error rates stay fixed.
- B: Sensitivity is the share of actual positives that the classifier flags.
- C: They condition on different events: sensitivity on actual positives, positive predictive value on flagged cases.
- D: The false positive rate is the share of actual negatives flagged, the complement of specificity.
- E: That probability is the positive predictive value (precision); sensitivity conditions on fraud, not on the flag.

**Source:** Sensitivity, false positive rate, positive predictive value, prevalence

## MA-1.2

A help desk logs tickets by type (billing or technical) and by whether each was escalated. Which statements use the probability terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(escalated) over the full log is a marginal probability, a weighted average of the group-level conditional probabilities.
- [ ] B. Ticket type and escalation are independent when P(escalated | billing) differs from P(escalated | technical).
- [ ] C. P(billing and escalated) is a joint probability: the share of the full log that is both billing and escalated.
- [ ] D. P(billing | escalated) is the same quantity as P(escalated | billing) with the words reordered.
- [ ] E. P(escalated | billing) is a conditional probability: the chance of escalation within the billing tickets.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A marginal probability ignores the grouping and equals the sum of each group share times its conditional probability.
- B: Independence needs the conditional probability to equal the marginal for each group; differing rates signal dependence.
- C: A joint probability is the chance that two events happen together.
- D: Swapping the conditioning event gives a different conditional probability with a different value.
- E: A conditional probability restricts attention to the cases where the given event holds.

**Source:** Conditional, joint and marginal probability

## MA-1.3

Two automated checkers each miss a given defect with probability 0.10, and a reviewer asks whether the two misses are independent events. Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Independence means the two events do not occur together.
- [ ] B. If P(second misses | first misses) equals 1, the two misses are independent events.
- [ ] C. Two events are independent when the joint probability equals the product of the two marginal probabilities.
- [ ] D. Two checkers built with the same method that tend to miss the same defects have independent misses.
- [ ] E. Mutually exclusive events that each have positive probability are independent.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Events that do not occur together are mutually exclusive, which is a different property from independence.
- B: Independence needs the conditional probability to equal the marginal 0.10; a value of 1 is extreme dependence.
- C: The product rule for joint probability is the definition of independence.
- D: Shared blind spots make the misses positively dependent, not independent.
- E: If one occurs the other has probability 0, so knowing one changes the other; they are dependent.

**Source:** Independence and dependence of events

## MA-1.4

A statistician explains the shared-birthday result for a group of people, assuming 365 equally likely birthdays that are independent. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The event "some pair in the group shares a birthday" has the same probability as the event "one named person shares a birthday with someone else in the group".
- [ ] B. The growth of a match chance in a small group is explained by counting pairs of people instead of counting people.
- [ ] C. The complement rule computes P(at least two share a birthday) as 1 minus P(no two share a birthday).
- [ ] D. Birthdays clustered on certain dates make a match less likely than under the uniform model.
- [ ] E. "At least two share a birthday" and "exactly two share a birthday" name the same event.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The named-person event is far less likely; the pair event has many more chances to occur.
- B: The number of pairs grows roughly with the square of the group size.
- C: The complement of "at least one match" is "no match", which is easier to count.
- D: Non-uniform frequencies make a match more likely; the uniform case is the least likely to produce one.
- E: "At least two" includes larger shared groups; "exactly two" excludes them.

**Source:** Complement rule, pairs, and "at least one" events

## MA-1.5

A mail filter knows that 30% of messages are spam, that the word "urgent" appears in 60% of spam and in 10% of legitimate messages, and it wants the chance that a message containing "urgent" is spam. Which statements name the pieces correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P("urgent" | spam) = 0.60 is a likelihood and is a different quantity from the posterior probability of spam.
- [ ] B. P(spam | "urgent") is the posterior probability.
- [ ] C. The likelihood ratio is the posterior probability divided by the prior probability.
- [ ] D. Posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] E. The 30% share of spam before looking at the word is the prior probability.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A likelihood is the probability of the evidence given a hypothesis; the posterior is the probability of the hypothesis given the evidence.
- B: The posterior is the updated probability of the hypothesis after the evidence.
- C: The likelihood ratio compares the probability of the evidence under two hypotheses, here 0.60 divided by 0.10.
- D: This is the odds form of Bayes' rule.
- E: The prior is the probability assigned before the evidence is considered.

**Source:** Prior, likelihood, posterior, likelihood ratio, odds

## MA-1.6

A school buys a detector that labels essays "AI-written" and states it is "98% accurate", meaning it flags 98% of AI-written essays and wrongly flags 2% of human-written essays. A teacher asks how likely a flagged essay is to be AI-written. Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. When AI-written essays are rare, the positive predictive value of a flag is higher than when they are common.
- [ ] B. The vendor's "accuracy" claim reports the false discovery rate of the detector.
- [ ] C. Treating P(flagged | AI-written) as if it were P(AI-written | flagged) is an application of the law of total probability.
- [ ] D. The vendor's 98% is a sensitivity, P(flagged | AI-written), and it does not answer the teacher's question.
- [ ] E. The teacher's question asks for the positive predictive value of a flag.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A lower base rate lowers the positive predictive value because false flags from the large legitimate group dominate.
- B: The claim reports error rates conditional on the true class, not the share of flags that are wrong.
- C: That error is called transposing the conditional; it ignores the base rate and is also called the base rate fallacy.
- D: The teacher needs the reverse conditional, P(AI-written | flagged).
- E: Positive predictive value is the probability that a flagged case is truly positive.

**Source:** Transposed conditional, base rate fallacy, positive predictive value

## MA-1.7

A face-matching system searches a database of 2,000,000 people. It declares a match for a person who is not the source with probability 1 in 10,000. A prosecutor says: "The chance this match is a coincidence is 1 in 10,000, so there is a 99.99% chance he is the source." Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The 1 in 10,000 rate is the false positive rate, so it is also the false discovery proportion among declared matches.
- [ ] B. Independent evidence about the person raises the prior odds, and posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] C. A match found by testing one suspect already singled out by other evidence carries the same weight as a match found by trawling a large database.
- [ ] D. Searching a large database raises the expected number of coincidental matches.
- [ ] E. The prosecutor transposed the conditional: P(match | not the source) is not P(not the source | match).

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The false discovery proportion is the share of matches that are wrong, which also depends on how many non-sources are tested.
- B: Independent evidence changes the prior odds before the match is weighed.
- C: Trawling produces many coincidental matches, so a match from a trawl carries a lower posterior probability.
- D: The count of false matches grows with the number of non-source people tested.
- E: The 1 in 10,000 is a false positive rate; the prosecutor read it as the reverse conditional.

**Source:** Prosecutor's fallacy, false positive rate versus false discovery proportion

## MA-1.8

Model A beats Model B on easy questions and also on hard questions, yet Model B has the higher overall accuracy because Model B was tested mostly on easy questions. Which statements name this correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The difference in question mix between the two models is a confounder of the overall comparison.
- [ ] B. Overall accuracy is a conditional accuracy given question difficulty.
- [ ] C. A trend that holds in each group and reverses in the combined data is Simpson's paradox.
- [ ] D. Stratifying by question difficulty is a sound fix when difficulty is a property of the question and not an effect of the model.
- [ ] E. Overall accuracy is a weighted average of the group accuracies, with weights set by each model's own mix of questions.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The mix of easy and hard questions is linked to both which model is scored and the accuracy obtained.
- B: Overall accuracy ignores difficulty; accuracy within a difficulty level is the conditional quantity.
- C: Simpson's paradox is a reversal between group-level and aggregate comparisons.
- D: Stratification compares like with like on a variable that is not downstream of the treatment.
- E: Different weights can reverse the order of the averages.

**Source:** Simpson's paradox, confounder, stratification

# 2. Random variables and distributions

## MA-2.1

An agent retries a failing tool call before giving up. Let X be the number of retries in one run, with P(X=0) = 0.50, P(X=1) = 0.30, P(X=2) = 0.15 and P(X=3) = 0.05. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The mode of X is its most probable value, and it can differ from the expected value.
- [ ] B. The expected value of X is the probability-weighted mean of its possible values.
- [ ] C. Adding a constant to a random variable changes its variance.
- [ ] D. Variance is measured in squared units of X, while standard deviation is measured in the units of X.
- [ ] E. The expected value of a discrete random variable is itself one of its possible values.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Here the mode is 0 while the mean is 0.75.
- B: Expected value is the long-run average, the sum of each value times its probability.
- C: A shift moves the distribution but leaves its spread, and so its variance, unchanged.
- D: The standard deviation is the square root of the variance.
- E: The mean of 0.75 is not a possible number of retries.

**Source:** Expected value, mode, variance, standard deviation

## MA-2.2

X is a continuous random variable, uniformly distributed on the interval from 0 to 0.5. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The cumulative distribution function can decrease as x increases.
- [ ] B. The area under the density curve between two points is the expected value of X.
- [ ] C. A probability mass function is the right description for a continuous variable.
- [ ] D. For a continuous variable the probability of one exact value is 0.
- [ ] E. A probability density function value is not a probability and can exceed 1.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The cumulative distribution function P(X ≤ x) is non-decreasing.
- B: That area is the probability that X falls between the two points.
- C: A probability mass function belongs to discrete variables; continuous variables use a density.
- D: Probability comes from the area under the density over an interval, and a single point has no width.
- E: Density is probability per unit length; for this uniform variable it is 2.

**Source:** Probability density function, cumulative distribution function, probability mass function

## MA-2.3

A model answers each of 20 test prompts correctly with probability 0.8, independently, and the number correct is modeled as binomial. Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The binomial variance is np, which equals its mean.
- [ ] B. Overdispersion means the observed variance is smaller than the model variance.
- [ ] C. Positively correlated trials, such as near-duplicate prompts, cause overdispersion: the count varies more than the binomial variance says.
- [ ] D. A binomial count is the number of successes in a fixed number of independent trials that share one success probability.
- [ ] E. Overdispersion and underdispersion both describe the sample mean differing from the population mean.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: The binomial variance is np(1 − p); equal mean and variance is a property of the Poisson.
- B: That is underdispersion; overdispersion is larger observed variance.
- C: Overdispersion means observed variance exceeds the model variance.
- D: These are the defining conditions of the binomial model.
- E: They describe variance relative to the model, not a difference in means.

**Source:** Binomial distribution, independence, overdispersion

## MA-2.4

Request latency for a service is modeled as a normal distribution with mean 200 ms and standard deviation 40 ms. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A z-score counts how many standard deviations a value lies from the mean.
- [ ] B. A fat-tailed (heavy-tailed) distribution tends to put more probability far from the mean than a normal with the same mean and standard deviation.
- [ ] C. Two distributions with the same mean and standard deviation have the same tail probabilities.
- [ ] D. About 68% of a normal distribution lies within two standard deviations of the mean.
- [ ] E. The 68-95-99.7 rule holds for skewed distributions as well as for normal ones.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A 280 ms request has z = (280 − 200) / 40 = 2.
- B: Heavy tails make extreme values more common than the normal curve predicts.
- C: Tail mass depends on the whole shape, not just the first two moments.
- D: About 68% lies within one standard deviation; about 95% lies within two.
- E: The empirical rule is a property of the normal distribution.

**Source:** Normal distribution, z-score, empirical rule, fat tails

## MA-2.5

A team sets an alert at the mean plus a multiple of the standard deviation, and a reviewer questions the quoted false-alarm rate. Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Chebyshev's inequality bounds tail probability for distributions with finite variance, whatever their shape.
- [ ] B. At 3 standard deviations the Chebyshev bound is 1/9, which is looser than the normal tail figure.
- [ ] C. A quantile-quantile plot compares the data's quantiles with a reference distribution and can show whether the tails are heavier than normal.
- [ ] D. The Cauchy distribution has a finite mean, so sample averages settle down as the sample grows.
- [ ] E. A "six-sigma" failure rate computed from the normal curve stays valid when the real distribution is heavy-tailed.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The bound P(|X − μ| ≥ kσ) ≤ 1/k² needs only a finite variance.
- B: The normal puts about 0.27% beyond 3 standard deviations, far under 11%.
- C: Points bending away from the line in the ends signal tail shape that differs from the reference.
- D: The Cauchy has no finite mean, and the average of Cauchy observations is as spread out as one observation.
- E: The tiny figure depends on the normal shape; heavy tails put far more probability at extreme distances.

**Source:** Chebyshev's inequality, tail risk, quantile-quantile plot, Cauchy

## MA-2.6

An agent run makes 500 tool calls. Each call fails with probability 0.002, independently, and one failed call ruins the run. A manager calls 99.8% per-call reliability "basically perfect". Which statements are correct? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A Poisson distribution with mean n × p approximates this binomial when n is large and p is small.
- [ ] B. Small per-step failure probabilities compound across steps and lower end-to-end success.
- [ ] C. The number of failed calls per run is binomial with 500 trials and a per-trial failure probability of 0.002.
- [ ] D. Failures that share a cause, such as a down service, are positively correlated, so the independence-based figure for run success should be checked against observed runs.
- [ ] E. Per-call reliability and per-run (end-to-end) reliability are the same quantity.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The Poisson approximation to the binomial is the rare-event limit.
- B: The chance of no failure is (1 − p) raised to the number of steps.
- C: Fixed number of independent trials with equal failure probability gives a binomial count.
- D: Correlated failures violate the independence assumption behind the product rule.
- E: Per-run reliability is a product over steps and is much lower than the per-call figure.

**Source:** Binomial, Poisson approximation, compounding, end-to-end reliability

# 3. Sampling, the central limit theorem and inference

## MA-3.1

An engineer runs 400 independent evaluation prompts and 320 pass, an observed pass rate of 0.80. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The standard error and the standard deviation of the individual pass-or-fail outcomes are the same quantity.
- [ ] B. The standard error of a proportion is largest when p is near 0 or 1.
- [ ] C. Doubling the number of prompts halves the standard error.
- [ ] D. The standard error of the pass rate measures how much the sample proportion varies from one sample to another.
- [ ] E. The margin of error of a 95% interval is the critical value (about 1.96) times the standard error.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: The standard deviation describes single outcomes; the standard error describes the estimate and shrinks as n grows.
- B: The quantity p(1 − p) peaks at p = 0.5, so the standard error is largest there.
- C: The standard error falls in proportion to 1 over the square root of n, so doubling n shrinks it by about 29%.
- D: A standard error is the standard deviation of a statistic across repeated samples.
- E: Margin of error = critical value × standard error.

**Source:** Standard error, margin of error, confidence interval

## MA-3.2

An A/B test with 20,000 users per arm gives a two-sided p-value of 0.048 for a 0.6 percentage point lift in conversion. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A p-value is the probability of data at least as extreme as observed, computed assuming the null hypothesis is true.
- [ ] B. One minus the p-value, 0.952, is the probability that the feature truly raises conversion.
- [ ] C. A p-value of 0.048 is the probability that the null hypothesis is true.
- [ ] D. A small p-value shows that the effect size is large.
- [ ] E. Statistical significance and practical significance are different judgments.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It is a probability about data under the null, not about the hypothesis.
- B: That would be a posterior probability, which needs a prior and a different calculation.
- C: The p-value assumes the null; it does not give the probability that the null is true.
- D: With large samples a small effect can still give a small p-value; effect size is a separate quantity.
- E: A result can be statistically significant yet too small to matter in practice.

**Source:** p-value, effect size, statistical versus practical significance

## MA-3.3

A group screens 200 independent hypotheses, 20 of them true effects, using significance level 0.05 and power 0.80. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The false discovery rate among significant results depends on the base rate of true effects, so alpha alone does not set it.
- [ ] B. Power is 1 minus the Type II error rate, the probability of detecting an effect that is real.
- [ ] C. A significance level of 0.05 means that 95% of significant findings are real effects.
- [ ] D. The significance level is the Type I error rate: the probability of rejecting a null hypothesis that is true.
- [ ] E. A Type II error is a false positive.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Where true effects are rare, false positives from many true nulls make up a large share of discoveries.
- B: Type II error is a miss, and power is its complement.
- C: The share of significant findings that are real depends on the base rate of true effects, not on alpha alone.
- D: Type I error is a false positive among true nulls.
- E: A Type II error is a false negative; a false positive is a Type I error.

**Source:** Type I error, Type II error, power, false discovery rate, base rate

## MA-3.4

A team tests 20 prompt variants against a baseline, each at significance level 0.05, and none truly differs. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The family-wise error rate is the expected share of false findings among the discoveries.
- [ ] B. The false discovery rate is the expected proportion of false findings among the results declared significant.
- [ ] C. Testing 20 variants and reporting the best raw p-value is a multiple comparisons (multiplicity) problem.
- [ ] D. The Benjamini–Hochberg procedure controls the family-wise error rate.
- [ ] E. The Bonferroni correction divides the significance level by the number of tests.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That describes the false discovery rate; the family-wise error rate is the probability of at least one false positive.
- B: It is a weaker guarantee than controlling the family-wise error rate.
- C: The chance of at least one false positive grows with the number of tests.
- D: Benjamini–Hochberg controls the false discovery rate; Bonferroni and Holm control the family-wise error rate.
- E: With 20 tests the per-test threshold becomes 0.05 / 20 = 0.0025.

**Source:** Multiple comparisons, Bonferroni, family-wise error rate, false discovery rate

## MA-3.5

A study reports an accuracy improvement of 2.0 percentage points, with a frequentist 95% confidence interval of 0.5 to 3.5 points. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A credible interval is a Bayesian interval that states the probability that the parameter lies in it, given the data and a prior.
- [ ] B. The interval describes the spread of individual query-level improvements.
- [ ] C. The statement "there is a 95% probability that the true improvement lies between 0.5 and 3.5" is the standard frequentist reading of a confidence interval.
- [ ] D. The 95% in a confidence interval describes the long-run coverage of the procedure across repeated samples.
- [ ] E. A 90% confidence interval from the same data is wider than the 95% interval.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The credible interval gives a direct probability statement about the parameter.
- B: The interval concerns the mean improvement; the spread of individual changes is a prediction-interval or standard-deviation matter and is much wider.
- C: That reading belongs to a credible interval; a computed confidence interval either contains the true value or does not.
- D: About 95% of intervals built this way contain the true value.
- E: A lower confidence level uses a smaller multiplier and so gives a narrower interval.

**Source:** Confidence interval, credible interval, coverage, prediction interval

## MA-3.6

Consider the sample mean of n independent, identically distributed observations from a right-skewed population with finite variance, such as task completion times. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The sampling distribution of the mean is the distribution of the sample mean across repeated samples of size n.
- [ ] B. Strong positive correlation among observations enlarges the effective sample size.
- [ ] C. The central limit theorem says the sampling distribution of the mean is normal at small n as well as at large n.
- [ ] D. The central limit theorem says a histogram of the individual observations becomes bell-shaped as n grows.
- [ ] E. The skewness of the sample mean grows as n grows.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A sampling distribution describes a statistic, not the raw data.
- B: Correlated observations carry less information, so the effective sample size is smaller than n.
- C: The theorem is a limit statement; the approximation improves as n grows, and skewed data can need a large n.
- D: The raw data keep the population's shape; the distribution of the sample mean is what approaches normal.
- E: Skewness of the mean shrinks toward 0 in proportion to 1 over the square root of n.

**Source:** Sampling distribution, central limit theorem, effective sample size

## MA-3.7

A tutoring app invites its 1.25 million users to a satisfaction survey. A total of 50,000 respond and 92% of respondents say they are satisfied. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Respondents choosing for themselves whether to answer is self-selection, a source of nonresponse bias.
- [ ] B. A larger number of respondents reduces random error but leaves selection bias in place.
- [ ] C. The standard error quantifies the systematic bias that comes from who chose to respond.
- [ ] D. A large volunteer sample is a probability sample because it is large.
- [ ] E. Selection bias and measurement bias are two names for the same problem.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Those who answer can differ systematically from those who do not.
- B: Bias depends on the response mechanism, not on the count.
- C: The standard error captures chance variation and cannot detect a systematic difference between responders and non-responders.
- D: A probability sample needs known selection chances, and size does not supply them.
- E: Selection bias concerns who ends up in the data; measurement bias concerns errors in how values are recorded.

**Source:** Nonresponse bias, self-selection, standard error versus bias

## MA-3.8

A team runs 20 retrieval-quality trials, and the result is non-significant. Another analyst notes the sample was small. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Low power makes a non-significant result strong evidence that there is no effect.
- [ ] B. Statistical power is the probability of rejecting the null hypothesis when a true effect of a given size exists.
- [ ] C. A confidence interval that includes zero and also includes large benefits marks the study as inconclusive.
- [ ] D. An equivalence test is the tool for supporting the claim of "no meaningful effect".
- [ ] E. A non-significant result does not show the null hypothesis is true: absence of evidence differs from evidence of absence.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: With low power the test would likely miss a real effect, so the result is uninformative.
- B: Low power makes a non-significant result expected even if the effect is real.
- C: The data are compatible with both no effect and a sizable one.
- D: Equivalence testing sets a margin and tests that the effect lies within it.
- E: Failing to reject is not the same as confirming no effect.

**Source:** Absence of evidence, statistical power, equivalence test, inconclusive result

## MA-3.9

A team compares 40 prompt variants with a baseline, announces the best variant as significant at p = 0.03, and then plans a follow-up. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A preregistered hypothesis is one chosen after the data have been examined.
- [ ] B. The raw p-value of a selected best result understates how easily chance produces such a result.
- [ ] C. The Holm procedure controls the family-wise error rate and is less conservative than the Bonferroni correction.
- [ ] D. A Bonferroni-adjusted p-value is the raw p-value divided by the number of tests.
- [ ] E. Picking the best of many variants after seeing the data is exploratory; testing the winner once on fresh held-out data with a pre-specified hypothesis is confirmatory.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Preregistration fixes the hypothesis and analysis plan before looking at the outcome data.
- B: The smallest of many null p-values is routinely small.
- C: Holm is a step-down method that rejects at least as many hypotheses as Bonferroni.
- D: The adjusted p-value is the raw value multiplied by the number of tests, capped at 1.
- E: Confirmatory analysis fixes the hypothesis before the data are seen.

**Source:** Exploratory versus confirmatory analysis, Holm, adjusted p-value, preregistration

## MA-3.10

A safety filter passes 300 of 300 independent test prompts, and the report says "the failure rate is 0%". Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Zero observed failures give an upper confidence bound on the failure rate and do not establish a point value of zero.
- [ ] B. A higher confidence level gives a lower upper bound on the failure rate.
- [ ] C. By the rule of three, the 95% upper confidence bound after n failure-free tests is about 3 divided by n.
- [ ] D. The bound applies to inputs outside the distribution of the test prompts.
- [ ] E. Near-duplicate test prompts raise the effective number of independent tests.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A rare failure can be missed by chance in a limited test.
- B: Demanding more confidence widens the bound, so it rises.
- C: For n = 300 the bound is about 1%.
- D: The bound speaks only to inputs like those sampled; uncovered or adversarial inputs lie outside it.
- E: Near-duplicates are positively correlated and carry less independent information, so the effective sample size drops.

**Source:** Upper confidence bound, rule of three, representativeness

## MA-3.11

An analyst describes four data problems in plain words. Which statements name the problem correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Measurement bias and sampling bias are synonyms.
- [ ] B. Measurement bias shrinks when a larger random sample is drawn.
- [ ] C. A sensor that reads two degrees too high has measurement bias.
- [ ] D. A telephone survey that leaves out people without phones has a coverage (sampling) bias.
- [ ] E. Studying the companies that survived while ignoring those that failed is survivorship bias, a form of selection bias.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: One concerns recorded values, the other concerns who is in the sample.
- B: A bias in the instrument repeats in every observation, so more data do not remove it.
- C: Measurement bias is a systematic error in how a value is recorded.
- D: The sampling frame does not include part of the target population.
- E: Only the cases that passed a filter appear in the data.

**Source:** Sampling bias, selection bias, measurement bias, survivorship bias

# 4. Exploratory data analysis, data quality and missing data

## MA-4.1

A survey records age for each respondent and asks for income, which some respondents leave blank. Which statements use the missingness terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Missing not at random (MNAR) means missingness depends on the unobserved value itself, such as higher earners skipping because of income.
- [ ] B. Whether income is missing not at random can be confirmed from the observed values alone.
- [ ] C. Higher earners skipping the income question because of their income is missing at random.
- [ ] D. Missing completely at random (MCAR) means missingness is unrelated to the observed variables and to the unobserved values.
- [ ] E. Missing at random (MAR) means missingness depends on observed variables, such as older respondents skipping more often, and not on the missing value itself.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The reason for the gap is the very value that is absent.
- B: The observed data cannot reveal dependence on unobserved values; it takes outside knowledge or assumptions.
- C: Missingness driven by the value itself is MNAR, not MAR.
- D: MCAR is the least problematic missingness mechanism.
- E: Conditioning on the observed variable removes the dependence.

**Source:** MCAR, MAR, MNAR

## MA-4.2

A column has 10 rows; five values are observed and five are missing. An analyst fills each blank with the observed mean and treats the 10 rows as real data. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Mean imputation removes the bias when missingness is MNAR.
- [ ] B. Median imputation preserves the original variance.
- [ ] C. Mean imputation leaves the sample mean unchanged and shrinks the sample variance.
- [ ] D. Multiple imputation fills each blank once with the single best guess.
- [ ] E. Treating imputed values as observed data makes the standard error too small and overstates precision.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: If missingness depends on the missing value, filling with the observed mean keeps the bias.
- B: A single constant at the center lowers the variance, whether it is the mean or the median.
- C: Adding values equal to the mean adds no spread.
- D: Multiple imputation creates several completed datasets so the uncertainty about the imputed values is carried through.
- E: The invented values add rows without adding information.

**Source:** Mean imputation, multiple imputation, standard error

## MA-4.3

Eleven response times are 12, 13, 14, 14, 15, 15, 16, 18, 18, 19 and 120 seconds. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The interquartile range is the difference between the maximum and the minimum.
- [ ] B. The median and the interquartile range are robust (resistant) statistics, while the mean and standard deviation are sensitive to extreme values.
- [ ] C. The 1.5 × IQR rule flags candidate outliers for inspection.
- [ ] D. The mean of 24.9 seconds is a reliable summary of the typical response time here.
- [ ] E. A value flagged by the 1.5 × IQR rule is a data error and is deleted automatically.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: That is the range; the interquartile range is the third quartile minus the first.
- B: One extreme value moves the mean and standard deviation much more than the median and IQR.
- C: A flag marks a value to examine, not a verdict.
- D: The single extreme value pulls the mean far above the central bulk of the data.
- E: A flagged value can be a genuine rare event; deletion depends on how the value arose.

**Source:** Robust statistics, median, IQR, outlier rule

## MA-4.4

A pipeline joins an orders table to a customer table. The orders table has 50,000 rows and the joined table has 47,500, and the dropped rows belong to one region. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Row reconciliation compares counts by source, stage and group before and after a join against what is expected.
- [ ] B. Checks on null values, types and ranges can pass on the remaining rows even though rows are missing.
- [ ] C. If 5% of rows are lost, the statistics computed afterward are within 5% of their true values.
- [ ] D. A check repeated within each group can reveal a loss that the overall total hides.
- [ ] E. An anti-join lists the records in one table that have no matching key in the other, which reveals dropped keys.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A mismatch in counts exposes rows that were dropped.
- B: Checks on present rows leave no trace of rows that never arrived.
- C: Lost rows can differ systematically from the rest, so a statistic can shift by much more than the share lost.
- D: A stratified check shows that one region lost a quarter of its rows.
- E: An anti-join returns the unmatched rows.

**Source:** Row reconciliation, anti-join, stratified check, silent data loss

## MA-4.5

An analyst summarizes data with statistics and plots. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Pearson correlation measures linear association, so a perfect nonlinear relationship can have a correlation near 0.
- [ ] B. A Pearson correlation of 0.9 in observational data is a causal effect.
- [ ] C. A spike at exactly 0 in a measurement that should be continuous suggests a sentinel value such as a default or missing-value code.
- [ ] D. Datasets with identical summary statistics produce identical scatter plots.
- [ ] E. Pearson correlation is a robust statistic that one outlier barely changes.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Y = X² on a symmetric range has correlation 0 with X.
- B: Correlation is association; confounding or reverse causation can produce it without causation.
- C: A sentinel value is a placeholder entered in place of a real measurement.
- D: Anscombe's quartet shows very different plots that share the same means, variances and correlation.
- E: One far point can move the correlation from near 0 to near 1.

**Source:** Pearson correlation, sentinel value, Anscombe's quartet, correlation versus causation

## MA-4.6

A hospital estimates 30-day readmission from follow-up calls that reach only part of the patients; poorer-health patients are reached less often, and health status is recorded for each patient. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Complete-case analysis (listwise deletion) is justified when the missingness is MCAR, meaning unrelated to the data.
- [ ] B. When missingness depends on a recorded variable such as health status, weighting or imputing within strata can correct the bias.
- [ ] C. Dropping the incomplete rows gives an unbiased estimate when missingness depends on health status.
- [ ] D. Under MNAR, a sensitivity analysis shows how conclusions change under different assumptions about the missingness mechanism.
- [ ] E. A missingness indicator is a technique that makes MNAR data identifiable from the observed values.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Dropping incomplete rows leaves an unbiased subsample only under MCAR.
- B: Inverse probability weighting and stratified imputation use the observed variable.
- C: Under MAR, complete-case analysis is biased because the reached patients differ from the rest.
- D: The observed data cannot settle the mechanism, so assumptions are varied.
- E: A missingness indicator is a column that records which values were missing; it does not make the mechanism identifiable.

**Source:** Complete-case analysis, inverse probability weighting, sensitivity analysis, missingness indicator

## MA-4.7

An analyst describes the shape of a response-time variable and the best plot for it. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Standard deviation and variance are measures of central tendency.
- [ ] B. The median is the middle value of the sorted data, while the mean is the balance point of the data.
- [ ] C. In a right-skewed distribution the mean exceeds the median.
- [ ] D. The mode is another name for the average.
- [ ] E. A histogram shows the distribution of one variable, and a scatter plot shows the relationship between two variables.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: They measure spread, not center.
- B: They are two different measures of center.
- C: A long right tail pulls the mean upward more than the median.
- D: The mode is the most frequent value; the average is the mean.
- E: Histograms display shape; scatter plots display association.

**Source:** Skewness, mean versus median, mode, histogram versus scatter plot

# 5. Modeling basics: fit, overfitting and evaluation

## MA-5.1

A classifier for a rare event is scored at three thresholds, and a missed positive costs far more than a false alarm. Which statements use the metric terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy is a dependable summary when the positive class is rare.
- [ ] B. Recall is the share of actual positives that the classifier flags.
- [ ] C. F1 is the harmonic mean of precision and recall.
- [ ] D. Raising the decision threshold tends to raise precision and lower recall.
- [ ] E. Precision is the share of flagged cases that are truly positive.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: With a rare class, accuracy is dominated by the majority class and can be high for a useless model.
- B: Recall = true positives / (true positives + false negatives).
- C: F1 combines the two into one number that is low when either is low.
- D: A stricter cutoff flags fewer cases, mostly confident ones, and misses more positives.
- E: Precision = true positives / (true positives + false positives).

**Source:** Precision, recall, F1, accuracy, threshold

## MA-5.2

Polynomial regressions of increasing degree are fit to 40 training points, and errors are measured on the training points and on held-out points. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Underfitting shows as low training error and high held-out error.
- [ ] B. An overly flexible model has high bias and low variance.
- [ ] C. Regularization increases the flexibility of a model by adding more parameters.
- [ ] D. Training error is a dependable estimate of generalization error.
- [ ] E. Overfitting shows as low training error together with high held-out error.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Underfitting shows high error on both sets with a small gap between them.
- B: Overly flexible models have low bias and high variance.
- C: Regularization penalizes large coefficients to limit the effective flexibility.
- D: Training error falls as flexibility rises and says little about performance on new data.
- E: The model has fit noise in the training set.

**Source:** Overfitting, underfitting, regularization, training versus generalization error

## MA-5.3

A data scientist has 60 examples and 5,000 pure-noise features. They pick the 20 features most correlated with the label using all 60 examples, run 5-fold cross-validation on those features and report 92% accuracy. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Selecting features using the labels of the full dataset before cross-validation is leakage.
- [ ] B. Fitting a label-dependent step such as target encoding on the full data before splitting is also leakage.
- [ ] C. Data leakage means information from the held-out data influences model training or selection.
- [ ] D. With noise features and fair-coin labels, an honest evaluation should show accuracy near chance.
- [ ] E. Using more folds removes the leakage from the feature selection done before the split.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The held-out labels shaped which features were chosen.
- B: Any step that sees held-out labels contaminates the estimate; such steps belong inside each training fold.
- C: Leakage makes the held-out estimate optimistic.
- D: A model has no signal to learn, so honest accuracy is about 50%.
- E: The selection already used every label, so the number of folds does not change the leak.

**Source:** Data leakage, cross-validation, target encoding

## MA-5.4

A logistic regression predicts whether an account is flagged: log-odds of being flagged = −2.0 + 0.9 × x, where x is the number of prior incidents. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The coefficient 0.9 is the change in log-odds of being flagged for one more prior incident.
- [ ] B. The exponential of the coefficient, about 2.46, is an odds ratio per additional incident.
- [ ] C. Odds are the probability p divided by 1 minus p.
- [ ] D. Each additional prior incident multiplies the predicted probability of being flagged by 2.46.
- [ ] E. The effect of one more incident on the predicted probability is constant across the range of x.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Logistic regression is linear in the log-odds.
- B: Each added incident multiplies the odds by exp(0.9).
- C: Odds compare the chance of the event with the chance of its complement.
- D: The coefficient acts on the odds, not on the probability.
- E: The probability curve is S-shaped, so the change in probability depends on where you start.

**Source:** Log-odds, odds, odds ratio, predicted probability

## MA-5.5

A scorer assigns probabilities of being positive to nine cases, and an analyst compares AUC, calibration and log loss for it. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Cubing the scores leaves the AUC unchanged.
- [ ] B. A high AUC guarantees that the scores are well calibrated.
- [ ] C. Log loss treats a confident wrong prediction the same as an unsure wrong one.
- [ ] D. AUC is the probability that a randomly chosen positive is scored above a randomly chosen negative, so it measures discrimination (ranking).
- [ ] E. Calibration means that predicted probabilities match observed frequencies, such as 70% of cases scored 0.7 being positive.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: A monotonic transformation preserves the ranking, and AUC depends only on ranking.
- B: AUC measures ranking, so a well-ranked scorer can still have scores that do not match observed frequencies.
- C: Log loss grows steeply as the probability given to the true outcome approaches 0.
- D: AUC uses only the order of the scores.
- E: Calibration compares predicted probability with the actual rate.

**Source:** AUC, discrimination, calibration, log loss

## MA-5.6

A vendor says its screening model is "99.3% accurate" on a test set where 0.8% of cases are positive. The model flags 300 cases, of which 200 are truly positive. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A baseline that flags nothing can score high accuracy when the positive class is rare, which is why a majority-class baseline is a comparison point.
- [ ] B. A false negative is an actual positive that the model failed to flag.
- [ ] C. Specificity is the share of actual negatives that the model correctly leaves unflagged.
- [ ] D. Sensitivity and specificity are the same pair of quantities as precision and recall.
- [ ] E. A 0.5 cutoff minimizes expected cost regardless of the relative costs of the two error types.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Accuracy reflects mostly the common class.
- B: False negatives are the missed positives.
- C: Specificity = true negatives / (true negatives + false positives).
- D: Sensitivity equals recall, but specificity is a different quantity from precision.
- E: The cost-minimizing threshold depends on the relative cost of false negatives and false positives.

**Source:** Confusion matrix, false negative, specificity, majority-class baseline, cost-based threshold

## MA-5.7

A team tries 200 hyperparameter configurations, scores each on the same fixed test set, and reports the best score as the expected accuracy in production. Which statements use the terms correctly? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tuning belongs on a validation set or in cross-validation, and the test set is used once at the end.
- [ ] B. Nested cross-validation uses an inner loop for tuning and an outer loop for estimating performance.
- [ ] C. Choosing the best of many configurations on the test set makes the reported score optimistic, a selection effect called the winner's curse.
- [ ] D. Distribution shift between the test data and production data leaves the test accuracy a valid estimate of production accuracy.
- [ ] E. Near-duplicate examples shared between training and test splits make the score pessimistic.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Keeping the test set untouched gives an independent estimate.
- B: The outer folds never influence the choices made in the inner loop.
- C: The maximum of many noisy scores is biased upward.
- D: Under distribution shift, test accuracy can overstate performance in production.
- E: Shared near-duplicates leak information and make the score optimistic.

**Source:** Winner's curse, validation set, nested cross-validation, distribution shift
