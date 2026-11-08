# INFO 7375 Computational Skepticism for AI: practice exam 01: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A school buys a detector that labels essays "AI-written" and states it is "98% accurate", meaning it flags 98% of AI-written essays and wrongly flags 2% of human-written essays. A teacher asks how likely a flagged essay is to be AI-written. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. When AI-written essays are rare, the positive predictive value of a flag is higher than when they are common.
- [ ] B. The vendor's "accuracy" claim reports the false discovery rate of the detector.
- [ ] C. Treating P(flagged | AI-written) as if it were P(AI-written | flagged) is an application of the law of total probability.
- [ ] D. The vendor's 98% is a sensitivity, P(flagged | AI-written), and it does not answer the teacher's question.
- [ ] E. The teacher's question asks for the positive predictive value of a flag.

**Key:** A=F B=F C=F D=T E=T  |  `MA-1.6`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Transposed conditional, base rate fallacy, positive predictive value

- A (false): A lower base rate lowers the positive predictive value because false flags from the large legitimate group dominate.
- B (false): The claim reports error rates conditional on the true class, not the share of flags that are wrong.
- C (false): That error is called transposing the conditional; it ignores the base rate and is also called the base rate fallacy.
- D (true): The teacher needs the reverse conditional, P(AI-written | flagged).
- E (true): Positive predictive value is the probability that a flagged case is truly positive.

**2.** An analyst describes four data problems in plain words. Which statements name the problem correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Measurement bias and sampling bias are synonyms.
- [ ] B. Measurement bias shrinks when a larger random sample is drawn.
- [ ] C. A sensor that reads two degrees too high has measurement bias.
- [ ] D. A telephone survey that leaves out people without phones has a coverage (sampling) bias.
- [ ] E. Studying the companies that survived while ignoring those that failed is survivorship bias, a form of selection bias.

**Key:** A=F B=F C=T D=T E=T  |  `MA-3.11`  |  *3. Sampling, the central limit theorem and inference*  |  source: Sampling bias, selection bias, measurement bias, survivorship bias

- A (false): One concerns recorded values, the other concerns who is in the sample.
- B (false): A bias in the instrument repeats in every observation, so more data do not remove it.
- C (true): Measurement bias is a systematic error in how a value is recorded.
- D (true): The sampling frame does not include part of the target population.
- E (true): Only the cases that passed a filter appear in the data.

**3.** An engineer says the pipeline has been validated because the output matches the written specification. Check each statement that is true.  *(5 points)*

- [ ] A. Verification asks whether the system meets the real need of its users.
- [ ] B. Verification and validation answer the same question.
- [ ] C. Validation means re-running the same code to check it gives the same output.
- [ ] D. Validation asks whether the output conforms to the written specification.
- [ ] E. A pipeline can conform to its specification and still fail to serve the real need.

**Key:** A=F B=F C=F D=F E=T  |  `MA-jargon.14`  |  *Jargon test: data validation and provenance*  |  source: Validation vs verification

- A (false): That describes validation.
- B (false): Building it right differs from building the right thing.
- C (false): That is reproducibility.
- D (false): That describes verification.
- E (true): Passing verification does not guarantee validation.

**4.** A regulator asks whether a screening tool shows disparate treatment, disparate impact, or both. Check each statement that is true.  *(5 points)*

- [ ] A. Disparate treatment means deciding differently for people because of a protected attribute, such as using race as an input.
- [ ] B. Disparate treatment describes unequal outcome rates regardless of how decisions are made.
- [ ] C. Disparate impact requires proof of intent to discriminate.
- [ ] D. A model that does not take the protected attribute as input is free of disparate impact.
- [ ] E. Disparate impact means a neutral-looking practice produces substantially different outcomes across groups.

**Key:** A=T B=F C=F D=F E=T  |  `MA-jargon.59`  |  *Jargon test: bias and fairness*  |  source: Disparate treatment vs disparate impact

- A (true): It concerns the basis for the decision.
- B (false): That is closer to disparate impact.
- C (false): Intent is part of disparate treatment, not disparate impact.
- D (false): Proxies can produce unequal outcomes without the attribute as an input.
- E (true): It concerns the effect of the practice.

**5.** A report gives a 95% interval for a mean and a second report gives a 95% interval from a Bayesian model. Check each statement that is true.  *(5 points)*

- [ ] A. Confidence interval and credible interval are two names for the same thing.
- [ ] B. A 95% credible interval says that, given the model and prior, the parameter lies in the interval with probability 0.95.
- [ ] C. A confidence interval is a posterior probability statement about the parameter in the one interval computed.
- [ ] D. A 95% confidence interval comes from a procedure that captures the true parameter in about 95% of repeated samples.
- [ ] E. A credible interval needs a prior distribution.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.3`  |  *Jargon test: probability and confidence*  |  source: Confidence interval vs credible interval

- A (false): They have different meanings and different assumptions.
- B (true): A credible interval is a posterior probability statement.
- C (false): That reading belongs to a credible interval.
- D (true): Confidence refers to the long-run behaviour of the procedure.
- E (true): The posterior, and so the interval, combines prior and likelihood.

**6.** Eleven response times are 12, 13, 14, 14, 15, 15, 16, 18, 18, 19 and 120 seconds. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The interquartile range is the difference between the maximum and the minimum.
- [ ] B. The median and the interquartile range are robust (resistant) statistics, while the mean and standard deviation are sensitive to extreme values.
- [ ] C. The 1.5 × IQR rule flags candidate outliers for inspection.
- [ ] D. The mean of 24.9 seconds is a reliable summary of the typical response time here.
- [ ] E. A value flagged by the 1.5 × IQR rule is a data error and is deleted automatically.

**Key:** A=F B=T C=T D=F E=F  |  `MA-4.3`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Robust statistics, median, IQR, outlier rule

- A (false): That is the range; the interquartile range is the third quartile minus the first.
- B (true): One extreme value moves the mean and standard deviation much more than the median and IQR.
- C (true): A flag marks a value to examine, not a verdict.
- D (false): The single extreme value pulls the mean far above the central bulk of the data.
- E (false): A flagged value can be a genuine rare event; deletion depends on how the value arose.

**7.** A model is trained on patients who had a lab panel in the first hours of admission. Patients who looked unstable were less likely to get the panel, so the retained patients do not represent all admissions. Check each statement that is true.  *(5 points)*

- [ ] A. A baseline risk learned from the retained patients is miscalibrated for the full admitted population.
- [ ] B. Weighting retained patients by the inverse of their retention probability corrects the skew even when retention depends on an unrecorded variable.
- [ ] C. Collecting more records under the same retention rule removes the bias.
- [ ] D. This is measurement bias, because the lab values are recorded with error.
- [ ] E. This is selection bias, because inclusion in the data depends on a variable related to the outcome.

**Key:** A=T B=F C=F D=F E=T  |  `MA-ch06.2`  |  *None*  |  source: Selection bias and inverse probability weighting

- A (true): Calibration means predicted risks match observed frequencies, and a skewed sample breaks that match.
- B (false): Weighting needs a recorded variable that explains who was kept.
- C (false): More data from the same filter reproduces the same skewed mix with less noise.
- D (false): Measurement bias concerns how values are recorded, whereas here the issue is who is recorded.
- E (true): Selection bias arises when the rule that decides who enters the data is tied to what is being predicted.

**8.** Request latency for a service is modeled as a normal distribution with mean 200 ms and standard deviation 40 ms. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A z-score counts how many standard deviations a value lies from the mean.
- [ ] B. A fat-tailed (heavy-tailed) distribution tends to put more probability far from the mean than a normal with the same mean and standard deviation.
- [ ] C. Two distributions with the same mean and standard deviation have the same tail probabilities.
- [ ] D. About 68% of a normal distribution lies within two standard deviations of the mean.
- [ ] E. The 68-95-99.7 rule holds for skewed distributions as well as for normal ones.

**Key:** A=T B=T C=F D=F E=F  |  `MA-2.4`  |  *2. Random variables and distributions*  |  source: Normal distribution, z-score, empirical rule, fat tails

- A (true): A 280 ms request has z = (280 − 200) / 40 = 2.
- B (true): Heavy tails make extreme values more common than the normal curve predicts.
- C (false): Tail mass depends on the whole shape, not just the first two moments.
- D (false): About 68% lies within one standard deviation; about 95% lies within two.
- E (false): The empirical rule is a property of the normal distribution.

**9.** A vendor says its screening model is "99.3% accurate" on a test set where 0.8% of cases are positive. The model flags 300 cases, of which 200 are truly positive. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A baseline that flags nothing can score high accuracy when the positive class is rare, which is why a majority-class baseline is a comparison point.
- [ ] B. A false negative is an actual positive that the model failed to flag.
- [ ] C. Specificity is the share of actual negatives that the model correctly leaves unflagged.
- [ ] D. Sensitivity and specificity are the same pair of quantities as precision and recall.
- [ ] E. A 0.5 cutoff minimizes expected cost regardless of the relative costs of the two error types.

**Key:** A=T B=T C=T D=F E=F  |  `MA-5.6`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Confusion matrix, false negative, specificity, majority-class baseline, cost-based threshold

- A (true): Accuracy reflects mostly the common class.
- B (true): False negatives are the missed positives.
- C (true): Specificity = true negatives / (true negatives + false positives).
- D (false): Sensitivity equals recall, but specificity is a different quantity from precision.
- E (false): The cost-minimizing threshold depends on the relative cost of false negatives and false positives.

**10.** An analyst reports that ice cream sales is the most important feature for predicting drownings and concludes that cutting ice cream sales will cut drownings. Check each statement that is true.  *(5 points)*

- [ ] A. Feature importance measures how much a model relies on an input to make predictions.
- [ ] B. A causal effect describes how the outcome changes when the input is set by intervention.
- [ ] C. An input can have high importance because it acts as a proxy for the true cause.
- [ ] D. A high feature importance shows that the input causes the outcome.
- [ ] E. A confounder such as hot weather can drive both variables and make one predict the other.

**Key:** A=T B=T C=T D=F E=T  |  `MA-jargon.42`  |  *Jargon test: explainability*  |  source: Feature importance vs causal effect

- A (true): It describes the fitted model's dependence on the input, not the world.
- B (true): Causal effect is defined by an intervention, not by predictive usefulness.
- C (true): A proxy carries information about the cause, so the model leans on it without it being causal.
- D (false): Importance reflects association the model exploited, which a confounder can create.
- E (true): A confounder is a common cause that produces a non-causal association.

**11.** A student says: "the model memorised the training set, so it has high bias." Check each statement that is true.  *(5 points)*

- [ ] A. Overfitting is the result of high bias.
- [ ] B. High bias means the model is flexible enough to memorise noise.
- [ ] C. High variance means the model is too simple to capture the pattern.
- [ ] D. Overfitting means low error on training data and high error on held-out data.
- [ ] E. Bias in the bias-variance sense is the same as demographic bias.

**Key:** A=F B=F C=F D=T E=F  |  `MA-jargon.77`  |  *Jargon test: wrong word, right word*  |  source: Overfitting, bias, variance

- A (false): Overfitting is typically associated with high variance.
- B (false): High bias means the model is too simple, which is underfitting.
- C (false): High variance means sensitivity to the particular training sample.
- D (true): The model fits noise in the training set.
- E (false): The statistical bias-variance sense is about systematic error of the model's predictions, not about groups.

**12.** A team plans monitoring for a deployed classifier. Check each statement that is true.  *(5 points)*

- [ ] A. Input drift monitoring needs labels.
- [ ] B. Monitoring is finished once the model passes offline tests.
- [ ] C. Performance monitoring needs ground truth, which often arrives with delay.
- [ ] D. A feature distribution alert is the same as an accuracy drop.
- [ ] E. Monitoring tracks inputs, predictions and outcomes of a deployed model over time.

**Key:** A=F B=F C=T D=F E=T  |  `MA-jargon.32`  |  *Jargon test: robustness and distribution shift*  |  source: Monitoring

- A (false): Input drift compares feature distributions and needs no labels.
- B (false): Shift happens after release, so monitoring continues.
- C (true): Accuracy cannot be computed until outcomes are known.
- D (false): An alert concerns inputs and accuracy concerns outcomes.
- E (true): It is ongoing observation after release.

**13.** A help desk logs tickets by type (billing or technical) and by whether each was escalated. Which statements use the probability terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. P(escalated) over the full log is a marginal probability, a weighted average of the group-level conditional probabilities.
- [ ] B. Ticket type and escalation are independent when P(escalated | billing) differs from P(escalated | technical).
- [ ] C. P(billing and escalated) is a joint probability: the share of the full log that is both billing and escalated.
- [ ] D. P(billing | escalated) is the same quantity as P(escalated | billing) with the words reordered.
- [ ] E. P(escalated | billing) is a conditional probability: the chance of escalation within the billing tickets.

**Key:** A=T B=F C=T D=F E=T  |  `MA-1.2`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Conditional, joint and marginal probability

- A (true): A marginal probability ignores the grouping and equals the sum of each group share times its conditional probability.
- B (false): Independence needs the conditional probability to equal the marginal for each group; differing rates signal dependence.
- C (true): A joint probability is the chance that two events happen together.
- D (false): Swapping the conditioning event gives a different conditional probability with a different value.
- E (true): A conditional probability restricts attention to the cases where the given event holds.

**14.** A team tests 20 prompt variants against a baseline, each at significance level 0.05, and none truly differs. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The family-wise error rate is the expected share of false findings among the discoveries.
- [ ] B. The false discovery rate is the expected proportion of false findings among the results declared significant.
- [ ] C. Testing 20 variants and reporting the best raw p-value is a multiple comparisons (multiplicity) problem.
- [ ] D. The Benjamini–Hochberg procedure controls the family-wise error rate.
- [ ] E. The Bonferroni correction divides the significance level by the number of tests.

**Key:** A=F B=T C=T D=F E=T  |  `MA-3.4`  |  *3. Sampling, the central limit theorem and inference*  |  source: Multiple comparisons, Bonferroni, family-wise error rate, false discovery rate

- A (false): That describes the false discovery rate; the family-wise error rate is the probability of at least one false positive.
- B (true): It is a weaker guarantee than controlling the family-wise error rate.
- C (true): The chance of at least one false positive grows with the number of tests.
- D (false): Benjamini–Hochberg controls the false discovery rate; Bonferroni and Holm control the family-wise error rate.
- E (true): With 20 tests the per-test threshold becomes 0.05 / 20 = 0.0025.

**15.** A column named age holds the value 240 in one row, and a date column holds text such as "next Tuesday". Check each statement that is true.  *(5 points)*

- [ ] A. A semantic check is another name for a schema check.
- [ ] B. An age of 240 stored as an integer passes the schema check but fails a semantic check.
- [ ] C. Text in a date column fails the schema check.
- [ ] D. A schema check tests structure such as column names, types and required fields.
- [ ] E. A semantic check tests whether values make sense in the domain, such as a plausible age.

**Key:** A=F B=T C=T D=T E=T  |  `MA-jargon.15`  |  *Jargon test: data validation and provenance*  |  source: Schema vs semantic check

- A (false): The two check different things.
- B (true): The type is right but the value is implausible.
- C (true): The type does not match the declared type.
- D (true): Schema concerns shape and type, not meaning.
- E (true): Semantic checks use domain meaning.

**16.** A risk score is well calibrated across the whole population but its calibration has not been checked for each group. Check each statement that is true.  *(5 points)*

- [ ] A. A reliability diagram is a standard way to inspect calibration.
- [ ] B. Overall calibration guarantees calibration within each group.
- [ ] C. Calibration is the same as accuracy.
- [ ] D. Calibration means that among people given score p, about a fraction p have the outcome.
- [ ] E. Calibration within groups asks for that match separately in each group.

**Key:** A=T B=F C=F D=T E=T  |  `MA-jargon.65`  |  *Jargon test: bias and fairness*  |  source: Calibration

- A (true): It plots predicted probability against observed frequency.
- B (false): Group-level miscalibration can cancel out in the average.
- C (false): Calibration compares probabilities to frequencies; accuracy counts correct decisions.
- D (true): Stated probability matches observed frequency.
- E (true): The condition is applied per group.

**17.** A dashboard shows "churn will be 12%" with no range, and a reviewer asks for an interval estimate. Check each statement that is true.  *(5 points)*

- [ ] A. An interval estimate gives a range that expresses uncertainty.
- [ ] B. A point estimate carries a measure of its own uncertainty.
- [ ] C. A point estimate is a single value reported as the best guess.
- [ ] D. Raising the confidence level from 90% to 99% widens the interval, other things equal.
- [ ] E. A wider interval at the same confidence level signals more uncertainty.

**Key:** A=T B=F C=T D=T E=T  |  `MA-jargon.9`  |  *Jargon test: probability and confidence*  |  source: Point estimate vs interval

- A (true): The range reflects sampling or model uncertainty.
- B (false): A bare point estimate is silent about uncertainty.
- C (true): It gives one number with no spread.
- D (true): A higher level needs a wider range to capture the parameter as often.
- E (true): Width is a direct reading of the uncertainty.

**18.** A hospital estimates 30-day readmission from follow-up calls that reach only part of the patients; poorer-health patients are reached less often, and health status is recorded for each patient. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Complete-case analysis (listwise deletion) is justified when the missingness is MCAR, meaning unrelated to the data.
- [ ] B. When missingness depends on a recorded variable such as health status, weighting or imputing within strata can correct the bias.
- [ ] C. Dropping the incomplete rows gives an unbiased estimate when missingness depends on health status.
- [ ] D. Under MNAR, a sensitivity analysis shows how conclusions change under different assumptions about the missingness mechanism.
- [ ] E. A missingness indicator is a technique that makes MNAR data identifiable from the observed values.

**Key:** A=T B=T C=F D=T E=F  |  `MA-4.6`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Complete-case analysis, inverse probability weighting, sensitivity analysis, missingness indicator

- A (true): Dropping incomplete rows leaves an unbiased subsample only under MCAR.
- B (true): Inverse probability weighting and stratified imputation use the observed variable.
- C (false): Under MAR, complete-case analysis is biased because the reached patients differ from the rest.
- D (true): The observed data cannot settle the mechanism, so assumptions are varied.
- E (false): A missingness indicator is a column that records which values were missing; it does not make the mechanism identifiable.

**19.** A table has an income column. Group B has 40% blank incomes and group A has 1%, and the overall missing rate is under 3%. A quality gate flags a column only when its overall missing rate is above 5%. Check each statement that is true.  *(5 points)*

- [ ] A. A blank rate that differs by group means the missingness is not MCAR.
- [ ] B. The gate on the overall rate can pass while one group holds most of the blanks.
- [ ] C. Dropping the rows with a blank income, complete-case analysis, is safe because few rows are lost overall.
- [ ] D. Missingness that depends on group but not on income within a group is MAR.
- [ ] E. Reporting the missing rate within each group is a stratified check that the overall rate does not replace.

**Key:** A=T B=T C=F D=T E=T  |  `MA-ch03.10`  |  *None*  |  source: Differential missingness and stratified checks

- A (true): MCAR requires the chance of a blank to be independent of observed variables such as group.
- B (true): An aggregate rate hides concentration, so a small overall rate says little about a subgroup.
- C (false): Complete-case analysis removes much of group B, which changes the group mix and can bias results about B.
- D (true): Dependence on an observed variable alone is the definition of MAR.
- E (true): A stratified check computes a statistic within subgroups, which exposes differences that an overall figure averages away.

**20.** An agent retries a failing tool call before giving up. Let X be the number of retries in one run, with P(X=0) = 0.50, P(X=1) = 0.30, P(X=2) = 0.15 and P(X=3) = 0.05. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The mode of X is its most probable value, and it can differ from the expected value.
- [ ] B. The expected value of X is the probability-weighted mean of its possible values.
- [ ] C. Adding a constant to a random variable changes its variance.
- [ ] D. Variance is measured in squared units of X, while standard deviation is measured in the units of X.
- [ ] E. The expected value of a discrete random variable is itself one of its possible values.

**Key:** A=T B=T C=F D=T E=F  |  `MA-2.1`  |  *2. Random variables and distributions*  |  source: Expected value, mode, variance, standard deviation

- A (true): Here the mode is 0 while the mean is 0.75.
- B (true): Expected value is the long-run average, the sum of each value times its probability.
- C (false): A shift moves the distribution but leaves its spread, and so its variance, unchanged.
- D (true): The standard deviation is the square root of the variance.
- E (false): The mean of 0.75 is not a possible number of retries.
