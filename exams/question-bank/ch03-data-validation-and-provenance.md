# Chapter 3: Data validation and the epistemic frame of a dataset

## MA-ch03.1

An analyst receives an export of the insurance claims paid to one hospital system, about 6 million rows, and plans to use it to estimate how common a chronic condition is among adults in the surrounding city. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The city's adults are the target population, and the people who appear in the claims export are the frame actually available for study.
- [ ] B. Administrative data come from a designed probability sample, so coverage of the city is known in advance.
- [ ] C. Residents who are uninsured or who use other hospital systems are an undercoverage problem for this estimate.
- [ ] D. With 6 million rows, undercoverage is removed because sampling error becomes negligible.
- [ ] E. A diagnosis code recorded for billing is a proxy for the clinical condition, not a direct measurement of it.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The target population is the group the claim is about, and the frame is the list or file from which people are actually observed.
- B: Administrative data are collected to run a system such as billing, so who appears follows that purpose rather than a sampling design.
- C: Undercoverage means part of the target population has no chance of appearing in the frame.
- D: A large size shrinks random error but leaves the systematic gap between the frame and the target population.
- E: A proxy is a recorded variable that stands in for the concept of interest, and a billing code reflects billing practice.

**Source:** Target population, frame and proxy in administrative data

## MA-ch03.2

A team inner-joins a table of support tickets to a customer table on customer_id. Tickets from one region carry a legacy identifier format, so a large share of them find no match and vanish from the result, while other regions lose few rows. A missing-value report on the joined table shows zero blanks. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Tickets dropped by an inner join appear as blank cells, so a missing-value report flags them.
- [ ] B. Comparing the row count before and after the join, ideally within each region, is row reconciliation.
- [ ] C. A small overall loss rate shows that the dropped rows are spread evenly across regions.
- [ ] D. A left join would keep the unmatched tickets and show blanks in the customer columns.
- [ ] E. Losing rows to a legacy identifier format is an example of random measurement error in the remaining cells.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Rows removed by an inner join are absent rather than blank, so a cell-level report has nothing to flag.
- B: Row reconciliation compares counts at each step against what was expected, and a per-group version shows where rows were lost.
- C: An overall rate can mask a severe loss in a subgroup, which is a form of differential loss.
- D: A left join preserves every row of the left table and fills the right-hand columns with blanks when no match exists.
- E: Dropping whole rows is a coverage problem; measurement error concerns inaccurate values in rows that remain.

**Source:** Row reconciliation and silent loss in joins

## MA-ch03.3

An orders table is joined to a customers table on customer_id. One customer_id appears twice in the customers table because of a data-entry duplicate. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Asserting that the key is unique in the customers table before joining detects the duplicate key.
- [ ] B. A left join returns the matched rows from both tables and drops the unmatched rows of the left table.
- [ ] C. A duplicate key on the right side of a left join can multiply rows, so the output has more rows than the left table, an effect often called fan-out.
- [ ] D. An inner join keeps unmatched rows from the left table and fills the right-hand columns with blanks.
- [ ] E. A full outer join keeps just the keys that are present in both tables.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A uniqueness check, which tests a candidate key constraint, flags duplicates before they inflate the output.
- B: That describes an inner join; a left join keeps the unmatched rows of the left table.
- C: Fan-out is the multiplication of rows that occurs when one left key matches several right rows.
- D: That describes a left join; an inner join drops rows without a match.
- E: A full outer join keeps keys from either table and fills blanks where one side is missing.

**Source:** Join types, uniqueness and fan-out

## MA-ch03.4

A satisfaction survey appears as a pop-up inside a mobile app after a purchase, and the form cannot be submitted unless the questions are answered. The resulting file has 12,000 responses and no empty cells. The company wants to describe the satisfaction of its whole customer base, which includes web-only customers and people who abandoned a purchase. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Having no empty cells shows that the sample covers the whole customer base.
- [ ] B. Customers who use the website and not the app, so did not see the pop-up are a coverage gap, since they had no chance to respond.
- [ ] C. Respondents who answer some questions and skip others are an example of unit nonresponse.
- [ ] D. Customers who saw the pop-up but chose not to submit are unit nonresponse, which biases the average when the choice relates to satisfaction.
- [ ] E. Making the questions mandatory removes selection bias.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Completeness of recorded cells is a different property from coverage of the intended population.
- B: Coverage error arises when part of the target population is missing from the frame.
- C: Skipping some questions is item nonresponse; unit nonresponse is a sampled person who gives no response at all.
- D: Nonresponse that depends on the outcome produces nonresponse bias in the observed average.
- E: Mandatory fields control item nonresponse, not who sees the form or who submits it.

**Source:** Coverage, unit and item nonresponse

## MA-ch03.5

A researcher draws a random sample from a phone directory that lists 20% of the under-30 adults in a city and 80% of the older adults, and everyone sampled responds. The researcher wants to describe average transit-app use among all adults in the city. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A random draw from the directory is a probability sample of the city's adults.
- [ ] B. Enlarging the sample from the same directory shrinks the coverage bias toward zero.
- [ ] C. Post-stratification weights correct the age mix to the extent that listed and unlisted people in the same age group have similar outcomes.
- [ ] D. Undercoverage is another name for sampling error.
- [ ] E. Random selection within a frame makes the sample mean unbiased for the whole city population.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Random draws from a frame give a probability sample of the frame's population, which here differs from the city's adults.
- B: More draws from the same frame reduce random error but converge to the frame's own mean.
- C: Post-stratification adjusts the group mix, and it works only to the extent that missing people resemble listed people within each group.
- D: Undercoverage is a systematic gap between frame and target population; sampling error is random variation between samples.
- E: Unbiasedness holds for the frame's population, not for a target population that the frame misses unevenly.

**Source:** Sampling frame, undercoverage and post-stratification

## MA-ch03.6

A database lists the annualized returns of investment funds that are still operating today. Funds that closed over the past decade, which on average performed poorly, are absent from it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Studying just the funds that still exist is an example of survivorship bias.
- [ ] B. Using the median of the survivors instead of the mean removes survivorship bias.
- [ ] C. Survivorship bias is selection on the outcome, because closure is related to the returns being studied.
- [ ] D. A missing-value check on the survivor file shows the closed funds as blank rows.
- [ ] E. Survivorship bias has the same size whether or not closure is related to returns.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Survivorship bias is the distortion from analyzing only the units that persisted.
- B: A median of the filtered group is still computed on survivors and still excludes the poor performers.
- C: Selection that depends on the outcome makes the absent units a non-random subset.
- D: Closed funds are absent rows, not rows with blanks, so cell-level checks cannot see them.
- E: If closure were unrelated to returns, the survivors would be a random subset and the bias would not arise.

**Source:** Survivorship bias

## MA-ch03.7

In a city, diseases A and B are independent of each other. A hospital admits people who have A or B (or both) and a small share of people who have neither. An analyst studies how A and B are related using only the hospital's admission records and finds a negative association. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Admission is a confounder of diseases A and B.
- [ ] B. Admission is a collider, a common effect of A and B.
- [ ] C. Analyzing just the admitted patients conditions on the collider and can create a spurious association, an example of Berkson's paradox.
- [ ] D. Adjusting for age and sex in a regression on the admission records removes the artifact.
- [ ] E. In the full population the association is absent, so the pattern in the admission records is an artifact of how patients enter the data.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: A confounder is a common cause of two variables; admission is caused by them, not a cause of them.
- B: A collider is a variable influenced by two or more other variables.
- C: Conditioning on a collider opens a non-causal path between its causes, which is the mechanism of Berkson's paradox.
- D: Unrelated covariates do not undo the selection, which depends on A and B themselves.
- E: A spurious association is one that appears in the analyzed data but not in the population it is meant to describe.

**Source:** Collider bias and Berkson's paradox

## MA-ch03.8

A lender approved applicants with a fixed rule on a legacy score, and repayment outcomes exist only for approved applicants. The lender plans to train a model on the approved loans and use it to score all future applicants. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Having outcomes for just the approved applicants is called the selective labels problem.
- [ ] B. Because a fixed rule rejected applicants, the missing outcomes are MCAR.
- [ ] C. Accuracy measured on the approved loans is an unbiased estimate of accuracy across the full applicant pool.
- [ ] D. Reject inference means dropping the rejected applicants from the data.
- [ ] E. Predicting in a score range that the old rule rejected is extrapolation beyond the range covered by the training data.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Selective labels describes outcomes that are observed only for cases that a prior decision rule let through.
- B: Missingness depends on the legacy score, which is related to risk, so it is not missing completely at random.
- C: Evaluation on a selected subset describes that subset, and the rejected region is untested.
- D: Reject inference is the set of methods that estimate outcomes for rejected applicants using stated assumptions.
- E: Extrapolation is prediction outside the region where the model saw data, so its behavior there is an assumption.

**Source:** Selective labels, reject inference and extrapolation

## MA-ch03.9

A dataset has blank values in several columns. The standard missingness mechanisms are MCAR (missing completely at random), MAR (missing at random, given the observed data) and MNAR (missing not at random). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Younger respondents skipping an income question more often, with skipping unrelated to income within age groups, is MAR.
- [ ] B. High earners skipping an income question because of how much they earn is MAR.
- [ ] C. Sensor readings lost at random moments, unrelated to the quantity measured, are MCAR.
- [ ] D. Tests on the observed data can confirm that missingness is MAR rather than MNAR given enough rows.
- [ ] E. A patient skipping a final visit because the measured condition has worsened is MNAR.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: When missingness depends on an observed variable such as age, and on nothing further, the mechanism is MAR.
- B: Missingness driven by the unobserved value itself is MNAR.
- C: MCAR means the chance of a blank is independent of observed and unobserved values.
- D: MAR and MNAR differ in dependence on values that were not recorded, which the observed data cannot reveal.
- E: A blank caused by the value it hides is the defining case of MNAR.

**Source:** MCAR, MAR and MNAR

## MA-ch03.10

A table has an income column. Group B has 40% blank incomes and group A has 1%, and the overall missing rate is under 3%. A quality gate flags a column only when its overall missing rate is above 5%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A blank rate that differs by group means the missingness is not MCAR.
- [ ] B. The gate on the overall rate can pass while one group holds most of the blanks.
- [ ] C. Dropping the rows with a blank income, complete-case analysis, is safe because few rows are lost overall.
- [ ] D. Missingness that depends on group but not on income within a group is MAR.
- [ ] E. Reporting the missing rate within each group is a stratified check that the overall rate does not replace.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: MCAR requires the chance of a blank to be independent of observed variables such as group.
- B: An aggregate rate hides concentration, so a small overall rate says little about a subgroup.
- C: Complete-case analysis removes much of group B, which changes the group mix and can bias results about B.
- D: Dependence on an observed variable alone is the definition of MAR.
- E: A stratified check computes a statistic within subgroups, which exposes differences that an overall figure averages away.

**Source:** Differential missingness and stratified checks

## MA-ch03.11

An analyst fills the blanks of a numeric column with the mean of the observed values and then computes statistics on the filled column. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Mean imputation increases the variance of the column.
- [ ] B. Standard errors computed after mean imputation are too large, since extra rows were added.
- [ ] C. Mean imputation strengthens the correlation between this column and other columns.
- [ ] D. Mean imputation leaves the column mean unchanged but shrinks its variance.
- [ ] E. Median imputation leaves the column mean unchanged in a skewed column.

**Key:** A=F B=F C=F D=T E=F

**Why:**

- A: Filled values sit at the center, so the spread of the column falls rather than rises.
- B: Filled values are treated as real observations, which makes standard errors too small.
- C: Filled rows sit at the column mean regardless of other columns, which attenuates correlations toward zero.
- D: Adding copies of the mean keeps the mean but the added zero deviations reduce the variance.
- E: A median differs from the mean in a skewed column, so filling with it moves the mean.

**Source:** Mean imputation

## MA-ch03.12

An analyst decides how to handle blanks in a numeric column and knows the mechanism that produced them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under MCAR, complete-case analysis (listwise deletion) gives an unbiased mean at the cost of precision.
- [ ] B. Multiple imputation creates one best completed dataset and discards the uncertainty about the filled values.
- [ ] C. Filling a categorical column with its mean is a meaningful imputation.
- [ ] D. When the largest values go missing because they are large, the mechanism is MAR and deletion leaves the mean unbiased.
- [ ] E. When missingness depends on an observed column, imputing within groups of that column reduces bias compared with deleting rows.

**Key:** A=T B=F C=F D=F E=T

**Why:**

- A: Under MCAR the complete rows are a random subset, so deletion loses information but not accuracy.
- B: Multiple imputation creates several completed datasets and pools the results so imputation uncertainty is carried through.
- C: A mean of categories has no meaning; the most frequent class or a model-based method is used instead.
- D: Values missing because of their size are MNAR, and deleting them leaves a truncated, biased sample.
- E: Under MAR, conditioning on the observed driver of missingness lets the imputation reflect the missing rows.

**Source:** Complete-case analysis and multiple imputation

## MA-ch03.13

A patient table stores age as an integer and uses -999 for unknown age. A type check confirms the column is integer, and no range check was written. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A type check on the age column detects the placeholder, because -999 is not a valid age.
- [ ] B. A value such as -999 that stands in for unknown is a sentinel value.
- [ ] C. A range check for plausible ages flags the sentinel.
- [ ] D. Replacing -999 with 0 gives a defensible estimate of average age, since 0 is an integer.
- [ ] E. A sentinel is a random data-entry error and is found by a duplicate check.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: -999 is a valid integer, so a type check passes it.
- B: A sentinel is a special value written into a column to mean missing or unknown.
- C: A range check tests plausibility of values and exposes an impossible age.
- D: Zero is also an invalid age here; the sentinel should be recoded as a true missing value before computing statistics.
- E: A sentinel is a deliberate placeholder rather than a random error, and duplicate checks do not target it.

**Source:** Sentinel values and range checks

## MA-ch03.14

A pipeline validates a merged patient table against a schema: age is an integer from 0 to 120, weight is a number from 20 to 400, and the two date columns are dates. Every row passes. One hospital records weight in kilograms and another in pounds, and the table has no unit column. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Passing schema validation shows validity, conformity to declared formats and ranges, not correctness.
- [ ] B. A discharge date earlier than the admission date passes a date type check yet fails a cross-field rule.
- [ ] C. A range check from 20 to 400 tests whether the kilogram and pound sources are consistent.
- [ ] D. Adding a unit column validated against a list of allowed units makes the mismatch visible.
- [ ] E. Plotting the weight distribution by hospital would show one source shifted by a factor of about 2.2.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Validity concerns conformity to declared rules, while correctness concerns agreement with what actually happened.
- B: A type check looks at one value, and a cross-field rule checks a relationship between columns.
- C: A range check tests individual plausibility, not consistency of units between sources.
- D: Making the unit an explicit, validated field turns an implicit assumption into a testable one.
- E: A per-source comparison exposes a systematic shift that a pooled distribution can hide.

**Source:** Validity, correctness and cross-field rules

## MA-ch03.15

In pandas, comparing a missing value (NaN) with a number using >, <, <= or == gives False, and using != gives True. A table has some rows with missing age, some with age 0 or below, and the rest positive. An analyst writes df[df['age'] > 0] to remove only the invalid ages. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The filter removes the rows with missing age as well as the invalid ages, with no error.
- [ ] B. The filter raises a warning that rows with missing values were removed.
- [ ] C. The filter df[df['age'] != 0] keeps the rows with missing age, since NaN != 0 evaluates to True.
- [ ] D. Removing rows with missing age leaves the segment mix unchanged when the blanks are concentrated in one segment.
- [ ] E. A row-count assertion before and after a step is a cheap check for a silent drop.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: NaN > 0 is False, so missing rows fail the condition and vanish silently.
- B: The code is valid, so nothing signals the extra removal.
- C: NaN != 0 is True, so those rows pass that filter.
- D: Dropping rows concentrated in one segment shifts the segment mix of the table.
- E: A silent drop is a loss of rows without notice, and comparing counts to the expected result exposes it.

**Source:** Missing values in filters and silent drops

## MA-ch03.16

A table has one row per hospital visit, with a patient_id column and a visit_id column that is unique per visit. To remove duplicates, an analyst keeps the first visit for each patient_id. Each visit row carries its own label, readmitted within 30 days. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Deduplicating on patient_id is correct because repeat visits are redundant copies.
- [ ] B. A true duplicate is a repeated record of the same event, identified by a composite key such as patient_id plus visit_id.
- [ ] C. After keeping the first visit per patient, the readmission rate equals the rate in the original table.
- [ ] D. Keeping one row per patient changes the grain, the unit each row represents, from visit to patient.
- [ ] E. Grain refers to the number of columns in a table.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Rows with the same patient_id and different visit_id are different events, not copies.
- B: A duplicate means the same record twice, so the key must identify the event, not just the person.
- C: First visits and later visits can have different outcomes, so the rate generally shifts.
- D: Changing the entity key changes the unit of analysis and how heavily frequent users count.
- E: Grain is the level of detail a row represents, such as one row per visit.

**Source:** Duplicates, composite key and grain

## MA-ch03.17

Two annotators independently label the same items as toxic or not toxic, and the team computes agreement between them. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Observed agreement is the share of items given the same label by both annotators.
- [ ] B. Cohen's kappa adjusts observed agreement for agreement expected by chance.
- [ ] C. Kappa is usually higher than observed agreement because it adds credit for chance agreement.
- [ ] D. Disagreement between annotators establishes that the labeling guideline is flawed.
- [ ] E. Chance agreement depends on how often each annotator uses each label.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Observed agreement is a raw proportion of matching labels.
- B: Kappa measures agreement beyond what chance would produce.
- C: Kappa subtracts chance agreement, so it is lower than raw agreement.
- D: Disagreement can also come from ambiguous items, annotator error or legitimate differences in judgment.
- E: Expected agreement is computed from each annotator's label frequencies, so it is not fixed at one half.

**Source:** Inter-annotator agreement and Cohen's kappa

## MA-ch03.18

A binary classifier is scored against test labels from an annotator who flips the correct label on a random share of items, independently of the classifier. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Independent random label noise pulls measured accuracy below true accuracy for a model that beats chance.
- [ ] B. Label noise in the test set averages out, so measured differences between models stay the same size.
- [ ] C. Label noise in test labels does not affect evaluation, while label noise in training labels does.
- [ ] D. If label errors correlate with the model's errors, measured accuracy can exceed true accuracy.
- [ ] E. Independent label noise raises the signal-to-noise ratio when comparing two models.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Correct predictions are scored wrong when the label is flipped, and this outweighs wrong ones scored right.
- B: Independent symmetric noise compresses the measured gap between models.
- C: Noisy test labels cap measured performance, so evaluation labels need at least as much care as training labels.
- D: Correlated errors make the model agree with wrong labels, which inflates the score.
- E: The measured difference shrinks while sampling variability does not, so signal-to-noise falls.

**Source:** Label noise and measured accuracy

## MA-ch03.19

A model predicts whether a subscriber will cancel in the next 30 days. One feature, cancellation_survey_sent, is a flag set by an automated email that goes out at the moment a subscriber cancels. The model scores 0.99 AUC on a random hold-out. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A feature set at the moment the outcome occurs is an example of target leakage.
- [ ] B. A feature strongly associated with the label and without missing values is safe to keep.
- [ ] C. Removing the suspect feature and re-evaluating is an ablation.
- [ ] D. A random hold-out split exposes the leak, since leaked rows are kept apart from the training rows.
- [ ] E. Leakage inflates the offline score relative to live performance because the feature is unavailable at prediction time.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: Target leakage is the use of information produced by or after the outcome.
- B: Strong association and completeness say nothing about availability at prediction time.
- C: An ablation removes a component and measures the change in performance.
- D: A random split puts the leaked flag in both partitions, so it cannot reveal the leak.
- E: The hold-out measures the leak, which is absent from live data, so deployed performance falls short.

**Source:** Target leakage and ablation

## MA-ch03.20

A chest-X-ray model is trained on 20,000 images from 5,000 patients, four images per patient. The images are split at random by image into training and test sets. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Splitting by patient, a group split, keeps the images of a patient on one side.
- [ ] B. A random split by image prevents entity overlap between the training and test sets.
- [ ] C. Choosing hyperparameters repeatedly on the test set leaves the final test score an unbiased estimate.
- [ ] D. A separate validation set is used for model selection so that the test set gives a single final estimate.
- [ ] E. Test contamination is limited to test rows being used for gradient updates.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: A group split assigns each entity, here a patient, entirely to training or entirely to testing.
- B: Same-patient images land on both sides, which is entity leakage that inflates the score.
- C: Repeated selection on the test set fits the choices to it, so the final score is optimistic.
- D: The validation set absorbs tuning decisions, which keeps the test set untouched for a final estimate.
- E: Contamination also arises when same-entity or near-identical data sit on both sides of the split.

**Source:** Entity leakage, group split and validation set

## MA-ch03.21

A text dataset contains some records that appear twice as byte-identical rows. A random split by row puts one copy of some of these records in training and the other in testing. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Removing exact duplicates before splitting prevents identical rows from landing on both sides.
- [ ] B. Exact-match deduplication removes near-duplicates that differ in capitalization or trailing whitespace.
- [ ] C. Near-duplicates are found by normalizing the text or by similarity matching.
- [ ] D. Deduplication should be done after splitting so each partition keeps its natural frequency.
- [ ] E. A nearest-neighbor classifier benefits from train-test duplicates by copying the label of the identical training row.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: With one copy of each record, a record cannot sit in both partitions.
- B: Byte-exact comparison treats such texts as different, so near-duplicates survive.
- C: Normalization or similarity matching finds texts that are nearly, but not exactly, the same.
- D: Deduplicating after the split leaves the overlap in place, which is the leakage to be avoided.
- E: Memorizing models, including nearest-neighbor ones, gain from seeing the test row in training.

**Source:** Exact duplicates, near-duplicates and train-test overlap

## MA-ch03.22

A screening dataset has a low share of positive cases, 2%. A classifier has high recall and a modest false-positive rate, and its overall accuracy is above 90%. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Recall is the share of actual positives that the classifier flags.
- [ ] B. Precision is another name for recall.
- [ ] C. Rebalancing the test set to half positives gives the same precision as at deployment prevalence.
- [ ] D. At low prevalence, a majority-class baseline that predicts negative for everyone scores high accuracy, which is why accuracy misleads under class imbalance.
- [ ] E. Precision does not depend on prevalence.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Recall, also called sensitivity, is true positives divided by actual positives.
- B: Precision is true positives divided by flagged cases, a different quantity.
- C: Precision depends on prevalence, so a rebalanced test set overstates it relative to deployment.
- D: A majority-class baseline is the trivial rule of always predicting the common class, and it can beat accuracy of real models.
- E: Precision is the share of positives among those flagged, which rises and falls with prevalence.

**Source:** Class imbalance, precision and recall

## MA-ch03.23

A health system trains a model to choose patients for a care-management program using next-year spending as the label. One group faces access barriers, so at a given illness burden its patients generate less spending. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Next-year spending used as a label for illness burden is a proxy for the construct.
- [ ] B. High predictive accuracy on the label establishes construct validity.
- [ ] C. A label that understates need for one group is differential measurement bias.
- [ ] D. Dropping the group indicator from the features removes bias carried by the label.
- [ ] E. Fairness through unawareness, dropping the sensitive attribute, leaves bias carried by proxies in place.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: The construct is the underlying concept, illness burden, and spending is a measurable stand-in for it.
- B: Predicting a label well shows predictive fit, not that the label measures the intended concept.
- C: Differential measurement means the relationship between the measure and the construct differs across groups.
- D: The bias sits in the target, and other features correlated with group carry it as well.
- E: Fairness through unawareness fails when remaining variables or labels act as proxies for the sensitive attribute.

**Source:** Proxy labels and construct validity

## MA-ch03.24

A model is trained on data from 2019 to 2021 and run in 2024. An analyst compares the binned distribution of a numeric feature between the two periods using the population stability index (PSI). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Covariate shift is a change in the input distribution and can be detected without labels.
- [ ] B. Concept drift is a change in the input distribution with the input-output relationship unchanged.
- [ ] C. Label shift, also called prior probability shift, is a change in the base rate of the outcome.
- [ ] D. The population stability index compares a feature's binned distribution between two periods.
- [ ] E. Concept drift can reduce accuracy even when the feature distributions look unchanged.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Covariate shift concerns inputs, so comparing feature distributions needs no outcomes.
- B: That describes covariate shift; concept drift is a change in the relationship between inputs and outcome.
- C: Label shift is a change in how common each outcome class is.
- D: PSI sums a measure of difference over bins and is zero when the two distributions match.
- E: A changed input-output relationship harms accuracy without any visible change in inputs.

**Source:** Covariate shift, concept drift, label shift and PSI

## MA-ch03.25

A claims dataset covers 60 months and should hold about the same number of records each month. A count-by-month plot shows a drop to about half the usual count for three consecutive months. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A count-by-month plot shows a level shift but not its cause.
- [ ] B. Duplicating neighboring months' records restores the information missing from the gap.
- [ ] C. Breaking counts down by source system helps separate a collection outage from a real change in activity.
- [ ] D. A drop in counts is a finding if a known external event explains it, and noise otherwise.
- [ ] E. A shortfall that is a small share of total records is ignorable regardless of cause.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: A count series reports that something changed, not why.
- B: Copies of other months add no information about the missing months and distort the distribution.
- C: An outage affects specific feeds, while a real change in behavior appears across sources.
- D: An unexplained drop is itself a finding that needs an explanation.
- E: A small total can hide a large loss in a subgroup or period.

**Source:** Record counts over time and source breakdown

## MA-ch03.26

Proposals for datasheets for datasets list questions under motivation, composition, collection process, preprocessing, uses, distribution and maintenance. A team is deciding how much to rely on a datasheet written by a dataset's creators. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A completed datasheet verifies that the dataset is free of sampling and labeling bias.
- [ ] B. Answers about motivation and collection process help a user judge whether the dataset suits a different purpose.
- [ ] C. A datasheet from the creators replaces the user's own exploratory checks.
- [ ] D. Maintenance information, such as versioning and who updates the data, affects whether a result can be reproduced.
- [ ] E. The preprocessing section records transformations such as filtering, joining or relabeling that the final numbers no longer show.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: A datasheet documents claims and choices; it does not test the data for bias.
- B: Fitness for use depends on how and why the data were gathered.
- C: Documentation can be incomplete or out of date, so users still check the data against it.
- D: A result tied to an unversioned, changing dataset cannot be reproduced.
- E: Documented processing steps show what was done to the data before the user received it.

**Source:** Datasheets for datasets

## MA-ch03.27

A training table has a column risk_score. The documentation says only that it was computed upstream. A colleague adds that it is the output of an earlier team's model, trained on data that include part of the period now being used for evaluation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Lineage is the record of who collected the data and from where, and provenance is the sequence of transformations.
- [ ] B. Provenance records the origin of data, such as who produced it, when and how, while lineage traces the transformations from sources to a derived column.
- [ ] C. Naming the raw source file documents the lineage of a column produced by several transformation steps.
- [ ] D. A plausible histogram and no blanks establish what the column measures.
- [ ] E. Provenance information tells a user whether a value is correct.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The two definitions are swapped; provenance concerns origin and lineage concerns transformation steps.
- B: Provenance answers where data came from, and lineage answers what was done to them on the way to the current form.
- C: Lineage requires the intermediate steps, not just the starting point.
- D: Completeness and shape are properties of the values and say nothing about what produced them.
- E: Provenance documents origin and handling; correctness is a separate question that needs checking.

**Source:** Provenance versus lineage

## MA-ch03.28

A sample of 20 values has most values near 50 and two values near 100. An analyst applies the IQR rule, which flags values beyond fences set by the quartiles, and a z-score rule, which flags values more than three standard deviations from the mean. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The IQR rule is less affected by extreme values than a z-score rule because quartiles are robust statistics.
- [ ] B. The IQR rule decides whether a flagged value is a data-entry error.
- [ ] C. A flagged value is an error and should be deleted.
- [ ] D. Masking occurs when extreme values inflate the mean and standard deviation so that a z-score rule misses them.
- [ ] E. The IQR fences are the quartiles plus or minus three standard deviations.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: A robust statistic changes little when a few values are extreme.
- B: A rule only flags candidates; whether a value is an error depends on how it was recorded.
- C: A flagged outlier may be a legitimate extreme, so removing, capping or keeping it needs domain knowledge.
- D: Extreme values contaminate the very statistics a z-score rule relies on, which masks them.
- E: The fences are 1.5 times the IQR below the first quartile and above the third quartile.

**Source:** Outliers, IQR rule, z-score and masking

## MA-ch03.29

Four datasets have the same means, variances, Pearson correlation of about 0.82 and least-squares line, yet their scatter plots look very different. In one dataset, a single point far from the rest determines the fitted slope. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Pearson correlation measures linear association.
- [ ] B. A correlation heatmap of Pearson coefficients detects nonlinear dependence reliably.
- [ ] C. For y = x squared over a range symmetric around zero, the Pearson correlation is near zero despite a deterministic relationship.
- [ ] D. Datasets with identical summary statistics can have very different scatter plots, as Anscombe's quartet shows.
- [ ] E. A single influential point can create or dominate a high correlation.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Pearson correlation summarizes how well a straight line describes the relationship.
- B: A heatmap of Pearson coefficients can show near-zero values for strongly dependent but nonlinear pairs.
- C: The symmetric curve cancels the linear association, so the coefficient is near zero.
- D: Summary numbers discard shape, which is why plotting is needed alongside them.
- E: An influential point, one with high leverage, can drive the fitted line and the coefficient.

**Source:** Pearson correlation, Anscombe's quartet and influential points

## MA-ch03.30

A support-ticket table has columns ticket_id, category and body. An analytics tool is granted access to those three columns. The body column is free text in which customers sometimes paste phone numbers, partial card numbers and links to documents held in other systems. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A review of column types and permissions reveals phone numbers pasted into free text.
- [ ] B. Column-level permissions apply to a column as a unit, not to the content inside it.
- [ ] C. Scanning free text for sensitive patterns is a form of schema validation.
- [ ] D. Links inside a text field can widen an AI tool's effective data scope beyond what the access policy lists.
- [ ] E. Scanning free text for sensitive patterns is a content-level check that structural validation does not provide.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Types and permissions describe structure, not what customers typed into a text field.
- B: A permission granted on a column covers everything in it, including sensitive text.
- C: Schema validation tests structure such as type and range, not the content of free text.
- D: References inside data turn a bounded table into an entry point to other data.
- E: Content-level inspection finds identifiers and pointers that type and permission checks miss.

**Source:** Data scope, free text and content-level checks

## MA-ch03.31

Before modeling on a dataset it did not create, a team plans an audit. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A report that says no issues were found is as informative as a report listing the checks run and not run.
- [ ] B. Writing down the expected row count, time span and population before opening the data gives a benchmark that prevents hindsight rationalization.
- [ ] C. Passing type, range, missingness and duplicate checks confirms that the data cover the intended population.
- [ ] D. Tracing sampled records back to their source system can reveal undocumented transformations.
- [ ] E. When the source systems are unreachable, the documentation should be treated as verified.

**Key:** A=F B=T C=F D=T E=F

**Why:**

- A: Without the scope of the checks, a reader cannot tell what no issues covers.
- B: A prior expectation gives observed numbers something to be compared against.
- C: Those checks read the data as recorded and do not test coverage of the intended population.
- D: Record-level tracing, sometimes called a spot check against source, finds recodings and drops that documentation omits.
- E: Unverifiable documentation is a risk to be recorded, and the opacity is itself a finding.

**Source:** Audit planning, expected counts and record tracing

## MA-ch03.32

An orders table is joined to a customers table on customer_id, and the team wants an audit report on the result before anyone uses it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Orders whose customer_id has no match in the customers table are orphan records, a referential integrity problem.
- [ ] B. Orders without a customer and customers without an order are different kinds of unmatched keys with different meanings.
- [ ] C. A duplicate key indicates an error and is not a legitimate one-to-many relationship.
- [ ] D. The overall drop rate is sufficient because it reflects the loss in each group.
- [ ] E. Referential integrity is the requirement that each foreign key value matches an existing key in the referenced table.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: An orphan record is a child row whose referenced parent row does not exist.
- B: An order with no customer breaks integrity, while a customer with no orders is usually an expected state.
- C: One customer with many orders is an intended one-to-many relationship, so duplicate keys need a decision in advance.
- D: A small overall loss can hide a large loss in a subgroup, so drop rates are reported per group.
- E: Referential integrity ties every foreign key to a real row in the table it points to.

**Source:** Join audit, orphan records and referential integrity

## MA-ch03.33

A company runs an opt-in poll on its own website and reports that 82% of respondents say they would buy a new product. It announces that 82% of consumers would buy it. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A larger opt-in sample removes self-selection bias.
- [ ] B. Respondents who choose to answer form a voluntary response sample, a type of non-probability sample.
- [ ] C. Weighting by age and income corrects selection on interest in the product.
- [ ] D. The target population (the whole consumer base), the frame (people who see the poll) and the respondents (people who answer) are three different groups.
- [ ] E. A probability sample from a frame that covers the target population supports a defensible population estimate.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: More responses from the same process reduce random error, not systematic bias.
- B: A voluntary response sample is self-selected, so selection probabilities are unknown.
- C: Weighting adjusts for observed variables and does not fix selection on the outcome-related trait itself.
- D: Separating target population, frame and respondents shows where coverage and self-selection enter.
- E: Known selection probabilities from a covering frame allow design-based inference.

**Source:** Self-selection, voluntary response and probability samples

## MA-ch03.34

A dataset of loan applicants has an income column with many blanks. A missingness plot shows that blanks are far more common among applicants under 25, and the blank rate does not differ by region or loan size. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A blank rate that differs by age rules out MCAR.
- [ ] B. The observed data distinguish MAR from MNAR by comparing blank rates across age groups.
- [ ] C. A sensitivity analysis varies the assumed link between missingness and the unobserved income to see how results change.
- [ ] D. Dropping the blank rows is the handling that fits MAR.
- [ ] E. MNAR means missingness depends on observed variables such as age.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: MCAR requires blanks to be unrelated to observed variables, and age is observed.
- B: Telling MAR from MNAR requires knowing whether blanks depend on income itself, which was not recorded.
- C: Sensitivity analysis tests how conclusions hold under alternative assumptions about unobservable mechanisms.
- D: Under MAR, a method that uses age, such as imputation or stratified analysis, fits better than deletion.
- E: MNAR means missingness depends on the unobserved value; dependence on observed variables is MAR.

**Source:** Judging the missingness mechanism and sensitivity analysis

## MA-ch03.35

A team must treat a numeric predictor with 15% blank values before fitting a regression. They are comparing complete-case analysis, mean filling and multiple imputation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Under MNAR, multiple imputation corrects bias without further assumptions.
- [ ] B. Multiple imputation assumes MAR given the variables in the imputation model.
- [ ] C. Complete-case analysis is also called listwise deletion.
- [ ] D. Mean filling assumes MCAR.
- [ ] E. Sensitivity analysis reports how results change under alternative assumptions about the missing values.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: MNAR calls for explicit modeling of the missingness or sensitivity analysis, not a method that assumes MAR.
- B: Multiple imputation draws plausible values conditional on the observed variables in the model.
- C: Listwise deletion removes any row with a blank, which is the complete-case approach.
- D: Mean filling treats missing values as typical of the observed ones, which holds under MCAR.
- E: Sensitivity analysis shows how much conclusions depend on an untestable assumption.

**Source:** Choosing among missing-data treatments

## MA-ch03.36

A content-moderation team has each post labeled once by a crowd worker, and a pilot with two independent workers gives only moderate agreement as measured by kappa. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Adjudication means a third reviewer resolves disagreements between annotators.
- [ ] B. Hard labels preserve the spread of opinion among annotators.
- [ ] C. Soft labels represent annotator disagreement as probabilities instead of a single class.
- [ ] D. Gold-standard items, whose correct labels are known, are used to check annotator quality.
- [ ] E. A moderate kappa tells which sentence of the guideline is unclear.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: Adjudication is a resolution step that produces a final label for contested items.
- B: A hard label collapses several opinions into one class and hides the disagreement.
- C: A soft label is a distribution over classes that keeps the disagreement information.
- D: Gold items give an independent standard against which annotators are scored.
- E: Kappa is a summary of agreement and does not locate the source of disagreement.

**Source:** Label quality: adjudication, soft labels and gold items

## MA-ch03.37

A model predicting hospital readmission reports 0.98 AUC, while published models for the task reach about 0.70. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Target encoding computed from the full dataset, including test rows, before the split is not leakage.
- [ ] B. Fitting a scaler or imputer on the full dataset before splitting is preprocessing leakage.
- [ ] C. A score far above published results for the same task confirms the evaluation is sound.
- [ ] D. A random split of time-ordered data lets future information into training, which is temporal leakage.
- [ ] E. A temporal split trains on earlier periods and tests on later periods.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: Computing encodings with test labels lets test information shape training features, which is leakage.
- B: Statistics fitted on the test rows carry information about them into the training pipeline.
- C: A surprisingly high score is a reason to look for leakage before accepting it.
- D: Random splitting mixes periods, so a model can learn from events that occur after those it is tested on.
- E: A temporal split mimics deployment, where the future is unseen at training time.

**Source:** Preprocessing leakage and temporal leakage

## MA-ch03.38

A school district builds a model to identify students who need extra academic support. The training label is whether the student received a failing grade the next term. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A failing grade is the construct, and need for support is the measurement.
- [ ] B. High accuracy on the failing-grade label establishes construct validity.
- [ ] C. Comparing the label with an independent measure of need, such as assessments or counselor review, is a way to assess construct validity.
- [ ] D. Operationalizing a construct means collecting more rows of the same measurement.
- [ ] E. If agreement between the label and an independent measure is the same across schools, differential measurement is present.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: The construct is the underlying concept, need for support, and the failing grade is its measurable proxy.
- B: Accuracy shows the proxy is predicted well, not that it measures need.
- C: Agreement with an independent measure of the same concept is evidence of validity.
- D: Operationalizing means defining a measurable variable that stands for the concept.
- E: Differential measurement means the label tracks the construct differently across groups, which shows as unequal agreement.

**Source:** Construct, operationalization and construct validity

## MA-ch03.39

A fraud model trained on transactions from 2019 to 2021 is deployed in 2024, and its alert precision declines. Labels come mainly from chargebacks, which arrive weeks later, and from investigated alerts. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Random k-fold validation is the appropriate way to evaluate a model on drifting time-ordered data.
- [ ] B. Training on a past window assumes stationarity, meaning future data come from a process like the one that produced the training window.
- [ ] C. Chargeback labels that arrive weeks after the transaction are an example of label delay.
- [ ] D. Labels that exist mainly for flagged or investigated transactions create selection bias in the feedback.
- [ ] E. An audited random sample of live transactions gives an unbiased estimate of live performance.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Random folds mix periods, so they cannot reveal degradation caused by time.
- B: Stationarity is the assumption that the data-generating process does not change over time.
- C: Label delay means outcomes are known only some time after the prediction.
- D: Outcomes observed only for cases that the model or analysts selected are a biased sample of all cases.
- E: Random selection with careful labeling removes the dependence of labels on the model's own flags.

**Source:** Stationarity, label delay and selection in feedback

## MA-ch03.40

A data engineer reports that data passed validation: types are right, no value is null and values are within allowed ranges. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A value that is well formed but does not match what actually happened is valid yet incorrect.
- [ ] B. Totals that do not add up are detected by a type check.
- [ ] C. A frequency table showing spikes at special values reveals sentinels.
- [ ] D. Comparing distributions by source reveals unit or scale mismatches.
- [ ] E. Tracing sampled records back to their source reveals plausible but wrong entries.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Validity is conformity to declared rules, and correctness is agreement with reality.
- B: A relationship across fields needs a cross-field or reconciliation rule, not a type check.
- C: A spike at a value such as -999 or 1900-01-01 suggests a placeholder.
- D: A per-source comparison shows a constant factor between sources, as with kilograms and pounds.
- E: Plausible errors pass automated rules, so only comparison with the source can expose them.

**Source:** Validity versus correctness checks

## MA-ch03.41

A lender has repayment outcomes only for applicants approved under a fixed score cutoff and wants a model that scores all applicants. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Approving a small random share of applicants below the cutoff yields unbiased labels in that region.
- [ ] B. A lack of overlap between approved and rejected score ranges is called a positivity or overlap violation.
- [ ] C. Reject inference rests on assumptions that are untestable with the observed data.
- [ ] D. Reweighting by the old score recovers outcomes in the rejected score range when approval used a fixed cutoff.
- [ ] E. A sensitivity analysis reports how results change under alternative assumptions about unobserved outcomes.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: Randomization breaks the link between the old rule and the outcome in that region, which is a form of exploration.
- B: Positivity requires every group of interest to have some chance of being observed, and a fixed cutoff removes that for rejected scores.
- C: Reject inference fills in missing outcomes using modeled assumptions about rejected applicants.
- D: Reweighting needs observed cases to weight up, and none exist beyond the cutoff.
- E: Sensitivity analysis shows how much a conclusion depends on an untestable assumption.

**Source:** Remedies for selective labels

## MA-ch03.42

A team inherits a training table in which one column, customer_value, has no blanks and a clean distribution. The documentation says only that it was computed upstream, and the source systems cannot be reached. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An undocumented column that is untraceable should be treated as verified because it has no blanks.
- [ ] B. A column computed from a model or formula is a derived feature, not a raw measurement.
- [ ] C. Training the model with and without the column and comparing results is a sensitivity test.
- [ ] D. The time window that defines a feature has no bearing on whether it is available at prediction time.
- [ ] E. If the upstream owner changes the computation without notice, the feature can shift while the raw inputs stay the same, a silent upstream change.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: An untraceable column is unverified, and the opacity is itself a finding.
- B: A derived feature is produced by transforming or modeling other data, so it inherits their assumptions.
- C: A sensitivity test checks how much the result depends on one component.
- D: The window decides which events are included, and so whether information from the future or from the outcome entered it.
- E: A silent upstream change alters a feature's meaning or distribution without any change visible in the source data.

**Source:** Derived features and silent upstream change

## MA-ch03.43

A data validation report shows no missing values, reasonable distributions and no outliers. A separate investigation found that the training data include only customers who completed onboarding, while the deployed model will also score customers who abandoned onboarding. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The gap between the training population and the deployment population is a population mismatch that the clean report does not address.
- [ ] B. A clean report establishes that the model will run on the same population it was trained on.
- [ ] C. Shadow mode runs the model alongside the current process without acting on its outputs.
- [ ] D. Routing customers outside the validated population to human review is a scope restriction.
- [ ] E. Coverage and well-formedness are two names for the same property.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: A population mismatch means the cases scored in use differ from those used in training.
- B: A clean report shows well-formed, plausible rows, not who is in or out of the data.
- C: Shadow mode lets a model be evaluated on live cases without affecting decisions.
- D: Limiting the model's scope to the population it was validated on is a standard control.
- E: Coverage concerns who is represented; well-formedness concerns whether recorded values are valid.

**Source:** Population mismatch, shadow mode and scope restriction

## MA-ch03.44

An engineer proposes letting an AI coding assistant carry out a whole data audit, including writing the dataset documentation. The review team discusses what to delegate and what to check. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Validation asks whether the computation matches its specification, and verification asks whether the output fits the intended use.
- [ ] B. Verification asks whether the work was done correctly against a specification, and validation asks whether it serves its intended purpose.
- [ ] C. Fluent documentation drafted by an AI assistant is evidence that the documentation is correct.
- [ ] D. Deciding which population the dataset should represent is a mechanical check suited to full delegation.
- [ ] E. A hallucination is a model output that is fluent and grounded in its sources.

**Key:** A=F B=T C=F D=F E=F

**Why:**

- A: The two definitions are swapped.
- B: Verification checks building the thing right, and validation checks building the right thing.
- C: Fluent style is not evidence of correctness, because it can look complete without information the human supplied.
- D: Deciding what the data should represent depends on purpose and stakes, not on computation.
- E: A hallucination is fluent output that is unsupported or false.

**Source:** Verification, validation and delegation to AI

## MA-ch03.45

An analyst gives an AI tool the instruction: clean the data, remove duplicates and bad rows, and fill in the blanks. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Remove duplicates is ambiguous until the key is specified, such as the combination of patient_id and visit_id.
- [ ] B. Clean the data is precise because it names the operation.
- [ ] C. Remove bad rows is imprecise, while naming a rule such as values outside a valid range or failing a cross-field check is exact.
- [ ] D. Deduplicate on patient_id is a safe instruction for a table with one row per visit.
- [ ] E. Fill in the blanks is imprecise, while naming imputation and the assumed missingness mechanism is exact.

**Key:** A=T B=F C=T D=F E=T

**Why:**

- A: A duplicate is defined relative to a key, and the wrong key removes distinct events.
- B: Clean is a vague word that hides the operations, thresholds and assumptions.
- C: A named rule can be checked and reproduced, while bad is a judgment.
- D: On visit-level data that instruction collapses distinct visits into one row per patient.
- E: Imputation is the method, and the mechanism, MCAR, MAR or MNAR, states the assumption behind it.

**Source:** Precise wording in prompts for data cleaning

## MA-ch03.46

A validation report for a tabular dataset consists of histograms of numeric columns, a table of missing-value counts, a correlation heatmap and a line chart of record counts by month. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A histogram can show spikes at sentinel values.
- [ ] B. A table of missing-value counts does not reveal rows that were excluded before the file existed.
- [ ] C. A heatmap encodes values as color intensity, which people decode less accurately than position along a common scale.
- [ ] D. A dot chart with error bars shows uncertainty that a heatmap of coefficients leaves out.
- [ ] E. A correlation heatmap shows a confidence interval for each coefficient.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: A histogram shows the shape of a distribution, so a spike at a special value stands out.
- B: Counting blanks says nothing about rows that are absent from the file.
- C: Position along a common scale is read more accurately than color, so small differences are hard to judge.
- D: Error bars display the uncertainty of an estimate, which depends on sample size.
- E: A plain heatmap shows point estimates and not interval estimates.

**Source:** What validation charts show and hide
