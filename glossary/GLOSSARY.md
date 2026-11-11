# INFO 7375 Computational Skepticism for AI terminology glossary

Every term in every deck in `decks/`, with its meaning and a tag: **in the chapter** (the chapter uses and explains it), **in the exam-term list only** (a row in `docs/` exam-term lists, but the chapter does not explain it), or **outside source** (named in the slide's Source line). One deck per chapter, named "NN Title.html" with NN the chapter number. Generated from the decks by `make_glossary2.js`; edit the decks, not this file.

## Decks

| Deck | Slides | Terms |
|---|---|---|
| [The skeptic’s toolkit](decks/01%20The%20skeptic's%20toolkit.html) | 14 | 25 |
| [The confidence illusion](decks/02%20The%20confidence%20illusion.html) | 14 | 33 |
| [Data validation](decks/03%20Data%20validation.html) | 14 | 30 |
| [Robustness](decks/04%20Robustness.html) | 16 | 34 |
| [Model explainability](decks/05%20Model%20explainability.html) | 13 | 31 |
| [Bias: where it enters and who is responsible](decks/06%20Bias.html) | 14 | 33 |
| [Fairness metrics](decks/07%20Fairness%20metrics.html) | 14 | 31 |
| [Validating agentic AI](decks/08%20Validating%20agentic%20AI.html) | 14 | 32 |
| [Delegation and trust](decks/09%20Delegation%20and%20trust.html) | 14 | 33 |
| [Visualization under validation](decks/10%20Visualization%20under%20validation.html) | 14 | 32 |
| [Communicating uncertainty](decks/11%20Communicating%20uncertainty.html) | 14 | 34 |
| [Accountability](decks/12%20Accountability.html) | 14 | 30 |
| [The limits of AI](decks/13%20The%20limits%20of%20AI.html) | 14 | 34 |

Total: 13 decks, 412 term entries.

---

## The skeptic’s toolkit

[Open the deck](decks/01%20The%20skeptic's%20toolkit.html) · 14 slides · 25 terms

| Term | Meaning | Tag |
|---|---|---|
| Measure versus want | The number a system is scored on is a stand-in for what its builders actually need. | in the chapter |
| Gap from the start | The stand-in never matched the target; catch it by asking what the number is a number of. | in the chapter |
| Gap that opens later | The measure matched at first, then the world moved; only checking again and again catches it. | in the chapter |
| Goodhart’s law | When a measure becomes a target, it ceases to be a good measure. | in the chapter |
| Held-out test set | Data kept back from the builders and used only to score the model on cases it never saw. | in the chapter |
| Skepticism | A method, not a mood: moves performed on a claim, which can be taught and whose use can be seen. | in the chapter |
| Cartesian doubt | Doubt a claim until you can list the conditions under which it would be wrong. | in the chapter |
| Popperian falsifiability | A claim must name the metric, threshold and window that would show it false. | in the chapter |
| Rhetorical claim | A claim no observation could contradict: noise in technical language, not engineering. | in the chapter |
| Limit of induction (Hume’s move) | Each correct prediction adds no logical guarantee that the next one will be right. | in the chapter |
| Distribution shift | The world after deployment stops resembling the data the model learned from. | in the chapter |
| Drift | Inputs changing over time from what the model was built on, tracked with a score called PSI. | in the exam-term list only |
| Artifact versus world | The artifact is what the system outputs; the world is the real thing it should say something about. | in the chapter |
| Kantian slice | You only ever see a slice of the world; keep in view what lies outside it. | in the chapter |
| Solve-verify asymmetry | In computer science checking is easier than finding; in AI deployment, producing is cheap and verifying is costly. | in the chapter |
| Plausibility auditing (capacity 1) | Asking whether an output is even the kind of thing that could be true, given what you know. | in the chapter |
| Problem formulation (capacity 2) | Stating the question the system answers and checking it is the question you need answered. | in the chapter |
| Interpretive judgment (capacity 4) | Reading an output in its domain: the same number means different things in different deployments. | in the chapter |
| Tool orchestration (capacity 3) | Choosing which tool fits which sub-problem: AI, human judgment, another model, or none. | in the chapter |
| No tool yet | The call that nobody yet knows how to do this well enough to deploy, so nothing is deployed. | in the chapter |
| Executive integration (capacity 5) | Combining outputs from tools, models and people into one decision that someone owns. | in the chapter |
| Fluency trap | Fluent output raises confidence in the answer, then in your own evaluation of it. | in the chapter |
| Form versus content | How well an output reads and whether it is true are independent in AI output. | in the chapter |
| Institutional skepticism | The moves written into the checklist and the workflow instead of left to memory. | in the chapter |
| Prediction-lock | Write your prediction before seeing the result and never revise it; append what you observed. | in the chapter |

## The confidence illusion

[Open the deck](decks/02%20The%20confidence%20illusion.html) · 14 slides · 33 terms

| Term | Meaning | Tag |
|---|---|---|
| Sample space | The list of every outcome that could happen. | in the chapter |
| Event | Any group of outcomes you care about. | in the chapter |
| Three axioms | No negatives, the total is 1, and exclusive outcomes add. | in the chapter |
| Classical probability | Count the favourable outcomes out of equally likely ones. | in the chapter |
| Frequentist probability | The share of times it happens over a long run of repeats. | in the chapter |
| Bayesian probability | A degree of belief that evidence updates. | in the chapter |
| Prior | What you believed before seeing the evidence. | in the chapter |
| Conditional probability | The chance of A once you know B has happened. | in the chapter |
| Multiplication rule | Chance of both: each step's chance given the steps before it (the chain rule). | in the chapter |
| Independence | Knowing one event tells you nothing about the other. | in the chapter |
| Partition | Non-overlapping pieces that cover every case. | in the chapter |
| Total probability | Weight each piece's chance by its share, add up. | in the chapter |
| Likelihood | Chance of the evidence if the hypothesis is true. | in the chapter |
| Posterior | Belief after the evidence: prior updated. | in the chapter |
| Bayes' theorem | Prior × likelihood ÷ chance of the evidence. | in the chapter |
| Base rate | How common the thing is before any test. | in the chapter |
| Sensitivity | Of the truly sick, the share flagged. | in the chapter |
| Specificity | Of the healthy, the share cleared. | in the chapter |
| False positive | A healthy case the test wrongly flags. | in the chapter |
| PPV (positive predictive value) | Of everything flagged, the share that is real. | in the exam-term list only |
| Calibration | Stated confidence matches how often it comes true. | in the chapter |
| Calibration curve | Stated probability across, actual frequency up; the diagonal is perfect. | in the chapter |
| Overconfidence | Stated confidence runs above how often the model is right. | in the chapter |
| Decorative number | A confident figure nobody has checked against outcomes. | in the chapter |
| Temperature scaling | Divide the logits by one fitted T: same ranking, softer confidence. | in the chapter |
| ECE (expected calibration error) | Bin-weighted average gap between stated and actual. | in the exam-term list only |
| Calibration baseline | Write 90% intervals for questions, then count how many hit. | in the chapter |
| Plausibility auditing | Hearing the wrong note in a number before you can prove it wrong. | in the chapter |
| Distribution shift | The world after deployment stops matching the training data. | in the chapter |
| Hume's induction problem | The past does not guarantee the future; the world must cooperate. | in the chapter |
| Central limit theorem | Averages of many independent, finite-variance values look bell-shaped. | in the chapter |
| Heavy-tailed | Extremes are common enough that the average never settles. | in the chapter |
| Loss | What being wrong costs, not how often it happens. | in the chapter |

## Data validation

[Open the deck](decks/03%20Data%20validation.html) · 14 slides · 30 terms

| Term | Meaning | Tag |
|---|---|---|
| Epistemic frame | Every unwritten decision about what was recorded, kept, joined and cut off. | in the chapter |
| Row-count question | Ask why the table has exactly this many rows, and how many it should have had. | in the chapter |
| Silent join drop | Rows with no match across the sources vanish from the merge, with no error. | in the chapter |
| Recording instrument | The sensor, form or system that did the recording, and what it could not see. | in the chapter |
| Plato's Cave | A dataset is shadows on a wall. EDA measures the shadows, not the fire. | in the chapter |
| Procedural EDA | The standard pass: types, shape, distributions, missingness, correlations, outliers. | in the chapter |
| Column type | Numeric, count, nominal, ordinal, time or text. The right plot depends on it. | in the chapter |
| Sentinel value | A placeholder such as 999 or N/A standing in for unknown. | in the chapter |
| Pearson correlation | A score for straight-line association only. y = x² can score near zero. | in the chapter |
| MCAR | Missing completely at random: no pattern at all. | in the chapter |
| MAR | Missing at random: gaps follow a column you see. | in the chapter |
| MNAR | Missing not at random: gaps follow the value. | in the chapter |
| Missingness matrix | Dark where missing; stripes mean columns fail together. | in the chapter |
| Outlier | An extreme value flagged as a candidate. A person decides what it is. | in the chapter |
| IQR rule | Flag values below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR. | in the chapter |
| Z-score rule | Flag values with /z/ > 3. The mean and spread it uses are pulled by the outliers. | in the chapter |
| Marks and channels | A mark is the shape drawn per row; a channel is the visual property carrying a value. | in the chapter |
| Channel ranking | Position reads best, then length. Area and color intensity read worst. | in the chapter |
| Expressiveness | Match the channel to the data type. Size on a category implies an order that is not there. | outside source |
| Sampling assumption (also convenience sample) | The data is whoever was easy to reach; deployment meets everyone. | in the chapter |
| Time-window assumption | Trained on one period, deployed into a shifted one. | in the chapter |
| Label assumption | The label is a proxy, not the thing you care about. | in the chapter |
| Feature-engineering | A column that is someone's model output, not raw data. | in the chapter |
| Access boundary (the access assumption) | The data's reach is the schema plus everything its contents point to. | in the chapter |
| Datasheets for Datasets | Gebru et al.: 57 questions in seven sections that document a dataset's life. | in the chapter |
| Boundary leakage (unconsented data leakage) | Private material escaping through a corpus's edge; hard to find at scale without red-teaming. | in the chapter |
| Prediction-lock | A written, dated prediction of the dataset's frame, made before any plot. | in the chapter |
| Gap analysis | The difference between the locked prediction and the traced frame is what you learned. | in the chapter |
| Row tracing | Pick one row and follow its values back through every source system. | in the chapter |
| Do not delegate | Rebuilding the frame stays with you; an AI version holds nothing you lacked. | in the chapter |

## Robustness

[Open the deck](decks/04%20Robustness.html) · 16 slides · 34 terms

| Term | Meaning | Tag |
|---|---|---|
| Adversarial example | An input nudged on purpose so the answer flips while a person sees no real change. | in the chapter |
| Proxy | A signal that tracked the right label in training but is not the thing itself. | in the chapter |
| Robust features | Patterns tied to the label that survive small changes, such as shape. | in the chapter |
| Non-robust features | Fine-grained patterns tied to the label in training that a small push can move. | in the chapter |
| FGSM (Fast Gradient Sign Method) | One step of size ε along the sign of the loss gradient. | in the chapter |
| Perturbation budget (ε) | The most any one input value may change (the L∞ budget). | in the chapter |
| Linearity hypothesis | Tiny pushes on thousands of inputs add up to a large change in a locally linear score. | in the chapter |
| Low-variance direction | A direction in which the training data barely varies, so training gave little signal. | in the chapter |
| Boundary tilting | A boundary running almost alongside the data, so a tiny step in a low-variance direction crosses it. | in the chapter |
| White-box attack (gradient-based) | The attacker has the weights and gradients. | in the chapter |
| Black-box attack (query-based) | The attacker sees only outputs and estimates the gradient by probing. | in the chapter |
| Transfer attack | A perturbation crafted on a surrogate model that also fools the target. | in the chapter |
| Patch attack (patch / physical) | A large change in a small region, such as a sticker or printed pattern. | in the chapter |
| Natural adversarial | No attacker: a rare, long-tail input the model never generalized to. | in the chapter |
| Prompt injection | Instructions hidden in data the agent reads, which it treats as commands. | in the chapter |
| PGD (Projected Gradient Descent) | Many small gradient-sign steps, each projected back into the ε-ball. | in the chapter |
| Adversarial training | Training on the worst-case perturbed input found at each step. | in the chapter |
| Robustness trade-off (accuracy-robustness trade-off) | Gaining robustness tends to cost accuracy on ordinary inputs. | in the chapter |
| Randomized smoothing | Vote over many noisy copies of the input; a clear winner gives a certified radius R. | in the chapter |
| Lipschitz constant | The most the output can change per unit change of the input. | in the chapter |
| Formal verification | A proof that a property holds for every input in a defined region. | in the chapter |
| Detection-based defense | Flags suspected adversarial inputs and routes them to a fallback or a person. | in the chapter |
| Input preprocessing | Denoising, quantizing or smoothing the input before the model sees it. | in the chapter |
| Adaptive attack | An attack built with knowledge of the defense, so it is designed to get past it. | in the chapter |
| Distribution shift | Deployment inputs stop resembling training inputs, with no attacker involved. | in the chapter |
| Semantic invariance | The answer stays the same when the input is reworded without changing its meaning. | in the chapter |
| Prompt sensitivity | Prompts that mean the same thing get noticeably different answers. | in the chapter |
| Adversarial testing | Testing with inputs built to fool the model, to see what it relies on. | in the exam-term list only |
| Robustness profile | What the model resists and what it does not, by attack, budget and shift, not one number. | in the chapter |
| Residual risk disclosure | A written list of known weaknesses that were not mitigated. | in the chapter |
| Monitoring specification | What is watched in production, and what triggers review or rollback. | in the chapter |
| Pearl's ladder | Three levels of causal question: seeing, doing, imagining. | in the chapter |
| Counterfactual | What would have happened in this case had one thing been different. | in the chapter |
| Governance question (governance counterfactual) | Asks whether the model would differ had the institutions around it differed. | in the chapter |

## Model explainability

[Open the deck](decks/05%20Model%20explainability.html) · 13 slides · 31 terms

| Term | Meaning | Tag |
|---|---|---|
| Fluency trap | Smooth, well-formed output taken as evidence it does not carry. | in the chapter |
| Accurate but misleading (technically accurate, practically misleading) | True about the model, yet leaves the reader believing something false about the world. | in the chapter |
| Shortcut | A spurious pattern that matches the label in training and fails on new data. | in the chapter |
| Post-hoc explanation | A reason worked out after the model has produced its output. | in the chapter |
| SHAP | A feature-attribution method from game theory: one number per feature, for one prediction. | in the chapter |
| Internal accounting | How the model itself divides credit among features. Real, and not the same as the world. | in the chapter |
| Rung 1 (association) | The level of seeing what goes with what, or what the model used. SHAP stays here. | in the chapter |
| Rung 2 (intervention) | The level of doing: what happens if X is set to a value. SHAP cannot answer it. | in the chapter |
| Value function | The expected prediction when only the features in a set S are known. | in the chapter |
| Coalition | A subset of features treated as already known. | in the chapter |
| Marginal contribution | What one feature adds to the prediction when it joins a coalition. | in the chapter |
| Shapley value | A feature’s marginal contribution, averaged over every order of arrival. | in the chapter |
| Efficiency | The values add up exactly to the prediction minus the average. | in the chapter |
| Symmetry | Features that do the same work get the same credit. | in the chapter |
| Dummy | A feature that changes nothing gets zero. A non-zero zip value means the model uses zip. | in the chapter |
| Additivity (also linearity) | Values for two models combined are the sums of the values for each. | in the chapter |
| Sampling (KernelSHAP) | Estimate the values from M random orderings instead of all of them. | in the chapter |
| TreeSHAP | Exact values for tree models, found by walking the few paths that change a prediction. | in the chapter |
| Correlated features | Drawing each feature on its own creates combinations that never occur in real data. | in the chapter |
| Conditional sampling | Draw the missing features given the known ones. Realistic, but the Dummy axiom can fail. | in the chapter |
| LIME | Fits a simple line to the model’s output around one input. The slope is the explanation. | in the chapter |
| LIME instability | The perturbations are random, so the same input can give a different explanation each run. | in the chapter |
| Off-manifold | Perturbed inputs that no real case resembles, where the line may describe nothing real. | in the chapter |
| Counterfactual (also counterfactual explanation) | States how the prediction would change if a feature had another value. | in the chapter |
| Transparency | A property of the system: its code, weights, architecture and data can be inspected. | in the chapter |
| Explainability | A property of outputs: each one comes with a stated reason. | in the chapter |
| Interpretability | A person can build a mental model good enough to predict new cases. | in the chapter |
| Rudin’s argument | For high-stakes decisions, use interpretable models rather than explaining black boxes. | in the chapter |
| Language game | The setting that gives a word its meaning, so one word can mean different things. | in the chapter |
| Language-game mismatch | Two parties use one word for different operations, so a true report misleads. | in the chapter |
| Audience question | Ask who reads the explanation, what its words mean in their game, and whether it serves that game. | in the chapter |

## Bias: where it enters and who is responsible

[Open the deck](decks/06%20Bias.html) · 14 slides · 33 terms

| Term | Meaning | Tag |
|---|---|---|
| Estimator | A procedure that turns data into a number, such as a mean or a risk score. | in the chapter |
| Unbiased estimator | Averages out to the true value, though it may miss on any one dataset. | in the chapter |
| Bias (Bias(θ̂) = E[θ̂] − θ) | How far the estimate sits from the truth on average, over every dataset you might collect. | in the chapter |
| Selection bias | Who ends up in the sample depends on what happened to them, so the sample average is off. | in the chapter |
| Sampling bias | Some groups are underrepresented because they were hard to reach, not because of their outcomes. | in the chapter |
| Inverse prob. weighting (Inverse probability weighting) | Weight each kept case by 1 over its chance of being kept, so it stands in for those dropped. | in the chapter |
| Confirmation bias | The researcher's prior steers what data is collected, kept and reported. | in the chapter |
| Self-report bias | People misreport themselves in a consistent direction, such as voting more than they did. | in the chapter |
| Publication bias | Significant results get published and nulls stay in drawers, so the literature looks stronger. | in the chapter |
| Funnel plot | Effect size against precision; an empty lower-left corner shows the missing small null studies. | in the chapter |
| Cohen's kappa | Agreement between two coders, corrected for the agreement chance alone would give. | in the chapter |
| Observer bias | A labeler's prior leaks into the label, so labels track what the labeler already believed. | in the chapter |
| Data-coding bias | Systematic miscoding when judgment is needed to fit material into categories. | in the chapter |
| Data-entry bias | Patterned transcription error, such as a buried code replaced by the nearest one. | in the chapter |
| Historical bias | A faithful, representative record of a world you did not want to reproduce; its accuracy is the harm. | in the chapter |
| Implicit bias | The unconscious associations of the people in the pipeline; the medium other biases swim in. | in the chapter |
| Dataset bias | The training sample does not represent the deployment population. | in the chapter |
| Label bias | The labels record a biased process, so the model predicts a distorted stand-in. | in the chapter |
| Biased measurement | A stand-in variable distorted on the way, such as re-arrest recorded for crime. | in the chapter |
| Structural bias | Good data, accurate labels, correct model, and still unfair outcomes because of the world it is deployed into. | in the chapter |
| Pearl's ladder | Three levels of causal reasoning: seeing, doing, imagining. | in the chapter |
| Association | Seeing: P(Y / X), the chance of Y given that we observe X. | in the chapter |
| Intervention | Doing: P(Y / do(X = x)), the chance of Y if we set X to a value. | in the chapter |
| Counterfactual | Imagining: what would have happened to this case if X had been different. | in the chapter |
| Causal graph | Nodes for variables, arrows from cause to effect. | in the chapter |
| Proxy | A feature correlated with the protected attribute. | in the chapter |
| Leverage analysis | List every path; find the fix that blocks most. | in the chapter |
| Leverage | How much bias-carrying flow an action blocks. | in the chapter |
| Accountable owner | Whoever controls the node at the leverage point. | in the chapter |
| Calibration parity | A score means the same thing in every group. | in the chapter |
| Equal FPR and FNR (Equalized odds) | Wrongly flagged and missed shares match in every group. | in the chapter |
| Impossibility theorem | With unequal base rates, not all three can hold at once. | in the chapter |
| Values claim | Choosing a metric is choosing which error you accept. | in the chapter |

## Fairness metrics

[Open the deck](decks/07%20Fairness%20metrics.html) · 14 slides · 31 terms

| Term | Meaning | Tag |
|---|---|---|
| Base rate (prevalence) | The share of a group that truly has the positive outcome. | in the chapter |
| True-positive rate | Of the people who truly are positive, the share the model flags. | in the chapter |
| False-positive rate | Of the people who truly are not positive, the share the model flags anyway. | in the chapter |
| Predictive value (PPV) (precision) | Of the people the model flags, the share who truly are positive. | in the chapter |
| Demographic parity (statistical parity) | The model says yes at the same rate in every group. | in the chapter |
| Equalized odds (equal TPR and FPR) | Both error rates match across groups. | in the chapter |
| Calibration parity (predictive parity) | A stated probability means the same observed rate in every group. | in the chapter |
| Impossibility theorem | With unequal base rates, calibration and equal error rates cannot both hold. | in the chapter |
| Threshold | The score cutoff above which the model says yes. | in the exam-term list only |
| COMPAS | A recidivism risk tool whose 2016 audit set two true claims against each other. | in the chapter |
| Values claim | The belief about who should bear errors that a choice of metric carries. | in the chapter |
| Defended choice | The deliverable: a chosen metric with written reasons, in six steps. | in the chapter |
| Group fairness | Fairness judged by comparing aggregate rates across whole groups. | in the chapter |
| Individual fairness | Similar people should be treated similarly, even when group totals balance. | in the chapter |
| Lipschitz condition ((D, d)-Lipschitz) | The difference in treatment may not exceed the difference between the people. | in the chapter |
| Similarity metric d | A task-specific measure of how alike two people are, and a values choice. | in the chapter |
| Awareness (FTA) (fairness through awareness) | Decide openly how much group membership counts when judging similarity. | in the chapter |
| Unawareness (FTU) (fairness through unawareness) | Drop the sensitive attribute from the model and call it fair. | in the chapter |
| Proxy | A feature such as zip code that reveals group membership indirectly. | in the chapter |
| Structural causal model | Variables with arrows for which causes which. | in the chapter |
| Direct effect (disparate treatment) | The attribute alone moves the prediction. | in the chapter |
| Indirect effect (disparate impact) | Attribute moves a mediator, which moves prediction. | in the chapter |
| Spurious effect | A confounder links them with no causal path. | in the chapter |
| Counterfactual fairness | Same decision for this person in another group. | in the chapter |
| Benefit | The number per person whose spread is measured: a score, a probability or an error flag. | in the chapter |
| GE Index (generalized entropy index) | One number for how unequally benefit is spread across people, as in income inequality. | in the chapter |
| Alpha (α) | Sets whose unfairness counts more: low alpha the bottom, high alpha the top. | in the chapter |
| GE decomposition | Total unfairness equals the within-group part plus the between-group part. | in the chapter |
| Pre-processing | Change the training data first, for example by reweighting. | in the chapter |
| In-processing | Change the training objective, for example by adding a fairness penalty. | in the chapter |
| Post-processing | Change predictions afterwards, for example with a threshold per group. | in the chapter |

## Validating agentic AI

[Open the deck](decks/08%20Validating%20agentic%20AI.html) · 14 slides · 32 terms

| Term | Meaning | Tag |
|---|---|---|
| Prediction system | A model whose outputs are statements about the world; a wrong one is wrong for one input. | in the chapter |
| Consequence system | A model that acts, so its outputs are changes of state that cannot always be rewound. | in the chapter |
| Open-ended loss | A wrong action costs as much as the agent's reach allows, not just one bad answer. | in the chapter |
| False success report | The agent says done while the world shows it is not, and nothing catches the mismatch. | in the chapter |
| Audit trail | The record of what the agent did, captured as it acts so it survives the action. | in the chapter |
| Gating condition | A confirmation from the owner required before an irreversible action may run. | in the chapter |
| False-success catch | After an action, observe the world independently and compare it with the report. | in the chapter |
| Stakeholder model | Who the agent serves and who its actions affect; without it, the most urgent speaker wins. | in the chapter |
| Self-model | What the agent's actions reach and when it is out of its depth; without it, done is reported early. | in the chapter |
| Deliberation surface | A private place to weigh options before acting, which leaves a trace of rejected ones. | in the chapter |
| Autonomy-competence gap | Acting at a high autonomy level while understanding at a much lower one. | in the chapter |
| Effective data scope | Everything that can be pulled out through the agent's access, indirect requests included. | in the chapter |
| Contextual privacy | Information shared in one setting should not be forwarded into another. | in the chapter |
| Displayed identity | A name or label shown in a channel, which anyone can change. | in the chapter |
| Verified identity | Identity confirmed by a check a changed name cannot fake, such as multi-factor sign-in. | in the chapter |
| Contingent failure | A failure engineering can close, such as a missing tool or a missing budget cap. | in the chapter |
| Fundamental failure | A failure rooted in the architecture; a patch only changes its shape. | in the chapter |
| Prompt injection | Instructions slipped in as data; the model reads both as the same kind of token. | in the chapter |
| Observability modeling | Knowing which channels are visible to whom; private reasoning alone does not supply it. | in the chapter |
| Cascading hallucination | An error is passed on, relied on and magnified, so the system errs more than any one agent. | in the chapter |
| Resource exhaustion | Agents together, or an outside sender, use up tokens, memory or server capacity. | in the chapter |
| Runaway loop | A process that repeats with no stopping condition. | in the chapter |
| Budget cap, rate limit | Hard limits on use per run or per period, which stop an unbounded process. | in the chapter |
| Authority laundering | Data handed on as a legitimate output; the receiver cannot check where it came from. | in the chapter |
| Provenance tracking | A record of what each agent passed to which other, and where it first came from. | in the chapter |
| Identity confusion | An agent takes its own earlier messages in a shared channel for a second agent. | in the chapter |
| Data validation lens | Asks what the agent's effective access really is, not what was written down. | in the chapter |
| Explainability lens | Asks whether the agent's account of its action matches the observed state. | in the chapter |
| Fairness lens | Asks whose values govern the behaviour: the provider's, the owner's or an editor's. | in the chapter |
| Robustness lens | Asks whether social pressure or spoofing across channels can flip the behaviour. | in the chapter |
| Circular verification | Checking an identity by asking the unverified source to confirm itself. | in the exam-term list only |
| Contingent luck | Resisting an attack for a reason that would not hold next time. | in the chapter |

## Delegation and trust

[Open the deck](decks/09%20Delegation%20and%20trust.html) · 14 slides · 33 terms

| Term | Meaning | Tag |
|---|---|---|
| Contract, not partition | A delegation sets out what the AI does, what the human does, the checkable handoff and what happens on failure. | in the chapter |
| Delegation map | A written document giving each pipeline step an owner, inputs, outputs and a signal that it finished correctly. | in the chapter |
| Handoff condition | The signal that a step finished correctly so the next can start; the load-bearing part of the map. | in the chapter |
| Testable | A stranger who did not build the pipeline can read the condition, look at the system and tell if it was met. | in the chapter |
| Graded testability | Testability has tiers: some conditions any outsider can check, some only a qualified reviewer. | in the chapter |
| Failure routing | A declared escalation path for when a step fails, so someone is accountable. | in the chapter |
| Broken pipeline | Missing items 1 to 4 of the map: it cannot run, so the gap shows at once. | in the chapter |
| Unsupervised pipeline | Missing items 5 to 8: it runs fine until an uncaught error surfaces downstream. | in the chapter |
| Audit trail | The record of inputs, decisions and outputs that lets a case be reconstructed afterwards. | in the chapter |
| Sign-off authority | A named human who is the accountable decision-maker for the pipeline's outputs. | in the chapter |
| Operational form | The concrete, documented version of a capacity that a pipeline contains: no artifact, no capacity. | in the chapter |
| Plausibility auditing | Checking whether an output could be true of the world it describes, with a recorded checklist. | in the chapter |
| Problem formulation | Writing down the question, the criteria and when AI is the right tool, before the AI is invoked. | in the chapter |
| Tool orchestration | Deciding which tool owns each step and the handoff between tools; made concrete, it is the map. | in the chapter |
| Interpretive judgment | Reading the output in its deployment context and recording what it means for the decision. | in the chapter |
| Executive integration | Combining outputs from several tools and people into one decision with named authority. | in the chapter |
| Irreducibly human | A step the AI cannot take because it needs domain knowledge, domain judgment or responsibility. | in the exam-term list only |
| Failure visibility | When something cannot be done, say so with a flag instead of inventing a plausible substitute. | in the chapter |
| Boondoggle Score | The course author's five-question heuristic for sorting sub-tasks; not validated outside the course. | in the chapter |
| Delegation buckets | The three outcomes of the sort: AI executes, human only, or hybrid with human checks. | in the chapter |
| Verification cost | How costly a human check is; near-redo checks quietly push people to accept the output. | in the chapter |
| Solve-verify asymmetry | Checking an answer is easier than finding it; that gap is why AI help is worth having. | in the exam-term list only |
| Stakes | The cost of being wrong on a step; when one error is catastrophic, the average is the wrong statistic. | in the chapter |
| Distribution match | Whether an input resembles what the AI was trained on or falls where it is undertrained. | in the chapter |
| Reversibility | Whether an action can be undone; irreversible ones need a human approval gate. | in the chapter |
| Audit trail clarity | Whether the AI's actions leave a trail that can be reviewed after the fact. | in the chapter |
| Calibrated trust | Reliance on the AI that matches its actual reliability for this kind of case. | in the chapter |
| Undertrust | Systematically discounting AI output even when it is reliable, so the value is lost. | in the chapter |
| Overtrust | Accepting AI output that should be checked, so errors surface later and quietly. | in the chapter |
| Monitoring gap | The distance between the monitoring data a deployment holds and the data anyone reviews. | in the chapter |
| AI Use Disclosure | A per-step record of how AI was used: the tool, the request, the output, what was checked, what changed. | in the chapter |
| Supervisory log | A disclosure read as a whole: where the person used each capacity, with evidence behind it. | in the chapter |
| Hierarchical mapping | Mapping by component, in step-by-step detail only at high-stakes interfaces and seams. | in the chapter |

## Visualization under validation

[Open the deck](decks/10%20Visualization%20under%20validation.html) · 14 slides · 32 terms

| Term | Meaning | Tag |
|---|---|---|
| Dashboard as argument | A dashboard's layout and defaults make a case before any number is read. | in the chapter |
| Medium is the message | The form of a communication shapes its meaning before the content arrives (McLuhan). | in the chapter |
| Output-layer failure | A chart that misstates sound findings is a validation failure, not a later communication problem. | in the chapter |
| FT question taxonomy | Nine question families; state the question, find its family, then pick the chart. | in the chapter |
| Perception hierarchy | Readers judge some channels more accurately than others: position, length, angle, area, volume, color. | in the chapter |
| Common-scale position | Values shown by where points sit on one shared axis, the most accurately read channel. | in the chapter |
| Aleatoric uncertainty | Variability from sampling and chance that cannot be removed; intervals and error bars show it. | in the chapter |
| Uncertainty over effect | The margin of error is bigger than the difference reported, so the honest reading is a tie. | in the chapter |
| Epistemic uncertainty | The gap between what is known and what is true, from limits of data, instruments and proxies. | in the chapter |
| Validate first | Check that the data measures what the question asks before drawing anything from it. | in the chapter |
| Error bars | A point estimate with its spread; the chart must say what the bar is, such as a 95% CI. | in the chapter |
| Selective uncertainty | Showing intervals where they help the argument and leaving them off where they would hurt. | in the chapter |
| Interval bands | A shaded region behind a line for uncertainty; the width is carried by weak shading. | in the chapter |
| Cone of uncertainty | A forecast region sized to hold about two thirds of past track errors; it is not the storm's size. | in the chapter |
| Quantile dotplot | Twenty dots, a few filled, showing a probability as a count of cases the reader can see. | in the chapter |
| Natural frequencies | Probabilities stated as counts out of a number of cases, which readers reason with more correctly. | in the chapter |
| Equal visual weight | The uncertainty drawn as prominently as the estimate, so it reads as part of the finding. | in the chapter |
| False precision | More digits than the uncertainty supports, implying a certainty that is not there. | in the chapter |
| Truncated axes | A value axis that starts above zero, so a small difference looks large. | in the chapter |
| Inconsistent axes | Side-by-side panels with different axis ranges, so the visual comparison is invalid. | in the chapter |
| Scale trickery | A linear axis for data that is naturally logarithmic, or the reverse, changing which region looks big. | in the chapter |
| Axis inversion | An axis run against convention (zero at the top), so a rise can look like a fall. | in the chapter |
| Hiding the distribution | A mean or median that conceals a long tail or several clusters in the data. | in the chapter |
| Cherry-picked window | A time window that starts at a low and ends at a high to exaggerate a trend. | in the chapter |
| Missing baseline | A metric shown without the comparison that gives it meaning, such as a random guess or the old system. | in the chapter |
| Color asymmetry | Colors of unequal salience that steer the eye toward some categories and away from others. | in the chapter |
| Chartjunk and 3D | Decoration and 3D effects that carry no data and distort how big values look (Tufte). | in the chapter |
| Labels that prejudge | Titles and legend entries that state a conclusion before the reader sees the data. | in the chapter |
| Living deck | A deck that shows its own dated version history instead of posing as finished. | in the chapter |
| Changelog slide | The slide listing what changed since the last version and why; second to last in the deck. | in the chapter |
| Evidence-grade chart | A chart that shows what would make the conclusion wrong, such as comparison cases, not only support. | in the chapter |
| Non-author reader test | Ask someone who did not make the chart what it says; a mismatch means the chart is not working. | in the chapter |

## Communicating uncertainty

[Open the deck](decks/11%20Communicating%20uncertainty.html) · 14 slides · 34 terms

| Term | Meaning | Tag |
|---|---|---|
| Warranted assertion | Being entitled to claim something only in proportion to the evidence for it. | in the chapter |
| Verb taxonomy (the frozen ladder) | Eight claim verbs in one fixed order, hypothesize weakest to prove strongest. | in the chapter |
| Observe | What the data show under stated conditions, with no claim beyond them. | in the chapter |
| Find | Across the evidence examined, the result holds; needs replication. | in the chapter |
| Conclude | The motivating question is settled; strongest verb short of proof, rarely warranted. | in the chapter |
| Fluency-trap detector | Treating a strong verb in AI output as a flag, then asking what evidence stands behind it. | in the chapter |
| Verb downgrade | Swapping in the weaker verb the evidence supports; the facts stay, the posture drops. | in the chapter |
| Build and audit (build/audit pairing) | Calibrate verbs in a report you write, then downgrade them in an AI claim handed to you. | in the chapter |
| Layer 1 summary | Plain-English paragraph opening each section: what was found and why it matters. | in the chapter |
| Layer 2 technical detail | Methods, equations, tables and references for the reader who must evaluate. | in the chapter |
| Layer 3 appendix | Reproducibility detail: code, hyperparameters, data documentation, full sensitivity analyses. | in the chapter |
| Epistemic uncertainty | Uncertainty in what is known; more evidence would shrink it. | in the chapter |
| Aleatoric uncertainty | Uncertainty in the system itself; more data does not remove it. | in the chapter |
| Throat-clearing hedge | A qualifier that names no specific gap, such as “further work is needed”, so it carries no information. | in the chapter |
| Peer critique protocol | Six steps for specific review: strengths, verb mismatches, evasive hedges, structure, one question. | in the chapter |
| Calibration | When the model says 80%, it is right about 80% of the time. | in the chapter |
| Reliability diagram (calibration curve) | Mean confidence against actual accuracy, one point per bin; perfect is the diagonal. | in the chapter |
| Overconfidence | Stated probability above what is warranted: the curve falls below the diagonal. | in the chapter |
| Underconfidence | Stated probability below what is warranted: the curve rises above the diagonal. | in the chapter |
| Brier score | Mean squared gap between predicted probability and the 0 or 1 outcome. | in the chapter |
| Proper scoring rule | A score that is best, in expectation, only when the model reports the true probability. | in the chapter |
| Brier decomposition (Murphy, 1973) | Uncertainty, minus resolution, plus calibration error. | in the chapter |
| Resolution (discrimination) | How far predictions vary around the base rate, so how well cases are told apart. | in the chapter |
| ECE (Expected Calibration Error) | Bin the predictions, then average the gap between confidence and accuracy, weighted by bin size. | in the chapter |
| Bin dependence | ECE changes with the number and width of bins, so the binning must be reported. | in the chapter |
| MCE (Maximum Calibration Error) | The largest bin gap instead of the average: the worst confidence range. | in the chapter |
| Subgroup ECE | ECE computed per named subgroup, then compared with the global ECE. | in the chapter |
| Epic Sepsis Model | A sepsis alert used in hundreds of hospitals; Wong et al. (2021) tested it outside its developer. | in the chapter |
| External validation | Testing at an outside site with its own patients, where the model was never validated. | in the chapter |
| Evidence ladder (calibration evidence ladder) | Six levels, L0 to L5, of calibration evidence, each licensing one verb. | in the chapter |
| Temperature scaling | Divide the logits by one learned T before the softmax: softer confidence, same predicted class. | in the chapter |
| Calibration set | Held-out data used only to fit T, after the model's weights are fixed. | in the chapter |
| Distribution shift | The deployment population differs from the calibration population, so the fix no longer holds. | in the chapter |
| Conformal prediction | Returns a set of labels covering the truth at least 1 − α of the time, if the data are exchangeable. | in the chapter |

## Accountability

[Open the deck](decks/12%20Accountability.html) · 14 slides · 30 terms

| Term | Meaning | Tag |
|---|---|---|
| Sign-off | The point where a person puts a name to work and takes responsibility for it. | in the exam-term list only |
| Necessary not sufficient | Each party's choice was needed for the failure; none alone was enough to cause it. | in the chapter |
| Responsibility gap | Nobody can fairly be blamed for what a learning machine did when nobody could predict it. | in the chapter |
| Meaningful human control | Design the system so a human sits at each point where someone must answer. | in the chapter |
| Shape versus substance | Looks like accountability, with a name and a claim of review, but no review stands behind it. | in the chapter |
| Answerability | Willingness to revise the work, face those who relied on it, and bear the cost if it was wrong. | in the chapter |
| Stakes | Something to lose if the judgment is wrong; a sanction only bites on a party that has it. | in the chapter |
| Episodic memory | Recall of specific past events in context; a model holds stored text, not a history of its own acts. | in the chapter |
| Moral salience | Whether a system can be harmed or hold standing; shame and regret, which sanctions use, need it. | in the chapter |
| Metacognition | Checking one's own reasoning; a model's self-check comes from the same system being checked. | in the chapter |
| Validator independence | A check counts only when it comes from outside the system being checked. | in the chapter |
| Common cause failure | Two checks built alike fail together; a monitor shares the blind spots of what it watches. | in the chapter |
| Gödel analogy | Gödel's result motivates distrust of self-certification, but it is an analogy and not a proof about AI. | in the chapter |
| Seven-tier taxonomy | Seven tiers of human capacity sorted by AI strength; the source is unpublished, so the labels are scaffolding. | in the chapter |
| Tier 4: supervisory | Metacognitive and supervisory work: auditing plausibility, framing the problem, judging meaning. | in the chapter |
| Plausibility auditor | A person with domain depth and AI-failure knowledge who judges whether outputs match reality. | in the chapter |
| Kantian framework | Responsibility follows the capacity to act otherwise multiplied by the duty the situation imposed. | in the chapter |
| Utilitarian framework | Hold accountable whoever it most improves outcomes to hold: deterrence, incentives, less harm. | in the chapter |
| Upstream leverage | Earlier choices, such as framework defaults, change the conditions for many deployments at once. | in the chapter |
| Specifications | A written task definition with acceptance criteria; a failure is a divergence from it. | in the chapter |
| Audit trail | A per-action record; capturing it is mechanical, reading it against the world is not. | in the chapter |
| Recourse | A channel where an affected person can contest a decision and be heard. | in the chapter |
| Independent review | A reviewer outside the deployment team with authority to halt or revise. | in the chapter |
| Sanctions | A consequence, internal or external, that attaches to a named accountable human. | in the chapter |
| Attestation | A document of four parts: what was tested, what was not, who cleared each gate, calibrated verbs. | in the chapter |
| What was NOT tested | The conditions and failure modes the validation did not probe, written down as declared limits. | in the chapter |
| Authority to withhold | The signer's power to refuse the signature and say the gate is not cleared. | in the chapter |
| Pearl's Rung 3 | Counterfactual reasoning: what would have happened to this case had one thing been different. | in the chapter |
| Counterfactual (regime) (also governance counterfactual) | Ask which regime, put in place earlier, would have prevented a documented failure. | in the chapter |
| Regime failure | A failure caused by the rules, reviews and incentives around a system, not by its algorithm. | in the chapter |

## The limits of AI

[Open the deck](decks/13%20The%20limits%20of%20AI.html) · 14 slides · 34 terms

| Term | Meaning | Tag |
|---|---|---|
| Capability scaling | Making a model bigger or giving it more data. | in the chapter |
| Functionalist objection | The reply that scaling shrinks the limit to nothing. | in the chapter |
| Data-world gap | A model is competent over its data, not the world; the data is always less than the world. | in the chapter |
| Categorical vs frequent | A categorical limit stays however much scaling cuts the error rate. | in the chapter |
| Meaning | What a symbol refers to in the world; the user supplies it, the system does not. | in the chapter |
| Semantic work | The supervisor mapping an output's symbols to their referents in the deployment. | in the chapter |
| Intentionality | Aboutness: what an output is directed at. It follows the reader, not a stable aim. | in the chapter |
| Hume's induction problem | No non-circular reason to expect the unobserved to resemble the observed. | in the chapter |
| Complementarity | A wider sample and the region it excludes always split the same world. | in the chapter |
| Categorical boundary | The edge of the sample, where the gap lives; scaling moves it, never removes it. | in the chapter |
| Structural limit | A limit built into what a sample is, not an obstacle to engineer around. | in the chapter |
| Mediocristan | A world where no single outlier dominates the average, such as heights. | in the chapter |
| Extremistan | A world where one outlier can outweigh all the rest, such as wealth. | in the chapter |
| Turkey problem | Confidence rises every day on evidence that fails on day 1,001. | in the chapter |
| Black swan | A rare event that no in-distribution data could have anticipated. | in the chapter |
| Validation set | Held-out data from the training distribution, used to test performance. | in the exam-term list only |
| Distribution shift | Deployment inputs drift away from the data the model learned on. | in the exam-term list only |
| Wrong tests | Tests scoped to the question the system answers, not the question the world asks. | in the chapter |
| Turing's argument | If behaviour is enough evidence for human minds, demanding more of machines is unprincipled. | in the chapter |
| Chinese Room | Following rules on symbols can look like understanding without being it. | in the chapter |
| Overclaiming | Crediting either argument with a stronger claim than it made. | in the chapter |
| Operational stance | Test behaviour seriously and also invoke the limits: do both. | in the chapter |
| Skepticism as method | Where the limits barely bite, skepticism verifies, monitors and calibrates. | in the chapter |
| Skepticism as safety | Where the limits bite, the supervisor's doubt is itself the safeguard. | in the chapter |
| Epic Sepsis Model | A real sepsis alert tool that did far worse in outside validation than marketed. | in the chapter |
| Circular signal | A model that learns to confirm a suspicion the clinician already has. | in the chapter |
| Override infrastructure | The time, authority and legibility that make an override a practice. | in the chapter |
| Fictitious override | An override on paper that staff have no time or standing to use. | in the chapter |
| Stop condition | A case where the limits and the stakes together mean: do not deploy. | in the chapter |
| Authority to refuse | The supervisor's power to refuse deployment; the most important authority. | in the chapter |
| Delegate freely | Mechanical, well-defined procedures whose output you can check by inspection. | in the chapter |
| Delegate and verify | Interpretive claims: plausible output that you must check against the world. | in the chapter |
| Do not delegate | Problem formulation, plausibility auditing, judgment under stakes, sign-off. | in the chapter |
| Accountability | Being answerable for the cost of being wrong, which only a person can carry. | in the chapter |

---

## Alphabetical index

| Term | Deck | Meaning |
|---|---|---|
| Access boundary | Data validation | The data's reach is the schema plus everything its contents point to. |
| Accountability | The limits of AI | Being answerable for the cost of being wrong, which only a person can carry. |
| Accountable owner | Bias: where it enters and who is responsible | Whoever controls the node at the leverage point. |
| Accurate but misleading | Model explainability | True about the model, yet leaves the reader believing something false about the world. |
| Adaptive attack | Robustness | An attack built with knowledge of the defense, so it is designed to get past it. |
| Additivity | Model explainability | Values for two models combined are the sums of the values for each. |
| Adversarial example | Robustness | An input nudged on purpose so the answer flips while a person sees no real change. |
| Adversarial testing | Robustness | Testing with inputs built to fool the model, to see what it relies on. |
| Adversarial training | Robustness | Training on the worst-case perturbed input found at each step. |
| AI Use Disclosure | Delegation and trust | A per-step record of how AI was used: the tool, the request, the output, what was checked, what changed. |
| Aleatoric uncertainty | Visualization under validation | Variability from sampling and chance that cannot be removed; intervals and error bars show it. |
| Aleatoric uncertainty | Communicating uncertainty | Uncertainty in the system itself; more data does not remove it. |
| Alpha (α) | Fairness metrics | Sets whose unfairness counts more: low alpha the bottom, high alpha the top. |
| Answerability | Accountability | Willingness to revise the work, face those who relied on it, and bear the cost if it was wrong. |
| Artifact versus world | The skeptic’s toolkit | The artifact is what the system outputs; the world is the real thing it should say something about. |
| Association | Bias: where it enters and who is responsible | Seeing: P(Y / X), the chance of Y given that we observe X. |
| Attestation | Accountability | A document of four parts: what was tested, what was not, who cleared each gate, calibrated verbs. |
| Audience question | Model explainability | Ask who reads the explanation, what its words mean in their game, and whether it serves that game. |
| Audit trail | Validating agentic AI | The record of what the agent did, captured as it acts so it survives the action. |
| Audit trail | Delegation and trust | The record of inputs, decisions and outputs that lets a case be reconstructed afterwards. |
| Audit trail | Accountability | A per-action record; capturing it is mechanical, reading it against the world is not. |
| Audit trail clarity | Delegation and trust | Whether the AI's actions leave a trail that can be reviewed after the fact. |
| Authority laundering | Validating agentic AI | Data handed on as a legitimate output; the receiver cannot check where it came from. |
| Authority to refuse | The limits of AI | The supervisor's power to refuse deployment; the most important authority. |
| Authority to withhold | Accountability | The signer's power to refuse the signature and say the gate is not cleared. |
| Autonomy-competence gap | Validating agentic AI | Acting at a high autonomy level while understanding at a much lower one. |
| Awareness (FTA) | Fairness metrics | Decide openly how much group membership counts when judging similarity. |
| Axis inversion | Visualization under validation | An axis run against convention (zero at the top), so a rise can look like a fall. |
| Base rate | The confidence illusion | How common the thing is before any test. |
| Base rate | Fairness metrics | The share of a group that truly has the positive outcome. |
| Bayes' theorem | The confidence illusion | Prior × likelihood ÷ chance of the evidence. |
| Bayesian probability | The confidence illusion | A degree of belief that evidence updates. |
| Benefit | Fairness metrics | The number per person whose spread is measured: a score, a probability or an error flag. |
| Bias | Bias: where it enters and who is responsible | How far the estimate sits from the truth on average, over every dataset you might collect. |
| Biased measurement | Bias: where it enters and who is responsible | A stand-in variable distorted on the way, such as re-arrest recorded for crime. |
| Bin dependence | Communicating uncertainty | ECE changes with the number and width of bins, so the binning must be reported. |
| Black swan | The limits of AI | A rare event that no in-distribution data could have anticipated. |
| Black-box attack | Robustness | The attacker sees only outputs and estimates the gradient by probing. |
| Boondoggle Score | Delegation and trust | The course author's five-question heuristic for sorting sub-tasks; not validated outside the course. |
| Boundary leakage | Data validation | Private material escaping through a corpus's edge; hard to find at scale without red-teaming. |
| Boundary tilting | Robustness | A boundary running almost alongside the data, so a tiny step in a low-variance direction crosses it. |
| Brier decomposition | Communicating uncertainty | Uncertainty, minus resolution, plus calibration error. |
| Brier score | Communicating uncertainty | Mean squared gap between predicted probability and the 0 or 1 outcome. |
| Broken pipeline | Delegation and trust | Missing items 1 to 4 of the map: it cannot run, so the gap shows at once. |
| Budget cap, rate limit | Validating agentic AI | Hard limits on use per run or per period, which stop an unbounded process. |
| Build and audit | Communicating uncertainty | Calibrate verbs in a report you write, then downgrade them in an AI claim handed to you. |
| Calibrated trust | Delegation and trust | Reliance on the AI that matches its actual reliability for this kind of case. |
| Calibration | The confidence illusion | Stated confidence matches how often it comes true. |
| Calibration | Communicating uncertainty | When the model says 80%, it is right about 80% of the time. |
| Calibration baseline | The confidence illusion | Write 90% intervals for questions, then count how many hit. |
| Calibration curve | The confidence illusion | Stated probability across, actual frequency up; the diagonal is perfect. |
| Calibration parity | Bias: where it enters and who is responsible | A score means the same thing in every group. |
| Calibration parity | Fairness metrics | A stated probability means the same observed rate in every group. |
| Calibration set | Communicating uncertainty | Held-out data used only to fit T, after the model's weights are fixed. |
| Capability scaling | The limits of AI | Making a model bigger or giving it more data. |
| Cartesian doubt | The skeptic’s toolkit | Doubt a claim until you can list the conditions under which it would be wrong. |
| Cascading hallucination | Validating agentic AI | An error is passed on, relied on and magnified, so the system errs more than any one agent. |
| Categorical boundary | The limits of AI | The edge of the sample, where the gap lives; scaling moves it, never removes it. |
| Categorical vs frequent | The limits of AI | A categorical limit stays however much scaling cuts the error rate. |
| Causal graph | Bias: where it enters and who is responsible | Nodes for variables, arrows from cause to effect. |
| Central limit theorem | The confidence illusion | Averages of many independent, finite-variance values look bell-shaped. |
| Changelog slide | Visualization under validation | The slide listing what changed since the last version and why; second to last in the deck. |
| Channel ranking | Data validation | Position reads best, then length. Area and color intensity read worst. |
| Chartjunk and 3D | Visualization under validation | Decoration and 3D effects that carry no data and distort how big values look (Tufte). |
| Cherry-picked window | Visualization under validation | A time window that starts at a low and ends at a high to exaggerate a trend. |
| Chinese Room | The limits of AI | Following rules on symbols can look like understanding without being it. |
| Circular signal | The limits of AI | A model that learns to confirm a suspicion the clinician already has. |
| Circular verification | Validating agentic AI | Checking an identity by asking the unverified source to confirm itself. |
| Classical probability | The confidence illusion | Count the favourable outcomes out of equally likely ones. |
| Coalition | Model explainability | A subset of features treated as already known. |
| Cohen's kappa | Bias: where it enters and who is responsible | Agreement between two coders, corrected for the agreement chance alone would give. |
| Color asymmetry | Visualization under validation | Colors of unequal salience that steer the eye toward some categories and away from others. |
| Column type | Data validation | Numeric, count, nominal, ordinal, time or text. The right plot depends on it. |
| Common cause failure | Accountability | Two checks built alike fail together; a monitor shares the blind spots of what it watches. |
| Common-scale position | Visualization under validation | Values shown by where points sit on one shared axis, the most accurately read channel. |
| COMPAS | Fairness metrics | A recidivism risk tool whose 2016 audit set two true claims against each other. |
| Complementarity | The limits of AI | A wider sample and the region it excludes always split the same world. |
| Conclude | Communicating uncertainty | The motivating question is settled; strongest verb short of proof, rarely warranted. |
| Conditional probability | The confidence illusion | The chance of A once you know B has happened. |
| Conditional sampling | Model explainability | Draw the missing features given the known ones. Realistic, but the Dummy axiom can fail. |
| Cone of uncertainty | Visualization under validation | A forecast region sized to hold about two thirds of past track errors; it is not the storm's size. |
| Confirmation bias | Bias: where it enters and who is responsible | The researcher's prior steers what data is collected, kept and reported. |
| Conformal prediction | Communicating uncertainty | Returns a set of labels covering the truth at least 1 − α of the time, if the data are exchangeable. |
| Consequence system | Validating agentic AI | A model that acts, so its outputs are changes of state that cannot always be rewound. |
| Contextual privacy | Validating agentic AI | Information shared in one setting should not be forwarded into another. |
| Contingent failure | Validating agentic AI | A failure engineering can close, such as a missing tool or a missing budget cap. |
| Contingent luck | Validating agentic AI | Resisting an attack for a reason that would not hold next time. |
| Contract, not partition | Delegation and trust | A delegation sets out what the AI does, what the human does, the checkable handoff and what happens on failure. |
| Correlated features | Model explainability | Drawing each feature on its own creates combinations that never occur in real data. |
| Counterfactual | Robustness | What would have happened in this case had one thing been different. |
| Counterfactual | Model explainability | States how the prediction would change if a feature had another value. |
| Counterfactual | Bias: where it enters and who is responsible | Imagining: what would have happened to this case if X had been different. |
| Counterfactual (regime) | Accountability | Ask which regime, put in place earlier, would have prevented a documented failure. |
| Counterfactual fairness | Fairness metrics | Same decision for this person in another group. |
| Dashboard as argument | Visualization under validation | A dashboard's layout and defaults make a case before any number is read. |
| Data validation lens | Validating agentic AI | Asks what the agent's effective access really is, not what was written down. |
| Data-coding bias | Bias: where it enters and who is responsible | Systematic miscoding when judgment is needed to fit material into categories. |
| Data-entry bias | Bias: where it enters and who is responsible | Patterned transcription error, such as a buried code replaced by the nearest one. |
| Data-world gap | The limits of AI | A model is competent over its data, not the world; the data is always less than the world. |
| Dataset bias | Bias: where it enters and who is responsible | The training sample does not represent the deployment population. |
| Datasheets for Datasets | Data validation | Gebru et al.: 57 questions in seven sections that document a dataset's life. |
| Decorative number | The confidence illusion | A confident figure nobody has checked against outcomes. |
| Defended choice | Fairness metrics | The deliverable: a chosen metric with written reasons, in six steps. |
| Delegate and verify | The limits of AI | Interpretive claims: plausible output that you must check against the world. |
| Delegate freely | The limits of AI | Mechanical, well-defined procedures whose output you can check by inspection. |
| Delegation buckets | Delegation and trust | The three outcomes of the sort: AI executes, human only, or hybrid with human checks. |
| Delegation map | Delegation and trust | A written document giving each pipeline step an owner, inputs, outputs and a signal that it finished correctly. |
| Deliberation surface | Validating agentic AI | A private place to weigh options before acting, which leaves a trace of rejected ones. |
| Demographic parity | Fairness metrics | The model says yes at the same rate in every group. |
| Detection-based defense | Robustness | Flags suspected adversarial inputs and routes them to a fallback or a person. |
| Direct effect | Fairness metrics | The attribute alone moves the prediction. |
| Displayed identity | Validating agentic AI | A name or label shown in a channel, which anyone can change. |
| Distribution match | Delegation and trust | Whether an input resembles what the AI was trained on or falls where it is undertrained. |
| Distribution shift | The skeptic’s toolkit | The world after deployment stops resembling the data the model learned from. |
| Distribution shift | The confidence illusion | The world after deployment stops matching the training data. |
| Distribution shift | Robustness | Deployment inputs stop resembling training inputs, with no attacker involved. |
| Distribution shift | Communicating uncertainty | The deployment population differs from the calibration population, so the fix no longer holds. |
| Distribution shift | The limits of AI | Deployment inputs drift away from the data the model learned on. |
| Do not delegate | Data validation | Rebuilding the frame stays with you; an AI version holds nothing you lacked. |
| Do not delegate | The limits of AI | Problem formulation, plausibility auditing, judgment under stakes, sign-off. |
| Drift | The skeptic’s toolkit | Inputs changing over time from what the model was built on, tracked with a score called PSI. |
| Dummy | Model explainability | A feature that changes nothing gets zero. A non-zero zip value means the model uses zip. |
| ECE | The confidence illusion | Bin-weighted average gap between stated and actual. |
| ECE | Communicating uncertainty | Bin the predictions, then average the gap between confidence and accuracy, weighted by bin size. |
| Effective data scope | Validating agentic AI | Everything that can be pulled out through the agent's access, indirect requests included. |
| Efficiency | Model explainability | The values add up exactly to the prediction minus the average. |
| Epic Sepsis Model | Communicating uncertainty | A sepsis alert used in hundreds of hospitals; Wong et al. (2021) tested it outside its developer. |
| Epic Sepsis Model | The limits of AI | A real sepsis alert tool that did far worse in outside validation than marketed. |
| Episodic memory | Accountability | Recall of specific past events in context; a model holds stored text, not a history of its own acts. |
| Epistemic frame | Data validation | Every unwritten decision about what was recorded, kept, joined and cut off. |
| Epistemic uncertainty | Visualization under validation | The gap between what is known and what is true, from limits of data, instruments and proxies. |
| Epistemic uncertainty | Communicating uncertainty | Uncertainty in what is known; more evidence would shrink it. |
| Equal FPR and FNR | Bias: where it enters and who is responsible | Wrongly flagged and missed shares match in every group. |
| Equal visual weight | Visualization under validation | The uncertainty drawn as prominently as the estimate, so it reads as part of the finding. |
| Equalized odds | Fairness metrics | Both error rates match across groups. |
| Error bars | Visualization under validation | A point estimate with its spread; the chart must say what the bar is, such as a 95% CI. |
| Estimator | Bias: where it enters and who is responsible | A procedure that turns data into a number, such as a mean or a risk score. |
| Event | The confidence illusion | Any group of outcomes you care about. |
| Evidence ladder | Communicating uncertainty | Six levels, L0 to L5, of calibration evidence, each licensing one verb. |
| Evidence-grade chart | Visualization under validation | A chart that shows what would make the conclusion wrong, such as comparison cases, not only support. |
| Executive integration | The skeptic’s toolkit | Combining outputs from tools, models and people into one decision that someone owns. |
| Executive integration | Delegation and trust | Combining outputs from several tools and people into one decision with named authority. |
| Explainability | Model explainability | A property of outputs: each one comes with a stated reason. |
| Explainability lens | Validating agentic AI | Asks whether the agent's account of its action matches the observed state. |
| Expressiveness | Data validation | Match the channel to the data type. Size on a category implies an order that is not there. |
| External validation | Communicating uncertainty | Testing at an outside site with its own patients, where the model was never validated. |
| Extremistan | The limits of AI | A world where one outlier can outweigh all the rest, such as wealth. |
| Failure routing | Delegation and trust | A declared escalation path for when a step fails, so someone is accountable. |
| Failure visibility | Delegation and trust | When something cannot be done, say so with a flag instead of inventing a plausible substitute. |
| Fairness lens | Validating agentic AI | Asks whose values govern the behaviour: the provider's, the owner's or an editor's. |
| False positive | The confidence illusion | A healthy case the test wrongly flags. |
| False precision | Visualization under validation | More digits than the uncertainty supports, implying a certainty that is not there. |
| False success report | Validating agentic AI | The agent says done while the world shows it is not, and nothing catches the mismatch. |
| False-positive rate | Fairness metrics | Of the people who truly are not positive, the share the model flags anyway. |
| False-success catch | Validating agentic AI | After an action, observe the world independently and compare it with the report. |
| Feature-engineering | Data validation | A column that is someone's model output, not raw data. |
| FGSM | Robustness | One step of size ε along the sign of the loss gradient. |
| Fictitious override | The limits of AI | An override on paper that staff have no time or standing to use. |
| Find | Communicating uncertainty | Across the evidence examined, the result holds; needs replication. |
| Fluency trap | The skeptic’s toolkit | Fluent output raises confidence in the answer, then in your own evaluation of it. |
| Fluency trap | Model explainability | Smooth, well-formed output taken as evidence it does not carry. |
| Fluency-trap detector | Communicating uncertainty | Treating a strong verb in AI output as a flag, then asking what evidence stands behind it. |
| Form versus content | The skeptic’s toolkit | How well an output reads and whether it is true are independent in AI output. |
| Formal verification | Robustness | A proof that a property holds for every input in a defined region. |
| Frequentist probability | The confidence illusion | The share of times it happens over a long run of repeats. |
| FT question taxonomy | Visualization under validation | Nine question families; state the question, find its family, then pick the chart. |
| Functionalist objection | The limits of AI | The reply that scaling shrinks the limit to nothing. |
| Fundamental failure | Validating agentic AI | A failure rooted in the architecture; a patch only changes its shape. |
| Funnel plot | Bias: where it enters and who is responsible | Effect size against precision; an empty lower-left corner shows the missing small null studies. |
| Gap analysis | Data validation | The difference between the locked prediction and the traced frame is what you learned. |
| Gap from the start | The skeptic’s toolkit | The stand-in never matched the target; catch it by asking what the number is a number of. |
| Gap that opens later | The skeptic’s toolkit | The measure matched at first, then the world moved; only checking again and again catches it. |
| Gating condition | Validating agentic AI | A confirmation from the owner required before an irreversible action may run. |
| GE decomposition | Fairness metrics | Total unfairness equals the within-group part plus the between-group part. |
| GE Index | Fairness metrics | One number for how unequally benefit is spread across people, as in income inequality. |
| Gödel analogy | Accountability | Gödel's result motivates distrust of self-certification, but it is an analogy and not a proof about AI. |
| Goodhart’s law | The skeptic’s toolkit | When a measure becomes a target, it ceases to be a good measure. |
| Governance question | Robustness | Asks whether the model would differ had the institutions around it differed. |
| Graded testability | Delegation and trust | Testability has tiers: some conditions any outsider can check, some only a qualified reviewer. |
| Group fairness | Fairness metrics | Fairness judged by comparing aggregate rates across whole groups. |
| Handoff condition | Delegation and trust | The signal that a step finished correctly so the next can start; the load-bearing part of the map. |
| Heavy-tailed | The confidence illusion | Extremes are common enough that the average never settles. |
| Held-out test set | The skeptic’s toolkit | Data kept back from the builders and used only to score the model on cases it never saw. |
| Hiding the distribution | Visualization under validation | A mean or median that conceals a long tail or several clusters in the data. |
| Hierarchical mapping | Delegation and trust | Mapping by component, in step-by-step detail only at high-stakes interfaces and seams. |
| Historical bias | Bias: where it enters and who is responsible | A faithful, representative record of a world you did not want to reproduce; its accuracy is the harm. |
| Hume's induction problem | The confidence illusion | The past does not guarantee the future; the world must cooperate. |
| Hume's induction problem | The limits of AI | No non-circular reason to expect the unobserved to resemble the observed. |
| Identity confusion | Validating agentic AI | An agent takes its own earlier messages in a shared channel for a second agent. |
| Implicit bias | Bias: where it enters and who is responsible | The unconscious associations of the people in the pipeline; the medium other biases swim in. |
| Impossibility theorem | Bias: where it enters and who is responsible | With unequal base rates, not all three can hold at once. |
| Impossibility theorem | Fairness metrics | With unequal base rates, calibration and equal error rates cannot both hold. |
| In-processing | Fairness metrics | Change the training objective, for example by adding a fairness penalty. |
| Inconsistent axes | Visualization under validation | Side-by-side panels with different axis ranges, so the visual comparison is invalid. |
| Independence | The confidence illusion | Knowing one event tells you nothing about the other. |
| Independent review | Accountability | A reviewer outside the deployment team with authority to halt or revise. |
| Indirect effect | Fairness metrics | Attribute moves a mediator, which moves prediction. |
| Individual fairness | Fairness metrics | Similar people should be treated similarly, even when group totals balance. |
| Input preprocessing | Robustness | Denoising, quantizing or smoothing the input before the model sees it. |
| Institutional skepticism | The skeptic’s toolkit | The moves written into the checklist and the workflow instead of left to memory. |
| Intentionality | The limits of AI | Aboutness: what an output is directed at. It follows the reader, not a stable aim. |
| Internal accounting | Model explainability | How the model itself divides credit among features. Real, and not the same as the world. |
| Interpretability | Model explainability | A person can build a mental model good enough to predict new cases. |
| Interpretive judgment | The skeptic’s toolkit | Reading an output in its domain: the same number means different things in different deployments. |
| Interpretive judgment | Delegation and trust | Reading the output in its deployment context and recording what it means for the decision. |
| Interval bands | Visualization under validation | A shaded region behind a line for uncertainty; the width is carried by weak shading. |
| Intervention | Bias: where it enters and who is responsible | Doing: P(Y / do(X = x)), the chance of Y if we set X to a value. |
| Inverse prob. weighting | Bias: where it enters and who is responsible | Weight each kept case by 1 over its chance of being kept, so it stands in for those dropped. |
| IQR rule | Data validation | Flag values below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR. |
| Irreducibly human | Delegation and trust | A step the AI cannot take because it needs domain knowledge, domain judgment or responsibility. |
| Kantian framework | Accountability | Responsibility follows the capacity to act otherwise multiplied by the duty the situation imposed. |
| Kantian slice | The skeptic’s toolkit | You only ever see a slice of the world; keep in view what lies outside it. |
| Label assumption | Data validation | The label is a proxy, not the thing you care about. |
| Label bias | Bias: where it enters and who is responsible | The labels record a biased process, so the model predicts a distorted stand-in. |
| Labels that prejudge | Visualization under validation | Titles and legend entries that state a conclusion before the reader sees the data. |
| Language game | Model explainability | The setting that gives a word its meaning, so one word can mean different things. |
| Language-game mismatch | Model explainability | Two parties use one word for different operations, so a true report misleads. |
| Layer 1 summary | Communicating uncertainty | Plain-English paragraph opening each section: what was found and why it matters. |
| Layer 2 technical detail | Communicating uncertainty | Methods, equations, tables and references for the reader who must evaluate. |
| Layer 3 appendix | Communicating uncertainty | Reproducibility detail: code, hyperparameters, data documentation, full sensitivity analyses. |
| Leverage | Bias: where it enters and who is responsible | How much bias-carrying flow an action blocks. |
| Leverage analysis | Bias: where it enters and who is responsible | List every path; find the fix that blocks most. |
| Likelihood | The confidence illusion | Chance of the evidence if the hypothesis is true. |
| LIME | Model explainability | Fits a simple line to the model’s output around one input. The slope is the explanation. |
| LIME instability | Model explainability | The perturbations are random, so the same input can give a different explanation each run. |
| Limit of induction | The skeptic’s toolkit | Each correct prediction adds no logical guarantee that the next one will be right. |
| Linearity hypothesis | Robustness | Tiny pushes on thousands of inputs add up to a large change in a locally linear score. |
| Lipschitz condition | Fairness metrics | The difference in treatment may not exceed the difference between the people. |
| Lipschitz constant | Robustness | The most the output can change per unit change of the input. |
| Living deck | Visualization under validation | A deck that shows its own dated version history instead of posing as finished. |
| Loss | The confidence illusion | What being wrong costs, not how often it happens. |
| Low-variance direction | Robustness | A direction in which the training data barely varies, so training gave little signal. |
| MAR | Data validation | Missing at random: gaps follow a column you see. |
| Marginal contribution | Model explainability | What one feature adds to the prediction when it joins a coalition. |
| Marks and channels | Data validation | A mark is the shape drawn per row; a channel is the visual property carrying a value. |
| MCAR | Data validation | Missing completely at random: no pattern at all. |
| MCE | Communicating uncertainty | The largest bin gap instead of the average: the worst confidence range. |
| Meaning | The limits of AI | What a symbol refers to in the world; the user supplies it, the system does not. |
| Meaningful human control | Accountability | Design the system so a human sits at each point where someone must answer. |
| Measure versus want | The skeptic’s toolkit | The number a system is scored on is a stand-in for what its builders actually need. |
| Mediocristan | The limits of AI | A world where no single outlier dominates the average, such as heights. |
| Medium is the message | Visualization under validation | The form of a communication shapes its meaning before the content arrives (McLuhan). |
| Metacognition | Accountability | Checking one's own reasoning; a model's self-check comes from the same system being checked. |
| Missing baseline | Visualization under validation | A metric shown without the comparison that gives it meaning, such as a random guess or the old system. |
| Missingness matrix | Data validation | Dark where missing; stripes mean columns fail together. |
| MNAR | Data validation | Missing not at random: gaps follow the value. |
| Monitoring gap | Delegation and trust | The distance between the monitoring data a deployment holds and the data anyone reviews. |
| Monitoring specification | Robustness | What is watched in production, and what triggers review or rollback. |
| Moral salience | Accountability | Whether a system can be harmed or hold standing; shame and regret, which sanctions use, need it. |
| Multiplication rule | The confidence illusion | Chance of both: each step's chance given the steps before it (the chain rule). |
| Natural adversarial | Robustness | No attacker: a rare, long-tail input the model never generalized to. |
| Natural frequencies | Visualization under validation | Probabilities stated as counts out of a number of cases, which readers reason with more correctly. |
| Necessary not sufficient | Accountability | Each party's choice was needed for the failure; none alone was enough to cause it. |
| No tool yet | The skeptic’s toolkit | The call that nobody yet knows how to do this well enough to deploy, so nothing is deployed. |
| Non-author reader test | Visualization under validation | Ask someone who did not make the chart what it says; a mismatch means the chart is not working. |
| Non-robust features | Robustness | Fine-grained patterns tied to the label in training that a small push can move. |
| Observability modeling | Validating agentic AI | Knowing which channels are visible to whom; private reasoning alone does not supply it. |
| Observe | Communicating uncertainty | What the data show under stated conditions, with no claim beyond them. |
| Observer bias | Bias: where it enters and who is responsible | A labeler's prior leaks into the label, so labels track what the labeler already believed. |
| Off-manifold | Model explainability | Perturbed inputs that no real case resembles, where the line may describe nothing real. |
| Open-ended loss | Validating agentic AI | A wrong action costs as much as the agent's reach allows, not just one bad answer. |
| Operational form | Delegation and trust | The concrete, documented version of a capacity that a pipeline contains: no artifact, no capacity. |
| Operational stance | The limits of AI | Test behaviour seriously and also invoke the limits: do both. |
| Outlier | Data validation | An extreme value flagged as a candidate. A person decides what it is. |
| Output-layer failure | Visualization under validation | A chart that misstates sound findings is a validation failure, not a later communication problem. |
| Overclaiming | The limits of AI | Crediting either argument with a stronger claim than it made. |
| Overconfidence | The confidence illusion | Stated confidence runs above how often the model is right. |
| Overconfidence | Communicating uncertainty | Stated probability above what is warranted: the curve falls below the diagonal. |
| Override infrastructure | The limits of AI | The time, authority and legibility that make an override a practice. |
| Overtrust | Delegation and trust | Accepting AI output that should be checked, so errors surface later and quietly. |
| Partition | The confidence illusion | Non-overlapping pieces that cover every case. |
| Patch attack | Robustness | A large change in a small region, such as a sticker or printed pattern. |
| Pearl's ladder | Robustness | Three levels of causal question: seeing, doing, imagining. |
| Pearl's ladder | Bias: where it enters and who is responsible | Three levels of causal reasoning: seeing, doing, imagining. |
| Pearl's Rung 3 | Accountability | Counterfactual reasoning: what would have happened to this case had one thing been different. |
| Pearson correlation | Data validation | A score for straight-line association only. y = x² can score near zero. |
| Peer critique protocol | Communicating uncertainty | Six steps for specific review: strengths, verb mismatches, evasive hedges, structure, one question. |
| Perception hierarchy | Visualization under validation | Readers judge some channels more accurately than others: position, length, angle, area, volume, color. |
| Perturbation budget (ε) | Robustness | The most any one input value may change (the L∞ budget). |
| PGD | Robustness | Many small gradient-sign steps, each projected back into the ε-ball. |
| Plato's Cave | Data validation | A dataset is shadows on a wall. EDA measures the shadows, not the fire. |
| Plausibility auditing | The skeptic’s toolkit | Asking whether an output is even the kind of thing that could be true, given what you know. |
| Plausibility auditing | The confidence illusion | Hearing the wrong note in a number before you can prove it wrong. |
| Plausibility auditing | Delegation and trust | Checking whether an output could be true of the world it describes, with a recorded checklist. |
| Plausibility auditor | Accountability | A person with domain depth and AI-failure knowledge who judges whether outputs match reality. |
| Popperian falsifiability | The skeptic’s toolkit | A claim must name the metric, threshold and window that would show it false. |
| Post-hoc explanation | Model explainability | A reason worked out after the model has produced its output. |
| Post-processing | Fairness metrics | Change predictions afterwards, for example with a threshold per group. |
| Posterior | The confidence illusion | Belief after the evidence: prior updated. |
| PPV | The confidence illusion | Of everything flagged, the share that is real. |
| Pre-processing | Fairness metrics | Change the training data first, for example by reweighting. |
| Prediction system | Validating agentic AI | A model whose outputs are statements about the world; a wrong one is wrong for one input. |
| Prediction-lock | The skeptic’s toolkit | Write your prediction before seeing the result and never revise it; append what you observed. |
| Prediction-lock | Data validation | A written, dated prediction of the dataset's frame, made before any plot. |
| Predictive value (PPV) | Fairness metrics | Of the people the model flags, the share who truly are positive. |
| Prior | The confidence illusion | What you believed before seeing the evidence. |
| Problem formulation | The skeptic’s toolkit | Stating the question the system answers and checking it is the question you need answered. |
| Problem formulation | Delegation and trust | Writing down the question, the criteria and when AI is the right tool, before the AI is invoked. |
| Procedural EDA | Data validation | The standard pass: types, shape, distributions, missingness, correlations, outliers. |
| Prompt injection | Robustness | Instructions hidden in data the agent reads, which it treats as commands. |
| Prompt injection | Validating agentic AI | Instructions slipped in as data; the model reads both as the same kind of token. |
| Prompt sensitivity | Robustness | Prompts that mean the same thing get noticeably different answers. |
| Proper scoring rule | Communicating uncertainty | A score that is best, in expectation, only when the model reports the true probability. |
| Provenance tracking | Validating agentic AI | A record of what each agent passed to which other, and where it first came from. |
| Proxy | Robustness | A signal that tracked the right label in training but is not the thing itself. |
| Proxy | Bias: where it enters and who is responsible | A feature correlated with the protected attribute. |
| Proxy | Fairness metrics | A feature such as zip code that reveals group membership indirectly. |
| Publication bias | Bias: where it enters and who is responsible | Significant results get published and nulls stay in drawers, so the literature looks stronger. |
| Quantile dotplot | Visualization under validation | Twenty dots, a few filled, showing a probability as a count of cases the reader can see. |
| Randomized smoothing | Robustness | Vote over many noisy copies of the input; a clear winner gives a certified radius R. |
| Recording instrument | Data validation | The sensor, form or system that did the recording, and what it could not see. |
| Recourse | Accountability | A channel where an affected person can contest a decision and be heard. |
| Regime failure | Accountability | A failure caused by the rules, reviews and incentives around a system, not by its algorithm. |
| Reliability diagram | Communicating uncertainty | Mean confidence against actual accuracy, one point per bin; perfect is the diagonal. |
| Residual risk disclosure | Robustness | A written list of known weaknesses that were not mitigated. |
| Resolution | Communicating uncertainty | How far predictions vary around the base rate, so how well cases are told apart. |
| Resource exhaustion | Validating agentic AI | Agents together, or an outside sender, use up tokens, memory or server capacity. |
| Responsibility gap | Accountability | Nobody can fairly be blamed for what a learning machine did when nobody could predict it. |
| Reversibility | Delegation and trust | Whether an action can be undone; irreversible ones need a human approval gate. |
| Rhetorical claim | The skeptic’s toolkit | A claim no observation could contradict: noise in technical language, not engineering. |
| Robust features | Robustness | Patterns tied to the label that survive small changes, such as shape. |
| Robustness lens | Validating agentic AI | Asks whether social pressure or spoofing across channels can flip the behaviour. |
| Robustness profile | Robustness | What the model resists and what it does not, by attack, budget and shift, not one number. |
| Robustness trade-off | Robustness | Gaining robustness tends to cost accuracy on ordinary inputs. |
| Row tracing | Data validation | Pick one row and follow its values back through every source system. |
| Row-count question | Data validation | Ask why the table has exactly this many rows, and how many it should have had. |
| Rudin’s argument | Model explainability | For high-stakes decisions, use interpretable models rather than explaining black boxes. |
| Runaway loop | Validating agentic AI | A process that repeats with no stopping condition. |
| Rung 1 (association) | Model explainability | The level of seeing what goes with what, or what the model used. SHAP stays here. |
| Rung 2 (intervention) | Model explainability | The level of doing: what happens if X is set to a value. SHAP cannot answer it. |
| Sample space | The confidence illusion | The list of every outcome that could happen. |
| Sampling (KernelSHAP) | Model explainability | Estimate the values from M random orderings instead of all of them. |
| Sampling assumption | Data validation | The data is whoever was easy to reach; deployment meets everyone. |
| Sampling bias | Bias: where it enters and who is responsible | Some groups are underrepresented because they were hard to reach, not because of their outcomes. |
| Sanctions | Accountability | A consequence, internal or external, that attaches to a named accountable human. |
| Scale trickery | Visualization under validation | A linear axis for data that is naturally logarithmic, or the reverse, changing which region looks big. |
| Selection bias | Bias: where it enters and who is responsible | Who ends up in the sample depends on what happened to them, so the sample average is off. |
| Selective uncertainty | Visualization under validation | Showing intervals where they help the argument and leaving them off where they would hurt. |
| Self-model | Validating agentic AI | What the agent's actions reach and when it is out of its depth; without it, done is reported early. |
| Self-report bias | Bias: where it enters and who is responsible | People misreport themselves in a consistent direction, such as voting more than they did. |
| Semantic invariance | Robustness | The answer stays the same when the input is reworded without changing its meaning. |
| Semantic work | The limits of AI | The supervisor mapping an output's symbols to their referents in the deployment. |
| Sensitivity | The confidence illusion | Of the truly sick, the share flagged. |
| Sentinel value | Data validation | A placeholder such as 999 or N/A standing in for unknown. |
| Seven-tier taxonomy | Accountability | Seven tiers of human capacity sorted by AI strength; the source is unpublished, so the labels are scaffolding. |
| SHAP | Model explainability | A feature-attribution method from game theory: one number per feature, for one prediction. |
| Shape versus substance | Accountability | Looks like accountability, with a name and a claim of review, but no review stands behind it. |
| Shapley value | Model explainability | A feature’s marginal contribution, averaged over every order of arrival. |
| Shortcut | Model explainability | A spurious pattern that matches the label in training and fails on new data. |
| Sign-off | Accountability | The point where a person puts a name to work and takes responsibility for it. |
| Sign-off authority | Delegation and trust | A named human who is the accountable decision-maker for the pipeline's outputs. |
| Silent join drop | Data validation | Rows with no match across the sources vanish from the merge, with no error. |
| Similarity metric d | Fairness metrics | A task-specific measure of how alike two people are, and a values choice. |
| Skepticism | The skeptic’s toolkit | A method, not a mood: moves performed on a claim, which can be taught and whose use can be seen. |
| Skepticism as method | The limits of AI | Where the limits barely bite, skepticism verifies, monitors and calibrates. |
| Skepticism as safety | The limits of AI | Where the limits bite, the supervisor's doubt is itself the safeguard. |
| Solve-verify asymmetry | The skeptic’s toolkit | In computer science checking is easier than finding; in AI deployment, producing is cheap and verifying is costly. |
| Solve-verify asymmetry | Delegation and trust | Checking an answer is easier than finding it; that gap is why AI help is worth having. |
| Specifications | Accountability | A written task definition with acceptance criteria; a failure is a divergence from it. |
| Specificity | The confidence illusion | Of the healthy, the share cleared. |
| Spurious effect | Fairness metrics | A confounder links them with no causal path. |
| Stakeholder model | Validating agentic AI | Who the agent serves and who its actions affect; without it, the most urgent speaker wins. |
| Stakes | Delegation and trust | The cost of being wrong on a step; when one error is catastrophic, the average is the wrong statistic. |
| Stakes | Accountability | Something to lose if the judgment is wrong; a sanction only bites on a party that has it. |
| Stop condition | The limits of AI | A case where the limits and the stakes together mean: do not deploy. |
| Structural bias | Bias: where it enters and who is responsible | Good data, accurate labels, correct model, and still unfair outcomes because of the world it is deployed into. |
| Structural causal model | Fairness metrics | Variables with arrows for which causes which. |
| Structural limit | The limits of AI | A limit built into what a sample is, not an obstacle to engineer around. |
| Subgroup ECE | Communicating uncertainty | ECE computed per named subgroup, then compared with the global ECE. |
| Supervisory log | Delegation and trust | A disclosure read as a whole: where the person used each capacity, with evidence behind it. |
| Symmetry | Model explainability | Features that do the same work get the same credit. |
| Temperature scaling | The confidence illusion | Divide the logits by one fitted T: same ranking, softer confidence. |
| Temperature scaling | Communicating uncertainty | Divide the logits by one learned T before the softmax: softer confidence, same predicted class. |
| Testable | Delegation and trust | A stranger who did not build the pipeline can read the condition, look at the system and tell if it was met. |
| Three axioms | The confidence illusion | No negatives, the total is 1, and exclusive outcomes add. |
| Threshold | Fairness metrics | The score cutoff above which the model says yes. |
| Throat-clearing hedge | Communicating uncertainty | A qualifier that names no specific gap, such as “further work is needed”, so it carries no information. |
| Tier 4: supervisory | Accountability | Metacognitive and supervisory work: auditing plausibility, framing the problem, judging meaning. |
| Time-window assumption | Data validation | Trained on one period, deployed into a shifted one. |
| Tool orchestration | The skeptic’s toolkit | Choosing which tool fits which sub-problem: AI, human judgment, another model, or none. |
| Tool orchestration | Delegation and trust | Deciding which tool owns each step and the handoff between tools; made concrete, it is the map. |
| Total probability | The confidence illusion | Weight each piece's chance by its share, add up. |
| Transfer attack | Robustness | A perturbation crafted on a surrogate model that also fools the target. |
| Transparency | Model explainability | A property of the system: its code, weights, architecture and data can be inspected. |
| TreeSHAP | Model explainability | Exact values for tree models, found by walking the few paths that change a prediction. |
| True-positive rate | Fairness metrics | Of the people who truly are positive, the share the model flags. |
| Truncated axes | Visualization under validation | A value axis that starts above zero, so a small difference looks large. |
| Turing's argument | The limits of AI | If behaviour is enough evidence for human minds, demanding more of machines is unprincipled. |
| Turkey problem | The limits of AI | Confidence rises every day on evidence that fails on day 1,001. |
| Unawareness (FTU) | Fairness metrics | Drop the sensitive attribute from the model and call it fair. |
| Unbiased estimator | Bias: where it enters and who is responsible | Averages out to the true value, though it may miss on any one dataset. |
| Uncertainty over effect | Visualization under validation | The margin of error is bigger than the difference reported, so the honest reading is a tie. |
| Underconfidence | Communicating uncertainty | Stated probability below what is warranted: the curve rises above the diagonal. |
| Undertrust | Delegation and trust | Systematically discounting AI output even when it is reliable, so the value is lost. |
| Unsupervised pipeline | Delegation and trust | Missing items 5 to 8: it runs fine until an uncaught error surfaces downstream. |
| Upstream leverage | Accountability | Earlier choices, such as framework defaults, change the conditions for many deployments at once. |
| Utilitarian framework | Accountability | Hold accountable whoever it most improves outcomes to hold: deterrence, incentives, less harm. |
| Validate first | Visualization under validation | Check that the data measures what the question asks before drawing anything from it. |
| Validation set | The limits of AI | Held-out data from the training distribution, used to test performance. |
| Validator independence | Accountability | A check counts only when it comes from outside the system being checked. |
| Value function | Model explainability | The expected prediction when only the features in a set S are known. |
| Values claim | Bias: where it enters and who is responsible | Choosing a metric is choosing which error you accept. |
| Values claim | Fairness metrics | The belief about who should bear errors that a choice of metric carries. |
| Verb downgrade | Communicating uncertainty | Swapping in the weaker verb the evidence supports; the facts stay, the posture drops. |
| Verb taxonomy | Communicating uncertainty | Eight claim verbs in one fixed order, hypothesize weakest to prove strongest. |
| Verification cost | Delegation and trust | How costly a human check is; near-redo checks quietly push people to accept the output. |
| Verified identity | Validating agentic AI | Identity confirmed by a check a changed name cannot fake, such as multi-factor sign-in. |
| Warranted assertion | Communicating uncertainty | Being entitled to claim something only in proportion to the evidence for it. |
| What was NOT tested | Accountability | The conditions and failure modes the validation did not probe, written down as declared limits. |
| White-box attack | Robustness | The attacker has the weights and gradients. |
| Wrong tests | The limits of AI | Tests scoped to the question the system answers, not the question the world asks. |
| Z-score rule | Data validation | Flag values with /z/ > 3. The mean and spread it uses are pulled by the outliers. |
