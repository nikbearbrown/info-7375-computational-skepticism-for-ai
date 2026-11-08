# INFO 7375 Computational Skepticism for AI: practice exam 05

**PRACTICE FORM. Drawn at random from the question bank; not the real exam; not signed off by the instructor.**

20 questions, 5 points each, 100 points. Name: ______________________

**Scoring.** Five statements, each true or false, 1 point each. The student checks the statements they believe are true. A statement scores 1 point if it is checked and true, or unchecked and false; otherwise 0. Read every statement on its own and decide whether it is true by itself. Strong words (always, never, every, proves) are often what makes a statement false, but a strong-sounding statement is not false for sounding strong.

---

**1.** A team monitors input features in production against the training data. Check each statement that is true.  *(5 points)*

- [ ] A. A drift alarm shows that accuracy has dropped.
- [ ] B. A two-sample Kolmogorov-Smirnov test needs labels for production rows.
- [ ] C. Population stability index compares binned distributions of a feature between two periods.
- [ ] D. Data drift is a change in the distribution of input features between reference data and new data.
- [ ] E. A drift check measures model accuracy on production data.

**2.** After a new camera model is introduced, the distribution of input images changes, but the rule that links an image to its label has not changed. Check each statement that is true.  *(5 points)*

- [ ] A. Covariate shift means the labelling rule changed.
- [ ] B. Concept drift and covariate shift are two names for the same thing.
- [ ] C. This is covariate shift.
- [ ] D. Label shift, also called prior shift, is a change in P(y) with P(x | y) unchanged.
- [ ] E. Concept drift is a change in P(y | x), the relationship between inputs and target.

**3.** A company wants to meet several fairness criteria at once and asks why the metrics disagree. Check each statement that is true.  *(5 points)*

- [ ] A. Different metrics encode different notions of fairness, so the chosen metric should be stated with the reason.
- [ ] B. Fairness criteria are compatible in ordinary conditions, so a model meets each at the same time.
- [ ] C. A fairness trade-off means improving one criterion can worsen another criterion or overall accuracy.
- [ ] D. Choosing among fairness metrics is a value judgement about context, not just a statistical decision.
- [ ] E. Raising a threshold for one group to equalise true positive rates can change selection rates across groups.

**4.** A school district builds a model to identify students who need extra academic support. The training label is whether the student received a failing grade the next term. Check each statement that is true.  *(5 points)*

- [ ] A. A failing grade is the construct, and need for support is the measurement.
- [ ] B. High accuracy on the failing-grade label establishes construct validity.
- [ ] C. Comparing the label with an independent measure of need, such as assessments or counselor review, is a way to assess construct validity.
- [ ] D. Operationalizing a construct means collecting more rows of the same measurement.
- [ ] E. If agreement between the label and an independent measure is the same across schools, differential measurement is present.

**5.** A classifier says 0.8 and is right about 80% of the time at that score, but it ranks positive cases above negative cases poorly. Check each statement that is true.  *(5 points)*

- [ ] A. The model is well calibrated.
- [ ] B. Calibration describes agreement between predicted probabilities and observed frequencies.
- [ ] C. Discrimination is the ability to rank positives above negatives, often summarised by AUC.
- [ ] D. The model has high discrimination.
- [ ] E. Accuracy is the same quantity as calibration.

**6.** Model A beats Model B on easy questions and also on hard questions, yet Model B has the higher overall accuracy because Model B was tested mostly on easy questions. Which statements name this correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The difference in question mix between the two models is a confounder of the overall comparison.
- [ ] B. Overall accuracy is a conditional accuracy given question difficulty.
- [ ] C. A trend that holds in each group and reverses in the combined data is Simpson's paradox.
- [ ] D. Stratifying by question difficulty is a sound fix when difficulty is a property of the question and not an effect of the model.
- [ ] E. Overall accuracy is a weighted average of the group accuracies, with weights set by each model's own mix of questions.

**7.** A safety filter passes 300 of 300 independent test prompts, and the report says "the failure rate is 0%". Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. Zero observed failures give an upper confidence bound on the failure rate and do not establish a point value of zero.
- [ ] B. A higher confidence level gives a lower upper bound on the failure rate.
- [ ] C. By the rule of three, the 95% upper confidence bound after n failure-free tests is about 3 divided by n.
- [ ] D. The bound applies to inputs outside the distribution of the test prompts.
- [ ] E. Near-duplicate test prompts raise the effective number of independent tests.

**8.** An analyst writes: "this 95 percent confidence interval means there is a 95 percent probability the true effect lies inside it." Check each statement that is true.  *(5 points)*

- [ ] A. The terms credible interval and confidence interval are interchangeable.
- [ ] B. A p-value is the posterior probability that the null hypothesis is true.
- [ ] C. A credible interval is a range built from repeated sampling in the long run.
- [ ] D. The 95 percent in a confidence interval refers to the long-run share of such intervals that cover the true value.
- [ ] E. The analyst's sentence describes a credible interval, not a confidence interval.

**9.** A lender tells a denied applicant: "had your income been 6,000 higher, you would have been approved." Check each statement that is true.  *(5 points)*

- [ ] A. A counterfactual explanation requires an intrinsically interpretable model.
- [ ] B. It guarantees approval after the income rises, even if the lender retrains the model.
- [ ] C. It is a feature importance score for income.
- [ ] D. This is a counterfactual explanation: a change to the inputs that would flip the outcome.
- [ ] E. It describes a nearby alternative input, not the model's full internal logic.

**10.** A manager asks an AI agent: "Check the data is clean and correct and from a trusted source." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Report lineage as the licence and the author.
- [ ] B. Record the provenance, meaning the source and collection method.
- [ ] C. Run a schema check on column types and required fields.
- [ ] D. Verify that test rows do not leak by deleting the test set.
- [ ] E. Run semantic checks such as plausible value ranges.

**11.** A team distinguishes adversarial examples from noisy inputs. Check each statement that is true.  *(5 points)*

- [ ] A. Random noise is a perturbation not chosen to target the model.
- [ ] B. A model robust to random noise is robust to adversarial examples.
- [ ] C. An adversarial example is an input deliberately perturbed, often by a small amount, to cause a wrong output.
- [ ] D. An adversarial example can look nearly unchanged to a human.
- [ ] E. Adversarial perturbations can be found using the model's gradients or by querying it.

**12.** A review board states fairness criteria and needs the exact term for each. Check each statement that is true.  *(5 points)*

- [ ] A. Equal opportunity asks for equal false positive rates across groups.
- [ ] B. Predictive parity asks for equal true positive rates across groups.
- [ ] C. Calibration within groups asks for equal selection rates.
- [ ] D. Demographic parity asks for equal positive-prediction rates across groups.
- [ ] E. Equalized odds asks for equal true positive rates and equal false positive rates across groups.

**13.** A team must treat a numeric predictor with 15% blank values before fitting a regression. They are comparing complete-case analysis, mean filling and multiple imputation. Check each statement that is true.  *(5 points)*

- [ ] A. Under MNAR, multiple imputation corrects bias without further assumptions.
- [ ] B. Multiple imputation assumes MAR given the variables in the imputation model.
- [ ] C. Complete-case analysis is also called listwise deletion.
- [ ] D. Mean filling assumes MCAR.
- [ ] E. Sensitivity analysis reports how results change under alternative assumptions about the missing values.

**14.** A report says "p = 0.03, so there is a 3% chance the null hypothesis is true." Check each statement that is true.  *(5 points)*

- [ ] A. A posterior probability of the null needs no prior.
- [ ] B. The p-value is the probability of data at least this extreme if the null hypothesis is true.
- [ ] C. The p-value is the posterior probability of the null hypothesis.
- [ ] D. A small p-value gives the probability that the alternative hypothesis is true.
- [ ] E. The report confuses P(data | null) with P(null | data).

**15.** An engineer runs 400 independent evaluation prompts and 320 pass, an observed pass rate of 0.80. Which statements use the terms correctly? Check each statement that is true.  *(5 points)*

- [ ] A. The standard error and the standard deviation of the individual pass-or-fail outcomes are the same quantity.
- [ ] B. The standard error of a proportion is largest when p is near 0 or 1.
- [ ] C. Doubling the number of prompts halves the standard error.
- [ ] D. The standard error of the pass rate measures how much the sample proportion varies from one sample to another.
- [ ] E. The margin of error of a 95% interval is the critical value (about 1.96) times the standard error.

**16.** An analyst writes: "I tuned the hyperparameters on the test set, then reported the best test score." Check each statement that is true.  *(5 points)*

- [ ] A. Tuning on the test set is the same as cross-validation.
- [ ] B. Data leakage is information from outside the training data, such as test labels, influencing the training.
- [ ] C. A validation set is used to tune hyperparameters and choose between models.
- [ ] D. A test set is held back for the final estimate of generalization.
- [ ] E. Tuning on the test set leaks information, so the reported score is optimistic.

**17.** A model trained on hospital records predicts lower pneumonia mortality for patients with asthma, because those patients were sent straight to intensive care. Check each statement that is true.  *(5 points)*

- [ ] A. Intensive care treatment acts as a confounder that explains the pattern.
- [ ] B. The pattern shows that asthma protects patients from dying of pneumonia.
- [ ] C. A large attribution to asthma shows its causal effect on survival.
- [ ] D. A correlation in observational data can reflect a confounder instead of a causal effect.
- [ ] E. The model has learned a correlation present in the records.

**18.** A spec says the dataset has "labels" and a reviewer asks whether they are ground truth. Check each statement that is true.  *(5 points)*

- [ ] A. Label noise refers to random features added to the inputs.
- [ ] B. Ground truth is the model's predicted value.
- [ ] C. Inter-annotator agreement measures how close the labels are to ground truth.
- [ ] D. Labels from a single annotator are ground truth.
- [ ] E. A label is the target value attached to an example, whether or not it is correct.

**19.** A reviewer asks for a stress test and a perturbation test of a text classifier. Check each statement that is true.  *(5 points)*

- [ ] A. A stress test is run on the training set to measure fit.
- [ ] B. A stress test evaluates a model under extreme or rare conditions beyond typical inputs.
- [ ] C. A perturbation test applies small controlled changes to inputs and checks that the output stays stable.
- [ ] D. A changed output under a label-preserving perturbation signals fragility.
- [ ] E. Typo injection and paraphrasing are perturbations for a text model.

**20.** A review board describes requirements in words and asks which fairness criterion each one names. Check each statement that is true.  *(5 points)*

- [ ] A. "Approval rates among repayers and among defaulters both match across groups" names demographic parity.
- [ ] B. "The share approved is the same for each group regardless of repayment" names equalized odds.
- [ ] C. "Among people who truly repay, the approval rate is the same for each group" names equal opportunity.
- [ ] D. "A score of 0.7 should mean about 70 percent observed repayment in each group" names calibration within groups.
- [ ] E. "Among people approved, the share who repay is the same for each group" names predictive parity.
