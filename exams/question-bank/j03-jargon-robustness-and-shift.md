# Jargon test: robustness and distribution shift

## MA-jargon.25

After a new camera model is introduced, the distribution of input images changes, but the rule that links an image to its label has not changed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Covariate shift means the labelling rule changed.
- [ ] B. Concept drift and covariate shift are two names for the same thing.
- [ ] C. This is covariate shift.
- [ ] D. Label shift, also called prior shift, is a change in P(y) with P(x | y) unchanged.
- [ ] E. Concept drift is a change in P(y | x), the relationship between inputs and target.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A changed labelling rule is concept drift.
- B: They change different parts of the joint distribution.
- C: Covariate shift is a change in P(x) with P(y | x) unchanged.
- D: The class proportions moved but the class-conditional inputs did not.
- E: The mapping itself has moved.

**Source:** Covariate shift vs concept drift vs label shift

## MA-jargon.26

Match each situation to a shift term. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A seasonal change in input features alone is concept drift.
- [ ] B. A disease becomes more common while its symptoms given the disease stay the same, which is label shift.
- [ ] C. A change in P(y | x) is called covariate shift.
- [ ] D. Fraudsters change tactics so the same transaction features now mean fraud, which is concept drift.
- [ ] E. Photos arrive from a new phone model under the same labelling rule, which is label shift.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Changes confined to inputs are covariate shift.
- B: The class prior changed.
- C: That change is concept drift.
- D: The input-to-target relationship changed.
- E: Only the input distribution changed, so it is covariate shift.

**Source:** Match the shift term

## MA-jargon.27

A medical imaging model trained on one hospital's scanners is tested on a different hospital's. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An out-of-distribution input is drawn from a distribution different from the training data.
- [ ] B. A held-out test set from the same source as training is out-of-distribution.
- [ ] C. A model's softmax confidence is low on out-of-distribution inputs.
- [ ] D. Out-of-distribution detection aims to flag inputs unlike the training data.
- [ ] E. In-distribution inputs come from the same distribution as the training data.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: OOD inputs fall outside what training covered.
- B: Same-source data is in-distribution.
- C: Confidence can stay high on inputs unlike the training data.
- D: Detection is how such inputs are caught.
- E: That is the meaning of in-distribution.

**Source:** In-distribution vs out-of-distribution

## MA-jargon.28

A report says a model is robust because it scores well on a random held-out test set from its own source. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Good in-distribution test accuracy shows robustness.
- [ ] B. Robustness is performance staying acceptable under perturbation or shift.
- [ ] C. Robustness and generalization are identical.
- [ ] D. A model can generalize well in-distribution and still be fragile under shift.
- [ ] E. Generalization is performance on new data from the same distribution as the training data.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It shows generalization; robustness needs perturbed or shifted data.
- B: Robustness concerns conditions that differ from training.
- C: They test different conditions.
- D: The two properties can come apart.
- E: A same-source test measures generalization.

**Source:** Robustness vs generalization

## MA-jargon.29

A team distinguishes adversarial examples from noisy inputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Random noise is a perturbation not chosen to target the model.
- [ ] B. A model robust to random noise is robust to adversarial examples.
- [ ] C. An adversarial example is an input deliberately perturbed, often by a small amount, to cause a wrong output.
- [ ] D. An adversarial example can look nearly unchanged to a human.
- [ ] E. Adversarial perturbations can be found using the model's gradients or by querying it.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It is not optimised against the model.
- B: Targeted perturbations can succeed where random ones fail.
- C: The perturbation is chosen to attack the model.
- D: The change can be small and still flip the output.
- E: Attacks use model access to search for failures.

**Source:** Adversarial example vs noise

## MA-jargon.30

A reviewer asks for a stress test and a perturbation test of a text classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A stress test is run on the training set to measure fit.
- [ ] B. A stress test evaluates a model under extreme or rare conditions beyond typical inputs.
- [ ] C. A perturbation test applies small controlled changes to inputs and checks that the output stays stable.
- [ ] D. A changed output under a label-preserving perturbation signals fragility.
- [ ] E. Typo injection and paraphrasing are perturbations for a text model.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Fit on training data is not a stress test.
- B: It probes the edges of expected use.
- C: It measures sensitivity to small input changes.
- D: The label should not change, so a change shows sensitivity.
- E: They change the surface of the input in a controlled way.

**Source:** Stress test and perturbation

## MA-jargon.31

A demand-forecasting model scores well on a random split but poorly after deployment, and the data changes over time. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A random held-out split is the right choice when the data drifts over time.
- [ ] B. A held-out split sets aside data that is not used for training.
- [ ] C. A random split is not a held-out set.
- [ ] D. An out-of-time split trains on earlier data and tests on later data.
- [ ] E. Out-of-time evaluation better mimics deployment when the distribution changes over time.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: It mixes periods and hides the effect of drift.
- B: It provides an unseen evaluation set.
- C: A random split can still produce a held-out set.
- D: The test period follows the training period.
- E: Deployment always faces the future, which the split imitates.

**Source:** Held-out vs out-of-time split

## MA-jargon.32

A team plans monitoring for a deployed classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Input drift monitoring needs labels.
- [ ] B. Monitoring is finished once the model passes offline tests.
- [ ] C. Performance monitoring needs ground truth, which often arrives with delay.
- [ ] D. A feature distribution alert is the same as an accuracy drop.
- [ ] E. Monitoring tracks inputs, predictions and outcomes of a deployed model over time.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: Input drift compares feature distributions and needs no labels.
- B: Shift happens after release, so monitoring continues.
- C: Accuracy cannot be computed until outcomes are known.
- D: An alert concerns inputs and accuracy concerns outcomes.
- E: It is ongoing observation after release.

**Source:** Monitoring

## MA-jargon.33

A model that was well calibrated on its validation set is deployed on shifted data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Overconfidence under shift means accuracy exceeds stated confidence.
- [ ] B. Under distribution shift, calibration often degrades.
- [ ] C. A model calibrated on its validation set stays calibrated under shift.
- [ ] D. Calibration can be re-measured on a labelled sample of shifted data.
- [ ] E. Temperature scaling fitted on in-distribution data repairs calibration on shifted data.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: That is underconfidence.
- B: Stated probabilities stop matching observed frequencies.
- C: Calibration is tied to the distribution it was fitted on.
- D: A fresh reliability check shows the current gap.
- E: The fitted correction reflects the old distribution.

**Source:** Calibration under shift

## MA-jargon.34

A user prompts an AI: "The model got worse because the data changed." Choose the rewrites that use exact terms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Call a random perturbation an adversarial example.
- [ ] B. State whether P(x) changed, which is covariate shift, or P(y | x) changed, which is concept drift.
- [ ] C. Report accuracy on the training set to show robustness.
- [ ] D. Describe the held-out test as out-of-time if it is a random sample.
- [ ] E. Call it covariate shift if the class proportions changed.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Adversarial means deliberately targeted.
- B: That separates the two kinds of change.
- C: Training accuracy does not test robustness.
- D: An out-of-time split orders data by time.
- E: A change in class proportions is label shift.

**Source:** Rewrite a vague shift prompt

## MA-jargon.35

Fraud rises from 1% to 3% of transactions, and fraudulent transactions look the same as before. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. P(y) has changed.
- [ ] B. The decision threshold may need adjusting because the class prior changed.
- [ ] C. This is label shift, also called prior shift.
- [ ] D. P(x | y) is unchanged.
- [ ] E. This is concept drift.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: The proportion of fraud moved.
- B: The optimal threshold depends on the prior.
- C: The class prior changed.
- D: Fraud looks the same as before.
- E: Concept drift would need P(y | x) to change.

**Source:** Label (prior) shift

## MA-jargon.36

Match each description to its term. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A test image from the training source is out-of-distribution.
- [ ] B. Training on January to June and testing on July to December is an out-of-time split.
- [ ] C. Applying a random blur to an image is an adversarial example.
- [ ] D. Swapping a word for a synonym in a prompt is a perturbation.
- [ ] E. Testing a document model on very long documents is a stress test.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Same-source images are in-distribution.
- B: The test period follows training.
- C: A random blur is not targeted at the model.
- D: It is a small controlled input change.
- E: It pushes the model beyond typical inputs.

**Source:** Match robustness terms
