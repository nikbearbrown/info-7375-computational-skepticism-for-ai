# INFO 7375 Computational Skepticism for AI: practice exam 06

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** A cleaner proposes deleting the largest transactions and calling them anomalies. Check each statement that is true.  *(5 points)*

- [ ] A. An outlier is a data point far from the bulk of the distribution.
- [ ] B. An outlier is a data entry error that should be deleted.
- [ ] C. Anomaly detection is another name for imputation.
- [ ] D. A value can be a statistical outlier and still be a valid measurement.
- [ ] E. An anomaly is an observation that does not conform to expected behaviour, and it may signal a fault or fraud.

**2.** A face dataset is collected from social media photos of young adults and then used for people of many ages. Check each statement that is true.  *(5 points)*

- [ ] A. Some texts call this representation bias.
- [ ] B. This is sampling bias: the sample's makeup differs from the population where the model will be used.
- [ ] C. It is measurement bias because the photos are inaccurate.
- [ ] D. Evaluating separately by age group helps reveal its effect.
- [ ] E. Adding more rows from the same source reduces it.

**3.** A team compares 40 prompt variants with a baseline, announces the best variant as significant at p = 0.03, and then plans a follow-up. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A preregistered hypothesis is one chosen after the data have been examined.
- [ ] B. The raw p-value of a selected best result understates how easily chance produces such a result.
- [ ] C. The Holm procedure controls the family-wise error rate and is less conservative than the Bonferroni correction.
- [ ] D. A Bonferroni-adjusted p-value is the raw p-value divided by the number of tests.
- [ ] E. Picking the best of many variants after seeing the data is exploratory; testing the winner once on fresh held-out data with a pre-specified hypothesis is confirmatory.

**4.** A lender trains a model on past loans to predict default from 30 recorded features, and it ranks risk well on new applicants who resemble past borrowers. Check each statement that is true.  *(5 points)*

- [ ] A. Feature importance is a different thing from causal effect.
- [ ] B. The model estimates conditional probabilities, which is association at rung 1.
- [ ] C. A feature that is a consequence of the label can inflate accuracy, which is leakage.
- [ ] D. A large weight on a feature shows that the feature causes default.
- [ ] E. Good prediction on similar cases shows what would happen if the lender changed a feature.

**5.** A report says a model is robust because it scores well on a random held-out test set from its own source. Check each statement that is true.  *(5 points)*

- [ ] A. Good in-distribution test accuracy shows robustness.
- [ ] B. Robustness is performance staying acceptable under perturbation or shift.
- [ ] C. Robustness and generalization are identical.
- [ ] D. A model can generalize well in-distribution and still be fragile under shift.
- [ ] E. Generalization is performance on new data from the same distribution as the training data.

**6.** A prompt to an analyst says: "check the data is clean." Check each statement that is true.  *(5 points)*

- [ ] A. Data validation checks that data meet stated rules, such as types, ranges and missing values.
- [ ] B. A precise rewrite names the checks, such as schema validation, missingness, duplicates and outliers.
- [ ] C. Cleaning the data removes sampling bias.
- [ ] D. Provenance is the record of where data came from and how it was changed.
- [ ] E. A dataset that passes validation checks is guaranteed to be accurate.

**7.** A user asks a language model "how sure are you?" and it answers "95% confident." Check each statement that is true.  *(5 points)*

- [ ] A. Token probabilities are a different signal from verbalized confidence.
- [ ] B. A stated 95% is a calibrated probability by construction.
- [ ] C. Agreement across repeated samples is another way to estimate confidence.
- [ ] D. Verbalized confidence is a probability the model states in words.
- [ ] E. Verbalized confidence can be checked by comparing stated values with observed correctness.

**8.** A vendor brochure calls its model "explainable, interpretable and transparent", and the buyer wants each word pinned down. Check each statement that is true.  *(5 points)*

- [ ] A. Interpretability is the degree to which a person can understand the model's own mechanism, as with a short decision tree.
- [ ] B. The three words are synonyms for the same property.
- [ ] C. Publishing the full weights of a large neural network makes it interpretable.
- [ ] D. Transparency means the model, its design and its data are open to inspection.
- [ ] E. An explanation is a statement or artifact offered about why a particular output came out as it did.

**9.** A team asks an agent to "document the provenance of the table" but really wants the steps from the raw file to the final table. Check each statement that is true.  *(5 points)*

- [ ] A. Lineage traces the transformations and movements of data from source to current form.
- [ ] B. Lineage describes the licence terms of the data.
- [ ] C. Provenance records the origin of data, such as who collected it and how.
- [ ] D. For the steps from raw file to final table, the better term is provenance.
- [ ] E. Provenance and lineage are identical.

**10.** A default model is trained only on applicants who were approved in the past, then used to score the whole applicant pool. Check each statement that is true.  *(5 points)*

- [ ] A. Gathering more outcomes from the same approved group reduces it.
- [ ] B. This is label bias because annotators mislabelled applicants.
- [ ] C. Data from approved applicants alone are representative of the whole applicant pool.
- [ ] D. This is measurement bias because a feature's scale differs between applicants.
- [ ] E. This is selection bias: the data are a non-random subset chosen by a process related to the outcome.

**11.** A group screens 200 independent hypotheses, 20 of them true effects, using significance level 0.05 and power 0.80. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The false discovery rate among significant results depends on the base rate of true effects, so alpha alone does not set it.
- [ ] B. Power is 1 minus the Type II error rate, the probability of detecting an effect that is real.
- [ ] C. A significance level of 0.05 means that 95% of significant findings are real effects.
- [ ] D. The significance level is the Type I error rate: the probability of rejecting a null hypothesis that is true.
- [ ] E. A Type II error is a false positive.

**12.** Team 1 trains a model on past healthcare spending as a stand-in for medical need. Team 2's demand forecaster had low error for two years, until a new competitor changed customers' buying habits and the error began to rise. Check each statement that is true.  *(5 points)*

- [ ] A. Team 1 used a proxy label, and the proxy was not the target to begin with.
- [ ] B. Concept drift is a change in the distribution of inputs while the relation of outcome to inputs stays fixed.
- [ ] C. Team 2's rising error after the competitor appeared is concept drift, since the relation between inputs and outcome changed.
- [ ] D. Label shift is a change in the proportion of outcome classes between training and use.
- [ ] E. Retraining Team 1's model on newer data with the same proxy label closes the gap between label and need.

**13.** Match each description to its term. Check each statement that is true.  *(5 points)*

- [ ] A. A test image from the training source is out-of-distribution.
- [ ] B. Training on January to June and testing on July to December is an out-of-time split.
- [ ] C. Applying a random blur to an image is an adversarial example.
- [ ] D. Swapping a word for a synonym in a prompt is a perturbation.
- [ ] E. Testing a document model on very long documents is a stress test.

**14.** A report says: "the p-value is 0.03, so there is a 97 percent chance the effect is real." Check each statement that is true.  *(5 points)*

- [ ] A. A p-value is computed by assuming the null hypothesis.
- [ ] B. A p-value is the probability of data at least this extreme if the null hypothesis were true.
- [ ] C. A p-value is the probability that the null hypothesis is true.
- [ ] D. A p-value of 0.03 means a 97 percent probability that the effect is real.
- [ ] E. A posterior probability is the probability of a hypothesis given the data, in the Bayesian sense.

**15.** A reviewer asks for exact terms for a screening test. Check each statement that is true.  *(5 points)*

- [ ] A. Precision is the share of positive predictions that are truly positive.
- [ ] B. Specificity is the share of actual negatives classified as negative.
- [ ] C. Recall is another name for sensitivity.
- [ ] D. Precision is the share of actual positives that the test catches.
- [ ] E. Specificity is also called the true negative rate.

**16.** A team lists requests to an explanation tool and wants the exact term for each. Check each statement that is true.  *(5 points)*

- [ ] A. Asking for a ranking of inputs by average reliance across the dataset asks for global feature importance.
- [ ] B. Asking for a rule-based model a regulator can read directly asks for an intrinsically interpretable model.
- [ ] C. Asking whether the explanation reflects what the model really does asks about plausibility.
- [ ] D. Asking for the smallest input change that flips a denial asks for a counterfactual explanation.
- [ ] E. Asking why this one case got its score asks for a global explanation.

**17.** An audit lists four situations, and the team labels each with a bias term. Check each statement that is true.  *(5 points)*

- [ ] A. A thermometer that reads two degrees high at one clinic produces measurement bias.
- [ ] B. Training on past customers who were approved for loans, since they have repayment outcomes, produces selection bias.
- [ ] C. A scale that reads high is an example of sampling bias.
- [ ] D. Annotators who label one dialect as toxic more often produce label bias.
- [ ] E. Label bias is another name for overfitting.

**18.** An A/B test with 20,000 users per arm gives a two-sided p-value of 0.048 for a 0.6 percentage point lift in conversion. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A p-value is the probability of data at least as extreme as observed, computed assuming the null hypothesis is true.
- [ ] B. One minus the p-value, 0.952, is the probability that the feature truly raises conversion.
- [ ] C. A p-value of 0.048 is the probability that the null hypothesis is true.
- [ ] D. A small p-value shows that the effect size is large.
- [ ] E. Statistical significance and practical significance are different judgments.

**19.** Parents notice that children who play a musical instrument have higher maths scores, and ask whether learning an instrument raises maths scores. Here the treatment is playing an instrument and the outcome is the maths score. Check each variable that is a confounder in this situation.  *(5 points)*

- [ ] A. Hours of daily practice, which are accumulated by children who play an instrument and which may build focus.
- [ ] B. Membership in the school orchestra, which follows from playing an instrument.
- [ ] C. Whether the child enters a maths competition, which is more likely for children who already have high scores.
- [ ] D. Family income, which affects whether a family can afford lessons and instruments and also affects the resources that support learning maths.
- [ ] E. The parents' level of education, which affects whether children are steered toward music lessons and also how well they are helped with maths.

**20.** A report says: "ads and sales are correlated, so ad spend is a confounder of sales", and also treats the correlation as proof that ads drive sales. Check each statement that is true.  *(5 points)*

- [ ] A. The correlation coefficient measures how well a nonlinear curve fits the data.
- [ ] B. A strong correlation shows that one variable causes the other.
- [ ] C. A spurious correlation is an association not due to a causal link between the variables.
- [ ] D. A confounder is a common cause of both the exposure and the outcome.
- [ ] E. A correlation of zero shows the variables are independent.
