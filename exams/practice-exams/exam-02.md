# INFO 7375 Computational Skepticism for AI: practice exam 02

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** A classifier for a rare event is scored at three thresholds, and a missed positive costs far more than a false alarm. Which statements use the metric terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Accuracy is a dependable summary when the positive class is rare.
- [ ] B. Recall is the share of actual positives that the classifier flags.
- [ ] C. F1 is the harmonic mean of precision and recall.
- [ ] D. Raising the decision threshold tends to raise precision and lower recall.
- [ ] E. Precision is the share of flagged cases that are truly positive.

**2.** Two groups have different shares of people who truly have the positive outcome, and a classifier is imperfect. Check each statement that is true.  *(5 points)*

- [ ] A. A base-rate difference is evidence that the model is biased.
- [ ] B. With differing base rates and an imperfect classifier, calibration within groups and equalized odds generally do not hold together.
- [ ] C. The base rate is the proportion of a group that has the positive outcome.
- [ ] D. The base rate is the same as a group's false positive rate.
- [ ] E. A base-rate difference in the data can itself reflect historical bias.

**3.** An analyst prompts: "Tell me how accurate and how confident the model's 70% scores are." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Report discrimination as AUC and calibration as expected calibration error, as separate quantities.
- [ ] B. Use the word accuracy for the share of predictions that are correct.
- [ ] C. Report AUC to show the scores are calibrated.
- [ ] D. Call the bootstrap interval for accuracy a posterior.
- [ ] E. Report calibration of the predicted probabilities with a reliability diagram.

**4.** Fraud rises from 1% to 3% of transactions, and fraudulent transactions look the same as before. Check each statement that is true.  *(5 points)*

- [ ] A. P(y) has changed.
- [ ] B. The decision threshold may need adjusting because the class prior changed.
- [ ] C. This is label shift, also called prior shift.
- [ ] D. P(x | y) is unchanged.
- [ ] E. This is concept drift.

**5.** Two explanation methods are compared. Clinicians rate one method's heat maps as sensible, while a test shows the other method tracks the classifier's behaviour more closely. Check each statement that is true.  *(5 points)*

- [ ] A. Clinician ratings of how sensible heat maps look measure faithfulness.
- [ ] B. Faithfulness is how accurately an explanation reflects what the model actually does.
- [ ] C. A plausible explanation is therefore faithful.
- [ ] D. Plausibility is how closely an explanation matches the model's computation.
- [ ] E. An explanation can be faithful and implausible if the model relies on a spurious cue.

**6.** A support-ticket classifier is 93% accurate overall but 60% accurate on a small segment, and the team plans fixes. Check each statement that is true.  *(5 points)*

- [ ] A. A small segment yields a wide confidence interval on its accuracy.
- [ ] B. Group-robust objectives minimise overall accuracy.
- [ ] C. Underrepresentation in the training data is a plausible cause of a weak segment.
- [ ] D. Reweighting or oversampling an underrepresented segment is a standard mitigation.
- [ ] E. Group-robust objectives minimise the loss of the worst group rather than the average loss.

**7.** A report says: "the model is 90 percent confident, so it is 90 percent accurate." Check each statement that is true.  *(5 points)*

- [ ] A. Accuracy is the fraction of predictions that are correct.
- [ ] B. Confidence and accuracy are the same quantity.
- [ ] C. Confidence is the probability the model assigns to its prediction.
- [ ] D. Calibration is the match between stated confidence and the observed frequency of being correct.
- [ ] E. If 90 percent confident predictions are right 70 percent of the time, the model is well calibrated.

**8.** Match each situation to a missingness type. Check each statement that is true.  *(5 points)*

- [ ] A. Respondents with low recorded education skip an income question more often, which is MAR.
- [ ] B. Imputing the column mean is a test that distinguishes MNAR from MAR.
- [ ] C. MCAR means missingness depends on the value that is missing.
- [ ] D. A sensor drops readings at random because of power glitches unrelated to the readings, which is MCAR.
- [ ] E. Patients with the worst symptoms miss follow-up so their symptom score is missing, which is MAR.

**9.** A face-matching system searches a database of 2,000,000 people. It declares a match for a person who is not the source with probability 1 in 10,000. A prosecutor says: "The chance this match is a coincidence is 1 in 10,000, so there is a 99.99% chance he is the source." Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. The 1 in 10,000 rate is the false positive rate, so it is also the false discovery proportion among declared matches.
- [ ] B. Independent evidence about the person raises the prior odds, and posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] C. A match found by testing one suspect already singled out by other evidence carries the same weight as a match found by trawling a large database.
- [ ] D. Searching a large database raises the expected number of coincidental matches.
- [ ] E. The prosecutor transposed the conditional: P(match | not the source) is not P(not the source | match).

**10.** A team sets an alert at the mean plus a multiple of the standard deviation, and a reviewer questions the quoted false-alarm rate. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. Chebyshev's inequality bounds tail probability for distributions with finite variance, whatever their shape.
- [ ] B. At 3 standard deviations the Chebyshev bound is 1/9, which is looser than the normal tail figure.
- [ ] C. A quantile-quantile plot compares the data's quantiles with a reference distribution and can show whether the tails are heavier than normal.
- [ ] D. The Cauchy distribution has a finite mean, so sample averages settle down as the sample grows.
- [ ] E. A "six-sigma" failure rate computed from the normal curve stays valid when the real distribution is heavy-tailed.

**11.** A pipeline joins an orders table to a customer table. The orders table has 50,000 rows and the joined table has 47,500, and the dropped rows belong to one region. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Row reconciliation compares counts by source, stage and group before and after a join against what is expected.
- [ ] B. Checks on null values, types and ranges can pass on the remaining rows even though rows are missing.
- [ ] C. If 5% of rows are lost, the statistics computed afterward are within 5% of their true values.
- [ ] D. A check repeated within each group can reveal a loss that the overall total hides.
- [ ] E. An anti-join lists the records in one table that have no matching key in the other, which reveals dropped keys.

**12.** Consider the sample mean of n independent, identically distributed observations from a right-skewed population with finite variance, such as task completion times. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The sampling distribution of the mean is the distribution of the sample mean across repeated samples of size n.
- [ ] B. Strong positive correlation among observations enlarges the effective sample size.
- [ ] C. The central limit theorem says the sampling distribution of the mean is normal at small n as well as at large n.
- [ ] D. The central limit theorem says a histogram of the individual observations becomes bell-shaped as n grows.
- [ ] E. The skewness of the sample mean grows as n grows.

**13.** Polynomial regressions of increasing degree are fit to 40 training points, and errors are measured on the training points and on held-out points. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Underfitting shows as low training error and high held-out error.
- [ ] B. An overly flexible model has high bias and low variance.
- [ ] C. Regularization increases the flexibility of a model by adding more parameters.
- [ ] D. Training error is a dependable estimate of generalization error.
- [ ] E. Overfitting shows as low training error together with high held-out error.

**14.** An analyst says that labels came from reviewers who judged applicants from one neighbourhood more harshly, so the problem is sampling bias. Check each statement that is true.  *(5 points)*

- [ ] A. The problem described is label bias.
- [ ] B. Sampling bias concerns who ends up in the data, not how labels were assigned.
- [ ] C. Resampling to match population group proportions fixes label bias.
- [ ] D. Collecting more rows from the same reviewers removes the problem.
- [ ] E. Label bias can exist when the sample matches the target population in group proportions.

**15.** A fraud model flags 100 transactions and 40 are fraud. Of 80 fraudulent transactions in total, it flagged those 40, so 40/100 is 0.4 and 40/80 is 0.5. Check each statement that is true.  *(5 points)*

- [ ] A. The 0.5 figure is the specificity.
- [ ] B. The 0.4 figure is the precision.
- [ ] C. The 0.4 figure is the recall.
- [ ] D. Legitimate transactions that were flagged are false positives.
- [ ] E. The 0.5 figure is the recall, also called sensitivity.

**16.** A medical imaging model trained on one hospital's scanners is tested on a different hospital's. Check each statement that is true.  *(5 points)*

- [ ] A. An out-of-distribution input is drawn from a distribution different from the training data.
- [ ] B. A held-out test set from the same source as training is out-of-distribution.
- [ ] C. A model's softmax confidence is low on out-of-distribution inputs.
- [ ] D. Out-of-distribution detection aims to flag inputs unlike the training data.
- [ ] E. In-distribution inputs come from the same distribution as the training data.

**17.** Four requests are sent to an analyst: why was this one applicant denied; which inputs matter most across the whole portfolio; what does the average effect of income look like across many rows; and does the answer for one applicant match the portfolio ranking. Check each statement that is true.  *(5 points)*

- [ ] A. Asking which inputs matter most across the whole portfolio asks for a global explanation.
- [ ] B. A single-prediction attribution is a global explanation.
- [ ] C. A local explanation for one case is guaranteed to match the global ranking of inputs.
- [ ] D. Asking why one applicant was denied asks for a local explanation.
- [ ] E. A partial dependence plot averaged over many rows is a local explanation.

**18.** A company randomly sends half of its customers a reminder email about renewing and sends nothing to the others. To measure the effect of the email it looks only at customers who opened the email and compares their renewal rate with that of customers who were sent nothing. The email group renewed more. The company concludes that the email raises renewals. Check each statement that describes a possible problem for the conclusion.  *(5 points)*

- [ ] A. People who open emails may be more engaged customers who would have renewed anyway.
- [ ] B. The customers were assigned to get the email by chance.
- [ ] C. Customers who disliked the email may have deleted it unopened, so they are left out of the email group.
- [ ] D. Customers can renew without opening the email.
- [ ] E. Renewals were counted for both groups.

**19.** A manager says: "verify the model works for patients" and wants evidence the model serves its purpose on real patients. Check each statement that is true.  *(5 points)*

- [ ] A. Checking the model against its written specification in a test is verification.
- [ ] B. Validation asks whether the right system was built, meaning it serves its real purpose.
- [ ] C. Verification asks whether the system was built right, meaning it meets its specification.
- [ ] D. Evidence on real patients is validation.
- [ ] E. A unit test that the code computes a specified formula is validation.

**20.** A dataset is shared with a colleague and no documentation. Check each statement that is true.  *(5 points)*

- [ ] A. A datasheet for datasets documents motivation, composition, collection process and recommended uses.
- [ ] B. Recording known gaps and intended use helps downstream users judge fit.
- [ ] C. A data card summarises a dataset's provenance, contents and known limitations.
- [ ] D. A model card documents a dataset's collection process.
- [ ] E. A datasheet should state consent and licensing when they are known.
