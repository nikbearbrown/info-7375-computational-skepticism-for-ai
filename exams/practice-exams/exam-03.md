# INFO 7375 Computational Skepticism for AI: practice exam 03

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** A survey records age for each respondent and asks for income, which some respondents leave blank. Which statements use the missingness terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Missing not at random (MNAR) means missingness depends on the unobserved value itself, such as higher earners skipping because of income.
- [ ] B. Whether income is missing not at random can be confirmed from the observed values alone.
- [ ] C. Higher earners skipping the income question because of their income is missing at random.
- [ ] D. Missing completely at random (MCAR) means missingness is unrelated to the observed variables and to the unobserved values.
- [ ] E. Missing at random (MAR) means missingness depends on observed variables, such as older respondents skipping more often, and not on the missing value itself.

**2.** A user prompts an AI: "The model got worse because the data changed." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Call a random perturbation an adversarial example.
- [ ] B. State whether P(x) changed, which is covariate shift, or P(y | x) changed, which is concept drift.
- [ ] C. Report accuracy on the training set to show robustness.
- [ ] D. Describe the held-out test as out-of-time if it is a random sample.
- [ ] E. Call it covariate shift if the class proportions changed.

**3.** A hiring model is trained on twenty years of accurate, well-sampled records that show few women hired into engineering. Check each statement that is true.  *(5 points)*

- [ ] A. Collecting a larger random sample removes historical bias.
- [ ] B. Historical bias can be present when sampling and measurement are sound.
- [ ] C. Historical bias is a type of measurement bias because the records are inaccurate.
- [ ] D. Historical bias requires that the records contain data-entry errors.
- [ ] E. This is historical bias: accurate data that reflect a world containing past inequity.

**4.** A fraud team says its transaction classifier "catches 90% of fraud" and "wrongly flags 4% of legitimate transactions". Which statements name these quantities correctly? Check each statement that is true.  *(5 points)*

- [ ] A. For a fixed sensitivity and false positive rate, the prevalence (base rate) of fraud leaves the positive predictive value unchanged.
- [ ] B. "Catches 90% of fraud" is the sensitivity of the classifier, also called recall or the true positive rate.
- [ ] C. Sensitivity and positive predictive value are two names for one quantity.
- [ ] D. "Wrongly flags 4% of legitimate transactions" is the false positive rate, which equals 1 minus the specificity.
- [ ] E. The probability that a flagged transaction is fraudulent is the sensitivity.

**5.** A data scientist has 60 examples and 5,000 pure-noise features. They pick the 20 features most correlated with the label using all 60 examples, run 5-fold cross-validation on those features and report 92% accuracy. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Selecting features using the labels of the full dataset before cross-validation is leakage.
- [ ] B. Fitting a label-dependent step such as target encoding on the full data before splitting is also leakage.
- [ ] C. Data leakage means information from the held-out data influences model training or selection.
- [ ] D. With noise features and fair-coin labels, an honest evaluation should show accuracy near chance.
- [ ] E. Using more folds removes the leakage from the feature selection done before the split.

**6.** A model scores very high because some test rows are also in the training set, and a separate benchmark score is high because its questions appeared in the pretraining text. Check each statement that is true.  *(5 points)*

- [ ] A. Benchmark contamination is test items appearing in a model's training corpus.
- [ ] B. Data leakage is information from outside the training data, or from the target, getting into training so evaluation is inflated.
- [ ] C. Contamination is a type of missingness.
- [ ] D. A feature derived from the label is a source of leakage.
- [ ] E. Leakage describes a model that memorises noise in the training data.

**7.** A colleague says: "SHAP is the unique attribution method with efficiency, symmetry, dummy and additivity, so it is the correct way to explain a model." Check each statement that is true.  *(5 points)*

- [ ] A. For a fixed value function, the Shapley value is the unique allocation satisfying efficiency, symmetry, dummy and additivity.
- [ ] B. Satisfying the properties makes sampling estimates of Shapley values free of estimation error.
- [ ] C. The value function, meaning how a subset of inputs is valued, is a different choice from the allocation rule.
- [ ] D. The four properties also fix the value function, so the choice between marginal and conditional valuation is already settled.
- [ ] E. The properties show that the attribution answers the question a given user wants answered.

**8.** A model answers each of 20 test prompts correctly with probability 0.8, independently, and the number correct is modeled as binomial. Which statements are correct? Check each statement that is true.  *(5 points)*

- [ ] A. The binomial variance is np, which equals its mean.
- [ ] B. Overdispersion means the observed variance is smaller than the model variance.
- [ ] C. Positively correlated trials, such as near-duplicate prompts, cause overdispersion: the count varies more than the binomial variance says.
- [ ] D. A binomial count is the number of successes in a fixed number of independent trials that share one success probability.
- [ ] E. Overdispersion and underdispersion both describe the sample mean differing from the population mean.

**9.** A heat map highlights regions of a chest X-ray that drove a classifier's output. Check each statement that is true.  *(5 points)*

- [ ] A. A saliency map is a counterfactual explanation.
- [ ] B. A highlighted region shows where the disease is located in the patient.
- [ ] C. An attribution method assigns each input feature a share of a prediction.
- [ ] D. Shapley values are one kind of attribution method.
- [ ] E. A saliency map shows which input regions most affect the model's output score.

**10.** A prompt says: "make the model robust against attacks and against new data." Check each statement that is true.  *(5 points)*

- [ ] A. Distribution shift means test inputs come from a different distribution than the training data.
- [ ] B. Robustness to distribution shift is tested with adversarial examples.
- [ ] C. Adversarial robustness is measured on held-out data from the same distribution.
- [ ] D. Adversarial robustness concerns small deliberate input perturbations designed to cause errors.
- [ ] E. An adversarial example is naturally occurring noise in the data.

**11.** A vendor says a rare-disease test is "99% accurate", so a positive result means the patient is almost surely ill. Check each statement that is true.  *(5 points)*

- [ ] A. Positive predictive value is unaffected by the base rate.
- [ ] B. Sensitivity and specificity are defined by prevalence.
- [ ] C. Ignoring the base rate is called overfitting.
- [ ] D. With a low base rate, many positive results can be false positives even for a sensitive test.
- [ ] E. The base rate is the prevalence of the condition in the population tested.

**12.** A tutoring app invites its 1.25 million users to a satisfaction survey. A total of 50,000 respond and 92% of respondents say they are satisfied. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Respondents choosing for themselves whether to answer is self-selection, a source of nonresponse bias.
- [ ] B. A larger number of respondents reduces random error but leaves selection bias in place.
- [ ] C. The standard error quantifies the systematic bias that comes from who chose to respond.
- [ ] D. A large volunteer sample is a probability sample because it is large.
- [ ] E. Selection bias and measurement bias are two names for the same problem.

**13.** An analyst describes the shape of a response-time variable and the best plot for it. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Standard deviation and variance are measures of central tendency.
- [ ] B. The median is the middle value of the sorted data, while the mean is the balance point of the data.
- [ ] C. In a right-skewed distribution the mean exceeds the median.
- [ ] D. The mode is another name for the average.
- [ ] E. A histogram shows the distribution of one variable, and a scatter plot shows the relationship between two variables.

**14.** A demand-forecasting model scores well on a random split but poorly after deployment, and the data changes over time. Check each statement that is true.  *(5 points)*

- [ ] A. A random held-out split is the right choice when the data drifts over time.
- [ ] B. A held-out split sets aside data that is not used for training.
- [ ] C. A random split is not a held-out set.
- [ ] D. An out-of-time split trains on earlier data and tests on later data.
- [ ] E. Out-of-time evaluation better mimics deployment when the distribution changes over time.

**15.** A lender removes race from the inputs of its approval model but keeps zip code, which is correlated with race. Check each statement that is true.  *(5 points)*

- [ ] A. A proxy variable is itself a protected attribute.
- [ ] B. Race is a protected attribute: a characteristic that law or policy shields from discrimination.
- [ ] C. Removing zip code guarantees the outputs are independent of race.
- [ ] D. Dropping the protected attribute from the inputs, called fairness through unawareness, can leave a proxy in place.
- [ ] E. Zip code here acts as a proxy variable for race.

**16.** A statistician explains the shared-birthday result for a group of people, assuming 365 equally likely birthdays that are independent. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The event "some pair in the group shares a birthday" has the same probability as the event "one named person shares a birthday with someone else in the group".
- [ ] B. The growth of a match chance in a small group is explained by counting pairs of people instead of counting people.
- [ ] C. The complement rule computes P(at least two share a birthday) as 1 minus P(no two share a birthday).
- [ ] D. Birthdays clustered on certain dates make a match less likely than under the uniform model.
- [ ] E. "At least two share a birthday" and "exactly two share a birthday" name the same event.

**17.** A team tries 200 hyperparameter configurations, scores each on the same fixed test set, and reports the best score as the expected accuracy in production. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Tuning belongs on a validation set or in cross-validation, and the test set is used once at the end.
- [ ] B. Nested cross-validation uses an inner loop for tuning and an outer loop for estimating performance.
- [ ] C. Choosing the best of many configurations on the test set makes the reported score optimistic, a selection effect called the winner's curse.
- [ ] D. Distribution shift between the test data and production data leaves the test accuracy a valid estimate of production accuracy.
- [ ] E. Near-duplicate examples shared between training and test splits make the score pessimistic.

**18.** A cleaning step removes rows that are byte-for-byte identical, yet the train and test sets still share rows that differ only by trailing whitespace. Check each statement that is true.  *(5 points)*

- [ ] A. Removing exact duplicates also removes near-duplicates.
- [ ] B. Near-duplicates shared between train and test can cause leakage.
- [ ] C. Near-duplicates are records that differ slightly, such as a typo or whitespace, but carry the same content.
- [ ] D. Exact duplicates are records that are identical.
- [ ] E. Fuzzy matching or hashing of text shingles is a way to detect near-duplicates.

**19.** A city agency chooses between a boosted model with post-hoc Shapley explanations and a scoring rule with seven integer-weighted checks that has slightly lower accuracy. Check each statement that is true.  *(5 points)*

- [ ] A. Interpretable by design means the model is a neural network with an attention layer.
- [ ] B. A post-hoc explanation of the black box is as auditable as a transparent rule.
- [ ] C. An interpretable model gives lower accuracy than a black box on tabular data.
- [ ] D. Auditability means a third party can inspect and reproduce how a decision was reached.
- [ ] E. A scorecard of integer-weighted checks is an example of a model that is interpretable by design.

**20.** X is a continuous random variable, uniformly distributed on the interval from 0 to 0.5. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The cumulative distribution function can decrease as x increases.
- [ ] B. The area under the density curve between two points is the expected value of X.
- [ ] C. A probability mass function is the right description for a continuous variable.
- [ ] D. For a continuous variable the probability of one exact value is 0.
- [ ] E. A probability density function value is not a probability and can exceed 1.
