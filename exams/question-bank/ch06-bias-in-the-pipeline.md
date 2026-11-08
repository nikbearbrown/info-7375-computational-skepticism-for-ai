# Chapter 6: Bias, where it enters and who is responsible

## MA-ch06.1

A survey firm estimates citywide support for a measure by sampling landline numbers only, and residents without a landline support it less often than residents with one. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Enlarging the sample shrinks the bias along with the standard error.
- [ ] B. The gap is a coverage error, because part of the population is missing from the sampling frame.
- [ ] C. The estimate is biased in the statistical sense: its expected value differs from the population value.
- [ ] D. Reweighting the landline respondents to match the population's landline share repairs the estimate without sampling anyone else.
- [ ] E. Sampling error is a systematic offset that does not shrink as the sample grows.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: A larger sample reduces random sampling error but leaves the systematic offset where it was.
- B: Coverage error arises when the frame omits people the survey is meant to describe.
- C: Estimator bias is the gap between an estimator's average over repeated samples and the true value.
- D: Weighting adjusts the mix of people sampled, and a group with no respondents has nothing to weight up.
- E: Sampling error is chance variation that shrinks with sample size, and a systematic offset is bias.

**Source:** Estimator bias versus sampling error

## MA-ch06.2

A model is trained on patients who had a lab panel in the first hours of admission. Patients who looked unstable were less likely to get the panel, so the retained patients do not represent all admissions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A baseline risk learned from the retained patients is miscalibrated for the full admitted population.
- [ ] B. Weighting retained patients by the inverse of their retention probability corrects the skew even when retention depends on an unrecorded variable.
- [ ] C. Collecting more records under the same retention rule removes the bias.
- [ ] D. This is measurement bias, because the lab values are recorded with error.
- [ ] E. This is selection bias, because inclusion in the data depends on a variable related to the outcome.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Calibration means predicted risks match observed frequencies, and a skewed sample breaks that match.
- B: Weighting needs a recorded variable that explains who was kept.
- C: More data from the same filter reproduces the same skewed mix with less noise.
- D: Measurement bias concerns how values are recorded, whereas here the issue is who is recorded.
- E: Selection bias arises when the rule that decides who enters the data is tied to what is being predicted.

**Source:** Selection bias and inverse probability weighting

## MA-ch06.3

A lender deletes the protected attribute from its training table but keeps neighbourhood, which closely tracks group membership. A manager says the model treats groups equally because it never sees group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Deleting the attribute from the records leaves the lender able to compute outcome rates by group.
- [ ] B. Redundant encoding means group membership can be predicted from the remaining features.
- [ ] C. Fairness through unawareness is the practice of withholding the protected attribute, and it guarantees equal outcomes across groups.
- [ ] D. Neighbourhood acts as a proxy for the protected attribute.
- [ ] E. A feature that correlates with group is, by itself, proof of disparate treatment.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Without a recorded attribute, outcome rates by group cannot be computed.
- B: When other columns carry the same information, dropping one column does not remove the signal.
- C: Unawareness describes the withholding, but it does not guarantee equal outcomes.
- D: A proxy is a feature that stands in for another variable because the two are correlated.
- E: Correlation with group does not show improper use, since the feature may also carry legitimate information.

**Source:** Proxy and fairness through unawareness

## MA-ch06.4

A reviewer divides the lower group's selection rate by the higher group's selection rate, gets 0.67, and compares it with 0.8. A separate two-proportion test on the same counts gives a very small p-value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The four-fifths rule is a heuristic applied to aggregate selection rates, not a significance test.
- [ ] B. Subtracting the two selection rates gives the disparate impact ratio.
- [ ] C. The ratio of selection rates is called the disparate impact ratio, also known as the adverse impact ratio.
- [ ] D. Statistical significance says a gap is unlikely to be sampling noise, which is a different question from whether it is large enough to matter.
- [ ] E. A ratio of selection rates close to 1 indicates similar selection rates in the two groups.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It is a rule of thumb for flagging adverse impact and carries no test statistic.
- B: A subtraction gives a difference in rates, and the impact ratio is a quotient.
- C: It is the standard name for the lower selection rate divided by the higher.
- D: Statistical significance and practical significance answer different questions.
- E: A disparate impact ratio of 1 means equal selection rates, and lower values mean a larger relative gap.

**Source:** Disparate impact ratio and significance

## MA-ch06.5

An audit finds a large approval gap between two groups and wants to locate the pipeline stage that produced it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A statistically significant gap names the pipeline stage that produced it.
- [ ] B. Stratifying on legitimate covariates compares applicants with similar qualifications.
- [ ] C. An ablation reports the correlation between a component and the gap without changing the component.
- [ ] D. If the gap disappears after conditioning on a variable, that variable is a legitimate explanation of the gap.
- [ ] E. Matching balances the measured covariates but leaves unmeasured ones free to differ.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Significance says the gap is not noise but not where it arose.
- B: Stratification splits the data by a variable so groups are compared within levels.
- C: An ablation intervenes on a component, and a correlation does not.
- D: The conditioning variable may itself be shaped by group, so the gap running through it is not justified by that fact.
- E: Matching can only equalise the variables that were recorded.

**Source:** Stratification, ablation, matching

## MA-ch06.6

A company advanced candidates for two roles. Group B has the higher advancement rate within each role, yet group A has the higher advancement rate overall, because the two groups apply to the roles in different proportions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. This reversal between subgroup and aggregate comparisons is Simpson's paradox.
- [ ] B. The aggregate comparison is the right one to report because it uses the most data.
- [ ] C. Choosing between the stratified and the pooled table is settled by whichever has the larger sample.
- [ ] D. A reversal like this indicates an arithmetic error in the counts.
- [ ] E. Group is the stratifying variable whose different mix across roles produces the reversal.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Simpson's paradox is a trend within strata that reverses or vanishes after pooling.
- B: Using more data does not make the pooled table the answer to the causal question.
- C: Sample size does not decide which table answers the causal question.
- D: A reversal is routine when group composition differs across strata.
- E: Role is the stratifying variable, and the groups differ in how they spread across roles.

**Source:** Simpson's paradox in selection

## MA-ch06.7

In hospital records, the drug group recovered less often overall than the untreated group, but did better within each severity level, because doctors gave the drug mostly to severe patients. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Giving a treatment on the basis of a prognostic factor such as severity confounds the raw comparison.
- [ ] B. Randomised assignment breaks the link between severity and treatment, measured or not.
- [ ] C. Severity is a confounder because it influences both who gets the drug and how likely recovery is.
- [ ] D. Confounding by indication names the situation where sicker patients are the ones given the treatment.
- [ ] E. Adjusting for a mediator, a variable on the path from treatment to outcome, is the standard way to remove confounding.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A factor that drives both treatment and outcome confounds the comparison.
- B: Randomisation makes treatment independent of prior factors in expectation.
- C: A confounder is a common cause of treatment and outcome.
- D: The reason for treatment is itself related to the outcome.
- E: Adjusting for a mediator blocks part of the effect, while confounders are the variables to adjust for.

**Source:** Confounding by indication

## MA-ch06.8

A classifier has 90% overall accuracy, made of 95% on a large group A and 70% on a small group B. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Representation bias describes a model that predicts poorly for the majority group.
- [ ] B. Disaggregation means averaging the group metrics into one fair number.
- [ ] C. Disaggregated evaluation reports metrics separately for each subgroup.
- [ ] D. Pooled accuracy is an average weighted by group size, so the large group dominates it.
- [ ] E. A high overall accuracy implies that each subgroup's accuracy is near the overall figure.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Representation bias concerns a group being thinly represented in the data.
- B: That would be aggregation, the opposite of reporting the groups separately.
- C: Disaggregation splits a metric by group rather than averaging over them.
- D: A pooled metric reflects the biggest group most.
- E: A pooled average can hide a subgroup far below it.

**Source:** Pooled versus disaggregated metrics

## MA-ch06.9

Group B has 40 test examples with 15% error and group A has 2,000 test examples with 8% error. A 95% interval for group B's error rate is wide, and a significance test on the difference gives p = 0.13. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A Wilson interval is a credible interval computed from a posterior distribution.
- [ ] B. A non-significant result from a small sample is inconclusive rather than evidence of equal error rates.
- [ ] C. A wide confidence interval signals that the estimate for the small group is imprecise.
- [ ] D. Low statistical power means a test often fails to detect a real difference.
- [ ] E. Reporting just the pooled error rate hides the subgroup of interest.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: A Wilson interval is a frequentist confidence interval for a proportion.
- B: Failing to reject a null hypothesis is not evidence that it is true.
- C: Interval width reflects estimation uncertainty, which is large for small samples.
- D: Power is the chance of detecting a true effect, and it is low for small samples.
- E: Pooling averages the small group into a figure dominated by the large one.

**Source:** Confidence interval, p-value, power

## MA-ch06.10

An auditor tests 20 independent subgroups for an error-rate gap at the 5% significance level for each test, and the model performs identically in the subgroups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Choosing which subgroup to report after seeing the results is p-hacking, also called data dredging.
- [ ] B. A non-significant result in a small subgroup shows the model performs equally well there.
- [ ] C. A Bonferroni correction multiplies the significance level by the number of tests.
- [ ] D. The 5% significance level applies to the group of 20 tests taken together.
- [ ] E. Testing many subgroups raises the family-wise error rate, the chance of at least one false positive.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Searching for a significant result after the fact inflates false findings.
- B: A null result may reflect low power rather than equality.
- C: It divides the significance level by the number of tests.
- D: The level is set per test, so the combined false-positive chance is much higher.
- E: The per-test rate applies to a single test, and errors accumulate across a family.

**Source:** Multiple comparisons and p-hacking

## MA-ch06.11

A face-attribute classifier is evaluated by gender and, separately, by skin tone, and the marginal error rates look equal. Evaluating the four gender-by-skin-tone cells shows error rates from 1% to 21%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Equal marginal error rates imply equal error rates in each gender-by-skin-tone cell.
- [ ] B. Intersectional evaluation means evaluating each attribute separately and comparing the results.
- [ ] C. Intersectional evaluation reports metrics for combinations of attributes.
- [ ] D. The number of cells grows multiplicatively with each attribute added, so cells become small and noisy.
- [ ] E. Dropping a thin cell from the report is more honest than showing a wide interval.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Marginal equality can mask large differences between cells.
- B: Separate evaluation produces marginal results, not joint ones.
- C: It looks at joint subgroups rather than one attribute at a time.
- D: Combining attributes multiplies subgroups and thins out the data in each.
- E: Dropping a cell hides the subgroup, and a wide interval shows the uncertainty.

**Source:** Intersectional evaluation

## MA-ch06.12

A model predicts arrest in the next year as a proxy for offending. Two neighbourhoods have the same offence rate, but the more heavily patrolled one has a higher arrest rate per offence. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Label bias is the same thing as sampling bias.
- [ ] B. The label is recorded with different accuracy in different neighbourhoods, which is differential measurement bias.
- [ ] C. Collecting more arrest records fixes the label problem.
- [ ] D. A model that is highly accurate on the arrest label measures offending correctly.
- [ ] E. Arrest is a proxy label for offending, so the label is measured with error.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Label bias concerns how the outcome is recorded, and sampling bias concerns who is included.
- B: Differential measurement bias means measurement quality varies by group.
- C: More records from the same process estimate the same distorted rates more precisely.
- D: Accuracy is judged against the label and says nothing about whether the label tracks offending.
- E: A proxy label stands in for the outcome of interest and may track it imperfectly.

**Source:** Proxy label and measurement bias

## MA-ch06.13

A hospital enrols patients by predicted annual cost, as a stand-in for health need. One group faces access barriers, so its cost understates its need, and the model predicts cost perfectly. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Replacing the label with a measure closer to need addresses the mismatch.
- [ ] B. A model that predicts the label accurately shows that the label is valid.
- [ ] C. Accuracy in predicting a label is a different question from whether the label has construct validity.
- [ ] D. Cost is a proxy label for need.
- [ ] E. Construct validity is the question of whether the label measures the quantity of interest.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Moving the label toward the construct reduces label bias.
- B: Accuracy against a label says nothing about whether the label measures the construct.
- C: Predictive accuracy and construct validity answer different questions.
- D: A proxy label is a measurable quantity used in place of the one that matters.
- E: A valid construct measure tracks the concept it claims to capture.

**Source:** Construct validity and proxy labels

## MA-ch06.14

A lender sees repayment outcomes only for applicants it approved. It then trains a new model on those outcomes and wants to estimate how denied applicants would have performed. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reject inference is the name for estimating outcomes for denied applicants.
- [ ] B. Outcomes are observed for just those who received the favourable decision, which is the selective labels problem.
- [ ] C. Selective labels are the same problem as class imbalance.
- [ ] D. Approving a random sample of denied applicants gives outcome data that do not represent the denied group.
- [ ] E. Test accuracy computed on approved applicants is an unbiased estimate of performance on denied applicants.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: It is the term for inferring performance of applicants who were declined.
- B: Selective labels arise when the decision determines whether the outcome is recorded.
- C: Class imbalance is about unequal class frequencies, not about which outcomes get observed.
- D: A random draw from the denied group does represent that group.
- E: The approved group was selected by the earlier score, so it differs from the denied group.

**Source:** Selective labels and reject inference

## MA-ch06.15

Two districts have the same true incident rate. Patrol hours are allocated in proportion to incidents recorded in the previous cycle, and recorded incidents are proportional to patrol hours. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Proportional allocation drives the two districts toward their true rates over repeated cycles.
- [ ] B. Allocating more patrol hours to the district with more records breaks the loop.
- [ ] C. This is a runaway feedback loop, in which the system's decisions determine the data it later learns from.
- [ ] D. A feedback loop is random sampling error that averages out over time.
- [ ] E. Recorded incidents reflect observation effort as well as the true rate.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The initial split reproduces itself, because records mirror patrol hours.
- B: That allocation rule is the loop, so it reinforces the existing split.
- C: A feedback loop occurs when model outputs shape future training data.
- D: A feedback loop is systematic and reinforces itself rather than averaging out.
- E: Counts depend on where observers look, which is a measurement bias.

**Source:** Feedback loops

## MA-ch06.16

A reweighing scheme gives each combination of group and label a weight so that group and label are statistically independent in the weighted training data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reweighing leaves the recorded labels unchanged and alters how much each row counts.
- [ ] B. Reweighing is a pre-processing method, because it changes the training data rather than the learner.
- [ ] C. Reweighing guarantees equal selection rates in the model's predictions on new data.
- [ ] D. After reweighing, group and label are independent in the weighted training sample.
- [ ] E. Reweighing requires group membership to be recorded for the training rows, even when it is not a model input.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The weights change the influence of each row while the labels stay as recorded.
- B: Pre-processing methods adjust the data before training.
- C: Independence in the training sample does not carry over to predictions on new data.
- D: That independence is the purpose of the weights.
- E: The weights are computed from group, so it has to be recorded.

**Source:** Pre-processing: reweighing

## MA-ch06.17

A lender proposes setting a different score cutoff for each group after the model has produced its scores, to narrow a selection gap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Group-specific cutoffs can be applied without recording group membership at decision time.
- [ ] B. Adding a fairness penalty to the training loss is an in-processing method.
- [ ] C. Adjusting cutoffs by group is an in-processing method.
- [ ] D. Group-specific thresholds are a post-processing method.
- [ ] E. Post-processing retrains the model's scores separately for each group.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: A cutoff that depends on group needs the group to be known when deciding.
- B: In-processing builds the fairness criterion into the learning objective.
- C: In-processing alters the training procedure, and cutoffs act after training.
- D: Post-processing acts on a model's outputs after training.
- E: Post-processing leaves the learned scores in place and changes the decision rule.

**Source:** Post-processing and in-processing

## MA-ch06.18

A résumé-ranking model trained on past hiring decisions selects group B less often than group A at the same measured experience. The team considers reweighing, a fairness penalty, separate cutoffs, and changes to how reviewers use the ranking. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reweighing the training data also repairs disparity introduced by human reviewers.
- [ ] B. Pre-processing, in-processing and post-processing act on the outputs, the training and the data respectively.
- [ ] C. Historical bias means the data reflect earlier decisions that encoded disparities, even when the records are accurate.
- [ ] D. A human review stage after the model is outside the pipeline, so it adds no disparity.
- [ ] E. Lower agreement with past decisions shows the model is of lower quality.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Reweighing changes the training sample, so a disparity created at review is outside its reach.
- B: The order is data, training and outputs, so the stages are listed backwards here.
- C: Historical bias arises from the world that produced the data, not from recording errors.
- D: Review is part of deployment and can introduce disparity.
- E: The past decisions are suspect, so less agreement can mean less copying of earlier skew.

**Source:** Mitigation stages and historical bias

## MA-ch06.19

A bank buys a credit-risk model from a vendor, which trained it on records bought from a data broker with labels taken from another lender's approvals. The bank sets the approval cutoff and routes borderline cases to officers. An audit finds a large approval gap between groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The approval cutoff is a decision point that the bank owns.
- [ ] B. Buying a model from a vendor transfers accountability for the lending decisions to the vendor.
- [ ] C. Data provenance means the statistical distribution of the model's scores across groups.
- [ ] D. Assigning accountability for a disparity requires showing that someone intended it.
- [ ] E. Accountability can be assigned according to which party controls a decision point in the pipeline.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The party that sets a threshold owns its consequences.
- B: The bank makes the decisions and keeps accountability for them.
- C: Provenance is the origin and history of the data.
- D: Accountability attaches to roles that control a step and does not depend on a finding of intent.
- E: Control over a step is the usual basis for assigning responsibility for it.

**Source:** Accountability and provenance

## MA-ch06.20

A dataset's documentation records how and why the data were collected, who is represented, and how labels were produced. A separate document for the model states its intended uses, evaluation data and subgroup performance. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An audit is called external when a party independent of the developer performs it.
- [ ] B. A model card is a disclosure and does not by itself make a model fair.
- [ ] C. A model card reports intended uses and performance broken down by subgroup.
- [ ] D. A datasheet documents the origin, composition and collection of a dataset.
- [ ] E. A model card describes the collection process and label provenance of the training data.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Independence from the developer is what makes an audit external.
- B: A card can report poor performance without correcting it.
- C: Disaggregated performance and scope are standard model card contents.
- D: A datasheet is a disclosure document for data.
- E: That content belongs in a datasheet, and a model card describes the model.

**Source:** Datasheet, model card, audit

## MA-ch06.21

A model is benchmarked on data that is 90% group A and 10% group B, then deployed on a population that is half group A and half group B. Each group's accuracy stays the same in deployment. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A change in group mix between benchmark and deployment is a change in the input distribution, a form of covariate shift.
- [ ] B. A larger benchmark sample with the same composition removes the mismatch.
- [ ] C. Overall accuracy is a property of the model alone and does not depend on the population.
- [ ] D. Group-conditional accuracy has no use for predicting overall accuracy on a new mix.
- [ ] E. Reporting accuracy by group transfers to a new mix better than a single pooled figure.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Covariate shift is a change in the input distribution while the relationship to the outcome stays put.
- B: More data of the same mix cannot show how the model behaves on a different mix.
- C: Overall accuracy depends on the mix of groups it is measured over.
- D: Per-group figures combine with the new shares to give the deployment figure.
- E: Disaggregated figures remain usable when the composition changes.

**Source:** Covariate shift in group mix

## MA-ch06.22

In group A the outcome follows y = 2x and in group B it follows y = 2x + 6. A single line fitted to both groups together misses both of them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A high R-squared on the pooled fit shows that the model fits each group.
- [ ] B. Residuals split by group reveal consistent over- and under-prediction.
- [ ] C. Including a group indicator in the model lets the fit capture the offset between groups.
- [ ] D. Omitting a group indicator from the model is an omitted variable problem here.
- [ ] E. Fitting one model to heterogeneous groups can fit neither well, which is aggregation bias.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: R-squared summarises the pooled fit and can hide systematic misfit within groups.
- B: Disaggregated residuals expose a group-specific pattern that the pooled line hides.
- C: An indicator variable absorbs the group-specific intercept.
- D: The missing variable explains the offset between the groups.
- E: Aggregation bias arises when a pooled model assumes one relationship for different groups.

**Source:** Aggregation bias and omitted variable

## MA-ch06.23

A screening device reads a person's true value plus noise, and the noise is larger for group B than for group A. The same cutoff is applied to everyone. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Raising the cutoff for group B removes the effect of its larger noise.
- [ ] B. More rows of readings from the same instrument reduce the noise in each reading.
- [ ] C. Measurement quality that differs by group is differential measurement error.
- [ ] D. Larger measurement noise for group B produces more misclassification for group B at the same cutoff.
- [ ] E. The disparity comes from applying a different cutoff to each group.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: A different cutoff does not reduce the noise in the readings.
- B: The noise belongs to the instrument, so each reading stays equally noisy.
- C: It is measurement error whose size depends on group.
- D: Noise pushes readings across the cutoff more often for the noisier group.
- E: The cutoff is common to both groups, and the difference comes from the measurement.

**Source:** Differential measurement error

## MA-ch06.24

A classifier has the same true positive rate and the same false positive rate in two groups, but the share of truly positive people differs between the groups. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Predictive parity means equal positive predictive value across groups.
- [ ] B. Equalized odds means equal true positive and false positive rates across groups.
- [ ] C. Demographic parity means equal true positive rates across groups.
- [ ] D. With equal error rates and unequal base rates, the positive predictive values are also equal.
- [ ] E. With unequal base rates and an imperfect classifier, equalized odds and predictive parity hold together in general.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Positive predictive value is the share of flagged people who are truly positive.
- B: It constrains both error rates to match between groups.
- C: Demographic parity means equal selection rates, which is a different quantity.
- D: Positive predictive value depends on the base rate, so it differs.
- E: The two criteria conflict when base rates differ.

**Source:** Fairness criteria and base rate

## MA-ch06.25

A model approves 30% of group A and 18% of group B. Re-scoring the same applicants with the postcode input replaced by a constant leaves a smaller gap. Group is not an input. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The test shows how the model depends on postcode and not why the groups differ in postcode.
- [ ] B. A gap that remains after postcode is neutralised shows the model uses group directly.
- [ ] C. Neutralising an input and re-scoring is an ablation of that input.
- [ ] D. If group is not an input, no other input can carry group information.
- [ ] E. A smaller gap after neutralising postcode shows postcode causes differences in repayment.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: It is a statement about the model, not about the applicants.
- B: Other correlated inputs can carry the remaining gap without group being used.
- C: Ablation removes a component to see how outputs change.
- D: Correlated inputs can act as proxies that carry group information.
- E: The test intervenes on the model's input, so it says nothing about causes in the applicants.

**Source:** Ablation and proxy chains

## MA-ch06.26

Three candidate models have group A error rates of 5%, 6% and 3% and group B error rates of 30%, 20% and 45%, and group A is 90% of the data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Balanced accuracy gives groups weight in proportion to their size, so it equals pooled accuracy.
- [ ] B. Worst-group error is a different criterion from average error.
- [ ] C. Empirical risk minimisation optimises average loss, which weights each group by its share of the data.
- [ ] D. Two models can rank differently by average error and by worst-group error.
- [ ] E. Choosing the model with the lowest worst-group error is a minimax criterion.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Balanced accuracy weights each group equally, regardless of its size.
- B: It reports the group with the highest error rather than the weighted mean.
- C: The average loss follows the data mix, so the large group dominates.
- D: Average error and worst-group error are different criteria and can disagree.
- E: Minimax minimises the maximum loss across groups.

**Source:** Average versus worst-group error

## MA-ch06.27

A model flags the same share of applicants in two groups. A human reviewer then upholds flags in one group more often than in the other. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A funnel analysis combines the stages into one overall rate.
- [ ] B. Comparing reviewer decisions on like cases is needed to attribute the gap to reviewer behaviour.
- [ ] C. Different upheld rates establish that the reviewer is biased.
- [ ] D. A review stage that follows an equal flagging step leaves the selection rates equal between groups.
- [ ] E. Automation bias means reviewers ignore the model's flags.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: A funnel analysis reports each stage separately so the step where rates diverge can be found.
- B: Comparable cases separate case mix from reviewer treatment.
- C: The flagged cases may differ in true risk, so rates call for investigation but do not show bias.
- D: The review step can create or remove disparity after equal flag rates.
- E: Automation bias is over-reliance on an automated output.

**Source:** Pipeline stages and human review

## MA-ch06.28

Auditors submit paired résumés to a text-generating model, identical except for a first name signalling group A or group B, and count the pairs where the model's answers differ. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Submitting paired inputs that differ in one signal is a correspondence test, also called a paired audit.
- [ ] B. Finding that outputs depend on the name identifies the training data as the source.
- [ ] C. A sign test counts the concordant pairs and ignores the discordant pairs.
- [ ] D. Because outputs are sampled randomly, pairs with differing answers carry no information.
- [ ] E. Matching by construction controls for qualifications within each pair.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It isolates dependence of the output on the varied signal.
- B: Dependence could come from training data, tuning or the prompt, which is a separate question.
- C: A sign test uses the discordant pairs, those treated differently.
- D: Randomness is part of the null distribution, and a test on differing pairs accounts for it.
- E: Identical content removes qualifications as an explanation inside the pair.

**Source:** Correspondence test and sign test

## MA-ch06.29

Two annotators label 100 clinical notes. They agree on 90, and each calls 90% of the notes positive. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Cohen's kappa corrects observed agreement for the agreement expected by chance.
- [ ] B. Kappa can be low even when raw agreement is high.
- [ ] C. Inter-annotator agreement measures consistency of labelling, not validity.
- [ ] D. Chance agreement is high when one category dominates, so kappa falls below raw agreement.
- [ ] E. Agreement between annotators is a measure of label validity.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Kappa is observed agreement minus chance agreement, scaled by the maximum possible improvement over chance.
- B: A dominant category inflates chance agreement, which lowers kappa.
- C: Annotators can agree with each other and share the same systematic error.
- D: A skewed class balance inflates the chance term.
- E: Validity asks whether labels capture the true condition, which agreement does not show.

**Source:** Cohen's kappa and label validity

## MA-ch06.30

A skin-lesion classifier has a higher error rate on darker skin. A test set labelled by the same process as the training data and a separate audit set labelled by independent experts using biopsy results show the same gap. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The audit set shows that the gap comes from under-representation in the training data.
- [ ] B. Collecting more images of the same kind removes a label-quality problem.
- [ ] C. Biopsy results serve as a reference standard, also called ground truth, for the lesion labels.
- [ ] D. An independent labelling source addresses the possibility that test and training labels share errors.
- [ ] E. Image capture conditions can still differ by group, even with independent labels.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Under-representation is consistent with the gap but untested, and other causes remain.
- B: Label quality does not improve with more images produced by the same labelling process.
- C: A reference standard is the best available measure of the true condition.
- D: Independent labels remove shared label error as an explanation of the gap.
- E: Independent labelling does not control for how images were produced.

**Source:** Reference standard and label error

## MA-ch06.31

A causal framework describes three rungs: association (seeing), intervention (doing) and counterfactual (imagining). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A counterfactual question is a rung 2 question about an average effect.
- [ ] B. A counterfactual question asks what happens on average when X is set by force.
- [ ] C. Observing a conditional probability and setting a variable by force give the same quantity in general.
- [ ] D. A rung 1 question concerns the conditional probability of an outcome given an observed value, P(Y given X).
- [ ] E. A rung 2 question concerns the probability of an outcome under an intervention, written P(Y given do(X)).

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Counterfactuals sit on rung 3 and concern a specific case.
- B: That describes an intervention at rung 2, while a counterfactual concerns a specific case.
- C: Confounding makes the observed and interventional quantities differ.
- D: Association asks what goes with what in observed data.
- E: The do operator marks setting X by force rather than observing it.

**Source:** Ladder of causation, rungs 1 to 3

## MA-ch06.32

A lender trains a model on past loans to predict default from 30 recorded features, and it ranks risk well on new applicants who resemble past borrowers. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Feature importance is a different thing from causal effect.
- [ ] B. The model estimates conditional probabilities, which is association at rung 1.
- [ ] C. A feature that is a consequence of the label can inflate accuracy, which is leakage.
- [ ] D. A large weight on a feature shows that the feature causes default.
- [ ] E. Good prediction on similar cases shows what would happen if the lender changed a feature.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Importance describes use by the model, and causal effect describes the result of an intervention.
- B: Prediction fits observed relationships between features and outcome.
- C: Leakage lets the model use information that would not be available at prediction time.
- D: A feature can carry weight as a proxy, an effect of default, or a shared cause.
- E: A prediction describes what goes with a value, not what follows from changing it.

**Source:** Prediction versus causation, leakage

## MA-ch06.33

Customers who received a marketing email signed up at a higher rate than customers who did not. The email went mostly to customers who were already engaged with the app, and engaged customers sign up more often regardless. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The raw difference in sign-up rates is an association, a rung 1 quantity.
- [ ] B. Random assignment of the email makes the two groups equivalent in expectation.
- [ ] C. Confounding is the same thing as measurement bias.
- [ ] D. A larger sample removes the confounding.
- [ ] E. Engagement is a confounder, because it influences both who is emailed and who signs up.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: It describes how rates differ across observed groups.
- B: Randomisation removes confounding by making treatment independent of prior factors.
- C: Confounding is a shared cause of treatment and outcome, and measurement bias is an error in recording.
- D: More data shrinks random error but leaves the offset caused by who was emailed.
- E: A confounder is a common cause of treatment and outcome.

**Source:** Confounding and association

## MA-ch06.34

Engaged customers sign up at 10% without the email, and the email raises everyone's sign-up probability by 1.5 points. The email was sent to most engaged customers and few others, and engaged customers sign up more often anyway. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The raw difference between emailed and non-emailed customers is an unbiased estimate of the average treatment effect.
- [ ] B. An average treatment effect describes one named customer's response.
- [ ] C. Stratifying by engagement and comparing within strata removes confounding by engagement, if no other confounder remains.
- [ ] D. Standardisation weights each stratum's effect by that stratum's share of the population.
- [ ] E. The raw comparison overstates the effect, because engagement pushes the treated group's rate up.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Confounding makes the raw difference biased as an estimate of the effect.
- B: An average treatment effect is a population average, not an individual effect.
- C: Within a stratum, treated and untreated customers have the same engagement.
- D: Standardisation averages stratum effects over a reference population mix.
- E: A positive confounder inflates the observed difference.

**Source:** Stratification and standardisation

## MA-ch06.35

A dataset records two yes-or-no variables, coffee each day (X) and high resting heart rate (Y), which are associated. One story says coffee raises heart rate, another says a high heart rate leads people to drink coffee, and a third says anxiety raises both. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Randomly assigning coffee and comparing heart rates would separate them.
- [ ] B. The story in which heart rate leads to coffee is reverse causation.
- [ ] C. Under the confounder story, coffee and heart rate are not associated.
- [ ] D. The story in which anxiety raises both variables involves a confounder.
- [ ] E. Different causal graphs can imply the same joint distribution of X and Y, so the stories are observationally equivalent.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: An intervention on X removes arrows into X and tests the direct effect.
- B: Reverse causation means the outcome influences the supposed cause.
- C: A common cause creates association even when X has no effect on Y.
- D: A common cause produces association without a direct effect.
- E: Observational equivalence means data on X and Y alone cannot choose between the graphs.

**Source:** Reverse causation and confounding

## MA-ch06.36

An analyst adjusts a comparison for a variable that is influenced by both the treatment and the outcome, and separately for a variable lying on the path from treatment to outcome. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Conditioning on a collider can create a spurious association between its causes.
- [ ] B. Adding more adjustment variables reduces bias whatever their causal role.
- [ ] C. A variable with arrows pointing into it from two other variables is a collider.
- [ ] D. A mediator lies on the path from treatment to outcome, so adjusting for it blocks part of the effect.
- [ ] E. A confounder is a variable caused by the treatment.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Adjusting for a common effect opens a path that was closed.
- B: Adjusting for colliders or mediators can introduce or block real paths.
- C: A collider is a common effect of two variables.
- D: Mediators carry the effect, and conditioning on them removes that part.
- E: A confounder is a cause of both treatment and outcome, and a variable caused by treatment is a mediator or descendant.

**Source:** Collider, mediator and adjustment

## MA-ch06.37

A hospital wants to know what would have happened to patients who got a follow-up call had they not been called, and it compares them with patients who were not called. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The comparison group stands in for the missing outcomes if it is exchangeable with the called group.
- [ ] B. Each patient is observed under one condition, so the other potential outcome is missing, which is the fundamental problem of causal inference.
- [ ] C. An average treatment effect is a group-average quantity, whereas an individual treatment effect is unobserved.
- [ ] D. The counterfactual outcome is observed directly by looking at the same patient twice.
- [ ] E. Matching on measured variables guarantees exchangeability on unmeasured variables.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Exchangeability means the groups would have had the same outcomes absent treatment.
- B: A unit cannot be observed under both the treated and untreated condition.
- C: Group comparisons estimate averages, not what happened to one patient.
- D: The same patient cannot be both called and not called at the same time.
- E: Matching balances only the variables used.

**Source:** Potential outcomes and exchangeability

## MA-ch06.38

Among engaged customers, 11.5% sign up if emailed and 10% if not. One emailed engaged customer signed up, and the question is whether the email caused it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Group rates alone identify the individual-level probability without further assumptions.
- [ ] B. Without monotonicity, the data give bounds rather than a single value, which is partial identification.
- [ ] C. Probability of necessity is a rung 2 quantity.
- [ ] D. Under monotonicity and equivalent groups, the probability of necessity for an emailed sign-up is one minus the ratio of the two group rates.
- [ ] E. Monotonicity is the assumption that the email does not make an individual less likely to sign up.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Many individual patterns are compatible with the same group rates.
- B: Partial identification yields a range of values consistent with the data.
- C: It concerns a specific case and a contrary-to-fact action, so it sits on rung 3.
- D: Probability of necessity is the chance the outcome would not have occurred without the treatment, given that both occurred.
- E: Monotonicity rules out individuals who respond negatively to the treatment.

**Source:** Probability of necessity and monotonicity

## MA-ch06.39

A retailer studies whether a discount coupon keeps customers from leaving. It considers four questions: which customers who got coupons stayed, whether this customer will stay given her usage, how many would stay if coupons went to everyone, and whether this particular customer would have stayed without her coupon. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing the stay rate of coupon recipients with non-recipients is a rung 1 question.
- [ ] B. How many would stay if coupons went to everyone is a counterfactual, rung 3 question.
- [ ] C. A rung 2 question can be answered from association alone without extra assumptions.
- [ ] D. Predicting whether a customer will stay from her usage is a rung 2 question.
- [ ] E. Whether this customer would have stayed without the coupon is a rung 3 question.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: It describes how outcomes differ across observed groups.
- B: It asks about an intervention on the whole population, which is rung 2.
- C: Going from observed data to a causal claim needs assumptions or an intervention.
- D: Prediction from observed features is association, which is rung 1.
- E: It concerns a specific unit under a contrary-to-fact action.

**Source:** Ladder of causation, coupon example

## MA-ch06.40

A bank assigns a reminder to customers by coin flip and compares the share who pay on time between the reminded and the not-reminded. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Randomisation balances measured confounders but leaves unmeasured ones uncontrolled.
- [ ] B. The comparison identifies an average effect, not each customer's effect.
- [ ] C. Self-selection into the reminder reintroduces confounding.
- [ ] D. Random assignment makes the groups exchangeable in expectation, measured or not.
- [ ] E. Randomisation guarantees the two groups are balanced in each sample.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Its advantage over adjustment is that it handles unmeasured factors as well.
- B: Individual effects are not observed under randomisation either.
- C: People who opt in differ from those who do not, mixing the reminder with the drivers of opting in.
- D: Randomisation balances prior factors on average, including unmeasured ones.
- E: Chance leaves some imbalance in a finite sample, so equivalence holds only in expectation.

**Source:** Randomisation

## MA-ch06.41

A bank emailed every customer with income above a threshold and no customer below it, and recorded who signed up. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Without untreated customers at the same income level, a larger sample under the same rule still lacks a comparison group.
- [ ] B. Positivity, also called overlap, requires both treated and untreated units at each kind of customer.
- [ ] C. Assigning treatment by a threshold on income is a randomised design.
- [ ] D. Extrapolating the effect to low incomes rests on modelling assumptions rather than on data.
- [ ] E. Income is a confounder here, because it likely affects both who is emailed and who signs up.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: The missing comparison group is a design problem, not a sample size problem.
- B: Without overlap there is no comparison group at the same covariate values.
- C: A deterministic threshold on a covariate is not random assignment.
- D: No observations exist in that range to support the estimate.
- E: A variable that determines treatment and also affects the outcome confounds the comparison.

**Source:** Positivity and overlap

## MA-ch06.42

A coin lands heads with probability 0.7. A student estimates the heads probability from 20 flips and gets 0.65. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Calling the coin biased uses bias in the everyday sense of a process tilted away from a symmetric reference.
- [ ] B. Estimator bias is the expected value of an estimator minus the true value.
- [ ] C. An unbiased estimator can still miss the truth in a single sample.
- [ ] D. The sample proportion is a biased estimator of the heads probability.
- [ ] E. Sampling error and estimator bias are the same thing.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: The process itself departs from 0.5.
- B: It is a property of the estimator's average behaviour over repeated samples.
- C: Unbiased means correct on average, not correct each time.
- D: Its expected value equals the true probability, so its bias is zero.
- E: Sampling error is the miss in a single sample, and bias is the average miss.

**Source:** Two meanings of bias

## MA-ch06.43

In a population of 500,000 women and 500,000 men, 600 women and 1,400 men are data scientists. A separate league has a rule that only men may play. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An absolute difference and a ratio of rates carry the same information when the rates are small.
- [ ] B. A gap created by an explicit rule and a gap in occupational choice have the same cause.
- [ ] C. A ratio of rates hides exclusion that a small absolute difference shows.
- [ ] D. The probability of being a woman given being a data scientist differs from the probability of being a data scientist given being a woman.
- [ ] E. The event before the vertical bar supplies the denominator in a conditional probability.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Small rates can give a small difference alongside a large ratio.
- B: A rule that excludes a group is a different mechanism from differing rates of entry.
- C: A ratio exposes exclusion that a small absolute difference can hide.
- D: Transposing the conditional changes the denominator, which is a common error.
- E: The event after the bar is the condition and supplies the denominator.

**Source:** Conditional probability and rate comparisons

## MA-ch06.44

An analyst estimates a population variance using the sum of squared deviations from the sample mean divided by n, instead of n minus 1. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An unbiased estimator has the lowest mean squared error of the available estimators.
- [ ] B. The bias of the divide-by-n estimator grows as the sample size grows.
- [ ] C. Dividing by n gives a biased estimator that underestimates the variance on average.
- [ ] D. Mean squared error equals variance plus squared bias.
- [ ] E. Accepting a little bias for a large drop in variance is the bias-variance trade-off, which shrinkage estimators exploit.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A biased estimator with lower variance can have a smaller mean squared error.
- B: The bias shrinks in proportion to one over n.
- C: Deviations from the sample mean are smaller than deviations from the true mean.
- D: This decomposition holds for any estimator.
- E: Shrinkage lowers variance at the cost of some bias.

**Source:** Estimator bias and mean squared error

## MA-ch06.45

In a survey, every actual voter says they voted, and some non-voters also say they voted. Respondents were chosen by simple random sampling. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Nonresponse bias, meaning selected people declining to answer, is the cause here.
- [ ] B. Misreporting of this kind is response bias, a form of measurement bias.
- [ ] C. A gold standard on a validation subset lets analysts estimate the size of the recording error.
- [ ] D. Interviewing more respondents removes the misreporting offset.
- [ ] E. Selection bias is absent, because each resident had an equal chance of being sampled.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Respondents answered, so the issue is accuracy of answers and not refusal.
- B: Response bias arises when answers differ from the truth.
- C: The error cannot be seen from reported values alone.
- D: More respondents shrink random error around the distorted centre.
- E: The distortion is in what respondents report, not in who was chosen.

**Source:** Response bias and measurement bias

## MA-ch06.46

A researcher builds a map of startups from an online directory. The directory lists a startup more often if it is in Region R, and the researcher finds Region R holds a larger share than expected. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The listing probability is the inclusion probability, and it differs between regions here.
- [ ] B. A larger directory under the same listing rule corrects the distortion.
- [ ] C. A prior expectation that Region R should lead is a validation of the dataset.
- [ ] D. Inclusion that depends on the attribute being studied is selection bias.
- [ ] E. Selection bias disappears when inclusion is independent of the quantity being measured.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Unequal inclusion probabilities distort the shares in the data.
- B: The same rule reproduces the same skew with less noise.
- C: An expectation is a hypothesis, and a check compares the data against an independent source.
- D: The rule for entering the data is tied to the region.
- E: Without a link between inclusion and the outcome, the sample is not distorted by it.

**Source:** Selection bias from inclusion rules

## MA-ch06.47

A poll draws 2,400,000 responses from a frame of telephone and car owners, in a period when owning those things is linked to voting intention, and reports a margin of error of 0.06 percentage points. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A very large sample cancels the bias.
- [ ] B. The margin of error quantifies sampling error and not bias.
- [ ] C. Excluding people without telephones or cars is nonresponse bias.
- [ ] D. A tiny margin around a skewed centre describes an accurate but imprecise estimate.
- [ ] E. Weighting repairs the gap for people the frame did not reach.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: Sample size shrinks variance but leaves the offset.
- B: It describes random variation under the sampling design.
- C: The frame never reached them, so it is coverage bias, not people declining to answer.
- D: It describes a precise but inaccurate estimate.
- E: People with no chance of selection have no respondents to weight up.

**Source:** Coverage bias, precision versus accuracy

## MA-ch06.48

X takes the values minus 1, 0 and 1 with equal probability, and Y equals 1 when X is not 0 and equals 0 when X is 0. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Zero correlation between X and Y does not imply that X and Y are independent.
- [ ] B. Independent variables can have a non-zero correlation.
- [ ] C. Correlation is a measure of association, which sits on rung 1.
- [ ] D. X and Y are statistically dependent, because knowing X changes the distribution of Y.
- [ ] E. A correlation of zero demonstrates that X has no causal effect on Y.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Correlation captures linear association, and other dependence can remain.
- B: Independence implies zero covariance and so zero correlation.
- C: It describes co-movement in observed data.
- D: Y is a function of X, which is the strongest dependence.
- E: Correlation is an association measure and does not speak to interventions.

**Source:** Correlation versus independence

## MA-ch06.49

A poll of 1,000 likely voters treated as a simple random sample finds candidate A at 48% and candidate B at 47%, and a headline reads that A leads. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The margin of error shrinks in proportion to one over the square root of the sample size.
- [ ] B. The margin of error includes the effect of nonresponse bias.
- [ ] C. The margin of error on the lead is larger than the margin of error on a single share.
- [ ] D. A lead smaller than the margin of error on a single share is evidence that the leader is ahead.
- [ ] E. The two shares are negatively related, because they come from the same respondents.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Quadrupling the sample halves the margin.
- B: It reflects random sampling error only under the stated design.
- C: The lead is a difference of two shares and has more variability.
- D: A lead that small is well within the variability of the estimate.
- E: More support for one candidate means fewer respondents left for the other.

**Source:** Margin of error on a lead

## MA-ch06.50

A forecaster gives three races win probabilities of 0.9, 0.8 and 0.6 and treats the races as independent, although a shared polling error could move all three together. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A forecast probability of 0.9 means the party wins 90% of the seats in a race.
- [ ] B. For independent events, the joint probability is the product of the individual probabilities.
- [ ] C. Treating the races as independent understates the chance of extreme results when errors are correlated.
- [ ] D. The expected number of wins equals the sum of the probabilities if the races are independent, and differs if they are correlated.
- [ ] E. A systematic polling error shared by the races produces correlated outcomes.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: It is a probability of winning, not a vote share.
- B: Independence means one outcome gives no information about another.
- C: Correlation fattens the tails of the joint distribution.
- D: Expectation is additive regardless of dependence.
- E: A common error source links the races beyond their individual probabilities.

**Source:** Independence and correlated errors

## MA-ch06.51

A team tests 20 unrelated hypotheses at the 5% significance level, and every null hypothesis is true. It writes up only the significant results. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Conditioning on significance keeps large estimates, so reported effects are inflated, a pattern called the winner's curse.
- [ ] B. Unreported tests leave no trace in the paper, which is how publication bias hides.
- [ ] C. A Type I error means failing to detect a real effect.
- [ ] D. Reporting just the significant results out of many tests is selective reporting.
- [ ] E. A significant result among 20 true nulls shows a real effect.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Selecting on significance favours overestimates.
- B: Publication bias arises when results are filtered before they are seen.
- C: A Type I error is rejecting a true null hypothesis.
- D: Filtering by outcome distorts the evidence shown.
- E: At a 5% rate, some false positives are expected among many tests.

**Source:** Publication bias and winner's curse

## MA-ch06.52

A classifier predicts whether each applicant is qualified. The qualified share is 30% in group A and 10% in group B, and the classifier is perfect. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Demographic parity means equal accuracy across groups.
- [ ] B. A perfect classifier satisfies demographic parity whatever the base rates.
- [ ] C. Satisfying demographic parity here would require misclassifying some applicants.
- [ ] D. A perfect classifier satisfies equalized odds.
- [ ] E. With unequal base rates, a perfect classifier has unequal selection rates, which violates demographic parity.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: It means equal selection rates, which differs from equal accuracy.
- B: Perfect predictions mirror the base rates, so parity fails when they differ.
- C: Equal selection rates need some qualified people rejected or some unqualified ones accepted.
- D: The true positive rate is one and the false positive rate is zero in both groups.
- E: Selection rates equal the base rates when predictions are perfect.

**Source:** Perfect classifier and fairness criteria

## MA-ch06.53

A company trains a ranking model on ten years of its own hiring records. Disparities can enter at different stages: past hiring decisions, who appears in the data, how features and labels are measured, how the model is evaluated, and how the ranking is used afterwards. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Applicants screened out earlier have no outcomes in the data, which is a form of selection bias.
- [ ] B. Noisier or distorted features and labels for some groups are measurement bias.
- [ ] C. Past decisions that reflect earlier practices are historical bias.
- [ ] D. Disparity created when reviewers act on the ranking is called representation bias.
- [ ] E. Using a pooled metric that hides weak subgroups is called deployment bias.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: Who has recorded outcomes depends on earlier decisions.
- B: Measurement bias concerns how variables are recorded.
- C: Historical bias comes from the world that produced the data.
- D: That arises at use and belongs to deployment, whereas representation bias concerns thin coverage in the data.
- E: Hiding subgroups in a pooled metric is aggregation or evaluation bias.

**Source:** Bias types mapped to pipeline stages

## MA-ch06.54

An audit finds that a triage model refers 24% of patients from group X and 15% of patients from group Y to a specialist programme, and the difference is far too large to be chance. A manager concludes the model is biased against group Y. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Clinical need can differ between the groups, so the disparity does not by itself show bias in the model.
- [ ] B. The gap is a disparity, a descriptive difference in outcomes between groups.
- [ ] C. A rung 1 comparison of referral rates answers whether the model would refer more group Y patients if group membership were changed.
- [ ] D. Statistical significance of the gap shows which pipeline stage caused it.
- [ ] E. Comparing patients of similar severity separates need from other causes, with the limit that unmeasured factors remain.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Differences in need, data, labels, cutoffs or review can each produce a gap.
- B: A disparity records that outcomes differ without saying why.
- C: That is an interventional question, which a descriptive comparison cannot answer.
- D: Significance rules out chance and does not locate a cause.
- E: Stratifying on legitimate covariates narrows the explanations.

**Source:** Disparity versus bias

## MA-ch06.55

A firm trains a model to predict promotion from ten years of its own records and finds it highly accurate on held-out records. In those years promotion went to one group more often than to others at comparable measured performance. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Accuracy on held-out records from the same process measures how fair the labels are.
- [ ] B. A model that reproduces a biased label accurately is evidence that the label is fair.
- [ ] C. A held-out split drawn from the same process is an out-of-distribution evaluation.
- [ ] D. This situation is label bias carried through historical bias.
- [ ] E. Evaluating on records from the same pipeline detects bias in the labels.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Accuracy measures agreement with the labels and says nothing about their fairness.
- B: High accuracy can mean the model copied the bias.
- C: A split from the same process is an in-distribution evaluation.
- D: The labels encode past decisions that favoured one group.
- E: Test labels share the source of the training labels and carry the same bias.

**Source:** Accuracy against biased labels

## MA-ch06.56

A vendor claims its hiring model is not biased because it trained on 20 million records, that it has 94% accuracy for each group on held-out data from its own pipeline, and that it passes the one fairness metric tested. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A large training set shrinks variance but leaves bias from the data collection process.
- [ ] B. Held-out data from the same pipeline is an in-distribution test, which can miss problems that appear elsewhere.
- [ ] C. Passing one fairness metric shows that the model satisfies the other fairness criteria.
- [ ] D. External validity concerns whether results hold in the population where the model will be used.
- [ ] E. Equal accuracy across groups implies equal selection rates and equal error rates of each type.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Volume does not correct a skewed process.
- B: In-distribution results may not transfer to a different population.
- C: Fairness criteria can conflict, so passing one does not imply the rest.
- D: Generalising beyond the test pipeline is a separate question from internal accuracy.
- E: Accuracy hides how errors are split between false positives and false negatives.

**Source:** Evaluating vendor claims

## MA-ch06.57

A salary-recommendation model predicts salaries for women that are on average 8% lower than for men. Among employees at the same job level, the gap is 2%. Job level was assigned by earlier promotion decisions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A smaller adjusted gap shows the model does not discriminate.
- [ ] B. Job level can be a mediator, because group may influence promotion, which then influences salary.
- [ ] C. The 8% figure is an unadjusted gap, and the 2% figure is a gap adjusted for job level.
- [ ] D. The adjusted gap is the better figure because job level is a legitimate explanation of pay.
- [ ] E. Adjusting for job level removes the part of the gap that runs through promotion.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: The remaining gap and the part running through job level are each open to question.
- B: A mediator lies on a path from group to outcome.
- C: Adjusting for a variable compares people within its levels.
- D: Job level was itself shaped by earlier decisions, so it may carry the bias being studied.
- E: Conditioning on a mediator blocks the effect that travels through it.

**Source:** Adjusted versus unadjusted gap and mediation

## MA-ch06.58

A company deploys a support assistant built on a language model licensed from a provider. Testers find that answer quality and tone differ across customer groups in ways that the company's own prompts, data and code do not explain. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The company can show where the disparity entered without information from the provider.
- [ ] B. Using a licensed model transfers accountability for the assistant's behaviour to the provider.
- [ ] C. Behavioural testing with paired prompts can probe the model without access to its training data.
- [ ] D. A model card or system documentation from the provider is useful evidence for the investigation.
- [ ] E. The licensed model is an upstream component, and the company's prompts and code are downstream.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Locating the source in training data or tuning needs documentation from the provider.
- B: The company deploys the system and keeps accountability for its use.
- C: Black-box testing relies on inputs and outputs.
- D: Documentation of intended use and subgroup performance helps the deployer judge fitness for use.
- E: Upstream and downstream describe position in the supply chain of a system.

**Source:** Upstream models and accountability
