# Chapter 1: The skeptic's toolkit

## MA-ch01.1

A reviewer rewrites the vague claim "the assistant is reliable" so that it can be tested, and asks for the exact terms for each part. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An assumption is a result observed after the test has been run.
- [ ] B. A falsifier is a statement of how confident the team is that the claim will hold.
- [ ] C. A claim that no possible observation could contradict is called unfalsifiable.
- [ ] D. A falsifier names an observation, with a threshold and a time window, that would count against the claim.
- [ ] E. "The assistant performs well in the situations that matter" is a falsifier because it names the goal.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: An assumption is a condition taken as given, and stated beforehand, for the claim to hold.
- B: A falsifier is an observation that would count against the claim, not a statement of confidence.
- C: Unfalsifiable claims are compatible with every outcome, so they carry no testable content.
- D: A checkable falsifier says in advance which result would show the claim to be wrong.
- E: Naming a goal without a metric or threshold leaves no observation that could contradict the statement.

**Source:** Falsifier and unfalsifiable claim

## MA-ch01.2

A team says that adding a retrieval step makes its assistant hallucinate less, and a reviewer asks for the claim in testable form on a held-out question set. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An assumption is a condition taken as given, such as that the held-out questions resemble real use.
- [ ] B. A falsifier could be a hallucination rate with retrieval that is no lower than the rate without it, at a stated threshold.
- [ ] C. A falsifier is the prediction repeated in different words.
- [ ] D. A held-out set is data used to train the retrieval step.
- [ ] E. The prediction states a measurable direction of change, such as a lower hallucination rate, on a named held-out set.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Assumptions are the conditions under which the prediction is expected to hold.
- B: It names a result that would count as failure of the claim.
- C: A falsifier is the result that would refute the prediction, not a restatement of it.
- D: A held-out set is data withheld from training and tuning so it can test the claim.
- E: A prediction is a specific, measurable statement made before the test.

**Source:** Prediction, assumption, falsifier, held-out set

## MA-ch01.3

A vendor says its content filter lets through no step-by-step instructions for listed hazardous compounds. As evidence it reports that 10,000 prompts written by its own staff to look like ordinary requests produced none. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Zero failures in a test prove that the true failure rate is zero.
- [ ] B. Prompts written to resemble ordinary requests are a non-adversarial sample and say little about deliberate attempts to get past the filter.
- [ ] C. A universal claim of this kind is refuted by a single counterexample.
- [ ] D. The 10,000 passing prompts verify the universal claim.
- [ ] E. Red teaming means repeating the vendor's ordinary prompts at larger volume.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Zero observed failures gives an upper bound on the rate that is above zero.
- B: The test inputs differ in kind from the inputs the claim is about.
- C: One observed instance of the forbidden output is enough to contradict a claim stated as a universal.
- D: A finite set of passing cases supports the claim to a limited degree and does not verify it.
- E: Red teaming is deliberate, adversarial effort to make the system fail.

**Source:** Universal claim, counterexample, red teaming

## MA-ch01.4

A manager wants her team to practise methodical skepticism, and asks which words describe what she wants and what she wants to avoid. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Methodical skepticism is a procedure applied to a specific claim, whose use can be seen.
- [ ] B. Confirmation bias is the tendency to favour evidence that agrees with what one already believes.
- [ ] C. Cynicism is a procedure that can be performed on one particular claim.
- [ ] D. Writing down what a wrong answer would look like before reading the output fixes the criterion in advance.
- [ ] E. Agreement between an output and the reviewer's own earlier judgments is independent evidence that the output is right.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Methodical skepticism is a repeatable method, such as writing the failure criterion first.
- B: It makes a reviewer accept outputs that match prior judgment.
- C: Cynicism is a general attitude of distrust, not a procedure applied to a claim.
- D: A criterion set beforehand cannot be bent to fit whatever the output says.
- E: That agreement is not independent of the reviewer, and can repeat the reviewer's mistakes.

**Source:** Methodical skepticism, cynicism, confirmation bias

## MA-ch01.5

A loan-scoring system outputs "default risk 0.82, decline" for an applicant, and a reviewer lists the conditions under which that score would be wrong for this person. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If few training examples resemble this applicant, the score is an extrapolation and deserves less trust.
- [ ] B. Submitting the same application twice and receiving the same score shows that the score is accurate.
- [ ] C. Writing the list of conditions is itself the test that shows which conditions hold.
- [ ] D. A unit mismatch between two source systems is a modelling error, not an input data fault.
- [ ] E. If applicants now arriving come from a different population than the validation sample, the validation result may not carry over; this is distribution shift.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Extrapolation means predicting in a region the training data covers thinly.
- B: Reproducibility shows consistency, not accuracy.
- C: The list names suspects; each condition still needs its own inspection.
- D: Entering income in thousands in one system and in units in another is a data-quality fault in the input.
- E: Distribution shift is a change between the data a model was validated on and the data it now sees.

**Source:** Distribution shift, extrapolation, reproducibility versus accuracy

## MA-ch01.6

Before an experiment a researcher writes in a dated file: the new prompt will raise exact-match accuracy by at least 2 points, and a gain below 0.5 points or any drop means the claim has failed. The run shows a gain of 1.2 points. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Moving the failure line to 1 point after seeing the result keeps the test a pre-registered test.
- [ ] B. Shifting a threshold after seeing the result is called moving the goalposts.
- [ ] C. A gain between the failure line and the predicted size leaves the claim neither confirmed nor refuted, which is an inconclusive result.
- [ ] D. Recording the prediction and failure rule in a dated file before the run is pre-registration.
- [ ] E. A gain of 1.2 points meets the stated prediction.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Changing the rule after the result removes the protection pre-registration gives.
- B: The criterion is adjusted to fit the outcome instead of the outcome being judged against the criterion.
- C: The pre-set rule marks the claim as failed or supported only outside this middle band.
- D: Pre-registration fixes the prediction and decision rule before the data are seen.
- E: The prediction was a gain of at least 2 points, so the result falls short of it.

**Source:** Pre-registration, inconclusive result, moving the goalposts

## MA-ch01.7

After a prompt change shows no overall gain, an analyst compares 20 customer segments, finds one with p = 0.03, and says the change works there because that segment uses shorter queries. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The explanation about shorter queries, written after the result, is a prediction.
- [ ] B. The chance of at least one false positive across a set of tests is the familywise error rate, and it rises with the number of comparisons.
- [ ] C. A correction for multiple comparisons makes the per-test threshold looser.
- [ ] D. A p-value of 0.03 means there is a 3% probability that the change has no effect in that segment.
- [ ] E. Reporting the one significant segment out of 20 comparisons is an example of multiple comparisons, and of p-hacking when the others are not reported.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: An explanation written after the result is post hoc, since it can be fitted to the data.
- B: Each added test adds another chance of a spurious result.
- C: A correction makes the per-test threshold stricter.
- D: A p-value is the probability of data this extreme if there is no effect, not the probability that there is no effect.
- E: Many tests inflate the chance of at least one small p-value arising by chance.

**Source:** Multiple comparisons, p-value, post hoc explanation

## MA-ch01.8

An LLM assistant with no access to a company's systems is asked why a query is slow, and replies with a confident, well-organised account naming a specific table and setting. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A confident tone is a measure of calibration.
- [ ] B. Naming a specific table is evidence that the model had access to the system.
- [ ] C. An explanation not grounded in access to the system is a hallucination, sometimes called confabulation.
- [ ] D. The right status for the account is a hypothesis that still needs a test.
- [ ] E. Fluency describes the style of the text and not the evidence behind it.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Calibration is agreement between stated confidence and the observed fraction correct, and tone does not measure it.
- B: Specific detail is easy to generate and does not show access.
- C: The model produces plausible text without evidence about this database.
- D: A hypothesis becomes a finding only after an observation that could have contradicted it.
- E: A well-written answer can be unsupported.

**Source:** Fluency, hallucination, hypothesis

## MA-ch01.9

An LLM given only a table of weekly revenue writes a specific account blaming a competitor's price cut for an 8% fall, though a shifted billing date or a moved holiday fits the table equally well. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The account the model wrote should be chosen because it is the most fluent.
- [ ] B. When several accounts fit the same data equally well, the data underdetermine the cause.
- [ ] C. Restating the same table in more detail in the prompt breaks the tie.
- [ ] D. Telling the accounts apart takes a discriminating observation, such as billing-date records, that the rival accounts predict differently.
- [ ] E. Rival accounts that fit the data equally well are called confounders.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Fluency is not evidence and does not break a tie between accounts.
- B: Underdetermination means the evidence does not single out one explanation.
- C: More detail of the same data does not separate accounts that already fit it equally.
- D: A discriminating observation is one whose outcome differs under the rival accounts.
- E: They are rival or alternative hypotheses; a confounder is a variable linked to both cause and outcome.

**Source:** Underdetermination, rival hypotheses

## MA-ch01.10

An LLM assistant states at least 90% confidence on 200 answers, and an audit finds 150 of them correct. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The audit measures discrimination, the ability to rank correct answers above incorrect ones.
- [ ] B. Stating the same confidence on each answer is required for a model to count as calibrated.
- [ ] C. Accuracy and calibration are different properties.
- [ ] D. Calibration is agreement between stated confidence and the fraction of answers that are correct.
- [ ] E. Stated confidence above the observed fraction correct is overconfidence.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: Comparing stated confidence with hit rate measures calibration.
- B: A model can vary its confidence and still be calibrated.
- C: A model can be accurate overall and still state confidence that is too high or too low.
- D: A calibrated 90% statement is right about 90% of the time.
- E: The model's confidence statements are higher than its hit rate.

**Source:** Calibration, overconfidence, accuracy

## MA-ch01.11

An analyst wants a second check on a model-written answer to a question about a company's revenue in a given year. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Looking up the figure in the company's filed annual report is a check independent of the model's recall.
- [ ] B. A check is independent when its errors do not move together with the errors of the first check.
- [ ] C. A second model trained on largely the same data gives errors that are uncorrelated with the first model's.
- [ ] D. Asking the same model the same question again and getting the same answer is an independent check.
- [ ] E. Agreement among checks that copy the same source strengthens the evidence in proportion to the number of checks.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: A primary source has errors unrelated to the model's errors.
- B: Independence of errors is what makes a second check add evidence.
- C: Shared training data makes the two models' errors move together.
- D: Repeating a source gives a correlated answer, not independent evidence.
- E: Copies of one source count as one source.

**Source:** Independent evidence, correlated errors

## MA-ch01.12

Two reviewers inspect the same batch for a defect, and a manager asks how redundancy helps and what terms describe the reviewers' performance. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. If the reviewers' misses are independent, the chance that both miss a defect is lower than for either alone.
- [ ] B. Correlated errors reduce the benefit of adding a second reviewer.
- [ ] C. Redundancy improves detection whatever the correlation between reviewers.
- [ ] D. Two reviewers who use the same checklist and the same examples have independent errors.
- [ ] E. Precision is the share of real defects that a reviewer finds.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Independent failures combine so that joint failure is rarer.
- B: If both tend to miss the same defects, the second adds little.
- C: The gain from redundancy shrinks as errors become more correlated.
- D: Shared method and training make errors correlated.
- E: The share of real defects found is recall, also called sensitivity.

**Source:** Redundancy, correlated errors, recall versus precision

## MA-ch01.13

A team has a language model answer 500 support questions and then grades each answer pass or fail by prompting the same model as a judge, reporting a 94% pass rate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Using the same model to generate and to grade creates circularity, because the two share blind spots.
- [ ] B. A 94% pass rate from the judge is an estimate of accuracy against ground truth.
- [ ] C. A model judge's verdicts are ground truth labels.
- [ ] D. Self-preference bias is a judge's tendency to prefer outputs from other models.
- [ ] E. Comparing the judge's verdicts with human labels on a sample checks the judge against an independent reference.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: A judge with the same weaknesses as the generator tends to approve its mistakes.
- B: It measures agreement with the judge, which is not ground truth.
- C: Ground truth comes from an independent, trusted source, not from another model's opinion.
- D: Self-preference bias is the tendency to prefer its own outputs.
- E: Human labels from a domain expert supply a reference the judge did not produce.

**Source:** LLM-as-judge, circularity, ground truth

## MA-ch01.14

A reporter finds the statistic "62% of firms have adopted technology X" in five articles that cite different outlets, but all five trace to one press release from a vendor that sells X, with no sample size or method given. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The number of articles that repeat a statistic is a measure of its reliability.
- [ ] B. Provenance is the record of where a claim or dataset originated.
- [ ] C. Five articles repeating one release is circular reporting, which is one source and not five.
- [ ] D. A vendor that sells the technology has no conflict of interest in reporting its adoption.
- [ ] E. Lineage names the original source of a claim, while provenance records the transformations applied to it.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Repetition measures spread, not accuracy.
- B: Provenance answers the question of origin.
- C: Circular reporting is repetition of a single origin that looks like several.
- D: A source with a stake in the result has a conflict of interest, which is a reason to seek the primary data.
- E: Provenance records where a claim or dataset came from, and lineage records the chain of transformations it went through.

**Source:** Circular reporting, provenance versus lineage

## MA-ch01.15

A migration job logs "Migrated 12,000 rows: SUCCESS" and exits with status 0, but a row count run directly on the destination table returns 11,400. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing the destination count with the source count is validation, meaning a check that the right system was built.
- [ ] B. A claim of success is evidence of the same kind as an observed outcome.
- [ ] C. Exit status 0 shows that the output is correct.
- [ ] D. The log line is a report about the job, while the row count is a direct observation of the destination state.
- [ ] E. Verification checks the artifact itself instead of relying on the process's own account.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Comparing against the specification or source is verification; validation asks whether the system meets the real need.
- B: A claim reports an outcome and an observation shows it.
- C: It shows only that the process ended without reporting an error.
- D: A report and an observation are different kinds of evidence.
- E: Direct inspection of the output is what makes a check independent of the job's claim.

**Source:** Report versus state, verification

## MA-ch01.16

A nightly backup job has written "backup completed" and exited with status 0 on 400 nights in a row, and the goal is that data can be restored after a loss. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A restore test checks the goal, that data can be recovered, directly.
- [ ] B. 400 completion log lines are 400 independent verifications of recoverability.
- [ ] C. The "backup completed" log line is a proxy for recoverability.
- [ ] D. A proxy is a measure that stands in for the goal without being the goal.
- [ ] E. A restore test can still miss conditions it did not exercise, such as a partial loss.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Restoring from a backup is the observation that matches the goal.
- B: Each line is a report from the same job and says nothing about whether a restore works.
- C: A proxy is a measurable stand-in for the quantity that matters.
- D: Proxies can come apart from the goal they represent.
- E: A check covers only the cases it actually exercised.

**Source:** Proxy versus goal, restore test

## MA-ch01.17

A developer says her patch fixes a crash when a customer's name contains an apostrophe. Her test exports a record for "Olivia Smith" and passes after the patch. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An input at the boundary of normal variation, such as a name with an apostrophe, is an edge case.
- [ ] B. The "Olivia Smith" test is a regression test for the apostrophe bug.
- [ ] C. A passing test suite proves that the bug is fixed.
- [ ] D. A test that passes both before and after the patch does not discriminate between fixed and unfixed code.
- [ ] E. A test that fails on the unpatched code and passes on the patched code is a discriminating test.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Edge cases are where defects tend to hide.
- B: It does not exercise the failing condition, so it cannot catch a return of the bug.
- C: A pass shows only that the tested inputs behave correctly.
- D: A useful test is one whose result differs between the two states.
- E: Fail-before, pass-after shows the test responds to the fault.

**Source:** Discriminating test, regression test, edge case

## MA-ch01.18

A safety evaluation runs a chatbot on 100 prompts drawn at random from expected traffic and records 0 harmful responses. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The observed rate of zero in the sample is the population parameter.
- [ ] B. Random sampling from expected traffic lets the result describe adversarial traffic.
- [ ] C. Zero events in 100 trials gives an upper confidence bound on the harmful-response rate that is above zero.
- [ ] D. A confidence interval around an observed rate of zero is a single point at zero.
- [ ] E. Zero observed harmful responses means the true rate is zero.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: A sample statistic estimates the population parameter and can differ from it.
- B: A random sample describes the traffic it was drawn from.
- C: A small sample cannot rule out a modest rate; the rule of three gives roughly 3 divided by the number of trials.
- D: The interval has an upper end above zero when the sample is finite.
- E: The observed frequency is an estimate and has uncertainty.

**Source:** Zero events, confidence bound, statistic versus parameter

## MA-ch01.19

A static-analysis tool finds each instance of a vulnerability class with probability 0.6 and raises no false alarms. It reports nothing for a module. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Failing to report a real vulnerability is a false negative.
- [ ] B. Precision is the share of real instances that the tool finds.
- [ ] C. Raising no false alarms corresponds to a specificity of 0.
- [ ] D. The 0.6 chance of finding a real instance is the tool's sensitivity, also called recall.
- [ ] E. A silent report establishes that the module contains no instance.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: A false negative is a real case that the test misses.
- B: Precision is the share of reported instances that are real; the share found is recall.
- C: No false alarms corresponds to a specificity of 1.
- D: Sensitivity is the share of real instances the tool detects.
- E: With sensitivity below 1, a silent report leaves some chance that an instance is present.

**Source:** Sensitivity, specificity, false negative, precision

## MA-ch01.20

A team injects 50 small deliberate faults into its code, one at a time, and reruns its passing test suite for each. The suite detects 31 of the 50. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Injecting deliberate faults to see whether tests catch them is mutation testing.
- [ ] B. A passing suite means less when its mutation score is low.
- [ ] C. The share of injected faults detected is the suite's false positive rate.
- [ ] D. The share of injected faults that the suite detects is called the mutation score.
- [ ] E. A mutant that changes behavior on no possible input is an equivalent mutant, and it does not show a gap in the tests.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Mutation testing measures the strength of a test suite.
- B: A suite that misses many injected faults could also miss real ones.
- C: It is the mutation score, also called the kill rate.
- D: A higher score means the suite responds to more kinds of faults.
- E: No test could detect it, since the program's behavior is unchanged.

**Source:** Mutation testing, mutation score

## MA-ch01.21

A discussion compares the effort needed to produce an answer with the effort needed to check it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Solve-verify asymmetry names a gap between the effort to produce an answer and the effort to check it.
- [ ] B. For open-ended text such as summaries, verifying is cheaper than generating.
- [ ] C. Checking a proposed factorisation by multiplying is a case where verifying is cheaper than solving.
- [ ] D. When the cost of generating falls toward zero, the cost of verifying falls with it.
- [ ] E. The gap between solving and checking runs in one direction across task types.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: The gap can be large in either direction, depending on the task.
- B: Checking a summary against its source can cost as much as writing it.
- C: Some tasks are hard to solve and easy to check.
- D: Cheap generation does not make checking cheaper.
- E: The direction varies with the task.

**Source:** Solve-verify asymmetry

## MA-ch01.22

A model drafts 2,000 contract summaries a day at negligible cost, and a lawyer needs 10 minutes to check one summary against its contract. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Outputs that were not checked are unverified, not verified-correct, even if no error was reported.
- [ ] B. A random-sample audit catches each material error in the batch.
- [ ] C. Auditing a random sample estimates the error rate of the batch without checking each item.
- [ ] D. Directing more checking effort toward higher-risk items is risk-based sampling.
- [ ] E. When generation is cheap and checking is expensive, verification becomes the bottleneck.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Lack of a reported error is not evidence of correctness.
- B: A sample finds only the errors that fall inside it.
- C: Sampling trades coverage for cost while keeping an estimate of the rate.
- D: Risk-based sampling spends scarce review effort where errors cost the most.
- E: Throughput is limited by the slowest step, which here is checking.

**Source:** Verification bottleneck, sampling, unverified

## MA-ch01.23

A support team rewards agents, and its AI drafting assistant, for average handle time. Handle time falls from 11 to 7 minutes while repeat contacts about the same issue rise from 14% to 26%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reward hacking means an agent improves the true goal beyond what the metric asked.
- [ ] B. Average handle time is a proxy for service quality.
- [ ] C. The rise in repeat contacts is evidence that handle time measures resolution well.
- [ ] D. A proxy validated once still tracks the goal after the incentives change.
- [ ] E. When a measure becomes a target, it stops being a good measure; this is Goodhart's law.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Reward hacking is scoring high on the specified metric without achieving the intended goal.
- B: It stands in for quality without being quality.
- C: Rising repeats show that handle time and resolution have come apart.
- D: Incentives can change behavior and break a relationship that held before.
- E: Optimising a proxy directly breaks its link to the goal.

**Source:** Goodhart's law, proxy, reward hacking

## MA-ch01.24

Team 1 trains a model on past healthcare spending as a stand-in for medical need. Team 2's demand forecaster had low error for two years, until a new competitor changed customers' buying habits and the error began to rise. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Team 1 used a proxy label, and the proxy was not the target to begin with.
- [ ] B. Concept drift is a change in the distribution of inputs while the relation of outcome to inputs stays fixed.
- [ ] C. Team 2's rising error after the competitor appeared is concept drift, since the relation between inputs and outcome changed.
- [ ] D. Label shift is a change in the proportion of outcome classes between training and use.
- [ ] E. Retraining Team 1's model on newer data with the same proxy label closes the gap between label and need.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A proxy label is a measured stand-in for the quantity that matters.
- B: That description fits covariate shift.
- C: Concept drift is a change in how inputs relate to the outcome.
- D: It is also called prior probability shift.
- E: The same flawed label reproduces the same gap.

**Source:** Proxy label, concept drift, covariate shift, label shift

## MA-ch01.25

A delivery-time predictor was within its stated margin on 98% of 50,000 orders in a year of normal operation. The company opens a new region with a different road network. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. External validity is whether a result carries over to settings other than the one tested.
- [ ] B. Covariate shift means that the relation of the outputs to the inputs changes.
- [ ] C. Accuracy on held-out data from the same period is an in-distribution estimate.
- [ ] D. Inputs from the new region differ from the earlier inputs, which is distribution shift, specifically covariate shift if the relation of outcome to inputs holds.
- [ ] E. The 98% figure is an out-of-distribution estimate for the new region.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: The new region is a setting outside the tested one.
- B: That describes concept drift; covariate shift changes the input distribution.
- C: It describes performance on data like the data it was tested on.
- D: Covariate shift changes the input distribution while the outcome relation stays the same.
- E: It was measured on the old region and does not describe the new one.

**Source:** Covariate shift, in-distribution versus out-of-distribution, external validity

## MA-ch01.26

A pneumonia classifier is trained and tested on pooled images from two hospitals with very different pneumonia rates, and each image carries a visible scanner tag that identifies its hospital. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The hospital is a confounder, since it is linked to both the tag and the pneumonia rate.
- [ ] B. Pooling the data from two hospitals does not remove the confounding.
- [ ] C. High accuracy on the pooled test set shows that the model generalises to a third hospital.
- [ ] D. A spurious correlation is a link in the training data, here between tag and label, that does not reflect the disease.
- [ ] E. A model that relies on the hospital tag as a cue instead of the lung image is shortcut learning.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: A confounder is related to both the cue and the outcome.
- B: The hospital remains linked to both the tag and the label.
- C: The pooled test set shares the same shortcut, so it does not show generalisation.
- D: The association comes from how the data were pooled.
- E: Shortcut learning means using an easy cue that happens to predict the label.

**Source:** Spurious correlation, shortcut learning, confounder

## MA-ch01.27

A pipeline lets an AI reviewer approve routine configuration changes proposed by an AI agent, and the record reads "Approved by ReviewBot." One approved change causes an outage. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Responsibility transfers to the AI model because it performed the review.
- [ ] B. Rubber-stamping is a meaningful review carried out at speed.
- [ ] C. An approval attributed to a software component assigns accountability.
- [ ] D. An audit trail records who decided what and when.
- [ ] E. Accountability needs a person who accepted the risk, can explain the decision, and had the authority to make it.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: A software component cannot be held answerable, so responsibility stays with the people who deployed it.
- B: Rubber-stamping is approval given without real examination.
- C: Accountability needs an identifiable person who can answer for the decision.
- D: An audit trail supports later review even though it does not prevent errors.
- E: Without such a person nobody answers for the outcome.

**Source:** Accountability, audit trail, rubber-stamping

## MA-ch01.28

Reviewers approve 4,850 of 5,000 AI recommendations, at a median of 4 seconds each. An independent audit finds that 400 of the 5,000 were wrong. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The approval rate measures how many of the recommendations were correct.
- [ ] B. Automation bias is the tendency to over-rely on suggestions from an automated system.
- [ ] C. A human-in-the-loop step is meaningful when the person has the time, the information and the authority to reject.
- [ ] D. Rejecting 150 items when 400 were wrong means the reviewers' sensitivity to errors was below 100%.
- [ ] E. Approvals given without examination are called rubber-stamping.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The approval rate describes reviewers' decisions, which the audit shows can differ from correctness.
- B: It can lead reviewers to approve without examining.
- C: A reviewer lacking any of these cannot provide a real check.
- D: At most 150 of the 400 wrong items could have been caught.
- E: A very high approval rate with very short review times is consistent with it.

**Source:** Automation bias, human-in-the-loop, sensitivity

## MA-ch01.29

A test report reads: "Tested 40 of 40 sample invoices: all processed correctly. Not tested: handwritten scans, invoices in languages other than English, behavior under production load." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The scope of a claim is the set of conditions under which it was tested.
- [ ] B. The 40 correct invoices support the claim that the system handles handwritten scans.
- [ ] C. A sample of 40 clean invoices is representative of behavior under production load.
- [ ] D. Absence of a failure in untested conditions counts as a pass.
- [ ] E. Conditions that were not tested should be labelled unverified.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: The claim extends only as far as the conditions that were exercised.
- B: Handwritten scans are outside the scope that was tested.
- C: The sample differs in kind from the load conditions it is meant to stand for.
- D: No test was run there, so there is no result either way.
- E: Unverified means unknown, which differs from tested and passed.

**Source:** Scope of a claim, unverified status

## MA-ch01.30

A vendor reports 91% accuracy for its model on a benchmark. Eight training runs that differ only in random seed scored between 83% and 91%, and the vendor reported the best run, picked by looking at test accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Reporting the best of several runs, chosen using the test score, is cherry-picking.
- [ ] B. Reporting the mean and spread across seeds, with selection done on a validation set, is p-hacking.
- [ ] C. The spread of results across random seeds is called bias.
- [ ] D. The best of eight runs is an upward-biased estimate of the expected accuracy of a fresh run, an effect called the winner's curse.
- [ ] E. Choosing a run by test accuracy uses the test set for model selection, which is a form of leakage.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The reported number is selected for being high.
- B: That reporting separates selection from testing and shows the variability.
- C: The spread across seeds is variance.
- D: Selecting the maximum of noisy results overstates the typical result.
- E: The test set no longer gives an unbiased estimate once it guides choices.

**Source:** Cherry-picking, leakage, variance across seeds

## MA-ch01.31

A deployment team wants its skeptical checks to happen reliably instead of depending on whether one engineer remembers to be careful. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A checklist item phrased as a yes-or-no question makes a general worry something that can be inspected.
- [ ] B. Setting a threshold in a monitoring alert before launch applies the criterion without relying on memory.
- [ ] C. A named person with authority to hold a release gives a failed check consequences.
- [ ] D. Once a check is written into the process, the check does not need review.
- [ ] E. A check is a gate when its failure can halt or delay a release.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A specific question can be assigned, answered and audited.
- B: A pre-set alert runs whether or not anyone is thinking about it.
- C: Authority to act is what makes the check effective.
- D: Checks drift away from the real risk as the system and its use change.
- E: A check that cannot stop anything only records a problem.

**Source:** Checks as team practice, gate

## MA-ch01.32

A data scientist trains several variants, looks at validation results, and then writes a plausible explanation of why one variant won. A colleague writes a prediction and a decision rule before running the same comparison. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing many variants on the validation set and picking the best leaves the validation estimate unbiased.
- [ ] B. A decision rule fixed before the comparison keeps the analyst from choosing the criterion after seeing results.
- [ ] C. An explanation written after seeing results is post hoc, since it can be fitted to whatever the data showed.
- [ ] D. HARKing means forming the hypothesis before the results are known.
- [ ] E. A prediction written before the run is weaker evidence because the data had not been seen.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Repeated selection on the validation set makes its estimate optimistic, a form of overfitting to it.
- B: The rule is set without knowledge of the outcome.
- C: Post hoc accounts are easy to produce for any outcome.
- D: HARKing is hypothesizing after the results are known.
- E: A prediction that could have failed is stronger evidence when it succeeds.

**Source:** Post hoc explanation, HARKing, decision rule

## MA-ch01.33

A credit-risk model has been accurate for two years, and the team is designing post-deployment monitoring. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Past accuracy is inductive evidence and does not guarantee future accuracy when conditions change.
- [ ] B. Data drift monitoring compares the distribution of live inputs with the distribution of the training inputs.
- [ ] C. Concept drift can be detected from the input distribution alone.
- [ ] D. A drift alert tells the team the cause of a drop in performance.
- [ ] E. Monitoring performance needs ground-truth outcomes, which often arrive late; this is label delay.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Conditions that held in the past can stop holding, which is nonstationarity.
- B: It flags changes in the inputs before outcomes are known.
- C: Concept drift is a change in the relation of outcome to inputs, which inputs alone can miss.
- D: An alert signals that something changed, not why.
- E: Loan defaults appear long after the decision.

**Source:** Data drift, concept drift, label delay, nonstationarity

## MA-ch01.34

People relabel a random sample of 50 answers from a model judge. In the sample the judge passed 45 answers and the humans passed 38; the judge failed 5 answers, of which 4 the humans also failed. The team wants terms for how well the judge matches the humans. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The share of judge-pass answers that humans also pass is the judge's recall.
- [ ] B. A judge that passes answers humans fail is lenient, producing false passes.
- [ ] C. Agreement between two raters corrected for chance agreement is measured by Cohen's kappa.
- [ ] D. Raw percent agreement already adjusts for chance agreement.
- [ ] E. The share of answers that humans fail and the judge also fails is the judge's sensitivity, or recall, for failures.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: That share is the precision of the judge's pass verdicts.
- B: A false pass is a judge pass where the reference says fail.
- C: Kappa discounts the agreement expected from chance.
- D: Raw agreement ignores chance, which is why kappa is used.
- E: Sensitivity for a target class is the share of true members of that class that are detected.

**Source:** Judge agreement, recall, precision, Cohen's kappa

## MA-ch01.35

A vendor claims its meeting-summary assistant "saves managers time", and an evaluator turns this into a measurable test. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. "Saves time" is already an operational definition.
- [ ] B. A control group is the group that receives the tool.
- [ ] C. Operationalising a claim means choosing a measurable quantity that stands for it, such as minutes spent on meeting follow-up.
- [ ] D. Counting how many managers say they like the tool measures time saved.
- [ ] E. A baseline is the number reported after the tool has been introduced.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: It names no measurable quantity or unit.
- B: A control group is the comparison group that does not receive the tool.
- C: An operational definition makes a vague term measurable.
- D: A satisfaction rating measures a different construct than minutes saved.
- E: A baseline is a measurement taken before the change, or in a comparison group without it.

**Source:** Operational definition, baseline, control group

## MA-ch01.36

An AI reviewer scans 400 pull requests for security flaws, reports none, and a manager concludes that the code base is secure. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Seeding known flaws and counting how many the reviewer flags estimates its sensitivity, or recall.
- [ ] B. Reporting no findings establishes that the code is secure.
- [ ] C. A reviewer with high specificity has high sensitivity as a result.
- [ ] D. A true negative is a flaw that the reviewer missed.
- [ ] E. The prevalence of flaws is a property of the reviewer.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: Seeded flaws give the denominator needed to measure detection.
- B: No findings is consistent with a reviewer that misses flaws.
- C: Specificity and sensitivity are separate properties.
- D: A missed flaw is a false negative; a true negative is a clean item correctly passed.
- E: Prevalence is a property of the code being reviewed.

**Source:** Negative finding, sensitivity, false negative, prevalence

## MA-ch01.37

A company plans for an AI agent to prepare production price changes, with one Approve button for a person beside the agent's own summary of the change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Approval by a person with no ability to reject the change is meaningful oversight.
- [ ] B. A named approver whose identity is recorded makes the decision attributable to a person.
- [ ] C. Segregation of duties means that the same agent proposes and approves a change.
- [ ] D. Showing the agent's own summary alone has the approver review the agent's account instead of the change itself.
- [ ] E. Showing the actual difference and its expected impact lets the approver judge the change on independent evidence.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Oversight needs the practical ability to stop the action.
- B: Attribution to a person is a precondition of accountability.
- C: Segregation of duties means that different parties propose and approve.
- D: The summary is a report, and the diff of the change is the observation.
- E: Independent evidence is what makes the approval a check.

**Source:** Approval design, segregation of duties, accountability

## MA-ch01.38

A reviewer picks words for three requests to an analyst: confirm the build matches its specification, confirm the system serves the real need, and look for a result that would refute the claim. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Falsification means collecting more cases that agree with the claim.
- [ ] B. Verification asks whether the system was built to its specification.
- [ ] C. Validation asks whether the system meets the real need it was built for.
- [ ] D. Verification and validation are interchangeable words for this purpose.
- [ ] E. A test designed to falsify looks for cases expected to agree with the claim.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Falsification seeks an observation that would contradict the claim.
- B: Verification compares the artifact with its specification.
- C: A system can pass verification and still fail validation.
- D: They answer different questions: built right versus right thing built.
- E: A falsifying test targets cases where the claim could fail.

**Source:** Verification, validation, falsification
