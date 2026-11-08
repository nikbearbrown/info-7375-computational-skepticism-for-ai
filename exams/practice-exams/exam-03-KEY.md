# INFO 7375 Computational Skepticism for AI: practice exam 03: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A survey records age for each respondent and asks for income, which some respondents leave blank. Which statements use the missingness terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Missing not at random (MNAR) means missingness depends on the unobserved value itself, such as higher earners skipping because of income.
- [ ] B. Whether income is missing not at random can be confirmed from the observed values alone.
- [ ] C. Higher earners skipping the income question because of their income is missing at random.
- [ ] D. Missing completely at random (MCAR) means missingness is unrelated to the observed variables and to the unobserved values.
- [ ] E. Missing at random (MAR) means missingness depends on observed variables, such as older respondents skipping more often, and not on the missing value itself.

**Key:** A=T B=F C=F D=T E=T  |  `MA-4.1`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: MCAR, MAR, MNAR

- A (true): The reason for the gap is the very value that is absent.
- B (false): The observed data cannot reveal dependence on unobserved values; it takes outside knowledge or assumptions.
- C (false): Missingness driven by the value itself is MNAR, not MAR.
- D (true): MCAR is the least problematic missingness mechanism.
- E (true): Conditioning on the observed variable removes the dependence.

**2.** A user prompts an AI: "The model got worse because the data changed." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Call a random perturbation an adversarial example.
- [ ] B. State whether P(x) changed, which is covariate shift, or P(y | x) changed, which is concept drift.
- [ ] C. Report accuracy on the training set to show robustness.
- [ ] D. Describe the held-out test as out-of-time if it is a random sample.
- [ ] E. Call it covariate shift if the class proportions changed.

**Key:** A=F B=T C=F D=F E=F  |  `MA-jargon.34`  |  *Jargon test: robustness and distribution shift*  |  source: Rewrite a vague shift prompt

- A (false): Adversarial means deliberately targeted.
- B (true): That separates the two kinds of change.
- C (false): Training accuracy does not test robustness.
- D (false): An out-of-time split orders data by time.
- E (false): A change in class proportions is label shift.

**3.** A hiring model is trained on twenty years of accurate, well-sampled records that show few women hired into engineering. Check each statement that is true.  *(5 points)*

- [ ] A. Collecting a larger random sample removes historical bias.
- [ ] B. Historical bias can be present when sampling and measurement are sound.
- [ ] C. Historical bias is a type of measurement bias because the records are inaccurate.
- [ ] D. Historical bias requires that the records contain data-entry errors.
- [ ] E. This is historical bias: accurate data that reflect a world containing past inequity.

**Key:** A=F B=T C=F D=F E=T  |  `MA-jargon.55`  |  *Jargon test: bias and fairness*  |  source: Historical bias

- A (false): A bigger faithful sample reproduces the same inequity.
- B (true): It does not depend on a flaw in data collection.
- C (false): The records are accurate; the bias lies in the world they describe.
- D (false): Errors are not needed; accurate records can carry it.
- E (true): Historical bias comes from the world, not from collection errors.

**4.** A fraud team says its transaction classifier "catches 90% of fraud" and "wrongly flags 4% of legitimate transactions". Which statements name these quantities correctly? Check each statement that is true.  *(5 points)*

- [ ] A. For a fixed sensitivity and false positive rate, the prevalence (base rate) of fraud leaves the positive predictive value unchanged.
- [ ] B. "Catches 90% of fraud" is the sensitivity of the classifier, also called recall or the true positive rate.
- [ ] C. Sensitivity and positive predictive value are two names for one quantity.
- [ ] D. "Wrongly flags 4% of legitimate transactions" is the false positive rate, which equals 1 minus the specificity.
- [ ] E. The probability that a flagged transaction is fraudulent is the sensitivity.

**Key:** A=F B=T C=F D=T E=F  |  `MA-1.1`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Sensitivity, false positive rate, positive predictive value, prevalence

- A (false): The positive predictive value rises with prevalence even when the two error rates stay fixed.
- B (true): Sensitivity is the share of actual positives that the classifier flags.
- C (false): They condition on different events: sensitivity on actual positives, positive predictive value on flagged cases.
- D (true): The false positive rate is the share of actual negatives flagged, the complement of specificity.
- E (false): That probability is the positive predictive value (precision); sensitivity conditions on fraud, not on the flag.

**5.** A data scientist has 60 examples and 5,000 pure-noise features. They pick the 20 features most correlated with the label using all 60 examples, run 5-fold cross-validation on those features and report 92% accuracy. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Selecting features using the labels of the full dataset before cross-validation is leakage.
- [ ] B. Fitting a label-dependent step such as target encoding on the full data before splitting is also leakage.
- [ ] C. Data leakage means information from the held-out data influences model training or selection.
- [ ] D. With noise features and fair-coin labels, an honest evaluation should show accuracy near chance.
- [ ] E. Using more folds removes the leakage from the feature selection done before the split.

**Key:** A=T B=T C=T D=T E=F  |  `MA-5.3`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Data leakage, cross-validation, target encoding

- A (true): The held-out labels shaped which features were chosen.
- B (true): Any step that sees held-out labels contaminates the estimate; such steps belong inside each training fold.
- C (true): Leakage makes the held-out estimate optimistic.
- D (true): A model has no signal to learn, so honest accuracy is about 50%.
- E (false): The selection already used every label, so the number of folds does not change the leak.

**6.** A model scores very high because some test rows are also in the training set, and a separate benchmark score is high because its questions appeared in the pretraining text. Check each statement that is true.  *(5 points)*

- [ ] A. Benchmark contamination is test items appearing in a model's training corpus.
- [ ] B. Data leakage is information from outside the training data, or from the target, getting into training so evaluation is inflated.
- [ ] C. Contamination is a type of missingness.
- [ ] D. A feature derived from the label is a source of leakage.
- [ ] E. Leakage describes a model that memorises noise in the training data.

**Key:** A=T B=T C=F D=T E=F  |  `MA-jargon.16`  |  *Jargon test: data validation and provenance*  |  source: Leakage vs contamination

- A (true): The benchmark was seen before it was tested.
- B (true): Leakage breaks the separation between training and evaluation.
- C (false): Contamination concerns overlap with training data, not absent values.
- D (true): It encodes the answer the model is meant to predict.
- E (false): That is overfitting.

**7.** A colleague says: "SHAP is the unique attribution method with efficiency, symmetry, dummy and additivity, so it is the correct way to explain a model." Check each statement that is true.  *(5 points)*

- [ ] A. For a fixed value function, the Shapley value is the unique allocation satisfying efficiency, symmetry, dummy and additivity.
- [ ] B. Satisfying the properties makes sampling estimates of Shapley values free of estimation error.
- [ ] C. The value function, meaning how a subset of inputs is valued, is a different choice from the allocation rule.
- [ ] D. The four properties also fix the value function, so the choice between marginal and conditional valuation is already settled.
- [ ] E. The properties show that the attribution answers the question a given user wants answered.

**Key:** A=T B=F C=T D=F E=F  |  `MA-ch05.6`  |  *None*  |  source: Value function versus allocation rule

- A (true): This is the uniqueness result for the allocation rule.
- B (false): Sampled estimates have variance even though the target quantity is well defined.
- C (true): Marginal and conditional value functions give different Shapley values under the same rule.
- D (false): The value function is a separate modeling choice that the axioms do not determine.
- E (false): Uniqueness of the rule says nothing about whether the explanation fits the purpose.

**8.** A model answers each of 20 test prompts correctly with probability 0.8, independently, and the number correct is modeled as binomial. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. The binomial variance is np, which equals its mean.
- [ ] B. Overdispersion means the observed variance is smaller than the model variance.
- [ ] C. Positively correlated trials, such as near-duplicate prompts, cause overdispersion: the count varies more than the binomial variance says.
- [ ] D. A binomial count is the number of successes in a fixed number of independent trials that share one success probability.
- [ ] E. Overdispersion and underdispersion both describe the sample mean differing from the population mean.

**Key:** A=F B=F C=T D=T E=F  |  `MA-2.3`  |  *2. Random variables and distributions*  |  source: Binomial distribution, independence, overdispersion

- A (false): The binomial variance is np(1 − p); equal mean and variance is a property of the Poisson.
- B (false): That is underdispersion; overdispersion is larger observed variance.
- C (true): Overdispersion means observed variance exceeds the model variance.
- D (true): These are the defining conditions of the binomial model.
- E (false): They describe variance relative to the model, not a difference in means.

**9.** A heat map highlights regions of a chest X-ray that drove a classifier's output. Check each statement that is true.  *(5 points)*

- [ ] A. A saliency map is a counterfactual explanation.
- [ ] B. A highlighted region shows where the disease is located in the patient.
- [ ] C. An attribution method assigns each input feature a share of a prediction.
- [ ] D. Shapley values are one kind of attribution method.
- [ ] E. A saliency map shows which input regions most affect the model's output score.

**Key:** A=F B=F C=T D=T E=T  |  `MA-jargon.46`  |  *Jargon test: explainability*  |  source: Saliency and attribution

- A (false): A counterfactual describes an altered input that flips the outcome; a saliency map scores existing inputs.
- B (false): The map describes the model's reliance, not the patient's biology.
- C (true): Attribution divides a prediction among inputs.
- D (true): Shapley values attribute a prediction to features using a game-theoretic definition.
- E (true): Saliency is a sensitivity of the output to the input.

**10.** A prompt says: "make the model robust against attacks and against new data." Check each statement that is true.  *(5 points)*

- [ ] A. Distribution shift means test inputs come from a different distribution than the training data.
- [ ] B. Robustness to distribution shift is tested with adversarial examples.
- [ ] C. Adversarial robustness is measured on held-out data from the same distribution.
- [ ] D. Adversarial robustness concerns small deliberate input perturbations designed to cause errors.
- [ ] E. An adversarial example is naturally occurring noise in the data.

**Key:** A=T B=F C=F D=T E=F  |  `MA-jargon.75`  |  *Jargon test: wrong word, right word*  |  source: Adversarial robustness vs distribution shift

- A (true): It is a change in the data-generating distribution.
- B (false): It is tested with data from a shifted distribution.
- C (false): Same-distribution held-out data tests ordinary generalization.
- D (true): Adversarial examples are crafted to fool the model.
- E (false): It is a deliberate perturbation.

**11.** A vendor says a rare-disease test is "99% accurate", so a positive result means the patient is almost surely ill. Check each statement that is true.  *(5 points)*

- [ ] A. Positive predictive value is unaffected by the base rate.
- [ ] B. Sensitivity and specificity are defined by prevalence.
- [ ] C. Ignoring the base rate is called overfitting.
- [ ] D. With a low base rate, many positive results can be false positives even for a sensitive test.
- [ ] E. The base rate is the prevalence of the condition in the population tested.

**Key:** A=F B=F C=F D=T E=T  |  `MA-jargon.7`  |  *Jargon test: probability and confidence*  |  source: Base rate

- A (false): Positive predictive value falls as prevalence falls.
- B (false): They are properties of the test given the condition and do not depend on prevalence.
- C (false): Ignoring the base rate is the base rate fallacy.
- D (true): Few true cases means false positives from the large healthy group can dominate.
- E (true): Base rate means how common the condition is before testing.

**12.** A tutoring app invites its 1.25 million users to a satisfaction survey. A total of 50,000 respond and 92% of respondents say they are satisfied. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Respondents choosing for themselves whether to answer is self-selection, a source of nonresponse bias.
- [ ] B. A larger number of respondents reduces random error but leaves selection bias in place.
- [ ] C. The standard error quantifies the systematic bias that comes from who chose to respond.
- [ ] D. A large volunteer sample is a probability sample because it is large.
- [ ] E. Selection bias and measurement bias are two names for the same problem.

**Key:** A=T B=T C=F D=F E=F  |  `MA-3.7`  |  *3. Sampling, the central limit theorem and inference*  |  source: Nonresponse bias, self-selection, standard error versus bias

- A (true): Those who answer can differ systematically from those who do not.
- B (true): Bias depends on the response mechanism, not on the count.
- C (false): The standard error captures chance variation and cannot detect a systematic difference between responders and non-responders.
- D (false): A probability sample needs known selection chances, and size does not supply them.
- E (false): Selection bias concerns who ends up in the data; measurement bias concerns errors in how values are recorded.

**13.** An analyst describes the shape of a response-time variable and the best plot for it. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Standard deviation and variance are measures of central tendency.
- [ ] B. The median is the middle value of the sorted data, while the mean is the balance point of the data.
- [ ] C. In a right-skewed distribution the mean exceeds the median.
- [ ] D. The mode is another name for the average.
- [ ] E. A histogram shows the distribution of one variable, and a scatter plot shows the relationship between two variables.

**Key:** A=F B=T C=T D=F E=T  |  `MA-4.7`  |  *4. Exploratory data analysis, data quality and missing data*  |  source: Skewness, mean versus median, mode, histogram versus scatter plot

- A (false): They measure spread, not center.
- B (true): They are two different measures of center.
- C (true): A long right tail pulls the mean upward more than the median.
- D (false): The mode is the most frequent value; the average is the mean.
- E (true): Histograms display shape; scatter plots display association.

**14.** A demand-forecasting model scores well on a random split but poorly after deployment, and the data changes over time. Check each statement that is true.  *(5 points)*

- [ ] A. A random held-out split is the right choice when the data drifts over time.
- [ ] B. A held-out split sets aside data that is not used for training.
- [ ] C. A random split is not a held-out set.
- [ ] D. An out-of-time split trains on earlier data and tests on later data.
- [ ] E. Out-of-time evaluation better mimics deployment when the distribution changes over time.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.31`  |  *Jargon test: robustness and distribution shift*  |  source: Held-out vs out-of-time split

- A (false): It mixes periods and hides the effect of drift.
- B (true): It provides an unseen evaluation set.
- C (false): A random split can still produce a held-out set.
- D (true): The test period follows the training period.
- E (true): Deployment always faces the future, which the split imitates.

**15.** A lender removes race from the inputs of its approval model but keeps zip code, which is correlated with race. Check each statement that is true.  *(5 points)*

- [ ] A. A proxy variable is itself a protected attribute.
- [ ] B. Race is a protected attribute: a characteristic that law or policy shields from discrimination.
- [ ] C. Removing zip code guarantees the outputs are independent of race.
- [ ] D. Dropping the protected attribute from the inputs, called fairness through unawareness, can leave a proxy in place.
- [ ] E. Zip code here acts as a proxy variable for race.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.56`  |  *Jargon test: bias and fairness*  |  source: Protected attribute and proxy variable

- A (false): A proxy is an ordinary input that stands in for one.
- B (true): Protected attributes are the characteristics fairness rules refer to.
- C (false): Other correlated inputs can still carry the information.
- D (true): Unawareness removes the column but not correlated information.
- E (true): A proxy is an input correlated enough with a protected attribute to carry its information.

**16.** A statistician explains the shared-birthday result for a group of people, assuming 365 equally likely birthdays that are independent. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The event "some pair in the group shares a birthday" has the same probability as the event "one named person shares a birthday with someone else in the group".
- [ ] B. The growth of a match chance in a small group is explained by counting pairs of people instead of counting people.
- [ ] C. The complement rule computes P(at least two share a birthday) as 1 minus P(no two share a birthday).
- [ ] D. Birthdays clustered on certain dates make a match less likely than under the uniform model.
- [ ] E. "At least two share a birthday" and "exactly two share a birthday" name the same event.

**Key:** A=F B=T C=T D=F E=F  |  `MA-1.4`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Complement rule, pairs, and "at least one" events

- A (false): The named-person event is far less likely; the pair event has many more chances to occur.
- B (true): The number of pairs grows roughly with the square of the group size.
- C (true): The complement of "at least one match" is "no match", which is easier to count.
- D (false): Non-uniform frequencies make a match more likely; the uniform case is the least likely to produce one.
- E (false): "At least two" includes larger shared groups; "exactly two" excludes them.

**17.** A team tries 200 hyperparameter configurations, scores each on the same fixed test set, and reports the best score as the expected accuracy in production. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Tuning belongs on a validation set or in cross-validation, and the test set is used once at the end.
- [ ] B. Nested cross-validation uses an inner loop for tuning and an outer loop for estimating performance.
- [ ] C. Choosing the best of many configurations on the test set makes the reported score optimistic, a selection effect called the winner's curse.
- [ ] D. Distribution shift between the test data and production data leaves the test accuracy a valid estimate of production accuracy.
- [ ] E. Near-duplicate examples shared between training and test splits make the score pessimistic.

**Key:** A=T B=T C=T D=F E=F  |  `MA-5.7`  |  *5. Modeling basics: fit, overfitting and evaluation*  |  source: Winner's curse, validation set, nested cross-validation, distribution shift

- A (true): Keeping the test set untouched gives an independent estimate.
- B (true): The outer folds never influence the choices made in the inner loop.
- C (true): The maximum of many noisy scores is biased upward.
- D (false): Under distribution shift, test accuracy can overstate performance in production.
- E (false): Shared near-duplicates leak information and make the score optimistic.

**18.** A cleaning step removes rows that are byte-for-byte identical, yet the train and test sets still share rows that differ only by trailing whitespace. Check each statement that is true.  *(5 points)*

- [ ] A. Removing exact duplicates also removes near-duplicates.
- [ ] B. Near-duplicates shared between train and test can cause leakage.
- [ ] C. Near-duplicates are records that differ slightly, such as a typo or whitespace, but carry the same content.
- [ ] D. Exact duplicates are records that are identical.
- [ ] E. Fuzzy matching or hashing of text shingles is a way to detect near-duplicates.

**Key:** A=F B=T C=T D=T E=T  |  `MA-jargon.17`  |  *Jargon test: data validation and provenance*  |  source: Duplicates vs near-duplicates

- A (false): Exact matching misses slightly different copies.
- B (true): The model has effectively seen the test item.
- C (true): They are close copies rather than identical copies.
- D (true): Identical rows match on every field.
- E (true): Those methods score similarity instead of requiring equality.

**19.** A city agency chooses between a boosted model with post-hoc Shapley explanations and a scoring rule with seven integer-weighted checks that has slightly lower accuracy. Check each statement that is true.  *(5 points)*

- [ ] A. Interpretable by design means the model is a neural network with an attention layer.
- [ ] B. A post-hoc explanation of the black box is as auditable as a transparent rule.
- [ ] C. An interpretable model gives lower accuracy than a black box on tabular data.
- [ ] D. Auditability means a third party can inspect and reproduce how a decision was reached.
- [ ] E. A scorecard of integer-weighted checks is an example of a model that is interpretable by design.

**Key:** A=F B=F C=F D=T E=T  |  `MA-ch05.35`  |  *None*  |  source: Inherently interpretable models and auditability

- A (false): It refers to structure a person can follow, such as a sparse linear model, a small tree or a scorecard.
- B (false): Post-hoc output is an approximation produced by a method, which can itself be wrong.
- C (false): The accuracy gap is often small, and no fixed trade-off holds.
- D (true): A simple rule can be reproduced step by step.
- E (true): Its structure is the explanation.

**20.** X is a continuous random variable, uniformly distributed on the interval from 0 to 0.5. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The cumulative distribution function can decrease as x increases.
- [ ] B. The area under the density curve between two points is the expected value of X.
- [ ] C. A probability mass function is the right description for a continuous variable.
- [ ] D. For a continuous variable the probability of one exact value is 0.
- [ ] E. A probability density function value is not a probability and can exceed 1.

**Key:** A=F B=F C=F D=T E=T  |  `MA-2.2`  |  *2. Random variables and distributions*  |  source: Probability density function, cumulative distribution function, probability mass function

- A (false): The cumulative distribution function P(X ≤ x) is non-decreasing.
- B (false): That area is the probability that X falls between the two points.
- C (false): A probability mass function belongs to discrete variables; continuous variables use a density.
- D (true): Probability comes from the area under the density over an interval, and a single point has no width.
- E (true): Density is probability per unit length; for this uniform variable it is 2.
