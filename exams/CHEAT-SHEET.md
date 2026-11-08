# INFO 7375 Computational Skepticism for AI: exam cheat sheet

**Status: DRAFT v0.1, 2026-11-08, for TA review.** Written by Claude from the jargon glossary and the question bank. **The instructor has not signed it off.** Every definition below is taken from the glossary; the few lines that add general knowledge are marked *(not checked)*.

Full term list: [GLOSSARY-jargon-midterm.md](/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/exams/GLOSSARY-jargon-midterm.md). Practice: [practice-exams](/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/exams/practice-exams) and the [question bank](/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/exams/question-bank/INDEX.md).

## Executive summary

**What this is.** One sheet of the words and numbers the exam leans on, grouped by chapter. The exam is a language test: if you can name the exact term, you can tell a model exactly what to check. "Check that the model is good" is a guess; "report sensitivity and specificity at a 0.5 threshold with a Wilson interval" is a claim.

**How to use it.** Read the ten-second version, then the "tell apart" table: most wrong answers come from swapping two near-neighbour terms. For any line you cannot say in your own words, look it up in the glossary, then take a practice exam.

**What the exam asks.** Multiple-answer: five statements per question, each true or false on its own, 1 point each. A statement is not false because it sounds strong; decide whether it is true. Strong words (always, never, proves) are often the trap, not always.

**Where it stops.** Foundations and chapters 1 to 7. Chapters 8 to 13 are not in the bank yet.

## The ten-second version

- Skepticism tests a claim and keeps what survives; cynicism rejects without testing.
- A claim you cannot falsify, you cannot test. Name the observation that would prove it wrong.
- A test set is used once. Reusing it to choose models is adaptive overfitting.
- A p-value is P(data this extreme | null), not P(hypothesis | data).
- A 95% interval describes the procedure over repeated samples, not a 95% chance for this one interval.
- Confidence is not accuracy; they match only if the model is calibrated.
- Valid is not correct: data can pass every rule and still be false.
- Say which drift: covariate shift, label shift or concept drift.
- Feature importance describes the model, not the world.
- An explanation can be plausible and unfaithful.
- Fairness needs a named criterion; accuracy says nothing about groups.
- When a measure becomes a target it stops being a good measure (Goodhart).

## Numbers and formulas to know

| Name | Statement |
|---|---|
| Bayes (odds form) | posterior odds = prior odds x likelihood ratio |
| Odds | p / (1 - p); log-odds = log(p / (1 - p)) |
| PPV (precision) | of those flagged, the share truly positive; depends on the base rate |
| Sensitivity / specificity | share of true positives caught / share of true negatives cleared |
| False positive rate | 1 - specificity; false negative rate = 1 - sensitivity |
| Mean squared error | variance + squared bias |
| Standard error | SD of a statistic over repeated samples; shrinks as n grows |
| Empirical rule | about 68 / 95 / 99.7 percent within 1 / 2 / 3 SD (normal) |
| Chebyshev | at most 1/k^2 of values lie more than k SD from the mean, any distribution |
| IQR rule | outlier if beyond 1.5 IQR past the first or third quartile |
| Rule of three | zero events in n trials: approximate 95% upper bound is 3/n |
| Bonferroni | divide the significance level by the number of tests (controls family-wise error) |
| Power | 1 - Type II error rate |
| Cohen's kappa | (observed - chance) / (1 - chance) |
| Brier score | mean squared gap between predicted probability and the 0/1 outcome; lower is better |
| Expected calibration error | average gap between confidence and accuracy across bins |
| Four-fifths rule | selection-rate ratio below 0.8 is evidence of adverse impact |
| AUC | chance a random positive scores above a random negative |
| Jaccard | overlap / union of two sets |

## Tell apart (most wrong answers are here)

| Pair | The difference |
|---|---|
| Skepticism vs cynicism | tests then accepts what survives / rejects without testing |
| Verification vs validation | built to the spec / meets the real need |
| Claim vs evidence; report vs state | what was said / what you can confirm; what happened / what is true now |
| Reproducible vs accurate | same result again / true result |
| Statistical vs practical significance | unlikely under the null / large enough to matter |
| Confidence interval vs credible interval | procedure covers the truth in 95% of repeats / posterior probability of the parameter |
| Prediction interval vs confidence interval | one future value (wider) / the mean |
| FWER vs FDR | at least one false positive / share of rejections that are false |
| Exploratory vs confirmatory | generates hypotheses / tests one stated in advance |
| Accuracy vs calibration vs discrimination | share correct / stated probability matches frequency / ranks positives above negatives |
| Overconfident vs underconfident | stated confidence above / below actual correctness |
| Validity vs correctness | satisfies the rules / is true |
| Provenance vs lineage | where data came from and who handled it / the transformations applied since |
| Schema check vs semantic check | names and types / values make sense |
| MCAR / MAR / MNAR | missingness unrelated to anything / depends on observed variables / depends on the missing value |
| Selection bias vs measurement bias | how cases entered / how values were recorded |
| Covariate shift vs label shift vs concept drift | P(x) changes / P(y) changes / P(y given x) changes |
| Clean vs robust accuracy | unaltered inputs / inputs within the perturbation budget |
| Attack vs certificate | upper bound on robust accuracy / lower bound |
| White-box vs black-box | knows internals and gradients / sees only inputs and outputs |
| Faithful vs plausible explanation | reflects what the model computed / sounds reasonable |
| Fidelity vs accuracy | surrogate matches the model / model matches the truth |
| Local vs global explanation | one prediction / overall behaviour |
| Importance vs causal effect | what the model relies on / what would change the outcome |
| Permutation vs impurity importance | drop when a feature is shuffled / tree node impurity (biased to many-valued features) |
| Disparity vs bias | an observed gap / a systematic error or unfairness |
| Disparate treatment vs disparate impact | uses the attribute / neutral rule, unequal effect |
| Demographic parity vs equal opportunity vs equalized odds | equal selection rate / equal true positive rate / equal TPR and FPR |
| Predictive parity vs calibration within groups | equal PPV / probabilities mean the same in each group |
| Pre- vs in- vs post-processing | change the data / change the training objective / adjust outputs |
| Fairness through unawareness | drops the attribute; proxies still carry it |

## By chapter

**Foundations.** Conditional probability, chain rule, independence (P(A and B) = P(A)P(B)); base rate fallacy and the transposed conditional (prosecutor's fallacy); central limit theorem needs finite variance; Cauchy has no mean, so averages never settle; Anscombe's quartet means plot your data; Simpson's paradox is a reversal when groups merge; correlation zero does not mean independent; precision vs accuracy; aleatoric (irreducible) vs epistemic (reducible with data) uncertainty.

**1. The skeptic's toolkit.** Falsifier, scope, assumption, rival hypotheses, underdetermination. Cherry-picking, moving the goalposts, circular reporting. Held-out data: validation tunes, test is for the final estimate once. Benchmark contamination. LLM-as-judge shows self-preference bias. Goodhart and reward hacking. Mutation testing checks that tests can fail. Solve-verify asymmetry: checking is cheaper than producing. Human-in-the-loop only helps if approval is real (no rubber-stamping, segregation of duties). Least privilege.

**2. Probability, uncertainty, confidence.** Null, p-value, Type I and II errors, power. No evidence of an effect is not evidence of none (use an equivalence test). Multiple comparisons: Bonferroni and Holm control FWER, Benjamini-Hochberg controls FDR. P-hacking, HARKing, preregistration, winner's curse. Calibration tools: reliability diagram, ECE, Brier score, log loss. Proper scoring rules reward honest probabilities. Temperature scaling and recalibration adjust the probabilities; temperature scaling leaves the ranking (and so AUC) unchanged *(not checked)*.

**3. Data validation and provenance.** Schema, type, range and cross-field checks; referential integrity and orphans; sentinel values (-999 looks real). Silent drops in joins; anti-join finds what was lost; fan-out multiplies rows. Coverage error and undercoverage; nonresponse bias; selection on the outcome; survivorship; Berkson's paradox; selective labels and reject inference. Label noise: Cohen's kappa. Leakage kinds: target, entity, preprocessing, temporal. Group split and temporal split prevent them.

**4. Robustness and distribution shift.** Shift types above. Detect with PSI, KS test or a domain classifier; correct with importance weighting. Label delay slows monitoring. Adversarial examples need a threat model and a perturbation budget (L2 vs L-infinity). FGSM-style one step vs PGD with restarts. Gradient masking is false robustness; test with adaptive attacks. Adversarial training: min-max, robust overfitting. Randomized smoothing gives a certified radius. Report worst-group accuracy and slices.

**5. Explainability.** Interpretable by design vs post-hoc. LIME is a local surrogate; scaffolding can fool perturbation-based explainers. Shapley properties: efficiency, symmetry, dummy, additivity. TreeSHAP is exact for trees; KernelSHAP approximates. Marginal vs conditional value function. Sanity checks: model and data randomization tests; deletion test. Counterfactual explanation: proximity, sparsity, actionability, recourse. Rashomon effect: many models fit equally, explain differently. Chain-of-thought can be unfaithful rationalization; test by intervention. Probes need a control task (selectivity).

**6. Bias in the pipeline.** Representation, label, historical and aggregation bias; omitted variables; differential measurement error; redundant encoding and proxies. Disaggregated and intersectional evaluation instead of a pooled metric. Confounder, mediator, collider; confounding by indication. Ladder of causation (association, intervention, counterfactual); do operator; average treatment effect; fundamental problem of causal inference; exchangeability and positivity. Feedback loops. Model cards and external audits.

**7. Fairness metrics.** Criteria above. Impossibility result: calibration and equal error rates cannot both hold when base rates differ, except trivially. Accuracy-fairness trade-off and Pareto frontier. Individual fairness (similar people, similar outcomes; Lipschitz). Counterfactual fairness uses a causal graph; path-specific fairness blocks some paths. Generalized entropy index splits inequality into between-group and within-group parts.

## Wrong word, right word

- "Make it more accurate so it's fair" needs a fairness criterion.
- "Check the data is clean" means named checks: schema, missingness, duplicates, outliers.
- "90 percent confident so 90 percent accurate" needs calibration.
- "The data drifted" says which kind.
- "Tested on the test set so it is validated" mixes verification and validation, and a reused test set is contaminated.
- "It does not use gender so it is unbiased" ignores proxies.
- "The model is robust" needs a threat model and a budget.
- "We checked many things and one was significant" is p-hacking without a multiplicity correction.

## What you will not be asked

Chapters 8 to 13 are not covered by the bank. **Open conflict for the instructor:** the separate causal-inference glossary (`docs/exam-glossary.md` in this repo) says none of its terms is on the exam and lists only a few causal ideas (confounders, observational data, controlling for a variable, randomization, treatment effect). The question bank, and so this sheet, also tests ladder of causation, do operator, exchangeability, positivity and similar terms in chapter 6. Decide which list is right and trim one of them.
