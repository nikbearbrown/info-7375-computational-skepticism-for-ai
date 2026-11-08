# Jargon test: bias and fairness

## MA-jargon.53

An audit lists four situations, and the team labels each with a bias term. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A thermometer that reads two degrees high at one clinic produces measurement bias.
- [ ] B. Training on past customers who were approved for loans, since they have repayment outcomes, produces selection bias.
- [ ] C. A scale that reads high is an example of sampling bias.
- [ ] D. Annotators who label one dialect as toxic more often produce label bias.
- [ ] E. Label bias is another name for overfitting.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Measurement bias is systematic error in how a value is recorded.
- B: The process that decides who enters the data is related to the outcome.
- C: That is measurement bias; sampling bias concerns who ends up in the sample.
- D: Label bias is systematic error in the assigned target labels.
- E: Label bias is an error in labels, while overfitting is poor generalization.

**Source:** Sampling, selection, measurement and label bias

## MA-jargon.54

An analyst says that labels came from reviewers who judged applicants from one neighbourhood more harshly, so the problem is sampling bias. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The problem described is label bias.
- [ ] B. Sampling bias concerns who ends up in the data, not how labels were assigned.
- [ ] C. Resampling to match population group proportions fixes label bias.
- [ ] D. Collecting more rows from the same reviewers removes the problem.
- [ ] E. Label bias can exist when the sample matches the target population in group proportions.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The target labels carry systematic reviewer error.
- B: Sampling bias is about the makeup of the sample.
- C: Resampling changes group makeup but leaves the label errors in place.
- D: More rows with the same biased labels repeat the bias.
- E: The two problems are independent of each other.

**Source:** Label bias vs sampling bias

## MA-jargon.55

A hiring model is trained on twenty years of accurate, well-sampled records that show few women hired into engineering. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Collecting a larger random sample removes historical bias.
- [ ] B. Historical bias can be present when sampling and measurement are sound.
- [ ] C. Historical bias is a type of measurement bias because the records are inaccurate.
- [ ] D. Historical bias requires that the records contain data-entry errors.
- [ ] E. This is historical bias: accurate data that reflect a world containing past inequity.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: A bigger faithful sample reproduces the same inequity.
- B: It does not depend on a flaw in data collection.
- C: The records are accurate; the bias lies in the world they describe.
- D: Errors are not needed; accurate records can carry it.
- E: Historical bias comes from the world, not from collection errors.

**Source:** Historical bias

## MA-jargon.56

A lender removes race from the inputs of its approval model but keeps zip code, which is correlated with race. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A proxy variable is itself a protected attribute.
- [ ] B. Race is a protected attribute: a characteristic that law or policy shields from discrimination.
- [ ] C. Removing zip code guarantees the outputs are independent of race.
- [ ] D. Dropping the protected attribute from the inputs, called fairness through unawareness, can leave a proxy in place.
- [ ] E. Zip code here acts as a proxy variable for race.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A proxy is an ordinary input that stands in for one.
- B: Protected attributes are the characteristics fairness rules refer to.
- C: Other correlated inputs can still carry the information.
- D: Unawareness removes the column but not correlated information.
- E: A proxy is an input correlated enough with a protected attribute to carry its information.

**Source:** Protected attribute and proxy variable

## MA-jargon.57

A review board states fairness criteria and needs the exact term for each. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal opportunity asks for equal false positive rates across groups.
- [ ] B. Predictive parity asks for equal true positive rates across groups.
- [ ] C. Calibration within groups asks for equal selection rates.
- [ ] D. Demographic parity asks for equal positive-prediction rates across groups.
- [ ] E. Equalized odds asks for equal true positive rates and equal false positive rates across groups.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Equal opportunity asks for equal true positive rates.
- B: Predictive parity asks for equal precision, also called positive predictive value.
- C: Calibration within groups asks that a score mean the same observed frequency in each group.
- D: It compares selection rates.
- E: It matches both error-related rates.

**Source:** Fairness criteria definitions

## MA-jargon.58

A review board describes requirements in words and asks which fairness criterion each one names. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Approval rates among repayers and among defaulters both match across groups" names demographic parity.
- [ ] B. "The share approved is the same for each group regardless of repayment" names equalized odds.
- [ ] C. "Among people who truly repay, the approval rate is the same for each group" names equal opportunity.
- [ ] D. "A score of 0.7 should mean about 70 percent observed repayment in each group" names calibration within groups.
- [ ] E. "Among people approved, the share who repay is the same for each group" names predictive parity.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: That is equalized odds.
- B: That is demographic parity.
- C: Equal opportunity matches true positive rates.
- D: Calibration compares score to observed frequency per group.
- E: Predictive parity compares precision across groups.

**Source:** Matching descriptions to fairness criteria

## MA-jargon.59

A regulator asks whether a screening tool shows disparate treatment, disparate impact, or both. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Disparate treatment means deciding differently for people because of a protected attribute, such as using race as an input.
- [ ] B. Disparate treatment describes unequal outcome rates regardless of how decisions are made.
- [ ] C. Disparate impact requires proof of intent to discriminate.
- [ ] D. A model that does not take the protected attribute as input is free of disparate impact.
- [ ] E. Disparate impact means a neutral-looking practice produces substantially different outcomes across groups.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It concerns the basis for the decision.
- B: That is closer to disparate impact.
- C: Intent is part of disparate treatment, not disparate impact.
- D: Proxies can produce unequal outcomes without the attribute as an input.
- E: It concerns the effect of the practice.

**Source:** Disparate treatment vs disparate impact

## MA-jargon.60

Two groups have different shares of people who truly have the positive outcome, and a classifier is imperfect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A base-rate difference is evidence that the model is biased.
- [ ] B. With differing base rates and an imperfect classifier, calibration within groups and equalized odds generally do not hold together.
- [ ] C. The base rate is the proportion of a group that has the positive outcome.
- [ ] D. The base rate is the same as a group's false positive rate.
- [ ] E. A base-rate difference in the data can itself reflect historical bias.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A base-rate difference describes the data; the model can still be accurate.
- B: Known results show these criteria are in tension under unequal base rates.
- C: It is the prevalence of the outcome in the group.
- D: False positive rate is a model error rate, not outcome prevalence.
- E: Past inequity can shape which outcomes appear in the records.

**Source:** Base-rate difference

## MA-jargon.61

A company wants to meet several fairness criteria at once and asks why the metrics disagree. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Different metrics encode different notions of fairness, so the chosen metric should be stated with the reason.
- [ ] B. Fairness criteria are compatible in ordinary conditions, so a model meets each at the same time.
- [ ] C. A fairness trade-off means improving one criterion can worsen another criterion or overall accuracy.
- [ ] D. Choosing among fairness metrics is a value judgement about context, not just a statistical decision.
- [ ] E. Raising a threshold for one group to equalise true positive rates can change selection rates across groups.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: The metric choice is part of the claim being made.
- B: They are generally incompatible when base rates differ.
- C: Criteria can conflict, so gains on one come with costs elsewhere.
- D: The right criterion depends on the harms involved.
- E: Adjusting a threshold moves several rates at once.

**Source:** Fairness trade-off

## MA-jargon.62

An audit finds similar error rates for women overall and for older people overall, but high error for older women. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Good results on each single attribute can hide poor results at the intersection.
- [ ] B. Reporting metrics by gender and by age separately is an intersectional analysis.
- [ ] C. Intersectional analysis examines subgroups defined by combinations of attributes.
- [ ] D. Intersectional means measuring fairness across different time periods.
- [ ] E. Intersectional subgroups can be small, so estimates there can be noisy.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Averages over a single attribute can mask a small subgroup.
- B: Separate breakdowns miss the combined subgroups.
- C: Intersections like older women are the unit of analysis.
- D: It refers to overlapping group memberships, not time.
- E: Small groups give wide uncertainty.

**Source:** Intersectional analysis

## MA-jargon.63

An analyst says: "the model has disparate treatment because the false negative rate is higher for group B, even though group is not an input." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equalized odds would also ask for matching false positive rates.
- [ ] B. A higher false negative rate means a lower true positive rate for that group.
- [ ] C. Equal opportunity is the criterion that targets a gap in true positive rates.
- [ ] D. Disparate treatment fits because group is not an input.
- [ ] E. Unequal error rates with no group input are closer to disparate impact.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Equalized odds covers both true and false positive rates.
- B: False negative rate plus true positive rate equal one.
- C: It requires matching true positive rates.
- D: Treatment concerns using the attribute, which did not happen here.
- E: The practice is neutral on its face but outcomes differ.

**Source:** Wrong word: disparate treatment

## MA-jargon.64

A face dataset is collected from social media photos of young adults and then used for people of many ages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Some texts call this representation bias.
- [ ] B. This is sampling bias: the sample's makeup differs from the population where the model will be used.
- [ ] C. It is measurement bias because the photos are inaccurate.
- [ ] D. Evaluating separately by age group helps reveal its effect.
- [ ] E. Adding more rows from the same source reduces it.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Representation bias is a near-synonym for sampling bias in this sense.
- B: Sampling bias is a mismatch between sample and target population.
- C: The photos can be accurate; the problem is who is represented.
- D: Subgroup evaluation exposes weaker performance on under-represented groups.
- E: More rows from the same source repeat the same skew.

**Source:** Sampling bias

## MA-jargon.65

A risk score is well calibrated across the whole population but its calibration has not been checked for each group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A reliability diagram is a standard way to inspect calibration.
- [ ] B. Overall calibration guarantees calibration within each group.
- [ ] C. Calibration is the same as accuracy.
- [ ] D. Calibration means that among people given score p, about a fraction p have the outcome.
- [ ] E. Calibration within groups asks for that match separately in each group.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: It plots predicted probability against observed frequency.
- B: Group-level miscalibration can cancel out in the average.
- C: Calibration compares probabilities to frequencies; accuracy counts correct decisions.
- D: Stated probability matches observed frequency.
- E: The condition is applied per group.

**Source:** Calibration

## MA-jargon.66

A default model is trained only on applicants who were approved in the past, then used to score the whole applicant pool. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Gathering more outcomes from the same approved group reduces it.
- [ ] B. This is label bias because annotators mislabelled applicants.
- [ ] C. Data from approved applicants alone are representative of the whole applicant pool.
- [ ] D. This is measurement bias because a feature's scale differs between applicants.
- [ ] E. This is selection bias: the data are a non-random subset chosen by a process related to the outcome.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The skew comes from the missing group, not the count of approved cases.
- B: No mislabelling is described; the issue is who is in the data.
- C: Rejected applicants are missing, so the data are skewed.
- D: Nothing about measurement is described.
- E: Past approvals decided who has outcomes.

**Source:** Selection bias
