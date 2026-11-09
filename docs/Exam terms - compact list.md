# Exam terms: the compact list, with the limited scope

What is on this list: Chapters 1 to 9, the "what uncertainty is and calibration" half of Chapter 11, and the one accountability point of Chapter 12. Not on it: Chapter 10 (visualization), the communicating half of Chapter 11, the rest of Chapter 12, Chapter 13 (marked not on the exam; to be confirmed in class), and the Chapter 5 methods LIME and SHAP (learn them, not on the exam). Table columns: term, the chapters that teach it, one plain sentence, and a flag. Full definitions, book sentences and examples are in "Exam terms - shortlist.md".

Flags: **book** = defined in one sentence in the book; *spread* = the book explains it across passages; *not in book* = common usage Bear named.

## Where the terms sit, by chapter

| Chapter | Terms in Parts A and B | of which Bear's priority terms |
|---|---|---|
| 1, The Skeptic's Toolkit | 15 | 9 |
| 2, The Confidence Illusion | 18 | 13 |
| 3, Data Validation | 12 | 7 |
| 4, Robustness | 7 | 5 |
| 5, Model Explainability | 14 | 6 |
| 6, Bias | 38 | 29 |
| 7, Fairness Metrics | 22 | 17 |
| 8, Validating Agentic AI | 15 | 14 |
| 9, Delegation and Trust | 13 | 5 |
| 10, Visualization Under Validation (not on the exam) | 1 | 0 |
| 11, Communicating Uncertainty (half) | 12 | 8 |
| 12, Accountability (one point) | 4 | 1 |
| 13, The Limits of AI (not on the exam) | 4 | 1 |

## Bear's priority terms, by theme (115)

### The five supervisory capacities (8)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **plausibility auditing** | 1, 2, 3, 4, 8, 9 | The first supervisory capacity: using what you know about the world to ask whether an output is even the kind of thing that could be true, before any… | book |
| **problem formulation** | 1, 3, 6, 7, 8, 9 | The second supervisory capacity: stating exactly what question the AI is being asked and checking, before deployment, that it matches the question th… | book |
| **Interpretive Judgment** | 1, 5, 7, 8, 9 | Interpretive Judgment is the supervisory capacity of supplying the meaning and accountability that an explanation cannot supply for itself. | book |
| **supervisory capacity** | 1, 6, 7, 8, 9 | The chapter's named skill: you supply the meaning and the accountability that the model cannot. | book |
| **tool orchestration** | 1, 8, 9 | The third supervisory capacity: deciding which tool fits which sub-problem (AI, human judgment, a different model, or no tool yet). | book |
| **executive integration** | 1, 8, 9 | The fifth supervisory capacity: combining outputs from several tools, models and people into one decision that someone owns. | book |
| **solve-verify asymmetry** | 1, 3, 9 | The classic idea in computer science that checking a solution is easier than finding one, like factoring a huge number versus multiplying the factors… | book |
| **no tool yet** | 1 | The decision that we do not yet know how to do this well enough to deploy, so no tool, AI or otherwise, should be used. | *spread* |

### Fluency (4)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **fluency trap** | 1, 2, 4, 5, 6, 9 | The more fluently an AI presents its output, the more you trust the output, and then the more you trust your own judgment of it, so you accept any an… | book |
| **fluent output** | 1, 2, 4, 5, 6, 9 | A smooth, finished-looking result that you produced or generated yourself, which makes you reluctant to doubt it. | book |
| **fluent answer** | 6 | A smooth, reassuring answer that sounds complete but is not true: the claim that historical bias has a clean technical fix. | *spread* |
| **fluent report** | 8 | A report or action that reads smoothly and looks correct while the real state of the world is wrong. | *spread* |

### Samples and populations (7)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **sample** | 3 | The records you actually have and train on, which is only the part of the population that was collected. | *spread* |
| **population** | 3 | The whole group the model will actually be used on, including parts that never made it into the data you trained on. | *spread* |
| **subpopulation** | 3 | A distinct group within the larger population, such as the customers whose identifiers were formatted differently in one source system. | *spread* |
| **convenience sample** | 3 | A sample made up of whatever data was easiest to collect, so it leans toward the easy-to-reach end of every distribution it came from. | *spread* |
| **target population** | 3 | The group the model will actually be used on, which the training data is supposed to stand for. | *spread* |
| **representative sample** | 3 | A sample is representative when it was drawn from, and so matches, the population the model will be deployed against, instead of skewing toward the e… | *spread* |
| **sensitivity analysis** | 11 | Re-running the analysis while changing the assumptions or conditions to see whether the conclusion still holds. | *spread* |

### Robustness and adversarial testing (7)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **robustness** | 4 | In this chapter, robustness is less about patching a model and more about asking what its reaction to attacks reveals about what it learned. | *spread* |
| **Agentic Red-Team Casebook** | 4, 8 | The running course project: each chapter adds an artifact about your chosen agent, and this chapter assembles them into a final delivery folder for a… | book |
| **adversarial example** | 4 | An input deliberately altered, by small steps that follow the model's own gradient, so that the model's answer flips while a person sees no meaningfu… | *spread* |
| **semantic invariance** | 4 | A text model has this property if its answer stays the same when the input is reworded in a different style, vocabulary or emotional tone without cha… | book |
| **robustness profile** | 4 | A report of what the model is robust against and what it is not, by attack class, perturbation budget and distribution shift, instead of one number. | *spread* |
| **unconsented data leakage through a corpus's boundary** | 3 | The chapter's open problem: no clean diagnostic finds data leaking through a corpus's boundary at scale, so reliable detection seems to need some for… | *spread* |
| **adversarial testing** | 4 | Deliberately testing a model with inputs built to fool it, to see what it actually relies on instead of how it scores on ordinary data. | *spread* |

### Bias, in words and in symbols (20)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **bias** | 6 | The gap between what an estimator returns on average over every dataset you might collect, E[estimate], and the true quantity theta, written Bias = E… | *spread* |
| **structural bias** | 6 | The data and labels are fine and the model does its job, yet the system still produces unfair outcomes because the world it is deployed into was uneq… | book |
| **label bias** | 6 | The training labels record a process that was itself biased, so the model accurately predicts a distorted stand-in for what you actually care about;… | book |
| **estimator** | 6 | Any procedure that computes a quantity from data, such as a mean, a regression coefficient, a risk score or a classification output. | book |
| **dataset bias** | 6 | The training set did not represent the population the model is deployed on, so the bias lives in the sample and fixing the sample in principle fixes… | book |
| **selection bias** | 6 | Who ends up in your sample depends on what happened to them (for example, a reasonable-sounding query drops the sickest patients), so the sample aver… | book |
| **observer bias** | 6 | A labeler's prior leaks into a single measurement or label, so the labels learn to track what the labeler already believed instead of the real state. | book |
| **data-coding bias** | 6 | Systematic miscoding that appears when judgment is needed to squeeze qualitative material into categories. | book |
| **implicit bias** | 6 | The unconscious associations of the people in the pipeline. | book |
| **confirmation bias** | 6 | The researcher's prior beliefs shape which data gets collected, kept and reported, as if evidence that flatters the hypothesis counted for more and e… | book |
| **publication bias** | 6 | Significant results get submitted, accepted and cited while null results stay in drawers, so a meta-analysis of the published literature reads an eff… | book |
| **self-report bias** | 6 | People's reports about themselves are distorted in a consistent direction (voting more, drinking less, exercising more than they do), not randomly. | book |
| **data-entry bias** | 6 | Transcription errors that follow a pattern instead of being random slips, such as a form that buries the accurate diagnosis code so the nearest code… | book |
| **sampling bias** | 6 | A special case of selection bias in which subgroups are underrepresented because they were hard to reach, not because of their outcomes. | book |
| **biased estimator** | 6 | An estimator is biased when, on average across all the datasets you might collect, it lands on a value different from the true quantity, always off t… | book |
| **conditional probability** | 2, 6 | The probability of Y once you know X, written P(Y / X): what happens given what we see. | *spread* |
| **historical bias** | 6 | Skew that comes from the world itself, not from any data error: the sample is representative and the labels are accurate, yet the data faithfully rec… | *spread* |
| **biased measurement** | 6 | A recorded variable that stands in for the thing you actually care about but is distorted on the way, such as re-arrest standing in for crime when po… | *spread* |
| **inverse probability weighting** | 6 | A fix for selection bias: weight each person you kept by 1 divided by their selection probability P(i ∈ S), so the survivors of the filter stand in f… | *spread* |
| **unbiased estimator** | 6 | An estimator whose bias E[estimate] − theta is zero: averaged over every dataset you might collect it lands on the true value, though it may miss on… | book |

### Probability, base rate, accuracy and loss (10)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **accuracy** | 2, 7 | Whether the model is right, which the chapter treats as a separate question from whether its errors and predictions are spread equitably across group… | *spread* |
| **loss** | 2 | What it costs when the system is wrong, not how often it is wrong. | *spread* |
| **base rate** | 2, 6, 7 | The share of people in a group who truly have the positive outcome (for example, who really are re-arrested), measured against the truth and not agai… | *spread* |
| **false positive** | 2 | A healthy person whom the test wrongly flags as positive. | *spread* |
| **specificity** | 2 | Of the people who are healthy, the share the test correctly returns negative on; the same idea as the true negative rate. | *spread* |
| **true-positive rate** | 2, 7 | Among the people who really are positive, the share the model correctly flags. | book |
| **loss function** | 7 | The training objective the model optimizes. | *spread* |
| **heavy-tailed distribution** | 2 | A distribution where extreme events are common enough that averaging does not tame them, so the sample mean keeps getting moved by the next observati… | *spread* |
| **Bayes' theorem** | 2 | A formula for updating a belief: multiply the prior by the likelihood of the evidence and divide by the total probability of the evidence, to get the… | *spread* |
| **uncertainty component (base rate)** | 11 | The base-rate part of the Brier score: how often the positive outcome occurs in the data, entered in the chapter's formula as the base rate times one… | *spread* |

### Failure modes and points of failure (6)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **failure mode** | 9, 11 | A named way a deployment, claim or process goes wrong that you can recognise from its signs. | *spread* |
| **delegation map** | 9 | A written document that lists, for each step of an AI pipeline, who owns it (AI, human or hybrid), what goes in and out, and what has to be true befo… | *spread* |
| **handoff condition** | 9 | The signal that a step has finished correctly so the next step can start. | *spread* |
| **verification cost** | 9 | How costly it is for a person to check the AI's output: cheap if checking is quick, expensive if it takes about as much work as producing the output. | book |
| **point of failure** | 9, 11 | A place where a pipeline can go wrong; the phrase is not in the chapter, whose nearest wording is where failures happen and where they surface. | *spread* |
| **single point of failure** | 9 | One place where a single lapse lets a failure through; the phrase is not in the chapter. | *spread* |

### Calibration and temperature (11)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **calibration** | 2, 11 | How closely the confidence a model states matches how often it is actually right, so that among 1,000 cases where it says 70%, about 700 turn out pos… | book |
| **ECE** | 2 | A calibration score named in the LLM exercise: Chapter 11 will compute it, together with the Brier score, from the calibration data your plan collect… | book |
| **overconfidence** | 2, 11 | The model claims more certainty than its track record justifies; on a reliability diagram the curve sits below the diagonal. | book |
| **calibration curve** | 2, 11 | A plot of what the model says against what actually happens: stated probability on one axis, the actual share of positives on the other. | *spread* |
| **miscalibrated** | 2, 11 | A model is miscalibrated when its stated probabilities do not match what happens, so its calibration curve peels off the diagonal; overconfident and… | *spread* |
| **Brier score** | 11 | The average squared gap between the predicted probability and what actually happened (1 or 0). | *spread* |
| **temperature scaling** | 2, 11 | A cheap fix for an overconfident model: divide its raw pre-softmax scores by one learned number T, fit on held-out data, which softens its stated con… | *spread* |
| **Maximum Calibration Error** | 11 | The largest bin gap between mean confidence and actual accuracy, instead of the average gap. | book |
| **decorative number** | 2 | A confident-looking number that nobody has checked against reality, so you cannot tell how far off it is. | *spread* |
| **Expected Calibration Error** | 11 | Sort predictions into equal-width confidence bins, then average, weighted by bin size, the gap between mean predicted confidence and actual accuracy… | *spread* |
| **conformal prediction** | 11 | A method that returns a set of possible labels for each case, built so the true label is inside the set with a chosen probability, whatever the model… | *spread* |

### Proxy, drift and the gap (5)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **distribution shift** | 1, 2, 3, 4, 11 | When the real world after deployment stops looking like the data the model was trained on, so the patterns it learned no longer apply while its confi… | book |
| **proxy** | 4, 6, 7 | A feature such as zip code, surname or occupation that correlates with group membership, so the model can effectively rebuild the sensitive attribute… | book |
| **drift** | 1 | The chapter does not define drift; it appears as the vague claim "We have mitigated drift," which the table rewrites as a checkable test. | *spread* |
| **Goodhart's law** | 1 | When people aim at a number as the goal, the number stops being a reliable sign of the thing it was meant to stand for. | book |
| **detecting distribution shift** | 2 | A model looks equally confident while the world changes, so dashboards of its outputs stay green. | *spread* |

### The ladder: association, intervention, counterfactual (5)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **counterfactual** | 4, 6 | Imagining: asking what would have happened to this specific case if X had been different, with everything else held fixed. | book |
| **intervention** | 5, 6 | Doing: asking what happens to Y if we set X to a particular value instead of just watching it, written P(Y / do(X = x)). | book |
| **Pearl's ladder** | 4, 5, 6, 7 | Pearl's three levels of causal reasoning: Rung 1 is seeing what goes with what (association), Rung 2 is doing (intervention), Rung 3 is imagining wha… | book |
| **association** | 6 | Seeing: noticing what goes together in the data, the probability of Y given that we observe X, written P(Y / X). | book |
| **Rung 1 (association)** | 5 | Rung 1 is the level of association: what goes with what, or what the model used. | *spread* |

### Explainability, transparency, interpretability (4)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **transparency** | 5 | Transparency means the system's insides can be inspected: code, parameters, architecture and training data. | book |
| **explainability** | 5 | Explainability means each output comes with a stated reason for it. | book |
| **interpretability** | 5 | Interpretability means a person can build a working mental model of the system, good enough to predict what it will do on new cases. | book |
| **counterfactual explanation** | 5 | A counterfactual explanation says how the prediction would change if a feature had a different value, rather than how much the feature contributed. | book |

### Agents and consequence (13)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **prompt injection** | 4, 8 | Slipping instructions to an agent inside what looks like ordinary data. | book |
| **prediction system** | 8 | A model whose outputs are statements about the world, such as a label for an image, so a wrong output is wrong for one input. | book |
| **resource exhaustion** | 8 | Agents interacting with each other (or with an outside sender) use up resources such as tokens, memory or server capacity in a way no single agent wo… | book |
| **consequence system** | 8 | A model that acts in the world, so what it produces is a change to the state of things, not a statement. | book |
| **cascading hallucination** | 8 | A small error from one agent is passed on, relied on by the next agent and made worse, so the whole system's error rate ends up far above any single… | book |
| **authority laundering** | 8 | One agent hands another some data as if it were a legitimate output, and the second agent cannot check where it really came from, so the data borrows… | book |
| **autonomy-competence gap** | 8 | The agents acted with a high level of independence (installing packages, running any command, rewriting their own settings) while understanding what… | book |
| **false success report** | 8 | The agent says the job is done while the real state of the world shows it is not, and nothing catches the mismatch. | book |
| **identity confusion** | 8 | In a shared channel an agent mistakes its own earlier messages for a second agent, which only happens when several agents share infrastructure. | book |
| **effective data scope** | 8 | All the data that can actually be pulled out through the agent's access, including by indirect requests, as opposed to the data the deployment team p… | book |
| **displayed identity** | 8 | The name or label a person shows (such as a Discord display name) that the agent treats as proof of who they are, even though anyone can change it. | book |
| **runaway loops** | 8 | A process that keeps repeating with no stopping condition, such as two agents passing messages back and forth for days or a routine request that spaw… | *spread* |
| **verified identity** | 8 | An identity confirmed by a check that a changed name cannot fake; the chapter names cryptographically grounded or multi-factor authentication as exam… | *spread* |

### Fairness, its kinds and trade-offs (14)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **disparate impact** | 7 | In the chapter's causal picture, the indirect path from the sensitive attribute to the prediction through legitimate mediators such as education or e… | book |
| **equalized odds** | 6, 7 | The model makes the same kinds of mistakes in every group: among people who truly are positive the same share are caught, and among people who truly… | book |
| **calibration parity** | 6, 7 | A score means the same thing in every group: when the model says seventy percent, about seventy percent of people in group A and in group B really ar… | book |
| **demographic parity** | 6, 7 | The model says yes to the same share of people in every group, so the positive-prediction rate does not depend on group. | book |
| **base-rate difference** | 7 | The condition that triggers the impossibility theorem: the groups have different shares of true positives in the data, and the chapter says that is t… | *spread* |
| **individual fairness** | 7 | Fairness checked person by person: people who are similar should get similar treatment, even when the group totals balance. | book |
| **counterfactual fairness** | 7 | A person-level causal test: would this individual have got the same decision if they had belonged to a different group, with everything else about th… | book |
| **impossibility theorem** | 6, 7 | When groups have different base rates, no model can have calibration parity, equal false-positive rates and equal false-negative rates at once; pick… | book |
| **fairness through awareness** | 7 | Openly deciding how much group membership counts when you judge whether two people are similar. | book |
| **fairness through unawareness** | 7 | Dropping the sensitive attribute from the model and calling it fair. | book |
| **disparate treatment** | 7 | In the chapter's causal picture, the direct path from the sensitive attribute to the prediction. | book |
| **group fairness** | 7 | Fairness judged across whole demographic groups: do the groups end up with different aggregate error rates or outcome rates? | *spread* |
| **Generalized Entropy Index** | 7 | A single number for how unequally benefit or error burden is spread across people, borrowed from income-inequality math. | *spread* |
| **correlates versus causes** | 6, 7 | A system that correlates the bias just reproduces patterns that go together in the data (Rung 1), while a system that causes it would change the outc… | *spread* |

### Accountability (1)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| **human in the accountability chain** | 12 | The chapter's prior question: not only who is responsible but why a human must be in the accountability chain at all, instead of closing the loop wit… | *spread* |

## Other strong candidates (60)

| Term | Ch | In plain words | Flag |
|---|---|---|---|
| what would change my mind | 1, 3, 4, 6 | The chapter's stated falsifier: its leverage-analysis framing would need revision if a debiasing algorithm were shown to robustly remove structural b… | book |
| lock your prediction | 1, 2, 3, 4, 6, 7, 9 | Before you read the post-mortem, write down which of the ten bias mechanisms you think are active and the highest-leverage intervention for each, nam… | book |
| agentic | 1 | A property of an AI system that takes actions in the world through tools, rather than only producing text. | book |
| Glimmer | 1, 5 | A Glimmer is a longer, higher-stakes exercise that sends you to primary sources, and the chapter says not to abridge it. | book |
| deployment context | 6 | Everything around the model where its output actually gets used: the human reviewer, the threshold, the appeal process. | book |
| frame | 6 | The pool of people a sample is drawn from; if it leaves some people out or overweights others, the sample is skewed however large it is. | *spread* |
| threshold | 7 | The score cutoff above which the model says yes. | *spread* |
| artifact | 1 | The artifact is the output a system produces (a rating, a score, a leaderboard number); the world is the real thing it is supposed to say something a… | *spread* |
| leverage | 6 | How much of the bias an intervention actually removes. | *spread* |
| stakes | 9 | How much damage a wrong answer on a sub-task would cause. | book |
| System Dossier | 1 | A one-paragraph description of the agent you will red-team, pasted into your Claude Project's system prompt so every chapter inherits the context. | book |
| the pairing | 5 | The division of labour from Chapter 1: the machine supplies speed and coverage, such as a faithful number on every prediction, and the human supplies… | book |
| event | 2 | Any collection of outcomes from the sample space that you care about, which can be a single outcome or several. | book |
| gap analysis | 1, 3, 6 | After comparing the post-mortem's proposed fix to your locked prediction, write up where they differ. | book |
| casebook journal | 1 | The log where you record a dated prediction-lock before each red-team observation of your agent, kept with a reusable one-page case-write-up template. | *spread* |
| composite | 5 | A composite is a story built to illustrate a real mechanism rather than a documented incident, and the author labels it so readers do not trust it as… | book |
| skepticism | 1 | A set of moves you perform on a claim, not a mood: not eye-rolling or cynicism, but a method that can be taught and whose use can be seen. | *spread* |
| Agents of Chaos | 3, 4, 5, 8 | A 2026 study in which twenty researchers spent two weeks probing and trying to break autonomous AI agents (six agents on the OpenClaw framework) in a… | *spread* |
| self-explanation audit | 5 | A self-explanation audit sets what an agent says it did next to what it actually did and logs the language-game mismatches. | book |
| computational skepticism | 3 | The pairing the book rests on: the machine quickly produces plausible artifacts (tables, plots, a 'the data is clean' paragraph) and you supply the d… | book |
| false-positive rate | 7 | Among the people who really are not positive, the share the model wrongly flags. | book |
| resolution | 11 | In the Brier breakdown, how much the model's predictions vary around the base rate, which measures how well it tells cases apart. | book |
| the supervisor | 1 | The human who owns the checking: asking what a measure stands for and checking it again over time. | *spread* |
| audit trail | 8, 9 | The per-action record of what the system did (inputs, outputs, tool calls, decisions, timestamps, reviewers). | *spread* |
| the machine's speed, your doubt | 9 | The pairing from Chapter 1: the machine brings speed and the human brings doubt. | book |
| outlier | 3 | An unusually extreme value that a rule flags as a candidate. | *spread* |
| Data Frame Audit | 3 | The deliverable of the chapter's LLM exercise: one file holding a dataset inventory, a six-step reconstruction, a structural-assumption audit and a h… | book |
| operational form | 9 | Each supervisory capacity counts only if the pipeline contains a concrete, documented version of it, not because someone felt careful. | *spread* |
| shortcut | 5 | A shortcut is a spurious feature that happens to match the label in the training data but does not carry over to new data. | *spread* |
| Hume's induction problem | 2, 3 | The old problem of inferring what will hold from what happened to hold before. | book |
| testable | 9 | A handoff condition is testable if someone who did not build the pipeline can read it, look at the system, and tell whether it was met. | book |
| faithful | 5 | An explanation is faithful when it correctly reports what the model actually did internally. | *spread* |
| robust features | 4 | Patterns in the data that go with the label and hold steady when the input is slightly altered; they are the shape and structure that people use to r… | book |
| positive predictive value | 2, 7 | Of the people the model flags as positive, the share who really are positive. | book |
| causal graph | 6 | A diagram of the variables from the protected attribute down to the final outcome, with arrows showing which variable causes which. | book |
| external validation | 11 | Testing a model at a specific outside deployment site, with its own patient population, where it had never been validated before. | *spread* |
| non-robust features | 4 | Patterns that go with the label in the training data but are fine-grained, easily disrupted, and meaningless to a person. | *spread* |
| posterior | 2 | What you believe after you have seen the evidence: your prior updated by the evidence. | *spread* |
| epistemic frame | 3 | The set of choices made before and while a dataset was built: what to record, what to include, how to join, where to stop. | book |
| AI Use Disclosure | 9 | A written record of how AI was used to produce a piece of work: what was used, on which step, and how it was verified. | *spread* |
| build/audit pairing | 2, 7, 11 | A two-pass way to learn to write an attestation honestly: write one for something you built, then reconstruct the attestation nobody wrote for a syst… | book |
| structural reason | 5 | The structural reason is the specific mechanism that made an explanation misleading, such as a Rung 1 limitation, a language-game mismatch or a scope… | *spread* |
| alpha (α) | 7 | The setting in the GE index that chooses where to look: low alpha weights differences at the bottom of the distribution, high alpha weights differenc… | book |
| likelihood | 2 | How probable the evidence would be if a given hypothesis were true. | *spread* |
| governance counterfactual | 4 | For a failure that already happened, asking which set of rules and practices (specifications, audit trail, recourse, independent review, sanctions),… | book |
| do not delegate | 3 | The third tier: keep problem formulation, plausibility auditing, interpretive judgment under stakes and accountability sign-off for yourself. | book |
| partition | 2 | A split of the sample space into pieces that cannot overlap (mutually exclusive), together cover every possibility (collectively exhaustive), and eac… | book |
| values claim | 6, 7 | Because no model can satisfy every fairness definition when base rates differ, choosing a metric means deciding which kind of error you are less will… | *spread* |
| supervisory log | 9 | What the AI Use Disclosure becomes when read as a whole: a record of where the person exercised each supervisory capacity. | book |
| language game | 5 | A language game is the context in which words get their meaning, so the same word can mean different things in different contexts. | book |
| distribution match | 9 | Whether the input to a sub-task looks like the data the AI was trained on, or lands in a region where the AI is undertrained. | book |
| calibration baseline | 2, 4 | A repeated exercise in which you give 90% confidence intervals for forecasting questions and check what fraction of them contain the truth. | *spread* |
| irreducibly human | 9 | Some steps cannot be handed to the AI because they need domain knowledge, domain judgment or interpretive responsibility that a pattern-completion en… | *spread* |
| leverage analysis | 6 | A four-step procedure: draw the causal graph, list all paths from the protected attribute to the outcome, ask for each candidate intervention which p… | *spread* |
| true positive | 2 | A sick person whom the test correctly flags as positive. | *spread* |
| discrimination | 11 | How well a model's scores rank or separate cases; the chapter ties it to resolution. | *spread* |
| Epic Sepsis Model | 2, 11 | A real sepsis early-warning tool, deployed across hundreds of hospitals, whose reported validation metrics looked fine on internal data but which per… | book |
| benefit | 7 | The number assigned to each person whose spread the GE index measures: a score, a predicted probability, or an error indicator (1 if misclassified, 0… | *spread* |
| aleatoric uncertainty | 11 | Uncertainty from sampling, natural variation and chance that cannot be removed; the chapter calls it the 'spread of the data'. | book |
| calibration set | 11 | A held-out set, separate from training, used only to fit the correction after the model's weights are fixed (the temperature T, or the score cutoff i… | *spread* |

## Terms Bear named that the book does not use

| Term | Where it lives | In plain words |
|---|---|---|
| **AI is not accountable; you are** | Ch 12 (the whole point) | When you sign off, you sign your name; once you sign it is as if you did it, however much the AI did. |
| **sign-off** | Ch 9 and Ch 12 | The point where you put your name to work and take responsibility; it needs substance behind it. |
| **agent** | Ch 8 (described, not defined) | A model connected to tools, memory and messaging so it acts in the world; its outputs are state changes. |
| **the work split** | Ch 9 (Bear's name) | Who does what: the AI does AI things, humans do human things; the human part is the five capacities. |
| **cost versus risk** | Ch 9 (Bear's framing) | Delegation matches the cost of checking to the risk of being wrong. |
| **provenance** | Ch 8, 9, 12 (literal, thin) | The record of who or what did each step, so you can verify the AI did AI things and humans did human things. |
| **silent failure** | Ch 1, Ch 8 | A failure that tells no one, so the system looks like it works. |
| **silent success** | Ch 1, Ch 8 | The job is done with no signal, so it cannot be told from a silent failure. |
| **need to know** | Ch 8 | Give the agent only what the task needs; ask: does it need to know this? |
| **survivorship bias** | Ch 6 (nearest idea only) | Concluding from the cases that passed a filter and ignoring those that dropped out. |
| **precision / recall** | Ch 2 (not in the book as metrics) | Precision: of those flagged, the share truly positive. Recall: the true positive rate. |
| **temperature (sampling)** | Ch 2, Ch 11 (scaling only) | A setting that controls how random a language model's text is; not the same as temperature scaling. |
| **kinds of drift** | Ch 2, Ch 4 | Data drift, label drift, concept drift, model decay; not adversarial perturbation. |
| **P(A) not equal to P(A given B)** | Ch 6 (Bear's shorthand) | Knowing B changes the chance of A; a bias when B should not matter or the sample was filtered on B. |
| **point of failure** | Ch 9, five-capacities deck | A place where a pipeline can fail; the single point of failure takes everything down. |
| **reuse versus bespoke; step with no tool; mechanical versus human tests** | five-capacities deck | Use an existing tool when it is cheap to check and low risk; a step with no tool is an error; machines run exact tests, humans run taste tests. |

## Not on the exam (for reference)

- Chapter 5: LIME, SHAP and the other attribution methods (35 terms in the inventory): learn them, not on the exam.
- Chapter 10 (visualization), the communicating half of Chapter 11, the rest of Chapter 12 and Chapter 13: 265 terms.

