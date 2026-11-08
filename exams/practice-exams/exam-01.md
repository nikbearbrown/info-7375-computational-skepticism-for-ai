# INFO 7375 Computational Skepticism for AI: practice exam 01

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** A school buys a detector that labels essays "AI-written" and states it is "98% accurate", meaning it flags 98% of AI-written essays and wrongly flags 2% of human-written essays. A teacher asks how likely a flagged essay is to be AI-written. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. When AI-written essays are rare, the positive predictive value of a flag is higher than when they are common.
- [ ] B. The vendor's "accuracy" claim reports the false discovery rate of the detector.
- [ ] C. Treating P(flagged | AI-written) as if it were P(AI-written | flagged) is an application of the law of total probability.
- [ ] D. The vendor's 98% is a sensitivity, P(flagged | AI-written), and it does not answer the teacher's question.
- [ ] E. The teacher's question asks for the positive predictive value of a flag.

**2.** An analyst describes four data problems in plain words. Which statements name the problem correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Measurement bias and sampling bias are synonyms.
- [ ] B. Measurement bias shrinks when a larger random sample is drawn.
- [ ] C. A sensor that reads two degrees too high has measurement bias.
- [ ] D. A telephone survey that leaves out people without phones has a coverage (sampling) bias.
- [ ] E. Studying the companies that survived while ignoring those that failed is survivorship bias, a form of selection bias.

**3.** An engineer says the pipeline has been validated because the output matches the written specification. Check each statement that is true.  *(5 points)*

- [ ] A. Verification asks whether the system meets the real need of its users.
- [ ] B. Verification and validation answer the same question.
- [ ] C. Validation means re-running the same code to check it gives the same output.
- [ ] D. Validation asks whether the output conforms to the written specification.
- [ ] E. A pipeline can conform to its specification and still fail to serve the real need.

**4.** A regulator asks whether a screening tool shows disparate treatment, disparate impact, or both. Check each statement that is true.  *(5 points)*

- [ ] A. Disparate treatment means deciding differently for people because of a protected attribute, such as using race as an input.
- [ ] B. Disparate treatment describes unequal outcome rates regardless of how decisions are made.
- [ ] C. Disparate impact requires proof of intent to discriminate.
- [ ] D. A model that does not take the protected attribute as input is free of disparate impact.
- [ ] E. Disparate impact means a neutral-looking practice produces substantially different outcomes across groups.

**5.** A report gives a 95% interval for a mean and a second report gives a 95% interval from a Bayesian model. Check each statement that is true.  *(5 points)*

- [ ] A. Confidence interval and credible interval are two names for the same thing.
- [ ] B. A 95% credible interval says that, given the model and prior, the parameter lies in the interval with probability 0.95.
- [ ] C. A confidence interval is a posterior probability statement about the parameter in the one interval computed.
- [ ] D. A 95% confidence interval comes from a procedure that captures the true parameter in about 95% of repeated samples.
- [ ] E. A credible interval needs a prior distribution.

**6.** Eleven response times are 12, 13, 14, 14, 15, 15, 16, 18, 18, 19 and 120 seconds. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The interquartile range is the difference between the maximum and the minimum.
- [ ] B. The median and the interquartile range are robust (resistant) statistics, while the mean and standard deviation are sensitive to extreme values.
- [ ] C. The 1.5 × IQR rule flags candidate outliers for inspection.
- [ ] D. The mean of 24.9 seconds is a reliable summary of the typical response time here.
- [ ] E. A value flagged by the 1.5 × IQR rule is a data error and is deleted automatically.

**7.** A model is trained on patients who had a lab panel in the first hours of admission. Patients who looked unstable were less likely to get the panel, so the retained patients do not represent all admissions. Check each statement that is true.  *(5 points)*

- [ ] A. A baseline risk learned from the retained patients is miscalibrated for the full admitted population.
- [ ] B. Weighting retained patients by the inverse of their retention probability corrects the skew even when retention depends on an unrecorded variable.
- [ ] C. Collecting more records under the same retention rule removes the bias.
- [ ] D. This is measurement bias, because the lab values are recorded with error.
- [ ] E. This is selection bias, because inclusion in the data depends on a variable related to the outcome.

**8.** Request latency for a service is modeled as a normal distribution with mean 200 ms and standard deviation 40 ms. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A z-score counts how many standard deviations a value lies from the mean.
- [ ] B. A fat-tailed (heavy-tailed) distribution tends to put more probability far from the mean than a normal with the same mean and standard deviation.
- [ ] C. Two distributions with the same mean and standard deviation have the same tail probabilities.
- [ ] D. About 68% of a normal distribution lies within two standard deviations of the mean.
- [ ] E. The 68-95-99.7 rule holds for skewed distributions as well as for normal ones.

**9.** A vendor says its screening model is "99.3% accurate" on a test set where 0.8% of cases are positive. The model flags 300 cases, of which 200 are truly positive. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A baseline that flags nothing can score high accuracy when the positive class is rare, which is why a majority-class baseline is a comparison point.
- [ ] B. A false negative is an actual positive that the model failed to flag.
- [ ] C. Specificity is the share of actual negatives that the model correctly leaves unflagged.
- [ ] D. Sensitivity and specificity are the same pair of quantities as precision and recall.
- [ ] E. A 0.5 cutoff minimizes expected cost regardless of the relative costs of the two error types.

**10.** An analyst reports that ice cream sales is the most important feature for predicting drownings and concludes that cutting ice cream sales will cut drownings. Check each statement that is true.  *(5 points)*

- [ ] A. Feature importance measures how much a model relies on an input to make predictions.
- [ ] B. A causal effect describes how the outcome changes when the input is set by intervention.
- [ ] C. An input can have high importance because it acts as a proxy for the true cause.
- [ ] D. A high feature importance shows that the input causes the outcome.
- [ ] E. A confounder such as hot weather can drive both variables and make one predict the other.

**11.** A student says: "the model memorised the training set, so it has high bias." Check each statement that is true.  *(5 points)*

- [ ] A. Overfitting is the result of high bias.
- [ ] B. High bias means the model is flexible enough to memorise noise.
- [ ] C. High variance means the model is too simple to capture the pattern.
- [ ] D. Overfitting means low error on training data and high error on held-out data.
- [ ] E. Bias in the bias-variance sense is the same as demographic bias.

**12.** A team plans monitoring for a deployed classifier. Check each statement that is true.  *(5 points)*

- [ ] A. Input drift monitoring needs labels.
- [ ] B. Monitoring is finished once the model passes offline tests.
- [ ] C. Performance monitoring needs ground truth, which often arrives with delay.
- [ ] D. A feature distribution alert is the same as an accuracy drop.
- [ ] E. Monitoring tracks inputs, predictions and outcomes of a deployed model over time.

**13.** A help desk logs tickets by type (billing or technical) and by whether each was escalated. Which statements use the probability terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. P(escalated) over the full log is a marginal probability, a weighted average of the group-level conditional probabilities.
- [ ] B. Ticket type and escalation are independent when P(escalated | billing) differs from P(escalated | technical).
- [ ] C. P(billing and escalated) is a joint probability: the share of the full log that is both billing and escalated.
- [ ] D. P(billing | escalated) is the same quantity as P(escalated | billing) with the words reordered.
- [ ] E. P(escalated | billing) is a conditional probability: the chance of escalation within the billing tickets.

**14.** A team tests 20 prompt variants against a baseline, each at significance level 0.05, and none truly differs. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The family-wise error rate is the expected share of false findings among the discoveries.
- [ ] B. The false discovery rate is the expected proportion of false findings among the results declared significant.
- [ ] C. Testing 20 variants and reporting the best raw p-value is a multiple comparisons (multiplicity) problem.
- [ ] D. The Benjamini–Hochberg procedure controls the family-wise error rate.
- [ ] E. The Bonferroni correction divides the significance level by the number of tests.

**15.** A column named age holds the value 240 in one row, and a date column holds text such as "next Tuesday". Check each statement that is true.  *(5 points)*

- [ ] A. A semantic check is another name for a schema check.
- [ ] B. An age of 240 stored as an integer passes the schema check but fails a semantic check.
- [ ] C. Text in a date column fails the schema check.
- [ ] D. A schema check tests structure such as column names, types and required fields.
- [ ] E. A semantic check tests whether values make sense in the domain, such as a plausible age.

**16.** A risk score is well calibrated across the whole population but its calibration has not been checked for each group. Check each statement that is true.  *(5 points)*

- [ ] A. A reliability diagram is a standard way to inspect calibration.
- [ ] B. Overall calibration guarantees calibration within each group.
- [ ] C. Calibration is the same as accuracy.
- [ ] D. Calibration means that among people given score p, about a fraction p have the outcome.
- [ ] E. Calibration within groups asks for that match separately in each group.

**17.** A dashboard shows "churn will be 12%" with no range, and a reviewer asks for an interval estimate. Check each statement that is true.  *(5 points)*

- [ ] A. An interval estimate gives a range that expresses uncertainty.
- [ ] B. A point estimate carries a measure of its own uncertainty.
- [ ] C. A point estimate is a single value reported as the best guess.
- [ ] D. Raising the confidence level from 90% to 99% widens the interval, other things equal.
- [ ] E. A wider interval at the same confidence level signals more uncertainty.

**18.** A hospital estimates 30-day readmission from follow-up calls that reach only part of the patients; poorer-health patients are reached less often, and health status is recorded for each patient. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Complete-case analysis (listwise deletion) is justified when the missingness is MCAR, meaning unrelated to the data.
- [ ] B. When missingness depends on a recorded variable such as health status, weighting or imputing within strata can correct the bias.
- [ ] C. Dropping the incomplete rows gives an unbiased estimate when missingness depends on health status.
- [ ] D. Under MNAR, a sensitivity analysis shows how conclusions change under different assumptions about the missingness mechanism.
- [ ] E. A missingness indicator is a technique that makes MNAR data identifiable from the observed values.

**19.** A table has an income column. Group B has 40% blank incomes and group A has 1%, and the overall missing rate is under 3%. A quality gate flags a column only when its overall missing rate is above 5%. Check each statement that is true.  *(5 points)*

- [ ] A. A blank rate that differs by group means the missingness is not MCAR.
- [ ] B. The gate on the overall rate can pass while one group holds most of the blanks.
- [ ] C. Dropping the rows with a blank income, complete-case analysis, is safe because few rows are lost overall.
- [ ] D. Missingness that depends on group but not on income within a group is MAR.
- [ ] E. Reporting the missing rate within each group is a stratified check that the overall rate does not replace.

**20.** An agent retries a failing tool call before giving up. Let X be the number of retries in one run, with P(X=0) = 0.50, P(X=1) = 0.30, P(X=2) = 0.15 and P(X=3) = 0.05. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The mode of X is its most probable value, and it can differ from the expected value.
- [ ] B. The expected value of X is the probability-weighted mean of its possible values.
- [ ] C. Adding a constant to a random variable changes its variance.
- [ ] D. Variance is measured in squared units of X, while standard deviation is measured in the units of X.
- [ ] E. The expected value of a discrete random variable is itself one of its possible values.
