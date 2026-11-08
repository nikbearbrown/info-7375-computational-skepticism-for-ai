# INFO 7375 Computational Skepticism for AI: practice exam 05: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A team monitors input features in production against the training data. Check each statement that is true.  *(5 points)*

- [ ] A. A drift alarm shows that accuracy has dropped.
- [ ] B. A two-sample Kolmogorov-Smirnov test needs labels for production rows.
- [ ] C. Population stability index compares binned distributions of a feature between two periods.
- [ ] D. Data drift is a change in the distribution of input features between reference data and new data.
- [ ] E. A drift check measures model accuracy on production data.

**Key:** A=F B=F C=T D=T E=F  |  `MA-jargon.21`  |  *Jargon test: data validation and provenance*  |  source: Data drift checks

- A (false): Inputs can drift without a change in accuracy.
- B (false): It compares feature distributions and needs no labels.
- C (true): It scores how much a binned distribution moved.
- D (true): It compares feature distributions across time.
- E (false): Drift checks compare inputs; accuracy needs outcomes.

**2.** After a new camera model is introduced, the distribution of input images changes, but the rule that links an image to its label has not changed. Check each statement that is true.  *(5 points)*

- [ ] A. Covariate shift means the labelling rule changed.
- [ ] B. Concept drift and covariate shift are two names for the same thing.
- [ ] C. This is covariate shift.
- [ ] D. Label shift, also called prior shift, is a change in P(y) with P(x | y) unchanged.
- [ ] E. Concept drift is a change in P(y | x), the relationship between inputs and target.

**Key:** A=F B=F C=T D=T E=T  |  `MA-jargon.25`  |  *Jargon test: robustness and distribution shift*  |  source: Covariate shift vs concept drift vs label shift

- A (false): A changed labelling rule is concept drift.
- B (false): They change different parts of the joint distribution.
- C (true): Covariate shift is a change in P(x) with P(y | x) unchanged.
- D (true): The class proportions moved but the class-conditional inputs did not.
- E (true): The mapping itself has moved.

**3.** A company wants to meet several fairness criteria at once and asks why the metrics disagree. Check each statement that is true.  *(5 points)*

- [ ] A. Different metrics encode different notions of fairness, so the chosen metric should be stated with the reason.
- [ ] B. Fairness criteria are compatible in ordinary conditions, so a model meets each at the same time.
- [ ] C. A fairness trade-off means improving one criterion can worsen another criterion or overall accuracy.
- [ ] D. Choosing among fairness metrics is a value judgement about context, not just a statistical decision.
- [ ] E. Raising a threshold for one group to equalise true positive rates can change selection rates across groups.

**Key:** A=T B=F C=T D=T E=T  |  `MA-jargon.61`  |  *Jargon test: bias and fairness*  |  source: Fairness trade-off

- A (true): The metric choice is part of the claim being made.
- B (false): They are generally incompatible when base rates differ.
- C (true): Criteria can conflict, so gains on one come with costs elsewhere.
- D (true): The right criterion depends on the harms involved.
- E (true): Adjusting a threshold moves several rates at once.

**4.** A school district builds a model to identify students who need extra academic support. The training label is whether the student received a failing grade the next term. Check each statement that is true.  *(5 points)*

- [ ] A. A failing grade is the construct, and need for support is the measurement.
- [ ] B. High accuracy on the failing-grade label establishes construct validity.
- [ ] C. Comparing the label with an independent measure of need, such as assessments or counselor review, is a way to assess construct validity.
- [ ] D. Operationalizing a construct means collecting more rows of the same measurement.
- [ ] E. If agreement between the label and an independent measure is the same across schools, differential measurement is present.

**Key:** A=F B=F C=T D=F E=F  |  `MA-ch03.38`  |  *None*  |  source: Construct, operationalization and construct validity

- A (false): The construct is the underlying concept, need for support, and the failing grade is its measurable proxy.
- B (false): Accuracy shows the proxy is predicted well, not that it measures need.
- C (true): Agreement with an independent measure of the same concept is evidence of validity.
- D (false): Operationalizing means defining a measurable variable that stands for the concept.
- E (false): Differential measurement means the label tracks the construct differently across groups, which shows as unequal agreement.

**5.** A classifier says 0.8 and is right about 80% of the time at that score, but it ranks positive cases above negative cases poorly. Check each statement that is true.  *(5 points)*

- [ ] A. The model is well calibrated.
- [ ] B. Calibration describes agreement between predicted probabilities and observed frequencies.
- [ ] C. Discrimination is the ability to rank positives above negatives, often summarised by AUC.
- [ ] D. The model has high discrimination.
- [ ] E. Accuracy is the same quantity as calibration.

**Key:** A=T B=T C=T D=F E=F  |  `MA-jargon.1`  |  *Jargon test: probability and confidence*  |  source: Calibration vs accuracy vs discrimination

- A (true): Calibration means predicted probabilities match observed frequencies.
- B (true): That agreement is the definition of calibration.
- C (true): AUC measures how well scores separate the classes.
- D (false): Discrimination is ranking ability, which is poor here.
- E (false): Accuracy is the share of correct predictions; calibration is about probability values.

**6.** Model A beats Model B on easy questions and also on hard questions, yet Model B has the higher overall accuracy because Model B was tested mostly on easy questions. Which statements name this correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The difference in question mix between the two models is a confounder of the overall comparison.
- [ ] B. Overall accuracy is a conditional accuracy given question difficulty.
- [ ] C. A trend that holds in each group and reverses in the combined data is Simpson's paradox.
- [ ] D. Stratifying by question difficulty is a sound fix when difficulty is a property of the question and not an effect of the model.
- [ ] E. Overall accuracy is a weighted average of the group accuracies, with weights set by each model's own mix of questions.

**Key:** A=T B=F C=T D=T E=T  |  `MA-1.8`  |  *1. Probability, conditional probability and Bayes' theorem*  |  source: Simpson's paradox, confounder, stratification

- A (true): The mix of easy and hard questions is linked to both which model is scored and the accuracy obtained.
- B (false): Overall accuracy ignores difficulty; accuracy within a difficulty level is the conditional quantity.
- C (true): Simpson's paradox is a reversal between group-level and aggregate comparisons.
- D (true): Stratification compares like with like on a variable that is not downstream of the treatment.
- E (true): Different weights can reverse the order of the averages.

**7.** A safety filter passes 300 of 300 independent test prompts, and the report says "the failure rate is 0%". Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Zero observed failures give an upper confidence bound on the failure rate and do not establish a point value of zero.
- [ ] B. A higher confidence level gives a lower upper bound on the failure rate.
- [ ] C. By the rule of three, the 95% upper confidence bound after n failure-free tests is about 3 divided by n.
- [ ] D. The bound applies to inputs outside the distribution of the test prompts.
- [ ] E. Near-duplicate test prompts raise the effective number of independent tests.

**Key:** A=T B=F C=T D=F E=F  |  `MA-3.10`  |  *3. Sampling, the central limit theorem and inference*  |  source: Upper confidence bound, rule of three, representativeness

- A (true): A rare failure can be missed by chance in a limited test.
- B (false): Demanding more confidence widens the bound, so it rises.
- C (true): For n = 300 the bound is about 1%.
- D (false): The bound speaks only to inputs like those sampled; uncovered or adversarial inputs lie outside it.
- E (false): Near-duplicates are positively correlated and carry less independent information, so the effective sample size drops.

**8.** An analyst writes: "this 95 percent confidence interval means there is a 95 percent probability the true effect lies inside it." Check each statement that is true.  *(5 points)*

- [ ] A. The terms credible interval and confidence interval are interchangeable.
- [ ] B. A p-value is the posterior probability that the null hypothesis is true.
- [ ] C. A credible interval is a range built from repeated sampling in the long run.
- [ ] D. The 95 percent in a confidence interval refers to the long-run share of such intervals that cover the true value.
- [ ] E. The analyst's sentence describes a credible interval, not a confidence interval.

**Key:** A=F B=F C=F D=T E=T  |  `MA-jargon.70`  |  *Jargon test: wrong word, right word*  |  source: Confidence interval vs credible interval

- A (false): They rest on different definitions of probability.
- B (false): A p-value is computed assuming the null hypothesis, and it is not a posterior probability.
- C (false): That describes a confidence interval; a credible interval is a Bayesian posterior range.
- D (true): The coverage is a property of the procedure over repeated samples.
- E (true): A direct probability statement about the parameter is Bayesian.

**9.** A lender tells a denied applicant: "had your income been 6,000 higher, you would have been approved." Check each statement that is true.  *(5 points)*

- [ ] A. A counterfactual explanation requires an intrinsically interpretable model.
- [ ] B. It guarantees approval after the income rises, even if the lender retrains the model.
- [ ] C. It is a feature importance score for income.
- [ ] D. This is a counterfactual explanation: a change to the inputs that would flip the outcome.
- [ ] E. It describes a nearby alternative input, not the model's full internal logic.

**Key:** A=F B=F C=F D=T E=T  |  `MA-jargon.47`  |  *Jargon test: explainability*  |  source: Counterfactual explanation

- A (false): Counterfactuals are usually computed post-hoc for black-box models.
- B (false): The statement is about the current model, and a retrained model can decide differently.
- C (false): Feature importance ranks inputs; a counterfactual gives a specific change.
- D (true): That is the definition of a counterfactual explanation.
- E (true): A counterfactual answers one what-if, not how the whole model works.

**10.** A manager asks an AI agent: "Check the data is clean and correct and from a trusted source." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Report lineage as the licence and the author.
- [ ] B. Record the provenance, meaning the source and collection method.
- [ ] C. Run a schema check on column types and required fields.
- [ ] D. Verify that test rows do not leak by deleting the test set.
- [ ] E. Run semantic checks such as plausible value ranges.

**Key:** A=F B=T C=T D=F E=T  |  `MA-jargon.24`  |  *Jargon test: data validation and provenance*  |  source: Rewrite a vague data-quality prompt

- A (false): Lineage is the transformation path.
- B (true): Provenance covers origin.
- C (true): That names the structural check.
- D (false): Leakage checks look for overlap such as duplicates, and deleting the test set removes the evaluation.
- E (true): That names the domain-meaning check.

**11.** A team distinguishes adversarial examples from noisy inputs. Check each statement that is true.  *(5 points)*

- [ ] A. Random noise is a perturbation not chosen to target the model.
- [ ] B. A model robust to random noise is robust to adversarial examples.
- [ ] C. An adversarial example is an input deliberately perturbed, often by a small amount, to cause a wrong output.
- [ ] D. An adversarial example can look nearly unchanged to a human.
- [ ] E. Adversarial perturbations can be found using the model's gradients or by querying it.

**Key:** A=T B=F C=T D=T E=T  |  `MA-jargon.29`  |  *Jargon test: robustness and distribution shift*  |  source: Adversarial example vs noise

- A (true): It is not optimised against the model.
- B (false): Targeted perturbations can succeed where random ones fail.
- C (true): The perturbation is chosen to attack the model.
- D (true): The change can be small and still flip the output.
- E (true): Attacks use model access to search for failures.

**12.** A review board states fairness criteria and needs the exact term for each. Check each statement that is true.  *(5 points)*

- [ ] A. Equal opportunity asks for equal false positive rates across groups.
- [ ] B. Predictive parity asks for equal true positive rates across groups.
- [ ] C. Calibration within groups asks for equal selection rates.
- [ ] D. Demographic parity asks for equal positive-prediction rates across groups.
- [ ] E. Equalized odds asks for equal true positive rates and equal false positive rates across groups.

**Key:** A=F B=F C=F D=T E=T  |  `MA-jargon.57`  |  *Jargon test: bias and fairness*  |  source: Fairness criteria definitions

- A (false): Equal opportunity asks for equal true positive rates.
- B (false): Predictive parity asks for equal precision, also called positive predictive value.
- C (false): Calibration within groups asks that a score mean the same observed frequency in each group.
- D (true): It compares selection rates.
- E (true): It matches both error-related rates.

**13.** A team must treat a numeric predictor with 15% blank values before fitting a regression. They are comparing complete-case analysis, mean filling and multiple imputation. Check each statement that is true.  *(5 points)*

- [ ] A. Under MNAR, multiple imputation corrects bias without further assumptions.
- [ ] B. Multiple imputation assumes MAR given the variables in the imputation model.
- [ ] C. Complete-case analysis is also called listwise deletion.
- [ ] D. Mean filling assumes MCAR.
- [ ] E. Sensitivity analysis reports how results change under alternative assumptions about the missing values.

**Key:** A=F B=T C=T D=T E=T  |  `MA-ch03.35`  |  *None*  |  source: Choosing among missing-data treatments

- A (false): MNAR calls for explicit modeling of the missingness or sensitivity analysis, not a method that assumes MAR.
- B (true): Multiple imputation draws plausible values conditional on the observed variables in the model.
- C (true): Listwise deletion removes any row with a blank, which is the complete-case approach.
- D (true): Mean filling treats missing values as typical of the observed ones, which holds under MCAR.
- E (true): Sensitivity analysis shows how much conclusions depend on an untestable assumption.

**14.** A report says "p = 0.03, so there is a 3% chance the null hypothesis is true." Check each statement that is true.  *(5 points)*

- [ ] A. A posterior probability of the null needs no prior.
- [ ] B. The p-value is the probability of data at least this extreme if the null hypothesis is true.
- [ ] C. The p-value is the posterior probability of the null hypothesis.
- [ ] D. A small p-value gives the probability that the alternative hypothesis is true.
- [ ] E. The report confuses P(data | null) with P(null | data).

**Key:** A=F B=T C=F D=F E=T  |  `MA-jargon.4`  |  *Jargon test: probability and confidence*  |  source: p-value vs posterior

- A (false): A posterior comes from combining a prior with the likelihood.
- B (true): That is the definition of a p-value.
- C (false): A posterior probability is P(null | data), a different quantity.
- D (false): It does not give a probability for either hypothesis.
- E (true): The p-value is the first; the quoted sentence claims the second.

**15.** An engineer runs 400 independent evaluation prompts and 320 pass, an observed pass rate of 0.80. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The standard error and the standard deviation of the individual pass-or-fail outcomes are the same quantity.
- [ ] B. The standard error of a proportion is largest when p is near 0 or 1.
- [ ] C. Doubling the number of prompts halves the standard error.
- [ ] D. The standard error of the pass rate measures how much the sample proportion varies from one sample to another.
- [ ] E. The margin of error of a 95% interval is the critical value (about 1.96) times the standard error.

**Key:** A=F B=F C=F D=T E=T  |  `MA-3.1`  |  *3. Sampling, the central limit theorem and inference*  |  source: Standard error, margin of error, confidence interval

- A (false): The standard deviation describes single outcomes; the standard error describes the estimate and shrinks as n grows.
- B (false): The quantity p(1 − p) peaks at p = 0.5, so the standard error is largest there.
- C (false): The standard error falls in proportion to 1 over the square root of n, so doubling n shrinks it by about 29%.
- D (true): A standard error is the standard deviation of a statistic across repeated samples.
- E (true): Margin of error = critical value × standard error.

**16.** An analyst writes: "I tuned the hyperparameters on the test set, then reported the best test score." Check each statement that is true.  *(5 points)*

- [ ] A. Tuning on the test set is the same as cross-validation.
- [ ] B. Data leakage is information from outside the training data, such as test labels, influencing the training.
- [ ] C. A validation set is used to tune hyperparameters and choose between models.
- [ ] D. A test set is held back for the final estimate of generalization.
- [ ] E. Tuning on the test set leaks information, so the reported score is optimistic.

**Key:** A=F B=T C=T D=T E=T  |  `MA-jargon.78`  |  *Jargon test: wrong word, right word*  |  source: Validation set, test set, leakage

- A (false): Cross-validation tunes on folds of the training data, not on the held-back test set.
- B (true): Leakage breaks the separation between fitting and evaluation.
- C (true): It guides model selection.
- D (true): It is used once the choices are made.
- E (true): The test data influenced the choices, so it no longer measures unseen performance.

**17.** A model trained on hospital records predicts lower pneumonia mortality for patients with asthma, because those patients were sent straight to intensive care. Check each statement that is true.  *(5 points)*

- [ ] A. Intensive care treatment acts as a confounder that explains the pattern.
- [ ] B. The pattern shows that asthma protects patients from dying of pneumonia.
- [ ] C. A large attribution to asthma shows its causal effect on survival.
- [ ] D. A correlation in observational data can reflect a confounder instead of a causal effect.
- [ ] E. The model has learned a correlation present in the records.

**Key:** A=T B=F C=F D=T E=T  |  `MA-jargon.49`  |  *Jargon test: explainability*  |  source: Correlation vs causation

- A (true): The treatment affects both who has the label of asthma-care and the outcome.
- B (false): The association comes from the treatment pathway, not a protective effect.
- C (false): An attribution describes the model's reliance, not an intervention result.
- D (true): Confounding is the standard reason association differs from causation.
- E (true): It captured an association between asthma and outcome.

**18.** A spec says the dataset has "labels" and a reviewer asks whether they are ground truth. Check each statement that is true.  *(5 points)*

- [ ] A. Label noise refers to random features added to the inputs.
- [ ] B. Ground truth is the model's predicted value.
- [ ] C. Inter-annotator agreement measures how close the labels are to ground truth.
- [ ] D. Labels from a single annotator are ground truth.
- [ ] E. A label is the target value attached to an example, whether or not it is correct.

**Key:** A=F B=F C=F D=F E=T  |  `MA-jargon.22`  |  *Jargon test: data validation and provenance*  |  source: Labels vs ground truth

- A (false): Label noise means wrong or inconsistent labels.
- B (false): Ground truth is a reference for the real value, not a prediction.
- C (false): Agreement measures consistency among annotators, not correctness.
- D (false): One annotator can be wrong or inconsistent.
- E (true): Labels are assigned values and can contain errors.

**19.** A reviewer asks for a stress test and a perturbation test of a text classifier. Check each statement that is true.  *(5 points)*

- [ ] A. A stress test is run on the training set to measure fit.
- [ ] B. A stress test evaluates a model under extreme or rare conditions beyond typical inputs.
- [ ] C. A perturbation test applies small controlled changes to inputs and checks that the output stays stable.
- [ ] D. A changed output under a label-preserving perturbation signals fragility.
- [ ] E. Typo injection and paraphrasing are perturbations for a text model.

**Key:** A=F B=T C=T D=T E=T  |  `MA-jargon.30`  |  *Jargon test: robustness and distribution shift*  |  source: Stress test and perturbation

- A (false): Fit on training data is not a stress test.
- B (true): It probes the edges of expected use.
- C (true): It measures sensitivity to small input changes.
- D (true): The label should not change, so a change shows sensitivity.
- E (true): They change the surface of the input in a controlled way.

**20.** A review board describes requirements in words and asks which fairness criterion each one names. Check each statement that is true.  *(5 points)*

- [ ] A. "Approval rates among repayers and among defaulters both match across groups" names demographic parity.
- [ ] B. "The share approved is the same for each group regardless of repayment" names equalized odds.
- [ ] C. "Among people who truly repay, the approval rate is the same for each group" names equal opportunity.
- [ ] D. "A score of 0.7 should mean about 70 percent observed repayment in each group" names calibration within groups.
- [ ] E. "Among people approved, the share who repay is the same for each group" names predictive parity.

**Key:** A=F B=F C=T D=T E=T  |  `MA-jargon.58`  |  *Jargon test: bias and fairness*  |  source: Matching descriptions to fairness criteria

- A (false): That is equalized odds.
- B (false): That is demographic parity.
- C (true): Equal opportunity matches true positive rates.
- D (true): Calibration compares score to observed frequency per group.
- E (true): Predictive parity compares precision across groups.
