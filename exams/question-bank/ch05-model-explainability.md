# Chapter 5: Model explainability

## MA-ch05.1

A bank reviews four credit-scoring setups: a sparse logistic regression, a depth-3 decision tree, a boosted ensemble explained afterwards with Shapley values, and a neural network explained afterwards with LIME. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A shallow decision tree needs a post-hoc method before the path to a decision can be read.
- [ ] B. A post-hoc explanation is a faithful description of the model by definition.
- [ ] C. A sparse linear model is interpretable by design, because its structure shows how each input moves the score.
- [ ] D. Computing Shapley values for the boosted ensemble makes it interpretable by design.
- [ ] E. LIME is a post-hoc method, because it explains a model that has already been trained.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The root-to-leaf path of a small tree is the computation, so it is interpretable by design.
- B: Post-hoc explanations approximate the model and can be unfaithful, unstable or off target.
- C: The explanation is the model itself, so no added method is needed.
- D: Shapley values describe an opaque model after training; they do not change its structure.
- E: Post-hoc means the explanation is produced after training from the fitted model.

**Source:** Interpretable by design versus post-hoc

## MA-ch05.2

An analyst holds a trained classifier and asks four questions. Q1: for one applicant, how is the gap between the score and the average score divided among the inputs? Q2: for one denied applicant, what small input change would flip the decision? Q3: near one applicant, what simple model approximates the classifier? Q4: across a held-out set, how much does accuracy fall when one input column is shuffled? Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Q4 is answered by permutation importance, which is a global measure.
- [ ] B. Q2 is answered by a Shapley value.
- [ ] C. Q2 is answered by a counterfactual explanation.
- [ ] D. Q3 is answered by fitting a local surrogate model, as LIME does.
- [ ] E. Q1 is answered by a feature attribution such as a Shapley value.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: Permutation importance is the performance drop when a column is shuffled, summarized over a data set.
- B: Q2 is answered by a counterfactual explanation; Shapley values divide a gap, they do not search for a flip.
- C: A counterfactual explanation names a changed input set that would reverse the decision.
- D: A local surrogate is a simple model fitted to the classifier's outputs near one input.
- E: An attribution splits the difference between one prediction and a reference prediction across inputs.

**Source:** Matching questions to methods

## MA-ch05.3

A reviewer sorts explanation outputs into local and global ones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. An explanation of why one applicant was denied is a local explanation.
- [ ] B. Averaging the absolute Shapley values over a data set turns local attributions into a global importance.
- [ ] C. A partial dependence plot is a local explanation of one customer's prediction.
- [ ] D. The coefficients of a linear model give a global description of how scores are computed.
- [ ] E. An individual conditional expectation curve is a global explanation, because it averages over customers.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: A local explanation concerns a single prediction.
- B: The mean absolute attribution summarizes how large an input's contribution typically is.
- C: A partial dependence plot averages over the data, so it is a global view of an input's effect.
- D: The same coefficients apply to each prediction, so they describe the model as a whole.
- E: An ICE curve is drawn for one instance, so it is local; the partial dependence plot is the average.

**Source:** Local versus global explanation

## MA-ch05.4

A lender explains one denial with Shapley values and finds that the main reason changes when the explanation is measured against a different reference group. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing with approved applicants and comparing with the whole population ask different questions, so the top reason can differ.
- [ ] B. By efficiency, the values sum to the applicant's prediction minus the reference's expected prediction.
- [ ] C. Shapley values depend on the model alone, so the choice of reference leaves the values unchanged.
- [ ] D. The reference is part of what a Shapley explanation says, since the values describe a gap from the reference prediction.
- [ ] E. A different top reason across references is a property of the contrast chosen and does not mean the model changed.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Each reference defines a different contrast, such as why denied rather than approved.
- B: Efficiency fixes the total that the attributions must split.
- C: The value function is built from the reference, so a different reference changes the values.
- D: Shapley values split the difference between the prediction and the expected prediction under the reference.
- E: The model is fixed; the reference supplies the comparison.

**Source:** Reference (baseline) in Shapley values

## MA-ch05.5

A data scientist lists four properties that a feature attribution can satisfy: efficiency, symmetry, dummy and additivity. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Satisfying these properties shows that the attributions are causal effects of the inputs in the world.
- [ ] B. Efficiency means the attributions sum to the prediction minus the baseline prediction.
- [ ] C. Symmetry means an input listed earlier in the feature vector receives the larger value.
- [ ] D. Additivity means the attributions for a sum of two models equal the sums of the models' attributions.
- [ ] E. The dummy property means an input that makes no difference to the output receives a value of zero.

**Key:** A=F B=T C=F D=T E=T

**Why:**

- A: The properties constrain how credit is divided among inputs of the model, not what happens under intervention.
- B: Efficiency says the whole gap is distributed with nothing left over.
- C: Symmetry says inputs that play interchangeable roles receive equal values; list order is irrelevant.
- D: Attribution of a combined model decomposes into the parts' attributions.
- E: A null input earns no credit.

**Source:** Shapley axioms

## MA-ch05.6

A colleague says: "SHAP is the unique attribution method with efficiency, symmetry, dummy and additivity, so it is the correct way to explain a model." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For a fixed value function, the Shapley value is the unique allocation satisfying efficiency, symmetry, dummy and additivity.
- [ ] B. Satisfying the properties makes sampling estimates of Shapley values free of estimation error.
- [ ] C. The value function, meaning how a subset of inputs is valued, is a different choice from the allocation rule.
- [ ] D. The four properties also fix the value function, so the choice between marginal and conditional valuation is already settled.
- [ ] E. The properties show that the attribution answers the question a given user wants answered.

**Key:** A=T B=F C=T D=F E=F

**Why:**

- A: This is the uniqueness result for the allocation rule.
- B: Sampled estimates have variance even though the target quantity is well defined.
- C: Marginal and conditional value functions give different Shapley values under the same rule.
- D: The value function is a separate modeling choice that the axioms do not determine.
- E: Uniqueness of the rule says nothing about whether the explanation fits the purpose.

**Source:** Value function versus allocation rule

## MA-ch05.7

A model predicts 4 times x1 and ignores x2. In the population x2 is an exact copy of x1. A team values a subset of fixed inputs in two ways: the marginal (interventional) way draws unfixed inputs independently of the fixed ones, and the conditional (observational) way draws them given the fixed ones. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The marginal version draws the unfixed inputs given the fixed ones, so it preserves the correlation.
- [ ] B. The marginal version can evaluate the model on input combinations that do not occur in real data.
- [ ] C. With the conditional value function, x2 can receive a nonzero value because it is informative about x1.
- [ ] D. With the marginal value function, x2 receives a value of zero because the model does not read it.
- [ ] E. The two versions give the same values when the inputs are strongly correlated.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: That describes the conditional version; the marginal version ignores the correlation.
- B: Independent draws of correlated inputs produce unrealistic rows.
- C: Conditioning on x2 changes the expected value of x1, so credit leaks to x2.
- D: Breaking the dependence means fixing x2 changes nothing about the output.
- E: Correlation is where the two versions diverge most.

**Source:** Marginal versus conditional value function

## MA-ch05.8

Two columns in a data set are exact copies of each other. Three models, one using the first column, one using the second, and one using both equally, give identical predictions on every row, yet their attributions differ. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Two columns that are exact copies are an extreme case of multicollinearity.
- [ ] B. Shapley values split credit equally between exact copies regardless of what the model reads.
- [ ] C. A model that gives the second copy a value of zero shows that the second copy carries no information about the outcome.
- [ ] D. A zero attribution means the model does not use the input, which differs from the input being uninformative about the outcome.
- [ ] E. Models with identical predictions on the observed rows can receive different attributions.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Multicollinearity means inputs are strongly correlated, so their separate roles are hard to identify.
- B: Credit follows the model's use; a model reading one copy credits that one under the marginal version.
- C: The copy carries the same information; the model simply does not read it.
- D: Use by the model and information in the data are different properties.
- E: Attribution describes how the model reads its inputs, not the predictions alone.

**Source:** Attribution versus information in the data

## MA-ch05.9

A team averages two models' predicted probabilities to form an ensemble and asks how to explain the ensemble. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Averaging two models makes the attributions of the ensemble zero when the members disagree about an input.
- [ ] B. Additivity says the ensemble's attribution equals the larger of the two models' attributions.
- [ ] C. The ensemble's attributions sum to its prediction minus its average prediction, by efficiency.
- [ ] D. The ensemble's attribution for an input equals the average of the two models' attributions, by additivity.
- [ ] E. The ensemble's attributions need a fresh computation because they are not obtainable from the two models' attributions.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Disagreement shrinks the averaged value only partly; it does not cancel to zero.
- B: Additivity is linear combination, not a maximum.
- C: Efficiency applies to the ensemble as it does to each member.
- D: Attributions of a sum or average decompose into the parts' attributions.
- E: Additivity makes the combination direct when the same reference is used.

**Source:** Additivity of attributions

## MA-ch05.10

An analyst computes exact Shapley values by evaluating the model on subsets of the input features, called coalitions. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. TreeSHAP ignores the tree structure and enumerates the coalitions one by one.
- [ ] B. KernelSHAP is model-specific and needs the model's internal weights.
- [ ] C. Exact computation grows exponentially with the number of inputs because the number of coalitions doubles with each added input.
- [ ] D. Averaging marginal contributions over random feature orderings gives a sampling (Monte Carlo) estimate of Shapley values.
- [ ] E. The cost of exact computation grows linearly with the number of inputs.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: TreeSHAP uses the tree structure to avoid full enumeration.
- B: KernelSHAP is model-agnostic and needs only the model's outputs.
- C: With n inputs there are 2 to the power n coalitions.
- D: Permutation sampling trades exactness for speed.
- E: Exact enumeration is exponential, which is why approximations are used.

**Source:** Computing Shapley values

## MA-ch05.11

A model predicts y as s times x, where s is a binary input equal to +1 for half the customers and -1 for the others, independent of x. A partial dependence plot for x comes out flat. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Partial dependence plots show causal effects of x even when x is correlated with other inputs.
- [ ] B. The partial dependence plot is the average of the individual conditional expectation (ICE) curves.
- [ ] C. Opposite-sloping ICE curves can average to a flat partial dependence plot, hiding the interaction with s.
- [ ] D. A flat partial dependence plot shows that x has no influence on individual predictions.
- [ ] E. ICE plots are a global summary and partial dependence plots are local.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: Averaging over unrealistic combinations can mislead, and the plot describes the model, not causation.
- B: PDP is the pointwise mean of the ICE curves.
- C: Averaging conceals heterogeneity across instances.
- D: Individual predictions still change with x; the average hides it.
- E: ICE curves are per instance (local); the PDP averages them (global).

**Source:** Partial dependence versus ICE

## MA-ch05.12

A team reports importance scores for a random forest. Permutation importance is computed on held-out data, and the forest also reports impurity-based importance. One input is a random customer ID, and two other columns are copies of each other. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Impurity-based importance is measured on held-out data.
- [ ] B. With two copies of the same information, shuffling one column can understate reliance, because the model can use the other copy.
- [ ] C. Impurity-based importance can favour inputs with many distinct values, such as an ID, because they offer more candidate splits.
- [ ] D. Permutation importance is the drop in model performance when one input column is shuffled.
- [ ] E. A positive permutation importance shows that the input has a causal effect on the real-world outcome.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: Impurity-based importance totals split gains on the training data.
- B: Correlated inputs share credit, so single-column permutation importance is diluted.
- C: High-cardinality inputs can earn importance by fitting noise.
- D: Shuffling breaks the link between the column and the label, and the score drop measures reliance.
- E: Permutation importance measures reliance by the model, which is predictive, not causal.

**Source:** Permutation versus impurity-based importance

## MA-ch05.13

A subscription company's model for cancellation has a large average Shapley attribution for months since signup. A memo says: "Tenure drives churn, so a free extension will keep new customers." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Predictive importance and causal effect are two names for the same quantity.
- [ ] B. A randomized experiment is uninformative here, because the attributions already measure the effect of an intervention.
- [ ] C. An attribution measures how the model uses an input, not the effect of intervening on that input in the world.
- [ ] D. Checking that the attributions sum to the prediction validates them as a causal effect.
- [ ] E. Confounding is irrelevant to reading an attribution as an effect.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: They are distinct: one is reliance of a model, the other is the response of the outcome to an intervention.
- B: A randomized experiment (A/B test) is the standard way to estimate an intervention's causal effect.
- C: Predictive reliance describes association learned from data.
- D: Efficiency is an accounting property and says nothing about causation.
- E: Confounders can create associations that the model uses without any effect of the input.

**Source:** Feature importance versus causal effect

## MA-ch05.14

A researcher compares plain gradient saliency with integrated gradients (IG) on the model f(x1, x2) equal to the sum x1 + x2 capped at 1, at the input (1, 1) with baseline (0, 0). Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The choice of baseline can change IG attributions, so the baseline is part of the explanation.
- [ ] B. A plain gradient saliency map satisfies completeness.
- [ ] C. A gradient can be near zero where the output is saturated, so a saliency map can miss an input that matters.
- [ ] D. Integrated gradients attribute by integrating the gradient along a path from a baseline to the input.
- [ ] E. Completeness means the attributions sum to the output at the input minus the output at the baseline.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: A different baseline gives a different path and different values.
- B: Plain gradients do not sum to the change in output; IG was built to fix this.
- C: Gradient saturation hides influence in flat regions.
- D: IG accumulates gradient along the straight-line path.
- E: This is the IG counterpart of efficiency.

**Source:** Integrated gradients and completeness

## MA-ch05.15

A team tests a saliency-map method for a chest X-ray classifier by recomputing the maps after replacing the trained weights with random weights (model randomization) and after retraining on shuffled labels (data randomization). The maps barely change. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Maps that stay the same with random weights show the method is insensitive to what the model learned.
- [ ] B. A method whose maps act like an edge detector whichever model is used is describing the image, not the model.
- [ ] C. Passing both randomization tests is sufficient to establish that a method is faithful.
- [ ] D. Radiologists approving the maps is a test of faithfulness.
- [ ] E. Retraining on shuffled labels is called a data randomization test.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: An explanation of a trained model should differ from that of an untrained model.
- B: An explanation insensitive to the model fails the sanity checks.
- C: These are necessary sanity checks, not proof of faithfulness.
- D: Approval measures plausibility, not whether the maps reflect the model.
- E: It checks whether maps depend on the relation between inputs and labels.

**Source:** Sanity checks for saliency maps

## MA-ch05.16

Two attribution methods, P and Q, rank pixels of chest X-rays. A deletion test replaces the top-ranked pixels with a grey value and measures how far the classifier's predicted probability falls, with a random ranking as the comparison. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A large drop after deleting a region shows that the region causes the disease in patients.
- [ ] B. A deletion test measures how plausible the highlighted regions look to a clinician.
- [ ] C. Replacing pixels can create images unlike the training data, so some of the drop can reflect the replacement rather than importance.
- [ ] D. A drop just slightly larger than the random-ranking drop is strong evidence of faithfulness.
- [ ] E. A deletion test removes the highest-ranked features and checks whether the model's output falls.

**Key:** A=F B=F C=T D=F E=T

**Why:**

- A: The drop shows model sensitivity, not a causal role in the patient.
- B: Plausibility is a human rating; a deletion test checks model behavior.
- C: This is the out-of-distribution problem of perturbation-based tests.
- D: The random ranking is the baseline, and a small gap is weak evidence.
- E: A faithful ranking should identify features the model relies on.

**Source:** Deletion test

## MA-ch05.17

Clinicians rate heat maps from two explanation methods for whether the highlighted regions make clinical sense, and one method scores much higher. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A highly plausible explanation is therefore a highly faithful one.
- [ ] B. Faithfulness means the explanation reflects what the model actually computes.
- [ ] C. Tuning an explanation generator to maximize human ratings can raise plausibility while lowering faithfulness.
- [ ] D. Plausibility means the explanation reproduces the model's output on perturbed inputs.
- [ ] E. Faithfulness is measured by asking users to rate how convincing the explanation is.

**Key:** A=F B=T C=T D=F E=F

**Why:**

- A: The two can diverge, for example when a model relies on a cue clinicians find odd.
- B: It is a property relating the explanation to the model.
- C: Optimizing for approval rewards appearance rather than fidelity.
- D: Plausibility is how reasonable the explanation looks to people.
- E: User ratings measure plausibility; faithfulness needs tests such as intervention on inputs.

**Source:** Faithfulness versus plausibility

## MA-ch05.18

A model trained on hospital records assigns lower mortality risk to patients with asthma, and a Shapley explanation gives the asthma input a negative value. In the records, patients with asthma were sent straight to intensive care. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The model has learned a spurious association between asthma and low risk.
- [ ] B. Collecting more data under the same admission policy does not remove the pattern.
- [ ] C. The recorded outcome is partly a consequence of the treatment given, so the label is influenced by clinical decisions.
- [ ] D. The negative attribution shows that asthma protects patients from dying of the infection.
- [ ] E. The attribution can accurately report the model's reliance on asthma while the pattern reflects care decisions, not biology.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: A spurious association is one that does not reflect the outcome's dependence on the input.
- B: The policy keeps producing the same biased outcome records.
- C: Outcomes shaped by interventions can mislead a model about risk.
- D: Attribution reports model reliance, and here the effect is that of treatment policy.
- E: Accurate attribution of a flawed learned pattern is still a flawed pattern.

**Source:** Confounding in the training data

## MA-ch05.19

A lender approves when a score reaches a threshold. A denied applicant is given a counterfactual explanation. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Restricting counterfactuals to changes the person can make is imposing actionability constraints.
- [ ] B. A counterfactual stays valid after the model is retrained, so it works as a promise to the applicant.
- [ ] C. A counterfactual that changes age is called actionable.
- [ ] D. A counterfactual explanation names a change to the inputs that would flip the decision.
- [ ] E. More than one distinct counterfactual can exist for the same applicant.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Feasibility constraints exclude immutable or impossible changes.
- B: The decision boundary can shift when the model is retrained, so the guarantee does not carry over.
- C: A change to a fixed attribute is not actionable; actionability needs changes the person can make.
- D: It answers what would have to be different for another outcome.
- E: Several different changes can cross the threshold, a multiplicity of explanations.

**Source:** Counterfactual explanation

## MA-ch05.20

A lender returns for each denied applicant the nearest approved point, measured by Euclidean distance on standardized features, and calls it a path to approval. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The counterfactual nearest in standardized distance is the cheapest route for the person.
- [ ] B. Recourse is the ability of a person to change a decision through actions they can take.
- [ ] C. Closeness in a counterfactual depends on a chosen distance, such as standardized Euclidean distance or the person's cost.
- [ ] D. A sparse counterfactual changes as many inputs as possible.
- [ ] E. A plausible counterfactual resembles realistic data rather than an unusual combination of inputs.

**Key:** A=F B=T C=T D=F E=T

**Why:**

- A: Statistical distance is not the person's effort or cost.
- B: Recourse needs actionable, feasible changes.
- C: Different metrics rank candidate counterfactuals differently.
- D: Sparsity means the change involves few inputs.
- E: Plausibility asks that the changed point lie where real cases lie.

**Source:** Proximity, plausibility and recourse

## MA-ch05.21

A manager runs LIME twice on the same input of a deterministic classifier and gets different top features. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The overlap of top-k feature sets across runs, such as the Jaccard similarity, quantifies stability.
- [ ] B. Drawing more perturbed samples typically reduces run-to-run variation.
- [ ] C. The variation shows that the classifier returns different outputs for the same input.
- [ ] D. The variation comes from the random sampling of perturbed points, which makes the explanation unstable.
- [ ] E. Picking the run whose features look most sensible is cherry-picking, not a way to settle the disagreement.

**Key:** A=T B=T C=F D=T E=T

**Why:**

- A: Jaccard similarity is the size of the intersection over the size of the union.
- B: A larger sample reduces randomness in the fitted surrogate.
- C: The classifier is deterministic; the sampling inside the explainer varies.
- D: LIME's surrogate is fitted to random samples.
- E: Selecting by plausibility ignores the evidence about instability.

**Source:** Instability of LIME

## MA-ch05.22

LIME fits a weighted linear model to the classifier's outputs on synthetic points sampled around one input, and the weighted R-squared of the fit is low. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A well-fitting local surrogate describes the classifier far from the input.
- [ ] B. Because LIME applies to many kinds of classifier, its coefficients are faithful regardless of the fit.
- [ ] C. Independently perturbed points are guaranteed to resemble real data.
- [ ] D. Widening the neighborhood improves how well a linear model fits the classifier's local behavior.
- [ ] E. A low weighted R-squared signals low fidelity: the surrogate reproduces little of the classifier's local behavior.

**Key:** A=F B=F C=F D=F E=T

**Why:**

- A: The explanation is local; fit near one input says nothing about distant regions.
- B: Model-agnostic does not mean faithful; fit quality must be checked.
- C: Independent perturbation can create unrealistic, out-of-distribution points.
- D: A wider region is more nonlinear; a narrower one fits better but covers less.
- E: Fidelity is how closely the surrogate matches the model near the input.

**Source:** Fidelity of a local surrogate

## MA-ch05.23

A vendor wraps a lending model in a router that sends inputs resembling the synthetic points produced by perturbation-based explainers to a different model, one that ignores a sensitive attribute. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing group-level approval and error rates on real inputs tests the deployed system directly.
- [ ] B. The attack works because Shapley values violate the efficiency property.
- [ ] C. Explanations supplied by the party being audited are an independent audit.
- [ ] D. Perturbation-based explainers such as LIME and KernelSHAP generate off-distribution points, which a detector can recognize.
- [ ] E. The deployed system can behave differently on explainer-generated queries than on real applications, hiding the sensitive attribute.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: Outcome auditing does not depend on the explainer's queries.
- B: Efficiency still holds; the explainer is simply given different queries.
- C: The auditee controls the evidence, so it is not independent.
- D: Independent perturbation produces points that differ from real data.
- E: The explainer is mostly querying the substitute model.

**Source:** Fooling perturbation-based explainers

## MA-ch05.24

A language model's written step-by-step reasoning is shown to auditors as the explanation of its answer. In a test, a hint that a colleague believes the answer is C changes many answers, and the written reasoning rarely mentions the hint. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A rationalization is a justification written to support an answer without being what produced it.
- [ ] B. Adding a biasing hint and checking whether the answer changes is an intervention test of faithfulness.
- [ ] C. Unfaithful reasoning means that a step contains an arithmetic error.
- [ ] D. Whether written reasoning reflects what actually produced the answer is a question of faithfulness.
- [ ] E. Fluent reasoning that supports the final answer is good evidence that those steps produced it.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: It is plausible but not the actual cause.
- B: An intervention reveals influences that the text does not report.
- C: Unfaithful means the stated reasons differ from the real causes, even if each step is correct.
- D: Faithful reasoning describes the real causes of the output.
- E: Fluency shows the text is coherent, not that it is causal.

**Source:** Faithfulness of written reasoning

## MA-ch05.25

Researchers train a linear probe on a language model's internal activations to predict whether a sentence's subject is singular or plural. A control task with random labels per word type gets near-chance accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. High probe accuracy shows that the information is linearly decodable from the activations.
- [ ] B. Selectivity is the gap between probe accuracy on the real task and on the control task.
- [ ] C. A high-capacity probe can learn the task itself, which is why control tasks are used.
- [ ] D. Changing the activations along the probe's direction and checking whether the behavior changes tests whether the information is used.
- [ ] E. High probe accuracy shows that the model uses that information in its output.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Decodability is what a probe measures.
- B: A large gap suggests the representation, not the probe, carries the information.
- C: The control task checks whether the probe is doing the work rather than the representation.
- D: This is a causal intervention on the representation.
- E: Information being present is different from being used; a causal test is needed.

**Source:** Probing

## MA-ch05.26

A pneumonia classifier is trained on images pooled from two hospitals with different pneumonia rates. Each image has a scanner tag identifying the hospital, and the attribution maps highlight the tag. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. High overall accuracy on the pooled data rules out reliance on the tag.
- [ ] B. The hospital acts as a confounder, because it is linked to both the tag and the pneumonia rate.
- [ ] C. Shortcut learning is relying on a cue that correlates with the label in the training data but is not the real signal.
- [ ] D. Evaluating separately within each hospital and on a third hospital is a way to check for reliance on the tag.
- [ ] E. Attribution on the tag proves the classifier uses no information about the lungs.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A tag-driven classifier can score well on pooled data that shares the same confounding.
- B: A confounder affects both the cue and the outcome.
- C: The tag predicts the label through the hospital, not through the lungs.
- D: External validation and stratified evaluation expose shortcut use.
- E: It shows the tag is used, not that nothing else is.

**Source:** Shortcut learning

## MA-ch05.27

An operations agent is told to delete a customer's record. It sets a deleted flag on the row and reports that the record has been deleted, while the database keeps flagged rows and backups keep the row. The customer wanted the data to be unrecoverable. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A confident, fluent report counts as verification of the system's state.
- [ ] B. A precise instruction would say to permanently erase the record, including backups, instead of using the ambiguous word delete.
- [ ] C. Feature attribution applied to the agent's model would have flagged the mismatch between the agent's wording and the customer's meaning.
- [ ] D. Asking the agent afterwards why it said deleted gives a faithful account of what it did.
- [ ] E. Setting a flag on a row is a soft delete, which differs from a hard delete that physically removes the data.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Verification means checking the state directly, not trusting a report.
- B: Naming the exact operation prevents the ambiguity between soft and hard delete.
- C: Attribution does not compare a report with the real system state.
- D: A later self-report is a new generated text, not a log of the action.
- E: Soft delete marks a record; hard delete erases it.

**Source:** Soft delete, hard delete and verification

## MA-ch05.28

A hospital's contract requires an explainable reason for each prediction of a sepsis model. The vendor publishes the weights of its large neural network and lists the five inputs with the largest Shapley values for each patient. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The Shapley values tell the patient which actions would lower the risk.
- [ ] B. Publishing the weights gives transparency about the model's internals, which differs from letting a clinician predict what the model will do.
- [ ] C. A large neural network becomes simulatable once its weights are published.
- [ ] D. A short scoring rule a clinician can follow is a post-hoc explanation of the network.
- [ ] E. Whether an explanation is adequate depends on the audience and the decision, so one explanation can suit a developer and fail a patient.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: Attributions describe contributions to the prediction, not actions that change the outcome.
- B: Access to internals does not make the model understandable.
- C: Simulatability means a person can step through the computation, which is unrealistic at that scale.
- D: A scoring rule is a different model that is interpretable by design.
- E: Adequacy is relative to who reads it and for what purpose.

**Source:** Transparency, simulatability and adequacy

## MA-ch05.29

To explain a gradient-boosted credit model, an analyst trains a shallow decision tree on the black-box model's decisions and checks how often the two agree, finding lower agreement for one subgroup. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. High overall fidelity can hide low fidelity in a subgroup.
- [ ] B. A global surrogate is an interpretable model trained to imitate the predictions of a black box.
- [ ] C. Perfect fidelity would show that the black box is correct about applicants.
- [ ] D. The fidelity of the surrogate is measured by its agreement with the true repayment outcomes.
- [ ] E. Fidelity and accuracy are different quantities, since one compares with the black box and the other with the truth.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: Subgroup fidelity should be checked separately.
- B: The surrogate is fitted to the black box's outputs rather than to the true labels.
- C: A perfect imitation copies the black box's mistakes too.
- D: Fidelity is agreement with the black box; agreement with outcomes is accuracy.
- E: A faithful surrogate can still be wrong about applicants.

**Source:** Global surrogate and fidelity

## MA-ch05.30

A lender removes race from its approval model's inputs but keeps zip code, which is correlated with race. Shapley explanations show a large value for zip code and none for race. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Comparing approval rates and error rates across groups, as in demographic parity or equalized odds, finds disparities that attributions can miss.
- [ ] B. Removing the protected attribute from the inputs, called fairness through unawareness, assures equal outcomes across groups.
- [ ] C. Disparate treatment and disparate impact mean the same thing.
- [ ] D. Zip code can act as a proxy variable, an input that carries information about a protected attribute.
- [ ] E. A large attribution to zip code on its own establishes that the lender discriminates on race.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: Group fairness metrics measure outcomes directly.
- B: Correlated inputs can reproduce the same disparities.
- C: Disparate treatment is intentional use of a protected attribute; disparate impact is unequal outcomes from a neutral rule.
- D: A proxy encodes the protected attribute indirectly.
- E: It shows reliance on zip code, which may or may not reflect discrimination.

**Source:** Proxy variables and fairness checks

## MA-ch05.31

A logistic regression for loan default uses two nearly identical inputs, balance_today and balance_yesterday. The two coefficients change sign and size across bootstrap resamples, while the predictions stay similar. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A coefficient is the change in the output per unit change in an input with the other inputs held fixed.
- [ ] B. Multicollinearity makes individual coefficients unstable across resamples, even while predictions stay stable.
- [ ] C. Ridge regularization stabilizes the coefficients by shrinking them.
- [ ] D. A regression coefficient is the effect of an input ignoring the other inputs.
- [ ] E. A negative coefficient on balance_yesterday shows that a higher balance yesterday lowers default risk.

**Key:** A=T B=T C=T D=F E=F

**Why:**

- A: That ceteris paribus reading breaks down when inputs move together.
- B: The data pin down the combined effect better than each separate coefficient.
- C: The penalty spreads weight across correlated inputs.
- D: It is a partial effect that adjusts for the other inputs.
- E: With a correlated input in the model, the sign can reflect an offset to its partner.

**Source:** Multicollinearity and coefficients

## MA-ch05.32

A team plans several uses of feature attributions such as Shapley values computed on validation data. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. For safety sign-off, a clean attribution pattern on validation data shows the model will perform well on a new population.
- [ ] B. For regulatory review, a list of the top three inputs for each decision shows whether the model treats demographic groups differently.
- [ ] C. For debugging, heavy attribution to an input the team did not expect is a lead for data leakage or a shortcut.
- [ ] D. For recourse, attribution values alone tell an applicant which actions would change the decision.
- [ ] E. For trust, a user's increased confidence after reading an explanation is evidence that the model is more accurate.

**Key:** A=F B=F C=T D=F E=F

**Why:**

- A: Attributions say nothing about robustness under distribution shift.
- B: Group treatment needs group-level outcome comparisons, not per-decision lists.
- C: Unexpected reliance points to a possible artifact.
- D: Recourse needs counterfactual, actionable changes.
- E: Persuasion is not evidence; trust should be calibrated to actual accuracy.

**Source:** Purposes of feature attributions

## MA-ch05.33

Two teams train models for the same task with the same data. Both reach about the same AUC and agree on most decisions, but their importance rankings put different inputs first. The two inputs are strongly correlated. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The differing rankings show that one of the two models is wrong.
- [ ] B. The importance ranking of whichever model scores higher identifies the true driver of the outcome.
- [ ] C. The Rashomon effect is that many different models reach similar accuracy while using the inputs differently.
- [ ] D. With strongly correlated inputs, credit can shift or split between them from one model to another.
- [ ] E. Equal AUC means the two models rely on the same inputs.

**Key:** A=F B=F C=T D=T E=F

**Why:**

- A: Both can fit the data equally well while splitting credit differently.
- B: A ranking describes a model, not the data-generating process.
- C: Equal accuracy does not pin down a single explanation.
- D: Correlated inputs are substitutes for each other.
- E: Performance is a poor guide to which inputs a model reads.

**Source:** Rashomon effect and importance rankings

## MA-ch05.34

A skin-lesion classifier scores well in internal validation but poorly at a new clinic. Its attribution maps concentrate on a ruler and on ink marks that clinicians add near lesions they find suspicious. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The drop at a new site is an example of distribution shift between the development data and the deployment data.
- [ ] B. Ink marks added by clinicians who suspect a lesion act as leakage, since they carry information about the label.
- [ ] C. Attribution maps concentrating on the ruler are confirmation that the model uses the ruler as a shortcut.
- [ ] D. External validation means evaluating on a random split of the development hospital's own data.
- [ ] E. Cropping out the ruler and re-scoring is an ablation that tests a suspected shortcut without relying on the explanation.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: The new site differs in conditions from the training data.
- B: A cue created by the labeling judgment leaks the answer.
- C: An attribution is a hypothesis to test, not a confirmation.
- D: External validation uses data from a different site.
- E: An intervention on the input confirms or refutes the hypothesis.

**Source:** Distribution shift and leakage

## MA-ch05.35

A city agency chooses between a boosted model with post-hoc Shapley explanations and a scoring rule with seven integer-weighted checks that has slightly lower accuracy. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Interpretable by design means the model is a neural network with an attention layer.
- [ ] B. A post-hoc explanation of the black box is as auditable as a transparent rule.
- [ ] C. An interpretable model gives lower accuracy than a black box on tabular data.
- [ ] D. Auditability means a third party can inspect and reproduce how a decision was reached.
- [ ] E. A scorecard of integer-weighted checks is an example of a model that is interpretable by design.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: It refers to structure a person can follow, such as a sparse linear model, a small tree or a scorecard.
- B: Post-hoc output is an approximation produced by a method, which can itself be wrong.
- C: The accuracy gap is often small, and no fixed trade-off holds.
- D: A simple rule can be reproduced step by step.
- E: Its structure is the explanation.

**Source:** Inherently interpretable models and auditability

## MA-ch05.36

A team must report importance for a random-forest model of loan default using three tools: impurity-based importance, permutation importance on held-out data, and the mean absolute Shapley value. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. The mean absolute Shapley value summarizes the typical size of an input's contribution to predictions.
- [ ] B. Different importance measures answer different questions, so they can rank inputs differently.
- [ ] C. The mean absolute Shapley value shows whether an input raises or lowers predictions on average.
- [ ] D. Permutation importance measures how large an input's contribution to the predictions is, not its effect on accuracy.
- [ ] E. Permutation importance is computed from the training-time splits of the trees.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Taking absolute values and averaging over rows gives a global magnitude.
- B: One measures split gain, one measures performance loss, one measures contribution size.
- C: The absolute value discards direction.
- D: It measures the effect on performance; contribution size is what Shapley magnitudes measure.
- E: Permutation importance uses performance after shuffling, ideally on held-out data.

**Source:** Choosing an importance measure

## MA-ch05.37

A rule would require that a decision denying a benefit come with a clear explanation of the main factors, and a vendor proposes printing the three inputs with the largest Shapley values for each decision. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Contestability, the ability to challenge a decision, needs reasons tied to facts about the person's case that they can check.
- [ ] B. A top-three list is enough to detect discrimination across groups.
- [ ] C. A list that sums to the prediction minus the reference is, by that fact, a contestable explanation.
- [ ] D. Interpretability and explanation are synonyms, so describing one decision after the fact makes the model interpretable.
- [ ] E. Recourse means the explanation names the inputs with the largest Shapley values.

**Key:** A=T B=F C=F D=F E=F

**Why:**

- A: A reason that cannot be checked cannot be disputed.
- B: Detecting discrimination requires group-level comparison of outcomes.
- C: Efficiency is accounting; it does not make reasons checkable.
- D: Interpretability is a property of the model; an explanation is a description of it produced by a method.
- E: Recourse is about actions that change the outcome, not the size of attributions.

**Source:** Purposes of an explanation

## MA-ch05.38

A reviewer notes that the words interpretability, explanation and transparency are used loosely in a vendor document. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Transparency means a method produces a reason for each prediction.
- [ ] B. Publishing the weights makes a model interpretable.
- [ ] C. An explanation is a property of the model's architecture, such as being linear.
- [ ] D. Interpretability is a property of the model: how readily a person can understand how it maps inputs to outputs.
- [ ] E. An explanation is a description of a model or a prediction, produced by a method for a particular purpose.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Transparency means access to the model's internals, such as weights and code.
- B: Access to weights is transparency, and a large network stays hard to understand.
- C: An explanation is a description produced for a purpose, often post-hoc; architecture relates to interpretability.
- D: A sparse linear model is more interpretable than a deep network.
- E: It can be local or global and can be faithful or unfaithful.

**Source:** Interpretability, explanation and transparency

## MA-ch05.39

In a model, the output rises only when inputs A and B are both present, and input C never changes the output. A team explains the output with Shapley values. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Shapley values divide the joint contribution of interacting inputs between them.
- [ ] B. An interaction means the effect of one input depends on the value of another.
- [ ] C. An input's marginal contribution depends on which other inputs are already present, so Shapley values average over orderings.
- [ ] D. An input with no effect alone can still have a nonzero Shapley value through interactions.
- [ ] E. Removing one input at a time gives effects that add up to the total, even with an interaction.

**Key:** A=T B=T C=T D=T E=F

**Why:**

- A: Averaging marginal contributions over orderings shares the interaction credit.
- B: The contribution of A depends on whether B is present.
- C: Averaging over coalitions makes the credit independent of order.
- D: Its marginal contribution can be positive in some coalitions.
- E: With an interaction, one-at-a-time effects can miss or double count the joint contribution.

**Source:** Interactions and Shapley values

## MA-ch05.40

An analyst groups explanation methods by how they access the model. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A saliency map assigns importance scores to input regions, often from gradients.
- [ ] B. Gradient-based methods apply directly to a model made of decision trees.
- [ ] C. TreeSHAP is model-specific, because it uses the structure of tree ensembles.
- [ ] D. Integrated gradients is model-specific, because it needs a differentiable model.
- [ ] E. LIME and KernelSHAP are model-agnostic, because they need just the model's outputs.

**Key:** A=T B=F C=T D=T E=T

**Why:**

- A: It highlights which pixels the output is most sensitive to.
- B: Tree ensembles are not differentiable in the inputs.
- C: It exploits the tree structure for efficient computation.
- D: It uses gradients of the output with respect to the inputs.
- E: They query the model as a black box.

**Source:** Model-agnostic versus model-specific methods

## MA-ch05.41

A hospital runs a trial that randomizes clinicians to see an AI recommendation alone or with a feature-attribution explanation, on cases where the recommendation is wrong. More clinicians follow the wrong advice when the explanation is shown, but the interval for the difference is wide. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A confidence interval for the difference expresses how uncertain the estimated effect is.
- [ ] B. Random assignment to arms supports a causal reading of the difference between arms.
- [ ] C. A higher following rate with the explanation shows that the explanation is an unfaithful description of the model.
- [ ] D. An interval for the difference that includes zero shows that the explanation has no effect.
- [ ] E. Overreliance is following AI advice when it is wrong.

**Key:** A=T B=T C=F D=F E=T

**Why:**

- A: A wide interval means the estimate is imprecise.
- B: Randomization balances other differences between groups on average.
- C: Following rate is a human outcome; faithfulness concerns the explanation and the model.
- D: It means the data are compatible with no difference, which differs from evidence of no difference.
- E: It is the human-side failure that explanations are sometimes expected to reduce.

**Source:** Overreliance and uncertainty
