# Jargon test: explainability

## MA-jargon.41

A vendor brochure calls its model "explainable, interpretable and transparent", and the buyer wants each word pinned down. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Interpretability is the degree to which a person can understand the model's own mechanism, as with a short decision tree.
- [ ] B. The three words are synonyms for the same property.
- [ ] C. Publishing the full weights of a large neural network makes it interpretable.
- [ ] D. Transparency means the model, its design and its data are open to inspection.
- [ ] E. An explanation is a statement or artifact offered about why a particular output came out as it did.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: That is the standard meaning: understanding the mechanism itself.
- B: They name different things: understanding the mechanism, access to internals, and a produced account of an output.
- C: Open weights make a model transparent, but a person still cannot read a large network's mechanism, so it is not interpretable.
- D: Transparency is about access to the internals, not about understanding them.
- E: An explanation is something produced about a model's output, which may or may not reflect the mechanism.

**Source:** Explanation, interpretability, transparency

## MA-jargon.42

An analyst reports that ice cream sales is the most important feature for predicting drownings and concludes that cutting ice cream sales will cut drownings. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Feature importance measures how much a model relies on an input to make predictions.
- [ ] B. A causal effect describes how the outcome changes when the input is set by intervention.
- [ ] C. An input can have high importance because it acts as a proxy for the true cause.
- [ ] D. A high feature importance shows that the input causes the outcome.
- [ ] E. A confounder such as hot weather can drive both variables and make one predict the other.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: It describes the fitted model's dependence on the input, not the world.
- B: Causal effect is defined by an intervention, not by predictive usefulness.
- C: A proxy carries information about the cause, so the model leans on it without it being causal.
- D: Importance reflects association the model exploited, which a confounder can create.
- E: A confounder is a common cause that produces a non-causal association.

**Source:** Feature importance vs causal effect

## MA-jargon.43

Four requests are sent to an analyst: why was this one applicant denied; which inputs matter most across the whole portfolio; what does the average effect of income look like across many rows; and does the answer for one applicant match the portfolio ranking. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Asking which inputs matter most across the whole portfolio asks for a global explanation.
- [ ] B. A single-prediction attribution is a global explanation.
- [ ] C. A local explanation for one case is guaranteed to match the global ranking of inputs.
- [ ] D. Asking why one applicant was denied asks for a local explanation.
- [ ] E. A partial dependence plot averaged over many rows is a local explanation.

**Key:** A=T B=F C=F D=T E=F

**Why:**

- A: A global explanation describes behaviour in aggregate.
- B: An attribution for one prediction is local.
- C: Local and global explanations can disagree, since one case need not resemble the average.
- D: A local explanation covers a single prediction.
- E: Averaging over many rows gives a global view of an input's effect.

**Source:** Local vs global explanation

## MA-jargon.44

A team has to explain a credit model and is choosing between intrinsic and post-hoc approaches. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Applying a saliency method to a trained network is an intrinsic approach.
- [ ] B. Choosing a short rule list instead of a deep network is a choice of an intrinsic approach.
- [ ] C. An intrinsically interpretable model is understandable by its structure, such as a sparse linear model.
- [ ] D. A post-hoc explanation is produced after training by analysing a fitted model.
- [ ] E. Post-hoc methods change the trained weights to make the model readable.

**Key:** A=F B=T C=T D=T E=F

**Why:**

- A: A saliency method is applied after training, so it is post-hoc.
- B: The model is chosen so its structure is readable.
- C: Intrinsic means interpretability is built into the model form.
- D: Post-hoc methods leave the model as trained and explain it afterward.
- E: Post-hoc methods leave the model unchanged.

**Source:** Post-hoc vs intrinsic

## MA-jargon.45

An analyst fits a depth-3 decision tree to imitate a black-box model and reads the tree to understand the black box. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. High fidelity on held-out inputs is not proof that the black box uses the same internal logic.
- [ ] B. The tree is a surrogate model of the black box.
- [ ] C. A surrogate fitted near one input is called a global surrogate.
- [ ] D. Agreement of the tree with the true labels is the measure of surrogate fidelity.
- [ ] E. The tree is trained on the true labels so that it explains the black box.

**Key:** A=T B=T C=F D=F E=F

**Why:**

- A: Matching outputs does not show matching reasoning.
- B: A surrogate is a simpler model fitted to approximate a more complex one.
- C: A surrogate fitted near one input is a local surrogate.
- D: Fidelity is agreement with the black box's outputs.
- E: To explain the black box the surrogate is trained on the black box's own predictions.

**Source:** Surrogate model

## MA-jargon.46

A heat map highlights regions of a chest X-ray that drove a classifier's output. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A saliency map is a counterfactual explanation.
- [ ] B. A highlighted region shows where the disease is located in the patient.
- [ ] C. An attribution method assigns each input feature a share of a prediction.
- [ ] D. Shapley values are one kind of attribution method.
- [ ] E. A saliency map shows which input regions most affect the model's output score.

**Key:** A=F B=F C=T D=T E=T

**Why:**

- A: A counterfactual describes an altered input that flips the outcome; a saliency map scores existing inputs.
- B: The map describes the model's reliance, not the patient's biology.
- C: Attribution divides a prediction among inputs.
- D: Shapley values attribute a prediction to features using a game-theoretic definition.
- E: Saliency is a sensitivity of the output to the input.

**Source:** Saliency and attribution

## MA-jargon.47

A lender tells a denied applicant: "had your income been 6,000 higher, you would have been approved." Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A counterfactual explanation requires an intrinsically interpretable model.
- [ ] B. It guarantees approval after the income rises, even if the lender retrains the model.
- [ ] C. It is a feature importance score for income.
- [ ] D. This is a counterfactual explanation: a change to the inputs that would flip the outcome.
- [ ] E. It describes a nearby alternative input, not the model's full internal logic.

**Key:** A=F B=F C=F D=T E=T

**Why:**

- A: Counterfactuals are usually computed post-hoc for black-box models.
- B: The statement is about the current model, and a retrained model can decide differently.
- C: Feature importance ranks inputs; a counterfactual gives a specific change.
- D: That is the definition of a counterfactual explanation.
- E: A counterfactual answers one what-if, not how the whole model works.

**Source:** Counterfactual explanation

## MA-jargon.48

Two explanation methods are compared. Clinicians rate one method's heat maps as sensible, while a test shows the other method tracks the classifier's behaviour more closely. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Clinician ratings of how sensible heat maps look measure faithfulness.
- [ ] B. Faithfulness is how accurately an explanation reflects what the model actually does.
- [ ] C. A plausible explanation is therefore faithful.
- [ ] D. Plausibility is how closely an explanation matches the model's computation.
- [ ] E. An explanation can be faithful and implausible if the model relies on a spurious cue.

**Key:** A=F B=T C=F D=F E=T

**Why:**

- A: They measure plausibility.
- B: Faithfulness is about agreement with the model's behaviour.
- C: Looking sensible to a reader says nothing about matching the model.
- D: That describes faithfulness; plausibility is how convincing the explanation looks to a person.
- E: The explanation then points at the cue, which looks odd but is true to the model.

**Source:** Faithfulness vs plausibility

## MA-jargon.49

A model trained on hospital records predicts lower pneumonia mortality for patients with asthma, because those patients were sent straight to intensive care. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Intensive care treatment acts as a confounder that explains the pattern.
- [ ] B. The pattern shows that asthma protects patients from dying of pneumonia.
- [ ] C. A large attribution to asthma shows its causal effect on survival.
- [ ] D. A correlation in observational data can reflect a confounder instead of a causal effect.
- [ ] E. The model has learned a correlation present in the records.

**Key:** A=T B=F C=F D=T E=T

**Why:**

- A: The treatment affects both who has the label of asthma-care and the outcome.
- B: The association comes from the treatment pathway, not a protective effect.
- C: An attribution describes the model's reliance, not an intervention result.
- D: Confounding is the standard reason association differs from causation.
- E: It captured an association between asthma and outcome.

**Source:** Correlation vs causation

## MA-jargon.50

A language model writes step-by-step reasoning before giving an answer, and a user treats that reasoning as the explanation of the answer. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. A chain-of-thought is a different thing from an attribution over the input features.
- [ ] B. A model's after-the-fact account of why it answered is a post-hoc rationale that may not reflect the computation.
- [ ] C. One faithfulness test is to add a hint to the input and check whether the answer changes while the reasoning does not mention the hint.
- [ ] D. A plausible chain-of-thought is evidence that it is faithful.
- [ ] E. Chain-of-thought is generated text, so it is not by itself a faithful account of the model's computation.

**Key:** A=T B=T C=T D=F E=T

**Why:**

- A: One is generated text and the other is a score assigned to inputs.
- B: Asking the model why afterwards yields a rationale, not a trace of the mechanism.
- C: An intervention that changes the answer but not the stated reasoning shows the reasoning is unfaithful.
- D: Plausibility and faithfulness are different properties.
- E: The text is an output and may not reflect the process that produced the answer.

**Source:** Chain-of-thought as explanation

## MA-jargon.51

An analyst lists four explanation tools: LIME, SHAP, permutation importance and a partial dependence plot, and asks which is which. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. SHAP assigns attributions based on Shapley values.
- [ ] B. A partial dependence plot is a local explanation of one prediction.
- [ ] C. Permutation importance measures how much performance drops when one feature is shuffled.
- [ ] D. LIME fits a local surrogate on perturbed points near one input.
- [ ] E. Integrated gradients is a global surrogate model.

**Key:** A=T B=F C=T D=T E=F

**Why:**

- A: SHAP is the Shapley value attribution method.
- B: It averages over many rows to show an input's average effect, a global view.
- C: It is a global importance measure based on shuffling.
- D: LIME is a local surrogate method.
- E: Integrated gradients is an attribution method that accumulates gradients along a path from a baseline.

**Source:** Named explanation methods

## MA-jargon.52

A team lists requests to an explanation tool and wants the exact term for each. Check each statement that is true. Each statement is worth 1 point (5 points total).

- [ ] A. Asking for a ranking of inputs by average reliance across the dataset asks for global feature importance.
- [ ] B. Asking for a rule-based model a regulator can read directly asks for an intrinsically interpretable model.
- [ ] C. Asking whether the explanation reflects what the model really does asks about plausibility.
- [ ] D. Asking for the smallest input change that flips a denial asks for a counterfactual explanation.
- [ ] E. Asking why this one case got its score asks for a global explanation.

**Key:** A=T B=T C=F D=T E=F

**Why:**

- A: Averaged reliance across the dataset is a global importance.
- B: Rule-based models are readable by their structure.
- C: That question is about faithfulness.
- D: A counterfactual states the change that flips the outcome.
- E: A single case calls for a local explanation.

**Source:** Choosing the exact explanation term
