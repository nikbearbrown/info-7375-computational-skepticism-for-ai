# INFO 7375 midterm glossary: say it exactly

The jargon test is a language test. Precise words let you tell a language model exactly what to check, compute or build. If you write "report sensitivity and specificity at a 0.5 threshold, with a 95 percent Wilson interval" you get that. If you write "check that the model is good" the agent guesses, and a guess is not a claim you can test.

Each table gives the term and one plain sentence. Meanings are standard usage in statistics and machine learning. Where one row holds two terms ("X vs Y"), the row says how they differ.

## Probability and statistics foundations

| Term | Meaning |
|---|---|
| Probability | A number from 0 to 1 that measures how likely an event is, or how strongly it is believed |
| Complement rule | The probability that an event does not happen is 1 minus the probability that it does |
| Mutually exclusive events | Events that cannot both happen; their joint probability is zero |
| Addition rule (inclusion-exclusion) | P(A or B) = P(A) + P(B) - P(A and B); the subtraction removes the overlap counted twice |
| Joint probability | The probability that two events both happen |
| Marginal probability | The probability of one event on its own, ignoring the others |
| Conditional probability | The probability of an event given that another event has happened, P(A given B) |
| Chain rule | P(A and B) = P(A) times P(B given A); joint probabilities are built from conditionals |
| Law of total probability | An event's overall probability is the sum, over a set of exclusive and exhaustive cases, of P(case) times P(event given case) |
| Independence | Learning one event happened does not change the probability of the other, so P(A and B) = P(A) P(B) |
| Dependence | Events that are not independent: knowing one changes the probability of the other |
| Conditional independence | Two events are independent once a third event or variable is held fixed |
| Coherence | Probabilities that obey the rules (between 0 and 1, add up correctly), so no combination of bets guarantees a loss |
| Normalization | Requiring that the probabilities of all possible outcomes add up to 1 |
| Dutch book | A set of bets that guarantees a loss because the stated probabilities are incoherent |
| Prior | The probability of a hypothesis before seeing the new evidence |
| Likelihood | The probability of the observed data if a given hypothesis were true; it is not the probability of the hypothesis |
| Posterior | The updated probability of a hypothesis after combining the prior with the evidence |
| Posterior probability | The probability that a hypothesis is true given the data; a p-value is not this |
| Odds | The ratio of the probability an event happens to the probability it does not, p / (1 - p) |
| Prior odds | The odds of a hypothesis before seeing the evidence |
| Likelihood ratio | How many times more probable the evidence is under one hypothesis than under another |
| Bayes' rule | Posterior odds equal prior odds times the likelihood ratio; it updates a prior with evidence |
| Base rate (prevalence) | How common the condition is in the population before any test result is known |
| Base rate fallacy (base rate neglect) | Ignoring the base rate and judging only from the test result, which overstates how likely a positive is true |
| Transposed conditional (prosecutor's fallacy) | Confusing P(evidence given innocent) with P(innocent given evidence) |
| Expected value | The probability-weighted average of the possible outcomes |
| Mode | The most frequent or most probable value |
| Variance | The average squared distance of values from their mean; it measures spread |
| Standard deviation | The square root of the variance, in the same units as the data |
| Skewness | A measure of how lopsided a distribution is; a long tail on one side gives skew |
| Probability mass function | For a discrete variable, the probability of each exact value |
| Probability density function | For a continuous variable, a curve whose area over an interval gives that interval's probability |
| Cumulative distribution function | The probability that a variable is at or below a given value |
| Binomial | The count of successes in a fixed number of independent trials with the same success probability |
| Overdispersion | More variability than a model such as the binomial or Poisson predicts, often from dependence or hidden groups |
| Underdispersion | Less variability than the model predicts |
| Poisson approximation | For many trials each with small probability, the binomial count is close to a Poisson with the same mean |
| Normal distribution | The symmetric bell-shaped distribution set by its mean and standard deviation |
| Z-score | How many standard deviations a value lies from the mean |
| Empirical rule | For a normal distribution, about 68, 95 and 99.7 percent of values fall within 1, 2 and 3 standard deviations |
| Fat tails (heavy tails) | Extreme values occur far more often than a normal distribution would allow |
| Chebyshev's inequality | For any distribution with finite variance, at most 1/k squared of values lie more than k standard deviations from the mean |
| Cauchy | A heavy-tailed distribution with no mean or variance, so averages do not settle down as data grow |
| Quantile-quantile plot | A plot of sample quantiles against a reference distribution's quantiles; points on a line mean a good fit |
| Compounding | Multiplying probabilities across steps, so many individually reliable steps can give a low overall probability |
| End-to-end reliability | The probability that a whole chain of steps all succeed, not just each step alone |
| Sampling distribution | The distribution of a statistic (such as the mean) over repeated samples |
| Central limit theorem | Averages of many independent values are approximately normal, whatever the underlying distribution (with finite variance) |
| Statistic vs parameter | A statistic is computed from a sample; a parameter is the fixed true value in the population |
| Point estimate | A single best-guess value for a parameter |
| Estimator bias | The systematic gap between an estimator's average value and the true parameter |
| Estimator bias vs everyday bias | Estimator bias is a statistical property of an estimate; everyday bias means unfairness or prejudice, a different claim |
| Mean squared error | The average squared difference between estimates and the truth; it equals variance plus squared bias |
| Bias-variance trade-off | Flexible models have low bias but high variance, simple models the reverse; total error balances the two |
| Precision vs accuracy (measurement) | Precision is how tightly repeated estimates cluster; accuracy is how close they are to the truth |
| Sampling error | Random difference between a sample statistic and the population value because only part of the population was observed |
| Standard error | The standard deviation of a statistic's sampling distribution; it shrinks as sample size grows |
| Effective sample size | The number of independent observations the data are worth; correlated data have fewer than their row count |
| Non-sampling error | Error that does not come from random sampling, such as measurement, coverage or nonresponse error |
| Correlation vs independence | Zero correlation rules out only a linear relationship; independent variables are uncorrelated but not the reverse |
| Pearson correlation | A number from -1 to 1 that measures the strength of the linear relationship between two variables |
| Nonlinear dependence | A relationship that is not a straight line, which Pearson correlation can miss entirely |
| Correlated errors | Mistakes that tend to happen together, so combining sources gives less protection than independence would |
| Anscombe's quartet | Four datasets with nearly identical summary statistics but very different shapes, which shows why to plot data |
| Histogram | A bar chart of how many values fall in each range |
| Scatter plot | A plot of two variables as points, used to see their relationship |
| Correlation heatmap | A grid that colours each pairwise correlation, used to spot related variables |
| Error bars | Marks on a chart showing uncertainty, such as a confidence interval or standard error |
| Simpson's paradox | A trend that appears in every subgroup can reverse when the groups are combined |
| Stratification | Splitting data into subgroups (strata) and analysing each, or adjusting within them |
| Spurious association (spurious correlation) | A relationship that shows up in the data but does not reflect a real or stable connection |
| Confounder | A variable that influences both the supposed cause and the outcome, producing a misleading association |
| Outlier | A value far from the rest of the data |
| IQR rule | Flag a value as an outlier if it lies more than 1.5 interquartile ranges beyond the first or third quartile |
| Outlier rule | A stated numeric test (such as the IQR rule or a z-score cutoff) for calling a value an outlier |
| Median | The middle value when data are sorted; it barely moves when outliers appear |
| IQR (interquartile range) | The distance between the 25th and 75th percentiles |
| Robust statistic (robust statistics) | A summary, such as the median or IQR, that is not much changed by outliers |
| Masking | Several outliers hiding each other so that a rule such as the z-score fails to flag them |
| Influential point | A point whose removal would noticeably change a fitted result such as a regression line |
| Anomaly | An observation that does not fit the expected pattern; it may be an error or a real rare event |
| Sensitivity (recall, true positive rate) | Of the cases that are truly positive, the share the test or model catches |
| Specificity (true negative rate) | Of the cases that are truly negative, the share the test or model correctly clears |
| False positive rate | Of the truly negative cases, the share wrongly flagged as positive; it equals 1 minus specificity |
| False negative rate | Of the truly positive cases, the share the test missed; it equals 1 minus sensitivity |
| Positive predictive value (precision) | Of the cases flagged positive, the share that are truly positive; it depends on the base rate |
| False positive | A negative case wrongly flagged as positive |
| False negative | A positive case wrongly cleared as negative |
| True negative | A negative case correctly cleared |
| True positive | A positive case correctly flagged |
| Accuracy | The share of all predictions that are correct |
| F1 | The harmonic mean of precision and recall |
| Confusion matrix | A table counting true positives, false positives, true negatives and false negatives |
| Threshold (cutoff, decision threshold) | The score above which a model predicts positive; moving it trades false positives against false negatives |
| Cost-based threshold | A threshold chosen by weighing the costs of false positives and false negatives |
| Majority-class baseline | The accuracy from always predicting the most common class; a model must beat it to add anything |
| Class imbalance | One class is far more common than another, which makes accuracy misleading |
| Log-odds | The logarithm of the odds, log(p / (1 - p)); the scale on which logistic regression is linear |
| Odds ratio | The ratio of the odds of an outcome in one group to the odds in another |
| AUC | Area under the ROC curve; the chance a random positive is scored above a random negative |
| Overfitting | Fitting noise in the training data so that performance on new data is worse |
| Underfitting | A model too simple to capture the real pattern, so it does badly even on training data |
| Regularization | A penalty that limits model complexity to reduce overfitting |
| Ridge regularization | An L2 penalty on squared coefficients that shrinks them toward zero |
| Training vs generalization error | Training error is measured on the data used to fit; generalization error is the expected error on new data |
| Generalization gap | The difference between performance on training data and on new data |
| Cross-validation | Repeatedly training on part of the data and testing on the held-out part, then averaging |
| Nested cross-validation | Cross-validation with an inner loop for choosing settings and an outer loop for an honest estimate |
| Bias (bias-variance) | Error from a model's assumptions being too simple or wrong, even with unlimited data |
| Hyperparameter tuning | Choosing settings that are not learned from the data, such as regularization strength, by trying values |
| Target encoding | Replacing a category with the average outcome for that category; it leaks if computed using the row's own label |
| Correlation coefficient | A number summarising the strength and direction of a linear relationship; Pearson's r is the usual one |
| Aleatoric uncertainty | Uncertainty from randomness in the world that more data cannot remove |
| Epistemic uncertainty | Uncertainty from limited knowledge or data that more data can reduce |

## Claims and the skeptic's toolkit

| Term | Meaning |
|---|---|
| Methodical skepticism | Doubting a claim in order to test it, then accepting what survives the test |
| Cynicism | Rejecting claims without testing them; it is not the same as skepticism |
| Confirmation bias | Seeking and favouring evidence that supports what you already believe |
| Falsifier | An observation that, if it occurred, would show the claim is wrong |
| Falsification | Trying to show a claim false by a test it could fail |
| Unfalsifiable claim | A claim that no possible observation could contradict, so it cannot be tested |
| Falsifiable claim | A claim that names an observation that would prove it wrong |
| Prediction | A specific, checkable statement of what will be observed if a claim is true |
| Assumption | A condition taken as true without being tested, on which a conclusion depends |
| Scope of a claim | The conditions, data and population over which a claim is asserted to hold |
| Universal claim | A claim about all cases, which one counterexample can refute |
| Counterexample | A single case that contradicts a universal claim |
| Underdetermination | The same evidence fits more than one explanation, so the evidence alone cannot choose |
| Rival hypotheses | Competing explanations that must be ruled out before accepting a claim |
| Upstream and downstream components | Parts that feed a system (upstream) and parts that use its output (downstream); an error upstream propagates downstream |
| Scope restriction | Narrowing a claim to the conditions that the evidence actually covers |
| Cherry-picking | Reporting only the results or examples that favour a claim |
| Moving the goalposts | Changing what would count as success after seeing the result |
| Inconclusive result | A test whose outcome neither supports nor refutes the claim |
| Negative finding | A result showing no effect or no support, which is still information |
| Residual risk | The risk that remains after checks and mitigations |
| Red teaming | Deliberately attacking a system to find ways it fails |
| Held-out set | Data kept out of training and tuning, used only to estimate performance on new data |
| Held-out split | The division of data into parts so that one part is never used to fit the model |
| Validation set | Data used to tune and select models, not to give the final performance estimate |
| Test set | Data used once at the end to estimate performance on unseen cases |
| Test-set contamination | Information from the test set leaking into training or tuning, which inflates results |
| Benchmark contamination | Benchmark questions or answers appearing in a model's training data, which inflates its score |
| Adaptive overfitting | Overfitting to a test set by repeatedly choosing models according to its results |
| Variance across seeds | Differences in results from changing only the random seed; one run may not represent the method |
| Baseline | A simple reference result that a new method has to beat |
| Control group | A comparison group that does not get the treatment, so the effect can be isolated |
| Randomization (randomisation) | Assigning units to groups by chance so that groups differ only by luck |
| A/B test | A randomized comparison of two versions to measure the effect of the change |
| Operational definition | A definition stated as a measurable procedure, so that others can apply it the same way |
| Independent evidence | Evidence from a source whose errors do not depend on the other sources |
| Redundancy | Several independent checks of the same thing, which helps only if their errors are not correlated |
| Circularity | Using the conclusion, or something derived from it, as evidence for itself |
| Circular reporting | One original source repeated through several reports that look like independent confirmation |
| LLM-as-judge | Using a language model to score or grade other model outputs |
| Self-preference bias | A language model judge's tendency to favour outputs that resemble its own |
| Ground truth | The reference labels or facts treated as correct for evaluation |
| Reference standard | The best available measure of the true answer, against which a test is compared |
| Reproducibility vs accuracy | Reproducibility means getting the same result again; a result can be reproducible and still wrong |
| Provenance vs lineage | Provenance records where data came from and who handled it; lineage traces the steps that transformed it |
| Report vs state | A report says what happened; the state is what is actually true now, which must be checked directly |
| Verification vs validation | Verification checks that something was built to its specification; validation checks that it meets the real need |
| Verification | Checking that an output or system satisfies a stated requirement |
| Validation | Checking that a result or system does what it is actually needed for |
| Restore test | Actually restoring from a backup to prove the backup works |
| Discriminating test | A test whose result differs depending on which hypothesis is true |
| Regression test | A test that checks previously working behaviour still works after a change |
| Edge case | An unusual input at the limit of expected conditions, where failures often hide |
| Mutation testing | Deliberately inserting small bugs (mutants) to check whether the tests catch them |
| Mutation score | The share of mutants that the tests detect |
| Equivalent mutant | A mutant that behaves the same as the original, so no test can detect it |
| Solve-verify asymmetry | Checking an answer is often much cheaper than producing it |
| Verification bottleneck | When generating output is cheap but checking it takes scarce human time |
| Random sampling vs risk-based sampling | Random sampling gives every item an equal chance and supports estimates; risk-based sampling targets the likeliest failures |
| Audited random sample | A randomly chosen subset that is checked by hand to estimate the error rate of the whole |
| Unverified | Not yet checked; it is different from false |
| Goodhart's law | When a measure becomes a target, it stops being a good measure |
| Reward hacking | A system gaining a high score on the stated objective in a way that misses the intended goal |
| Accountability | Having a named person or body answerable for a decision or outcome |
| Audit trail | A record of who did what and when, so decisions can be reconstructed |
| Rubber-stamping | Approving without real review |
| Automation bias | Over-trusting automated output and failing to question it |
| Overreliance | Depending on a tool's output more than its reliability justifies |
| Human-in-the-loop | A design in which a person reviews or approves decisions before they take effect |
| Gate | A required check that work must pass before moving to the next stage |
| Segregation of duties | Requiring that the person who produces work is not the one who approves it |
| Approval design | How review and sign-off steps are structured so that they actually catch errors |
| Auditability | The property that a system's decisions can be examined and checked after the fact |
| Hallucination (confabulation) | A language model producing fluent, confident statements that are false or unsupported |
| Fluency | How smooth and natural text reads; it says nothing about whether it is true |
| Post hoc explanation | An explanation constructed after the result was seen, which may not reflect the real cause |
| HARKing | Hypothesizing after the results are known, then presenting the hypothesis as if it had come first |
| Precise prompt wording | Naming the exact quantity, method and criterion in an instruction, so the model has nothing to guess |
| Behavioural testing | Testing a model's outputs on designed inputs rather than examining its internals |
| Invariance test | Checking that the output does not change under changes that should not matter |
| Directional expectation test | Checking that the output moves in the expected direction when an input is changed |
| Minimal pair | Two inputs that differ in one small detail, used to isolate that detail's effect |
| Prompt sensitivity | Changes in a model's output caused by harmless rewording of the prompt |
| Indirect prompt injection | Malicious instructions hidden in content a model reads, such as a web page or document |
| Least privilege | Giving a system only the access it needs for its task |

## Probability, uncertainty and confidence

| Term | Meaning |
|---|---|
| Null hypothesis | The default claim of no effect or no difference, which a test tries to reject |
| P-value | The probability of data at least this extreme if the null hypothesis were true |
| P-value vs posterior probability | A p-value is P(data given null); a posterior probability is P(hypothesis given data), and they are not the same |
| Significance level | The cutoff (often 0.05) for the p-value, equal to the Type I error rate the test allows |
| Statistical significance | The result is unlikely under the null hypothesis at the chosen significance level |
| Practical significance | The effect is large enough to matter in the real setting |
| Statistical vs practical significance | A tiny effect can be statistically significant with enough data, and a large effect can fail to reach significance with little data |
| Effect size | The magnitude of a difference or relationship, independent of sample size |
| Type I error | Rejecting a true null hypothesis; a false positive finding |
| Type II error | Failing to reject a false null hypothesis; a missed real effect |
| Power (statistical power) | The probability of detecting a real effect of a given size; it equals 1 minus the Type II error rate |
| Confidence interval | A range computed by a procedure that captures the true parameter in a stated share (such as 95 percent) of repeated samples |
| Confidence level | The long-run share of intervals from a procedure that contain the true value, such as 95 percent |
| Interval estimate | A range of plausible values for a parameter rather than a single number |
| Margin of error | The half-width of a confidence interval, the plus-or-minus around the estimate |
| Coverage | The share of the time a stated interval actually contains the true value |
| Nominal coverage | The coverage an interval claims, such as 95 percent, which may differ from its actual coverage |
| Credible interval | A Bayesian range that contains the parameter with a stated posterior probability |
| Prediction interval | A range expected to contain a single future observation; it is wider than a confidence interval for the mean |
| Bootstrap interval | An interval built by resampling the data with replacement many times |
| Wilson interval | A confidence interval for a proportion that behaves well for small samples and extreme proportions |
| Upper confidence bound | A value that the true quantity is below, with stated confidence |
| Rule of three | With zero events in n trials, an approximate 95 percent upper bound on the event rate is 3/n |
| Absence of evidence | Not finding an effect is not proof that it is absent, particularly with a small sample |
| Equivalence test | A test designed to show that a difference is smaller than a stated margin, rather than merely not significant |
| False precision | Reporting more digits or tighter certainty than the data justify |
| Multiple comparisons (multiple comparisons problem) | Running many tests makes at least one false positive likely |
| Family-wise error rate (familywise error rate) | The probability of at least one false positive across a set of tests |
| False discovery rate | The expected share of rejected hypotheses that are actually false discoveries |
| False discovery proportion | The share of the discoveries in one particular set of results that are false |
| Bonferroni correction (Bonferroni) | Divide the significance level by the number of tests to control the family-wise error rate |
| Holm | A step-down procedure that controls the family-wise error rate and is never less powerful than Bonferroni |
| Benjamini-Hochberg | A procedure that controls the false discovery rate by comparing sorted p-values to a rising threshold |
| Adjusted p-value | A p-value changed to account for the number of tests performed |
| P-hacking | Trying analyses until one crosses the significance threshold, then reporting only that one |
| Exploratory vs confirmatory | Exploratory analysis generates hypotheses from the data; confirmatory analysis tests a hypothesis stated in advance |
| Preregistration (pre-registration) | Publishing the hypothesis and analysis plan before seeing the data |
| Publication bias | Significant or positive results are more likely to be published, which distorts the record |
| Winner's curse | The best-looking result among many is likely to be overestimated and to fall back on retest |
| Calibration | The match between stated probabilities and how often those outcomes actually occur |
| Calibration decay | Calibration getting worse over time as the data change |
| Discrimination | A model's ability to rank positives above negatives, separate from whether its probabilities are well calibrated |
| Overconfidence (overconfident) | Stated confidence higher than the actual frequency of being correct |
| Underconfidence | Stated confidence lower than the actual frequency of being correct |
| Confidence (model) | The probability a model assigns to its own prediction |
| Reliability diagram | A plot of predicted probability against observed frequency; a well-calibrated model sits on the diagonal |
| Expected calibration error | The average gap between predicted confidence and observed accuracy across confidence bins |
| Maximum calibration error | The largest gap between confidence and accuracy in any bin |
| Subgroup calibration | Calibration checked separately within each group |
| Brier score | The mean squared difference between predicted probabilities and the 0-or-1 outcomes; lower is better |
| Brier skill score | The Brier score's improvement over a reference forecast; above zero means better than the reference |
| Reference (climatological) forecast | A simple forecast, such as the overall base rate, used as the benchmark |
| Log loss | The negative average log probability given to the true outcome; it punishes confident wrong answers heavily |
| Proper scoring rule | A score that is best, in expectation, when the forecaster reports their true probabilities |
| Strictly proper scoring rule | A proper scoring rule where honest reporting is the only way to get the best expected score |
| Verbalized confidence | A confidence a language model states in words or numbers, which can be poorly calibrated |
| Token probability (logprob) | The probability, usually as a log, that a model assigns to each generated token |
| Self-consistency | Sampling several answers and treating agreement among them as a sign of confidence |
| Temperature scaling | Dividing the model's logits by a single number so that its probabilities become better calibrated |
| Recalibration | Adjusting a model's probabilities after training so that they match observed frequencies |
| Expected cost | The probability-weighted average cost of the possible outcomes of a decision |
| Tail risk | The danger from rare extreme outcomes that average-based summaries hide |
| Paired comparison | Comparing two methods on the same items, which removes item-to-item variation |
| Monitoring | Tracking a deployed system's inputs and performance over time |

## Data validation and provenance

| Term | Meaning |
|---|---|
| Data validation | Checking that data meet stated rules such as types, ranges and completeness |
| Data scope | The population, period and fields that the data actually cover |
| Schema check | Confirming that columns, names and types match the expected structure |
| Type check | Confirming that each value has the expected data type |
| Range check | Confirming that values fall within allowed limits |
| Cross-field rule | A rule linking several fields, such as an end date not before the start date |
| Semantic check | Confirming that values make sense in meaning, not just in format |
| Content-level check | A check on the values themselves rather than just the file structure |
| Referential integrity | Every reference in one table points to a record that exists in another |
| Orphan record | A record that refers to a parent record that does not exist |
| Validity vs correctness | A value is valid if it satisfies the rules; it is correct only if it is true |
| Unit mismatch | The same field recorded in different units, such as pounds and kilograms |
| Sentinel value | A placeholder number such as -999 or 9999 that stands for missing data but looks real |
| Provenance | The record of where data came from and how it was handled |
| Data provenance | Same idea applied to a dataset: its origin, collection method and changes |
| Lineage | The traced path of transformations from source data to a derived value |
| Derived feature | A feature computed from other fields rather than collected directly |
| Silent upstream change | A change to a source system that alters data without warning to those downstream |
| Datasheet (datasheet for datasets) | A standard document describing a dataset's origin, composition, collection and intended use |
| Data card | A summary document describing a dataset's contents, sources and limits |
| Reproducibility | Being able to get the same result again from the same data and method |
| Row reconciliation | Comparing row counts before and after a step to account for every row |
| Silent drop (silent data loss) | Rows lost without any error or warning, often through a join or filter |
| Anti-join | A join that returns the rows in one table with no match in the other, used to find what was lost |
| Inner join | Keeps only the rows that match in both tables |
| Left join | Keeps every row from the left table and fills in unmatched ones with blanks |
| Full outer join | Keeps every row from both tables, with blanks where there is no match |
| Fan-out | A join that multiplies rows because one key matches several rows on the other side |
| Uniqueness check | Confirming that a field or set of fields has no repeated values |
| Duplicate | A record that appears more than once |
| Exact duplicate | A record identical to another in every field |
| Near-duplicate | A record that is almost the same as another but differs slightly in text or format |
| Deduplication | Finding and removing duplicate records |
| Composite key | A key made from more than one column that is unique only in combination |
| Grain (unit of analysis) | What one row represents, such as one patient or one visit |
| Sampling frame | The list from which a sample is drawn |
| Target population | The group the conclusion is meant to describe |
| Undercoverage | Part of the target population is missing from the sampling frame |
| Coverage error | Error because the frame does not match the target population |
| Coverage bias | Bias because some groups are missing from the frame and differ from the others |
| Administrative data | Records collected to run a service, not for research, and reused for analysis |
| Proxy | A measurable stand-in for something that cannot be measured directly |
| Proxy feature | A feature that stands in for another quantity, often one not meant to be used |
| Proxy variable | A variable that correlates with a protected or unmeasured attribute and so can carry its influence |
| Missing completely at random (MCAR) | Missingness unrelated to any value, observed or not |
| Missing at random (MAR) | Missingness depends only on observed variables |
| Missing not at random (MNAR) | Missingness depends on the missing value itself |
| Complete-case analysis (listwise deletion) | Dropping every row that has any missing value |
| Mean imputation | Filling missing values with the average, which understates variance |
| Multiple imputation | Filling missing values several times with random draws, then combining the analyses |
| Imputation | Filling in missing values with estimated ones |
| Missingness indicator | A variable flagging whether a value was missing, so a model can use the pattern |
| Differential missingness | Missingness rates that differ across groups |
| Stratified check | Running a data check separately within each subgroup |
| Unit nonresponse | A sampled person gives no response at all |
| Item nonresponse | A respondent answers some questions but skips others |
| Nonresponse bias | Bias because those who respond differ from those who do not |
| Response bias | Bias from respondents giving inaccurate answers |
| Selection bias | Bias because the way cases entered the data is related to the outcome |
| Self-selection | People deciding for themselves whether to be in the sample |
| Voluntary response sample | A sample made of people who chose to respond, which tends to over-represent strong opinions |
| Probability sample | A sample where every unit has a known, nonzero chance of selection |
| Inclusion probability | The chance that a given unit is selected into the sample |
| Sampling bias | A sample that systematically differs from the population it is meant to represent |
| Post-stratification | Reweighting a sample so its subgroup shares match known population shares |
| Inverse probability weighting | Weighting each case by the inverse of its probability of being observed |
| Survivorship bias | Studying only the cases that survived a selection process, so failures are missing |
| Selection on the outcome | Selecting cases using the outcome you want to study, which distorts relationships |
| Collider | A variable caused by two others; conditioning on it creates a false association between them |
| Berkson's paradox | A false negative association between two traits that appears when selection depends on either |
| Selective labels | Outcomes are observed only for cases that received a decision, such as loans that were approved |
| Reject inference | Estimating what would have happened to rejected cases, to correct for selective labels |
| Extrapolation | Predicting outside the range of the data the model has seen |
| Positivity (overlap) | Every kind of unit has a nonzero chance of both treatment levels, so comparisons are possible |
| Sensitivity analysis | Testing how much conclusions change when assumptions are changed |
| Measurement bias | Systematic error in how a quantity is measured |
| Label | The value a model is trained to predict |
| Label noise | Errors in the labels |
| Signal-to-noise | How strong the real pattern is compared with random variation |
| Inter-annotator agreement | How closely different labelers agree on the same items |
| Observed agreement | The raw share of items on which raters agree |
| Chance agreement | The agreement that would be expected if raters labelled at random |
| Cohen's kappa | Agreement corrected for chance: (observed - chance) / (1 - chance) |
| Adjudication | Having a third reviewer or expert settle labels the annotators disagree on |
| Soft label | A label expressed as a probability or distribution over classes |
| Hard label | A single definite class label |
| Gold-standard item | An item with a trusted, expert-verified label used to check labelers |
| Construct | The abstract concept you want to measure, such as intelligence or risk |
| Operationalization | Turning a construct into a concrete measurement procedure |
| Construct validity | How well a measure captures the construct it claims to |
| Proxy label | A label that stands in for the true outcome of interest |
| Data leakage | Information that would not be available at prediction time getting into training or evaluation |
| Target leakage | A feature that contains or is derived from the outcome being predicted |
| Entity leakage | The same person or entity appearing in both training and test data |
| Preprocessing leakage | Fitting a step such as scaling or imputation on all the data before splitting |
| Temporal leakage | Using information from the future to predict the past |
| Group split | Splitting data so that all rows from one group go to the same side |
| Temporal split (out-of-time split) | Training on earlier data and testing on later data |
| Ablation | Removing one component or feature to see how much it contributed |

## Robustness and distribution shift

| Term | Meaning |
|---|---|
| Robustness | A model keeping its performance when inputs are noisy, changed or shifted |
| Distribution shift | The data a model sees in use differ in distribution from its training data |
| In-distribution vs out-of-distribution | In-distribution inputs resemble the training data; out-of-distribution inputs do not |
| In-distribution evaluation | Testing on data drawn from the same distribution as training |
| OOD detection | Flagging inputs that appear unlike the training data |
| Covariate shift vs concept drift | In covariate shift the inputs change while the input-to-label relationship stays; in concept drift that relationship itself changes |
| Label shift (label (prior) shift, prior shift, prior probability shift) | The share of each class changes while the class-conditional input distribution stays |
| Concept shift | The relationship between inputs and the label changes |
| Data drift | The distribution of the input data changes over time |
| Nonstationarity | The statistical properties of the data change over time |
| Stationarity | The statistical properties of the data stay the same over time |
| Population stability index (PSI) | A score of how much a variable's distribution has moved between two periods |
| Kolmogorov-Smirnov test | A test of whether two samples come from the same distribution, based on the largest gap in their cumulative distributions |
| Domain classifier | A classifier trained to tell old data from new; if it succeeds, the distributions differ |
| Two-sample test | A statistical test of whether two samples come from the same distribution |
| Importance weighting | Reweighting training examples so they resemble the new distribution |
| Support overlap | Whether the new data fall in regions where training data also exist |
| Label delay | The wait before the true outcome becomes known, which delays performance monitoring |
| Feedback loop | The model's decisions change the data that it later learns from |
| External validation | Testing a model on data from a different source, place or time |
| External validity | Whether a result holds in settings other than the one studied |
| Shortcut learning | A model relying on an easy cue that works in training but not in general |
| Slice-based evaluation | Measuring performance on defined subsets of the data |
| Worst-group accuracy | The accuracy on the group where the model does worst |
| Subpopulation mix | The proportions of the different subgroups in the data |
| Group-robust objective | A training goal that focuses on the worst-performing group instead of the average |
| Reweighting | Giving examples different weights in training or analysis to correct imbalance |
| Resampling | Changing the dataset by repeatedly drawing from it, for example to balance classes |
| Oversampling | Duplicating or synthesising examples of a rare class |
| Stress test | Evaluating a system under extreme or unusual conditions |
| Random noise | Unstructured random changes added to an input |
| Natural corruption | Realistic degradation such as blur, weather or compression |
| Perturbation | A small deliberate change to an input |
| Adversarial example | An input altered slightly, often imperceptibly, to make a model err |
| Adversarial robustness | A model's resistance to adversarial examples |
| Perturbation budget (epsilon) | The largest change an attacker is allowed to make to an input |
| L2 norm | The straight-line (Euclidean) size of a change |
| L-infinity norm (L∞ norm) | The largest change to any single input feature |
| Linearity hypothesis | The idea that adversarial vulnerability comes from models behaving nearly linearly in high dimensions |
| Gradient-sign step | A one-step attack moving each input feature by epsilon in the direction that increases the loss |
| Projected gradient descent | An iterative attack that takes repeated gradient steps and projects back into the allowed budget |
| Random restarts | Running the attack from several random starting points to find a worse case |
| Worst-case perturbation | The allowed change that does the most damage to the model |
| Threat model | A statement of what an attacker knows, can do and wants |
| White-box | The attacker knows the model's internals and gradients |
| Black-box | The attacker can only send inputs and see outputs |
| Query-based attack | A black-box attack that learns from many queries to the model |
| Transfer attack | An attack made on one model that also works against another |
| Surrogate model | A stand-in model used to approximate another model's behaviour |
| Targeted attack | An attack aiming for a specific wrong output |
| Untargeted attack | An attack aiming only for any wrong output |
| Gradient masking | Making gradients useless to an attacker without making the model truly robust |
| Adaptive attack | An attack designed with knowledge of the defence, which is the proper test of a defence |
| Upper bound | A value the true quantity cannot exceed; an attack gives an upper bound on robust accuracy |
| Lower bound | A value the true quantity is at least as large as; a certificate gives a lower bound on robust accuracy |
| Certified accuracy | The share of examples proven to be correct for every allowed perturbation |
| Sound verifier | A verifier whose "robust" answers are always correct |
| Incomplete verifier | A verifier that may answer "unknown" for cases that are in fact robust |
| Formal verification | Proving mathematically that a property holds for all allowed inputs |
| Randomized smoothing | Making predictions from many noisy copies of the input to obtain a certified radius |
| Certified radius | The size of change within which the prediction is proven not to change |
| Adversarial training | Training on adversarial examples to improve robustness |
| Min-max | An objective where the defender minimises the loss that the attacker maximises |
| Robust overfitting | Robust accuracy on the test set getting worse with longer adversarial training |
| Clean accuracy | Accuracy on unaltered inputs |
| Robust accuracy | Accuracy on inputs altered within the allowed perturbation budget |
| Robustness profile | Robust accuracy reported across a range of perturbation sizes |
| Decision boundary | The surface in input space where the model's prediction changes class |
| Boundary tilting | The decision boundary leaning toward directions that make it easy to cross with small changes |
| Margin | The distance from an input to the decision boundary |
| Causal feature | A feature that actually influences the outcome |
| Feasibility constraint | A rule limiting changes to those that are realistic or possible |
| Monotonicity constraint | A requirement that the output moves in only one direction as an input increases |
| Shadow mode | Running a new system on live data without acting on its outputs |
| Population mismatch | The data used in evaluation do not match the population where the system is used |
| Generalization | A model's performance on data it was not trained on |

## Explainability

| Term | Meaning |
|---|---|
| Explanation | An account of why a model produced a particular output |
| Interpretability | How well a person can understand how a model works or why it decides |
| Transparency | How much of a model, its data and its process is open to inspection |
| Interpretability vs explanation vs transparency | Interpretability is understanding the model, an explanation is an account of one output, and transparency is access to the workings |
| Interpretable by design (intrinsic) | A model simple enough to read directly, such as a short rule list or linear model |
| Post-hoc | Applied after the model is trained, to a model that was not built to be understood |
| Post-hoc rationale | A justification generated after the answer, which may not reflect how it was reached |
| Model-agnostic vs model-specific | A model-agnostic method works on any model through inputs and outputs; a model-specific one uses a model's internals |
| Local vs global explanation | A local explanation covers one prediction; a global explanation covers the model's behaviour overall |
| Faithful (unfaithful) | An explanation is faithful if it reflects what the model actually computed |
| Faithfulness vs plausibility | Faithfulness is matching the model's real reasoning; plausibility is sounding reasonable to a person |
| Plausibility (counterfactual) | A counterfactual is plausible if it describes a realistic case |
| Fidelity vs accuracy | Fidelity is how well a surrogate matches the original model; accuracy is how well a model matches the truth |
| Fidelity | How closely a surrogate's predictions match the model it explains |
| Surrogate model | A simpler model trained to mimic a complex one so that it can be inspected |
| Local surrogate | A simple model fitted around one prediction to explain it, as LIME does |
| Global surrogate | A simple model fitted to the whole model's predictions to approximate its behaviour |
| LIME | A method that explains a single prediction with a simple model fitted to perturbed nearby inputs |
| Scaffolding (fooling perturbation explainers) | Building a model that detects explanation probes and behaves innocently on them, hiding its real behaviour |
| Feature attribution (attribution) | Assigning each input feature a share of a prediction |
| Feature importance | A measure of how much a feature matters to a model's predictions |
| Feature importance vs causal effect | Importance shows what a model relies on; it does not show what would change the real outcome |
| Causal effect | How the outcome would change if a variable were intervened on |
| Correlation vs causation | Two variables moving together does not show that one causes the other |
| Permutation importance | The drop in performance when one feature's values are shuffled |
| Impurity-based importance | A tree model's importance score based on how much each feature reduces node impurity |
| High-cardinality bias | Impurity-based importance favouring features with many distinct values |
| Shapley value | A feature's average marginal contribution over all orders in which features could be added |
| SHAP | A method that explains predictions with Shapley values |
| TreeSHAP | An efficient exact algorithm for Shapley values in tree models |
| KernelSHAP | A model-agnostic, sampling-based approximation of Shapley values |
| Mean absolute Shapley value | A feature's global importance, the average size of its Shapley values across examples |
| Reference (baseline) | The input or distribution that a feature's contribution is measured against |
| Efficiency | The Shapley property that the attributions add up to the prediction minus the reference prediction |
| Symmetry | The Shapley property that features contributing equally get equal attributions |
| Dummy | The Shapley property that a feature with no effect gets zero attribution |
| Additivity | The Shapley property that attributions for a sum of models are the sum of attributions |
| Value function | The function giving the model's output for a subset of features |
| Marginal (interventional) vs conditional (observational) value function | The marginal (interventional) version averages over independent feature values; the conditional (observational) version respects correlations |
| Coalition | A subset of features considered together when computing Shapley values |
| Monte Carlo (sampling estimate) | Approximating an exact quantity by random sampling |
| Multicollinearity | Features strongly correlated with each other, which makes individual effects hard to separate |
| Interaction | An effect that depends on two or more features together rather than each separately |
| Partial effect (coefficient) | The change in the outcome for a one-unit change in a feature with the others held fixed |
| Partial dependence plot | A plot of the average prediction as one feature varies |
| ICE curve | An individual conditional expectation curve, showing how one example's prediction changes as one feature varies |
| Integrated gradients | An attribution method that accumulates gradients along a path from a baseline to the input |
| Completeness | The property that attributions sum to the difference between the output and the baseline output |
| Gradient saturation | Gradients near zero where the output is flat, so they understate a feature's importance |
| Saliency map | An image showing which input pixels most affect the output, usually from gradients |
| Model randomization test | A sanity check: explanations should change when the model's weights are randomized |
| Data randomization test | A sanity check: explanations should change when the model is trained on shuffled labels |
| Deletion test | Removing the features flagged as important and measuring how much the prediction drops |
| Out-of-distribution | Inputs unlike the training data, where model behaviour and explanations are unreliable |
| Counterfactual explanation | The smallest change to an input that would change the model's decision |
| Actionability | Whether a counterfactual involves changes the person can actually make |
| Recourse | What a person can do to obtain a different decision |
| Proximity | How close a counterfactual is to the original input |
| Sparsity | How few features a counterfactual changes |
| Instability | Small input changes producing very different explanations |
| Jaccard similarity | The size of the overlap of two sets divided by the size of their union |
| Rashomon effect | Many different models fit the data about equally well but explain it differently |
| Outcome audit | Checking a system's real results rather than its stated reasons |
| Chain-of-thought | A language model's written step-by-step reasoning before its answer |
| Chain-of-thought faithfulness | Whether the stated reasoning is what actually produced the answer |
| Intervention test | Changing something and seeing whether the output changes, to test whether it matters |
| Rationalization | A plausible-sounding reason given after the fact that did not cause the output |
| Linear probe | A simple linear classifier trained on a model's internal activations to test what they encode |
| Decodability | Whether a property can be read out of a model's internal representation |
| Control task | A task with random labels used to check that a probe is not just memorizing |
| Selectivity | A probe's accuracy on the real task minus its accuracy on the control task |
| Simulatability | Whether a person can step through the model and predict its output |
| Adequacy | Whether an explanation is enough for its purpose |
| Purposes of attribution (debugging, trust, recourse) | The main uses of attributions: finding model faults, deciding how far to rely on a model, and advising people |
| Scorecard | A simple points-based model that a person can compute by hand |
| Contestability | The ability of an affected person to challenge a decision |
| Soft vs hard delete | A soft delete marks a record as removed but keeps it; a hard delete removes it permanently |
| Label influenced by treatment | An outcome label shaped by the very decision being studied, so the data cannot show what would have happened otherwise |

## Bias in the pipeline

| Term | Meaning |
|---|---|
| Representation bias | The data under-represent some groups relative to where the model is used |
| Label bias | Labels systematically differ from the truth for some groups |
| Historical bias | Past inequity that is reflected accurately in the data and carried into the model |
| Aggregation bias | One model fitted to a mixed population fits no subgroup well |
| Omitted variable | A relevant variable left out of the analysis, which can bias the estimated effects |
| Differential measurement bias (differential measurement error) | A measure that is more error-prone, or biased differently, for some groups |
| Redundant encoding | A protected attribute being recoverable from several other features |
| Fairness through unawareness | Excluding the protected attribute from the model, which does not remove bias carried by proxies |
| Protected attribute | A characteristic, such as race or sex, that law or policy says must not be the basis of decisions |
| Disaggregated evaluation | Reporting metrics separately for each group instead of one pooled figure |
| Pooled metric | A metric computed over everyone together, which can hide group gaps |
| Intersectional evaluation (intersectional analysis, intersectional subgroup) | Evaluating subgroups defined by combinations of attributes, such as race and sex together |
| Matching | Pairing treated and untreated units with similar characteristics to compare them |
| Confounding by indication | Treatment is given to sicker people, so the treatment looks harmful or ineffective |
| Mediator | A variable on the causal path from cause to outcome |
| Standardisation | Adjusting results to a common population mix so that groups are comparable |
| Reverse causation | The outcome causes the supposed cause rather than the other way round |
| Observational equivalence | Different causal stories producing the same observed data, so the data cannot tell them apart |
| Ladder of causation | Pearl's three levels: association, intervention, counterfactual |
| Association | The level of seeing: how variables are related in observed data |
| Intervention | The level of doing: what happens if a variable is set by action |
| Counterfactual | The level of imagining: what would have happened had things been different |
| Do operator | Notation do(X = x) for setting a variable by intervention rather than observing it |
| Average treatment effect | The average difference in outcome between everyone being treated and no one being treated |
| Fundamental problem of causal inference | Each unit's outcome can be seen under only one treatment, never both |
| Exchangeability | Treated and untreated groups would have had the same outcomes had they been treated alike |
| Monotonicity | The treatment never hurts anyone, or never helps anyone, in the assumed direction |
| Probability of necessity | The probability that the outcome would not have occurred without the cause, given that both occurred |
| Partial identification | Reporting a range of possible effects when the assumptions needed for a single value do not hold |
| Disparity vs bias | A disparity is an observed gap between groups; bias is a systematic error or unfairness, which may or may not explain it |
| Feedback loop (bias) | Model decisions shape future data so that the original bias is reinforced |
| Pre-processing | A fairness intervention that changes the training data before the model is fit |
| In-processing | A fairness intervention built into the model's training objective |
| Post-processing | A fairness intervention that adjusts the model's outputs after training |
| Group-specific threshold (group-specific cutoffs) | Using different decision thresholds for different groups to equalise a chosen metric |
| Reweighing | A pre-processing method that weights examples so group and label are statistically independent |
| Empirical risk minimisation | Training a model to minimise average loss over the whole training set |
| Worst-group error | The error rate in the group with the highest error |
| Minimax | Minimising the worst-case loss across groups |
| Funnel analysis | Tracking how outcomes change at each stage of a multi-step process to see where gaps arise |
| Correspondence test | A field experiment sending matched applications that differ only in a group signal, to detect discrimination |
| Sign test | A test that counts which of paired outcomes is larger, using only the direction of each difference |
| Model card | A standard document reporting a model's intended use, performance by group and limits |
| External audit | An evaluation by an independent party, not the builder |

## Fairness metrics

| Term | Meaning |
|---|---|
| Fairness criterion | A precise, measurable condition, such as equal true positive rates, that counts as fair |
| Fairness trade-off (fairness-accuracy trade-off) | Imposing a fairness criterion can reduce overall accuracy |
| Trade-off frontier | The set of best achievable combinations of accuracy and fairness |
| Pareto-optimal | A point where neither measure can improve without making the other worse |
| Demographic parity (statistical parity) | Each group receives the favourable outcome at the same rate |
| Selection rate | The share of a group that receives the favourable outcome |
| Favorable outcome | The decision that benefits the person, such as approval or hiring |
| Disparate impact ratio (adverse impact ratio) | A group's selection rate divided by the highest group's selection rate |
| Four-fifths rule | A guideline treating a selection-rate ratio below 0.8 as evidence of adverse impact |
| Equal opportunity | Equal true positive rates across groups |
| Equalized odds | Equal true positive rates and equal false positive rates across groups |
| Predictive parity | Equal positive predictive value across groups |
| Accuracy parity | Equal overall accuracy across groups |
| Calibration within groups | Predicted probabilities mean the same thing in each group: among those scored p, a share p are positive in every group |
| Impossibility result | Except in trivial cases, calibration and equal error rates cannot hold together when base rates differ |
| Perfect classifier | A classifier that makes no errors, which satisfies all the criteria at once |
| Trivial classifier | A classifier that gives everyone the same result, which satisfies some criteria uselessly |
| Disparate treatment | Treating people differently because of a protected attribute |
| Disparate treatment vs disparate impact | Disparate treatment is intentional use of the attribute; disparate impact is a neutral rule with unequal effects |
| Business necessity | A defence that a practice with disparate impact is job-related and required |
| Less discriminatory alternative | A different practice that meets the same goal with less disparity |
| Adversarial debiasing | Training a model while an adversary tries to predict the protected attribute from its output |
| Individual fairness | Similar individuals should receive similar outcomes |
| Lipschitz condition | A bound saying outcomes may differ by no more than a constant times the distance between individuals |
| Similarity metric | The definition of which individuals count as similar |
| Counterfactual fairness | A decision is fair if it would be the same in a world where the person's protected attribute were different |
| Causal graph | A diagram of which variables directly cause which |
| Path-specific fairness | Fairness that blocks the influence of the protected attribute along some causal paths but not others |
| Background factors | Unobserved variables, held fixed when a counterfactual is evaluated |
| Generalized entropy index | An inequality measure that can be split into between-group and within-group parts |
| Between-group component | The part of total inequality that comes from differences between groups |
| Within-group component | The part of total inequality that comes from differences inside groups |
| Tolerance | The size of a gap in a metric that is accepted as equal |
| True-positive rate | The share of actual positives that are predicted positive; the same as recall |

## Wrong word, right word

- "Make the model more accurate so it's fair" needs a **fairness criterion** such as demographic parity or equalized odds. Accuracy is overall correctness and says nothing about groups.
- "Check the data is clean" should be named checks: **schema check**, missingness, **duplicates** and **outliers**. A dataset that passes validation can still be wrong.
- "The model is 90 percent confident, so it is 90 percent accurate" confuses **confidence** with **accuracy**. They match only if the model is **calibrated**.
- "The result is 95 percent likely to be true" is a claim about a **posterior probability**. A **p-value** is the probability of data this extreme if the null were true.
- "The 95 percent confidence interval has a 95 percent chance of containing the truth" is the wrong reading for one computed interval. The **confidence level** describes the procedure over repeated samples. A **credible interval** gives the probability statement.
- "The data drifted" should say which kind: **covariate shift** (inputs change), **label shift** (class mix changes) or **concept drift** (the input-to-label relationship changes).
- "We tested it on the test set, so it is validated" mixes up **verification** (built to the specification) and **validation** (meets the real need), and a reused test set can suffer **test-set contamination**.
- "The model does not use gender, so it is unbiased" ignores **proxy variables**. **Fairness through unawareness** does not remove bias carried by correlated features.
- "The feature is important, so changing it will change the outcome" confuses **feature importance** with **causal effect**. Importance describes the model, not the world.
- "The explanation sounds right, so it is accurate" confuses **plausibility** with **faithfulness**. A faithful explanation reflects what the model computed.
- "The model is robust" needs a **threat model** and a **perturbation budget**. An attack result is an **upper bound** on robust accuracy; a certificate is a **lower bound**.
- "We checked many things and one was significant" is **p-hacking** unless a **multiple comparisons** correction such as **Bonferroni** or **Benjamini-Hochberg** was applied.
