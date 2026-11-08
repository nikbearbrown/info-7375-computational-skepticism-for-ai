# INFO 7375 Computational Skepticism for AI: practice exam 02: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A classifier for a rare event is scored at three thresholds, and a missed positive costs far more than a false alarm. Which statements use the metric terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Accuracy is a dependable summary when the positive class is rare.
- [ ] B. Recall is the share of actual positives that the classifier flags.
- [ ] C. F1 is the harmonic mean of precision and recall.
- [ ] D. Raising the decision threshold tends to raise precision and lower recall.
- [ ] E. Precision is the share of flagged cases that are truly positive.

**Key:** A=F B=T C=T D=T E=T  |  `MA-5.1`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Precision, recall, F1, accuracy, threshold

- A (false): With a rare class, accuracy is dominated by the majority class and can be high for a useless model.
- B (true): Recall = true positives / (true positives + false negatives).
- C (true): F1 combines the two into one number that is low when either is low.
- D (true): A stricter cutoff flags fewer cases, mostly confident ones, and misses more positives.
- E (true): Precision = true positives / (true positives + false positives).

**2.** Two groups have different shares of people who truly have the positive outcome, and a classifier is imperfect. Check each statement that is true.  *(5 points)*

- [ ] A. A base-rate difference is evidence that the model is biased.
- [ ] B. With differing base rates and an imperfect classifier, calibration within groups and equalized odds generally do not hold together.
- [ ] C. The base rate is the proportion of a group that has the positive outcome.
- [ ] D. The base rate is the same as a group's false positive rate.
- [ ] E. A base-rate difference in the data can itself reflect historical bias.

**Key:** A=F B=T C=T D=F E=T  |  `MA-jargon.60`  |  *Jargon test: bias and fairness*  |  source: Base-rate difference

- A (false): A base-rate difference describes the data; the model can still be accurate.
- B (true): Known results show these criteria are in tension under unequal base rates.
- C (true): It is the prevalence of the outcome in the group.
- D (false): False positive rate is a model error rate, not outcome prevalence.
- E (true): Past inequity can shape which outcomes appear in the records.

**3.** An analyst prompts: "Tell me how accurate and how confident the model's 70% scores are." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Report discrimination as AUC and calibration as expected calibration error, as separate quantities.
- [ ] B. Use the word accuracy for the share of predictions that are correct.
- [ ] C. Report AUC to show the scores are calibrated.
- [ ] D. Call the bootstrap interval for accuracy a posterior.
- [ ] E. Report calibration of the predicted probabilities with a reliability diagram.

**Key:** A=T B=T C=F D=F E=T  |  `MA-jargon.12`  |  *Jargon test: probability and confidence*  |  source: Rewrite a vague probability prompt

- A (true): The two properties are distinct and need distinct metrics.
- B (true): Accuracy is the proportion correct.
- C (false): AUC is discrimination, not calibration.
- D (false): A bootstrap interval is a confidence interval, not a posterior.
- E (true): That names the property of probability values the prompt is after.

**4.** Fraud rises from 1% to 3% of transactions, and fraudulent transactions look the same as before. Check each statement that is true.  *(5 points)*

- [ ] A. P(y) has changed.
- [ ] B. The decision threshold may need adjusting because the class prior changed.
- [ ] C. This is label shift, also called prior shift.
- [ ] D. P(x | y) is unchanged.
- [ ] E. This is concept drift.

**Key:** A=T B=T C=T D=T E=F  |  `MA-jargon.35`  |  *Jargon test: robustness and distribution shift*  |  source: Label (prior) shift

- A (true): The proportion of fraud moved.
- B (true): The optimal threshold depends on the prior.
- C (true): The class prior changed.
- D (true): Fraud looks the same as before.
- E (false): Concept drift would need P(y | x) to change.

**5.** Two explanation methods are compared. Clinicians rate one method's heat maps as sensible, while a test shows the other method tracks the classifier's behaviour more closely. Check each statement that is true.  *(5 points)*

- [ ] A. Clinician ratings of how sensible heat maps look measure faithfulness.
- [ ] B. Faithfulness is how accurately an explanation reflects what the model actually does.
- [ ] C. A plausible explanation is therefore faithful.
- [ ] D. Plausibility is how closely an explanation matches the model's computation.
- [ ] E. An explanation can be faithful and implausible if the model relies on a spurious cue.

**Key:** A=F B=T C=F D=F E=T  |  `MA-jargon.48`  |  *Jargon test: explainability*  |  source: Faithfulness vs plausibility

- A (false): They measure plausibility.
- B (true): Faithfulness is about agreement with the model's behaviour.
- C (false): Looking sensible to a reader says nothing about matching the model.
- D (false): That describes faithfulness; plausibility is how convincing the explanation looks to a person.
- E (true): The explanation then points at the cue, which looks odd but is true to the model.

**6.** A support-ticket classifier is 93% accurate overall but 60% accurate on a small segment, and the team plans fixes. Check each statement that is true.  *(5 points)*

- [ ] A. A small segment yields a wide confidence interval on its accuracy.
- [ ] B. Group-robust objectives minimise overall accuracy.
- [ ] C. Underrepresentation in the training data is a plausible cause of a weak segment.
- [ ] D. Reweighting or oversampling an underrepresented segment is a standard mitigation.
- [ ] E. Group-robust objectives minimise the loss of the worst group rather than the average loss.

**Key:** A=T B=F C=T D=T E=T  |  `MA-ch04.40`  |  *None*  |  source: Group-robust mitigation

- A (true): Few samples give an uncertain estimate.
- B (false): They minimise the worst-group loss.
- C (true): Models fit common groups best.
- D (true): It raises the segment's influence on training.
- E (true): They target the worst-affected group.

**7.** A report says: "the model is 90 percent confident, so it is 90 percent accurate." Check each statement that is true.  *(5 points)*

- [ ] A. Accuracy is the fraction of predictions that are correct.
- [ ] B. Confidence and accuracy are the same quantity.
- [ ] C. Confidence is the probability the model assigns to its prediction.
- [ ] D. Calibration is the match between stated confidence and the observed frequency of being correct.
- [ ] E. If 90 percent confident predictions are right 70 percent of the time, the model is well calibrated.

**Key:** A=T B=F C=T D=T E=F  |  `MA-jargon.69`  |  *Jargon test: wrong word, right word*  |  source: Confidence vs accuracy vs calibration

- A (true): Accuracy is an observed rate.
- B (false): One is a stated probability and the other an observed rate.
- C (true): Confidence is the model's stated probability.
- D (true): A calibrated 90 percent confidence is right about 90 percent of the time.
- E (false): That model is overconfident, so it is poorly calibrated.

**8.** Match each situation to a missingness type. Check each statement that is true.  *(5 points)*

- [ ] A. Respondents with low recorded education skip an income question more often, which is MAR.
- [ ] B. Imputing the column mean is a test that distinguishes MNAR from MAR.
- [ ] C. MCAR means missingness depends on the value that is missing.
- [ ] D. A sensor drops readings at random because of power glitches unrelated to the readings, which is MCAR.
- [ ] E. Patients with the worst symptoms miss follow-up so their symptom score is missing, which is MAR.

**Key:** A=T B=F C=F D=T E=F  |  `MA-jargon.19`  |  *Jargon test: data validation and provenance*  |  source: Missingness situations

- A (true): Missingness depends on a recorded variable.
- B (false): Imputation is a repair, not a diagnostic of the mechanism.
- C (false): That describes MNAR.
- D (true): Unrelated causes give missing completely at random.
- E (false): Missingness depends on the unobserved score, so it is MNAR.

**9.** A face-matching system searches a database of 2,000,000 people. It declares a match for a person who is not the source with probability 1 in 10,000. A prosecutor says: "The chance this match is a coincidence is 1 in 10,000, so there is a 99.99% chance he is the source." Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. The 1 in 10,000 rate is the false positive rate, so it is also the false discovery proportion among declared matches.
- [ ] B. Independent evidence about the person raises the prior odds, and posterior odds equal prior odds multiplied by the likelihood ratio.
- [ ] C. A match found by testing one suspect already singled out by other evidence carries the same weight as a match found by trawling a large database.
- [ ] D. Searching a large database raises the expected number of coincidental matches.
- [ ] E. The prosecutor transposed the conditional: P(match | not the source) is not P(not the source | match).

**Key:** A=F B=T C=F D=T E=T  |  `MA-1.7`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Prosecutor's fallacy, false positive rate versus false discovery proportion

- A (false): The false discovery proportion is the share of matches that are wrong, which also depends on how many non-sources are tested.
- B (true): Independent evidence changes the prior odds before the match is weighed.
- C (false): Trawling produces many coincidental matches, so a match from a trawl carries a lower posterior probability.
- D (true): The count of false matches grows with the number of non-source people tested.
- E (true): The 1 in 10,000 is a false positive rate; the prosecutor read it as the reverse conditional.

**10.** A team sets an alert at the mean plus a multiple of the standard deviation, and a reviewer questions the quoted false-alarm rate. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. Chebyshev's inequality bounds tail probability for distributions with finite variance, whatever their shape.
- [ ] B. At 3 standard deviations the Chebyshev bound is 1/9, which is looser than the normal tail figure.
- [ ] C. A quantile-quantile plot compares the data's quantiles with a reference distribution and can show whether the tails are heavier than normal.
- [ ] D. The Cauchy distribution has a finite mean, so sample averages settle down as the sample grows.
- [ ] E. A "six-sigma" failure rate computed from the normal curve stays valid when the real distribution is heavy-tailed.

**Key:** A=T B=T C=T D=F E=F  |  `MA-2.5`  |  *2. Random variables and distributions*  |  source: Chebyshev's inequality, tail risk, quantile-quantile plot, Cauchy

- A (true): The bound P(|X − μ| ≥ kσ) ≤ 1/k² needs only a finite variance.
- B (true): The normal puts about 0.27% beyond 3 standard deviations, far under 11%.
- C (true): Points bending away from the line in the ends signal tail shape that differs from the reference.
- D (false): The Cauchy has no finite mean, and the average of Cauchy observations is as spread out as one observation.
- E (false): The tiny figure depends on the normal shape; heavy tails put far more probability at extreme distances.

**11.** A pipeline joins an orders table to a customer table. The orders table has 50,000 rows and the joined table has 47,500, and the dropped rows belong to one region. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Row reconciliation compares counts by source, stage and group before and after a join against what is expected.
- [ ] B. Checks on null values, types and ranges can pass on the remaining rows even though rows are missing.
- [ ] C. If 5% of rows are lost, the statistics computed afterward are within 5% of their true values.
- [ ] D. A check repeated within each group can reveal a loss that the overall total hides.
- [ ] E. An anti-join lists the records in one table that have no matching key in the other, which reveals dropped keys.

**Key:** A=T B=T C=F D=T E=T  |  `MA-4.4`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Row reconciliation, anti-join, stratified check, silent data loss

- A (true): A mismatch in counts exposes rows that were dropped.
- B (true): Checks on present rows leave no trace of rows that never arrived.
- C (false): Lost rows can differ systematically from the rest, so a statistic can shift by much more than the share lost.
- D (true): A stratified check shows that one region lost a quarter of its rows.
- E (true): An anti-join returns the unmatched rows.

**12.** Consider the sample mean of n independent, identically distributed observations from a right-skewed population with finite variance, such as task completion times. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The sampling distribution of the mean is the distribution of the sample mean across repeated samples of size n.
- [ ] B. Strong positive correlation among observations enlarges the effective sample size.
- [ ] C. The central limit theorem says the sampling distribution of the mean is normal at small n as well as at large n.
- [ ] D. The central limit theorem says a histogram of the individual observations becomes bell-shaped as n grows.
- [ ] E. The skewness of the sample mean grows as n grows.

**Key:** A=T B=F C=F D=F E=F  |  `MA-3.6`  |  *3. Sampling, the central limit theorem and inference*  |  source: Sampling distribution, central limit theorem, effective sample size

- A (true): A sampling distribution describes a statistic, not the raw data.
- B (false): Correlated observations carry less information, so the effective sample size is smaller than n.
- C (false): The theorem is a limit statement; the approximation improves as n grows, and skewed data can need a large n.
- D (false): The raw data keep the population's shape; the distribution of the sample mean is what approaches normal.
- E (false): Skewness of the mean shrinks toward 0 in proportion to 1 over the square root of n.

**13.** Polynomial regressions of increasing degree are fit to 40 training points, and errors are measured on the training points and on held-out points. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Underfitting shows as low training error and high held-out error.
- [ ] B. An overly flexible model has high bias and low variance.
- [ ] C. Regularization increases the flexibility of a model by adding more parameters.
- [ ] D. Training error is a dependable estimate of generalization error.
- [ ] E. Overfitting shows as low training error together with high held-out error.

**Key:** A=F B=F C=F D=F E=T  |  `MA-5.2`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Overfitting, underfitting, regularization, training versus generalization error

- A (false): Underfitting shows high error on both sets with a small gap between them.
- B (false): Overly flexible models have low bias and high variance.
- C (false): Regularization penalizes large coefficients to limit the effective flexibility.
- D (false): Training error falls as flexibility rises and says little about performance on new data.
- E (true): The model has fit noise in the training set.

**14.** An analyst says that labels came from reviewers who judged applicants from one neighbourhood more harshly, so the problem is sampling bias. Check each statement that is true.  *(5 points)*

- [ ] A. The problem described is label bias.
- [ ] B. Sampling bias concerns who ends up in the data, not how labels were assigned.
- [ ] C. Resampling to match population group proportions fixes label bias.
- [ ] D. Collecting more rows from the same reviewers removes the problem.
- [ ] E. Label bias can exist when the sample matches the target population in group proportions.

**Key:** A=T B=T C=F D=F E=T  |  `MA-jargon.54`  |  *Jargon test: bias and fairness*  |  source: Label bias vs sampling bias

- A (true): The target labels carry systematic reviewer error.
- B (true): Sampling bias is about the makeup of the sample.
- C (false): Resampling changes group makeup but leaves the label errors in place.
- D (false): More rows with the same biased labels repeat the bias.
- E (true): The two problems are independent of each other.

**15.** A fraud model flags 100 transactions and 40 are fraud. Of 80 fraudulent transactions in total, it flagged those 40, so 40/100 is 0.4 and 40/80 is 0.5. Check each statement that is true.  *(5 points)*

- [ ] A. The 0.5 figure is the specificity.
- [ ] B. The 0.4 figure is the precision.
- [ ] C. The 0.4 figure is the recall.
- [ ] D. Legitimate transactions that were flagged are false positives.
- [ ] E. The 0.5 figure is the recall, also called sensitivity.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.6`  |  *Jargon test: probability and confidence*  |  source: Match the metric to the situation

- A (false): Specificity concerns actual negatives.
- B (true): Of the flagged cases, 40 percent are truly fraud.
- C (false): Recall divides by the actual positives, not the flagged ones.
- D (true): A false positive is a negative case predicted positive.
- E (true): Of the actual frauds, half were found.

**16.** A medical imaging model trained on one hospital's scanners is tested on a different hospital's. Check each statement that is true.  *(5 points)*

- [ ] A. An out-of-distribution input is drawn from a distribution different from the training data.
- [ ] B. A held-out test set from the same source as training is out-of-distribution.
- [ ] C. A model's softmax confidence is low on out-of-distribution inputs.
- [ ] D. Out-of-distribution detection aims to flag inputs unlike the training data.
- [ ] E. In-distribution inputs come from the same distribution as the training data.

**Key:** A=T B=F C=F D=T E=T  |  `MA-jargon.27`  |  *Jargon test: robustness and distribution shift*  |  source: In-distribution vs out-of-distribution

- A (true): OOD inputs fall outside what training covered.
- B (false): Same-source data is in-distribution.
- C (false): Confidence can stay high on inputs unlike the training data.
- D (true): Detection is how such inputs are caught.
- E (true): That is the meaning of in-distribution.

**17.** Four requests are sent to an analyst: why was this one applicant denied; which inputs matter most across the whole portfolio; what does the average effect of income look like across many rows; and does the answer for one applicant match the portfolio ranking. Check each statement that is true.  *(5 points)*

- [ ] A. Asking which inputs matter most across the whole portfolio asks for a global explanation.
- [ ] B. A single-prediction attribution is a global explanation.
- [ ] C. A local explanation for one case is guaranteed to match the global ranking of inputs.
- [ ] D. Asking why one applicant was denied asks for a local explanation.
- [ ] E. A partial dependence plot averaged over many rows is a local explanation.

**Key:** A=T B=F C=F D=T E=F  |  `MA-jargon.43`  |  *Jargon test: explainability*  |  source: Local vs global explanation

- A (true): A global explanation describes behaviour in aggregate.
- B (false): An attribution for one prediction is local.
- C (false): Local and global explanations can disagree, since one case need not resemble the average.
- D (true): A local explanation covers a single prediction.
- E (false): Averaging over many rows gives a global view of an input's effect.

**18.** A company randomly sends half of its customers a reminder email about renewing and sends nothing to the others. To measure the effect of the email it looks only at customers who opened the email and compares their renewal rate with that of customers who were sent nothing. The email group renewed more. The company concludes that the email raises renewals. Check each statement that describes a possible problem for the conclusion.  *(5 points)*

- [ ] A. People who open emails may be more engaged customers who would have renewed anyway.
- [ ] B. The customers were assigned to get the email by chance.
- [ ] C. Customers who disliked the email may have deleted it unopened, so they are left out of the email group.
- [ ] D. Customers can renew without opening the email.
- [ ] E. Renewals were counted for both groups.

**Key:** A=T B=F C=T D=F E=F  |  `MA-ch03.49`  |  *None*  |  source: Hidden assumptions that hide in plain sight

- A (true): Opening is chosen by the customer, so the openers differ from the rest.
- B (false): Random assignment is a strength; the problem is the comparison made afterwards.
- C (true): Dropping the people who reacted badly makes the email group look better than the email deserves.
- D (false): That is true of both groups and is not a problem for the comparison.
- E (false): Counting both groups is needed for the comparison.

**19.** A manager says: "verify the model works for patients" and wants evidence the model serves its purpose on real patients. Check each statement that is true.  *(5 points)*

- [ ] A. Checking the model against its written specification in a test is verification.
- [ ] B. Validation asks whether the right system was built, meaning it serves its real purpose.
- [ ] C. Verification asks whether the system was built right, meaning it meets its specification.
- [ ] D. Evidence on real patients is validation.
- [ ] E. A unit test that the code computes a specified formula is validation.

**Key:** A=T B=T C=T D=T E=F  |  `MA-jargon.72`  |  *Jargon test: wrong word, right word*  |  source: Verification vs validation

- A (true): Verification confirms the build meets its spec.
- B (true): Validation checks fit to the real need.
- C (true): Verification checks against the specification.
- D (true): It tests the purpose in the real setting.
- E (false): That is verification against a specification.

**20.** A dataset is shared with a colleague and no documentation. Check each statement that is true.  *(5 points)*

- [ ] A. A datasheet for datasets documents motivation, composition, collection process and recommended uses.
- [ ] B. Recording known gaps and intended use helps downstream users judge fit.
- [ ] C. A data card summarises a dataset's provenance, contents and known limitations.
- [ ] D. A model card documents a dataset's collection process.
- [ ] E. A datasheet should state consent and licensing when they are known.

**Key:** A=T B=T C=T D=F E=T  |  `MA-jargon.23`  |  *Jargon test: data validation and provenance*  |  source: Data card and datasheet

- A (true): It is a structured description of the dataset.
- B (true): Documentation lets users decide whether the data suits their task.
- C (true): It tells users what the data is and where it falls short.
- D (false): A model card documents a model.
- E (true): Those facts affect permitted use.
