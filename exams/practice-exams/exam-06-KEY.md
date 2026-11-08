# INFO 7375 Computational Skepticism for AI: practice exam 06: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A cleaner proposes deleting the largest transactions and calling them anomalies. Check each statement that is true.  *(5 points)*

- [ ] A. An outlier is a data point far from the bulk of the distribution.
- [ ] B. An outlier is a data entry error that should be deleted.
- [ ] C. Anomaly detection is another name for imputation.
- [ ] D. A value can be a statistical outlier and still be a valid measurement.
- [ ] E. An anomaly is an observation that does not conform to expected behaviour, and it may signal a fault or fraud.

**Key:** A=T B=F C=F D=T E=T  |  `MA-jargon.20`  |  *Jargon test: data validation and provenance*  |  source: Outlier vs anomaly

- A (true): Outlier is a statement about position in the distribution.
- B (false): An outlier can be a valid measurement.
- C (false): Imputation fills missing values; anomaly detection flags unusual cases.
- D (true): Extreme values are not automatically errors.
- E (true): Anomaly is a statement about behaviour against expectation.

**2.** A face dataset is collected from social media photos of young adults and then used for people of many ages. Check each statement that is true.  *(5 points)*

- [ ] A. Some texts call this representation bias.
- [ ] B. This is sampling bias: the sample's makeup differs from the population where the model will be used.
- [ ] C. It is measurement bias because the photos are inaccurate.
- [ ] D. Evaluating separately by age group helps reveal its effect.
- [ ] E. Adding more rows from the same source reduces it.

**Key:** A=T B=T C=F D=T E=F  |  `MA-jargon.64`  |  *Jargon test: bias and fairness*  |  source: Sampling bias

- A (true): Representation bias is a near-synonym for sampling bias in this sense.
- B (true): Sampling bias is a mismatch between sample and target population.
- C (false): The photos can be accurate; the problem is who is represented.
- D (true): Subgroup evaluation exposes weaker performance on under-represented groups.
- E (false): More rows from the same source repeat the same skew.

**3.** A team compares 40 prompt variants with a baseline, announces the best variant as significant at p = 0.03, and then plans a follow-up. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A preregistered hypothesis is one chosen after the data have been examined.
- [ ] B. The raw p-value of a selected best result understates how easily chance produces such a result.
- [ ] C. The Holm procedure controls the family-wise error rate and is less conservative than the Bonferroni correction.
- [ ] D. A Bonferroni-adjusted p-value is the raw p-value divided by the number of tests.
- [ ] E. Picking the best of many variants after seeing the data is exploratory; testing the winner once on fresh held-out data with a pre-specified hypothesis is confirmatory.

**Key:** A=F B=T C=T D=F E=T  |  `MA-3.9`  |  *3. Sampling, the central limit theorem and inference*  |  source: Exploratory versus confirmatory analysis, Holm, adjusted p-value, preregistration

- A (false): Preregistration fixes the hypothesis and analysis plan before looking at the outcome data.
- B (true): The smallest of many null p-values is routinely small.
- C (true): Holm is a step-down method that rejects at least as many hypotheses as Bonferroni.
- D (false): The adjusted p-value is the raw value multiplied by the number of tests, capped at 1.
- E (true): Confirmatory analysis fixes the hypothesis before the data are seen.

**4.** A lender trains a model on past loans to predict default from 30 recorded features, and it ranks risk well on new applicants who resemble past borrowers. Check each statement that is true.  *(5 points)*

- [ ] A. Feature importance is a different thing from causal effect.
- [ ] B. The model estimates conditional probabilities, which is association at rung 1.
- [ ] C. A feature that is a consequence of the label can inflate accuracy, which is leakage.
- [ ] D. A large weight on a feature shows that the feature causes default.
- [ ] E. Good prediction on similar cases shows what would happen if the lender changed a feature.

**Key:** A=T B=T C=T D=F E=F  |  `MA-ch06.32`  |  *None*  |  source: Prediction versus causation, leakage

- A (true): Importance describes use by the model, and causal effect describes the result of an intervention.
- B (true): Prediction fits observed relationships between features and outcome.
- C (true): Leakage lets the model use information that would not be available at prediction time.
- D (false): A feature can carry weight as a proxy, an effect of default, or a shared cause.
- E (false): A prediction describes what goes with a value, not what follows from changing it.

**5.** A report says a model is robust because it scores well on a random held-out test set from its own source. Check each statement that is true.  *(5 points)*

- [ ] A. Good in-distribution test accuracy shows robustness.
- [ ] B. Robustness is performance staying acceptable under perturbation or shift.
- [ ] C. Robustness and generalization are identical.
- [ ] D. A model can generalize well in-distribution and still be fragile under shift.
- [ ] E. Generalization is performance on new data from the same distribution as the training data.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.28`  |  *Jargon test: robustness and distribution shift*  |  source: Robustness vs generalization

- A (false): It shows generalization; robustness needs perturbed or shifted data.
- B (true): Robustness concerns conditions that differ from training.
- C (false): They test different conditions.
- D (true): The two properties can come apart.
- E (true): A same-source test measures generalization.

**6.** A prompt to an analyst says: "check the data is clean." Check each statement that is true.  *(5 points)*

- [ ] A. Data validation checks that data meet stated rules, such as types, ranges and missing values.
- [ ] B. A precise rewrite names the checks, such as schema validation, missingness, duplicates and outliers.
- [ ] C. Cleaning the data removes sampling bias.
- [ ] D. Provenance is the record of where data came from and how it was changed.
- [ ] E. A dataset that passes validation checks is guaranteed to be accurate.

**Key:** A=T B=T C=F D=T E=F  |  `MA-jargon.68`  |  *Jargon test: wrong word, right word*  |  source: Clean vs validated

- A (true): Validation is rule-based checking of data against a schema or expectations.
- B (true): "Clean" is vague, while named checks are testable.
- C (false): Cleaning fixes errors; it does not change who is in the sample.
- D (true): Provenance documents origin and custody.
- E (false): Validation checks stated rules, which do not prove the values are true.

**7.** A user asks a language model "how sure are you?" and it answers "95% confident." Check each statement that is true.  *(5 points)*

- [ ] A. Token probabilities are a different signal from verbalized confidence.
- [ ] B. A stated 95% is a calibrated probability by construction.
- [ ] C. Agreement across repeated samples is another way to estimate confidence.
- [ ] D. Verbalized confidence is a probability the model states in words.
- [ ] E. Verbalized confidence can be checked by comparing stated values with observed correctness.

**Key:** A=T B=F C=T D=T E=T  |  `MA-jargon.11`  |  *Jargon test: probability and confidence*  |  source: Verbalized confidence

- A (true): Logprobs come from the output distribution, not from the text.
- B (false): Stated values need to be checked against outcomes.
- C (true): Self-consistency is a sampling-based confidence signal.
- D (true): It is the self-reported number in the text output.
- E (true): That comparison is a calibration check.

**8.** A vendor brochure calls its model "explainable, interpretable and transparent", and the buyer wants each word pinned down. Check each statement that is true.  *(5 points)*

- [ ] A. Interpretability is the degree to which a person can understand the model's own mechanism, as with a short decision tree.
- [ ] B. The three words are synonyms for the same property.
- [ ] C. Publishing the full weights of a large neural network makes it interpretable.
- [ ] D. Transparency means the model, its design and its data are open to inspection.
- [ ] E. An explanation is a statement or artifact offered about why a particular output came out as it did.

**Key:** A=T B=F C=F D=T E=T  |  `MA-jargon.41`  |  *Jargon test: explainability*  |  source: Explanation, interpretability, transparency

- A (true): That is the standard meaning: understanding the mechanism itself.
- B (false): They name different things: understanding the mechanism, access to internals, and a produced account of an output.
- C (false): Open weights make a model transparent, but a person still cannot read a large network's mechanism, so it is not interpretable.
- D (true): Transparency is about access to the internals, not about understanding them.
- E (true): An explanation is something produced about a model's output, which may or may not reflect the mechanism.

**9.** A team asks an agent to "document the provenance of the table" but really wants the steps from the raw file to the final table. Check each statement that is true.  *(5 points)*

- [ ] A. Lineage traces the transformations and movements of data from source to current form.
- [ ] B. Lineage describes the licence terms of the data.
- [ ] C. Provenance records the origin of data, such as who collected it and how.
- [ ] D. For the steps from raw file to final table, the better term is provenance.
- [ ] E. Provenance and lineage are identical.

**Key:** A=T B=F C=T D=F E=F  |  `MA-jargon.13`  |  *Jargon test: data validation and provenance*  |  source: Provenance vs lineage

- A (true): Lineage is the path through processing steps.
- B (false): Licence terms are separate metadata.
- C (true): Provenance answers where the data came from.
- D (false): The better term for processing steps is lineage.
- E (false): They overlap but name different things.

**10.** A default model is trained only on applicants who were approved in the past, then used to score the whole applicant pool. Check each statement that is true.  *(5 points)*

- [ ] A. Gathering more outcomes from the same approved group reduces it.
- [ ] B. This is label bias because annotators mislabelled applicants.
- [ ] C. Data from approved applicants alone are representative of the whole applicant pool.
- [ ] D. This is measurement bias because a feature's scale differs between applicants.
- [ ] E. This is selection bias: the data are a non-random subset chosen by a process related to the outcome.

**Key:** A=F B=F C=F D=F E=T  |  `MA-jargon.66`  |  *Jargon test: bias and fairness*  |  source: Selection bias

- A (false): The skew comes from the missing group, not the count of approved cases.
- B (false): No mislabelling is described; the issue is who is in the data.
- C (false): Rejected applicants are missing, so the data are skewed.
- D (false): Nothing about measurement is described.
- E (true): Past approvals decided who has outcomes.

**11.** A group screens 200 independent hypotheses, 20 of them true effects, using significance level 0.05 and power 0.80. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The false discovery rate among significant results depends on the base rate of true effects, so alpha alone does not set it.
- [ ] B. Power is 1 minus the Type II error rate, the probability of detecting an effect that is real.
- [ ] C. A significance level of 0.05 means that 95% of significant findings are real effects.
- [ ] D. The significance level is the Type I error rate: the probability of rejecting a null hypothesis that is true.
- [ ] E. A Type II error is a false positive.

**Key:** A=T B=T C=F D=T E=F  |  `MA-3.3`  |  *3. Sampling, the central limit theorem and inference*  |  source: Type I error, Type II error, power, false discovery rate, base rate

- A (true): Where true effects are rare, false positives from many true nulls make up a large share of discoveries.
- B (true): Type II error is a miss, and power is its complement.
- C (false): The share of significant findings that are real depends on the base rate of true effects, not on alpha alone.
- D (true): Type I error is a false positive among true nulls.
- E (false): A Type II error is a false negative; a false positive is a Type I error.

**12.** Team 1 trains a model on past healthcare spending as a stand-in for medical need. Team 2's demand forecaster had low error for two years, until a new competitor changed customers' buying habits and the error began to rise. Check each statement that is true.  *(5 points)*

- [ ] A. Team 1 used a proxy label, and the proxy was not the target to begin with.
- [ ] B. Concept drift is a change in the distribution of inputs while the relation of outcome to inputs stays fixed.
- [ ] C. Team 2's rising error after the competitor appeared is concept drift, since the relation between inputs and outcome changed.
- [ ] D. Label shift is a change in the proportion of outcome classes between training and use.
- [ ] E. Retraining Team 1's model on newer data with the same proxy label closes the gap between label and need.

**Key:** A=T B=F C=T D=T E=F  |  `MA-ch01.24`  |  *None*  |  source: Proxy label, concept drift, covariate shift, label shift

- A (true): A proxy label is a measured stand-in for the quantity that matters.
- B (false): That description fits covariate shift.
- C (true): Concept drift is a change in how inputs relate to the outcome.
- D (true): It is also called prior probability shift.
- E (false): The same flawed label reproduces the same gap.

**13.** Match each description to its term. Check each statement that is true.  *(5 points)*

- [ ] A. A test image from the training source is out-of-distribution.
- [ ] B. Training on January to June and testing on July to December is an out-of-time split.
- [ ] C. Applying a random blur to an image is an adversarial example.
- [ ] D. Swapping a word for a synonym in a prompt is a perturbation.
- [ ] E. Testing a document model on very long documents is a stress test.

**Key:** A=F B=T C=F D=T E=T  |  `MA-jargon.36`  |  *Jargon test: robustness and distribution shift*  |  source: Match robustness terms

- A (false): Same-source images are in-distribution.
- B (true): The test period follows training.
- C (false): A random blur is not targeted at the model.
- D (true): It is a small controlled input change.
- E (true): It pushes the model beyond typical inputs.

**14.** A report says: "the p-value is 0.03, so there is a 97 percent chance the effect is real." Check each statement that is true.  *(5 points)*

- [ ] A. A p-value is computed by assuming the null hypothesis.
- [ ] B. A p-value is the probability of data at least this extreme if the null hypothesis were true.
- [ ] C. A p-value is the probability that the null hypothesis is true.
- [ ] D. A p-value of 0.03 means a 97 percent probability that the effect is real.
- [ ] E. A posterior probability is the probability of a hypothesis given the data, in the Bayesian sense.

**Key:** A=T B=T C=F D=F E=T  |  `MA-jargon.74`  |  *Jargon test: wrong word, right word*  |  source: p-value vs posterior probability

- A (true): The null defines the reference distribution.
- B (true): It is a probability of data given the null.
- C (false): It assumes the null, so it cannot be the probability of the null.
- D (false): The p-value is not a probability that the effect is real.
- E (true): It conditions on the data.

**15.** A reviewer asks for exact terms for a screening test. Check each statement that is true.  *(5 points)*

- [ ] A. Precision is the share of positive predictions that are truly positive.
- [ ] B. Specificity is the share of actual negatives classified as negative.
- [ ] C. Recall is another name for sensitivity.
- [ ] D. Precision is the share of actual positives that the test catches.
- [ ] E. Specificity is also called the true negative rate.

**Key:** A=T B=T C=T D=F E=T  |  `MA-jargon.5`  |  *Jargon test: probability and confidence*  |  source: Sensitivity, specificity, precision, recall

- A (true): Precision is also called positive predictive value.
- B (true): That is the true negative rate.
- C (true): Both are the true positive rate.
- D (false): That describes recall; precision concerns the positive predictions.
- E (true): It measures how well negatives are cleared.

**16.** A team lists requests to an explanation tool and wants the exact term for each. Check each statement that is true.  *(5 points)*

- [ ] A. Asking for a ranking of inputs by average reliance across the dataset asks for global feature importance.
- [ ] B. Asking for a rule-based model a regulator can read directly asks for an intrinsically interpretable model.
- [ ] C. Asking whether the explanation reflects what the model really does asks about plausibility.
- [ ] D. Asking for the smallest input change that flips a denial asks for a counterfactual explanation.
- [ ] E. Asking why this one case got its score asks for a global explanation.

**Key:** A=T B=T C=F D=T E=F  |  `MA-jargon.52`  |  *Jargon test: explainability*  |  source: Choosing the exact explanation term

- A (true): Averaged reliance across the dataset is a global importance.
- B (true): Rule-based models are readable by their structure.
- C (false): That question is about faithfulness.
- D (true): A counterfactual states the change that flips the outcome.
- E (false): A single case calls for a local explanation.

**17.** An audit lists four situations, and the team labels each with a bias term. Check each statement that is true.  *(5 points)*

- [ ] A. A thermometer that reads two degrees high at one clinic produces measurement bias.
- [ ] B. Training on past customers who were approved for loans, since they have repayment outcomes, produces selection bias.
- [ ] C. A scale that reads high is an example of sampling bias.
- [ ] D. Annotators who label one dialect as toxic more often produce label bias.
- [ ] E. Label bias is another name for overfitting.

**Key:** A=T B=T C=F D=T E=F  |  `MA-jargon.53`  |  *Jargon test: bias and fairness*  |  source: Sampling, selection, measurement and label bias

- A (true): Measurement bias is systematic error in how a value is recorded.
- B (true): The process that decides who enters the data is related to the outcome.
- C (false): That is measurement bias; sampling bias concerns who ends up in the sample.
- D (true): Label bias is systematic error in the assigned target labels.
- E (false): Label bias is an error in labels, while overfitting is poor generalization.

**18.** An A/B test with 20,000 users per arm gives a two-sided p-value of 0.048 for a 0.6 percentage point lift in conversion. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. A p-value is the probability of data at least as extreme as observed, computed assuming the null hypothesis is true.
- [ ] B. One minus the p-value, 0.952, is the probability that the feature truly raises conversion.
- [ ] C. A p-value of 0.048 is the probability that the null hypothesis is true.
- [ ] D. A small p-value shows that the effect size is large.
- [ ] E. Statistical significance and practical significance are different judgments.

**Key:** A=T B=F C=F D=F E=T  |  `MA-3.2`  |  *3. Sampling, the central limit theorem and inference*  |  source: p-value, effect size, statistical versus practical significance

- A (true): It is a probability about data under the null, not about the hypothesis.
- B (false): That would be a posterior probability, which needs a prior and a different calculation.
- C (false): The p-value assumes the null; it does not give the probability that the null is true.
- D (false): With large samples a small effect can still give a small p-value; effect size is a separate quantity.
- E (true): A result can be statistically significant yet too small to matter in practice.

**19.** Parents notice that children who play a musical instrument have higher maths scores, and ask whether learning an instrument raises maths scores. Here the treatment is playing an instrument and the outcome is the maths score. Check each variable that is a confounder in this situation.  *(5 points)*

- [ ] A. Hours of daily practice, which are accumulated by children who play an instrument and which may build focus.
- [ ] B. Membership in the school orchestra, which follows from playing an instrument.
- [ ] C. Whether the child enters a maths competition, which is more likely for children who already have high scores.
- [ ] D. Family income, which affects whether a family can afford lessons and instruments and also affects the resources that support learning maths.
- [ ] E. The parents' level of education, which affects whether children are steered toward music lessons and also how well they are helped with maths.

**Key:** A=F B=F C=F D=T E=T  |  `MA-ch06.65`  |  *None*  |  source: Pearl's Ladder — Rungs 1 and 2

- A (false): Playing causes the practice hours and they may then affect maths scores, so they are on the path from treatment to outcome.
- B (false): It is an effect of the treatment, so it cannot be a cause of it.
- C (false): It is an effect of the outcome, not a cause of either variable.
- D (true): Income influences both the treatment and the outcome, so it is a confounder.
- E (true): Parental education influences both the treatment and the outcome, so it is a confounder.

**20.** A report says: "ads and sales are correlated, so ad spend is a confounder of sales", and also treats the correlation as proof that ads drive sales. Check each statement that is true.  *(5 points)*

- [ ] A. The correlation coefficient measures how well a nonlinear curve fits the data.
- [ ] B. A strong correlation shows that one variable causes the other.
- [ ] C. A spurious correlation is an association not due to a causal link between the variables.
- [ ] D. A confounder is a common cause of both the exposure and the outcome.
- [ ] E. A correlation of zero shows the variables are independent.

**Key:** A=F B=F C=T D=T E=F  |  `MA-jargon.80`  |  *Jargon test: wrong word, right word*  |  source: Correlation, confounder, spurious correlation

- A (false): The standard correlation coefficient measures linear association.
- B (false): Association alone does not establish a causal direction.
- C (true): It can arise from chance or a confounder.
- D (true): It creates association without a direct causal link.
- E (false): Zero linear correlation leaves room for a nonlinear relationship.
