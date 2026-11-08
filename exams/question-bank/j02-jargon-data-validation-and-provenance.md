# Jargon test: data validation and provenance

## MA-jargon.13

A team asks an agent to "document the provenance of the table" but really wants the steps from the raw file to the final table. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Lineage traces the transformations and movements of data from source to current form.
- [ ] B. Lineage describes the licence terms of the data.
- [ ] C. Provenance records the origin of data, such as who collected it and how.
- [ ] D. For the steps from raw file to final table, the better term is provenance.
- [ ] E. Provenance and lineage are identical.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: Lineage is the path through processing steps.
- B: Licence terms are separate metadata.
- C: Provenance answers where the data came from.
- D: The better term for processing steps is lineage.
- E: They overlap but name different things.

**Source:** Provenance vs lineage

## MA-jargon.14

An engineer says the pipeline has been validated because the output matches the written specification. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Verification asks whether the system meets the real need of its users.
- [ ] B. Verification and validation answer the same question.
- [ ] C. Validation means re-running the same code to check it gives the same output.
- [ ] D. Validation asks whether the output conforms to the written specification.
- [ ] E. A pipeline can conform to its specification and still fail to serve the real need.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: That describes validation.
- B: Building it right differs from building the right thing.
- C: That is reproducibility.
- D: That describes verification.
- E: Passing verification does not guarantee validation.

**Source:** Validation vs verification

## MA-jargon.15

A column named age holds the value 240 in one row, and a date column holds text such as "next Tuesday". Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A semantic check is another name for a schema check.
- [ ] B. An age of 240 stored as an integer passes the schema check but fails a semantic check.
- [ ] C. Text in a date column fails the schema check.
- [ ] D. A schema check tests structure such as column names, types and required fields.
- [ ] E. A semantic check tests whether values make sense in the domain, such as a plausible age.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: The two check different things.
- B: The type is right but the value is implausible.
- C: The type does not match the declared type.
- D: Schema concerns shape and type, not meaning.
- E: Semantic checks use domain meaning.

**Source:** Schema vs semantic check

## MA-jargon.16

A model scores very high because some test rows are also in the training set, and a separate benchmark score is high because its questions appeared in the pretraining text. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Benchmark contamination is test items appearing in a model's training corpus.
- [ ] B. Data leakage is information from outside the training data, or from the target, getting into training so evaluation is inflated.
- [ ] C. Contamination is a type of missingness.
- [ ] D. A feature derived from the label is a source of leakage.
- [ ] E. Leakage describes a model that memorises noise in the training data.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: The benchmark was seen before it was tested.
- B: Leakage breaks the separation between training and evaluation.
- C: Contamination concerns overlap with training data, not absent values.
- D: It encodes the answer the model is meant to predict.
- E: That is overfitting.

**Source:** Leakage vs contamination

## MA-jargon.17

A cleaning step removes rows that are byte-for-byte identical, yet the train and test sets still share rows that differ only by trailing whitespace. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Removing exact duplicates also removes near-duplicates.
- [ ] B. Near-duplicates shared between train and test can cause leakage.
- [ ] C. Near-duplicates are records that differ slightly, such as a typo or whitespace, but carry the same content.
- [ ] D. Exact duplicates are records that are identical.
- [ ] E. Fuzzy matching or hashing of text shingles is a way to detect near-duplicates.

**Key:** A=F B=T C=T D=T E=T

**Why:**

- A: Exact matching misses slightly different copies.
- B: The model has effectively seen the test item.
- C: They are close copies rather than identical copies.
- D: Identical rows match on every field.
- E: Those methods score similarity instead of requiring equality.

**Source:** Duplicates vs near-duplicates

## MA-jargon.18

Income is missing more often for people with high income, and a reviewer asks for the exact missingness type. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. MCAR means the chance of a value being missing is unrelated to observed and unobserved values.
- [ ] B. MAR means missingness depends on observed variables but not on the missing value once they are accounted for.
- [ ] C. This pattern is MNAR, missing not at random.
- [ ] D. Older respondents skipping a question, with age recorded, is MNAR.
- [ ] E. Dropping incomplete rows is unbiased under MNAR.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: MCAR is missing completely at random.
- B: MAR is missing at random given recorded variables.
- C: Missingness depends on the unobserved value itself.
- D: It depends on an observed variable, so it is MAR.
- E: Under MNAR the remaining rows are a biased sample.

**Source:** MCAR vs MAR vs MNAR

## MA-jargon.19

Match each situation to a missingness type. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Respondents with low recorded education skip an income question more often, which is MAR.
- [ ] B. Imputing the column mean is a test that distinguishes MNAR from MAR.
- [ ] C. MCAR means missingness depends on the value that is missing.
- [ ] D. A sensor drops readings at random because of power glitches unrelated to the readings, which is MCAR.
- [ ] E. Patients with the worst symptoms miss follow-up so their symptom score is missing, which is MAR.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Missingness depends on a recorded variable.
- B: Imputation is a repair, not a diagnostic of the mechanism.
- C: That describes MNAR.
- D: Unrelated causes give missing completely at random.
- E: Missingness depends on the unobserved score, so it is MNAR.

**Source:** Missingness situations

## MA-jargon.20

A cleaner proposes deleting the largest transactions and calling them anomalies. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An outlier is a data point far from the bulk of the distribution.
- [ ] B. An outlier is a data entry error that should be deleted.
- [ ] C. Anomaly detection is another name for imputation.
- [ ] D. A value can be a statistical outlier and still be a valid measurement.
- [ ] E. An anomaly is an observation that does not conform to expected behaviour, and it may signal a fault or fraud.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Outlier is a statement about position in the distribution.
- B: An outlier can be a valid measurement.
- C: Imputation fills missing values; anomaly detection flags unusual cases.
- D: Extreme values are not automatically errors.
- E: Anomaly is a statement about behaviour against expectation.

**Source:** Outlier vs anomaly

## MA-jargon.21

A team monitors input features in production against the training data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A drift alarm shows that accuracy has dropped.
- [ ] B. A two-sample Kolmogorov-Smirnov test needs labels for production rows.
- [ ] C. Population stability index compares binned distributions of a feature between two periods.
- [ ] D. Data drift is a change in the distribution of input features between reference data and new data.
- [ ] E. A drift check measures model accuracy on production data.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Inputs can drift without a change in accuracy.
- B: It compares feature distributions and needs no labels.
- C: It scores how much a binned distribution moved.
- D: It compares feature distributions across time.
- E: Drift checks compare inputs; accuracy needs outcomes.

**Source:** Data drift checks

## MA-jargon.22

A spec says the dataset has "labels" and a reviewer asks whether they are ground truth. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Label noise refers to random features added to the inputs.
- [ ] B. Ground truth is the model's predicted value.
- [ ] C. Inter-annotator agreement measures how close the labels are to ground truth.
- [ ] D. Labels from a single annotator are ground truth.
- [ ] E. A label is the target value attached to an example, whether or not it is correct.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: Label noise means wrong or inconsistent labels.
- B: Ground truth is a reference for the real value, not a prediction.
- C: Agreement measures consistency among annotators, not correctness.
- D: One annotator can be wrong or inconsistent.
- E: Labels are assigned values and can contain errors.

**Source:** Labels vs ground truth

## MA-jargon.23

A dataset is shared with a colleague and no documentation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A datasheet for datasets documents motivation, composition, collection process and recommended uses.
- [ ] B. Recording known gaps and intended use helps downstream users judge fit.
- [ ] C. A data card summarises a dataset's provenance, contents and known limitations.
- [ ] D. A model card documents a dataset's collection process.
- [ ] E. A datasheet should state consent and licensing when they are known.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It is a structured description of the dataset.
- B: Documentation lets users decide whether the data suits their task.
- C: It tells users what the data is and where it falls short.
- D: A model card documents a model.
- E: Those facts affect permitted use.

**Source:** Data card and datasheet

## MA-jargon.24

A manager asks an AI agent: "Check the data is clean and correct and from a trusted source." Choose the rewrites that use exact terms. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Report lineage as the licence and the author.
- [ ] B. Record the provenance, meaning the source and collection method.
- [ ] C. Run a schema check on column types and required fields.
- [ ] D. Verify that test rows do not leak by deleting the test set.
- [ ] E. Run semantic checks such as plausible value ranges.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Lineage is the transformation path.
- B: Provenance covers origin.
- C: That names the structural check.
- D: Leakage checks look for overlap such as duplicates, and deleting the test set removes the evaluation.
- E: That names the domain-meaning check.

**Source:** Rewrite a vague data-quality prompt
