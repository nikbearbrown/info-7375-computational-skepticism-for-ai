# Chapter 7: Fairness metrics

## MA-ch07.1

A reviewer needs the exact name for each group fairness criterion of a binary classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal precision of favorable decisions across groups is equalized odds.
- [ ] B. Equal true-positive and equal false-positive rates across groups is equalized odds.
- [ ] C. Equal true-positive rates across groups is equal opportunity.
- [ ] D. Statistical parity is another name for demographic parity.
- [ ] E. Equal shares of favorable decisions across groups, whatever the true outcomes, is demographic parity.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Equal precision is predictive parity; equalized odds concerns true-positive and false-positive rates.
- B: Equalized odds is parity of both error-rate quantities conditional on the true outcome.
- C: Equal opportunity is parity of the rate at which truly qualified people receive the favorable decision.
- D: Both names describe equal selection rates across groups.
- E: Demographic parity compares selection rates and ignores the true outcome.

**Source:** Names of the group fairness criteria

## MA-ch07.2

An analyst is sorting out common rate names for a classifier that gives a favorable decision. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Positive predictive value is the share of favorable decisions that go to people who truly qualify.
- [ ] B. Specificity names the same quantity as the true-positive rate.
- [ ] C. Precision is another name for the false-positive rate.
- [ ] D. True-positive rate is also called recall or sensitivity.
- [ ] E. The false-positive rate is computed among people who received the favorable decision.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Positive predictive value is a synonym of precision.
- B: Specificity is the true-negative rate, one minus the false-positive rate.
- C: Precision is the share of favorable decisions that are correct; the false-positive rate is a different quantity.
- D: Each of these names the share of truly qualified people who receive the favorable decision.
- E: It is computed among people who truly do not qualify.

**Source:** Rate vocabulary: recall, precision, specificity

## MA-ch07.3

A reviewer lists what each fairness quantity conditions on. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A selection rate conditions on group membership and not on the true outcome.
- [ ] B. Precision conditions on people who received the favorable decision.
- [ ] C. A true-positive rate conditions on people who truly qualify.
- [ ] D. A false-positive rate conditions on people who received the favorable decision.
- [ ] E. Demographic parity conditions on the true outcome.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It is the share of a group's members receiving the favorable decision.
- B: It asks what share of favorable decisions are correct.
- C: It is measured within the set of true positives plus false negatives.
- D: It conditions on the true outcome being negative.
- E: It compares decisions across groups without reference to the true outcome.

**Source:** What each rate conditions on

## MA-ch07.4

An analyst tells an AI assistant, "Check that the model is fair by making sure accuracy is the same for men and women." Check each statement that is true. Each statement is worth 1 point (5 points total). about this prompt.

- [ ] A. Accuracy parity is another name for predictive parity.
- [ ] B. The prompt asks for accuracy parity, a different criterion from equalized odds.
- [ ] C. Replacing "accuracy" with "demographic parity" would keep the same meaning.
- [ ] D. Equal accuracy shows that the true-positive rates match across the two groups.
- [ ] E. Equal accuracy can hide false positives in one group and false negatives in the other.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Predictive parity equalizes precision, not overall accuracy.
- B: Accuracy parity equalizes the share of correct decisions, while equalized odds equalizes two error rates.
- C: Demographic parity compares selection rates and does not use correctness.
- D: Accuracy blends both kinds of correct decision and can match while true-positive rates differ.
- E: Two groups can have the same count of errors of different types.

**Source:** Imprecise word in a fairness prompt

## MA-ch07.5

A reviewer computes the ratio of the lower group's selection rate to the higher group's selection rate and compares it with 0.8, a screening convention often called the four-fifths rule. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The quantity is called the disparate impact ratio.
- [ ] B. The ratio compares the true-positive rates of the two groups.
- [ ] C. The ratio is built from the same quantities as demographic parity.
- [ ] D. Which outcome is called favorable changes the value of the ratio.
- [ ] E. A ratio below 0.8 is a legal finding of discrimination.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: It is the ratio of selection rates between groups.
- B: It uses selection rates and ignores who truly qualified.
- C: Both use group selection rates.
- D: The ratio of favorable rates differs from the ratio of adverse rates for the same data.
- E: It is a screening heuristic that prompts further review.

**Source:** Disparate impact ratio and four-fifths rule

## MA-ch07.6

A bank flags transactions for manual review, so being flagged is the adverse outcome. An analyst compares group flag rates and then compares group not-flagged rates. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A difference in selection rates is a ratio.
- [ ] B. The disparate impact ratio and the difference in selection rates are two names for one quantity.
- [ ] C. The difference in percentage points is the same whether computed on flag rates or on not-flagged rates.
- [ ] D. The four-fifths convention is defined on the rate of the adverse outcome.
- [ ] E. The ratio of flag rates and the ratio of not-flagged rates generally differ for the same data.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: A difference is a subtraction; a ratio is a division.
- B: One is a ratio and the other is a difference, and they can lead to different verdicts.
- C: A difference in complementary rates has the same size.
- D: It is defined on the rate of the favorable outcome.
- E: The two rates are complements, so their ratios are not equal.

**Source:** Choosing which outcome is favorable

## MA-ch07.7

A risk score between 0 and 1 is checked separately for each group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Calibration is the same property as discrimination, the ability to separate positives from negatives.
- [ ] B. Calibration within groups means that among people given score s, about a fraction s have the positive outcome, in each group.
- [ ] C. Calibration is the share of correct decisions at a chosen cutoff.
- [ ] D. Predictive parity concerns precision at a cutoff, while calibration concerns outcome rates at each score value.
- [ ] E. A score can be well calibrated and weak at discrimination.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Calibration is about whether scores match outcome frequencies; discrimination is about ranking.
- B: This is the definition of calibration of a probability score.
- C: That share is accuracy.
- D: The two criteria use different conditioning events.
- E: Giving every person the group's base rate is calibrated but separates no one.

**Source:** Calibration versus accuracy and discrimination

## MA-ch07.8

A team reports the expected calibration error (ECE) of a probability score. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. ECE is the weighted average gap between score and observed positive rate across score bins.
- [ ] B. A low ECE means the true-positive rate is high.
- [ ] C. A single pooled ECE for both groups is a calibration check by group.
- [ ] D. ECE can be computed without outcome labels.
- [ ] E. ECE measures the difference in true-positive rates between two groups.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Each bin's gap is weighted by the share of people in the bin.
- B: ECE says nothing about the true-positive rate.
- C: Pooling can hide that one group is more miscalibrated than the other.
- D: The observed positive rate in each bin needs the true outcomes.
- E: It measures score-versus-outcome agreement, not a between-group difference in error rates.

**Source:** Expected calibration error

## MA-ch07.9

In a calibration check, people in group B who were given a score of 0.2 turn out to have a positive-outcome rate of 0.30. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recalibrating the score separately within each group is a way to address it.
- [ ] B. The score overstates the risk of these people.
- [ ] C. The score understates the risk of these people.
- [ ] D. Detecting it needs outcome labels recorded by group.
- [ ] E. This is a calibration failure for group B at that score value.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Group-wise recalibration maps scores to observed outcome frequencies in that group.
- B: Overstating would mean the observed rate is below the score.
- C: The observed rate is above the stated score.
- D: The observed rate by group is computed from true outcomes.
- E: Calibration requires the observed rate to match the score.

**Source:** Reading a calibration gap

## MA-ch07.10

A risk model flags people at or above a cutoff. Analysts compare two criteria: predictive parity at the cutoff and calibration within groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Calibration within groups requires the observed positive rate to match the score at each score value in each group.
- [ ] B. Predictive parity compares the precision of flagged people across groups.
- [ ] C. Calibration within groups at each score value implies equal precision across groups at a cutoff.
- [ ] D. Predictive parity is defined using the people who were not flagged.
- [ ] E. Predictive parity at a cutoff guarantees calibration within groups.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: This is the definition of group-wise calibration.
- B: Precision of favorable decisions is the compared quantity.
- C: Precision depends on each group's mix of scores, which can differ.
- D: It uses the people who were flagged.
- E: Equal overall precision can coexist with scores that match outcomes poorly in each group.

**Source:** Predictive parity versus calibration

## MA-ch07.11

Two groups have different base rates and a classifier that is imperfect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Collecting more labeled data resolves the incompatibility.
- [ ] B. It is a defect of the learning algorithm that a more flexible model removes.
- [ ] C. This incompatibility is a result about the criteria themselves, often called an impossibility result.
- [ ] D. The incompatibility arises when the model uses group membership as an input, and disappears if the attribute is dropped.
- [ ] E. Equal precision together with equal true-positive and false-positive rates generally fails to hold.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: More data estimates the rates more precisely but does not change the arithmetic.
- B: It concerns population rates, so a better learner does not remove it.
- C: It follows from Bayes' rule applied to population rates.
- D: It holds for models that never see group membership.
- E: With different base rates, precision moves with the base rate when the error rates are equal.

**Source:** Impossibility of combining criteria

## MA-ch07.12

Two groups have different base rates. A reviewer compares a perfect classifier with a classifier that gives the favorable decision to each person. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The perfect classifier satisfies demographic parity.
- [ ] B. Giving the favorable decision to everyone satisfies demographic parity.
- [ ] C. Giving the favorable decision to everyone is a useful resolution of the conflict because it meets several criteria.
- [ ] D. When base rates are equal, the conflict between equal precision and equal error rates goes away.
- [ ] E. The perfect classifier satisfies equalized odds and predictive parity.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Its selection rates equal the unequal base rates.
- B: Both groups then have selection rate 1.
- C: It carries no information about individuals and so has no predictive value.
- D: Equal error rates and equal base rates give equal precision.
- E: It has true-positive rate 1, false-positive rate 0 and precision 1 in each group.

**Source:** Perfect and trivial classifiers

## MA-ch07.13

Two groups have different base rates and the recorded labels are correct. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A perfect classifier violates demographic parity.
- [ ] B. Maximizing overall accuracy treats a false positive and a false negative as equally costly.
- [ ] C. A perfect classifier satisfies equalized odds.
- [ ] D. Forcing equal selection rates moves some decisions away from the true labels.
- [ ] E. A trade-off between demographic parity and accuracy appears when base rates are equal.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Its selection rates equal the different base rates.
- B: Accuracy counts both kinds of error the same.
- C: It has the same true-positive and false-positive rates in both groups.
- D: That adds misclassifications relative to the recorded outcomes.
- E: With equal base rates and correct labels, a perfect classifier already meets parity.

**Source:** Fairness-accuracy trade-off

## MA-ch07.14

A product manager asks an analyst to show the trade-off between a fairness metric and accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Plotting a fairness gap against accuracy at several cutoffs displays a trade-off frontier.
- [ ] B. A Pareto-optimal option is one where improving one objective means worsening another.
- [ ] C. Raising the cutoff increases both the true-positive rate and the false-positive rate.
- [ ] D. A cutoff, also called a threshold, is a parameter of the training data.
- [ ] E. Choosing the most accurate model is a neutral choice that makes no decision about who bears errors.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Each cutoff gives a point, and the set of points shows what is gained and lost.
- B: No option dominates it on both objectives.
- C: A higher cutoff lowers both rates.
- D: A cutoff is applied to the model's scores to turn them into decisions.
- E: Accuracy weights all errors equally and lets error rates fall unevenly across groups.

**Source:** Trade-off frontier, cutoff and Pareto

## MA-ch07.15

A lender compares a single cutoff for all applicants with a separate cutoff for each group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Group-specific cutoffs are an in-processing method.
- [ ] B. Group-specific cutoffs chosen to equalize true-positive rates achieve demographic parity.
- [ ] C. Group-specific cutoffs require the group attribute at decision time.
- [ ] D. A single cutoff for everyone does not use the group attribute when deciding.
- [ ] E. With group-specific cutoffs, two people with the same score can receive different decisions, an individual fairness objection.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: They adjust decisions after training, so they are post-processing.
- B: Equalizing true-positive rates is equal opportunity, a different criterion.
- C: The cutoff to apply depends on the person's group.
- D: The same rule is applied to each person's score.
- E: Treating equal scores differently conflicts with treating similar people alike.

**Source:** Group-specific cutoffs

## MA-ch07.16

Practitioners sort bias-reduction methods into pre-processing, in-processing and post-processing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adjusting the cutoff of a frozen model is post-processing.
- [ ] B. Resampling the training data to balance groups is pre-processing.
- [ ] C. Reweighting training examples to balance group and label combinations is pre-processing.
- [ ] D. Adding a fairness penalty term to the training loss is post-processing.
- [ ] E. Adversarial debiasing, where a second network tries to predict the group from the model's representation, is in-processing.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It acts on the outputs after training.
- B: It changes the data before the model is trained.
- C: It changes the data before training.
- D: A penalty in the loss alters training, which is in-processing.
- E: It changes the training objective.

**Source:** Pre-, in- and post-processing

## MA-ch07.17

A company says its hiring model is fair because the gender field was removed from its inputs. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A proxy is a feature correlated with the protected attribute that carries some of its information.
- [ ] B. Fairness through unawareness guarantees equal error rates across groups.
- [ ] C. Fairness through unawareness means leaving the protected attribute out of the model's inputs.
- [ ] D. Features such as career gaps or postal code can let a model reconstruct the removed attribute.
- [ ] E. Auditing by group needs the protected attribute in the evaluation data even when the model does not use it.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Postal code standing in for ethnicity is a common example.
- B: Removing an input says nothing about error rates.
- C: That is the definition of the approach.
- D: Correlated features act as proxies.
- E: Group rates cannot be computed without group labels.

**Source:** Fairness through unawareness and proxies

## MA-ch07.18

A legal and ethical review distinguishes kinds of unequal treatment by an algorithm. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Disparate treatment concerns decisions that differ by protected attribute.
- [ ] B. Disparate impact concerns a neutral-looking practice with disproportionate effects on a group.
- [ ] C. Disparate impact requires evidence that the designer intended to discriminate.
- [ ] D. Group-specific cutoffs can raise disparate-treatment concerns in some jurisdictions.
- [ ] E. Disparate treatment and disparate impact are two names for the same doctrine.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Explicit use of the attribute in deciding is the core case.
- B: The practice is facially neutral but burdens one group more.
- C: It concerns effects, so intent is not required.
- D: Decision rules that depend on group membership can be restricted.
- E: They are distinct doctrines.

**Source:** Disparate treatment versus disparate impact

## MA-ch07.19

A practice with disparate impact is reviewed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A fairness metric is a legal standard.
- [ ] B. A less discriminatory alternative is a practice that increases the disparity.
- [ ] C. Satisfying equalized odds establishes legal compliance.
- [ ] D. A selection-rate ratio of 0.9 is the usual trigger for review.
- [ ] E. Business necessity is the kind of justification offered for a practice with disparate impact.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: A metric is a measurement; legal standards come from law.
- B: It is a practice that serves the same goal with a smaller disparity.
- C: Compliance depends on the applicable law and facts, not on one metric.
- D: The usual screening convention uses 0.8.
- E: The practice may be defended as needed for a legitimate goal.

**Source:** Business necessity and alternatives

## MA-ch07.20

An auditor reviews a model against the principle that similar individuals should be treated similarly. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. It can be evaluated from per-group confusion matrices alone.
- [ ] B. The Lipschitz form bounds the difference in two people's outcomes by a distance between the people.
- [ ] C. This principle is called individual fairness.
- [ ] D. Applying it requires a similarity metric chosen for the task.
- [ ] E. Individual fairness implies demographic parity.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Confusion matrices average over individuals and lose pairwise comparisons.
- B: Similar people must receive similar outcome distributions.
- C: It compares how individuals are treated rather than group averages.
- D: Someone must say which differences between people are relevant.
- E: Similar treatment of similar people can coexist with different group selection rates.

**Source:** Individual fairness and the similarity metric

## MA-ch07.21

A reviewer contrasts group fairness with individual fairness. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A model that treats similar people alike under a chosen metric can still show different group selection rates.
- [ ] B. Equal opportunity is an individual fairness criterion.
- [ ] C. Group fairness compares individuals pair by pair, while individual fairness compares group averages.
- [ ] D. A model can satisfy demographic parity and still treat two near-identical people very differently.
- [ ] E. The choice of similarity metric is a technical detail without a value judgment.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: The groups may differ on features the metric counts as relevant.
- B: Equal opportunity compares true-positive rates across groups.
- C: The two descriptions are swapped.
- D: Parity limits group rates, not which individuals receive the favorable decision.
- E: Deciding which differences are relevant is a substantive judgment.

**Source:** Group versus individual fairness

## MA-ch07.22

In a causal model of a loan decision, a protected attribute A affects an education credential E, which is an input to a predictor. Unobserved background factors U also affect E. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The causal graph tells which paths from A to the prediction are acceptable.
- [ ] B. A predictor whose inputs are variables that are not downstream of A is counterfactually fair in this model.
- [ ] C. Counterfactual fairness asks whether an individual's prediction would be the same had the attribute taken a different value, with the individual's background factors held fixed.
- [ ] D. Counterfactual fairness is another name for equalized odds.
- [ ] E. Judging counterfactual fairness requires assumptions about the causal structure.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The graph shows which paths exist; accepting a path is a value judgment.
- B: Its inputs do not change when A is changed.
- C: It is an individual-level causal question.
- D: Equalized odds is about error rates by group, not a causal question.
- E: Observed data alone cannot distinguish structures that imply different counterfactuals.

**Source:** Counterfactual fairness

## MA-ch07.23

In a causal graph, a protected attribute A affects a credential E, which feeds a predictor, and unobserved background factors U affect E. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Path-specific fairness allows some paths from the attribute to the prediction and blocks others.
- [ ] B. A counterfactual evaluation holds the background factors U fixed.
- [ ] C. A counterfactual is a quantity observed directly in the data.
- [ ] D. E is a confounder of A and the prediction.
- [ ] E. E is a mediator on the path from A to the prediction.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It treats paths differently according to a judgment about which are acceptable.
- B: The same individual is considered under a different attribute value.
- C: It concerns a hypothetical alternative that is not observed.
- D: A confounder is a common cause of two variables, which E is not here.
- E: A mediator lies on a path between a cause and an outcome.

**Source:** Causal graph vocabulary

## MA-ch07.24

A system gives a benefit to each person, and an analyst computes a generalized entropy index of the benefits, decomposed by group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A large within-group component with a zero between-group component means individuals receive equal benefits.
- [ ] B. When two groups have equal mean benefits, the between-group component is positive.
- [ ] C. The index splits into a between-group component and a within-group component.
- [ ] D. The generalized entropy index measures inequality in how benefits are distributed across individuals.
- [ ] E. The between-group component measures inequality between the groups' mean benefits.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It means benefits are unequal inside groups even though group means match.
- B: Equal means give a between-group component of zero.
- C: The decomposition separates group-mean inequality from inequality inside groups.
- D: Larger values mean more inequality.
- E: It is computed after replacing each person's benefit by the group mean.

**Source:** Generalized entropy index and decomposition

## MA-ch07.25

An audit scores a model on whether it predicts re-arrest. One neighborhood is patrolled much more heavily than another. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Selection bias and measurement bias are two names for the same problem.
- [ ] B. Using group-specific cutoffs removes label bias.
- [ ] C. A proxy label is a recorded outcome standing in for the quantity of interest.
- [ ] D. A recorded outcome that measures something other than the target quantity, such as arrests instead of offending, is a measurement bias problem.
- [ ] E. Equal error rates against recorded arrests establish equal error rates against actual offending.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Selection bias concerns who is included in the data; measurement bias concerns how outcomes are recorded.
- B: Cutoffs change decisions, not how the label relates to the behavior.
- C: Arrest records stand in for behavior.
- D: The label differs systematically from the quantity of interest.
- E: The recorded label may encode enforcement differences.

**Source:** Measurement bias and proxy labels

## MA-ch07.26

A lender's model decides which applicants to approve, and repayment is recorded for approved applicants. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Selective labels make error rates for the full applicant population uncertain.
- [ ] B. Reject inference is the attempt to estimate outcomes for declined applicants.
- [ ] C. Selective labels means the outcome is recorded for people who received the favorable decision and is missing for the rest.
- [ ] D. Selective labels is another name for overfitting.
- [ ] E. Repayment outcomes are observed for declined applicants as well as approved ones.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Rates for declined applicants must be estimated.
- B: The term names methods for filling in missing outcomes of rejected cases.
- C: Declined applicants have no repayment record.
- D: Overfitting concerns a model fitted too closely to training data.
- E: Declined applicants did not receive a loan, so no repayment is observed.

**Source:** Selective labels

## MA-ch07.27

An audit reports true-positive rates of 0.75 (400 qualified people) in one group and 0.60 (40 qualified people) in another. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A 95% confidence interval for the smaller group's rate is wider than the larger group's.
- [ ] B. Low statistical power means a real gap can go undetected.
- [ ] C. The multiple comparisons problem is that testing many subgroups makes a chance significant gap less likely.
- [ ] D. A non-significant difference shows that the two groups have equal rates.
- [ ] E. A p-value is the probability that the two groups have equal rates.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Interval width shrinks as the sample grows.
- B: Small samples give tests little ability to detect real differences.
- C: Testing many subgroups makes a chance significant gap more likely.
- D: Failing to detect a gap is not evidence of equality.
- E: A p-value is the probability of data this extreme if the rates were equal.

**Source:** Confidence interval, power, multiple comparisons

## MA-ch07.28

A reviewer checks selection rates by gender, by region and by gender-by-region combination. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing the check on each attribute separately implies passing on the combinations.
- [ ] B. Single-attribute selection rates can look equal while some combination cells differ.
- [ ] C. Checking combinations multiplies the number of subgroups, so samples per cell shrink and intervals widen.
- [ ] D. Intersectional analysis examines combinations of attributes such as gender and region together.
- [ ] E. A gender-by-region cell is an example of an intersectional subgroup.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Disparities can cancel in the margins.
- B: Opposite gaps in different cells can offset each other in the margins.
- C: Each added attribute splits the sample further.
- D: Disparities can exist in combinations.
- E: It is defined by more than one attribute.

**Source:** Intersectional subgroups

## MA-ch07.29

A classifier keeps the same true-positive and false-positive rates in each group after deployment, but one group's base rate rises. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Concept drift is a change in the input distribution alone.
- [ ] B. Label shift changes the true-positive and false-positive rates by definition.
- [ ] C. Precision is stable under a change in base rate.
- [ ] D. Covariate shift is a change in the relationship between the inputs and the outcome.
- [ ] E. A change in base rate with the class-conditional feature distributions unchanged is called label shift, also known as prior probability shift.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Concept drift is a change in the relationship between inputs and outcome.
- B: Those rates are conditional on the class and stay the same.
- C: Precision depends on the base rate.
- D: Covariate shift is a change in the input distribution.
- E: The share of positives changes while the features within each class stay the same.

**Source:** Label shift, covariate shift and concept drift

## MA-ch07.30

A hospital tests an assistant that states its own confidence in words for urgent-versus-not triage of messages in different languages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A calibration check by group needs no outcome labels.
- [ ] B. Stating the same confidence level equally often in two groups shows it is calibrated in each.
- [ ] C. A calibration check on one model version and prompt stays valid after either is changed.
- [ ] D. A confidence stated in words by a language model is a claim to test against outcomes.
- [ ] E. Hedged wording is evidence that the stated confidence is calibrated.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: It compares stated confidence with observed outcomes.
- B: Calibration needs agreement with observed outcomes.
- C: A change can alter the confidence statements, so the check is repeated.
- D: Fluent confidence need not match how often the model is right.
- E: Tone is not evidence of calibration.

**Source:** Calibration of stated confidence

## MA-ch07.31

An organization chooses which group criterion to prioritize for a cancer-screening aid, where a missed case is costly, and for a fraud flag that freezes payments. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. False-positive-rate parity targets wrongful flags, the main harm for the fraud flag.
- [ ] B. The false-negative rate equals one minus the true-positive rate.
- [ ] C. Equal opportunity targets unequal rates of missed cases across groups.
- [ ] D. Demographic parity is the criterion that targets the cost of each error type.
- [ ] E. The choice among criteria follows from the confusion matrices alone.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: It compares how often people who did nothing wrong are flagged.
- B: The two rates split the truly qualified people.
- C: Equal true-positive rates mean equal false-negative rates.
- D: Demographic parity ignores which errors occur.
- E: It depends on who bears the cost of each error type.

**Source:** Choosing a criterion by harm

## MA-ch07.32

A team has built a loan-approval model and must report fairness. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing the chosen metric means the other criteria are also satisfied.
- [ ] B. A model card is a plot of calibration.
- [ ] C. Minimizing average loss has no effect on how errors fall across groups.
- [ ] D. A regulator naming a metric fixes the formula and leaves open the groups, cutoff and tolerance.
- [ ] E. A tolerance states how close two rates have to be to count as equal.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Meeting one criterion can mean others fail.
- B: A model card is documentation of a model's use, data and limits.
- C: Average loss weights examples equally, which shapes the distribution of errors.
- D: Applying a named metric still requires decisions.
- E: Equality of estimated rates is judged within a stated margin.

**Source:** Metric, tolerance and documentation

## MA-ch07.33

Group A has 400 true positives, 100 false positives, 0 false negatives and 500 true negatives. Group B has 300 true positives, 0 false positives, 100 false negatives and 600 true negatives. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy parity holds between the two groups.
- [ ] B. Group B has the higher true-positive rate.
- [ ] C. The errors in group A are false positives and the errors in group B are false negatives.
- [ ] D. Equalized odds holds between the two groups.
- [ ] E. Equal accuracy means the two groups bear the same cost from errors.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Both groups have accuracy 0.90.
- B: Group A's is 1.0 and group B's is 0.75.
- C: Group A has only false positives and group B only false negatives.
- D: The true-positive rates are 1.0 and 0.75, and the false-positive rates differ too.
- E: Different error types can carry different costs.

**Source:** Confusion matrix terms

## MA-ch07.34

An analyst studies why precision changes with base rate for a classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. By Bayes' rule, the odds of a positive outcome given a positive prediction equal the prior odds times the likelihood ratio.
- [ ] B. Base rate is another word for the prevalence of the positive outcome in a group.
- [ ] C. Precision and the true-positive rate are two names for the same quantity.
- [ ] D. The likelihood ratio of a positive prediction is the true-positive rate divided by the false-positive rate.
- [ ] E. The posterior probability of the positive outcome given a positive prediction is the true-positive rate.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: This is the odds form of Bayes' rule applied to precision.
- B: Both name the share of the group with the positive outcome.
- C: They condition on different events.
- D: It compares how likely a positive prediction is for positives versus negatives.
- E: That posterior is the precision.

**Source:** Bayes' rule, base rate and likelihood ratio

## MA-ch07.35

A manager asks an AI assistant, "Check whether our hiring model is unbiased and fix it so everyone is treated the same." Check each statement that is true. Each statement is worth 1 point (5 points total). about writing a precise prompt.

- [ ] A. A precise prompt names the groups, the favorable outcome, the metric and the tolerance.
- [ ] B. Bias in the statistical sense is the same thing as unfairness.
- [ ] C. "Unbiased" is vague, and naming a criterion such as equalized odds fixes its meaning.
- [ ] D. "Treated the same" can mean demographic parity, equal error rates or individual fairness, which are distinct.
- [ ] E. Asking for post-processing names a family of methods that adjust decisions after training.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Each of these is needed to define the check.
- B: Statistical bias is systematic error, while fairness is a normative judgment.
- C: Each criterion is a specific, checkable condition.
- D: The phrase does not choose among distinct criteria.
- E: It specifies where in the pipeline the fix is applied.

**Source:** Rewriting a vague fairness prompt

## MA-ch07.36

A health system flags patients for a limited care program. The base rate of high need is higher in group X than in group Y, partly because group X has had less access to primary care. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Predictive parity holds automatically when error rates are equal.
- [ ] B. A group's base rate can partly reflect unequal access to care.
- [ ] C. Equal opportunity and demographic parity coincide when base rates differ.
- [ ] D. Equalized odds is another name for equal opportunity.
- [ ] E. With equal true-positive and false-positive rates in both groups, the selection rates differ when base rates differ.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Precision also depends on the base rate.
- B: Observed prevalence can come from how people were treated, not only from underlying need.
- C: They constrain different quantities and generally conflict then.
- D: Equal opportunity constrains only the true-positive rate.
- E: Selection rate depends on base rate and the two error rates.

**Source:** Base rates and choice of criterion

## MA-ch07.37

A reviewer compares equal opportunity with equalized odds. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Predictive parity follows from equalized odds.
- [ ] B. Equalized odds implies equal opportunity.
- [ ] C. Equalized odds adds false-positive-rate parity to equal opportunity.
- [ ] D. Equal opportunity implies equalized odds.
- [ ] E. Equal opportunity concerns people who truly qualify.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Precision depends on base rates as well as the error rates.
- B: Equal true-positive rates are one of its two components.
- C: It requires both error rates to match.
- D: False-positive rates can still differ.
- E: It compares true-positive rates.

**Source:** Equal opportunity versus equalized odds
