# INFO 7375 Computational Skepticism for AI: prompting practice exam: KEY

Total 100 points. Statement key: T = true (check it), F = false (leave it blank).

---

**1.** A user prompts an AI: "Tell me how good the churn model is." Choose the rewrites that give a model what it needs to act. Check each statement that is true.  *(5 points)*

- [ ] A. State the comparison, such as a majority-class baseline, so 'good' means better than something named.
- [ ] B. Ask for an overall quality score between 0 and 100.
- [ ] C. Say which data the numbers must come from, such as a held-out set the model was never tuned on.
- [ ] D. Name the metric, such as AUC for ranking and a calibration measure for the probabilities, and ask for them separately.
- [ ] E. Ask the model to report which numbers it computed and which it assumed.

**Key:** A=T B=F C=T D=T E=T  |  `DR-P.01`  |  *prompting*  |  source: Make a vague request exact

- A (true): 'Good' is relative to a baseline.
- B (false): An undefined score cannot be reproduced or compared.
- C (true): A number without its data is not checkable.
- D (true): A named quantity can be computed and checked.
- E (true): Separating computed from assumed shows what can be checked.

**2.** A student writes one prompt asking an AI to build a Bayes calculation, a base-rate inventory and a calibration plan. Choose the practices that make the result easier to trust. Check each statement that is true.  *(5 points)*

- [ ] A. State what a finished answer contains, such as the calculation, the sources and the assumptions.
- [ ] B. Put the tasks in a random order, because order cannot affect the result.
- [ ] C. Make the prompt as long as possible, since length makes the model more careful.
- [ ] D. Give each task its own labelled deliverable so each can be checked separately.
- [ ] E. Ask for two scenarios, such as a typical case and an edge case, so the answer shows how the result changes.

**Key:** A=T B=F C=F D=T E=T  |  `DR-P.07`  |  *prompting*  |  source: Split a compound task

- A (true): A defined deliverable lets the reader see what is missing.
- B (false): Later tasks often depend on earlier ones, such as a prior used in a calculation.
- C (false): Length does not add care; unclear instructions stay unclear.
- D (true): Separate outputs can fail separately and be reviewed separately.
- E (true): Scenarios show sensitivity to the inputs.

**3.** A student wants to be able to check an AI's answer to a calculation question. Choose the prompt instructions that help. Check each statement that is true.  *(5 points)*

- [ ] A. A fluent explanation alone is not evidence that the answer is right.
- [ ] B. Ask for code and run it, then compare the output with the claimed answer.
- [ ] C. Ask for only the final number, to keep the answer short.
- [ ] D. Ask the model to state the assumptions the answer depends on.
- [ ] E. Ask the model to show each step of the calculation.

**Key:** A=T B=T C=F D=T E=T  |  `DR-P.05`  |  *prompting*  |  source: Ask for work that can be verified

- A (true): Fluency and correctness are separate.
- B (true): Running the code is a check the model's text cannot fake.
- C (false): A bare number cannot be inspected.
- D (true): Hidden assumptions are where wrong answers hide.
- E (true): A visible chain can be rechecked.

**4.** A student asks an AI whether an agent's 'task complete' message can be trusted. Choose the prompt instructions that make the answer usable. Check each statement that is true.  *(5 points)*

- [ ] A. Ask for two scenarios, a typical task and an edge case, and compare the posteriors.
- [ ] B. State that the base rate is an estimate, name its source, and do not choose it to reassure.
- [ ] C. Ask the model to name the false positive rate of the agent's reports as a separate input.
- [ ] D. Ask for a prior, the likelihoods and the posterior, with the arithmetic shown.
- [ ] E. Ask for the answer as 'trustworthy' or 'not trustworthy' with no numbers.

**Key:** A=T B=T C=T D=T E=F  |  `DR-P.19`  |  *prompting*  |  source: Show the evidence behind a probability

- A (true): The prior differs by task, so the posterior does.
- B (true): An honest prior is stated with its basis.
- C (true): It is the number that controls how much a report is worth.
- D (true): Bayes' theorem turns a report into a probability of completion.
- E (false): A bare label hides the inputs.

**5.** A student prompts an AI to help evaluate a model and writes: "Tune the settings until the test score is as high as possible, then report it." Choose the better versions. Check each statement that is true.  *(5 points)*

- [ ] A. Report the test score once, after tuning is finished.
- [ ] B. Tune on a validation set and keep the test set untouched until the end.
- [ ] C. Check for leakage with a named test, not by how the data look.
- [ ] D. Tune on the test set but report the score as the true accuracy.
- [ ] E. Say that a drop on new data later would be expected, so monitoring is planned.

**Key:** A=T B=T C=T D=F E=T  |  `DR-P.16`  |  *prompting*  |  source: Keep the test set untouched

- A (true): Repeated peeking inflates the reported score.
- B (true): Tuning on the test set uses up its value as a fair check.
- C (true): Looking fine is not a check.
- D (false): The score is optimistic because the settings were chosen to fit that set.
- E (true): Performance on new data can differ from the held-out estimate.

**6.** A student asks an AI for a base rate of an agent's failures, and no published evaluation exists. Choose the prompt instructions that are sound. Check each statement that is true.  *(5 points)*

- [ ] A. Ask the model to label each figure as sourced or assumed.
- [ ] B. Tell the model to give a single confident number even if it must estimate.
- [ ] C. Treat a figure with a citation as verified.
- [ ] D. Tell the model to say so when no source exists, and name what evaluation would be needed to find out.
- [ ] E. Ask the model to cite a source for each figure and accept the citations as verification.

**Key:** A=T B=F C=F D=T E=F  |  `DR-P.03`  |  *prompting*  |  source: State what is missing instead of guessing

- A (true): It lets the reader weigh each number.
- B (false): That invites an invented figure.
- C (false): Models can produce citations to sources that do not say that, or do not exist.
- D (true): Missing data is a result, not a gap to fill.
- E (false): A citation is a claim until the source is opened and read.

**7.** A user prompts an AI: "The fraud model got worse because the world changed." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Ask for performance on a time-ordered split rather than a random split.
- [ ] B. Name the date from which the data differ, and the metric that fell.
- [ ] C. Report training-set accuracy to show the model is robust.
- [ ] D. Call a change in class proportions covariate shift.
- [ ] E. Say whether the inputs changed or the relationship between inputs and outcome changed.

**Key:** A=T B=T C=F D=F E=T  |  `DR-P.18`  |  *prompting*  |  source: Ask for the shift to be named

- A (true): A random split hides change over time.
- B (true): A named metric and date turn the complaint into a test.
- C (false): Training accuracy says nothing about new data.
- D (false): A change in class proportions is label shift.
- E (true): Covariate shift and concept drift need different fixes.

**8.** A student asks an AI for a one-page appendix summarizing an analysis and wants it to be honest about its limits. Check each statement that is true.  *(5 points)*

- [ ] A. Ask the model to list what it could not determine and why.
- [ ] B. Ask the model to leave out anything it is unsure about, so the page looks clean.
- [ ] C. Leave the labels out to keep the page short.
- [ ] D. Specify what the appendix must contain, such as the calculation, the sources and the assumptions.
- [ ] E. Ask the model to write in a confident tone so the reader trusts it.

**Key:** A=T B=F C=F D=T E=F  |  `DR-P.20`  |  *prompting*  |  source: Prompt that asks for a deliverable with limits

- A (true): Naming gaps is part of an honest report.
- B (false): Dropping uncertainty hides it.
- C (false): Labels are what show which claims rest on what.
- D (true): A defined structure shows what is missing.
- E (false): Tone is not evidence.

**9.** A student reruns a prompt after adding a constraint and wants to know whether the answer improved. Check each statement that is true.  *(5 points)*

- [ ] A. Change one thing at a time so a change in the answer can be attributed to the change in the prompt.
- [ ] B. Check the new answer against an outside source, not only against the old answer.
- [ ] C. Run each version once and treat any difference as an effect of the change.
- [ ] D. Define 'better' only after seeing the new answers.
- [ ] E. A more fluent answer is a better answer.

**Key:** A=T B=T C=F D=F E=F  |  `DR-P.09`  |  *prompting*  |  source: Improve a prompt by one change at a time

- A (true): Changing several things together hides which one mattered.
- B (true): Two model answers can agree and both be wrong.
- C (false): Model output varies from run to run; one comparison can be chance.
- D (false): A criterion chosen after the results can be fitted to them.
- E (false): Fluency is not accuracy.

**10.** A user prompts an AI: "What is the chance an email is spam if the filter flags it?" The user has the filter's sensitivity, false positive rate and the share of mail that is spam. Check each statement that is true.  *(5 points)*

- [ ] A. The prompt should ask for P(spam | flagged), the positive predictive value.
- [ ] B. The prompt should supply the share of mail that is spam, because the answer depends on it.
- [ ] C. The prompt should ask the model to show the arithmetic so the user can check it.
- [ ] D. Giving only the filter's sensitivity is enough to compute the answer.
- [ ] E. Asking for 'the accuracy' of the filter answers the question.

**Key:** A=T B=T C=T D=F E=F  |  `DR-P.02`  |  *prompting*  |  source: Specify the conditional's direction

- A (true): That is the reverse conditional the question needs.
- B (true): The base rate changes the posterior.
- C (true): A shown calculation can be verified step by step.
- D (false): Sensitivity is P(flagged | spam); it is the wrong direction and ignores the base rate.
- E (false): Accuracy mixes both classes and hides the base rate.

**11.** A user prompts an AI: "Give me a number for the average delivery time and how sure you are." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. State what the data are, such as the sample, the period and how deliveries were chosen.
- [ ] B. Ask for an interval around the estimate, not only a point estimate.
- [ ] C. Ask for the model's feeling of certainty as the measure of how sure it is.
- [ ] D. Say whether a confidence interval or a credible interval is wanted, and give the prior if it is the latter.
- [ ] E. A 95% confidence level describes how often the procedure captures the mean over repeated samples.

**Key:** A=T B=T C=F D=T E=T  |  `DR-P.13`  |  *prompting*  |  source: Ask for an interval and say which kind

- A (true): The interval is only as good as the data behind it.
- B (true): An interval shows how uncertain the estimate is.
- C (false): A model's stated certainty is not a statistical interval.
- D (true): They are different statements and need different inputs.
- E (true): It is a statement about the procedure, not about one computed interval.

**12.** A student asks an AI for a short biography of a historical figure and then looks the person up in an encyclopedia. Check each statement that is true.  *(5 points)*

- [ ] A. Comparing the answer with the encyclopedia shows what the model got right, got wrong or left out.
- [ ] B. A named source should be opened and read, not accepted on the model's say-so.
- [ ] C. The encyclopedia is itself a source with its own limits, so a disagreement is something to investigate.
- [ ] D. If the model's answer is detailed, there is no need to look anything up.
- [ ] E. Noting what was omitted is part of the check, not only what was wrong.

**Key:** A=T B=T C=T D=F E=T  |  `DR-P.10`  |  *prompting*  |  source: Verify the model's answer against an outside source

- A (true): The outside source is the check.
- B (true): A model can name a source that does not say what it claims.
- C (true): Neither source is automatically right.
- D (false): Detail is not evidence of accuracy.
- E (true): A short answer can mislead by what it leaves out.

**13.** A user prompts an AI: "Is a Brier score of 0.18 good?" Choose the rewrites that give the AI what it needs. Check each statement that is true.  *(5 points)*

- [ ] A. Name the reference forecast, such as always predicting the base rate, so the score is compared with something.
- [ ] B. Leave the base rate out, because the score does not depend on it.
- [ ] C. Ask whether 0.18 is above a standard cut-off that applies to all problems.
- [ ] D. Ask the model to call the score good if it feels low.
- [ ] E. Ask for the Brier skill score relative to that reference.

**Key:** A=T B=F C=F D=F E=T  |  `DR-P.17`  |  *prompting*  |  source: Name the baseline

- A (true): A score has no meaning without a reference.
- B (false): The reference forecast and the score depend on the base rate.
- C (false): No cut-off applies everywhere; it depends on the base rate.
- D (false): Judging by feel replaces the comparison.
- E (true): It states the improvement over the reference.

**14.** A user prompts an AI: "I think the hiring model is biased." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Ask the model to confirm that bias exists.
- [ ] B. Report overall accuracy to show the groups were treated equally.
- [ ] C. Ask for the selection rate for each group and the ratio between them.
- [ ] D. Treat unequal selection rates alone as proof of disparate treatment.
- [ ] E. Name the protected attribute and the groups to compare.

**Key:** A=F B=F C=T D=F E=T  |  `DR-P.06`  |  *prompting*  |  source: Rewrite a bias complaint into a testable request

- A (false): A request for confirmation invites agreement.
- B (false): Overall accuracy can hide large gaps between groups.
- C (true): That is a measurable disparate impact check.
- D (false): Unequal outcomes show disparate impact at most; disparate treatment is about using the attribute.
- E (true): A comparison needs named groups.

**15.** A course asks students to write a prediction in a journal before running an AI prompt, and to say why. Check each statement that is true.  *(5 points)*

- [ ] A. The prediction may be edited after the run to match what happened.
- [ ] B. Logging it in a dated journal makes the comparison honest.
- [ ] C. A prediction is still useful when the model is usually right, because it tests the student's own expectations.
- [ ] D. Writing the prediction first lets the student compare it with the result without hindsight.
- [ ] E. Including the reason makes it possible to see which belief was wrong when the prediction fails.

**Key:** A=F B=T C=T D=T E=T  |  `DR-P.08`  |  *prompting*  |  source: Predict before you run

- A (false): That removes its value as a test.
- B (true): A record is needed to check against.
- C (true): Prediction and check reveal how well calibrated the student is.
- D (true): A logged prediction cannot be quietly rewritten after seeing the output.
- E (true): The reason is the part that can be corrected.

**16.** A manager prompts an agent: "Look at the dataset and fix any problems." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Ask for counts of rows before and after each step.
- [ ] B. Choose a missing-data treatment before finding out how the values went missing.
- [ ] C. Tell the agent to delete any row with a missing value.
- [ ] D. Tell the agent to replace missing values with the column mean and report that the data are now clean.
- [ ] E. List the checks, such as duplicates, schema and type checks, and plausible value ranges.

**Key:** A=T B=F C=F D=F E=T  |  `DR-P.15`  |  *prompting*  |  source: Rewrite a data-check request

- A (true): Row counts expose silent data loss.
- B (false): The right treatment depends on the mechanism.
- C (false): Deleting rows can bias the data if the missingness is not random.
- D (false): Mean imputation understates uncertainty and 'clean' is not a check.
- E (true): Named checks can be run and reported.

**17.** A manager writes a prompt that delegates a task to an AI agent with access to company files. Choose the instructions that follow good practice. Check each statement that is true.  *(5 points)*

- [ ] A. Give a stop condition and tell the agent to ask before any step it cannot undo.
- [ ] B. Ask the agent to report what it did, and check that against logs or the files themselves.
- [ ] C. Treat a 'task complete' report as proof the task is complete.
- [ ] D. State what the agent may not do, such as deleting files or sending messages.
- [ ] E. Tell the agent to use its judgment on anything unclear.

**Key:** A=T B=T C=F D=T E=F  |  `DR-P.14`  |  *prompting*  |  source: Delegate to an agent with limits and a check

- A (true): A human check on irreversible actions needs to be real.
- B (true): A report is a claim; the environment is the evidence.
- C (false): Self-reports can be wrong, sometimes confidently.
- D (true): Limits go in the prompt and in the permissions.
- E (false): Unclear cases are where a stop or a question belongs.

**18.** A team uses an AI to grade the answers of another AI. Choose the statements about the prompt and the setup that are sound. Check each statement that is true.  *(5 points)*

- [ ] A. Ask for claims that can be checked, such as numbers and quotations, and check a sample.
- [ ] B. A model's stated confidence is a good substitute for ground truth.
- [ ] C. Ground truth should be observable independently of the model's report.
- [ ] D. Asking the same model 'are you sure?' is an independent check on its answer.
- [ ] E. A judge model can prefer its own style of answer, so its grades need checking against humans or a key.

**Key:** A=T B=F C=T D=F E=T  |  `DR-P.04`  |  *prompting*  |  source: Ground truth outside the model

- A (true): Checkable output can be audited.
- B (false): Confidence can be wrong; calibration is measured against outcomes.
- C (true): Otherwise the check inherits the model's mistakes.
- D (false): It is a second sample from the same source of error.
- E (true): Self-preference is a known bias of model judges.

**19.** A user has a claim that a new fraud model 'works well' and prompts an AI to test it. Choose the prompt instructions that follow a skeptic's method. Check each statement that is true.  *(5 points)*

- [ ] A. Ask for rival explanations of any good results, such as leakage or an easy test set.
- [ ] B. Ask where the claim stops applying, such as other regions or later dates.
- [ ] C. Ask what result would show the claim is wrong.
- [ ] D. Ask the model to agree with the claim and explain why.
- [ ] E. Ask the model to find evidence that the model works.

**Key:** A=T B=T C=T D=F E=F  |  `DR-P.11`  |  *prompting*  |  source: Ask for the falsifier

- A (true): Rivals show what else could produce the same evidence.
- B (true): Scope limits a claim to what the evidence covers.
- C (true): A claim that nothing could contradict is not testable.
- D (false): That prompts a justification, not a test.
- E (false): Asking only for support builds in confirmation.

**20.** A manager prompts an AI: "Make sure the loan model is fair to all groups." Choose the rewrites that use exact terms. Check each statement that is true.  *(5 points)*

- [ ] A. Call unequal outcome rates 'disparate treatment'.
- [ ] B. Name the fairness criterion to be checked, such as equal true positive rates across groups.
- [ ] C. Report calibration within each group, so a given score means the same thing for each.
- [ ] D. Report overall accuracy to show equal treatment of groups.
- [ ] E. Assume every fairness criterion can be met at once, whatever the base rates.

**Key:** A=F B=T C=T D=F E=F  |  `DR-P.12`  |  *prompting*  |  source: Rewrite a fairness request with exact terms

- A (false): Disparate treatment is about using the protected attribute; unequal outcomes from a neutral practice are disparate impact.
- B (true): 'Fair' means different measurable things; the prompt must pick one.
- C (true): Calibration by group is a named check.
- D (false): Overall accuracy can hide group gaps.
- E (false): With different base rates several criteria cannot all hold together.
