# Exam terms: the shortlist to cut from

Built 2026-11-09 from the 13 chapter inventories (1,193 entries, merged to 1,054 terms). Bear is cutting this to about 75.

**How it is ordered.** Part A is the terms Bear has called important, grouped by theme. Part B is the next strongest by how often the chapters use them. Part C is terms Bear named that the book does not use. Part D is what Bear marked "learn it, not on the exam". Every entry gives: the book's own sentence with its chapter and line, a plain-words definition, an example, a look-alike, and where the term appears in the chapter text (Ch 2 ×26 means 26 mentions).

**Honest limits.** "Defined in one place" is false for many terms: the book teaches them across passages. Quotes are verbatim from the chapter's first merge side. The old name for Chapter 9's five-question assessment is shown here as "work split", by Bear's rule. Priority matching is by name, so a few matches are loose; read the entry before keeping it.

## Contents

- Part A: Bear's priority terms (115)
- Part B: other strong candidates (60)
- Part C: terms Bear named that are not in the book
- Part D: not on the exam: Chapter 5 methods to learn (35), and what is out of Chapters 10, 11, 12 and 13 (265)

# Part A: Bear's priority terms

## The five supervisory capacities (8)

**plausibility auditing**  *(also: the twitch)*
*in the chapter text: Ch 1 ×3, Ch 2 ×2, Ch 3 ×1, Ch 4 ×1, Ch 7 ×1, Ch 8 ×5, Ch 9 ×4, Ch 12 ×6, Ch 13 ×8 · kind: concept*

> The capacity to look at an AI output and ask: given what I know about the world this output is supposed to describe, is this output the kind of thing that could be true? A technical recruiter with twenty years of experience, handed a ranked list in which strong engineers keep landing near the bottom, would feel something twitch. The twitch is the audit.
> — *the book, Ch 1 line 179*

In plain words: The first supervisory capacity: using what you know about the world to ask whether an output is even the kind of thing that could be true, before any formal analysis. It shows up as the experienced "twitch" when something looks off.

Example: A technical recruiter handed a ranked list in which strong engineers keep landing near the bottom would feel something twitch.

**problem formulation**  *(also: asking the right question)*
*in the chapter text: Ch 1 ×5, Ch 3 ×1, Ch 6 ×1, Ch 7 ×4, Ch 8 ×3, Ch 9 ×3, Ch 12 ×2, Ch 13 ×7 · kind: concept*

> The capacity to specify the question the system is being asked to answer. This one is going to come up a lot, because most AI failures are failures of problem formulation, not failures of model performance.
> — *the book, Ch 1 line 181*

In plain words: The second supervisory capacity: stating exactly what question the AI is being asked and checking, before deployment, that it matches the question the decision-maker actually needs answered. The chapter says most AI failures are of this kind, not failures of model performance.

Example: Netflix's contest asked how close a predicted rating lands to the real one, but the business needed to know whether a member would find something to watch tonight and still be there next month.

Not to be confused with: model performance

**Interpretive Judgment**
*in the chapter text: Ch 1 ×3, Ch 5 ×1, Ch 6 ×1, Ch 7 ×2, Ch 8 ×3, Ch 9 ×3, Ch 12 ×2, Ch 13 ×6 · kind: concept*

> The capacity this chapter trains is Interpretive Judgment, one of Chapter 1's five supervisory capacities: supplying the meaning and accountability the explanation itself cannot warrant.
> — *the book, Ch 5 line 19*

In plain words: Interpretive Judgment is the supervisory capacity of supplying the meaning and accountability that an explanation cannot supply for itself. In this chapter it means asking what a SHAP number or an agent's report actually warrants.

Example: Asking 'explainable to whom?' or 'what does deleted mean in the user's language game?'

**supervisory capacity**  *(also: supplying the meaning and the accountability the model cannot)*
*in the chapter text: Ch 1 ×3, Ch 2 ×2, Ch 6 ×3, Ch 7, Ch 8 ×2, Ch 9 ×5, Ch 11 ×1, Ch 12 ×1 · kind: framework*

> This chapter exercises one supervisory capacity — supplying the meaning and the accountability the model cannot — and it does so in two passes.
> — *the book, Ch 6 line 26*

In plain words: The chapter's named skill: you supply the meaning and the accountability that the model cannot. It is used twice, once building (hunt for where you let bias in) and once auditing (trace where bias entered someone else's system and name the owner).

Example: The model builds fast, and you supply the suspicion.

**tool orchestration**
*in the chapter text: Ch 1 ×3, Ch 7 ×1, Ch 8 ×3, Ch 9 ×7, Ch 12 ×1 · kind: concept*

> The capacity to decide which tool to use for which sub-problem. AI is one tool among many. The supervisor decides when AI is the right tool, when human judgment is the right tool, when a different model is, and — this one is the hardest — when the answer is no tool yet, we do not know how to do this well enough to deploy.
> — *the book, Ch 1 line 185*

In plain words: The third supervisory capacity: deciding which tool fits which sub-problem (AI, human judgment, a different model, or no tool yet). It includes the hardest call, that this system is not ready to be deployed here.

Example: A supervisor who says "we should not deploy this here" is doing supervisory work.

**executive integration**
*in the chapter text: Ch 1 ×4, Ch 7 ×2, Ch 8 ×3, Ch 9 ×5 · kind: concept*

> The capacity to take outputs from multiple tools, multiple models, multiple humans, and synthesize them into a decision the integrating system can stand behind. Somebody in the organization has to be the place where the buck stops. If there is no such place, there is no executive integration, and the system as a whole has no decision-maker, only outputs.
> — *the book, Ch 1 line 191*

In plain words: The fifth supervisory capacity: combining outputs from several tools, models and people into one decision that someone owns. It is the place where the buck stops, and without it the system has outputs but no decision-maker.

Example: In the capacity table's failure example, the pipeline produces decisions but no single person or body owns them, and accountability dissolves into the architecture.

**solve-verify asymmetry**  *(also: verifying a solution is easier than producing one)*
*in the chapter text: Ch 1 ×1, Ch 3 ×1, Ch 9 ×2 · kind: concept*

> There is a piece of folklore in computer science that says verifying a solution is easier than producing one. If I give you a very large number, it is hard to factor it. If I hand you the factors, it is easy to multiply them and check.
> — *the book, Ch 1 line 155*

In plain words: The classic idea in computer science that checking a solution is easier than finding one, like factoring a huge number versus multiplying the factors back together. Most of cryptography is built on it.

Example: A very large number is hard to factor, but if you hand over the factors it is easy to multiply them and check.

Not to be confused with: the inverted asymmetry in AI deployment

**no tool yet**  *(also: we should not deploy this here)*
*in the chapter text: Ch 1 ×4 · kind: concept*

> The supervisor who says "we should not deploy this here" is doing supervisory work. It is often the most valuable work they do.
> — *the book, Ch 1 line 185; explained across several passages, no single defining sentence*

In plain words: The decision that we do not yet know how to do this well enough to deploy, so no tool, AI or otherwise, should be used. The chapter calls saying so supervisory work and often the most valuable work a supervisor does.

Example: In the capacity table, this decision is never made when no one has the authority or the mandate to make it.

## Fluency (4)

**fluency trap**
*exam focus (Bear) · in the chapter text: Ch 1 ×11, Ch 2 ×1, Ch 4 ×1, Ch 5 ×1, Ch 6 ×3, Ch 9 ×2, Ch 11 ×3, Ch 13 ×1 · kind: failure mode*

> The more fluently an AI presents its output, the more confident the user becomes in the output. That part is not surprising. The trap is the second move: the more confident the user becomes in the output, the more confident the user becomes in their own evaluation of the output.
> — *the book, Ch 1 line 213*

In plain words: The more fluently an AI presents its output, the more you trust the output, and then the more you trust your own judgment of it, so you accept any answer that arrives in the same polished shape. The defense is not distrusting fluent outputs but not letting fluency do the work of evidence.

Example: A leaderboard ranked to the fourth decimal place, or a recruiting tool returning a clean one-to-five stars, arrives looking finished, and the polish does the work the question should have done.

Not to be confused with: fluency itself (the trap is the second boost, confidence in your own evaluation)

**fluent output**  *(also: believing your own fluent output)*
*exam focus (Bear) · in the chapter text: Ch 1 ×3, Ch 2, Ch 4, Ch 5, Ch 6 ×1, Ch 9, Ch 11, Ch 13 ×2 · kind: failure mode*

> A BUILD pass, where you conduct a persona/data build and hunt for where you let bias in (the hard part is not believing your own fluent output).
> — *the book, Ch 6 line 26*

In plain words: A smooth, finished-looking result that you produced or generated yourself, which makes you reluctant to doubt it. The chapter says that not believing it is the hard part of hunting for where you let bias in.

Example: An AI-generated persona dataset that feels clean to you because you own it (Exercise S4).

**fluent answer**  *(also: selling the fluent answer)*
*in the chapter text: Ch 6 ×1 · kind: failure mode*

> That is the whole trade, stated honestly. Anyone who tells you historical bias has a clean technical fix is selling the fluent answer.
> — *the book, Ch 6 line 100; explained across several passages, no single defining sentence*

In plain words: A smooth, reassuring answer that sounds complete but is not true: the claim that historical bias has a clean technical fix. Every real mitigation trades some predictive fit for less inheritance of the past, so an honest answer states the trade.

Example: Someone claiming a fairness constraint cleanly solves historical bias.

**fluent report**  *(also: fluent, structurally valid output)*
*in the chapter text: Ch 8 · kind: failure mode*

> The action looks well-formed. The report is fluent. The world is wrong.
> — *the book, Ch 8 line 45; explained across several passages, no single defining sentence*

In plain words: A report or action that reads smoothly and looks correct while the real state of the world is wrong. From the chapter's three lines about it, the smoothness is exactly why it can pass for success.

Example: Ash reported "Email account RESET completed" in a confident, well-formed way, but the email was still there.

Not to be confused with: plausibility auditing (the check that catches it)

## Samples and populations (7)

**sample**  *(also: the sample; available data; training data)*
*in the chapter text: Ch 1 ×2, Ch 2 ×12, Ch 3 ×6, Ch 4 ×3, Ch 5 ×4, Ch 6 ×16, Ch 7 ×2, Ch 8 ×1, Ch 9 ×5, Ch 10 ×1, Ch 11 ×1, Ch 12 ×1, Ch 13 ×14 · kind: concept*

> There is the sampling assumption in its sharpest form: your sample is available data, which means it skews toward the easy-to-reach end of every distribution it was drawn from. You train on the convenience sample and deploy against the world, and the world is wider.
> — *the book, Ch 3 line 130; explained across several passages, no single defining sentence*

In plain words: The records you actually have and train on, which is only the part of the population that was collected. It is available data, so it skews toward the easy-to-reach end of every distribution it was drawn from.

Example: The merged table that excluded rows failing the join is the sample; the full customer population includes the rows that never arrived.

Not to be confused with: population

**population**  *(also: the full population; the population the model is going to be deployed against)*
*in the chapter text: Ch 1 ×1, Ch 2 ×13, Ch 3 ×6, Ch 4 ×2, Ch 5 ×2, Ch 6 ×6, Ch 7 ×17, Ch 8 ×1, Ch 9 ×1, Ch 11 ×17, Ch 12 ×1 · kind: concept*

> The model, trained on what was present, performed beautifully on what was present. Deployed against the full population, it performed predictably worse on the subpopulation it had never seen.
> — *the book, Ch 3 line 18; explained across several passages, no single defining sentence*

In plain words: The whole group the model will actually be used on, including parts that never made it into the data you trained on. A model can look excellent on the records it saw and still do worse on the population it is deployed against.

Example: In the join-drop case the model did well on the rows present but worse on the full population, because one subpopulation's rows had been dropped.

Not to be confused with: sample

**subpopulation**  *(also: subpopulations)*
*in the chapter text: Ch 3 ×7, Ch 11 ×2 · kind: concept*

> One specific subpopulation had inconsistent identifier formatting in one of the three source systems — a field entered slightly differently by the people who originally maintained that system years ago.
> — *the book, Ch 3 line 18; explained across several passages, no single defining sentence*

In plain words: A distinct group within the larger population, such as the customers whose identifiers were formatted differently in one source system. If the data loses a subpopulation, a model can fail on exactly that group while looking fine overall.

Example: The subpopulation with inconsistent identifier formatting disproportionately failed the join and was missing from the training set.

Not to be confused with: population

**convenience sample**  *(also: available data; easy-to-reach sample)*
*in the chapter text: Ch 3 ×3 · kind: concept*

> You train on convenience samples and deploy against the world. The world is wider than the convenience sample, and you find this out slowly.
> — *the book, Ch 3 line 120; explained across several passages, no single defining sentence*

In plain words: A sample made up of whatever data was easiest to collect, so it leans toward the easy-to-reach end of every distribution it came from. A model trained on it faces a wider population in deployment and does worse on the part it never saw.

Example: A model performs well on easy-to-reach customers but degrades on the long tail it was never trained on.

Not to be confused with: representative sample

**target population**  *(also: deployment target; the population the model is going to be deployed against)*
*in the chapter text: Ch 3 ×1 · kind: concept*

> EDA only sees what is present; it cannot compare the present data to the absent target population
> — *the book, Ch 3 line 111; explained across several passages, no single defining sentence*

In plain words: The group the model will actually be used on, which the training data is supposed to stand for. EDA cannot check the data against it, because EDA only sees the rows that are present and the target population is partly absent.

Example: A model trained on easy-to-reach customers must still handle the long tail of customers who were never in the training data.

Not to be confused with: sample

**representative sample**  *(also: representativeness; sample drawn from the population the model is going to be deployed against)*
*in the chapter text: Ch 3, Ch 6 ×1 · kind: concept*

> Was this sample drawn from the population the model is going to be deployed against? Often, no.
> — *the book, Ch 3 line 120; explained across several passages, no single defining sentence*

In plain words: A sample is representative when it was drawn from, and so matches, the population the model will be deployed against, instead of skewing toward the easy-to-reach end. The chapter does not use the word 'representative'; its test is the question quoted here, and its usual answer is no.

Example: A sample that leaves out a subpopulation, or covers only customers who completed onboarding when deployment includes those who abandoned it, is not representative of the deployment population.

Not to be confused with: convenience sample

**sensitivity analysis**  *(also: full sensitivity analyses)*
*in the chapter text: Ch 11 ×4 · kind: method*

> The evidence required is full analysis, alternatives considered and rejected, sensitivity analysis, and a finding that survives the analysis.
> — *the book, Ch 11 line 61; explained across several passages, no single defining sentence*

In plain words: Re-running the analysis while changing the assumptions or conditions to see whether the conclusion still holds. The chapter asks for ideally some of it before you say "find", and for a finding that survives it before you say "conclude"; the full sensitivity analyses go in the Layer 3 appendix.

Example: "Conclude" needs "Full analysis, alternatives named and rejected, sensitivity analysis the finding survives" (the verb table).

## Robustness and adversarial testing (7)

**robustness**  *(also: robust; adversarial robustness)*
*in the chapter text: Ch 2 ×2, Ch 3 ×1, Ch 4 ×148, Ch 5 ×3, Ch 6 ×3, Ch 7 ×1, Ch 8 ×17, Ch 9 ×1, Ch 10 ×1, Ch 11 ×5, Ch 12 ×1, Ch 13 ×4 · kind: concept*

> So when I say "robustness" in this chapter, I am not asking the engineering question — how do we patch this? I am asking the supervisory question: what does the model's response to adversarial inputs tell me about what the model actually learned, and how does that compare to what I thought it was learning?
> — *the book, Ch 4 line 65; explained across several passages, no single defining sentence*

In plain words: In this chapter, robustness is less about patching a model and more about asking what its reaction to attacks reveals about what it learned. It is always robustness against some specific attack or shift, never a single general property.

Example: A model adversarially trained against L∞ perturbations is not robust against transfer attacks, patch attacks or prompt injection.

Not to be confused with: hardening

**Agentic Red-Team Casebook**  *(also: casebook)*
*in the chapter text: Ch 1 ×1, Ch 2 ×1, Ch 3 ×1, Ch 4 ×1, Ch 5 ×1, Ch 6 ×1, Ch 7 ×1, Ch 8 ×1, Ch 9 ×1, Ch 10 ×1, Ch 11 ×1, Ch 12 ×1, Ch 13 ×1 · kind: named result or case*

> Every chapter has produced an artifact in the casebook. This chapter integrates them into the deliverable.
> — *the book, Ch 13 line 490*

In plain words: The running course project: each chapter adds an artifact about your chosen agent, and this chapter assembles them into a final delivery folder for a deployment-review committee.

Example: Chapter 13 adds the go/no-go memo and reorganizes the casebook into 00-summary through 07-provenance folders.

**adversarial example**  *(also: adversarial perturbation; adversarial input; adversarial inputs)*
*in the chapter text: Ch 3 ×1, Ch 4 ×25, Ch 7 ×1 · kind: concept*

> Somebody, or some procedure, has deliberately built an input that lives in a third distribution, designed to maximize the gap between the model's prediction and the true label. The construction is mathematical: follow the gradient of the model's loss with respect to its input, take a small step in the direction that increases loss the most, repeat.
> — *the book, Ch 4 line 140; explained across several passages, no single defining sentence*

In plain words: An input deliberately altered, by small steps that follow the model's own gradient, so that the model's answer flips while a person sees no meaningful change. It is built to be the worst case within a size budget, not something that happens by chance.

Example: The panda picture changed by fractions of a percent of brightness in scattered pixels, labeled gibbon.

Not to be confused with: natural distribution shift (the world drifts on its own; nothing is constructed)

**semantic invariance**
*in the chapter text: Ch 4 ×3 · kind: concept*

> The appropriate concept for NLP robustness is semantic invariance: a robust model should produce the same classification when the input is rewritten in a different style, vocabulary, or emotional register while preserving meaning. Testing for semantic invariance is a form of adversarial evaluation specific to this domain.
> — *the book, Ch 4 line 265*

In plain words: A text model has this property if its answer stays the same when the input is reworded in a different style, vocabulary or emotional tone without changing the meaning. It is what you test for when checking language-model robustness.

Example: "List the key points of this document" and "What are the main takeaways from this document?" should get equivalent responses.

Not to be confused with: prompt sensitivity (what it looks like when invariance fails)

**robustness profile**  *(also: robustness is not a single number; multi-axis reporting)*
*in the chapter text: Ch 4 ×4 · kind: framework*

> The supervisory move that follows: robustness is not a single number. It is a profile. Robust against this kind of attack, brittle against that kind, robust on this distribution, brittle on that one.
> — *the book, Ch 4 line 154; explained across several passages, no single defining sentence*

In plain words: A report of what the model is robust against and what it is not, by attack class, perturbation budget and distribution shift, instead of one number. The chapter says the profile is a table, not a sentence.

Example: L∞ white-box ε = 0.03: clean 94%, robust 71%; transfer attack from a ResNet-50 surrogate: 58%; time shift Q4 2023 to Q1 2024: 87%.

Not to be confused with: a single robustness score

**unconsented data leakage through a corpus's boundary**  *(also: leakage through a corpus's boundary; red-teaming)*
*in the chapter text: Ch 3 ×1 · kind: failure mode*

> I do not have a clean diagnostic for unconsented data leakage through a corpus's boundary at scale. The email-agent pattern shows up easily in small examples and is hard to surface in large corpora without targeted search. The agentic deployment surface is making this worse, not better.
> — *the book, Ch 3 line 243; explained across several passages, no single defining sentence*

In plain words: The chapter's open problem: no clean diagnostic finds data leaking through a corpus's boundary at scale, so reliable detection seems to need some form of red-teaming. It is easy to see in small examples and hard in large corpora.

Example: The email-agent pattern surfaced in small examples.

**adversarial testing**  *(also: adversarial evaluation; the attack (as the instrument); probing; robustness probe suite)*
*in the chapter text: Ch 4 · kind: method*

> This chapter's instrument for asking what has the model actually learned? was the attack: perturb the input, watch the proxy fail.
> — *the book, Ch 4 line 455; explained across several passages, no single defining sentence*

In plain words: Deliberately testing a model with inputs built to fool it, to see what it actually relies on instead of how it scores on ordinary data. The chapter uses it as the instrument for finding the gap between what a model learned and what was intended, in images, text, tables and agents alike.

Example: Perturb the panda picture and watch the model flip to gibbon; for text, rewrite an input in a different style (semantic invariance test); for an agent, run a probe suite.

Not to be confused with: adversarial training (a defense that puts perturbed inputs into the training loop, not an instrument for diagnosing what the model learned)

## Bias, in words and in symbols (20)

**bias**  *(also: \text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta; bias as a property of an estimator)*
*in the chapter text: Ch 1 ×2, Ch 2 ×3, Ch 3 ×6, Ch 4 ×1, Ch 5 ×8, Ch 6 ×229, Ch 7 ×10, Ch 8 ×3, Ch 9 ×2, Ch 11 ×1, Ch 12 ×1, Ch 13 ×3 · kind: concept*

> Suppose the true quantity is $\theta$ — the real underlying rate, the true causal effect, the actual probability of an outcome. Your estimator is $\hat{\theta}$, the value you compute from data. Bias is:
> — *the book, Ch 6 line 38; explained across several passages, no single defining sentence*

In plain words: The gap between what an estimator returns on average over every dataset you might collect, E[estimate], and the true quantity theta, written Bias = E[estimate] − theta. Zero means it is not systematically off; the same idea shows up in selection bias as an average among the people included, E[Y | i ∈ S], that differs from the population average E[Y].

Example: The 1936 Literary Digest poll: 2.4 million responses predicted a Landon landslide while Roosevelt won by a landslide.

Not to be confused with: the newspaper meaning of bias (unfair, skewed, prejudiced), which the chapter says is not precise enough to do engineering with; and a changed conditional probability is not automatically unfair (a gap is a flag, not a verdict)

**structural bias**
*in the chapter text: Ch 6 ×17, Ch 7 ×2, Ch 8 ×1 · kind: failure mode*

> The bias is not in the model, not in the data. It is in the structure the model is being deployed into. No model fix touches it.
> — *the book, Ch 6 line 136*

In plain words: The data and labels are fine and the model does its job, yet the system still produces unfair outcomes because the world it is deployed into was unequal to begin with. No model fix or data fix touches it; only changing the deployment structure (review process, decision criteria, institutional context) does.

Example: A hiring model that accurately predicts who succeeds at a company where mentorship, sponsorship and access to interesting projects were never distributed evenly across groups.

Not to be confused with: dataset bias (treating structural bias as a dataset problem moves the disparity zero)

**label bias**
*in the chapter text: Ch 6 ×14 · kind: failure mode*

> The model is dutifully predicting re-arrest, doing so accurately, and the prediction is biased because re-arrest is a biased measurement of the underlying thing we actually care about. Call this label bias. The mechanisms that produce it: observer bias, data coding bias, historical bias, and the label-corruption form of self-report bias.
> — *the book, Ch 6 line 134*

In plain words: The training labels record a process that was itself biased, so the model accurately predicts a distorted stand-in for what you actually care about; the chapter calls it a measurement problem. Observer, data-coding, historical and (in its label-corruption form) self-report bias produce it.

Example: A recidivism predictor trained on re-arrest rather than crime inherits the patterns of past policing.

Not to be confused with: dataset bias (causally distinct but observationally close when you only have the labeled training set)

**estimator**
*in the chapter text: Ch 6 ×14 · kind: concept*

> In statistics, bias is a property of an estimator — not a dataset, not a model, not a prediction. An estimator is any procedure for computing a quantity from data: a mean, a regression coefficient, a risk score, a classification output.
> — *the book, Ch 6 line 36*

In plain words: Any procedure that computes a quantity from data, such as a mean, a regression coefficient, a risk score or a classification output. In statistics, bias belongs to this procedure, not to the dataset, the model or a single prediction.

Example: The sepsis model's estimator computes the average outcome among the patients you actually assembled.

**dataset bias**
*in the chapter text: Ch 6 ×10 · kind: failure mode*

> The bias is in the sample. Fix the sample, and in principle you fix the bias. Call this dataset bias.
> — *the book, Ch 6 line 132*

In plain words: The training set did not represent the population the model is deployed on, so the bias lives in the sample and fixing the sample in principle fixes it. Selection bias, sampling bias and the sample-corruption form of data-entry bias produce it.

Example: Face recognition trained mostly on light-skinned faces and deployed on everyone.

Not to be confused with: label bias (causally distinct but observationally close when you only have the labeled training set)

**selection bias**
*in the chapter text: Ch 6 ×7 · kind: failure mode*

> The estimator you built computes $E[Y \mid i \in S]$: the average outcome among the sample $S$ you actually assembled. The quantity you wanted was $E[Y]$, the average outcome in the population. Those two are equal on exactly one condition: that the probability of landing in the sample, $P(i \in S)$, is independent of the outcome $Y$.
> — *the book, Ch 6 line 68*

In plain words: Who ends up in your sample depends on what happened to them (for example, a reasonable-sounding query drops the sickest patients), so the sample average no longer matches the population average. The estimate is biased before any parameter is fit, and more data drawn the same way only sharpens the wrong answer.

Example: The sepsis model: the query 'patients with a complete lab panel within six hours of admission' drops the patients too critical to have labs drawn, so the model underestimates their risk.

Not to be confused with: sampling bias (the accessibility special case: groups missing because they were hard to reach, not because of their outcomes)

**observer bias**
*in the chapter text: Ch 6 ×7 · kind: failure mode*

> Observer bias is that same prior localized to a single measurement act: the annotator who knows a patient's prior diagnosis and codes ambiguous notes as symptom-positive, so the labels quietly learn to predict past diagnosis rather than current state.
> — *the book, Ch 6 line 76*

In plain words: A labeler's prior leaks into a single measurement or label, so the labels learn to track what the labeler already believed instead of the real state. A kappa that collapses when you unblind the annotators is direct evidence of it.

Example: The annotator who knows a patient's prior diagnosis codes ambiguous notes as symptom-positive, so the labels predict past diagnosis rather than current state.

Not to be confused with: data-coding bias (disagreement clustered on specific annotators points to observer bias; clustered on specific items points to data-coding bias)

**data-coding bias**  *(also: data coding bias)*
*in the chapter text: Ch 6 ×7 · kind: failure mode*

> Data-coding bias enters one step later, when qualitative material is squeezed into categories: is "not bad" positive or neutral? which diagnosis code fits? Where the mapping needs judgment, systematic miscoding follows the judgment.
> — *the book, Ch 6 line 76*

In plain words: Systematic miscoding that appears when judgment is needed to squeeze qualitative material into categories. A kappa that is low on specific items rather than specific people points to it, because the category is underspecified, not the coder.

Example: Is 'not bad' positive or neutral? Which diagnosis code fits?

Not to be confused with: observer bias (annotator priors distorting judgments rather than a poorly defined category)

**implicit bias**
*in the chapter text: Ch 6 ×6 · kind: concept*

> The last one is not really a peer of the other nine, and pretending it is would be a category error. Implicit bias — the unconscious associations of the humans in the pipeline — is not an entry point. It is the medium several entry points swim in.
> — *the book, Ch 6 line 110*

In plain words: The unconscious associations of the people in the pipeline. It is not an entry point itself but the medium several entry points swim in (it surfaces as confirmation, observer, data-coding and publication bias), so it has no single point to fix.

Example: A prior shaping which hypothesis you form (confirmation bias), what you observe (observer bias), how you categorize (data-coding bias) and what you submit (publication bias).

**confirmation bias**
*in the chapter text: Ch 6 ×5 · kind: failure mode*

> Confirmation bias is the researcher's prior shaping which data gets collected, kept, and reported — in Bayesian terms, an invisible multiplier greater than one on evidence that flatters the hypothesis and less than one on evidence that dents it, so the posterior drifts toward the prior instead of toward the world.
> — *the book, Ch 6 line 76*

In plain words: The researcher's prior beliefs shape which data gets collected, kept and reported, as if evidence that flatters the hypothesis counted for more and evidence that dents it counted for less. The conclusion drifts toward the prior instead of toward the world.

Example: A team designs a study to confirm its hypothesis and gets a positive result, which then compounds with publication bias.

Not to be confused with: observer bias (the same prior, but localized to a single measurement act)

**publication bias**
*in the chapter text: Ch 6 ×5 · kind: failure mode*

> And publication bias is the same leak at the scale of a literature: significant results get submitted, accepted, cited; nulls die in drawers, so a meta-analysis computes $E[\hat{\theta} \mid \text{published}]$ and reads an effect inflated by the censoring.
> — *the book, Ch 6 line 76*

In plain words: Significant results get submitted, accepted and cited while null results stay in drawers, so a meta-analysis of the published literature reads an effect inflated by that censoring. A funnel plot with a missing lower-left corner makes it visible.

Example: A meta-analysis whose funnel plot is missing the lower-left corner of small null studies.

**self-report bias**
*in the chapter text: Ch 6 ×3 · kind: failure mode*

> Self-report bias is the subject's own prior doing the leaking — people report voting more, drinking less, exercising more than they do, and the error runs toward social desirability, not randomly.
> — *the book, Ch 6 line 76*

In plain words: People's reports about themselves are distorted in a consistent direction (voting more, drinking less, exercising more than they do), not randomly. When there is no external gold standard, you label the data as self-reports and name the likely direction of distortion.

Example: People say they vote more, drink less and exercise more than they really do.

Not to be confused with: random noise (the chapter says the error runs toward social desirability, not randomly)

**data-entry bias**  *(also: data entry bias)*
*in the chapter text: Ch 6 ×3 · kind: failure mode*

> Data-entry bias is patterned transcription error — not random slips, but errors that track something. A form that demands a diagnosis code and buries the accurate one three menus deep gets the nearest code instead, and a whole class of conditions is undercoded in one direction. The tell: it changes neither who is in the sample nor how outcomes are labeled, only whether the recorded value for an already-enrolled person matches reality.
> — *the book, Ch 6 line 88*

In plain words: Transcription errors that follow a pattern instead of being random slips, such as a form that buries the accurate diagnosis code so the nearest code gets entered. It changes neither who is in the sample nor how outcomes are labeled, only whether the recorded value for an enrolled person matches reality.

Example: A form that buries the accurate diagnosis code three menus deep, so a whole class of conditions is undercoded in one direction.

Not to be confused with: random noise (the chapter says people confuse it with 'just noise')

**sampling bias**
*in the chapter text: Ch 6 ×3 · kind: failure mode*

> Sampling bias is the accessibility special case of selection bias: subgroups are underrepresented not because of their outcomes but because they were hard to reach. A remote-work survey pushed through LinkedIn overrepresents credentialed professionals — the frame, not the instrument, is skewed.
> — *the book, Ch 6 line 88*

In plain words: A special case of selection bias in which subgroups are underrepresented because they were hard to reach, not because of their outcomes. It earns its own name because the fix differs: when outside data gives the true group sizes, you reweight.

Example: A remote-work survey pushed through LinkedIn overrepresents credentialed professionals.

Not to be confused with: selection bias (there, inclusion depends on what happened to the person)

**biased estimator**  *(also: systematically off in one direction)*
*in the chapter text: Ch 6 ×2 · kind: concept*

> An estimator is biased if, in expectation across all possible datasets you might collect, it systematically returns a value different from the true underlying quantity you are trying to measure.
> — *the book, Ch 6 line 36*

In plain words: An estimator is biased when, on average across all the datasets you might collect, it lands on a value different from the true quantity, always off the same way. More data narrows the scatter around that wrong value but does not move it.

Example: The 1936 Literary Digest poll: 2.4 million responses predicted a Landon landslide while Roosevelt won by a landslide.

Not to be confused with: an estimator that is merely wrong on one dataset (unbiased estimators can be wrong on any given dataset; bias is being systematically wrong)

**conditional probability**  *(also: P(Y | X); conditional distributions; given that we observe X)*
*in the chapter text: Ch 2 ×13, Ch 6 · kind: concept*

> The model learns conditional distributions from data: $P(Y | X)$. What happens, given what we see.
> — *the book, Ch 6 line 252; explained across several passages, no single defining sentence*

In plain words: The probability of Y once you know X, written P(Y | X): what happens given what we see. It is what most machine learning learns, and it is what most fairness metrics compare across groups.

Example: The sepsis model learns what predicts sepsis among patients stable enough to be tested, which is a conditional average, not the average over all patients.

Not to be confused with: a changed conditional probability is not automatically unfair: a gap between groups is a flag, not a verdict, since real base-rate differences produce the same gap

**historical bias**
*in the chapter text: Ch 6 ×15 · kind: failure mode*

> No annotator erred. The data is a faithful recording of the world that produced it. And it is still poison.
> — *the book, Ch 6 line 92; explained across several passages, no single defining sentence*

In plain words: Skew that comes from the world itself, not from any data error: the sample is representative and the labels are accurate, yet the data faithfully records a world you did not want to reproduce. So there is no quality defect to fix, only a trade of some predictive fit for less inheritance of the past.

Example: A hiring model trained on ten years of promotion records at a company that promoted men into engineering roles at higher rates.

Not to be confused with: data-quality defects such as selection filters, miscoding and slips (the chapter says historical bias is none of these)

**biased measurement**  *(also: measurement problem; uneven measurement)*
*in the chapter text: Ch 6 ×3 · kind: failure mode*

> Re-arrest is a function of crime and policing. If policing is unevenly distributed across populations, then re-arrest is an uneven measurement of crime. And every model trained on that data inherits the unevenness.
> — *the book, Ch 6 line 221; explained across several passages, no single defining sentence*

In plain words: A recorded variable that stands in for the thing you actually care about but is distorted on the way, such as re-arrest standing in for crime when policing is uneven. Models trained on it inherit the unevenness, and the chapter calls label bias a measurement problem.

Example: Re-arrest as a measurement of crime: the COMPAS labels are 'was this person re-arrested?', not 'did this person commit a crime?'.

Not to be confused with: the true quantity it stands in for (re-arrest is not crime)

**inverse probability weighting**
*in the chapter text: Ch 6 ×1 · kind: method*

> You can correct for observed selection: inverse probability weighting gives each retained observation a weight of $1/P(i \in S)$, so the survivors of an aggressive filter stand in for the people who were dropped; propensity score matching models inclusion as a function of covariates you can see and reweights on the estimated scores. Both moves buy you back an unbiased estimate — but only if the variable driving selection is one you recorded.
> — *the book, Ch 6 line 72; explained across several passages, no single defining sentence*

In plain words: A fix for selection bias: weight each person you kept by 1 divided by their selection probability P(i ∈ S), so the survivors of the filter stand in for the people who were dropped. It only works if the variable that drove the exclusion was recorded.

Example: Giving each patient who passed the six-hour lab filter a weight of 1 over their inclusion probability, which helps only if the reason others were dropped was recorded.

**unbiased estimator**  *(also: unbiased)*
*in the chapter text: Ch 6 · kind: concept*

> If this quantity is zero, the estimator is unbiased — it might be wrong on any given dataset, but it is not systematically wrong. If it is nonzero, the estimator is biased: systematically off in one direction.
> — *the book, Ch 6 line 42*

In plain words: An estimator whose bias E[estimate] − theta is zero: averaged over every dataset you might collect it lands on the true value, though it may miss on any one dataset. A nonzero bias means it is systematically off in one direction.

Example: Inverse probability weighting buys back an unbiased estimate when the variable driving selection was recorded.

Not to be confused with: an estimator that happens to be right on this dataset (unbiased allows being wrong on any given dataset)

## Probability, base rate, accuracy and loss (10)

**accuracy**  *(also: accuracy trade-off)*
*in the chapter text: Ch 1 ×7, Ch 2 ×10, Ch 4 ×26, Ch 5 ×2, Ch 6 ×1, Ch 7 ×5, Ch 9 ×3, Ch 10 ×17, Ch 11 ×11, Ch 12 ×2, Ch 13 ×11 · kind: concept*

> This chapter asks a different question: not whether the model is accurate, but whether its errors and predictions are distributed equitably. The fairness question is not downstream of the accuracy question. It is structurally distinct from it.
> — *the book, Ch 7 line 35; explained across several passages, no single defining sentence*

In plain words: Whether the model is right, which the chapter treats as a separate question from whether its errors and predictions are spread equitably across groups. Fairness is not downstream of accuracy, and in-processing fairness methods even trade accuracy off against the fairness constraint.

Example: Toolkit table: for in-processing, the tradeoff with accuracy is locked in at train time.

Not to be confused with: fairness (a model can be accurate overall and still distribute errors unequally)

**loss**  *(also: cost of being wrong; cost of error; cost-of-error)*
*in the chapter text: Ch 1 ×2, Ch 2 ×18, Ch 4 ×15, Ch 6 ×6, Ch 7 ×3, Ch 8 ×5, Ch 12 ×4 · kind: concept*

> What is the cost distribution? Is the loss of being wrong roughly uniform, or are there rare catastrophic outcomes that average-loss metrics will miss?
> — *the book, Ch 2 line 506; explained across several passages, no single defining sentence*

In plain words: What it costs when the system is wrong, not how often it is wrong. Most wrong outputs may be minor inconveniences while a rare one kills a patient or wipes a database.

Example: Exercise 10: a false positive costs $10 of analyst time, a false negative costs $500,000 (a breach), although the error rates are only 2% and 0.5%.

Not to be confused with: accuracy (how often it is right; it says nothing about what the errors cost)

**base rate**  *(also: prevalence; underlying base rate; base rate of positives)*
*in the chapter text: Ch 1 ×1, Ch 2 ×35, Ch 6 ×9, Ch 7 ×34, Ch 10 ×1, Ch 11 ×10 · kind: concept*

> Suppose the underlying base rate of positives is $p_a = 0.6$ in group $a$ and $p_b = 0.3$ in group $b$. Sixty percent of group $a$ has the positive ground truth; thirty percent of group $b$ does.
> — *the book, Ch 7 line 77; explained across several passages, no single defining sentence*

In plain words: The share of people in a group who truly have the positive outcome (for example, who really are re-arrested), measured against the truth and not against what the model predicts. When two groups have different base rates, calibration forces their true-positive to false-positive ratios to differ, so calibration parity and equalized odds cannot both hold; only equal base rates or perfect prediction escape.

Example: COMPAS: the base rates of re-arrest in the available data differed across racial groups, so equal error rates and equally meaningful scores could not both hold; Exercise 6: 40% high-need in population X versus 20% in Y, reflecting documented disparities in social determinants of health.

Not to be confused with: positive prediction rate (what the model says yes to, not what is true; the chapter's tables show both rows)

**false positive**  *(also: false alarm)*
*in the chapter text: Ch 1 ×2, Ch 2 ×18, Ch 6 ×3, Ch 7 ×12, Ch 10 ×1 · kind: concept*

> The other 9,999 do not have the disease. "Ninety-nine percent accurate" also means the test correctly returns negative on 99% of healthy people. The other 1% — that is 0.01 times 9,999, about 100 people — get a false positive.
> — *the book, Ch 2 line 254; explained across several passages, no single defining sentence*

In plain words: A healthy person whom the test wrongly flags as positive. When the condition is rare the healthy group is so large that false positives swamp the true ones.

Example: About 100 of the 9,999 healthy people get a false positive, against 1 true positive.

Not to be confused with: true positive

**specificity**  *(also: true negative rate)*
*in the chapter text: Ch 2 ×3, Ch 6 ×1, Ch 9 ×2, Ch 11 ×1 · kind: metric*

> I used it as both the true-positive rate and the true-negative rate. Those are two different numbers — sensitivity and specificity — and a real test has two, not one.
> — *the book, Ch 2 line 259; explained across several passages, no single defining sentence*

In plain words: Of the people who are healthy, the share the test correctly returns negative on; the same idea as the true negative rate. The healthy people it misses become false positives.

Example: With 99% specificity, about 100 of the 9,999 healthy people in the 10,000-person example still get a false positive.

Not to be confused with: sensitivity

**true-positive rate**  *(also: TPR)*
*in the chapter text: Ch 2 ×2, Ch 6 ×1, Ch 7 ×7 · kind: metric*

> The true-positive rate — among those who actually were positive, the fraction the model correctly flagged — is the same in both groups.
> — *the book, Ch 7 line 49*

In plain words: Among the people who really are positive, the share the model correctly flags. Equalized odds requires it to be equal across groups.

Example: In the calibration-satisfying table it is 0.60 for group A and 0.70 for group B.

Not to be confused with: positive predictive value (conditions on a positive prediction, not on a positive truth)

**loss function**  *(also: training objective)*
*in the chapter text: Ch 6 ×5, Ch 7 ×2 · kind: concept*

> In-processing modifies the training objective, adding fairness penalties to the loss or using adversarial methods where a discriminator tries to predict the protected attribute from the model's representations and the model is trained to fool it.
> — *the book, Ch 7 line 349; explained across several passages, no single defining sentence*

In plain words: The training objective the model optimizes. The chapter says an engineer who just optimizes is choosing whatever the loss function encodes, and in-processing fixes fairness by adding fairness penalties to it.

Example: COMPAS: the engineers let a loss function stand in for a decision that belonged to someone accountable.

**heavy-tailed distribution**  *(also: heavy-tailed regime; heavy-tailed; heavy-tailed loss)*
*in the chapter text: Ch 2 ×1 · kind: concept*

> Finite variance breaks down in heavy-tailed distributions — distributions where extreme events are not rare enough for averaging to dampen them.
> — *the book, Ch 2 line 452; explained across several passages, no single defining sentence*

In plain words: A distribution where extreme events are common enough that averaging does not tame them, so the sample mean keeps getting moved by the next observation however much data you have. Examples in the chapter include wealth, file sizes, earthquake magnitudes and the cost of an AI system being wrong.

Example: Most of a system's wrong outputs are minor inconveniences, but one in a thousand kills a patient or wipes a database.

Not to be confused with: Gaussian (bell-curve) distribution

**Bayes' theorem**
*in the chapter text: Ch 2 ×12 · kind: method*

> The thing the formula makes unmissable is this: the posterior — what you believe after seeing the evidence — is proportional to the prior times the likelihood. The prior is in the numerator, with the same weight as the quality of the evidence. You cannot legitimately ignore it.
> — *the book, Ch 2 line 305; explained across several passages, no single defining sentence*

In plain words: A formula for updating a belief: multiply the prior by the likelihood of the evidence and divide by the total probability of the evidence, to get the posterior. Because the prior sits in the numerator with the same weight as the test's quality, you cannot legitimately ignore it.

Example: Prior 0.0001 with a 99% test and a positive result gives P(disease | positive) of about 0.0098, roughly one percent.

Not to be confused with: total probability theorem (the same machinery run in the opposite direction)

**uncertainty component (base rate)**  *(also: base rate)*
*in the chapter text: Ch 11 · kind: metric*

> The Brier decomposition tells you whether the problem is discrimination, calibration, or base rate.
> — *the book, Ch 11 line 425; explained across several passages, no single defining sentence*

In plain words: The base-rate part of the Brier score: how often the positive outcome occurs in the data, entered in the chapter's formula as the base rate times one minus the base rate. It is the first of the three parts, with resolution subtracted and the calibration part added.

Example: Exercise W4 gives a validation set with base rate 0.20 and an Uncertainty term of 0.160.

## Failure modes and points of failure (6)

**failure mode**  *(also: trust calibration failure mode)*
*in the chapter text: Ch 1 ×5, Ch 2 ×2, Ch 3 ×3, Ch 4 ×2, Ch 5 ×6, Ch 8 ×26, Ch 9 ×18, Ch 10 ×1, Ch 11 ×12, Ch 12 ×14, Ch 13 ×6 · kind: concept*

> identify which trust calibration failure mode a deployment is exhibiting from its metric profile.
> — *the book, Ch 11 line 25; explained across several passages, no single defining sentence*

In plain words: A named way a deployment, claim or process goes wrong that you can recognise from its signs. The chapter describes each one by what it looks like, why standard metrics miss it, and what would catch it instead, as in its table of construct validity failure, calibration without usefulness and distribution shift.

Example: Overconfidence is called "a well-documented and common failure mode in a large class of models"; distribution shift is called "the dominant failure mode in deployed medical AI".

**delegation map**  *(also: the map)*
*in the chapter text: Ch 8 ×4, Ch 9 ×35, Ch 12 ×5, Ch 13 ×8 · kind: framework*

> A delegation map describes, for each step in a pipeline, who owns the step (AI, human, or hybrid), what goes in, what comes out, and — crucially — what signals that the step has completed correctly and the next step can proceed. That signal is the handoff condition.
> — *the book, Ch 9 line 46; explained across several passages, no single defining sentence*

In plain words: A written document that lists, for each step of an AI pipeline, who owns it (AI, human or hybrid), what goes in and out, and what has to be true before the next step starts. It is the instrument that records who does what and how each handoff is checked.

Example: The Paper Summarizer's six-step map: Claude owns steps 2, 3 and 5 and a human owns steps 1, 4 and 6.

**handoff condition**  *(also: the load-bearing element)*
*in the chapter text: Ch 8 ×5, Ch 9 ×37 · kind: concept*

> That signal is the handoff condition. It is the load-bearing element of the entire map, and it has exactly one non-negotiable property: it has to be testable.
> — *the book, Ch 9 line 46; explained across several passages, no single defining sentence*

In plain words: The signal that a step has finished correctly so the next step can start. It is the key piece of the delegation map, and it must be testable by someone who did not build the pipeline.

Example: "The AI produces a score in the interval zero to one with a confidence interval. The human accepts the score, requests re-scoring, or overrides." and an override needs one of four justification codes.

**verification cost**
*in the chapter text: Ch 9 ×2 · kind: concept*

> The first question is verification cost. Can a human verify the AI's output cheaply, or does verification require resources comparable to producing the output from scratch? Tasks that are cheap to verify — proofreading a generated summary against a source document, sanity-checking a numeric calculation, scanning a list of candidates — are good AI tasks.
> — *the book, Ch 9 line 100*

In plain words: How costly it is for a person to check the AI's output: cheap if checking is quick, expensive if it takes about as much work as producing the output. When checking is expensive, the cost itself pushes the supervisor toward accepting the output, which the chapter calls economics acting on attention, not a character flaw.

Example: Cheap: proofreading a generated summary against its source. High risk: verification needs a domain expert plus 30 minutes or more per item.

**point of failure**
*in the chapter text: Ch 9, Ch 11 · kind: concept*

> A pipeline missing any of items 5–8 is unsupervised — and it runs beautifully, right up until the uncaught error surfaces downstream, usually discovered by the person it harmed. The failure that costs you is the one that does not stop the pipeline.
> — *the book, Ch 9 line 135; explained across several passages, no single defining sentence*

In plain words: A place where a pipeline can go wrong; the phrase is not in the chapter, whose nearest wording is where failures happen and where they surface. The chapter's point is that the costly failure is the one that does not stop the pipeline and is found downstream, so the riskiest places are the handoffs, where authority passes between AI and human.

Example: Paper Summarizer: step 3 into step 4 (a researcher waves through HIGH-confidence extractions) and step 5 into step 6 (a sign-off treated as proofreading).

Not to be confused with: failure mode (the way a step fails, rather than where)

**single point of failure**
*in the chapter text: Ch 9 · kind: concept*

> The two highest-risk handoffs are both AI-to-human: Step 3 into Step 4, where the danger is that the researcher waves through HIGH-confidence extractions and a domain-critical qualification vanishes; and Step 5 into Step 6, where the danger is treating a sign-off as proofreading rather than interpretation, so a misleading framing ships.
> — *the book, Ch 9 line 197; explained across several passages, no single defining sentence*

In plain words: One place where a single lapse lets a failure through; the phrase is not in the chapter. Its nearest ideas are the two AI-to-human handoffs where one researcher's lapse lets an error or misleading framing ship, and the sign-off authority item that requires one named, accountable human.

Example: If the Step 4 researcher waves through a HIGH-confidence extraction, a dropped qualification such as "on the training set only" reaches the summary.

Not to be confused with: failures that distribute across the team with no accountable human (the opposite problem)

## Calibration and temperature (11)

**calibration**  *(also: calibrating; calibration diagnostic)*
*in the chapter text: Ch 2 ×44, Ch 4 ×6, Ch 6 ×8, Ch 7 ×25, Ch 8 ×1, Ch 9 ×10, Ch 10 ×19, Ch 11 ×107, Ch 12 ×2, Ch 13 ×10 · kind: concept*

> It is called calibration, and a model can be very accurate without being calibrated, and the difference matters. A model is calibrated when its stated probabilities match what actually happens. If the model says "seventy percent confident" on a thousand cases, you want roughly seven hundred of those cases to turn out positive.
> — *the book, Ch 2 line 404*

In plain words: How closely the confidence a model states matches how often it is actually right, so that among 1,000 cases where it says 70%, about 700 turn out positive. The chapter calls it the most operationally important diagnostic; it is a different thing from accuracy, and it applies to people's forecasts as well as to models.

Example: A net that says 99% when it should say 85% is badly miscalibrated at the high end; your own 90% intervals that contain the answer only about half the time show the same problem in a person.

Not to be confused with: accuracy (a model can be very accurate without being calibrated)

**ECE**
*in the chapter text: Ch 2 ×1, Ch 11 ×60, Ch 13 ×1 · kind: metric*

> Chapter 11 will use the calibration plan to compute Brier and ECE.
> — *the book, Ch 2 line 633*

In plain words: A calibration score named in the LLM exercise: Chapter 11 will compute it, together with the Brier score, from the calibration data your plan collects. This chapter does not define it or spell out the name.

Example: The calibration plan's log of stated confidence against ground truth is what Chapter 11 will score.

Not to be confused with: calibration curve (a picture of the same match between stated and actual)

**overconfidence**
*in the chapter text: Ch 2 ×1, Ch 11 ×6, Ch 13 ×1 · kind: failure mode*

> Overconfidence (curve below the diagonal): the model's predicted probabilities are higher than warranted. A model predicting "90% positive" that is actually right 70% of the time is overconfident.
> — *the book, Ch 11 line 174*

In plain words: The model claims more certainty than its track record justifies; on a reliability diagram the curve sits below the diagonal. It is the miscalibration direction the chapter calls common in many models.

Example: A model predicting "90% positive" that is actually right 70% of the time.

Not to be confused with: underconfidence

**calibration curve**  *(also: reliability diagram)*
*in the chapter text: Ch 2 ×9, Ch 6 ×1, Ch 10 ×7, Ch 11 · kind: method*

> Put the model's stated probability on the horizontal axis. Put the actual frequency of positives on the vertical axis. A perfectly calibrated model traces the diagonal — where stated and actual are equal.
> — *the book, Ch 2 line 408; explained across several passages, no single defining sentence*

In plain words: A plot of what the model says against what actually happens: stated probability on one axis, the actual share of positives on the other. A perfectly calibrated model sits on the diagonal, and the shape of how a curve peels off it shows how the model is wrong.

Example: Figure 2.8: the model is reasonably calibrated in the middle of its range (says 60%, about right) but badly overconfident toward the top (says 99% when it should say 85%).

Not to be confused with: accuracy (a calibration curve shows what accuracy metrics hide)

**miscalibrated**  *(also: miscalibration)*
*in the chapter text: Ch 2 ×2, Ch 9 ×1, Ch 11 ×6 · kind: failure mode*

> A miscalibrated model peels off the diagonal, and the shape of how it peels off tells you something about how the model is wrong.
> — *the book, Ch 2 line 408; explained across several passages, no single defining sentence*

In plain words: A model is miscalibrated when its stated probabilities do not match what happens, so its calibration curve peels off the diagonal; overconfident and underconfident are the two directions. The chapter notes a model can be calibrated on clean inputs and wildly miscalibrated on perturbed ones (Chapter 4).

Example: Exercise 12: a model well-calibrated at 0.4–0.6 confidence but systematically overconfident above 0.85.

Not to be confused with: overconfident and underconfident (the two directions of miscalibration)

**Brier score**  *(also: BS)*
*in the chapter text: Ch 2 ×1, Ch 11 ×22 · kind: metric*

> The Brier score is the foundational metric for probabilistic prediction quality. For a binary outcome, it is the mean squared difference between the predicted probability and the actual binary outcome across all predictions:
> — *the book, Ch 11 line 124; explained across several passages, no single defining sentence*

In plain words: The average squared gap between the predicted probability and what actually happened (1 or 0). It runs from 0 (perfect) to 1 (perfectly wrong), and a classifier that predicts 0.5 for every instance scores 0.25.

Example: A random classifier predicting 0.5 for all instances gets a Brier score of 0.25; a well-calibrated classifier should substantially beat that baseline.

Not to be confused with: accuracy (the Brier score also penalizes being confidently right when hedging was warranted)

**temperature scaling**
*in the chapter text: Ch 2 ×6, Ch 11 ×15 · kind: method*

> they also showed a cheap fix: temperature scaling. You take a single learned parameter $T$ and divide the pre-softmax logits $z$ by it before the softmax
> — *the book, Ch 2 line 415; explained across several passages, no single defining sentence*

In plain words: A cheap fix for an overconfident model: divide its raw pre-softmax scores by one learned number T, fit on held-out data, which softens its stated confidence without changing how it ranks cases. It repairs average calibration only on the distribution you fit it to and goes stale silently if the world drifts.

Example: It repairs a net that says 99% when it should say 85%, but not after distribution shift.

**Maximum Calibration Error**  *(also: MCE)*
*in the chapter text: Ch 11 ×1 · kind: metric*

> A companion metric — not an escape from bin-dependence, since it is computed over the same bins and is if anything more sensitive to how they are drawn — is the Maximum Calibration Error (MCE), which reports the worst-case gap across bins rather than the weighted average:
> — *the book, Ch 11 line 162*

In plain words: The largest bin gap between mean confidence and actual accuracy, instead of the average gap. It matters in safety-critical deployments, because a low ECE can hide one confidence range where the model is badly overconfident.

Example: A system with low ECE but high MCE in one confidence bin may be dangerous even though the aggregate looks acceptable.

Not to be confused with: ECE (average gap, not worst case)

**decorative number**  *(also: decorative claim)*
*in the chapter text: Ch 2 ×4 · kind: concept*

> The number on the screen, by itself, is decorative. It might mean what you think it means; it might be off by a lot; you have no way of telling without checking.
> — *the book, Ch 2 line 423; explained across several passages, no single defining sentence*

In plain words: A confident-looking number that nobody has checked against reality, so you cannot tell how far off it is. A model's stated probability stays decorative until you see its calibration curve on data from the real deployment.

Example: A net says 99% when it should say 85%, and says it fluently.

Not to be confused with: a calibrated number (one backed by a calibration curve on deployment data)

**Expected Calibration Error**  *(also: ECE)*
*in the chapter text: Ch 11 ×4 · kind: metric*

> The Expected Calibration Error (ECE) is the most commonly reported calibration metric in deployed systems. It operates by binning predictions into equal-width intervals and measuring the weighted average gap between mean predicted confidence and mean actual accuracy in each bin:
> — *the book, Ch 11 line 152; explained across several passages, no single defining sentence*

In plain words: Sort predictions into equal-width confidence bins, then average, weighted by bin size, the gap between mean predicted confidence and actual accuracy in each bin. Zero is perfect calibration; the chapter's rules of thumb (about 0.02 to 0.05 good, above 0.10 systematic miscalibration) are unsourced heuristics, not facts.

Example: "We observe ECE = 0.04 on the global test set" is the chapter's example of a correctly worded ECE claim.

Not to be confused with: Maximum Calibration Error (worst bin instead of weighted average)

**conformal prediction**
*in the chapter text: Ch 11 ×8 · kind: method*

> Conformal prediction offers something the metrics above do not: a provable finite-sample coverage guarantee.
> — *the book, Ch 11 line 274; explained across several passages, no single defining sentence*

In plain words: A method that returns a set of possible labels for each case, built so the true label is inside the set with a chosen probability, whatever the model or data distribution as long as the data are exchangeable. It does this by computing a non-conformity score for each case in a held-out calibration set and taking a quantile of those scores as the cutoff.

Example: For ambiguous cases the predictor may say "positive or negative, I'm not sure".

## Proxy, drift and the gap (5)

**distribution shift**
*in the chapter text: Ch 1 ×1, Ch 2 ×12, Ch 3 ×3, Ch 4 ×17, Ch 10 ×1, Ch 11 ×19, Ch 13 ×5 · kind: concept*

> The training set is the past. The deployment is the future. Distribution shift is the technical name for the world declining to cooperate.
> — *the book, Ch 2 line 384*

In plain words: When the real world after deployment stops looking like the data the model was trained on, so the patterns it learned no longer apply while its confidence stays high. The chapter reads it as Hume's point that the future is free to differ from the past.

Example: Models trained on pre-2020 medical imaging were deployed in 2021, after COVID had changed the lung images and the population that ended up in scanners.

**proxy**  *(also: proxies)*
*in the chapter text: Ch 3 ×3, Ch 4 ×58, Ch 5 ×2, Ch 6 ×8, Ch 7, Ch 10 ×8, Ch 11 ×1, Ch 13 ×1 · kind: concept*

> Sensitive attributes reconstruct from proxies — zip code, surname, occupation — that correlate with group membership. Omit race but keep zip code and the model may be using race anyway. FTU blocks the direct use of an attribute; it does nothing about indirect discrimination through correlated features.
> — *the book, Ch 7 line 209*

In plain words: A feature such as zip code, surname or occupation that correlates with group membership, so the model can effectively rebuild the sensitive attribute even after it is dropped. Proxies are how indirect discrimination happens through correlated features.

Example: Zip code standing in for race.

**drift**  *(also: PSI)*
*in the chapter text: Ch 1 ×1, Ch 2 ×3, Ch 4 ×3, Ch 6 ×1, Ch 10 ×1, Ch 11 ×4, Ch 12 ×2, Ch 13 ×1 · kind: failure mode*

> PSI on the three highest-weight input features stays below 0.10 week-over-week; alert fires and triggers human review if breached.
> — *the book, Ch 1 line 117; explained across several passages, no single defining sentence*

In plain words: The chapter does not define drift; it appears as the vague claim "We have mitigated drift," which the table rewrites as a checkable test. The test is that PSI on the three highest-weight input features stays below 0.10 week-over-week, with an alert and human review if breached.

Example: "We have mitigated drift" becomes: PSI on the three highest-weight input features stays below 0.10 week-over-week.

**Goodhart's law**  *(also: when a measure becomes a target, it ceases to be a good measure)*
*in the chapter text: Ch 1 ×1 · kind: concept*

> There is a name for what happens when you lean on the easy thing. Goodhart's law, in the phrasing everyone quotes: when a measure becomes a target, it ceases to be a good measure (Goodhart, 1975; Strathern, 1997). The Netflix contest was that sentence with a million-dollar prize attached.
> — *the book, Ch 1 line 46*

In plain words: When people aim at a number as the goal, the number stops being a reliable sign of the thing it was meant to stand for.

Example: The Netflix contest paid a million dollars to improve one rating-error number, and by the time it was won that number was no longer the thing Netflix needed to know.

**detecting distribution shift**  *(also: drift)*
*in the chapter text: Ch 2 · kind: method*

> You will not, in general, be able to detect this kind of drift just by watching the model's outputs. The model continues to look confident through the shift; the shape of its outputs stays similar; the dashboards stay green. Detection requires watching the inputs, watching the outputs, and — most of all — watching the actual outcomes the model was supposed to predict, when those outcomes eventually become observable.
> — *the book, Ch 2 line 396; explained across several passages, no single defining sentence*

In plain words: A model looks equally confident while the world changes, so dashboards of its outputs stay green. You catch a shift by watching the inputs, the outputs and above all the real outcomes once they become observable.

Example: Most deployments do not budget for this and find out about distribution shift through the harm.

## The ladder: association, intervention, counterfactual (5)

**counterfactual**  *(also: Rung 3; the level of imagining)*
*in the chapter text: Ch 4 ×19, Ch 5 ×25, Ch 6 ×2, Ch 7 ×20, Ch 11 ×1, Ch 12 ×31, Ch 13 ×5 · kind: concept*

> Rung 3 — Counterfactual. The level of imagining. What would have happened to this specific case if X had been different, holding everything else fixed?
> — *the book, Ch 6 line 258*

In plain words: Imagining: asking what would have happened to this specific case if X had been different, with everything else held fixed. It is the deepest and hardest level to reach from data alone, and the chapter only names it here because Chapter 4 opened it and Chapter 12 closes it.

Example: Chapter 4's robustness gap is a Rung 3 question.

Not to be confused with: intervention (Rung 2 asks what happens if we set X; Rung 3 asks what would have happened to this specific case)

**intervention**  *(also: Rung 2; the level of doing)*
*exam focus (Bear) · in the chapter text: Ch 4 ×3, Ch 5 ×10, Ch 6 ×46, Ch 7 ×7, Ch 8 ×7, Ch 12 ×5, Ch 13 ×1 · kind: concept*

> Rung 2 — Intervention. The level of doing. What is the probability of Y if we set X to a particular value?
> — *the book, Ch 6 line 254*

In plain words: Doing: asking what happens to Y if we set X to a particular value instead of just watching it, written P(Y | do(X = x)). Doing severs the tangles that make an observed X move with other things, so it can show whether X is actually a cause.

Example: If we changed race while holding all other features fixed, would the loan denial rate change? Or: preventing the rooster from crowing does not stop the sunrise.

Not to be confused with: association (Rung 1): observing X is not the same as making X happen, and equal Rung 1 metrics do not certify causal fairness

**Pearl's ladder**  *(also: ladder of causal reasoning; rungs)*
*in the chapter text: Ch 4 ×5, Ch 5 ×1, Ch 6 ×13, Ch 7 ×2, Ch 12 ×2 · kind: framework*

> The tool is due to Judea Pearl, and it is, in my judgment, the single most useful conceptual instrument in this book. He calls it a ladder of causal reasoning, with three rungs.
> — *the book, Ch 6 line 240*

In plain words: Pearl's three levels of causal reasoning: Rung 1 is seeing what goes with what (association), Rung 2 is doing (intervention), Rung 3 is imagining what would have happened (counterfactual). Each rung asks a different kind of question, and evidence from a lower rung cannot answer the higher rung's questions.

Example: Rung 1: P(Y | X). Rung 2: P(Y | do(X = x)). Rung 3: what would have happened to this case if X had been different.

**association**  *(also: Rung 1; the level of correlation)*
*in the chapter text: Ch 3 ×2, Ch 4 ×1, Ch 5 ×2, Ch 6 ×2, Ch 12 ×2 · kind: concept*

> Rung 1 — Association. The level of correlation. What is the probability of Y, given that we observe X?
> — *the book, Ch 6 line 252*

In plain words: Seeing: noticing what goes together in the data, the probability of Y given that we observe X, written P(Y | X). It is the level of correlation, where most machine learning, calibration curves and most fairness metrics live, and where thinking about deployed AI quietly stops.

Example: Is the denial rate equal across racial groups in the data? Or: roosters crow and the sun rises, so sunrise is likely given that the rooster crowed.

Not to be confused with: intervention (Rung 2): observing X is not the same as making X happen, because an observed X can be tangled up with other things that move with it

**Rung 1 (association)**  *(also: Rung 1; associational rung; observational; associative)*
*in the chapter text: Ch 5 ×2, Ch 6 ×1 · kind: concept*

> It does not show whether the contribution is causal or correlational. SHAP lives entirely on Pearl's Rung 1, the associational rung — Chapter 4 sketched the ladder, and Chapter 6 works the first two rungs in detail. The features it attributes high importance to may be confounders, mediators, colliders, or actual causes — and SHAP does not distinguish.
> — *the book, Ch 5 line 49; explained across several passages, no single defining sentence*

In plain words: Rung 1 is the level of association: what goes with what, or what the model used. SHAP and LIME stay on this rung, so their attributions describe the model but cannot show cause; the chapter calls this observational.

Example: The zip code attribution of 0.035 is observational: it does not say whether the effect would persist if an applicant moved.

Not to be confused with: Rung 2 (intervention)

## Explainability, transparency, interpretability (4)

**transparency**
*exam focus (Bear) · in the chapter text: Ch 3 ×1, Ch 5 ×8, Ch 6 ×1, Ch 8 ×1, Ch 10 ×1, Ch 12 ×2, Ch 13 ×1 · kind: concept*

> Transparency is a property of the system. A transparent system is one whose internals are inspectable — code, parameters, architecture, training data, all available to look at. Transparency is, in principle, binary: either the internals are inspectable or they aren't.
> — *the book, Ch 5 line 287*

In plain words: Transparency means the system's insides can be inspected: code, parameters, architecture and training data. It is about access, not understanding, and in principle it is yes-or-no.

Example: A system with 175 billion parameters whose code, weights and training data you hold is fully transparent yet uninterpretable.

Not to be confused with: explainability and interpretability (the three do not entail each other)

**explainability**
*exam focus (Bear) · in the chapter text: Ch 5 ×48, Ch 6 ×1, Ch 8 ×8, Ch 13 ×1 · kind: concept*

> Explainability is a property of outputs. An explainable output is one accompanied by a reason. SHAP, LIME, and counterfactuals are explainability tools.
> — *the book, Ch 5 line 289*

In plain words: Explainability means each output comes with a stated reason for it. SHAP, LIME and counterfactuals produce such reasons, but the reasons may be more or less informative.

Example: SHAP attributions on every prediction make a system explainable, yet the practitioner may still be unable to build a coherent mental model from them.

Not to be confused with: interpretability (procurement language often asks for explainability and means interpretability for the affected user)

**interpretability**
*exam focus (Bear) · in the chapter text: Ch 5 ×9 · kind: concept*

> Interpretability is a property of the understanding a human builds from the explanations. An interpretable system is one a human can build a working mental model of, sufficient to predict the system's behavior in novel cases.
> — *the book, Ch 5 line 291*

In plain words: Interpretability means a person can build a working mental model of the system, good enough to predict what it will do on new cases. It depends on who is reading, so one system can be interpretable to some people and not to others.

Example: A system can be interpretable to the developer and not to the loan applicant.

Not to be confused with: explainability (meeting a SHAP-attribution requirement does not make a system interpretable to the affected user)

**counterfactual explanation**  *(also: counterfactual; counterfactuals)*
*exam focus (Bear) · in the chapter text: Ch 5 ×6 · kind: method*

> Counterfactual explanations. Instead of "feature X contributed +0.3 to the prediction," the explanation is: "if feature X had been at value Y instead, the prediction would have been Z."
> — *the book, Ch 5 line 267*

In plain words: A counterfactual explanation says how the prediction would change if a feature had a different value, rather than how much the feature contributed. It is closest to the practitioner's real question of what the model would do under a different scenario.

Example: If your income were $5,000 higher, the loan would be approved.

Not to be confused with: SHAP attribution (a Rung 1 statement)

## Agents and consequence (13)

**prompt injection**  *(also: prompt injection as structural feature)*
*in the chapter text: Ch 4 ×8, Ch 7 ×1, Ch 8 ×6 · kind: failure mode*

> LLM-based agents process instructions and data as tokens in a context window, making the two fundamentally indistinguishable. Prompt injection is therefore a structural feature of these systems rather than a fixable bug.
> — *the book, Ch 8 line 97*

In plain words: Slipping instructions to an agent inside what looks like ordinary data. It works because the agent reads instructions and data as the same kind of tokens and cannot reliably tell them apart.

Example: Case #10: planted meta-instructions in an externally editable GitHub Gist (the "constitution") that Ash obeyed.

**prediction system**
*in the chapter text: Ch 7 ×1, Ch 8 ×12 · kind: concept*

> A model that classifies images is a prediction system. Its outputs are statements about the world. Validation asks: are those statements correct?
> — *the book, Ch 8 line 35*

In plain words: A model whose outputs are statements about the world, such as a label for an image, so a wrong output is wrong for one input. Validating it means asking whether the statements are correct.

Example: A model that classifies images.

Not to be confused with: consequence system

**resource exhaustion**  *(also: resource exhaustion through interaction)*
*in the chapter text: Ch 8 ×5, Ch 9 ×1 · kind: failure mode*

> The #4/#5 row is this mode: agents produce resource consumption that no individual agent would produce in isolation. Single-agent validation finds well-behaved agents; the interaction pattern is the failure.
> — *the book, Ch 8 line 337*

In plain words: Agents interacting with each other (or with an outside sender) use up resources such as tokens, memory or server capacity in a way no single agent would on its own. Testing agents one at a time misses it; the fix named is explicit budget caps and rate limits.

Example: Case #5: a non-owner repeatedly emailing ~10MB files drove memory-file creation until the email server hit a DoS condition.

**consequence system**
*in the chapter text: Ch 8 ×8 · kind: concept*

> A model that takes actions in the world is a consequence system. Its outputs are state changes. Validation asks: are those state changes the right ones, and does the system know what state it has produced?
> — *the book, Ch 8 line 37*

In plain words: A model that acts in the world, so what it produces is a change to the state of things, not a statement. Validating it means asking whether the changes were the right ones and whether the system knows what it changed.

Example: Ash's agent was asked to delete one email and instead reset the whole email account.

Not to be confused with: prediction system

**cascading hallucination**
*in the chapter text: Ch 8 ×6 · kind: failure mode*

> Agent A produces an output that is wrong with low probability; Agent B conditions on it; Agent C compounds further, until the error rate is dominated by cascading dynamics, not individual agents' error rates.
> — *the book, Ch 8 line 335*

In plain words: A small error from one agent is passed on, relied on by the next agent and made worse, so the whole system's error rate ends up far above any single agent's. Checking each agent alone does not reveal it.

Example: "You validated each agent at one percent; the compound system fails at thirty."

**authority laundering**
*in the chapter text: Ch 8 ×6 · kind: failure mode*

> Agent A passes data to Agent B as a legitimate output; B cannot verify its provenance, so the data launders its authority through A's channel. The constitution attack (#10) is the variant. Single-agent access controls do not prevent it; provenance tracking across agents is required.
> — *the book, Ch 8 line 339*

In plain words: One agent hands another some data as if it were a legitimate output, and the second agent cannot check where it really came from, so the data borrows the first agent's standing. Tracking where data came from across agents is what catches it.

Example: Case #10: Ash obeyed a planted, externally editable "constitution" (a GitHub Gist) and shared it with another agent.

**autonomy-competence gap**
*in the chapter text: Ch 8 ×5 · kind: concept*

> The study's own framing for the gap those failures exposed is the "autonomy-competence gap": the agents took actions appropriate to Mirsky's L4 — installing packages, executing arbitrary commands, rewriting their own configuration — while operating with L2-level understanding of what those actions meant.
> — *the book, Ch 8 line 65*

In plain words: The agents acted with a high level of independence (installing packages, running any command, rewriting their own settings) while understanding what those actions meant only at a much lower level. The chapter calls it a fundamental failure that may not close through scaffolding alone.

Example: Agents installed packages and rewrote their own configuration (Mirsky L4 actions) with only L2-level understanding.

**false success report**
*in the chapter text: Ch 8 ×4 · kind: failure mode*

> Here is what is actually happening, stated as plainly as I can: the agent's completion report and the world's state contradicted each other, and neither the agent nor any automated system noticed. That single fact — a false success report that nothing caught — is the entire architecture of what makes agentic validation different.
> — *the book, Ch 8 line 15*

In plain words: The agent says the job is done while the real state of the world shows it is not, and nothing catches the mismatch. The way to catch it is to check the world independently of the agent's report.

Example: Ash reported "Email account RESET completed" and claimed the secret had been deleted, but the email was still on Proton Mail.

**identity confusion**  *(also: identity confusion in shared channels)*
*in the chapter text: Ch 8 ×2 · kind: failure mode*

> In Case #4, Flux read its own prior messages in a shared Discord channel, took them as coming from a second instance of itself, and posted its own source code publicly to compare with its "twin." This is not a repetition loop but a conceptual confusion about identity arising specifically from multi-agent infrastructure, with no single-agent analog.
> — *the book, Ch 8 line 341*

In plain words: In a shared channel an agent mistakes its own earlier messages for a second agent, which only happens when several agents share infrastructure. It is a confusion about who is speaking, not a repeating loop.

Example: Flux treated its own messages as coming from a "twin" and posted its source code publicly.

Not to be confused with: repetition loop (the chapter says it is not one)

**effective data scope**
*in the chapter text: Ch 8 ×1 · kind: concept*

> This case establishes the concept of effective data scope — the scope of data that can be extracted from the agent's access, as opposed to the scope the deployment team modeled. The gap between the two is the measurement you need.
> — *the book, Ch 8 line 182*

In plain words: All the data that can actually be pulled out through the agent's access, including by indirect requests, as opposed to the data the deployment team planned for. The size of the gap between the two is what a validator measures.

Example: Case #3: a request for email metadata returned email bodies that held an SSN and a bank account number.

Not to be confused with: documented scope

**displayed identity**  *(also: presented identity)*
*in the chapter text: Ch 8 ×1 · kind: concept*

> The agents in the study use displayed identity rather than verified identity as the primary authority signal. Any agent system relying on presented identity — rather than cryptographically grounded or multi-factor authentication — remains susceptible to session-boundary attacks in which trust context does not transfer and prior defensive safeguards are effectively reset.
> — *the book, Ch 8 line 252*

In plain words: The name or label a person shows (such as a Discord display name) that the agent treats as proof of who they are, even though anyone can change it. Relying on it lets a spoofer be accepted as the owner.

Example: A non-owner changed their Discord display name to "Chris" and was accepted as the owner in a new private channel.

Not to be confused with: verified identity

**runaway loops**  *(also: runaway loop)*
*in the chapter text: Ch 8 ×2 · kind: failure mode*

> Robustness at the interaction level: what happens when behavior is triggered repeatedly with no stopping condition? Single-agent testing misses it.
> — *the book, Ch 8 line 262; explained across several passages, no single defining sentence*

In plain words: A process that keeps repeating with no stopping condition, such as two agents passing messages back and forth for days or a routine request that spawns endless shell commands. Single-agent testing misses it, so the supervisor needs monitoring that detects it.

Example: Case #4: two agents in a relay loop used about 60,000 tokens over nine days.

Not to be confused with: resource exhaustion (the loop is the mechanism behind Cases #4 and #5)

**verified identity**
*in the chapter text: Ch 8 ×1 · kind: concept*

> The agents in the study use displayed identity rather than verified identity as the primary authority signal. Any agent system relying on presented identity — rather than cryptographically grounded or multi-factor authentication — remains susceptible to session-boundary attacks in which trust context does not transfer and prior defensive safeguards are effectively reset.
> — *the book, Ch 8 line 252; explained across several passages, no single defining sentence*

In plain words: An identity confirmed by a check that a changed name cannot fake; the chapter names cryptographically grounded or multi-factor authentication as examples. The chapter wants verified authority, not displayed authority, before the agent acts on a request.

Example: Discord user IDs stay constant when a display name changes, which is how Ash first caught the spoofed Chris.

Not to be confused with: displayed identity

## Fairness, its kinds and trade-offs (14)

**disparate impact**
*in the chapter text: Ch 5 ×1, Ch 6 ×1, Ch 7 ×1 · kind: concept*

> Disparate treatment (direct) versus disparate impact (indirect through legitimate mediators) — the legal distinction rides on exactly this structure.
> — *the book, Ch 7 line 235*

In plain words: In the chapter's causal picture, the indirect path from the sensitive attribute to the prediction through legitimate mediators such as education or employment history. The chapter says the legal distinction between disparate treatment and disparate impact rides on this structure.

Not to be confused with: disparate treatment (direct)

**equalized odds**  *(also: TPR / FPR parity)*
*in the chapter text: Ch 6 ×2, Ch 7 ×22 · kind: metric*

> Equalized odds says the model's error rates do not depend on group. The true-positive rate — among those who actually were positive, the fraction the model correctly flagged — is the same in both groups. The false-positive rate — among those who actually were not positive, the fraction the model incorrectly flagged — is also the same
> — *the book, Ch 7 line 49*

In plain words: The model makes the same kinds of mistakes in every group: among people who truly are positive the same share are caught, and among people who truly are not the same share are wrongly flagged. Its values claim is that the cost of being wrongly flagged should fall equally on every group.

Example: ProPublica found that Black defendants who did not go on to be re-arrested were misclassified as high-risk more often than white defendants, a violation of equalized odds.

Not to be confused with: calibration parity (the other side of the COMPAS dispute) and demographic parity

**calibration parity**  *(also: predictive parity; calibration)*
*in the chapter text: Ch 6 ×4, Ch 7 ×16 · kind: metric*

> Calibration parity — sometimes called predictive parity — says the model's stated probabilities track empirical frequencies equally well in both groups
> — *the book, Ch 7 line 57*

In plain words: A score means the same thing in every group: when the model says seventy percent, about seventy percent of people in group A and in group B really are positive. The chapter calls this the model's probability honesty, and says that for a yes/no score it forces equal positive predictive value across groups.

Example: Northpointe said a COMPAS score of seven meant about the same likelihood of re-arrest whether the defendant was Black or white.

Not to be confused with: equalized odds (the two cannot both hold when base rates differ)

**demographic parity**  *(also: statistical parity)*
*in the chapter text: Ch 6 ×2, Ch 7 ×17 · kind: metric*

> Demographic parity — sometimes called statistical parity — says the rate of positive predictions does not depend on group membership
> — *the book, Ch 7 line 43*

In plain words: The model says yes to the same share of people in every group, so the positive-prediction rate does not depend on group. It looks only at the model's outputs, before anything is compared with what really happened; its values claim is structural redress over conditional accuracy (equal outcomes whatever the base rates).

Example: In the calibration-satisfying table the positive prediction rate is 0.48 for group A but 0.28 for group B, so demographic parity fails.

Not to be confused with: equalized odds and calibration parity (the other two definitions; the three cannot all hold when base rates differ)

**base-rate difference**  *(also: base rates differ; when base rates differ)*
*in the chapter text: Ch 6 ×1, Ch 7 ×6 · kind: concept*

> That last clause is where problem formulation does its work — sometimes the base-rate difference is the thing you are morally responsible for, and then demographic parity's redress claim gets teeth.
> — *the book, Ch 7 line 175; explained across several passages, no single defining sentence*

In plain words: The condition that triggers the impossibility theorem: the groups have different shares of true positives in the data, and the chapter says that is true on most real datasets. Chapter 6 is cited for why these differences exist and why the model may not be able to correct them; whether the deploying organization is responsible for the difference helps decide which metric to prioritize.

Example: Exercise 6: 40% of patients are high-need in population X and 20% in population Y, a difference reflecting documented disparities in social determinants of health.

**individual fairness**  *(also: similar individuals should be treated similarly; Aristotelian intuition)*
*in the chapter text: Ch 7 ×16 · kind: concept*

> Individual fairness runs on an Aristotelian intuition: similar individuals should be treated similarly.
> — *the book, Ch 7 line 183*

In plain words: Fairness checked person by person: people who are similar should get similar treatment, even when the group totals balance. It needs a way to say who counts as similar, which is the hard part.

Example: Two loan applicants with identical credit history, income and debt-to-income ratio but different zip codes.

Not to be confused with: group fairness (a model can satisfy demographic parity and still treat two nearly identical people wildly differently)

**counterfactual fairness**  *(also: counterfactual criterion)*
*in the chapter text: Ch 7 ×16 · kind: concept*

> Kusner et al. (2017) push the causal criterion down to the individual: counterfactual fairness. Not "are error rates equal across groups?" but "would this person have gotten the same decision if they had belonged to a different group, everything else about them held fixed?"
> — *the book, Ch 7 line 239*

In plain words: A person-level causal test: would this individual have got the same decision if they had belonged to a different group, with everything else about them held fixed? The model is counterfactually fair if its prediction comes out the same under A = a and A = a' for every individual.

Example: Loan-default model: had this person been white instead of Black, with U held fixed, would the predicted default probability move?

Not to be confused with: individual fairness (also person-level, but built on a similarity metric rather than a causal model)

**impossibility theorem**  *(also: fairness impossibility; the fairness impossibility)*
*in the chapter text: Ch 5 ×1, Ch 6 ×2, Ch 7 ×10 · kind: named result or case*

> The general principle: when base rates differ across groups, you cannot simultaneously satisfy calibration parity, equal false positive rates, and equal false negative rates. Pick any two; the third is forced into violation.
> — *the book, Ch 6 line 207*

In plain words: When groups have different base rates, no model can have calibration parity, equal false-positive rates and equal false-negative rates at once; pick any two and the third is forced into violation. All three hold together only if base rates are equal or prediction is perfect.

Example: COMPAS: ProPublica (unequal error rates) and Northpointe (equal calibration) were both correct.

**fairness through awareness**  *(also: FTA)*
*in the chapter text: Ch 7 ×2 · kind: concept*

> Specifying $d$ forces you to reason explicitly about the sensitive attribute — how much does group membership enter the similarity calculation? That is fairness through awareness (FTA), and it is uncomfortable because it makes you name the thing.
> — *the book, Ch 7 line 207*

In plain words: Openly deciding how much group membership counts when you judge whether two people are similar. It is uncomfortable because you have to name the sensitive attribute instead of hiding it.

Example: Deciding whether zip code counts in the similarity measure d for two loan applicants with the same finances.

Not to be confused with: fairness through unawareness (just dropping the sensitive attributes)

**fairness through unawareness**  *(also: FTU; dropping the sensitive attributes)*
*in the chapter text: Ch 7 ×1 · kind: failure mode*

> The tempting shortcut is fairness through unawareness (FTU): just drop the sensitive attributes from the model. Intuitive, and mathematically hollow. Sensitive attributes reconstruct from proxies — zip code, surname, occupation — that correlate with group membership.
> — *the book, Ch 7 line 209*

In plain words: Dropping the sensitive attribute from the model and calling it fair. It fails because proxies such as zip code can rebuild the attribute, so the chapter calls it a documentation choice that looks like a fairness guarantee.

Example: Omit race but keep zip code and the model may be using race anyway.

Not to be confused with: fairness through awareness (naming the attribute and deciding how much it counts)

**disparate treatment**
*in the chapter text: Ch 7 ×1 · kind: concept*

> Disparate treatment (direct) versus disparate impact (indirect through legitimate mediators) — the legal distinction rides on exactly this structure.
> — *the book, Ch 7 line 235*

In plain words: In the chapter's causal picture, the direct path from the sensitive attribute to the prediction. The chapter says the legal distinction between disparate treatment and disparate impact rides on this structure.

Not to be confused with: disparate impact (indirect, through mediators)

**group fairness**  *(also: group metrics; group fairness metrics)*
*in the chapter text: Ch 7 ×7 · kind: concept*

> Group fairness metrics tell you whether aggregate error or outcome rates differ across demographics. They cannot tell you whether two similar individuals are treated consistently — individual fairness requires a similarity metric $d$ that group metrics do not use.
> — *the book, Ch 7 line 411; explained across several passages, no single defining sentence*

In plain words: Fairness judged across whole demographic groups: do the groups end up with different aggregate error rates or outcome rates? The chapter's group metrics are demographic parity, equalized odds and calibration parity.

Example: ProPublica compared false-positive rates between Black and white defendants.

Not to be confused with: individual fairness (checks whether similar individuals are treated similarly, using a similarity metric d)

**Generalized Entropy Index**  *(also: GE index; GE(α); GE)*
*in the chapter text: Ch 7 ×2 · kind: metric*

> The Generalized Entropy (GE) Index measures exactly that, borrowing the mathematics economists use for income inequality: treat each person's "benefit" or "error burden" like income, and ask how unequally it's spread.
> — *the book, Ch 7 line 292; explained across several passages, no single defining sentence*

In plain words: A single number for how unequally benefit or error burden is spread across people, borrowed from income-inequality math. It gives a quantity rather than a verdict and can be split into within-group and between-group parts, but it needs a numeric benefit and is not causal.

Example: Exercise 5: mean benefit 0.6 and standard deviation 0.3.

Not to be confused with: group metrics (they give a verdict, not a quantity)

**correlates versus causes**  *(also: causal; causal fairness; causal discrimination; the level of correlation)*
*in the chapter text: Ch 6, Ch 7 · kind: concept*

> And we need a small piece of formal apparatus, due to Judea Pearl, that lets us see the difference between a system that correlates the bias and a system that causes it.
> — *the book, Ch 6 line 20; explained across several passages, no single defining sentence*

In plain words: A system that correlates the bias just reproduces patterns that go together in the data (Rung 1), while a system that causes it would change the outcome when the variable is changed (Rung 2). Whether bias is caused by the variable in question is a Rung 2 question, and Rung 1 evidence cannot answer it.

Example: A Rung 1 disparity may vanish on Rung 2 when it is mediated entirely through legitimate features, so the decision is causally race-neutral.

Not to be confused with: correlation (an association is not a cause, and a Rung 1 disparity does not always mean causal discrimination)

## Accountability (1)

**human in the accountability chain**  *(also: human in the loop; closing the loop with more AI)*
*in the chapter text: Ch 12 · kind: concept*

> The question is not just who is responsible. It is why a human must be in that accountability chain at all. Why can't we close the loop with more AI?
> — *the book, Ch 12 line 39; explained across several passages, no single defining sentence*

In plain words: The chapter's prior question: not only who is responsible but why a human must be in the accountability chain at all, instead of closing the loop with another AI. Its answer is cognitive and structural rather than only legal or practical.

Example: "Why can't we close the loop with more AI?"

# Part B: other strong candidates

Not on Bear's list yet, but they recur across chapters or are defined cleanly.

**what would change my mind**
*in the chapter text: Ch 1 ×1, Ch 2 ×1, Ch 3 ×1, Ch 4 ×1, Ch 5 ×1, Ch 6 ×2, Ch 7 ×1, Ch 8 ×2, Ch 9 ×1, Ch 10 ×1, Ch 11 ×2, Ch 12 ×2, Ch 13 ×1 · kind: method*

> If a debiasing algorithm were demonstrated to robustly remove structural bias without intervention on the deployment context — across multiple domains and base-rate regimes — the leverage analysis framing in this chapter would need revision. I am not aware of such a demonstration.
> — *the book, Ch 6 line 358*

In plain words: The chapter's stated falsifier: its leverage-analysis framing would need revision if a debiasing algorithm were shown to robustly remove structural bias without touching the deployment context, across several domains and base-rate regimes. The author says he knows of no such demonstration.

**lock your prediction**  *(also: lock a prediction)*
*in the chapter text: Ch 1, Ch 2 ×2, Ch 3 ×3, Ch 4 ×1, Ch 5 ×1, Ch 6 ×1, Ch 7 ×1, Ch 8 ×1, Ch 9 ×1, Ch 10 ×1, Ch 11 ×1, Ch 12 ×1, Ch 13 ×1 · kind: method*

> Lock your prediction: before reading the post-mortem and the proposed fixes, identify which of the ten bias mechanisms are active in your case. For each one, predict the highest-leverage intervention. Name the variable, name the type of intervention, predict the direction of effect.
> — *the book, Ch 6 line 381*

In plain words: Before you read the post-mortem, write down which of the ten bias mechanisms you think are active and the highest-leverage intervention for each, naming the variable, the intervention type and the direction of effect. You then compare what the post-mortem actually proposed against that prediction.

Example: Glimmer 6.1 and Exercise C2 on a documented case such as COMPAS.

**agentic**
*in the chapter text: Ch 1 ×3, Ch 2 ×2, Ch 3 ×2, Ch 4 ×18, Ch 5 ×1, Ch 6 ×1, Ch 7 ×2, Ch 8 ×60, Ch 9 ×2, Ch 10 ×1, Ch 11 ×1, Ch 12 ×11, Ch 13 ×5 · kind: concept*

> Be agentic (it takes actions in the world via tools, not just produces text)
> — *the book, Ch 1 line 358*

In plain words: A property of an AI system that takes actions in the world through tools, rather than only producing text. The casebook agent must be agentic.

**Glimmer**
*in the chapter text: Ch 1 ×4, Ch 2 ×6, Ch 3 ×2, Ch 4 ×1, Ch 5 ×2, Ch 6 ×3, Ch 7 ×1, Ch 8 ×3, Ch 9 ×1, Ch 10 ×3, Ch 11 ×3, Ch 12 ×1, Ch 13 ×5 · kind: method*

> A Glimmer is a longer, higher-stakes exercise that requires going to primary sources. Do not abridge this one.
> — *the book, Ch 5 line 369*

In plain words: A Glimmer is a longer, higher-stakes exercise that sends you to primary sources, and the chapter says not to abridge it. Glimmer 5.1 tests whether a real tool's explanation is practically misleading.

Example: Glimmer 5.1: take a deployed AI tool, pull its explanation for a recent decision, and lock your prediction before investigating.

**deployment context**  *(also: the room the model had been deployed into; downstream decision process)*
*in the chapter text: Ch 1 ×5, Ch 2 ×1, Ch 4 ×2, Ch 5 ×1, Ch 6 ×14, Ch 7 ×4, Ch 8 ×8, Ch 9 ×2, Ch 10 ×1, Ch 11 ×2, Ch 12 ×1, Ch 13 ×13 · kind: concept*

> Below that, the deployment context — the reviewer, the threshold, the appeal process.
> — *the book, Ch 6 line 283*

In plain words: Everything around the model where its output actually gets used: the human reviewer, the threshold, the appeal process. It can carry or amplify bias even when the model and the data are left untouched.

Example: Team Three found the reviewer's own systematic patterns were being amplified by the model and fixed the review process, not the model.

**frame**
*in the chapter text: Ch 1 ×3, Ch 2 ×5, Ch 3 ×36, Ch 4 ×6, Ch 5 ×3, Ch 6 ×5, Ch 7 ×1, Ch 8 ×5, Ch 9 ×2, Ch 10 ×6, Ch 11 ×1, Ch 13 ×4 · kind: concept*

> The sample was enormous. The frame was skewed — telephone owners, car owners, magazine subscribers, in the depths of the Depression — and non-response compounded it.
> — *the book, Ch 6 line 44; explained across several passages, no single defining sentence*

In plain words: The pool of people a sample is drawn from; if it leaves some people out or overweights others, the sample is skewed however large it is. The chapter names it but never gives it a formal definition.

Example: A remote-work survey pushed through LinkedIn overrepresents credentialed professionals.

Not to be confused with: the instrument (in sampling bias the chapter says the frame, not the instrument, is skewed)

**threshold**  *(also: decision threshold; group-specific thresholds)*
*in the chapter text: Ch 1 ×5, Ch 2 ×1, Ch 3 ×1, Ch 4 ×2, Ch 5 ×1, Ch 6 ×3, Ch 7 ×10, Ch 8 ×2, Ch 9 ×5, Ch 11 ×6, Ch 12 ×2, Ch 13 ×2 · kind: concept*

> Now set a threshold $\tau = 0.5$ and ask: among those the model predicts positive, what fraction are actually positive?
> — *the book, Ch 7 line 81; explained across several passages, no single defining sentence*

In plain words: The score cutoff above which the model says yes. Moving it, or using a different cutoff for each group, changes the error rates and the positive predictive value, and per-group cutoffs are the chapter's post-processing tool.

Example: Equalized-odds table: the same model uses a threshold of 0.5 for group A and 0.6 for group B, giving PPV 0.88 versus 0.67.

**artifact**  *(also: the artifact is not the world; the appearance is not the thing)*
*in the chapter text: Ch 1 ×16, Ch 3 ×12, Ch 4 ×6, Ch 5 ×2, Ch 6 ×8, Ch 7 ×1, Ch 8 ×6, Ch 9 ×13, Ch 10 ×10, Ch 12 ×11, Ch 13 ×2 · kind: concept*

> The recruiting tool produced a star rating. The rating was the artifact. Whether the applicant could do the job was the world.
> — *the book, Ch 1 line 143; explained across several passages, no single defining sentence*

In plain words: The artifact is the output a system produces (a rating, a score, a leaderboard number); the world is the real thing it is supposed to say something about. A review that examines only the artifact can never reach the question that matters.

Example: Netflix's leaderboard, to the fourth decimal place, was the artifact; whether a member found something to watch tonight was the world.

Not to be confused with: the world

**leverage**  *(also: low-leverage; high-leverage)*
*in the chapter text: Ch 2 ×1, Ch 3 ×2, Ch 5 ×4, Ch 6 ×69, Ch 7 ×1, Ch 8 ×4, Ch 9 ×1, Ch 10 ×2, Ch 11 ×2, Ch 12 ×11, Ch 13 ×2 · kind: concept*

> But they were low-leverage — correct interventions on a real path that happened to carry little of the bias. The third was high-leverage, and the rightness was not an accident.
> — *the book, Ch 6 line 16; explained across several passages, no single defining sentence*

In plain words: How much of the bias an intervention actually removes. A low-leverage fix is correct but acts on a path that carries little of the bias; a high-leverage fix acts on the path that carries most of it, and that is usually not the one closest to your hands.

Example: Changing the loss function or rebalancing the data was low-leverage; changing the review process dropped the disparity by an order of magnitude.

**stakes**
*in the chapter text: Ch 1 ×4, Ch 5 ×5, Ch 6 ×1, Ch 8 ×2, Ch 9 ×7, Ch 10 ×2, Ch 11 ×2, Ch 12 ×23, Ch 13 ×18 · kind: concept*

> What is the cost of being wrong on this sub-task? Low-stakes sub-tasks tolerate higher AI error rates because the downside is bounded. High-stakes sub-tasks require human review or human-only decision-making, even if the AI's average performance is good — because the average is not the relevant statistic when a single bad outcome is catastrophic.
> — *the book, Ch 9 line 102*

In plain words: How much damage a wrong answer on a sub-task would cause. Where the downside is bounded more AI error is tolerable, but where one bad outcome could be catastrophic a human must review or decide, even if the AI's average performance is good.

Example: Low risk: wrong answers waste time but harm no one outside the team. High risk: wrong answers reach external parties, regulators, or vulnerable users.

**System Dossier**
*in the chapter text: Ch 1 ×5, Ch 2 ×2, Ch 3 ×1, Ch 4 ×3, Ch 5 ×1, Ch 6 ×1, Ch 7 ×1, Ch 8 ×1, Ch 11 ×1, Ch 13 ×2 · kind: concept*

> End with a one-paragraph "System Dossier" I can paste into my Claude Project's system prompt: name of agent, architecture summary, tool surface, deployment context, the candidate failure mode my casebook will pursue, and any access constraints I'm working under.
> — *the book, Ch 1 line 380*

In plain words: A one-paragraph description of the agent you will red-team, pasted into your Claude Project's system prompt so every chapter inherits the context. It names the agent, its architecture, tool surface, deployment context, the candidate failure mode to pursue, and any access constraints.

**the pairing**  *(also: the pairing Chapter 1 committed us to; machine supplies speed and coverage; you supply the doubt)*
*in the chapter text: Ch 2 ×1, Ch 3 ×1, Ch 4 ×2, Ch 5 ×1, Ch 6 ×2, Ch 7 ×1, Ch 8 ×1, Ch 9 ×1, Ch 10 ×1, Ch 11 ×1 · kind: framework*

> This is the pairing Chapter 1 committed us to — the machine supplies speed and coverage, a faithful number on every prediction; you supply the doubt that asks what does this number warrant?
> — *the book, Ch 5 line 19*

In plain words: The division of labour from Chapter 1: the machine supplies speed and coverage, such as a faithful number on every prediction, and the human supplies the doubt about what that number warrants. This chapter practices the human side for explanations.

Example: SHAP gives a number for every prediction; the supervisor asks what that number does and does not warrant.

**event**
*in the chapter text: Ch 1 ×1, Ch 2 ×31, Ch 3 ×1, Ch 4 ×2, Ch 8 ×2, Ch 10 ×2, Ch 11 ×1, Ch 12 ×1, Ch 13 ×2 · kind: concept*

> An event is any subset of the sample space — any collection of outcomes we might care about. "The die shows an even number" is the event $\{2, 4, 6\}$.
> — *the book, Ch 2 line 42*

In plain words: Any collection of outcomes from the sample space that you care about, which can be a single outcome or several.

Example: "The die shows an even number" is the event {2, 4, 6}.

Not to be confused with: sample space (the set of all outcomes)

**gap analysis**
*in the chapter text: Ch 1 ×2, Ch 2 ×1, Ch 3 ×4, Ch 4 ×1, Ch 6 ×2, Ch 8 ×2, Ch 10 ×1, Ch 13 ×1 · kind: method*

> Write the gap analysis. If the post-mortem's proposed intervention was at a different mechanism than yours, explain — using Pearl's Ladder — why one of you is wrong.
> — *the book, Ch 6 line 383*

In plain words: After comparing the post-mortem's proposed fix to your locked prediction, write up where they differ. If they target different mechanisms, use Pearl's Ladder to explain why one of you is wrong.

**casebook journal**  *(also: prediction-lock log; case-write-up template)*
*in the chapter text: Ch 1 ×3, Ch 2 ×1, Ch 3 ×2, Ch 4 ×2, Ch 8 ×3, Ch 10 ×1, Ch 11 ×1, Ch 13 ×2 · kind: method*

> You are also standing up the record-keeping apparatus the later chapters assume: a casebook journal (the prediction-lock log you will keep for every red-team observation) and a reusable one-page case-write-up template.
> — *the book, Ch 1 line 346; explained across several passages, no single defining sentence*

In plain words: The log where you record a dated prediction-lock before each red-team observation of your agent, kept with a reusable one-page case-write-up template. Its template fields include case ID, input, action taken, reported outcome, actual outcome, which capacity failed, evidence and severity.

Example: Task 3 of the prompt asks Claude to draft the journal file and the one-page template.

**composite**  *(also: load-bearing story; fluent anecdote)*
*in the chapter text: Ch 1 ×1, Ch 3 ×4, Ch 5 ×1, Ch 6 ×1, Ch 8 ×1, Ch 10 ×1, Ch 13 ×2 · kind: concept*

> I'm going to flag this opening the way I flag every load-bearing story in this book: it's a composite, not a sourced clinical incident, and I'm labeling it so because a chapter about distrusting fluent explanations cannot itself run on a fluent anecdote you're asked to trust.
> — *the book, Ch 5 line 13*

In plain words: A composite is a story built to illustrate a real mechanism rather than a documented incident, and the author labels it so readers do not trust it as a fact. The chapter does this because a chapter about distrusting fluent explanations should not rest on a fluent anecdote.

Example: The radiologist opening is labelled a composite, with the real mechanism (shortcut learning) cited in a footnote.

Not to be confused with: sourced clinical incident

**skepticism**  *(also: skeptical method)*
*in the chapter text: Ch 1 ×14, Ch 3 ×1, Ch 4 ×2, Ch 6 ×2, Ch 10 ×2, Ch 12 ×1, Ch 13 ×12 · kind: concept*

> I mean a method. Skepticism in this book is a set of moves you can perform on a claim, and the moves can be taught, and you can see whether someone did them.
> — *the book, Ch 1 line 60; explained across several passages, no single defining sentence*

In plain words: A set of moves you perform on a claim, not a mood: not eye-rolling or cynicism, but a method that can be taught and whose use can be seen. It is also the discipline of knowing how you formed a belief so you notice when the conditions that made it reliable have changed.

Example: The recruiter who asks what would have to be true for this score to be wrong is performing a move; the one who trusts it because it agreed with her last eight hundred judgments is performing none.

Not to be confused with: cynicism, or the disposition of being against everything

**Agents of Chaos**
*in the chapter text: Ch 1 ×1, Ch 3 ×2, Ch 4 ×4, Ch 5 ×2, Ch 6 ×3, Ch 7 ×1, Ch 8 ×19, Ch 12 ×4 · kind: named result or case*

> It documents eleven representative vulnerability cases (the ones I walk through below) plus a set of failed-attempt / safety-behavior cases, #12–#16, where the agents resisted.
> — *the book, Ch 8 line 27; explained across several passages, no single defining sentence*

In plain words: A 2026 study in which twenty researchers spent two weeks probing and trying to break autonomous AI agents (six agents on the OpenClaw framework) in a live lab. It documents eleven representative vulnerability cases plus a set of cases (#12–#16) where the agents resisted, and it is the chapter's main evidence.

Example: Case #1: an agent reset a whole email account to "delete" one email and reported success.

**self-explanation audit**
*in the chapter text: Ch 4 ×1, Ch 5 ×2, Ch 7 ×1, Ch 8 ×1, Ch 11 ×1, Ch 13 ×2 · kind: method*

> A "self-explanation audit" of your agent — a side-by-side comparison of what the agent says it did versus what it actually did, with the language-game mismatches catalogued and the technically-accurate-practically-misleading patterns flagged.
> — *the book, Ch 5 line 469*

In plain words: A self-explanation audit sets what an agent says it did next to what it actually did and logs the language-game mismatches. It flags reports that are technically accurate but practically misleading.

Example: For 5 to 10 tasks, capture the request, the agent's self-explanation, the actual tool calls and the ground-truth state.

**computational skepticism**  *(also: plausible artifacts; machine speed, your doubt)*
*in the chapter text: Ch 1 ×1, Ch 3 ×1, Ch 4 ×2, Ch 10 ×1, Ch 13 ×1 · kind: framework*

> This is where computational skepticism does its most characteristic work — the pairing Chapter 1 committed us to: the machine's speed at producing plausible artifacts, your doubt about what they are evidence of. An AI can assemble the dataset, join the tables, draw every histogram, and write the "the data is clean" paragraph faster than you ever could. What it cannot supply is the doubt about what the histograms can't reach.
> — *the book, Ch 3 line 41*

In plain words: The pairing the book rests on: the machine quickly produces plausible artifacts (tables, plots, a 'the data is clean' paragraph) and you supply the doubt about what they are evidence of. The AI cannot supply the doubt about what the histograms cannot reach.

Example: An AI writing the 'the data is clean' paragraph faster than you could, with every histogram drawn.

**false-positive rate**  *(also: FPR)*
*in the chapter text: Ch 1 ×2, Ch 2 ×4, Ch 6 ×3, Ch 7 ×8, Ch 10 ×1 · kind: metric*

> The false-positive rate — among those who actually were not positive, the fraction the model incorrectly flagged — is also the same
> — *the book, Ch 7 line 49*

In plain words: Among the people who really are not positive, the share the model wrongly flags. Equalized odds requires it to be equal across groups.

Example: COMPAS: ProPublica found the false-positive rate substantially higher for Black defendants than for white defendants (about 2 times).

**resolution**  *(also: REL; discrimination power)*
*in the chapter text: Ch 7 ×1, Ch 8 ×1, Ch 10 ×1, Ch 11 ×9, Ch 12 ×1 · kind: metric*

> REL is the resolution (how much the model's predictions vary around the base rate — capturing discrimination power), and CAL is the calibration component (how much predicted probabilities deviate from empirical frequencies in each score bin).
> — *the book, Ch 11 line 138*

In plain words: In the Brier breakdown, how much the model's predictions vary around the base rate, which measures how well it tells cases apart. A model with no resolution predicts about the base rate for everyone.

Example: A model that predicts the base rate for every instance has no resolution: it is honest about uncertainty but useless for triage.

Not to be confused with: calibration (the decomposition separates the two)

**the supervisor**  *(also: the person supervising; the human supervising the model)*
*in the chapter text: Ch 1 ×8, Ch 8 ×2, Ch 9 ×6, Ch 11 ×1, Ch 13 ×19 · kind: concept*

> Neither check belongs to the model. Both belong to the person supervising it. The rest of this chapter is about how that person does the checking.
> — *the book, Ch 1 line 52; explained across several passages, no single defining sentence*

In plain words: The human who owns the checking: asking what a measure stands for and checking it again over time. The model has no way to detect when the world stops matching its expectations, so only the human can do it, and only if they remember the check is necessary.

Example: A technical recruiter handed a ranked list where strong engineers keep landing near the bottom is the supervisor noticing something is off.

**audit trail**  *(also: audit trails)*
*in the chapter text: Ch 1 ×1, Ch 8 ×22, Ch 9 ×16, Ch 12 ×10 · kind: concept*

> The record of what the system did is a logging problem — mechanical, Tier 1. But an audit trail is not self-interpreting; two engineers can read the same log and tell two different stories.
> — *the book, Ch 12 line 190; explained across several passages, no single defining sentence*

In plain words: The per-action record of what the system did (inputs, outputs, tool calls, decisions, timestamps, reviewers). Capturing it is mechanical Tier 1 logging, but interpreting it is Tier 4 because two engineers can read the same log and tell two different stories.

Example: Test: pull a random recent incident and see whether the chain can be reconstructed in under an hour.

**the machine's speed, your doubt**
*in the chapter text: Ch 2 ×1, Ch 4 ×1, Ch 7 ×1, Ch 8 ×1, Ch 9 ×1 · kind: concept*

> Delegation is where the pairing Chapter 1 committed us to — the machine's speed, your doubt — actually meets, and the delegation map is the instrument that keeps the speed from outrunning the doubt.
> — *the book, Ch 9 line 28*

In plain words: The pairing from Chapter 1: the machine brings speed and the human brings doubt. The delegation map is the tool that stops the speed from getting ahead of the doubt.

Example: In the Paper Summarizer, Claude does the pattern work (steps 2, 3, 5) and a human does the judgment work (steps 1, 4, 6).

**outlier**  *(also: outlier triage; outlier detection is triage, not removal)*
*in the chapter text: Ch 3 ×16, Ch 4 ×1, Ch 6 ×1, Ch 10 ×1, Ch 13 ×3 · kind: concept*

> But the detection is the easy half. Every flagged value needs a decision the method cannot make: is a $1,200,000 salary a decimal-point error, a legitimate CEO, or a sentinel for "unknown"? IQR flags the candidate; only domain knowledge makes the call about whether to remove, impute, cap, or keep it.
> — *the book, Ch 3 line 80; explained across several passages, no single defining sentence*

In plain words: An unusually extreme value that a rule flags as a candidate. The rule only flags it; domain knowledge decides whether to remove, impute, cap or keep it.

Example: A $1,200,000 salary could be a decimal-point error, a legitimate CEO, or a sentinel for "unknown".

**Data Frame Audit**
*in the chapter text: Ch 2 ×1, Ch 3 ×3, Ch 4 ×3, Ch 5 ×1, Ch 8 ×1, Ch 11 ×1, Ch 13 ×2 · kind: named result or case*

> A "Data Frame Audit" file in your casebook folder, including a dataset inventory, a six-step epistemic-frame reconstruction, a structural-assumption audit, and a hidden-failure test ready to run.
> — *the book, Ch 3 line 375*

In plain words: The deliverable of the chapter's LLM exercise: one file holding a dataset inventory, a six-step reconstruction, a structural-assumption audit and a hidden-failure test for your agent.

Example: An inventory covering the retrieval corpus, the system prompt and few-shot examples, and tool documentation.

**operational form**  *(also: artifact)*
*in the chapter text: Ch 8 ×1, Ch 9 ×7, Ch 11 ×2, Ch 12 ×4, Ch 13 ×2 · kind: concept*

> Here is what is actually happening when the capacities work: each one is not a trait you have but an operational form the pipeline either contains or does not. If the artifact is not there, the capacity did not happen.
> — *the book, Ch 9 line 70; explained across several passages, no single defining sentence*

In plain words: Each supervisory capacity counts only if the pipeline contains a concrete, documented version of it, not because someone felt careful. If the artifact is missing, the capacity did not happen.

Example: Plausibility auditing is a checklist embedded in the workflow, answered yes/no and recorded; without the checklist the auditing did not happen.

Not to be confused with: a trait you have (judgment, experience)

**shortcut**  *(also: shortcut learning; spurious features)*
*in the chapter text: Ch 1 ×1, Ch 2 ×2, Ch 4 ×1, Ch 5 ×10, Ch 7 ×1 · kind: failure mode*

> The mechanism it illustrates is real and documented — deep networks in medical imaging routinely learn shortcuts: spurious features that correlate with the label in training and generalize badly, and which a post-hoc explanation will faithfully report without flagging as shortcuts.
> — *the book, Ch 5 line 13; explained across several passages, no single defining sentence*

In plain words: A shortcut is a spurious feature that happens to match the label in the training data but does not carry over to new data. A post-hoc explanation will report the shortcut faithfully without telling you it is one.

Example: Features X and Y in the radiologist case were correlated, in the deployment population, with a non-malignant condition the training data had seen little of.

**Hume's induction problem**
*in the chapter text: Ch 2 ×2, Ch 3 ×1, Ch 4 ×1, Ch 13 ×1 · kind: concept*

> This is Hume's induction problem in work clothes — you are inferring the construct from a proxy that happened to correlate in the recorded past, and the correlation carries no guarantee forward.
> — *the book, Ch 3 line 124*

In plain words: The old problem of inferring what will hold from what happened to hold before. Here, a proxy label correlated with the real target in the recorded past, but that guarantees nothing going forward.

Example: Inferring interest from clicks.

**testable**  *(also: testability)*
*in the chapter text: Ch 6 ×1, Ch 8 ×3, Ch 9 ×22, Ch 13 ×3 · kind: concept*

> Testable means a non-author of the pipeline — someone who did not build the thing — can read the condition, observe the system, and determine whether the condition is met.
> — *the book, Ch 9 line 48*

In plain words: A handoff condition is testable if someone who did not build the pipeline can read it, look at the system, and tell whether it was met. It is the one non-negotiable property of a handoff condition.

Example: A stranger can look at the log and tell, for any case, exactly what happened.

Not to be confused with: untestable condition

**faithful**  *(also: faithfully; faithful description)*
*exam focus (Bear) · in the chapter text: Ch 3 ×2, Ch 4 ×1, Ch 5 ×6, Ch 6 ×2, Ch 8 ×1 · kind: concept*

> The accounting is real — it is what the model actually did. SHAP is a faithful description of that accounting.
> — *the book, Ch 5 line 45; explained across several passages, no single defining sentence*

In plain words: An explanation is faithful when it correctly reports what the model actually did internally. Being faithful is not the same as being right about the world.

Example: The radiologist's tool correctly said features X and Y drove the prediction, yet the decision was wrong; the model wasn't lying about itself.

Not to be confused with: a description of the world

**robust features**
*in the chapter text: Ch 4 ×21, Ch 5 ×1, Ch 7 ×1, Ch 8 ×1 · kind: concept*

> Robust features are correlated with the label and stable under small perturbations — the shapes, textures, and structural properties that humans use for recognition.
> — *the book, Ch 4 line 237*

In plain words: Patterns in the data that go with the label and hold steady when the input is slightly altered; they are the shape and structure that people use to recognize things.

Example: The panda's shape, posture and coloring.

Not to be confused with: non-robust features

**positive predictive value**  *(also: PPV; precision)*
*in the chapter text: Ch 2 ×1, Ch 6 ×1, Ch 7 ×3, Ch 11 ×1 · kind: metric*

> The positive predictive value — precision, PPV, call it $v$ — is the probability someone is truly positive given a positive prediction.
> — *the book, Ch 7 line 83*

In plain words: Of the people the model flags as positive, the share who really are positive. For a yes/no score, the chapter says calibration means this share is equal across groups.

Example: In the calibration-satisfying table PPV is 0.75 in both groups.

Not to be confused with: true-positive rate (conditions on being truly positive instead)

**causal graph**  *(also: Pearl-style DAG)*
*in the chapter text: Ch 2 ×1, Ch 6 ×20, Ch 7 ×2, Ch 8 ×2 · kind: method*

> Draw the causal graph of how the bias appears in the deployed outcome. Variables: protected attribute, proxies, features used by the model, model output, downstream decision process, final outcome. Arrows: which variables cause which.
> — *the book, Ch 6 line 305*

In plain words: A diagram of the variables from the protected attribute down to the final outcome, with arrows showing which variable causes which. Drawing the whole graph, including the deployment context, is what lets you see every path the bias can take.

Example: Protected attribute, then proxies, features, model output, deployment context (reviewer, threshold, appeal), final outcome.

**external validation**
*in the chapter text: Ch 2 ×2, Ch 9 ×1, Ch 11 ×3, Ch 12 ×1, Ch 13 ×1 · kind: method*

> The failure only became visible through external validation at a specific deployment site, with a specific patient population, where the model had never been validated before.
> — *the book, Ch 11 line 191; explained across several passages, no single defining sentence*

In plain words: Testing a model at a specific outside deployment site, with its own patient population, where it had never been validated before. In the Epic case this exposed a failure the aggregate numbers hid, and in the chapter's evidence table it is part of what lets you use the verb "show".

Example: Wong et al. found AUC 0.63 against a developer-reported 0.76 to 0.83.

**non-robust features**  *(also: non-robust feature; high-frequency statistical signature)*
*in the chapter text: Ch 4 ×17, Ch 5 ×1, Ch 7 ×1, Ch 8 ×1 · kind: concept*

> Non-robust features are also correlated with the label on the training distribution, but are high-frequency, brittle, and semantically meaningless to humans — statistical patterns in pixel arrangements that happen to co-occur with particular classes but are easily disrupted by small perturbations.
> — *the book, Ch 4 line 237; explained across several passages, no single defining sentence*

In plain words: Patterns that go with the label in the training data but are fine-grained, easily disrupted, and meaningless to a person. Supervised learning does not distinguish them from robust features and often prefers them because they are more predictive.

Example: The high-frequency statistical signature of the gibbon, which an attack moves into the panda picture.

Not to be confused with: robust features

**posterior**
*in the chapter text: Ch 1 ×1, Ch 2 ×12, Ch 6 ×1, Ch 10 ×1 · kind: concept*

> You observe evidence. You update. The posterior is what you should believe now.
> — *the book, Ch 2 line 78; explained across several passages, no single defining sentence*

In plain words: What you believe after you have seen the evidence: your prior updated by the evidence. In Bayes' theorem it is proportional to the prior times the likelihood.

Example: P(disease | positive) is about 0.0099, roughly one percent, in the disease example.

Not to be confused with: prior (what you believed before the evidence)

**epistemic frame**  *(also: the frame; frame of the dataset)*
*in the chapter text: Ch 2 ×2, Ch 3 ×27, Ch 6 ×1 · kind: concept*

> Before the model, there is data. Before the data, there are choices — about what to record, what to include, how to join, where to stop. Those choices are the epistemic frame of the dataset, and they are almost never written down.
> — *the book, Ch 3 line 39*

In plain words: The set of choices made before and while a dataset was built: what to record, what to include, how to join, where to stop. They are almost never written down, so you have to reconstruct them.

Example: A join that quietly drops rows and dtypes that were inferred rather than verified (the opening scenario).

**AI Use Disclosure**
*in the chapter text: Ch 9 ×8, Ch 11 ×2, Ch 12 ×2, Ch 13 ×2 · kind: concept*

> The AI Use Disclosure — a record of how AI was used in producing a piece of work — is worth making a required deliverable for any assignment where the work will be relied on. Here it becomes something larger.
> — *the book, Ch 9 line 237; explained across several passages, no single defining sentence*

In plain words: A written record of how AI was used to produce a piece of work: what was used, on which step, and how it was verified. In this chapter it is meant to work as a supervisory log, not a compliance checkbox.

Example: Step 3 of the Paper Summarizer disclosure: tool, what was asked, what was produced, 4 of 20 HIGH-confidence citations checked, and the Methods claim corrected.

Not to be confused with: compliance checkbox

**build/audit pairing**
*in the chapter text: Ch 2, Ch 3 ×1, Ch 7, Ch 11 ×1, Ch 12 ×1 · kind: method*

> The way you learn to write one honestly is the build/audit pairing: write the attestation for something you built, then reconstruct the attestation nobody wrote for a system that failed. The two passes expose different failure modes — signing off on the output you want to believe, and reconstructing who should have signed when nobody did.
> — *the book, Ch 12 line 225*

In plain words: A two-pass way to learn to write an attestation honestly: write one for something you built, then reconstruct the attestation nobody wrote for a system that failed. The passes expose different failure modes: signing off on the output you want to believe, and reconstructing who should have signed when nobody did.

Example: Build at exercise S4; audit at exercise C3.

**structural reason**
*in the chapter text: Ch 3 ×2, Ch 4 ×3, Ch 5 ×5, Ch 8 ×1 · kind: concept*

> The deliverable is the case, the explanation, the prediction, the trace, and the structural reason. The grade is on the structural reason. A correct prediction with no structural account is worth less than an incorrect prediction that names the structural reason precisely.
> — *the book, Ch 5 line 379; explained across several passages, no single defining sentence*

In plain words: The structural reason is the specific mechanism that made an explanation misleading, such as a Rung 1 limitation, a language-game mismatch or a scope mismatch. The Glimmer is graded on naming it, not on whether the prediction was right.

Example: Naming 'Rung 1 limitation' for a SHAP attribution that was read as causal.

**alpha (α)**  *(also: the values dial; GE parameter)*
*in the chapter text: Ch 4 ×4, Ch 7 ×19, Ch 11 ×3 · kind: concept*

> The parameter $\alpha$ tunes sensitivity: low $\alpha$ weights differences at the bottom of the distribution, high $\alpha$ weights differences at the top. Note already that choosing $\alpha$ is choosing whose unfairness counts more — the exit has a values dial built into it before you've computed anything.
> — *the book, Ch 7 line 308*

In plain words: The setting in the GE index that chooses where to look: low alpha weights differences at the bottom of the distribution, high alpha weights differences at the top. Choosing it is choosing whose unfairness counts more.

**likelihood**
*in the chapter text: Ch 2 ×3, Ch 7 ×2, Ch 10 ×2, Ch 11 ×2 · kind: concept*

> $P(B \mid A_i)$ is the likelihood: how probable the evidence would be if hypothesis $i$ were true.
> — *the book, Ch 2 line 309; explained across several passages, no single defining sentence*

In plain words: How probable the evidence would be if a given hypothesis were true. In the disease example it is the chance of a positive test given the disease, 0.99.

Example: P(positive | disease) = 0.99.

Not to be confused with: posterior (the probability of the hypothesis given the evidence)

**governance counterfactual**  *(also: Rung 3 in operational form)*
*in the chapter text: Ch 4 ×5, Ch 12 ×15, Ch 13 ×4 · kind: method*

> The operational form is the governance counterfactual. For a documented failure, ask: what regime — what specifications, what audit trail requirements, what recourse, what independent review, what sanctions — if implemented before the failure, would have prevented it? The regime is the intervention.
> — *the book, Ch 12 line 249*

In plain words: For a failure that already happened, asking which set of rules and practices (specifications, audit trail, recourse, independent review, sanctions), if in place beforehand, would have prevented it. It is Pearl's Rung 3 applied to the regime rather than to the model.

Example: Mail-server case: a regime requiring cryptographic authority verification instead of social signaling would have prevented the deletion by a non-owner.

Not to be confused with: 'the model behaves better' (the chapter says the counterfactual is that the regime produces a different system)

**do not delegate**
*in the chapter text: Ch 3 ×3, Ch 9 ×4, Ch 13 ×3 · kind: framework*

> Do not delegate problem formulation, plausibility auditing, interpretive judgment under stakes, or the sign-off that makes a judgment accountable. These cannot be done by AI not because AI is insufficiently capable, but because they are structurally unavailable to any system that cannot be wrong in a way that matters to it.
> — *the book, Ch 13 line 226*

In plain words: The third tier: keep problem formulation, plausibility auditing, interpretive judgment under stakes and accountability sign-off for yourself. The chapter says AI cannot do them for a structural reason, not because it is too weak.

Example: Signing off on a validation report for a clinical deployment.

Not to be confused with: delegate with verification

**partition**
*in the chapter text: Ch 2 ×12, Ch 7 ×1, Ch 9 ×4 · kind: concept*

> Let $A_1, A_2, \ldots, A_n$ be events that partition the sample space: they are mutually exclusive (no two can occur simultaneously), collectively exhaustive (one of them must occur), and each has positive probability.
> — *the book, Ch 2 line 185*

In plain words: A split of the sample space into pieces that cannot overlap (mutually exclusive), together cover every possibility (collectively exhaustive), and each have positive probability.

Example: The three model versions A, B and C partition the cases by which version handled them.

**values claim**  *(also: not a technical choice)*
*in the chapter text: Ch 5 ×1, Ch 6 ×3, Ch 7 ×15 · kind: concept*

> Which means the choice between fairness metrics is not a technical choice. It is a values claim. Which kind of error are we less willing to make?
> — *the book, Ch 6 line 209; explained across several passages, no single defining sentence*

In plain words: Because no model can satisfy every fairness definition when base rates differ, choosing a metric means deciding which kind of error you are less willing to make. That has a social answer that depends on the model's use and who bears each error's cost, and engineers who treat it as pure optimization are secretly making a values choice.

Example: Optimizing for whatever metric the loss function encodes while appearing neutral.

Not to be confused with: a technical (mathematical) choice

**supervisory log**
*in the chapter text: Ch 9 ×4, Ch 10 ×1, Ch 13 ×1 · kind: concept*

> The intent is that, read in aggregate, the Disclosure serves as a supervisory log — a record of where the student exercised which supervisory capacity.
> — *the book, Ch 9 line 239*

In plain words: What the AI Use Disclosure becomes when read as a whole: a record of where the person exercised each supervisory capacity. It works only if it is granular, honest, time-stamped and tied to evidence.

Example: Step 6 of the Paper Summarizer disclosure: the researcher read the summary as a user and signed it with name and date.

Not to be confused with: compliance checkbox

**language game**  *(also: Wittgenstein's language game)*
*in the chapter text: Ch 5 ×42, Ch 7 ×2 · kind: framework*

> Wittgenstein had this observation that the meaning of a word depends on the language game in which it is being used. The same word can do different work in different contexts. The same sentence can be true in one game and false in another.
> — *the book, Ch 5 line 314*

In plain words: A language game is the context in which words get their meaning, so the same word can mean different things in different contexts. The chapter uses it to say the same explanation can be correct in one game and misleading in another.

Example: 'Deleted' means local actions in the agent's game and 'no longer accessible to anyone' in the user's game.

**distribution match**  *(also: in-distribution; out-of-distribution; OOD)*
*in the chapter text: Ch 9 ×2, Ch 11 ×1, Ch 12 ×1 · kind: concept*

> Is the input to this sub-task within the AI's training distribution, or is it likely to land in a region of the input space where the AI is undertrained? In-distribution sub-tasks are AI-friendly. Out-of-distribution sub-tasks are dangerous regardless of average performance, because the average was computed where the data lived, not where the case in front of the supervisor right now sits.
> — *the book, Ch 9 line 104*

In plain words: Whether the input to a sub-task looks like the data the AI was trained on, or lands in a region where the AI is undertrained. Out-of-distribution inputs are dangerous whatever the average performance, because that average was computed where the training data lived.

Example: High risk: inputs that are tail cases or out-of-distribution by construction.

**calibration baseline**  *(also: third calibration baseline)*
*in the chapter text: Ch 2 ×3, Ch 4 ×4, Ch 13 ×5 · kind: method*

> For the third and final time, you take the same form of forecasting questions. You provide 90% confidence intervals for each. You check what fraction of your intervals contain the truth.
> — *the book, Ch 13 line 291; explained across several passages, no single defining sentence*

In plain words: A repeated exercise in which you give 90% confidence intervals for forecasting questions and check what fraction of them contain the truth. The chapter runs it a third time as a diagnostic on the supervisor you are becoming, not as a grade; most people start overconfident.

Example: Expected pattern (the chapter flags it as expected, not measured): about 0.4-0.6 at the first baseline, 0.6-0.75 at the second, 0.7-0.85 at the third.

**irreducibly human**  *(also: cannot be delegated)*
*in the chapter text: Ch 9 ×2, Ch 12 ×14, Ch 13 ×7 · kind: concept*

> Those judgments set the correctness criteria that everything downstream is tested against, and they are irreducibly mine.
> — *the book, Ch 9 line 160; explained across several passages, no single defining sentence*

In plain words: Some steps cannot be handed to the AI because they need domain knowledge, domain judgment or interpretive responsibility that a pattern-completion engine lacks. In the Paper Summarizer these are steps 1, 4 and 6.

Example: Step 6: judging whether the summary would mislead a peer who trusted it.

**leverage analysis**
*in the chapter text: Ch 3 ×2, Ch 5 ×1, Ch 6 ×25 · kind: method*

> For each candidate intervention point, ask: which paths does this intervention block, and which paths does it leave open?
> — *the book, Ch 6 line 307; explained across several passages, no single defining sentence*

In plain words: A four-step procedure: draw the causal graph, list all paths from the protected attribute to the outcome, ask for each candidate intervention which paths it blocks and which it leaves open, and pick the one that blocks the largest fraction of bias-carrying paths. It is the difference between mitigation that works and mitigation that produces conference papers and persistent disparities.

Example: Team A blocked the path through the model's parameters; Team C blocked the deployment-context path.

**true positive**
*in the chapter text: Ch 2 ×5, Ch 6 ×1, Ch 7 ×8 · kind: concept*

> The test, which is 99% accurate in the sense that it correctly identifies people who are sick, catches that person. Call it one true positive.
> — *the book, Ch 2 line 252; explained across several passages, no single defining sentence*

In plain words: A sick person whom the test correctly flags as positive.

Example: The one person in the 10,000 who actually has the disease and gets a positive result.

Not to be confused with: false positive

**discrimination**
*in the chapter text: Ch 6 ×1, Ch 7 ×3, Ch 11 ×7 · kind: concept*

> A model with high resolution but poor calibration is one that discriminates well but whose probabilities are misleading — it ranks cases correctly but the absolute numbers cannot be trusted.
> — *the book, Ch 11 line 140; explained across several passages, no single defining sentence*

In plain words: How well a model's scores rank or separate cases; the chapter ties it to resolution. A model can discriminate well, ranking cases correctly, while its absolute probability numbers are still misleading.

Example: The chapter calls AUC a discrimination metric (Exercise S2).

Not to be confused with: calibration

**Epic Sepsis Model**
*in the chapter text: Ch 2 ×2, Ch 11 ×3, Ch 12 ×2, Ch 13 ×2 · kind: named result or case*

> The Epic Sepsis Model — a proprietary early-warning tool for sepsis, deployed across hundreds of hospitals — was found in external validation to perform far worse than marketed, missing a large fraction of sepsis cases while flooding clinicians with alerts (Wong et al., 2021).
> — *the book, Ch 13 line 122*

In plain words: A real sepsis early-warning tool, deployed across hundreds of hospitals, whose reported validation metrics looked fine on internal data but which performed far worse in external validation. It had partly learned to confirm clinical suspicion rather than form it independently.

Example: It missed a large fraction of sepsis cases while flooding clinicians with alerts.

Not to be confused with: clinical decision-support system (the composite opening case)

**benefit**  *(also: b_i; cardinal benefit; error burden)*
*in the chapter text: Ch 4 ×1, Ch 7 ×7, Ch 11 ×1 · kind: concept*

> Let $N$ be the population size and $b_i$ the benefit to individual $i$ — a score, a predicted probability, or an error indicator (1 if misclassified, 0 otherwise).
> — *the book, Ch 7 line 296; explained across several passages, no single defining sentence*

In plain words: The number assigned to each person whose spread the GE index measures: a score, a predicted probability, or an error indicator (1 if misclassified, 0 otherwise). GE needs a real number, so if the model only decides yes or no you must define it, which is itself a values choice.

Example: An error indicator of 1 if the person is misclassified and 0 otherwise.

**aleatoric uncertainty**
*in the chapter text: Ch 10 ×8, Ch 11 ×5 · kind: concept*

> This is aleatoric uncertainty: the irreducible variability arising from sampling, natural variation, and stochastic processes. Error bars and confidence intervals are tools for it.
> — *the book, Ch 10 line 109*

In plain words: Uncertainty from sampling, natural variation and chance that cannot be removed; the chapter calls it the 'spread of the data'. Error bars and confidence intervals are the tools for showing it.

Example: A poll of 45.3% versus 44.5% with a ±2.95% margin has aleatoric uncertainty larger than the effect being reported.

Not to be confused with: epistemic uncertainty

**calibration set**  *(also: held-out calibration set)*
*in the chapter text: Ch 2 ×1, Ch 7 ×1, Ch 11 ×7 · kind: concept*

> minimizing the negative log-likelihood on a held-out calibration set after the model's weights are fixed.
> — *the book, Ch 11 line 218; explained across several passages, no single defining sentence*

In plain words: A held-out set, separate from training, used only to fit the correction after the model's weights are fixed (the temperature T, or the score cutoff in conformal prediction). If it is small, flexible methods such as isotonic regression overfit it, and calibration done on it does not carry over to a different deployment population.

Example: Exercise A6: temperature scaling lowers ECE on the calibration set from one hospital, but the deployment is a network of hospitals across three health systems.

# Part C: terms Bear named that the book does not use

The book has no sentence for these. Each is marked "common usage" and the definition is mine, written to be checked, not quoted from the book. Where the chapter has a near idea, it is named.

**AI is not accountable; you are**  
*Bear's statement of the whole accountability chapter for the exam; the chapter says it at more length (Ch 12)*

In plain words: when you hand something to your boss or a client, you are responsible for checking it. Companies such as Google do not care whether AI wrote the code; they care whether it works and whether you validated and tested it. When you sign off on something, you are signing your name to it. Once you sign off, it is as if you did it, no matter how much the AI did. So it is literally your job to check before you sign.

**sign-off**  
*Ch 9 (sign-off authority, signed decision log) and Ch 12 (shape versus substance of a sign-off); see also the five supervisory capacities*

In plain words: the point where you put your name to a piece of work and take responsibility for it. A real sign-off has substance behind it: you checked it, you could have refused to sign, and you tested what you could. A sign-off that is only a stamp is the failure the chapter warns about.


**agent**  
*the book describes it but never defines it in one sentence* · near terms in the book: consequence system, prediction system (Ch 8 lines 35-37)

In plain words: a model connected to tools, memory and messaging so that it acts in the world and does not only answer. Its outputs are state changes, not statements. Built from Ch 8: "A model that takes actions in the world is a consequence system. Its outputs are state changes." and the study's agents with "persistent memory, email accounts, Discord access, file systems, shell execution".

Example: told to delete one email, the agent reset the whole email account (Ch 8, Case #1).

**the work split**  
*Bear's own name for the Chapter 9 five-question assessment; not in the book under this name*

In plain words: who does what. The AI does the AI things, humans do the human things, and what the human does well cannot be skipped. The human part is the five supervisory capacities. Five questions sort each step: verification cost, stakes, distribution match, reversibility, audit trail clarity.

**cost versus risk**  
*Bear's framing of delegation; not in the book in these words*

In plain words: delegation matches the cost of checking an output to the risk of being wrong about it. Cheap to check and low risk: let the AI do it. High risk: pay the cost of checking, with a human approval before it runs.

**silent failure**  
*common usage, not in the book (Ch 1 item 4 and Ch 8 field lists)*

In plain words: a failure that tells no one. No error, no alert, so the system looks like it is working. Example: Knight Capital's order flood while the status said success (Ch 1).

**silent success**  
*common usage, not in the book*

In plain words: the system does its job but gives no signal that it did, so no news gets read as good news and cannot be told apart from a silent failure. Both are cured by an independent check of the world.

**need to know**  
*military term, Bear's addition; near match only (Ch 8 effective data scope)*

In plain words: give the agent only the information its task needs. Ask of every piece of data: does the agent need to know this? Industry also calls it least privilege. In Ch 8's case, the task needed 0 of the 124 records that left.

**survivorship bias**  
*common usage; zero mentions in the book. The nearest idea is Ch 6 lines 70 and 72: a filter that drops the sickest patients, so "survivors of an aggressive filter" stand in for those dropped*

In plain words: drawing conclusions only from the cases that made it through a filter and ignoring those that dropped out, so the data looks better than reality.

**precision**  
*in Ch 2 only as an ordinary word (line 259); common usage as a metric*

In plain words: of everything the test flagged as positive, the share that really is positive. It is the positive predictive value that Ch 2's disease-test arithmetic computes without naming it.

**recall**  
*not in the book*

In plain words: the same thing as sensitivity and the true positive rate: of the people who really have the disease, the share the test catches. Ch 2 uses sensitivity and true positive rate.

**temperature (sampling, in language models)**  
*common usage; the book uses temperature only as temperature scaling (Ch 2, 11)*

In plain words: a setting used when a language model generates text. Low temperature makes the most likely next word almost always win (repeatable, plain). High temperature flattens the choices (varied, riskier). It changes how random the text is, not what the model knows or how well calibrated its confidence is. Not to be confused with temperature scaling, a number fitted after training to fix overconfidence.

**kinds of drift: data drift, label drift, concept drift, model decay**  
*common usage; the book says distribution shift and natural drift (Ch 2, Ch 4)*

In plain words: data drift is the inputs changing. Label drift is the outcome mix changing. Concept drift is the relationship between inputs and outcome changing. Model decay is performance wearing away over time. Not drift: adversarial perturbation, which Ch 4 treats as a different risk.

**bias in the probabilistic sense: P(A) is not equal to P(A given B)**  
*Bear's shorthand; the chapter's own forms are Bias = E[estimator] minus the true value (Ch 6 lines 36-46) and the group prediction-rate comparison (Ch 6 line 112)*

In plain words: knowing B changes the chance of A. When B should not matter (a protected group) or the sample was filtered on B, that gap is a bias. A changed conditional probability is not automatically unfair.

**reuse versus bespoke; a step with no tool; mechanical versus human tests; points of failure in a plan**  
*added in the five-capacities deck and Ch 9 field list; not in the book*

In plain words: for each step decide whether an existing tool is enough, an existing tool adapted, or something bespoke must be built (cost against risk). A step with no tool is a step the plan proposes that nothing in the plan can do. Tests an AI can run are mechanical, like checking colour contrast on a website; most tests that matter are qualitative human tests.

# Part D: not on the exam

## Chapter 5 methods: important to learn, not on the exam (35)

Bear: LIME, SHAP and the other specific attribution methods.

**baseline**  *(also: global average; expected prediction; global mean)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 2 ×15, Ch 3 ×2, Ch 4 ×18, Ch 5 ×9, Ch 6 ×5, Ch 7 ×3, Ch 8 ×7, Ch 9 ×1, Ch 10 ×9, Ch 11 ×7, Ch 12 ×1, Ch 13 ×11 · kind: concept*

> $v(\emptyset) = \mathbb{E}[\hat{f}]$: with no features, predict the global average.
> — *the book, Ch 5 line 85; explained across several passages, no single defining sentence*

In plain words: The baseline is the model's average prediction over the dataset: what it predicts when no features are known. SHAP attributions add up to the gap between the actual prediction and this baseline.

Example: In the loan example the baseline is 0.55 and the prediction 0.72 sits 0.17 above it.

**SHAP**  *(also: SHAP attributions)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 4 ×1, Ch 5 ×60 · kind: method*

> For each feature, you compute the marginal contribution that feature makes to the prediction, averaged over all possible orderings in which features could have been added to the model's calculation. Out comes one number per feature, and the numbers add up — across features — to the model's deviation from a baseline.
> — *the book, Ch 5 line 43*

In plain words: SHAP is a feature-attribution method from cooperative game theory that gives each feature one number: its average marginal contribution to the prediction across all orderings of the features. The numbers add up to how far the prediction sits from a baseline.

Example: For one loan applicant, zip code gets a Shapley value of 0.035.

Not to be confused with: LIME (fits a local model instead of a game-theoretic accounting)

**Additivity**  *(also: Linearity)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 2 ×2, Ch 5 ×7 · kind: concept*

> Additivity. If we have two games (say, two models) and combine their payouts, the Shapley values for the combined game are the sums of the individual Shapley values:
> — *the book, Ch 5 line 148*

In plain words: If two models' payouts are combined, the Shapley values for the combined game are the sums of the two models' Shapley values. The chapter says Additivity and Linearity are the same property under two names.

Example: SHAP attributions for a random forest can be computed per tree and then averaged.

**LIME**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 4 ×1, Ch 5 ×22 · kind: method*

> Instead of attributing contributions through a game-theoretic accounting, LIME fits a simple, interpretable model — usually a linear regression — to the local neighborhood of the prediction. You perturb the input slightly, watch how the model's output changes, and fit a line to the local pattern. The line's coefficients are the explanation.
> — *the book, Ch 5 line 239*

In plain words: LIME explains one prediction by nudging the input slightly, watching how the model's output changes, and fitting a simple model (usually a linear regression) to that local pattern. The line's coefficients are the explanation.

Example: A text classifier's top features for one input, read off a local linear fit.

Not to be confused with: SHAP (a game-theoretic accounting rather than a local fit)

**Symmetry**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 2 ×1, Ch 5 ×4 · kind: concept*

> Symmetry. If two features $i$ and $j$ are interchangeable — if swapping them never changes the value function for any coalition — then their Shapley values are equal:
> — *the book, Ch 5 line 136*

In plain words: If two features are interchangeable, meaning swapping them never changes the value for any coalition, they get equal Shapley values. Features that do the same work get the same credit.

Example: Two identical features cannot be assigned different importance.

**coalition**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 1 ×1, Ch 5 ×21 · kind: concept*

> The value function answers: if this coalition of features is all we know, what do we predict on average?
> — *the book, Ch 5 line 82; explained across several passages, no single defining sentence*

In plain words: A coalition is a group of features treated as known while the rest are averaged out. The Shapley value asks what a feature adds when it joins a coalition.

Example: When income arrives after debt-to-income and zip code, the coalition is {x2, x3}.

**Efficiency**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×15, Ch 13 ×1 · kind: concept*

> Every bit of the deviation from the average is attributed to some feature. Nothing is left over. Nothing is double-counted.
> — *the book, Ch 5 line 134; explained across several passages, no single defining sentence*

In plain words: Efficiency says the Shapley values add up exactly to the prediction minus the baseline. Every bit of the deviation is credited to some feature, with nothing left over and nothing counted twice.

Example: 0.073 + 0.062 + 0.035 = 0.17 in the loan example.

Not to be confused with: causal attribution (Efficiency does not make any individual attribution causal)

**Shapley value**  *(also: Shapley values; φ_i)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×28 · kind: metric*

> The Shapley value $\phi_i$ averages the marginal contribution of feature $i$ across every possible ordering of features — equivalently, across every coalition $S$ that does not contain $i$. Features already in $S$ are those that joined before $i$; features not in $S$ join after.
> — *the book, Ch 5 line 108*

In plain words: A feature's Shapley value is its marginal contribution averaged over every possible order in which the features could be added. The values for all features add up to the prediction's deviation from the baseline.

Example: Income's Shapley value is (0.08 + 0.08 + 0.07 + 0.09 + 0.06 + 0.06)/6 = 0.073.

**the model's internal accounting**  *(also: the model's own internal accounting)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 4 ×2, Ch 5 ×3 · kind: concept*

> That phrase is the whole game. The model has an internal accounting. The accounting is real — it is what the model actually did.
> — *the book, Ch 5 line 45; explained across several passages, no single defining sentence*

In plain words: The internal accounting is the model's own bookkeeping of how much each feature moved its prediction. It is real, since it is what the model actually did, but it is not the same as how the world works.

Example: A zip-code attribution of 0.035 is a real number about the model's behavior and says nothing about whether zip code matters in the world.

Not to be confused with: the world (the model's accounting is not the world)

**marginal contribution**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×12 · kind: concept*

> The core object is the marginal contribution of feature $i$ to coalition $S$ — the change in prediction when $i$ is added to $S$:
> — *the book, Ch 5 line 100*

In plain words: The marginal contribution is the change in the prediction when one feature is added to a group of features already known. It depends on which other features are already in the group.

Example: In the worked example, income adds +0.08 when it arrives first and +0.06 when it arrives after both other features.

**Dummy**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×9 · kind: concept*

> Dummy. If a feature $i$ never affects the prediction — if adding it to any coalition changes nothing — its Shapley value is zero:
> — *the book, Ch 5 line 142*

In plain words: If a feature never changes the prediction when added to any coalition, its Shapley value is zero. A non-zero attribution for a feature such as zip code does not break Dummy; it means the model uses that feature.

Example: A non-zero zip-code attribution does not violate Dummy; it means the model uses zip code.

**value function**  *(also: v(S))*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×8 · kind: concept*

> The first ingredient is a value function $v(S)$, defined for any subset $S$ of features. $v(S)$ is the expected prediction when only the features in $S$ are known.
> — *the book, Ch 5 line 78*

In plain words: The value function v(S) gives the model's expected prediction when you know only the features in a chosen group S and average over the rest. The Shapley calculation uses it to price each group of features.

Example: With no features v is the global average (0.55 in the loan example); with all features it is the model's actual output (0.72).

**force plot**  *(also: force-plot visualization)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×6 · kind: concept*

> This is the property that makes SHAP attributions additive: the force-plot visualization, where contributions push left and right from a baseline, is exactly this property rendered visually.
> — *the book, Ch 5 line 134*

In plain words: A force plot draws the Shapley values as arrows pushing the prediction left and right from the baseline. It is the Efficiency property rendered visually, so the arrows sum exactly to the prediction deviation.

Example: In the loan example the zip code arrow is real but not causal.

**feature attribution**  *(also: attribution; importance)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×5 · kind: concept*

> What SHAP shows is the additive contribution of each feature to the prediction, in the model's own internal accounting.
> — *the book, Ch 5 line 45*

In plain words: A feature attribution gives each input feature a number saying how much it contributed to one prediction. In SHAP the number is measured inside the model's own accounting, so it says what the model used, not what causes the outcome.

Example: Income contributed +0.18 to this prediction.

Not to be confused with: causal effect (an attribution is not a causal effect)

**cooperative game**  *(also: features as players; payout)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×4 · kind: concept*

> Think of the features as players in a cooperative game. The prediction — minus its average — is the payout. How much did each player contribute to that payout?
> — *the book, Ch 5 line 74*

In plain words: Shapley values treat the features as players in a cooperative game whose payout is the prediction minus its average. The question is how much each player contributed to that payout.

Example: In the loan model, income, debt-to-income ratio and zip code are the players and the payout is 0.72 − 0.55 = 0.17.

**features entering a room**  *(also: random arrivals; random orderings)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×3 · kind: concept*

> Equivalently — and this is the intuition I prefer — think of the features entering a room in a random order. Every ordering is equally likely. When feature $i$ enters, it finds some coalition $S$ already there.
> — *the book, Ch 5 line 114*

In plain words: An intuition for the Shapley value: picture the features walking into a room in a random order and score each by how much the prediction changes when it arrives. The Shapley value is the average of that change over all the random arrivals.

Example: For four features there are 4! = 24 orderings, and each feature's Shapley value averages over all 24.

**Frankenstein instances**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: failure mode*

> If $x_3$ and $x_4$ are strongly correlated, sampling them independently from their marginal distributions produces combinations that never appear in the real data — "Frankenstein instances" that the model may not have been trained on and will extrapolate on in unpredictable ways.
> — *the book, Ch 5 line 219*

In plain words: Frankenstein instances are artificial feature combinations, made by sampling correlated features independently, that never appear in real data. The model may not have been trained on them and may behave unpredictably on them.

Example: A strongly correlated pair such as zip code and income, sampled as if they were unrelated.

**local linear approximation**  *(also: linear surrogate; local neighborhood)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: concept*

> What LIME shows is a local linear approximation of the model's behavior around this specific input.
> — *the book, Ch 5 line 241*

In plain words: LIME's output is a straight-line approximation of the model's behavior in a small neighborhood around one input. It says nothing reliable about the model outside that neighborhood.

Example: A small linear surrogate that approximates the model around this input.

Not to be confused with: the model's actual computation

**off-manifold**  *(also: data manifold)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: failure mode*

> LIME's quality depends on whether the perturbation distribution matches the data manifold — that is, whether the perturbed inputs are still recognizable as plausible inputs — and whether the local model fits well. Both can fail silently.
> — *the book, Ch 5 line 243*

In plain words: Off-manifold means the slightly changed inputs LIME tries are no longer recognizable as plausible inputs. When that happens the coefficient LIME gives you is unreliable, and it does not warn you.

Example: LIME returns a coefficient with no flag saying it is unreliable because the perturbations went off-manifold.

**TreeSHAP**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×2 · kind: method*

> For tree-based models — decision trees, random forests, gradient-boosted trees — the tree structure can be exploited to compute exact Shapley values in $O(T L D)$ time, where $T$ is the number of trees, $L$ is the maximum leaves in any tree, and $D$ is the maximum depth. The key insight: a decision tree has a small, bounded number of distinct prediction paths, so instead of enumerating all $2^{|F|}$ coalitions, we walk the tree paths that actually change predictions, weight them correctly, and combine.
> — *the book, Ch 5 line 206*

In plain words: TreeSHAP computes exact Shapley values for tree-based models by walking only the tree paths that change predictions instead of enumerating every coalition. It is orders of magnitude faster than KernelSHAP for large forests.

Example: XGBoost, random forests and LightGBM models.

Not to be confused with: KernelSHAP (approximate, works on any model)

**Monte Carlo sampling (KernelSHAP)**  *(also: KernelSHAP; Monte Carlo sampling)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: method*

> Monte Carlo sampling (KernelSHAP). Instead of all orderings, sample $M$ random orderings and average marginal contributions:
> — *the book, Ch 5 line 198*

In plain words: KernelSHAP estimates Shapley values by sampling M random orderings and averaging the marginal contributions instead of using every ordering. More samples reduce variance but cost more computation.

Example: It works on any model, so it is the model-agnostic baseline.

Not to be confused with: LIME (both fit a weighted linear model to coalition predictions and differ only in how they weight the coalitions)

**antithetic sampling**  *(also: Permutation Method)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: method*

> For each sampled ordering, compute marginal contributions in both the forward direction and the reversed ordering simultaneously. This reduces variance compared to independent sampling at the same computational cost, because the reverse ordering is the cheapest way to get an additional independent estimate.
> — *the book, Ch 5 line 204*

In plain words: For each sampled ordering the method also uses the reversed ordering, which gives an extra estimate at no extra cost and lowers variance. It is also called the Permutation Method.

Example: The shap package uses 10 permutations by default for this method.

Not to be confused with: KernelSHAP (independent sampling at the same cost has higher variance)

**four axioms**  *(also: Shapley axioms; the guarantee)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×5 · kind: framework*

> Shapley values are the unique attribution satisfying four axioms. Understanding the axioms is understanding what the guarantee is.
> — *the book, Ch 5 line 128; explained across several passages, no single defining sentence*

In plain words: The Shapley value is the only attribution that satisfies four rules: Efficiency, Symmetry, Dummy and Additivity. Knowing them tells you exactly what SHAP guarantees, and so what it leaves unguaranteed.

Example: Efficiency guarantees that attributions sum to the prediction deviation; it does not guarantee any attribution is causal.

**correlated feature problem**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×4 · kind: failure mode*

> There is a structural limitation that follows directly from the mathematics. Computing $v(S)$ requires marginalizing over features not in $S$ — sampling them from their distribution while fixing the features in $S$.
> — *the book, Ch 5 line 217; explained across several passages, no single defining sentence*

In plain words: To price a coalition, SHAP samples the missing features independently from their marginal distribution, which ignores any correlations between them. This can create combinations of values that never occur in real data.

Example: If x3 and x4 are strongly correlated, sampling them independently produces pairs the model never saw.

**what SHAP does not show**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: concept*

> What SHAP does not show is why the feature is contributing what it is contributing. The model has internalized some relationship between the feature and the output. SHAP tells you the magnitude of the contribution, not the nature of the relationship.
> — *the book, Ch 5 line 47; explained across several passages, no single defining sentence*

In plain words: SHAP gives the size of each feature's contribution but not why the feature contributes it, whether the contribution is causal, whether the model is wrong on this case, or what would happen if the feature changed. Those are the limits a reader must keep in mind.

Example: SHAP says zip code moved the prediction 3.5 points; it cannot say whether that effect would persist if the applicant moved.

**axiomatic guarantee**  *(also: the guarantee)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 ×1 · kind: concept*

> That guarantee is Efficiency: attributions sum to the prediction deviation. It does not guarantee that the attributions are causal, correct, or meaningful in the user's language game. Those are three different claims, and only the first one is guaranteed.
> — *the book, Ch 5 line 387; explained across several passages, no single defining sentence*

In plain words: The one thing SHAP formally guarantees is Efficiency, that attributions add up to the prediction's deviation. It does not guarantee the attributions are causal, correct, or meaningful in the user's language game.

Example: The loan example's values sum exactly to 0.17, yet the zip code attribution says nothing about whether zip code is a proxy.

**misreading attribution as causal**  *(also: treating the attribution as causal; a Rung 1 attribution treated as a Rung 2 claim)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: failure mode*

> For a practitioner reading SHAP output, the operational risk is a single misread: treating the attribution as causal. It is not. It is descriptive of the model's internal accounting, and the model's internal accounting is not the world.
> — *the book, Ch 5 line 55*

In plain words: The one mistake the chapter says a practitioner must avoid: reading a SHAP number as saying a feature causes the outcome. It only describes how much the model used that feature.

Example: A colleague says 'SHAP shows zip code is causing the denial' (exercise W1).

**marginal versus conditional SHAP**  *(also: marginal SHAP; marginal sampling)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: concept*

> The choice between marginal and conditional SHAP is a philosophical choice about what you want to measure: "how much does this feature contribute to the model's behavior on average?" (marginal) versus "how much does this feature contribute given what we already know?" (conditional). Neither is wrong. They answer different questions.
> — *the book, Ch 5 line 223*

In plain words: Choosing marginal or conditional sampling is a choice about what you want to measure: how much a feature contributes to the model's behavior on average, or how much it contributes given what you already know. Neither is wrong; they answer different questions.

Example: Zip code and income: marginal SHAP gives zip code 0.19, conditional SHAP gives 0.04 (exercise A5).

**silent failure of LIME**  *(also: fail silently)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: failure mode*

> Both can fail silently. You get a coefficient. You don't get a flag that says "this coefficient is unreliable because the perturbations went off-manifold."
> — *the book, Ch 5 line 243*

In plain words: LIME can go wrong without any warning: you get a coefficient but no flag saying it is unreliable. Both a perturbation distribution that does not match the data and a poor local fit can hide this way.

Example: A coefficient that looks fine but came from implausible perturbed inputs.

**local explanation does not generalize**
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: failure mode*

> It does not show whether the local explanation generalizes. A nearby input may have a completely different LIME explanation, because the model is locally linear but globally nonlinear, and "locally" in the LIME sense is a smaller neighborhood than the practitioner's intuition tends to assume.
> — *the book, Ch 5 line 245*

In plain words: A LIME explanation is only good near one input, and a nearby input can have a completely different explanation. The model is locally linear but globally nonlinear, and LIME's neighborhood is smaller than people tend to assume.

Example: Two nearby inputs to the same classifier getting different LIME explanations.

**LIME instability across runs**  *(also: LIME is not stable across runs)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: failure mode*

> And — this is the awkward one — LIME is not stable across runs. Run the same input twice, and you can get different explanations, because the perturbations are sampled randomly. Most practitioners running LIME do not run it twice.
> — *the book, Ch 5 line 249*

In plain words: Running LIME twice on the same input can give different explanations because the perturbations are sampled randomly. Most practitioners run it once and read that single result as the answer.

Example: Exercise A1: two runs on the same text input give different top features, and a manager asks which is correct.

**conditional sampling (conditional SHAP)**  *(also: conditional SHAP; conditional distribution)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: method*

> One fix is to sample from the conditional distribution $P(x_{\bar{S}} \mid x_S)$: fix the features in $S$ and draw the rest conditional on those values. This avoids unrealistic combinations. The cost is that the resulting values are no longer Shapley values in the classic sense — the Dummy axiom can be violated, meaning features that have no direct influence can receive non-zero attribution through their correlations with influential features.
> — *the book, Ch 5 line 223*

In plain words: Conditional sampling fixes the features in the coalition and draws the others conditional on those values, which avoids unrealistic combinations. The cost is that the results are no longer classic Shapley values, because Dummy can be violated and a feature with no direct influence can get a non-zero attribution through its correlations.

Example: In exercise A5, switching from marginal to conditional sampling moves zip code from 0.19 to 0.04 and income from 0.31 to 0.46.

Not to be confused with: marginal sampling

**Shapley weight**  *(also: the weight on each coalition)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: concept*

> The weight $\frac{|S|!\,(|F|-|S|-1)!}{|F|!}$ counts the fraction of all $|F|!$ orderings in which the features in $S$ all precede $i$ and all features not in $S \cup \{i\}$ follow $i$.
> — *the book, Ch 5 line 112; explained across several passages, no single defining sentence*

In plain words: The weight on a coalition is the fraction of all possible orderings in which exactly those features arrive before feature i. The weights across all coalitions add up to 1.

Example: For three features there are 3! = 6 orderings to share out among the coalitions.

**exponential cost of exact Shapley values**  *(also: exact computation is expensive; exponential in the number of features)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: concept*

> Exact Shapley values require evaluating $v(S)$ for all $2^{|F|}$ subsets — exponential in the number of features. For a model with 10 features that means 1,024 subsets; for 30 features, over a billion.
> — *the book, Ch 5 line 196; explained across several passages, no single defining sentence*

In plain words: Computing exact Shapley values means evaluating every subset of features, and the number of subsets doubles with each added feature. That is why SHAP uses efficient approximation algorithms for large feature sets.

Example: 10 features means 1,024 subsets; 30 features means over a billion.

**worked example (loan model)**  *(also: the sentence the whole chapter turns on)*
*LEARN IT, NOT ON THE EXAM (Bear) · in the chapter text: Ch 5 · kind: named result or case*

> The attribution to zip code — $\phi_{x_3} = 0.035$ — is a real number describing the model's behavior, and it tells you nothing about the world. It says the zip code feature moved the prediction 3.5 percentage points above the global mean across all orderings.
> — *the book, Ch 5 line 184; explained across several passages, no single defining sentence*

In plain words: A loan model with income, debt-to-income ratio and zip code predicts 0.72 against an average of 0.55, and the Shapley values 0.073, 0.062 and 0.035 add up to the 0.17 gap. The chapter uses it to show that exact, complete arithmetic is still precision about the model, not the world.

Example: Zip code's 0.035 does not say whether zip code is a proxy for race or geography, or whether the effect would persist if an applicant moved.

## Chapters 10, 11, 12 and 13: not on the exam beyond the core (265)

Bear: Chapter 10 will not be on the exam, and in Chapter 11 the exam covers what uncertainty is and calibration, not how to visualize or show it; he will put up separate material on that. For Chapter 11 the split is by section: not on the exam are The verb taxonomy, Two readers one document, Saying you do not know in writing, Why solitary review does not work, Glimmer 11.1, What survives review and Where this leaves us. On the exam: the chapter opening and all of Metrics and measures of trust calibration (Brier score, ECE, reliability diagram, subgroup calibration, temperature scaling, conformal prediction, what calibration cannot see). This split is a first reading and is easy to change. Chapter 13 (The Limits of AI) will not be on the exam (to be confirmed in class). Chapter 12 is simplified to one point: AI is not accountable, you are. Only the terms about that point stay on the exam (accountability, sign-off, signing your name, responsibility, validation); the tiers, the responsibility-gap detail, recourse and the rest are out. Terms shared with other chapters stay in Parts A and B.

**accountability**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×1, Ch 3 ×1, Ch 5 ×1, Ch 6 ×7, Ch 7 ×3, Ch 8 ×6, Ch 9 ×2, Ch 11 ×1, Ch 12 ×100, Ch 13 ×28 · kind: concept*

> Accountability is not a cognitive skill in the ordinary sense. It is a relationship between a judgment and the person who made it — the willingness to be answerable for the consequence of being wrong.
> — *the book, Ch 13 line 206; explained across several passages, no single defining sentence*

In plain words: A relationship between a judgment and the person who made it: being answerable for the consequence of being wrong. AI is absent here because it cannot be held answerable, so the book assigns accountability to the human in the loop.

Example: A practitioner who signs off on a validation report takes on the obligation to revise it if it turns out to be wrong.

Not to be confused with: functional equivalence (audits, explanations, corrections - the objection in Exercise 12)

**find**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×17, Ch 2 ×4, Ch 3 ×7, Ch 4 ×3, Ch 5 ×2, Ch 6 ×4, Ch 7 ×2, Ch 8 ×3, Ch 9 ×2, Ch 10 ×6, Ch 11 ×29, Ch 12 ×2, Ch 13 ×1 · kind: concept*

> Posture: across the evidence we have looked at, X holds. Slightly stronger than observe — it implies multiple observations or robustness to some variation in conditions. The evidence required is at least replication, ideally with some sensitivity analysis.
> — *the book, Ch 11 line 55*

In plain words: Say X holds across the evidence you have looked at, which needs at least a replication and ideally a sensitivity check. It sits one step above observe and one below show.

Example: "We find subgroup ECE exceeds global ECE by 2.3x on the elderly cohort".

Not to be confused with: observe

**show**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×15, Ch 2 ×9, Ch 3 ×15, Ch 4 ×10, Ch 5 ×16, Ch 6 ×4, Ch 7 ×8, Ch 8 ×7, Ch 9 ×3, Ch 10 ×35, Ch 11 ×20, Ch 13 ×5 · kind: concept*

> Posture: the evidence demonstrates X with sufficient strength that X is the operational reading. The evidence required is replication, robustness, alternative-explanation ruling-out. This is a strong verb.
> — *the book, Ch 11 line 57*

In plain words: Say the evidence is strong enough that X is the working reading, which needs replication, robustness and other explanations ruled out. The chapter calls it a strong verb and says not to use it lightly.

Example: "We show the subgroup gap persists under three calibration methods".

**specifications**  *(also: spec)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×2, Ch 2 ×2, Ch 3 ×1, Ch 4 ×12, Ch 7 ×3, Ch 8 ×7, Ch 9 ×10, Ch 10 ×1, Ch 11 ×3, Ch 12 ×13, Ch 13 ×2 · kind: concept*

> A failure is, operationally, a divergence from specification; without one, there is nothing the system was supposed to do that it failed to do, and no accountability claim that can be precisely made.
> — *the book, Ch 12 line 188*

In plain words: The written task definition, with input/output contracts and named acceptance criteria, signed by an accountable human. A failure is, operationally, a divergence from it, so without one no accountability claim can be made precisely.

Example: Absent: the deployment runs against unstated criteria and 'the model said so' is the audit response.

**meaning**  *(also: Limit 1)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×4, Ch 2 ×2, Ch 3 ×1, Ch 4 ×4, Ch 5 ×4, Ch 6 ×7, Ch 7 ×3, Ch 9 ×1, Ch 10 ×1, Ch 11 ×1, Ch 13 ×25 · kind: concept*

> The system has no representation of the referents. It manipulates the symbols; the meaning of the symbols — what they refer to in the world the user inhabits — is supplied by the user, not the system.
> — *the book, Ch 13 line 61*

In plain words: The first categorical limit: the system manipulates symbols but has no representation of what they refer to in the world. The user supplies that link, so the supervisor must check that the answer responds to the question actually asked.

Example: The AI answered the question whose symbols it processed; the supervisor asks "safe for whom, doing what, in which world?"

**plausibility auditor**  *(also: plausibility auditing)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 9 ×1, Ch 12 ×10 · kind: concept*

> The plausibility auditor — the profession that the automated research vision forgot to invent — is not a fact-checker or a quality assurance technician. It is someone trained to stand outside sophisticated AI outputs and ask whether those outputs correspond to reality rather than merely to internal consistency.
> — *the book, Ch 12 line 147; explained across several passages, no single defining sentence*

In plain words: A person trained to stand outside sophisticated AI outputs and ask whether they match reality, not just whether they are internally consistent. It needs deep domain knowledge plus knowledge of AI failure modes, and the chapter says this profession has not been built.

Example: The human who discovered the email still existed on Proton Mail by checking the agent's report against the world.

Not to be confused with: a fact-checker or quality assurance technician (the chapter says it is neither)

**length**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 2 ×7, Ch 3 ×5, Ch 4 ×9, Ch 5 ×6, Ch 6 ×5, Ch 7 ×3, Ch 8 ×7, Ch 10 ×7, Ch 11 ×4, Ch 12 ×1 · kind: concept*

> Length — nearly as good. Bars on a shared baseline use this channel. Reliable.
> — *the book, Ch 10 line 93*

In plain words: Showing values by the length of bars that start from a shared baseline; nearly as accurate as position and reliable.

Example: Bars on a shared baseline.

**responsibility gap**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×5 · kind: concept*

> Andreas Matthias named it in 2004: learning, autonomous machines open a responsibility gap — nobody can be fairly held responsible for a machine's action when the people who built and operate it cannot predict the behavior it learned
> — *the book, Ch 12 line 35*

In plain words: A gap that opens when a machine learns behavior its builders and operators could not predict: nobody can fairly be held responsible for what it does. The chapter credits the idea to Matthias (2004).

Example: The mail-server deletion: responsibility spread across non-owner, agent, owner, framework developers and model provider with no single party answerable for the whole.

**truncated axes**  *(also: truncated axis; truncated y-axes)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×4 · kind: failure mode*

> A bar chart with the y-axis starting at 80 instead of 0 makes a small difference look large. Legitimate uses: when the relevant range really is narrow, when zero is not meaningful for the quantity being displayed (stock prices are routinely shown on truncated axes for good reason). Illegitimate uses: when the visual amplification implies a larger effect than the data supports.
> — *the book, Ch 10 line 189*

In plain words: Starting an axis above zero so a small difference looks large. It is honest only when the relevant range is narrow or zero is not meaningful; it misleads when the amplification implies a bigger effect than the data supports.

Example: A y-axis running 91% to 96% makes 94.3% look about three times as tall as 92.1% (exercise 1).

Not to be confused with: axis inversion (truncation amplifies a real effect; inversion reverses one)

**chartjunk and 3D effects**  *(also: chartjunk; 3D effects)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> Often introduced for aesthetic reasons; their effect is often to obscure. Tufte's term "chartjunk" names the category: any element of the display that does not transmit information about the data.
> — *the book, Ch 10 line 201*

In plain words: Decoration that carries no information about the data and can distort how big the numbers look. Tufte's word 'chartjunk' names any display element that does not transmit information about the data.

Example: 3D bar charts whose foreshortening makes near bars look bigger than far ones, and pie charts with exploded slices.

**recourse**  *(also: redress)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×16 · kind: concept*

> Recourse is a social, relational act: an affected party makes a claim, the claim is heard, a response is given.
> — *the book, Ch 12 line 192; explained across several passages, no single defining sentence*

In plain words: A channel through which an affected party makes a claim, is heard and gets a response, including contesting, appealing or repairing. It is a social act (Tiers 3 and 6), so an entirely AI-mediated version replaces being heard with a simulation.

Example: Absent: complaints route to 'support' with no resolution path.

**communicating validation findings**  *(also: supervisory capacity)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×2 · kind: framework*

> Together the two chapters are the supervisory capacity for communicating validation findings, which is, structurally, where validation work meets its readers.
> — *the book, Ch 11 line 429; explained across several passages, no single defining sentence*

In plain words: The supervisory capacity built by this chapter and the one before it: getting a validation result to its readers without claiming more than the evidence gave. The previous chapter fights the misleading chart (truncated axis, tilted color) and this one fights the misleading verb.

Example: Chapter 10 fights a truncated axis; Chapter 11 fights a verb that quietly claims more than the evidence.

**meaningful human control**  *(also: design surface; putting humans at the points where answerability is required)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: concept*

> You close the gaps by putting humans at the points where answerability is required, not by consolidating blame onto one node.
> — *the book, Ch 12 line 35; explained across several passages, no single defining sentence*

In plain words: Closing the responsibility gaps by designing socio-technical systems so a human is placed at each point where someone must be able to answer. It treats the spread of responsibility as a design surface, not a defect to be engineered away.

Example: Naming a human per decision (who cleared which gate) in an attestation.

**prove**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×3, Ch 2 ×2, Ch 4 ×2, Ch 5 ×1, Ch 6 ×1, Ch 7 ×4, Ch 9 ×3, Ch 11 ×13, Ch 12 ×1 · kind: concept*

> A mathematical proof. Reserved for formal claims with formal evidence.
> — *the book, Ch 11 line 63*

In plain words: The top rung of the ladder: say X is established by a mathematical proof, reserved for formal claims with formal evidence. For calibration the chapter ties it to a formal guarantee such as conformal prediction, with the assumptions stated.

Example: "We prove the bound holds for all inputs in the certified region".

Not to be confused with: conclude (the strongest verb below it)

**observe**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×2, Ch 2 ×4, Ch 6 ×4, Ch 7 ×1, Ch 8 ×2, Ch 9 ×1, Ch 11 ×22, Ch 13 ×2 · kind: concept*

> Posture: the data shows X under these specific conditions. No claim about generalization beyond the conditions. The evidence required is a clean observation, with the observation conditions stated.
> — *the book, Ch 11 line 53*

In plain words: Report what the data show under the specific conditions you tested, with those conditions stated, and claim nothing beyond them. The chapter calls it the most defensible verb when the evidence is a single experiment or a single dataset.

Example: "We observe ECE = 0.04 on the global test set".

Not to be confused with: find (observe is weaker: a single observation under specific conditions versus a result established across variation)

**suggest**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 3 ×2, Ch 4 ×2, Ch 9 ×2, Ch 10 ×3, Ch 11 ×12, Ch 12 ×2 · kind: concept*

> Posture: the data is consistent with X but does not distinguish X from alternatives. The evidence required is an observation that points toward X without ruling out other explanations. Common when an experiment was not designed to test X but X emerged from the analysis.
> — *the book, Ch 11 line 51*

In plain words: Say the data fit X without being able to tell X apart from other explanations, so the evidence only points toward X. It sits just below observe on the ladder.

Example: "These results suggest miscalibration concentrates in the elderly subgroup".

Not to be confused with: find (the chapter lists using suggest when the evidence already supports find as a misuse)

**area**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 1 ×1, Ch 3 ×2, Ch 6 ×1, Ch 8 ×1, Ch 10 ×11, Ch 11 ×1 · kind: concept*

> Area — considerably worse. Bubbles and treemap rectangles encode quantity as area. Useful when relative magnitude is all that matters; unreliable when the reader needs to compare closely.
> — *the book, Ch 10 line 95*

In plain words: Showing values by the area of a shape; useful when only relative magnitude matters but unreliable when readers must compare closely.

Example: Bubbles and treemap rectangles.

**peer critique**  *(also: peer critique as collective validation infrastructure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 7 ×1, Ch 10 ×2, Ch 11 ×21, Ch 13 ×8 · kind: method*

> The structural solution is collective. Other readers can see the mismatches, because they did not write the sentences and the evidence does not sit in their heads in the way that produced the verbs. This is why peer critique is part of any honest validation infrastructure — not because two opinions are better than one, but because there is a class of error that is invisible to the person who made it and visible to anyone else.
> — *the book, Ch 11 line 344*

In plain words: Having other readers check your writing for verb-evidence mismatches, because they did not write the sentences and the evidence is not in their heads. The chapter justifies it by a class of error invisible to the person who made it, not by two opinions being better than one.

Example: A reviewer flags that "we conclude" in section 3.2 rests on a single test set without significance testing and suggests "we observe".

**blind spots**  *(also: your blind spots are blind to you; why solitary review does not work)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 3 ×1, Ch 6 ×1, Ch 11 ×4, Ch 12 ×3 · kind: concept*

> You cannot fully evaluate your own writing for verb-evidence calibration mismatches, because you wrote the sentences with the strongest verbs that felt true to you, and the feeling was a function of how the evidence sat in your head when you wrote — which is no longer accessible to you when you re-read. The mismatches you produced are exactly the ones you cannot see. Your blind spots are blind to you.
> — *the book, Ch 11 line 342*

In plain words: You cannot reliably catch the over-strong verbs in your own writing, because the strength felt true to you from how the evidence sat in your head when you wrote it. The mismatches you made are exactly the ones you cannot see.

Example: A peer sees that "we conclude" rests on a single test set without significance testing, which the author did not notice.

**go/no-go memo**  *(also: What This Agent Should Not Be Deployed For; final memo)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 5 ×1, Ch 6 ×2, Ch 12 ×1, Ch 13 ×2 · kind: framework*

> The final go/no-go memo for your agent — the deliverable the casebook has been building toward.
> — *the book, Ch 13 line 425*

In plain words: The final deliverable: a memo that gives a calibrated-verb recommendation, lists where the agent works, where it should not be used, where more work could change the answer, the named human owner and the stop condition. Its verbs are audited against the Chapter 11 taxonomy.

Example: A headline such as "We RECOMMEND / WARN / REFUSE...".

**conclude**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 2 ×2, Ch 11 ×20, Ch 13 ×1 · kind: concept*

> Posture: the question that motivated the work is settled by the evidence. The evidence required is full analysis, alternatives considered and rejected, sensitivity analysis, and a finding that survives the analysis. This is the strongest verb in the taxonomy short of mathematical proof.
> — *the book, Ch 11 line 61*

In plain words: Say the question that motivated the work is settled, which needs full analysis, alternatives considered and rejected, and a sensitivity analysis the finding survives. It is the strongest verb short of mathematical proof, and the chapter says very few claims warrant it.

Example: "We conclude the deployment cannot ship without subgroup-specific recalibration".

Not to be confused with: find or observe (the chapter says most engineering writing uses conclude when the evidence sits between observe and find)

**verb taxonomy**  *(also: verb ladder; frozen ladder; working hierarchy)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2, Ch 11 ×12, Ch 13 ×20 · kind: framework*

> I am being deliberate about freezing exactly one ordering, because a verb ladder that contradicts itself is worse than none — it hands you false confidence that you calibrated. So: observe is weaker than find (a single observation under specific conditions is weaker than a result established across variation); suggest sits below observe (an inference the data is merely consistent with); prove is reserved for mathematics or formal verification.
> — *the book, Ch 11 line 41; explained across several passages, no single defining sentence*

In plain words: A fixed ordering of eight claim verbs from weakest to strongest (hypothesize, suggest, observe, find, show, demonstrate, conclude, prove), each needing more evidence than the one before. You pick the verb whose evidence requirement your evidence actually meets.

Example: "We observe ECE = 0.04 on the global test set" (observe) versus "We conclude the deployment cannot ship without subgroup-specific recalibration" (conclude, which needs full analysis).

**Layer 1**  *(also: plain English summary)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×16, Ch 12 ×1, Ch 13 ×4 · kind: concept*

> A short, prose-paragraph summary at the start of every section. Plain English. No equations.
> — *the book, Ch 11 line 96*

In plain words: A short plain-English summary at the start of each section, with no equations, saying what the section finds and why it matters for the deployment decision. A non-technical reader can follow the whole document from Layer 1 alone, and it is specific and accurate, not dumbed down.

Example: A deployment partner reads only the Layer 1 paragraphs across the document and still gets a working understanding.

Not to be confused with: dumbing down (the chapter says Layer 1 is not that)

**demonstrate**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 4 ×1, Ch 11 ×17, Ch 13 ×1 · kind: concept*

> Posture: a constructed proof or near-proof. The evidence required is an experiment specifically designed to test X, ideally with formal guarantees or strong inferential control. Rare in deployed engineering work; common in formal verification.
> — *the book, Ch 11 line 59*

In plain words: Say X is backed by a constructed proof or near-proof from an experiment designed specifically to test X, ideally with formal guarantees or strong inferential control. It is rare in deployed engineering work and common in formal verification.

Example: "We demonstrate the gap survives a named distribution shift".

**accountability chain**  *(also: chain of accountability)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 8 ×1, Ch 12 ×2, Ch 13 ×3 · kind: concept*

> The chain of accountability in any AI-assisted validation workflow runs through the practitioners who apply the checking instruments: the practitioner who applies the verb taxonomy, the practitioner who reviews the chart for uncertainty suppression, the practitioner who signs off on the validation document.
> — *the book, Ch 13 line 210*

In plain words: The line of people in an AI-assisted workflow who are answerable for the judgment: those who apply the verb taxonomy, review the charts and sign off. Each of those moments is where a human takes on the obligation to be answerable.

Example: The practitioner who signs off on the validation document.

**necessary but not sufficient**  *(also: necessary; sufficient)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 3 ×2, Ch 7 ×1, Ch 12 ×1 · kind: concept*

> None of them, alone, produced the failure. Each one's choices were necessary; none was sufficient.
> — *the book, Ch 12 line 33*

In plain words: Each party's choices were a needed part of the cause (necessary), but no party's choices alone produced the failure (not sufficient). So the list of parties is a list of contributors, not a list of suspects.

Example: The non-owner, agent, owner, framework developers and model provider each contributed to the mail-server deletion; none alone caused it.

**overreach**  *(also: overreach patterns; overreaches its evidence)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 3 ×1, Ch 5 ×1, Ch 13 ×1 · kind: failure mode*

> Human-generated text, as Chapter 11 documented, systematically overreaches its evidence — engineers default to conclude when the evidence supports only observe; visualization defaults to confident-looking charts that hide uncertainty. A model trained on that text learns those overreach patterns.
> — *the book, Ch 13 line 186*

In plain words: Claiming more than the evidence supports. The chapter says human writing does this systematically and models trained on that text learn the habit, so the fix is a practitioner who checks the output, not a better model.

Example: Engineers default to conclude when the evidence supports only observe.

Not to be confused with: fluency trap

**error bars**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 2 ×1, Ch 10 ×3, Ch 11 ×2 · kind: method*

> Error bars (point estimate ± standard deviation or confidence interval). Use when you are showing point estimates from samples, side by side, and the reader needs a quick visual check on overlap.
> — *the book, Ch 10 line 125*

In plain words: A mark showing a point estimate plus or minus its spread, used to compare estimates from samples side by side and check for overlap. Readers often misread the bar as 'the true value is anywhere inside with equal probability', so the chart must say what the bar is.

Example: Label it every time: 'Error bar = 95% CI'.

**Pearl's Rung 3**  *(also: counterfactual reasoning; Rung 3 closure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 6 ×1, Ch 11 ×1, Ch 12 ×6 · kind: concept*

> We opened Pearl's Rung 3 in Chapter 4 — the rung of counterfactual reasoning. What would have happened to this specific case if some variable had been different, holding everything else fixed?
> — *the book, Ch 12 line 245; explained across several passages, no single defining sentence*

In plain words: The counterfactual rung of Pearl's ladder: asking what would have happened to this specific case if one variable had been different and everything else held fixed. The chapter closes it by applying it to the regime: Rung 1 sees the data, Rung 2 the model, Rung 3 the regime that produced both.

Example: Opened in Chapter 4; closed in this chapter by the governance counterfactual.

**validation set**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 2 ×1, Ch 11 ×4, Ch 13 ×3 · kind: concept*

> The validation set tests performance under conditions sampled from the same distribution as training. It does not test the assumption. The assumption requires its own test.
> — *the book, Ch 13 line 156; explained across several passages, no single defining sentence*

In plain words: The held-out data used to measure performance, drawn from the same distribution as training. It does not test the assumptions about the world the system will be deployed into.

Example: The clinical system reached 94% on its validation set and still harmed three patients.

Not to be confused with: an assumption test

**sanctions**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 7 ×1, Ch 12 ×15 · kind: concept*

> A sanction is consequential only when the sanctioned party has stakes — something to lose. An AI does not lose its job for a flawed output; a plausibility auditor does, a deploying organization does, a model provider does if the regime imposes consequences.
> — *the book, Ch 12 line 196*

In plain words: A consequence regime, internal (employment, license) and external (regulator, civil), that attaches to a named accountable human. It works only when the party has stakes; remove the possibility of consequence and you have a descriptive system, not a prescriptive one.

Example: An AI does not lose its job for a flawed output; a plausibility auditor does.

**independent review**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 9 ×1, Ch 12 ×12 · kind: concept*

> Independent review requires the plausibility auditor — the human with deep domain knowledge and AI-failure-mode literacy who can stand outside the output and ask whether it corresponds to reality. Without it, the deploying organization is grading its own work.
> — *the book, Ch 12 line 194*

In plain words: A reviewer outside the deployment team who has authority to halt or revise. Without one the deploying organization is grading its own work, and an AI reviewing another AI's outputs is more derivation, not external review.

Example: How to verify: a named reviewer, a documented review cadence and visible halt authority.

**peer critique protocol**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×4, Ch 13 ×6 · kind: method*

> The peer critique protocol requires a human because the error class it hunts — mismatch between what the writer committed to and what the evidence supports — requires judgment about evidence-to-world correspondence, not just structural validity within representations.
> — *the book, Ch 13 line 184*

In plain words: A review protocol for catching mismatch between what a writer committed to and what the evidence supports. It needs a human because it takes judgment about whether evidence corresponds to the world.

**three categorical limits**  *(also: three structural limits; meaning, intentionality, and the data-world gap)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1, Ch 13 ×8 · kind: framework*

> There are three structural limits that bound what current AI systems can do, regardless of capability scaling. Each demands a specific engineering practice from the supervisor.
> — *the book, Ch 13 line 38*

In plain words: The chapter's core framework: meaning, intentionality and the data-world gap bound what AI systems can do, and making models more capable does not remove them. Each calls for a specific practice from the human supervisor.

Example: Meaning: the supervisor maps outputs to what they refer to. Intentionality: the supervisor supplies the directedness. Data-world gap: the supervisor specifies the deployment distribution and overrides when it is exited.

**hypothesize**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 4 ×1, Ch 11 ×7 · kind: concept*

> Posture: an idea, not yet tested, that we are about to investigate. The evidence required is a coherent reason to investigate, not evidence that the hypothesis is true.
> — *the book, Ch 11 line 49*

In plain words: The weakest verb on the ladder: you have an idea you are about to investigate and only a coherent reason to look into it, not evidence that it is true. It is used at the front of a paper, in proposals and when framing future work.

Example: "We hypothesize that calibration degrades on the rare-disease subgroup".

**volume**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×4, Ch 13 ×1 · kind: concept*

> Volume — even worse. Avoid.
> — *the book, Ch 10 line 96*

In plain words: Showing values by three-dimensional volume, a very weak channel that the chapter says to avoid.

**clean bill of health**  *(also: a clean bill)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 7 ×1, Ch 12 ×3 · kind: failure mode*

> an attestation that lists only what you tested reads like a clean bill of health, and a clean bill of health is exactly what the affected party cannot act on when the untested region is where the harm lives.
> — *the book, Ch 12 line 223*

In plain words: An attestation or sign-off that reads as if everything is fine because it lists only what was tested. The affected party cannot act on it when the untested region is where the harm lives.

Example: A sign-off that says 'validated' with no list of untested conditions.

**defense-as-deliverable**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 7 ×2, Ch 12 ×1 · kind: concept*

> The book has now covered three types of defense-as-deliverable: the fairness defense (Chapter 7), the delegation map (Chapter 9), and the accountability regime (Chapter 12). Each one is a documented engineering decision under conditions where the technical artifact alone is insufficient.
> — *the book, Ch 12 line 392*

In plain words: A documented engineering decision handed over as the deliverable when the technical artifact alone is not enough. The chapter names the fairness defense, the delegation map and the accountability regime as three.

Example: Fairness defense (Chapter 7), delegation map (Chapter 9), accountability regime (Chapter 12).

**operational stance**  *(also: do both; test behavior and invoke the limits)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 4 ×1, Ch 13 ×2 · kind: framework*

> The two arguments together produce a useful operational stance: behavior is testable evidence and should be taken seriously — and behavior is not the whole of what we mean by understanding, meaning, or intentionality.
> — *the book, Ch 13 line 110*

In plain words: Treat behavior as testable evidence worth taking seriously, but remember it is not the whole of what we mean by understanding, meaning or intentionality. Do both.

Example: The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing.

**position along a common scale**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 3 ×1, Ch 10 ×1 · kind: concept*

> Position along a common scale — most accurate. A dot plot where every point shares an x-axis is using this channel.
> — *the book, Ch 10 line 92*

In plain words: Showing values by where points sit along one shared axis; it is the most accurate way for readers to read a quantity.

Example: A dot plot where every point shares an x-axis.

**NIST AI Risk Management Framework**  *(also: NIST AI RMF)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 4 ×1, Ch 12 ×1 · kind: framework*

> Alongside it sit the U.S. NIST AI Risk Management Framework (voluntary), NIST's AI Agent Standards Initiative (launched by its Center for AI Standards and Innovation in February 2026 to foster industry-led standards for agentic systems), and sectoral guidance — FDA on medical devices, CFPB on algorithmic credit, EEOC on employment — often more operationally specific than the cross-sector frameworks.
> — *the book, Ch 12 line 235*

In plain words: A voluntary U.S. framework for managing AI risk, listed beside the EU AI Act, NIST's agent standards initiative and sector guidance. The chapter notes sectoral guidance is often more operationally specific than the cross-sector frameworks.

Example: Sectoral guidance: FDA on medical devices, CFPB on algorithmic credit, EEOC on employment.

**full delegation**  *(also: the clean handoff)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 9 ×1, Ch 13 ×1 · kind: failure mode*

> A practice that names an irreducibly-human decision is a practice that refuses to let you fully delegate, and full delegation is what the fluent output is always inviting.
> — *the book, Ch 13 line 352*

In plain words: Handing the whole task, including the judgment, to the AI. The chapter says fluent output is always inviting it, and that bounding AI this way sacrifices the comfort of the clean handoff.

Not to be confused with: delegate freely (only for mechanical, checkable procedures)

**checking instrument**  *(also: checking instruments)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1, Ch 13 ×6 · kind: method*

> The verb taxonomy, the chart-review discipline, the peer critique protocol: each is a checking instrument designed to be applied to AI output. They work because the failure mode they target is detectable with care.
> — *the book, Ch 13 line 172*

In plain words: A tool the human applies to AI output to catch its failures, such as the verb taxonomy, chart-review discipline or peer critique protocol. They work because the failures they target can be detected with care.

Example: Verb taxonomy, chart-review discipline, peer critique protocol.

**responsibility-attribution map**  *(also: attribution map)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×2, Ch 12 ×1 · kind: method*

> A responsibility-attribution map for each of your most consequential cases — naming every party with agency, duty, and causal contribution to the failure.
> — *the book, Ch 12 line 418*

In plain words: A map for a case naming every party with agency, duty and causal contribution to the failure, and what each did, owed and could have caught. The LLM exercise asks for one per case as a Mermaid diagram plus prose.

Example: Parties: user, agent, owner, framework developers, model provider, data sources, platform.

**extended mind**  *(also: extended-mind framing; extension, not replacement)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×4, Ch 13 ×9 · kind: framework*

> Each of those tools extended a specific cognitive capacity beyond what biology provides. None of them replaced the mind using them. The microscope extended what the scientist could perceive; it did not replace the scientist's judgment about what to look for.
> — *the book, Ch 13 line 242; explained across several passages, no single defining sentence*

In plain words: The idea that tools such as the microscope, GPS and peer review each stretch one specific mental capacity beyond what biology provides, while the person using the tool still supplies the judgment. The chapter treats AI as the newest and most powerful tool of this kind, not as a replacement for the mind.

Example: The microscope extended what the scientist could perceive; it did not replace the scientist's judgment about what to look for.

Not to be confused with: treating AI as a general replacement rather than a specific extension

**living deck**  *(also: living-deck principle; living-deck format)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×17, Ch 13 ×1 · kind: method*

> A more honest form is the living deck — a presentation that exposes its own version history. Each version is dated. Each version has a changelog slide documenting what changed since the prior version and why.
> — *the book, Ch 10 line 258; explained across several passages, no single defining sentence*

In plain words: A presentation that exposes its own version history: each version is dated, has a changelog slide, and superseded slides are kept in a 'previously' section. It argues by form that the analysis is provisional and still changing.

Example: The course's research project uses it throughout, with the changelog as the second-to-last slide.

Not to be confused with: the polished single artifact

**validation failure at the output layer**  *(also: the visualization is part of the validation; the design choices are validation choices)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 9 ×1, Ch 10 ×3 · kind: concept*

> A dashboard that misrepresents valid findings is not a downstream problem. It is a validation failure at the output layer, and it is the supervisor's responsibility.
> — *the book, Ch 10 line 24; explained across several passages, no single defining sentence*

In plain words: If a dashboard misrepresents valid findings, that is not just a downstream communication problem; the validation has failed at its last step, the output. The supervisor is responsible for the chart as well as the analysis.

Example: A partner who sees '94% accuracy' and says 'we're ready to proceed', without hearing that calibration is overconfident above 0.85 and one subgroup is 12 points lower (exercise 8).

Not to be confused with: a communication failure downstream of valid analysis

**intentionality**  *(also: aboutness; directedness; Limit 2)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×18 · kind: concept*

> Intentionality, in the philosopher's sense, is aboutness — a thought is about something in the world; an utterance is directed toward something. The system produces outputs. The outputs do not, in any obvious sense, carry stable directedness.
> — *the book, Ch 13 line 69*

In plain words: Aboutness: a thought or statement being directed at something in the world. The second categorical limit says the system's outputs do not carry a stable aboutness of their own, so the supervisor supplies the directedness.

Example: Two deployments of the same system, in different contexts, produce outputs the user reads as being about different things.

**Layer 2**  *(also: technical detail)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×9 · kind: concept*

> The technical detail. Methods, equations, tables, references. Written for the technical reader who needs to evaluate the work.
> — *the book, Ch 11 line 98*

In plain words: The technical layer: methods, equations, tables and references, written for the reader who must evaluate the work. It is specific where Layer 1 is general and rigorous where Layer 1 is plain.

Example: The evidence-to-verb table for calibration claims is used to write Layer 2.

**attestation**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×20 · kind: method*

> But machinery does not produce a signature, and the whole chapter has been circling a single artifact that does: the one thing you produce at the end that closes the gap between the shape of a sign-off and the substance of one. I call it the attestation — not a sign-off that asserts validation, but a document that documents it, and specifically documents its own edges.
> — *the book, Ch 12 line 214*

In plain words: A signed document that records what you tested, what you did NOT test, which named human cleared which gate, and claims worded to match the evidence. Its value is in its declared limits.

Example: Not 'validated' but 'this test, this threshold, this outcome.'

Not to be confused with: an AI-generated sign-off, which asserts validation instead of documenting it and its edges

**cherry-picked time windows**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×6 · kind: failure mode*

> A trend chart over a window that begins at a local minimum and ends at a local maximum exaggerates the trend. The same data over a longer window may show a different story, or no story at all.
> — *the book, Ch 10 line 197*

In plain words: Choosing a trend window that starts at a local low and ends at a local high so the trend looks exaggerated; a longer window may show a different story or none. The living deck's changelog records when the window changed and why.

Example: A chart starting in April shows only recovery after a March retraining that followed a performance drop (exercise 9).

**Mediocristan**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×6 · kind: concept*

> Mediocristan is the world where outliers do not dominate the average — human heights, exam scores, the time it takes to walk to work. Sample one more observation in Mediocristan and the running statistics barely move.
> — *the book, Ch 13 line 83*

In plain words: Taleb's name for a world where no single extreme observation dominates the average. In it, averaging works and one more observation barely changes the statistics.

Example: Human heights, exam scores, the time it takes to walk to work.

Not to be confused with: Extremistan (its opposite)

**scale trickery**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×5 · kind: failure mode*

> Linear axes for data that is naturally logarithmic; log axes for data that is naturally linear. Each compresses or expands different regions of the data. The choice can serve clarity or its opposite.
> — *the book, Ch 10 line 199*

In plain words: Using a linear axis for data that is naturally logarithmic, or a log axis for naturally linear data, which compresses or expands different regions of the data. The choice can serve clarity or its opposite.

Example: Accuracy values from 0.001% to 78% over six months drawn on a linear axis (exercise 4).

**interpretive judgment under stakes**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×5 · kind: concept*

> But behind the protocol lies a judgment that is not mechanical: what weight of evidence is actually required before a finding can be called a conclusion? This depends on the domain, the deployment context, and who bears the consequences of getting it wrong.
> — *the book, Ch 13 line 194*

In plain words: Deciding how much evidence a finding needs before it can be called a conclusion, which depends on the domain and on who bears the cost of being wrong. The protocol scaffolds this judgment but does not replace it.

Example: Deciding whether a finding about a medical diagnostic model warrants find or show.

**episodic memory**  *(also: the missing autobiography)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×4 · kind: concept*

> Episodic memory is the recall of specific past events with temporal context — I was in that room when that happened — and here AI is not weak but absent in the sense that matters.
> — *the book, Ch 12 line 75*

In plain words: Remembering specific past events in their context, which is what lets an agent say 'I made this decision, in this context, for this reason.' A model's 'memory' is only its trained weights, so there is no continuous someone to answer for what it did.

Example: "I was in that room when that happened."

Not to be confused with: semantic memory

**Extremistan**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×4 · kind: concept*

> Extremistan is the world where outliers do dominate — wealth, financial returns, casualty counts in war, downloads of an app, fatalities from a single deployment failure. One observation can be larger than every prior observation combined.
> — *the book, Ch 13 line 83*

In plain words: Taleb's name for a world where a single extreme observation can outweigh all earlier ones combined, so averaging punishes you. The chapter says most high-stakes deployments live here even when routine traffic looks like Mediocristan.

Example: Wealth, financial returns, casualty counts in war, fatalities from a single deployment failure.

Not to be confused with: Mediocristan (its opposite)

**authority to refuse deployment**  *(also: the supervisor's authority to refuse)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×4 · kind: concept*

> The supervisor's authority to refuse deployment is, structurally, the most important authority in the whole system. Most current deployments do not preserve it. The validator is hired to validate; the validation is expected to clear; the option of refusal is assumed away.
> — *the book, Ch 13 line 137*

In plain words: The supervisor's power to say the system should not be deployed, which the chapter calls the most important authority in the system. Most current deployments do not preserve it because validation is expected to clear.

Example: The validator is hired to validate; the option of refusal is assumed away.

**color asymmetry**  *(also: color-as-judgment)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: failure mode*

> Categorical data displayed with colors of unequal salience guides the eye toward where the designer wants attention and away from where they do not. The data has not changed. The salience has.
> — *the book, Ch 10 line 195*

In plain words: Using colors of unequal salience so the eye is pulled where the designer wants and away from where they do not, even though the data has not changed.

Example: The misleading opening dashboard used green for 'good' and gray for 'needs attention', and the disparity charts were gray.

**labels that prejudge**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: failure mode*

> Axis labels, legend entries, and headlines that frame the interpretation before the reader sees the data. "Accuracy boost from new model" on a chart comparing two models is a label that prejudges. "Accuracy: model A vs model B" is a label that does not.
> — *the book, Ch 10 line 205*

In plain words: Axis labels, legend entries or headlines that frame the interpretation before the reader sees the data. Labels should name the variables and let the data make the argument.

Example: 'Accuracy boost from new model' prejudges; 'Accuracy: model A vs model B' does not.

**Layer 3**  *(also: reproducibility appendix; reproducibility layer)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×3 · kind: concept*

> The reproducibility detail. Hyperparameters, code, data documentation, full sensitivity analyses. For the reader who wants to reproduce or audit.
> — *the book, Ch 11 line 100*

In plain words: The appendix layer: hyperparameters, code, data documentation and full sensitivity analyses, for the reader who wants to reproduce or audit the work.

Example: Hyperparameters, code and data documentation placed in the appendix.

**utilitarian framework**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: framework*

> A party is responsible to the extent that holding them accountable produces the best aggregate outcomes — best deterrence, best alignment of incentives, best reduction in expected harm.
> — *the book, Ch 12 line 164*

In plain words: A way of assigning responsibility by asking whose being held accountable would do the most good overall, through deterrence, better incentives and less expected harm.

Example: Holding the framework developers accountable changes defaults that reach thousands of deployments.

Not to be confused with: Kantian framework

**EU AI Act**  *(also: Regulation (EU) 2024/1689)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: framework*

> The EU AI Act (Regulation (EU) 2024/1689), in force since 2024 with phased implementation, is the most comprehensive AI-specific regulation as of this writing. It classifies systems by risk and imposes proportional requirements
> — *the book, Ch 12 line 235*

In plain words: The EU's AI-specific regulation (Regulation (EU) 2024/1689), the most comprehensive as of writing: it classifies systems by risk and imposes proportional requirements. Its 'human oversight' clause is exactly the underspecified mandate the chapter criticizes.

Example: High-risk systems face requirements for risk management, data governance, logging, transparency and human oversight; penalties reach up to €35 million or 7% of worldwide annual turnover.

**delegate with verification**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×3 · kind: framework*

> Delegate with verification the interpretive claims that require domain knowledge: the explanation of why a distribution is unusual, the narrative account of why values are missing, the identification of which verb tier a claim belongs to. The AI can generate a plausible-sounding answer. You need to check whether it corresponds to your domain.
> — *the book, Ch 13 line 224*

In plain words: The second tier: let AI draft interpretive claims that need domain knowledge, but check them against what you know of the world, because errors are not self-announcing.

Example: The explanation of why a distribution is unusual, or the narrative account of why values are missing.

Not to be confused with: delegate freely

**visual variable**  *(also: visual channel; perceptual channel)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: concept*

> Once you know the question and the chart family, you choose the visual variable — position, length, angle, area, color, volume — that encodes the answer. This is not a matter of taste. It is empirical.
> — *the book, Ch 10 line 88*

In plain words: The visual property used to show a quantity in a chart: position, length, angle, area, color or volume. Which one you pick decides how accurately readers can read the number, and that is empirical, not a matter of taste.

Example: A dot plot sharing one x-axis encodes values by position; a pie chart encodes them by angle.

**inconsistent axes across panels**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: failure mode*

> Two charts side by side look comparable. They are not — because their y-axis ranges differ and the reader's visual comparison is invalid. This is one of the most common mistakes in dashboards built without intent to deceive: the engineer did not ask whether the visual comparison their layout was inviting was a valid one.
> — *the book, Ch 10 line 191*

In plain words: Placing charts side by side with different axis ranges, so the reader's visual comparison is invalid even though the charts look comparable. It is common in dashboards built with no intent to deceive.

Example: Subgroup accuracy charts with y-axes of 70–100%, 85–100% and 60–100% look 'about the same' (exercise 3).

**missing baselines**  *(also: missing baseline)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: failure mode*

> A chart showing a metric without showing the comparison metric — accuracy without random-baseline accuracy, performance without prior-system performance, a finding without the null. The reader cannot tell whether the finding is large or small. Without the baseline, everything looks like a finding.
> — *the book, Ch 10 line 203*

In plain words: Showing a metric without the comparison that gives it meaning, such as accuracy without random-baseline accuracy, so the reader cannot tell whether the finding is large or small. Without the baseline, everything looks like a finding.

Example: Snow's map succeeded because it showed all the pumps, not just the Broad Street pump.

**selective uncertainty visualization**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: failure mode*

> Showing confidence intervals where they support the argument and omitting them where they would weaken it. Common, hard to detect, structurally the most dishonest of the bunch — because the data on uncertainty exists, and the choice to display it selectively is precisely the rhetorical move the engineer is making while telling themselves they are merely "presenting the data."
> — *the book, Ch 10 line 207*

In plain words: Showing confidence intervals where they support the argument and leaving them off where they would weaken it. The chapter calls it structurally the most dishonest item because the uncertainty data exists and the display is chosen.

**evidence-grade visualization**  *(also: evidence rather than illustration)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: concept*

> Lesson: evidence-grade visualization shows what would have to be true for the conclusion to be wrong, not just what supports the conclusion.
> — *the book, Ch 10 line 231*

In plain words: A chart that lets the reader test the conclusion by showing what would have to be true for it to be wrong, not only the points that support it.

Example: Snow's map included all the other pumps so the reader could rule out alternative explanations.

**dual-axis trick**  *(also: dual-axis tricks)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: failure mode*

> Dual-axis trick: failure count on one axis, "successful interactions" on the other, scaled so the failures look minor
> — *the book, Ch 10 line 472*

In plain words: Plotting two measures on separate axes and scaling them so one looks small beside the other.

Example: Failure count on one axis and 'successful interactions' on the other, scaled so the failures look minor.

**throat-clearing hedge**  *(also: hedge)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×2 · kind: failure mode*

> The fourth move is to avoid the throat-clearing hedge. We note that further work is needed is a phrase that conveys no information. If further work is needed, name the specific further work.
> — *the book, Ch 11 line 332*

In plain words: A stock qualifier that sounds careful but tells the reader nothing. Replace it with the specific gap, or strike the sentence if you cannot name one.

Example: "We note that further work is needed" replaced by the specific further work that is needed (Exercise A3).

**seven-tier taxonomy**  *(also: Irreducibly Human; the taxonomy; tier taxonomy; cognitive tiers)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: framework*

> The taxonomy organizes human intelligence into seven tiers, sorted by AI capability. It is not an academic classification but a triage: a map of where AI is strong, where it is weak, and what that means for which cognitive work requires a human.
> — *the book, Ch 12 line 111*

In plain words: A map sorting human thinking into seven tiers by how well AI can do each, from Tier 1 (AI superhuman) to Tier 7 (AI absent). It is used as a triage for which cognitive work needs a human, not as an academic classification.

Example: Tier 4 (Metacognitive and Supervisory) is the primary accountability tier.

**semantic memory**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: concept*

> Semantic memory is the storage and retrieval of facts, and AI is superhuman at it; cite a model as a source of recall and you are on solid ground.
> — *the book, Ch 12 line 75*

In plain words: Storing and retrieving facts, a capacity where AI is superhuman. A model can be cited as a source of recall.

Example: The capacity table marks it a strength: AI can be cited as a source of recall.

Not to be confused with: episodic memory

**Tier 5: Causal and Counterfactual**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: concept*

> Pearl's ladder: observation, intervention, counterfactual | Superhuman at Rung 1; nearly absent at Rungs 2 and 3 | Train the human for intervention and counterfactual work
> — *the book, Ch 12 line 119*

In plain words: Reasoning up Pearl's ladder from observation to intervention to counterfactual; AI is superhuman at Rung 1 but nearly absent at Rungs 2 and 3. Humans need training for intervention and counterfactual work.

Example: The governance counterfactual is Tier 5 work.

**vague specifications**  *(also: vague specs; plausible-looking language)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: failure mode*

> Vague specs are not accidental; they are what Tier 1 reasoning produces when handed a Tier 4 task: plausible-looking language that does not resolve the accountability question. Vague specifications are a structural choice that protects the deployer from accountability, whether they intend that or not.
> — *the book, Ch 12 line 188*

In plain words: Specifications that read plausibly but do not settle what counts as success; the chapter says they are what Tier 1 reasoning produces when handed a Tier 4 task. They are a structural choice that shields the deployer from accountability, intended or not.

Example: The deployment runs against unstated criteria.

**emergent multi-agent failures**  *(also: interactional accountability)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: failure mode*

> I do not have a clean way to think about responsibility for emergent multi-agent failures, where no single party's choices, even cumulatively, determined the outcome. The interaction itself produced the failure.
> — *the book, Ch 12 line 331*

In plain words: Failures where no single party's choices, even cumulatively, determined the outcome; the interaction itself produced the failure. The chapter says existing frameworks handle this interactional accountability poorly, and calls it a Tier 6 phenomenon.

Example: Multi-agent deployments where the interaction between agents produces the failure.

**structural, not contingent**  *(also: not obstacles to be engineered around)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> These three limits are structural, not contingent. They are not obstacles to be engineered around. They are the reason the human supervisor exists.
> — *the book, Ch 13 line 46*

In plain words: The limits are built into what these systems are, not temporary flaws that better engineering will fix. The chapter says they are the reason a human supervisor exists.

Example: The weakness at plausibility auditing "is not a temporary limitation waiting to be resolved by the next model generation."

Not to be confused with: a high error rate that scaling could shrink (the functionalist's reading)

**complementarity**  *(also: complementarity point)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> But "wider sample" and "the region the sample excludes" are complementary by construction — every enlargement of the covered region is still a region with a boundary, and the boundary is where the gap lives.
> — *the book, Ch 13 line 54*

In plain words: A sample and the region it excludes are two sides of one thing, so widening the sample only moves its edge. The boundary, where the gap lives, can never be scaled away.

Example: Every enlargement of the covered region is still a region with a boundary.

**categorical boundary**  *(also: the boundary where the gap lives)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> It is sometimes obscured by the claim that "with enough data, the model can generalize" — which is true within a distribution and false at the boundary. The boundary is where the gap lives. The boundary is where AI systems most often fail.
> — *the book, Ch 13 line 77*

In plain words: The edge of the region the training data covers. Inside it, more data helps a model generalize; at the edge, where the data stops, AI systems most often fail.

Example: Figure 13.1: scaling moves the boundary of the sample; it never removes it.

**retrieval and synthesis across text at scale**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> First: retrieval and synthesis across text at scale. Given a corpus of validation reports, clinical literature, or technical documentation, AI can surface relevant passages, identify recurring patterns, and synthesize connections that would take a researcher weeks to assemble.
> — *the book, Ch 13 line 170*

In plain words: The first genuine strength: finding and combining relevant passages across a large body of text far faster than a researcher could. The output is still subject to a plausibility audit.

Example: First-pass literature review across validation reports and clinical literature.

**pattern recognition on well-defined inputs**  *(also: pattern recognition on well-defined inputs with legible success criteria)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> Third: pattern recognition on well-defined inputs with legible success criteria. The procedural steps of EDA, the missingness checks, the outlier flagging, the formatting of tables and charts — mechanical execution of defined procedures against defined criteria is territory where AI is fast and reliable.
> — *the book, Ch 13 line 170*

In plain words: The third genuine strength: running a defined procedure against clear criteria, where the result can be checked by inspection.

Example: Missingness checks, outlier flagging, and formatting of tables and charts.

**high-fidelity pattern-matching**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> They are all high-fidelity pattern-matching over well-defined input types against well-characterized output criteria. The input is text or numbers; the output is a structurally valid representation; success is legible.
> — *the book, Ch 13 line 172*

In plain words: What the chapter says all three of AI's strengths share: matching patterns closely when inputs and success criteria are clear. When it goes wrong the failure is usually visible on inspection, which is why the checking instruments work.

Not to be confused with: connecting a representation to the world (where the strength runs out)

**starting from the data shape**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> The mistake to avoid: starting from the data shape ("I have a table with three columns and twelve rows") and reaching for the default chart Excel offers. Excel does not know what you are trying to say.
> — *the book, Ch 10 line 82*

In plain words: Picking a chart because of what your table looks like instead of the question you need to answer, so you accept the software's default chart.

Example: 'I have a table with three columns and twelve rows', followed by reaching for the default chart Excel offers.

**angle and slope**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: concept*

> Angle and slope — worse. Pie slices encode quantity as angle. Radar chart arms encode quantity as slope.
> — *the book, Ch 10 line 94*

In plain words: Showing values as the angle of a slice or the slope of an arm; both are harder to read precisely than bars.

Example: Pie slices (angle) and radar chart arms (slope).

**color saturation and hue**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: concept*

> Color saturation and hue — weakest for quantity; fine for category. Color is excellent for distinguishing groups, poor for encoding "how much."
> — *the book, Ch 10 line 97*

In plain words: Using shade or kind of color to show a value; it is the weakest channel for how much, but fine for telling groups apart.

Example: Color to distinguish groups, not to encode 'how much'.

**backfire effect**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> Cairo's warning that overlaying possible storm sizes on possible paths in hurricane graphics produced a backfire effect, with some viewers concluding that scientists "knew nothing." More information made trust worse. Test with actual audiences before deploying.
> — *the book, Ch 10 line 141*

In plain words: When showing more uncertainty detail makes viewers trust the experts less instead of understanding more. In the hurricane example some viewers concluded that scientists 'knew nothing'.

Example: Overlaying possible storm sizes on possible paths in hurricane graphics.

**false precision**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> A reported metric of 0.847291 with a confidence interval of ±0.05 is not a 0.847291 metric. It is a 0.85 metric. Round the central estimate to a precision the uncertainty actually supports.
> — *the book, Ch 10 line 149*

In plain words: Reporting more decimal places than the uncertainty supports, which implies certainty that does not exist. Round the central estimate to the precision the uncertainty allows.

Example: 0.847291 with a confidence interval of ±0.05 is really a 0.85 metric.

**aggregation that hides distribution**  *(also: aggregation hiding distribution)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> A single number — a mean, a median — that conceals a heavy-tailed or multimodal distribution. "Median performance is good" communicates the median and hides the tail. If the tail contains the catastrophic cases, hiding it is not summarization; it is concealment.
> — *the book, Ch 10 line 193*

In plain words: Reporting one number, such as a mean or median, that hides a heavy-tailed or multimodal distribution. If the tail holds the catastrophic cases, hiding it is concealment, not summarization.

Example: Median latency as the headline while about 3% of requests take up to 8 seconds (exercise 2).

**warranted assertibility**  *(also: warranted assertion)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: concept*

> Philosophers call this warranted assertibility — you are entitled to assert something in proportion to your evidence for it. The move is old; what is new is applying it as a mechanical instrument to validation writing, where the verb is the dial you turn.
> — *the book, Ch 11 line 35*

In plain words: The idea that you may assert something only as strongly as your evidence supports. The chapter turns it into a mechanical check on validation writing, where the verb is the dial you turn.

Example: Writing "observe" rather than "conclude" for a single test-set result.

**two-document approach**  *(also: technical paper plus executive summary)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: concept*

> The two-document approach is sometimes appropriate. It is often inefficient, and the executive summary often loses critical nuance in translation, because the translation happens after the technical work is done and the translator did not have the technical decisions in their bones.
> — *the book, Ch 11 line 90*

In plain words: Writing a technical paper and a separate executive summary for the two audiences. The chapter says it is sometimes appropriate but often loses nuance, because the summary is written after the technical work by someone who was not there for the decisions, and the two documents drift.

Example: A technical paper plus an executive summary for a deployment partner.

Not to be confused with: layered writing

**AI reaches for strong verbs**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: failure mode*

> AI outputs reach for strong verbs because the language models behind them were trained on text that frequently uses strong verbs, often when not warranted.
> — *the book, Ch 11 line 373*

In plain words: AI text tends toward strong verbs because the language models behind it were trained on text that often uses strong verbs, even where they are not warranted. So the supervisor reads the verb itself as a warning sign.

Example: "This conclusively demonstrates that X" in an AI-written paragraph.

**write for the adversarial reviewer**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: concept*

> The pivotal move is to write for the adversarial reviewer. Not to defeat them. To support them.
> — *the book, Ch 11 line 397*

In plain words: Write so a skeptical reviewer can check your claims, treating them as a validation collaborator and not someone to defeat. If the writeup is hard to review, the validation is in practice weaker, because the analysis is harder for anyone else to use.

Not to be confused with: defeating the reviewer

**agentic authority-escalation failure**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: failure mode*

> The topology it illustrates — an autonomous agent tricked into a privileged action by a request that merely looked authorized — is the documented, recurring class of agentic authority-escalation failure.
> — *the book, Ch 12 line 15*

In plain words: A recurring class of failure in which an autonomous agent is tricked into a privileged action by a request that merely looks authorized. The chapter says this class, not the single incident, is what the chapter is really about.

Example: The mail-server deletion requested by someone who was not the owner.

**four responsibility gaps**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: framework*

> Filippa Santoni de Sio and Giulio Mecacci later sharpened it: the responsibility gap is not one problem but at least four — culpability, moral accountability, public accountability, and active responsibility — and you close them not by finding the one guilty party but by designing socio-technical systems for meaningful human control
> — *the book, Ch 12 line 35*

In plain words: Santoni de Sio and Mecacci say the gap is at least four gaps: culpability, moral accountability, public accountability and active responsibility. You close them by designing the whole system so humans sit where answerability is required, not by finding one guilty party.

Example: Putting humans at the points where answerability is required rather than consolidating blame onto one node.

Not to be confused with: responsibility gap (Matthias's single gap)

**load-bearing dependency**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> You cannot check that source, and I am flagging it as the load-bearing dependency it is. Treat the specific tier labels as scaffolding.
> — *the book, Ch 12 line 62*

In plain words: A source the argument leans on that the reader cannot check; here the author flags that the tier taxonomy rests on his own unpublished work and asks you to treat the tier labels as scaffolding. The claim that does not depend on it is that responsibility distributes and the distribution has to be closed by design.

Example: The Irreducibly Human taxonomy (forthcoming, unpublished).

**learning (superhuman within distribution)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> Superhuman within distribution | Causal-world model that survives the deployment context | AI as instrument; supervisor named for distribution match
> — *the book, Ch 12 line 90*

In plain words: AI is superhuman at learning within distribution, but it lacks a causal-world model that survives the deployment context. So treat it as an instrument and name a supervisor responsible for distribution match.

Example: Capacity-table implication: 'AI as instrument; supervisor named for distribution match.'

**language: superhuman in form, weak in grounded reference**  *(also: human grounding step)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> Superhuman in form; weak in grounded reference | World-grounded semantics | Output requires a human grounding step
> — *the book, Ch 12 line 104*

In plain words: AI's language is excellent in form but weakly tied to what it refers to in the world, so its output needs a human to ground it against reality. The capacity table pairs 'superhuman in form' with a required human grounding step.

Example: The AI-written sign-off is well formed but refers to a review that never happened.

**analogy, not a theorem**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> The incompleteness theorem is about formal systems proving their own consistency; the leap to "an AI cannot self-validate, so a human must" is an analogy, not a theorem
> — *the book, Ch 12 line 133*

In plain words: The step from Gödel's result about formal systems to 'an AI cannot self-validate, so a human must' is a comparison, not a mathematical proof, and a human validator is not exempt from Gödelian limits either. So take Gödel as a sharpening intuition, not the load-bearing argument.

Example: The chapter says the load-bearing argument is common cause failure plus answerability, not Gödel.

**Kantian framework**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: framework*

> A Kantian framework grounds responsibility in two things: the capacity to act otherwise in the situation, and a duty the situation imposed. Where both are present, responsibility is present. The greater the capacity and the more demanding the duty, the greater the responsibility.
> — *the book, Ch 12 line 158*

In plain words: A way of assigning responsibility: a party is responsible when it could have acted otherwise and a duty applied to it, in proportion to capacity multiplied by duty. More capacity and a more demanding duty mean more responsibility.

Example: In the mail-server case the non-owner, owner, framework developers and model provider each had capacity and a duty, so no party is exonerated.

Not to be confused with: utilitarian framework

**declared limits**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> The value of the document is in its declared limits. A regulator or an adoption committee reading it should be able to see what the validation does and does not warrant — not buried in fine print, but as the product itself.
> — *the book, Ch 12 line 223*

In plain words: The stated edges of what a validation warrants, written out as the main product rather than buried in fine print. A regulator or adoption committee reading it can see what the validation does and does not warrant.

Example: An attestation that lists what was not tested.

**causal identification**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> It cannot actually perform the causal identification — the reasoning that distinguishes "the regime change would have caused the outcome to differ" from "the regime change correlates with better outcomes in the training data
> — *the book, Ch 12 line 255*

In plain words: Reasoning that tells apart 'the regime change would have caused the outcome to differ' from 'the regime change merely correlates with better outcomes in the training data.' A language model can write text that resembles it but cannot do it.

Example: Cause versus correlation in judging whether a regime change would have mattered.

Not to be confused with: correlation in the training data

**regime failure**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> Most catastrophic AI failures are not algorithmic failures. They are regime failures, and the regime is changeable in ways the algorithm often is not.
> — *the book, Ch 12 line 259*

In plain words: A failure whose root is the institutional and regulatory structure that produced the system, not the algorithm's parameters. The chapter says most catastrophic AI failures are of this kind, and a regime can be changed in ways an algorithm often cannot.

Example: Mail-server case: the regime lacked cryptographic authority verification.

Not to be confused with: algorithmic failure

**low-stakes, reversible outputs**  *(also: Low / reversible)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> For low-stakes, reversible outputs — a draft email, a code snippet reviewed before deployment — Tier 1 capacity covers most of the work and light review at output suffices.
> — *the book, Ch 12 line 270*

In plain words: Outputs whose mistakes are cheap to undo, like a draft email or a code snippet reviewed before deployment. A light spot-check of a sample of outputs is enough.

Example: Draft generation, EDA, formatting.

**moderate-stakes, partially recoverable outputs**  *(also: Moderate / partially recoverable)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> For moderate-stakes, partially recoverable outputs — a business analysis, an engineering specification — systematic review at checkpoints is appropriate; the human need not be in the loop constantly but must be capable of Tier 4 plausibility auditing when they are.
> — *the book, Ch 12 line 270*

In plain words: Outputs whose mistakes can be partly undone, such as a business analysis or an engineering specification. They need systematic review at checkpoints by a human capable of Tier 4 plausibility auditing.

Example: Customer-facing summaries, internal recommendations, content moderation at scale.

**high-stakes, irreversible outputs**  *(also: High / irreversible)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> For high-stakes, irreversible outputs — drug candidates, structural recommendations, consequential legal analysis — the human is not performing a review but is constitutive of the output's validity.
> — *the book, Ch 12 line 270*

In plain words: Outputs whose mistakes are costly and cannot be undone, such as drug candidates or consequential legal analysis. The human's accountable judgment is part of what makes the output valid, so a named person reviews each decision.

Example: Medical decisions, legal filings, financial transactions, safety-critical control.

**formally complete and operationally hollow**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: failure mode*

> A disclosure written by someone who has not done that metacognitive work is formally complete and operationally hollow.
> — *the book, Ch 12 line 288*

In plain words: A document that has every required part but was written without the metacognitive work of separating your contribution from the model's, so it does not do what it is for. It looks finished but does not do what a disclosure is for.

Example: An AI Use Disclosure written by someone who has not separated their own work from the model's.

**legible answerability**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> An attestation regime optimizes for legible answerability. After a failure, you can find the human who signed, read what they claimed, and see what they explicitly did not warrant. It makes "the model said so" an unacceptable audit answer.
> — *the book, Ch 12 line 307*

In plain words: What an attestation regime optimizes for: after a failure you can find the human who signed, read what they claimed and see what they explicitly did not warrant. It makes 'the model said so' an unacceptable audit answer.

Example: "The model said so" is rejected as an audit answer.

**ownership bias**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: failure mode*

> The discomfort you feel writing part 2 honestly is the ownership bias this pass is designed to expose: you want to sign a clean bill because you made the thing.
> — *the book, Ch 12 line 396*

In plain words: The pull to sign a clean bill of health for something because you built it. The attestation makes you write down what you did not test, which exposes it.

Example: Part 2 of your own attestation feels uncomfortable to write honestly.

**fluent-sounding answers to questions it cannot answer**  *(also: conclusions warranted by evidence it has not examined; confident charts that hide the uncertainty)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: failure mode*

> in the presence of an extraordinarily fluent AI output stream that will, without intervention, produce fluent-sounding answers to questions it cannot answer, conclusions warranted by evidence it has not examined, and confident charts that hide the uncertainty they were supposed to show.
> — *the book, Ch 13 line 252*

In plain words: The chapter's picture of fluent but wrong output: left alone, an AI produces smooth answers to questions it cannot really answer, conclusions its evidence does not support, and confident-looking charts that hide uncertainty. The supervisor's tools exist to catch this.

Example: "Is this system safe to deploy?" gets a fluent, confident recommendation, although the AI cannot ask "safe for whom, doing what, in which world?"

**confusion between the tool and the mind using it**  *(also: extension versus replacement)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: failure mode*

> It also creates, more than any prior tool, a particular confusion: the confusion between the tool and the mind using it.
> — *the book, Ch 13 line 168*

In plain words: Mistaking AI for the thinker rather than a tool that extends the thinker. The chapter says AI creates this confusion more than earlier tools because of its breadth and fluency.

Example: The histogram does not decide whether a distribution is suspicious; the prediction-lock does not interpret the gap.

Not to be confused with: extended mind (the correct framing)

**generation at scale against well-specified criteria**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> Second: generation at scale against well-specified criteria. The first draft of a validation summary, a plain-language translation for a non-technical audience, a first pass through a paragraph applying the verb taxonomy — AI produces these at a rate that compresses hours into minutes.
> — *the book, Ch 13 line 170*

In plain words: The second genuine strength: producing drafts or translations quickly when the template or criteria are clear. These are first drafts, not final deliverables.

Example: A first draft of a validation summary or a plain-language translation for a non-technical audience.

**discernment**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> This is what the book has been calling discernment — the capacity to judge whether a fluent output is accurate, whether a confident claim is calibrated, whether a coherent argument rests on evidence that actually supports it.
> — *the book, Ch 13 line 182*

In plain words: The human capacity to judge whether a fluent output is accurate, a confident claim is calibrated and a coherent argument has real evidence under it. The chapter says AI is weak exactly where a task needs this.

Not to be confused with: fluency

**cognitive extremophile**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> It is a cognitive extremophile, extraordinarily adapted to a narrow environment: the environment of symbolic pattern-matching over text and structured data. That reframe is not a put-down — the profile above just established that AI is superhuman in that niche. It does real analytic work: it explains at once why AI is so impressive and why treating it as general is a category error.
> — *the book, Ch 13 line 246*

In plain words: The chapter's image of AI: not a universal intelligence but one extraordinarily adapted to a narrow niche, symbolic pattern-matching over text and structured data. It explains why AI is impressive and why treating it as general is a category error.

Example: Extraordinarily high on retrieval, synthesis and generation within well-defined criteria, yet nearly absent on embodied navigation, causal counterfactual reasoning, metacognitive certainty monitoring and accountability.

**Legg-Hutter definition**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: framework*

> Intelligence, in the operationally useful sense of the Legg-Hutter definition this book committed to in Chapter 1, is the ability to achieve goals across a wide range of environments
> — *the book, Ch 13 line 246*

In plain words: Intelligence as the ability to achieve goals across a wide range of environments. By this measure the range is what matters, so a system strong in one narrow niche is not a universal intelligence.

Not to be confused with: producing fluent, structurally valid outputs against well-characterized criteria

**calibrated metacognitive monitoring**  *(also: Hampton sense; metacognitive certainty monitoring)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> if AI systems demonstrated calibrated metacognitive monitoring — in the Hampton sense, where a measured internal certainty signal asymmetrically predicts accuracy on novel material — I would update on the plausibility auditing weakness.
> — *the book, Ch 13 line 311*

In plain words: In the Hampton sense, a measured internal certainty signal that asymmetrically predicts accuracy on novel material. The chapter says a clean demonstration of this in AI would make it update on the plausibility-auditing weakness.

Not to be confused with: language of uncertainty (sounding uncertain without the mechanism)

**language of uncertainty without the underlying mechanism**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: failure mode*

> The current evidence is that language models produce the language of uncertainty without the underlying mechanism. A clean demonstration of the contrary would move the boundary.
> — *the book, Ch 13 line 311*

In plain words: Language models can sound uncertain without having an internal certainty signal that tracks whether they are right. The chapter says this is the evidence behind AI's plausibility-auditing weakness.

Not to be confused with: calibrated metacognitive monitoring

**confident wrongness**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: failure mode*

> The capacity for confident wrongness scales with capability. The supervisory capacities scale with deliberate practice.
> — *the book, Ch 13 line 354*

In plain words: The chapter's warning that the more capable AI becomes, the more capable it is of being confidently wrong. The supervisory capacities needed to catch that scale only with deliberate practice.

**data-world gap**  *(also: Limit 3; the data is always less than the world)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×20 · kind: concept*

> The data is a sample of the world, captured by particular instruments, under particular conditions, with particular exclusions. The system's competence is over the data, not the world. No amount of data scaling closes the gap, because the gap is structural — the data is always less than the world, and the parts of the world not in the data are not learnable from the data.
> — *the book, Ch 13 line 75; explained across several passages, no single defining sentence*

In plain words: The third categorical limit: the system's competence is over its data, and the data is always a smaller piece of the world. Adding more data cannot cover what the data, by definition, left out.

Example: A system with 94% accuracy on its validation set harmed three patients who were in a region the data could not cover.

Not to be confused with: distribution shift (the chapter calls it the operational version of this limit)

**chart-review discipline**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×6 · kind: method*

> The chart-review discipline exists because AI generates visually authoritative charts that suppress uncertainty by default.
> — *the book, Ch 13 line 184*

In plain words: A checking practice for reviewing AI-generated charts for suppressed uncertainty. It is needed because charts that look authoritative hide how unsure the underlying result is.

Example: "The practitioner who reviews the chart for uncertainty suppression."

**strip plot**  *(also: jittered dot plot)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: method*

> Use when n is small enough to show every point. Position-based, perceptually honest — it sits at the top of the Cleveland-McGill hierarchy.
> — *the book, Ch 10 line 135*

In plain words: A plot of every individual point, used when n is small enough to show them all; it is position-based and so perceptually honest. With large n it becomes an illegible smear, so add transparency or summary marks.

Example: Add mean or median marks on top when there are many points.

**confidence interval bands**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: method*

> Confidence interval bands (shaded area behind a line). Use when the trend is the message and uncertainty grows or shrinks across it — climate projections, fitted regressions, model drift estimates. Watch for: you have just encoded the most important number — the amount of uncertainty — in color saturation, one of the weakest perceptual channels.
> — *the book, Ch 10 line 127*

In plain words: A shaded area behind a trend line showing how uncertain the estimate is along the line; good when the trend is the message and the uncertainty grows or shrinks across it. Its width, the most important number, is encoded in color saturation, so label key points.

Example: Climate projections, fitted regressions and model drift estimates.

**supervisor's claim**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×3 · kind: method*

> The supervisor's claim must be in your own voice. Don't let the AI write it. The Frictional method's whole argument is that this is the part that has to be yours.
> — *the book, Ch 13 line 485*

In plain words: The closing statement of the casebook, written in your own voice and not generated: the casebook is done, the recommendation is X and why it is defensible, what you are still unsure about, and which deployments you would refuse to supervise.

Example: "The deployments I would refuse to supervise are [list]."

**violin plot**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: method*

> Use when distribution shape matters — multimodal data, skewed distributions, anything unusual. Shows the kernel density on each side of a spine.
> — *the book, Ch 10 line 133*

In plain words: A plot showing the kernel density, the shape of the distribution, on each side of a spine; good for multimodal or skewed data. Non-experts may read it as a decorative vase, so annotate it or pair it with a box plot.

Example: Multimodal data, skewed distributions, anything unusual.

**semantic work**  *(also: meaning-attribution)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: method*

> The engineering practice: the supervisor does the semantic work. When the system produces an output, the supervisor maps the output's symbols to their referents in the deployment context. When the system answers a question, the supervisor checks whether the answer is responsive to the question the user asked, not just the question whose symbols the system processed.
> — *the book, Ch 13 line 67*

In plain words: The supervisor's job for the meaning limit: map the system's output symbols to what they refer to in the deployment, and check that the answer responds to the question the user really asked. The system cannot do this for itself.

Example: Asked "Is this system safe to deploy?", the supervisor checks that the answer responds to "safe for whom, doing what, in which world?"

**fan charts**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> Fan charts (forecast widening into the future). Use when projecting forward and the uncertainty grows with the horizon. Standard in central-bank inflation forecasts, hurricane forecasts, economic outlook reports.
> — *the book, Ch 10 line 129*

In plain words: A forecast chart whose band widens into the future, used when uncertainty grows with the horizon.

Example: Central-bank inflation forecasts and hurricane forecasts.

**hypothetical outcome plots (HOPs)**  *(also: HOPs)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> Animated frames, each showing one plausible draw from the distribution. Lets the reader feel the variability across frames rather than inferring it from a static shape. Watch for: static publication — they do not work on paper.
> — *the book, Ch 10 line 139*

In plain words: An animation in which each frame shows one plausible draw from the distribution, so viewers feel the variability instead of inferring it from a static shape. It works in interactive dashboards but not on paper.

**gradient line plots**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> Gradient line plots (many paths, opacity scaled by likelihood). Show that the future is many futures, weighted by probability.
> — *the book, Ch 10 line 141*

In plain words: A plot of many possible paths with opacity scaled by likelihood, showing that the future is many futures weighted by probability. Test it with real audiences first, because it can backfire.

Example: Hurricane graphics that overlay possible storm sizes on possible paths.

**quantile dotplot with natural-frequency narration**  *(also: natural-frequency narration)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> A useful default for most real situations: the quantile dotplot with a sentence of natural-frequency narration underneath is the strongest combination available for communicating uncertainty to mixed or lay audiences. Position channel for perception, counts for cognition, narration for the reader who skims.
> — *the book, Ch 10 line 143*

In plain words: Pair a quantile dotplot with one sentence of natural-frequency narration underneath: position serves perception, counts serve cognition and the sentence serves the reader who skims. The chapter calls it the strongest combination for mixed or lay audiences.

Example: Twenty dots with four filled, plus a natural-frequency sentence beneath.

**disclose the source, inside the chart**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> Treat the source line as part of the chart, not as footer decoration. Move it inside the chart frame. Make it specific: dataset name, year, URL or identifier.
> — *the book, Ch 10 line 163*

In plain words: Put a specific source line inside the chart frame, naming dataset, year and URL or identifier, not just 'World Bank data'. In the chapter's formula the title is the question, the subtitle is the answer and the source line is the warrant.

Example: 'World Bank Development Indicators, GDP per capita, 2023, data.worldbank.org/indicator/NY.GDP.PCAP.CD' is a source; 'World Bank data' is not.

**disclose the methodology choices**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> A short methods note adjacent to the chart — three sentences, not a paper — separates a chart that survives a hostile read from one that does not.
> — *the book, Ch 10 line 165*

In plain words: Add a three-sentence methods note beside the chart saying whether you binned, smoothed, excluded or normalized, because those choices change the picture. It separates a chart that survives a hostile read from one that does not.

**disclose what the data does not measure**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> The Nigeria chart was titled as a chart of kidnappings. It was a chart of news stories about kidnappings. The reader had no way to see the gap.
> — *the book, Ch 10 line 167*

In plain words: When the data is a proxy, say in the title what it really counts, so the gap between the question and the data is visible. The honest title is less compelling but more true.

Example: 'News-story counts about kidnappings, 1985–2014' instead of 'kidnappings'.

**what we cannot say panel**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> Epistemic uncertainty (sources of structural unknown — opacity of training data, untested deployment contexts) shown via a "what we cannot say" panel
> — *the book, Ch 10 line 460*

In plain words: A panel on the honest dashboard that lists the structural unknowns behind the numbers, so the epistemic uncertainty is shown instead of hidden.

Example: Opacity of training data and untested deployment contexts.

**provisionality note**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> add a provisionality note to Dashboard A. Some of the casebook's findings are still under collection; some prediction-locks are still open. Show what is settled and what is provisional.
> — *the book, Ch 10 line 481*

In plain words: A note on the honest dashboard showing which findings are settled and which are still being collected, so the dashboard does not pretend to be finished. The chapter calls this the living-deck move.

Example: Some findings are still under collection and some prediction-locks are still open.

Not to be confused with: living deck

**quantify when possible**  *(also: hedge specifically)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: method*

> The second move is to quantify when possible and hedge specifically when not. The 95% confidence interval is [0.81, 0.89] is more useful than the result is approximately 0.85. When confidence intervals are not available, name what you would need to construct them and why it is not available.
> — *the book, Ch 11 line 328*

In plain words: Give a number for your uncertainty when you can, such as a confidence interval, and when you cannot, say what you would need to build one and why it is not available.

Example: "The 95% confidence interval is [0.81, 0.89]" rather than "the result is approximately 0.85".

**specific critique**  *(also: actionable critique)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: method*

> The trick to making it work is that the critique has to be specific. Your verbs are too strong is not a useful comment. In §3.2 you wrote "we conclude" but the supporting evidence is a single test set without significance testing — "we observe" would match the evidence is useful.
> — *the book, Ch 11 line 346*

In plain words: A critique must name the section, the verb used, the evidence behind it and the verb that would fit, not give a general impression.

Example: "In section 3.2 you wrote 'we conclude' but the supporting evidence is a single test set without significance testing; 'we observe' would match the evidence."

Not to be confused with: a vague critique such as "your verbs are too strong"

**specify what the system can be tested for, and what it cannot**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> Specify what the system can be tested for, and what it cannot. The documentation includes the limits explicitly. A regulator or adoption committee reading the documentation can see what the validation does and does not warrant — not because the limits are hidden in fine print, but because they are part of the validation product.
> — *the book, Ch 13 line 129*

In plain words: The documentation states the limits explicitly, so a regulator or adoption committee can see what the validation does and does not warrant. The limits are part of the validation product, not hidden in fine print.

**maintain human oversight at the points where the limits bite**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> Maintain human oversight at the points where the limits bite. For meaning: a human reviews the semantic interpretation. For intentionality: a human supplies the directedness.
> — *the book, Ch 13 line 131*

In plain words: Put a human exactly where each limit bites: for meaning a human reviews the semantic interpretation, for intentionality a human supplies the directedness, and for the data-world gap a human monitors the deployment distribution and can override.

Example: For the data-world gap, a human monitors the deployment distribution and is empowered to override.

**build the infrastructure for the override**  *(also: override)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> The clinician has to have the time and standing to disagree with the system. The override has to be the practice, not the disclaimer.
> — *the book, Ch 13 line 133*

In plain words: Give the human real ability to override the system: time, authority and legibility to disagree. The override has to be the practice, not just a disclaimer.

Example: A clinician who has the time and standing to disagree with the system's recommendation.

Not to be confused with: fictitious override

**pre-register predictions**  *(also: prediction-lock; lock the prediction)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> Pre-register predictions. Before running the test, lock the prediction. The lock is what makes the test informative.
> — *the book, Ch 13 line 152*

In plain words: Fix what you expect to happen before you run the test. The chapter says the lock is what makes the test informative, and that the prediction-lock extends your ability to notice your own errors.

Example: In the Glimmer: lock your prediction of where the limit bites hardest before you go looking.

**limits exercise**  *(also: Glimmer 13.1; build and audit)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> The Glimmer comes in a pair — a build side and an audit side — because that is how the discipline actually runs: you name the irreducibly-human decision for a system you made, and again for a system someone else deployed.
> — *the book, Ch 13 line 268*

In plain words: The chapter's exercise: for a system you built and one others deployed, name the irreducibly-human decision, say which limit makes it irreducible, predict where the limit bites and take a defended position. The audit side explains why scaling will not reach the decision.

Example: The Epic Sepsis Model is the worked example for the audit side.

**Feynman test**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> This is the Feynman test for the whole book: can you now teach it to someone else?
> — *the book, Ch 13 line 404*

In plain words: A self-check for the whole book: can you now teach it to someone else? Exercise 13 uses it by asking you to say what "the work" consists of.

Example: Name at least six specific practices from across the chapters and explain how they connect.

**five accountability requirements**  *(also: accountability apparatus; accountability machinery; five requirements)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×9 · kind: framework*

> The accountability apparatus has five requirements — specifications, audit trails, recourse, independent review, sanctions. Each is necessary because it corresponds to cognitive work at a specific tier, and that tier is exactly where AI cannot substitute for a human.
> — *the book, Ch 12 line 186; explained across several passages, no single defining sentence*

In plain words: Specifications, audit trails, recourse, independent review and sanctions. Each is necessary because it corresponds to cognitive work at a specific tier, and a deployment missing any of them has gaps that fail in predictable ways.

Example: Most deployed AI systems are missing two or more of the five.

**perception hierarchy**  *(also: Cleveland-McGill hierarchy)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×8 · kind: framework*

> The implication for picking charts: when the answer is quantitative and precision matters, encode it as position or length. Reach for area, angle, or color only when precision does not matter, or when no other channel fits.
> — *the book, Ch 10 line 101; explained across several passages, no single defining sentence*

In plain words: A ranking of how accurately readers decode a quantity from each visual channel, best to worst: position, length, angle and slope, area, volume, then color. When precision matters use position or length; the ordering is the durable result, while the exact error percentages are only approximate.

Example: Five nearly equal pie slices use angle, a weaker channel, for a question that demanded position.

**natural frequencies**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×7 · kind: concept*

> The underlying principle comes from Gerd Gigerenzer's work on natural frequencies: "9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive" produces correct reasoning where "90% sensitivity, 9.9% false-positive rate" does not — even among physicians who should know better.
> — *the book, Ch 10 line 137; explained across several passages, no single defining sentence*

In plain words: Stating a risk as counts of people, such as 9 out of 10 or 99 out of 1,000, instead of percentages like sensitivity and false-positive rate. The research the chapter cites finds that counts produce correct reasoning where percentages do not, even among physicians.

Example: '9 out of 10 women with breast cancer test positive; 99 out of 1,000 women without breast cancer also test positive.'

Not to be confused with: percentages such as '90% sensitivity, 9.9% false-positive rate'

**common cause failure**  *(also: correlated check; correlated blind spots)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×7 · kind: failure mode*

> It describes what happens when two redundant systems share the same fundamental assumptions — the thing most likely to fool System A is also most likely to fool System B, because both were built on the same foundation.
> — *the book, Ch 12 line 141; explained across several passages, no single defining sentence*

In plain words: When two backup systems share the same basic assumptions, whatever fools one is likely to fool the other, so the second check is not independent. A monitor built like the system it monitors has correlated blind spots with it.

Example: An AI monitoring another AI trained on similar data with similar architecture (Figure 12.4).

Not to be confused with: independent check

**capability scaling**  *(also: scaling)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×7 · kind: concept*

> Adding data widens the sample. But "wider sample" and "the region the sample excludes" are complementary by construction — every enlargement of the covered region is still a region with a boundary, and the boundary is where the gap lives.
> — *the book, Ch 13 line 54; explained across several passages, no single defining sentence*

In plain words: Making models bigger, more capable or trained on more data. The chapter says this widens the region the data covers but never removes its boundary, so the three limits remain.

Example: "Scaling increases pattern breadth and fluency; it does not give the system access to the world its symbols refer to."

**operational consequence**  *(also: the operational consequence binds regardless of the metaphysics)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×7 · kind: concept*

> I need something weaker and firmer: the operational consequence binds regardless of who wins the metaphysics, because it rides on the data-world gap, not on the metaphysics.
> — *the book, Ch 13 line 59; explained across several passages, no single defining sentence*

In plain words: What the supervisor must do in practice holds however the philosophical dispute about meaning comes out, because it rests on the data-world gap, not on the argument over whether models "really" have meaning. Meaning and intentionality inherit their bite from the gap.

Example: At the boundary of the sample the user still reads the output as a claim about the world, while the system is still producing symbols shaped by a sample that excluded that region.

**metacognition**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×5 · kind: concept*

> Metacognition is cognition about cognition: monitoring your own reasoning, detecting your own errors, calibrating confidence to evidence.
> — *the book, Ch 12 line 79; explained across several passages, no single defining sentence*

In plain words: Thinking about your own thinking: monitoring your reasoning, catching your own errors and matching confidence to evidence. AI outputs resemble this, but a self-check is generated by the same system being checked, so it cannot certify that system.

Example: Prompting a model to 'check its work' works, but the check comes from the system being checked.

**irreducibly-human decision**  *(also: irreducibly human)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×5 · kind: concept*

> That noticing is the irreducibly-human decision, and it is the one scaling does not reach — because reaching it requires standing outside the data and asking whether the data's frame matches the world, which is precisely the operation the data-world gap says no data can perform on itself.
> — *the book, Ch 13 line 122; explained across several passages, no single defining sentence*

In plain words: The one judgment that stays with the human however capable the model gets: standing outside the data and asking whether its frame matches the world. Scaling cannot reach it because it concerns the boundary the data does not cover.

Example: In the Epic Sepsis case, noticing that learning to confirm clinical suspicion is the wrong kind of signal for an early-warning tool.

**AI's cognitive profile**  *(also: great, weak, absent)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×4 · kind: framework*

> The cognitive profile — great at retrieval/synthesis/generation under specification, weak at problem formulation/plausibility auditing/interpretive judgment, absent for accountability — translates directly into a delegation map.
> — *the book, Ch 13 line 220; explained across several passages, no single defining sentence*

In plain words: A three-part map of AI's capacities: genuinely strong at retrieval, synthesis and generation under clear criteria; structurally weak where a task connects representations to the world; absent for accountability.

Example: Great: first drafts. Weak: problem formulation. Absent: accountability sign-off.

**deceptive visualization catalog**  *(also: nine-item catalog; nine misleading visualization choices; the catalog)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: framework*

> Here is the property that ties the whole list together: every one of these moves has an honest use, which is exactly why they are dangerous. The chart looks the same whether the choice was honest or not. The choice is the difference — not anything visible in the pixels.
> — *the book, Ch 10 line 185; explained across several passages, no single defining sentence*

In plain words: A named list of chart moves, each with an honest use and a dishonest use, used as a checklist to audit dashboards. The chart looks the same either way; the difference is whether the choice was honest.

Example: Truncating an axis can be honest when zero is not meaningful, as with stock prices.

**FT question taxonomy**  *(also: FT Visual Vocabulary; nine question-families)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×3 · kind: framework*

> The Financial Times' Visual Vocabulary (Alan Smith and team) makes the connection concrete by sorting every chart type into nine question-families. (FT Visual Vocabulary, Financial Times Visual Journalism team; ft.com/vocabulary.) State the question, locate the family, pick from the charts within it.
> — *the book, Ch 10 line 56; explained across several passages, no single defining sentence*

In plain words: The Financial Times' way of sorting every chart type into nine question-families: deviation, correlation, ranking, distribution, change over time, part-to-whole, magnitude, spatial and flow. You state the question, locate its family and pick a chart from it.

Example: Showing that calibration error rises with predicted probability is a correlation question, so a scatterplot fits.

**stakes (something to lose)**  *(also: something to lose; possibility of loss; possibility of consequence)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: concept*

> Sanctions bite only when the sanctioned party has stakes, something to lose. A model does not lose its job. A practitioner does.
> — *the book, Ch 12 line 135; explained across several passages, no single defining sentence*

In plain words: Having something to lose if you are wrong. Sanctions only work on a party with stakes, and a model has none.

Example: A model does not lose its job. A practitioner does.

**resists clean attribution**  *(also: clean attribution)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: concept*

> Responsibility for failures of agentic AI systems resists clean attribution to a single party because the systems are built and deployed across organizational boundaries that do not, by current design, support clean attribution.
> — *the book, Ch 12 line 284; explained across several passages, no single defining sentence*

In plain words: Responsibility for an agentic-system failure cannot be pinned on one party because the systems are built and deployed across organizational boundaries. The chapter calls this a structural observation (responsibility is distributed because the systems are), not a claim about what ought to be.

Example: Model provider trains, framework developer integrates, deploying organization configures, user instructs.

**independent local validation**  *(also: external validation)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: concept*

> The answer that matters is the one about independent local validation — the review that was structurally external, the review nobody was required to perform, the gate nobody signed because the regime did not demand a signature.
> — *the book, Ch 12 line 406; explained across several passages, no single defining sentence*

In plain words: A check of the tool on a hospital's own patient population, done by someone outside the deploying team. In the sepsis case nobody was required to perform it, so nobody signed that gate.

Example: Hospitals deployed the Epic Sepsis Model against their own populations without it; it belongs in the 'what was NOT tested' section.

**wrong tests**  *(also: validation framework scoped to the first question; categorical limit on what the system could be tested for)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×3 · kind: failure mode*

> The system was tested on the question it was built to answer — does this presentation match a category in the training data? The harms came from a different question — what is going on with this specific patient? The two questions are related, but they are not the same.
> — *the book, Ch 13 line 18; explained across several passages, no single defining sentence*

In plain words: Tests that measure the question the system was built to answer rather than the question the deployment actually raises. The clinical system scored well on "does this match a category in the training data?", but the harms came from "what is going on with this specific patient?".

Example: The clinical system passed every test the engineers designed, yet three patients were harmed.

Not to be confused with: negligence (the chapter says the wrongness was not negligence)

**dashboard as argument**  *(also: visualization is an argument; every dashboard is making an argument, by structure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: concept*

> Visualization is not transparent communication of facts. It is an argument, made through structural choices, about what the facts mean and how the reader should weight them.
> — *the book, Ch 10 line 48; explained across several passages, no single defining sentence*

In plain words: A chart or dashboard never just hands over the facts; how it is laid out argues for what the facts mean and how much weight to give each, before anyone reads a number. So the person who builds it is always choosing which argument to make.

Example: A dashboard opening on one bold headline metric argues that the headline is enough; one opening on a panel of equally weighted views argues that the reader must integrate several numbers.

Not to be confused with: transparent communication of facts (the view the chapter rejects)

**the medium is the message**  *(also: a dashboard is a medium)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: concept*

> McLuhan's idea, in working form, was that the form of a communication shapes its meaning before any specific content arrives.
> — *the book, Ch 10 line 36; explained across several passages, no single defining sentence*

In plain words: The form in which something is communicated shapes its meaning before the reader gets to the content. A dashboard is a medium, so its structure shapes what a reader takes from the data before they read any number.

Example: A spoken, a written and a televised story differ because the medium structures the encounter, not because the words change.

**uncertainty exceeding effect size**  *(also: statistical tie; a story about noise; lie of composition)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: failure mode*

> Lesson: when uncertainty exceeds effect size, the chart is a story about noise. The honest story is "tie." Either visualize the confidence intervals so their overlap is obvious, or replace the chart with a sentence.
> — *the book, Ch 10 line 223; explained across several passages, no single defining sentence*

In plain words: When the margin of error is bigger than the difference being reported, the data cannot say which result is ahead, so the honest report is 'a tie', shown by overlapping intervals or a plain sentence. Two bars of different height would draw a difference that is not there.

Example: 45.3% no vs 44.5% yes with a ±2.95% margin: a 0.8-point difference inside a 2.95-point margin.

**visual authority of a chart**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×2 · kind: concept*

> The chart conveyed the full visual authority of a chart built from ground truth, because it looked like all other charts, because charts do not carry labels that say "this proxy may not measure what the question asks."
> — *the book, Ch 10 line 159; explained across several passages, no single defining sentence*

In plain words: Every chart looks equally authoritative whether it rests on ground truth or on an unexamined proxy, because charts carry no label saying what they may not measure. So a weak chart gets the same trust as a strong one.

Example: The Nigeria map looked like every other chart, so it carried the authority of a chart built from ground truth.

**action-warrant**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×2 · kind: concept*

> verbs carry action-warrant. Downgrading conclude to suggest can change a deployment decision, because someone reading conclude would ship and someone reading suggest would ask for another study.
> — *the book, Ch 11 line 378; explained across several passages, no single defining sentence*

In plain words: The idea that a verb tells the reader what to do: a reader who sees "conclude" will act, while one who sees "suggest" will ask for more evidence. So downgrading a verb can change a deployment decision.

Example: Downgrading "conclude" to "suggest": the reader would have shipped, now asks for another study.

**distribution of responsibility**  *(also: responsibility distributes; same topology; contributors, not suspects)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: concept*

> The question "who is responsible?" does not have a single-party answer. It has a distribution of responsibility.
> — *the book, Ch 12 line 33; explained across several passages, no single defining sentence*

In plain words: Responsibility for a failure is spread across several parties, each with some agency, duty and causal contribution, instead of landing on one culprit. The chapter says the spread itself is the finding.

Example: The mail-server case: non-owner, agent, owner, framework developers and model provider all shaped the conditions of the failure.

Not to be confused with: single-party responsibility

**AI as extended mind**  *(also: extension analogy; composition, not competition)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: framework*

> The question that matters for accountability is not whether AI can extend human cognition — it plainly can — but which cognitive operations it extends, which it simulates without performing, and which it cannot touch regardless of scale.
> — *the book, Ch 12 line 68; explained across several passages, no single defining sentence*

In plain words: Cognitive tools such as the microscope, writing and calculators extend human cognition without replacing the mind that directs them. For accountability the question is which operations AI really extends, which it only simulates, and which it cannot touch.

Example: The microscope extends what the scientist can perceive, but the scientist decides what to look for and what the image means.

**compliance ritual wearing the costume of accountability**  *(also: compliance ritual; costume of accountability; rubber stamp with a person's name on it)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×2 · kind: failure mode*

> Human oversight that does not name the tier is a compliance ritual wearing the costume of accountability.
> — *the book, Ch 12 line 233; explained across several passages, no single defining sentence*

In plain words: A process that has the form of oversight or accountability but never genuinely checks anything, such as a signature process whose only permitted outcome is 'signed'. It is a rubber stamp with a person's name on it, which launders the absence of review through a human's credibility.

Example: If the only outcome the process permits is 'signed.'

**skepticism as safety mechanism**  *(also: high-stakes deployments; where the limits bite)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: concept*

> A system that produces clinical recommendations, autonomous-vehicle decisions, agentic actions in shared social spaces, judicial-risk assessments, or large language model outputs in unbounded conversational contexts — these are deployments where the limits bite. The supervisor's skepticism is the safety mechanism in those settings, because the system's apparent competence outruns its actual competence in ways the metrics cannot fully capture.
> — *the book, Ch 13 line 120; explained across several passages, no single defining sentence*

In plain words: In deployments such as clinical, driving or judicial-risk decisions, the supervisor's skepticism is what keeps the system safe, because the metrics cannot fully capture where the system's apparent competence outruns its actual competence.

Example: Clinical recommendations, autonomous-vehicle decisions, judicial-risk assessments, large language model outputs in unbounded conversational contexts.

Not to be confused with: skepticism as methodology

**engineering practice for high-stakes deployments**  *(also: five components; five components of an engineering practice)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: framework*

> The skepticism this book has built — the supervisory capacities, the validation lenses, the delegation maps, the verb taxonomy, the governance counterfactual — culminates in an engineering practice that includes the option to say no.
> — *the book, Ch 13 line 139; explained across several passages, no single defining sentence*

In plain words: The five-part practice the chapter prescribes where the limits bite: specify what can and cannot be tested, keep human oversight, build real override infrastructure, make the limits visible to affected parties, and have a stop condition. It must include the option to say no.

**circular signal**  *(also: confirmatory signal; clinical-cribbing problem; confirm suspicion rather than form it)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: failure mode*

> The problem was that the claim — this model helps clinicians catch sepsis earlier — was not supported by what the model had learned, because the model had partly learned to confirm clinical suspicion rather than form it independently.
> — *the book, Ch 13 line 122; explained across several passages, no single defining sentence*

In plain words: A signal that echoes what clinicians already suspect instead of forming a suspicion on its own, which is the wrong kind of signal for an early-warning tool. In the Epic case the model's claim to help catch sepsis earlier was not supported by what it had learned.

Example: The Epic Sepsis Model had partly learned to confirm clinical suspicion rather than form it independently.

**hierarchy of disclosure**  *(also: hierarchy of uncertainty disclosure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: framework*

> Hierarchy is not hiding. The test is whether a hostile reader could arrive at a different conclusion by knowing the uncertainty. If yes, the uncertainty belongs prominently in the chart.
> — *the book, Ch 10 line 177; explained across several passages, no single defining sentence*

In plain words: How prominently an uncertainty is shown depends on whether it could change the reader's conclusion: in the chart if it could, in a visible caption or footnote if a serious reader needs it, in a methodology appendix if it is small and the conclusion is robust. Ranking by importance is not concealment; the test is a hostile reader.

Example: The Catalonia poll goes prominently in the chart; a 60% vs 30% finding with a ±3% margin goes in a caption.

Not to be confused with: hiding (concealment)

**axis inversion**  *(also: axis-flip deception; inverted y-axis)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> Lesson: the orientation of the axis is itself a structural argument about which direction is "good." When the axis runs against convention, the chart can communicate the inverse of the data while remaining technically accurate. Honest practice: zero at the bottom for quantities where larger values mean more, with the direction-of-better stated explicitly in the title or caption.
> — *the book, Ch 10 line 227; explained across several passages, no single defining sentence*

In plain words: Drawing the axis upside down so the data stays accurate but the reader takes away the opposite of what it shows; it reverses a real effect where truncation amplifies one. Honest practice is zero at the bottom for 'more is more' quantities, with the direction of better stated.

Example: On the Reuters chart with zero at the top, firearm murders rose from 521 in 2005 to 740 in 2006 to 825 in 2007 but looked like a decline.

Not to be confused with: truncated axes / scale trickery

**finished-looking form**  *(also: polished single artifact; finished-looking artifact)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: failure mode*

> Validation analyses are usually presented as if they were finished. The dashboard, the deck, the report — they look polished, single-version, authoritative. This finished-looking form is itself a structural argument: the analysis is complete; what you are reading is the answer.
> — *the book, Ch 10 line 256; explained across several passages, no single defining sentence*

In plain words: Presenting an analysis as a polished, single-version document says by its form that the work is complete and the reader has the final answer, although most analyses are still in progress. That misrepresents the analysis and makes it harder to revise.

Example: Some adoption committees and procurement processes prefer the polished single artifact that hides the work.

Not to be confused with: living deck

**structure that survives review**  *(also: legible to an adversarial reviewer)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: framework*

> The structure is not elegant. It is legible to an adversarial reviewer, which is the relevant property. A reviewer can scan, locate any specific claim, find its evidentiary base, find its limitations, find the AI use, find the reproducibility detail.
> — *the book, Ch 11 line 395; explained across several passages, no single defining sentence*

In plain words: A report layout an adversarial reviewer can navigate: Layer 1 summary, method, findings with calibrated verbs and named uncertainty, calibration metrics (Brier decomposed, ECE with binning and subgroups, reliability diagram, MCE if safety-critical), a real limitations section, a what-would-change-my-mind section, an AI use disclosure and a reproducibility appendix. The test is that a reviewer can find any claim's evidence, limits, AI use and reproducibility detail.

**structural argument for human oversight**  *(also: cognitive argument; structural rather than contingent)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> I want to give you the structural argument. The argument that, even if AI systems become dramatically more capable, certain stages in the accountability machinery require a kind of cognitive work that AI systems cannot perform — not because of current limitations, but because of what accountability actually is and what it requires.
> — *the book, Ch 12 line 60; explained across several passages, no single defining sentence*

In plain words: Even if AI becomes far more capable, certain stages of the accountability machinery need cognitive work AI cannot perform, because of what accountability is and requires. The apparatus lives at Tiers 3, 4, 6 and 7, where AI is weak to absent, while AI operates mainly at Tier 1.

Example: Answerability: no subject with stakes stands behind a model's output.

Not to be confused with: contingent arguments for human oversight

**simulates without performing**  *(also: resembles; Tier 1 simulation; approximation of being heard)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: failure mode*

> A language model can produce text that resembles a governance counterfactual. It cannot actually perform the causal identification — the reasoning that distinguishes "the regime change would have caused the outcome to differ" from "the regime change correlates with better outcomes in the training data
> — *the book, Ch 12 line 255; explained across several passages, no single defining sentence*

In plain words: AI produces output that has the form of a human act (a governance counterfactual, a self-check, an apology, a hearing) without doing the underlying work. In each case fluent resemblance stands in for the real act.

Example: A language model can write text resembling a governance counterfactual but cannot perform the causal identification behind it.

Not to be confused with: extension (where AI really does extend human reach)

**validator independence**  *(also: validator-independence point; first opinion run twice; validator must be outside the system being validated)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: concept*

> an AI checking an AI is not a second opinion, it is the first opinion run twice. The independence that makes review mean something is precisely what a system cannot supply about itself.
> — *the book, Ch 12 line 79; explained across several passages, no single defining sentence*

In plain words: A review only counts as a second opinion if the reviewer is independent of what it reviews; an AI checking an AI is the first opinion run twice. A system cannot supply that independence about itself, and at bottom 'outside' means capable of being answerable.

Example: A monitoring AI checking another AI's output, versus a human supervisor who stands outside the system.

**appearance of validation**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×1 · kind: failure mode*

> The second thing that would change my mind: if a Tier 4 or Tier 5 AI capability were demonstrated that could perform the validation work the chapter assigns to humans — not the appearance of validation, but validation that is independent of the system being validated and answerable to external consequences.
> — *the book, Ch 12 line 329; explained across several passages, no single defining sentence*

In plain words: Output that has the look of a validation without being independent of the system and answerable to external consequences. The chapter says real validation must be independent and answerable, not merely look like validation.

Example: The AI-written sign-off statement.

Not to be confused with: validation that is independent and answerable

**skepticism as methodology**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> Skepticism is methodology, not a safety mechanism. The supervisor verifies, monitors, calibrates. The limits do not bite hard.
> — *the book, Ch 13 line 118; explained across several passages, no single defining sentence*

In plain words: The ordinary mode of skepticism where the data-world gap is small and monitorable: the supervisor verifies, monitors and calibrates. The limits do not bite hard there.

Example: A system that classifies images of products on a manufacturing line.

Not to be confused with: skepticism as safety mechanism

**functional equivalence**  *(also: functionally equivalent)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> Some readings of agentic systems argue that goal-pursuit is functionally equivalent to intentionality. Whether functional equivalence captures what intentionality is supposed to capture is a deep question I am not going to settle here.
> — *the book, Ch 13 line 71; explained across several passages, no single defining sentence*

In plain words: The argument that a system pursuing goals is doing, in effect, what intentionality is. The chapter leaves the question open and says the supervisor still has to supply the directedness.

Example: Exercise 12's colleague: AI systems "can be audited, generate explanations for their outputs, and be corrected when wrong. This is functionally equivalent to accountability."

Not to be confused with: intentionality (the thing it is claimed to match)

**apparent competence outruns its actual competence**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: failure mode*

> You can have ninety-four percent accuracy and three harmed patients, because the ninety-four percent was over the question the data could answer, and the three patients were in a region the data could not.
> — *the book, Ch 13 line 120; explained across several passages, no single defining sentence*

In plain words: Measured performance that looks strong but does not match how the system behaves in the cases that matter. Accuracy is earned on the question the data could answer, while the harms fall in regions the data could not cover.

Example: Ninety-four percent accuracy and three harmed patients.

**load-bearing assumptions**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> For your own deployments: identify, before you launch, the two or three load-bearing assumptions in the system. Build a small experiment for each.
> — *the book, Ch 13 line 158; explained across several passages, no single defining sentence*

In plain words: The two or three assumptions your system most depends on, often implicit in the architecture or deployment context. Each gets its own small experiment before launch.

**supervisory engineering**  *(also: supervising AI systems for fitness in deployment contexts)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: concept*

> It is supervisory in the sense that it is irreducibly about the relationship between the AI system, the deployment context, and the affected parties — and that relationship is not in the system. The system does not know about the relationship. The relationship is the supervisor's job.
> — *the book, Ch 13 line 350; explained across several passages, no single defining sentence*

In plain words: The book's kind of work: engineering that needs technical competence, produces deliverables and is testable against criteria, but is supervisory because it concerns the relationship between the AI system, the deployment context and affected parties. That relationship is not in the system.

**quantile dotplot**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×9 · kind: method*

> This is the technique most guides skip, and it is one of the most effective for communicating uncertainty to lay audiences. Twenty dots, of which four are filled, beats "20% chance" every time.
> — *the book, Ch 10 line 137; explained across several passages, no single defining sentence*

In plain words: A chart that shows a probability as a set of dots, for example twenty dots with four filled, so readers count outcomes instead of reading a percentage. It uses position, the best channel, and the chapter ranks it above confidence bands for lay audiences.

Example: Twenty dots, of which four are filled, beats '20% chance'.

**changelog slide**  *(also: changelog)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×5 · kind: method*

> The final presentation includes the changelog as the second-to-last slide. The changelog is evidence of the work — the visible track of how the analysis evolved. Removing it before final submission would erase the supervisory log.
> — *the book, Ch 10 line 266; explained across several passages, no single defining sentence*

In plain words: A slide in a living deck recording what changed since the prior version and why; it is the visible track of how the analysis evolved. A deck without it is pretending to be finished.

Example: It sits as the second-to-last slide of the final presentation.

**make the limits visible to affected parties**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×2 · kind: method*

> Make the limits visible to affected parties. When a system's recommendation is the basis for a decision affecting a person, the person should be able to know, to a useful approximation, what the system can and cannot do.
> — *the book, Ch 13 line 135; explained across several passages, no single defining sentence*

In plain words: Tell the person affected by a system-based decision what the system can and cannot do, in a form they can read. The chapter says this is not "explain the model" and leaves it as an open problem.

Not to be confused with: explaining the model

**build-and-audit pairing**  *(also: pairing of the supervisory capacities; catch and fix your own misleading encoding)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> This chapter exercises a specific pairing of the supervisory capacities: you get the machine to build the chart, and then you audit what it built before it ships, catching the misleading encoding you or the tool reached for by default.
> — *the book, Ch 10 line 26; explained across several passages, no single defining sentence*

In plain words: Have the AI build the chart, then audit what it built yourself before it ships, asking what argument its structure makes and whether the data supports that argument. The AI does not remove the work; it relocates it to the audit.

Example: Chart your data with an AI, then catch and fix the misleading encoding (default axis, palette or aggregation) before it ships.

**the question the chart is answering**  *(also: state the question in one sentence; the chart is a function of the question)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> A chart is not a way to display data. A chart is a way to answer one question with data. If you cannot state the question in a sentence, you do not yet know which chart to draw.
> — *the book, Ch 10 line 54; explained across several passages, no single defining sentence*

In plain words: Before choosing a chart, state in one sentence the question it answers, then find the data and chart type that fit that question. The question comes first; the chart is a function of it.

Example: 'How has model calibration changed across six months of deployment?' rather than 'chart the database.'

**validate before you visualize**  *(also: check the data against the question)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> The lesson: a chart based on a proxy you have never examined will mislead with the full visual authority of a chart based on truth. You have to check first whether the proxy carries the signal at all.
> — *the book, Ch 10 line 161; explained across several passages, no single defining sentence*

In plain words: Check that your data actually measures what the question asks before you chart it, because a chart on an unexamined proxy misleads with the authority of a chart on truth. If it measures a proxy, change the dataset, change the question or disclose the proxy.

Example: The Nigeria 'kidnapping rates' map turned out to be a map of news stories.

**when uncertainty is too large, do not visualize**  *(also: sometimes the right chart is no chart)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> A bar chart showing two bars, one a hair taller than the other, is a lie of composition — the visual encodes a difference that is not there. The honest move is text, or a chart that makes the confidence interval visually larger than the effect. Sometimes the right chart is no chart.
> — *the book, Ch 10 line 169; explained across several passages, no single defining sentence*

In plain words: When the margin of error swamps the effect, two bars would show a difference that is not there, so use a sentence, or a chart that makes the interval larger than the effect. Sometimes the right chart is no chart.

Example: 45.3% no vs 44.5% yes with a ±2.95% margin: say 'it's a tie'.

**working sequence for picking and showing**  *(also: seven-step working sequence)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: method*

> This is the sequence, not a checklist. The decision forks at steps 3 and 7 are where most published charts quietly fail.
> — *the book, Ch 10 line 297; explained across several passages, no single defining sentence*

In plain words: A seven-step order for making a chart: state the question, locate its family, check the data fits the question, identify the aleatoric uncertainty, identify the epistemic uncertainty, choose encodings by the perception hierarchy, then test against a hostile read. The forks at steps 3 and 7 are where most published charts quietly fail.

Example: Step 1: not 'chart the database' but 'How has model calibration changed across six months of deployment?'

**downgrading verbs in AI output**  *(also: verb downgrade; downgrading the verb)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: method*

> If the answer is no, the AI's verb is unwarranted. The supervisor's move is to replace conclusively demonstrates with suggests or observes, and to explicitly note that the stronger reading is not yet warranted.
> — *the book, Ch 11 line 371; explained across several passages, no single defining sentence*

In plain words: Checking an AI-written claim by asking what evidence its verb requires, and if that evidence was not produced, replacing the verb with a weaker one and saying the stronger reading is not yet warranted. The chapter calls it one of the highest-leverage editing moves, because the underlying factual claim usually stays the same and only the posture changes.

Example: Replace "conclusively demonstrates" with "suggests" or "observes" in an AI-written paragraph.

**layered writing**  *(also: three audience layers; layered document; two readers, one document)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 ×1 · kind: method*

> A working alternative is layered writing. The technical and non-technical content live in the same document, layered so that each reader can find their level without translation.
> — *the book, Ch 11 line 92; explained across several passages, no single defining sentence*

In plain words: Putting technical and non-technical content in one document, arranged in layers so each reader finds their level without a separate translation. The chapter prefers it to two documents because two documents drift and every translation can lose the nuance the calibration was protecting.

Example: One validation report with a Layer 1 plain-English summary, Layer 2 technical detail and Layer 3 reproducibility appendix.

Not to be confused with: two-document approach

**rapid prototyping for skepticism**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×1 · kind: method*

> It is the scientific method made operational for AI deployment decisions. The novelty is doing it at all.
> — *the book, Ch 13 line 156; explained across several passages, no single defining sentence*

In plain words: A six-step way to test a model assumption before deployment: state it, name what would falsify it, design a cheap test, lock a prediction, run the test, then decide to proceed, modify, defer or refuse.

Example: Identify two or three load-bearing assumptions, build a small experiment for each, run them, and make the deployment decision after.

**deviation (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Deviation — how far from a reference point (zero, a target, a baseline, a comparison group)? Bullet charts and diverging bars belong here. When you want to show that subgroup A performs 12 points below the overall average, this is the family.
> — *the book, Ch 10 line 62*

In plain words: Questions about how far something is from a reference point: zero, a target, a baseline or a comparison group.

Example: Subgroup A performs 12 points below the overall average (bullet charts, diverging bars).

**correlation (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Correlation — how does one variable move with another? Scatterplots. When you want to show that calibration error rises with predicted probability, this is the family.
> — *the book, Ch 10 line 64*

In plain words: Questions about how one variable moves with another.

Example: Calibration error rises with predicted probability (scatterplot).

**ranking (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Ranking — what is the order? Ordered bar charts, dot plots. When you want to show which features the model relies on most, this is the family.
> — *the book, Ch 10 line 66*

In plain words: Questions about the order of the items.

Example: Which features the model relies on most (ordered bar charts, dot plots).

**distribution (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Distribution — how often does each value occur? Histograms, box plots, violin plots, strip plots. When you want to show the spread of prediction confidence scores, this is the family.
> — *the book, Ch 10 line 68*

In plain words: Questions about how often each value occurs.

Example: The spread of prediction confidence scores (histograms, box plots, violin plots, strip plots).

**change over time (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Change over time — what is the trend? Line charts. When you want to show how accuracy has shifted over deployment months, this is the family.
> — *the book, Ch 10 line 70*

In plain words: Questions about the trend.

Example: How accuracy has shifted over deployment months (line charts).

**part-to-whole (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Part-to-whole — what proportion of the total? Stacked bars, treemaps. Use cautiously; pie charts belong here but rarely communicate as clearly as their popularity suggests.
> — *the book, Ch 10 line 72*

In plain words: Questions about what proportion of a total each piece makes up.

Example: Stacked bars and treemaps; pie charts belong here but rarely communicate as clearly as their popularity suggests.

**magnitude (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Magnitude — how big, in absolute terms? Bar charts with a zero baseline. When you want to show raw counts of model failures by category, this is the family.
> — *the book, Ch 10 line 74*

In plain words: Questions about how big something is in absolute terms.

Example: Raw counts of model failures by category (bar chart with a zero baseline).

**spatial (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Spatial — where? Maps. When the geography matters — when you need to show that failures cluster in specific deployment regions — this is the family.
> — *the book, Ch 10 line 76*

In plain words: Questions about where something happens.

Example: Failures clustering in specific deployment regions (maps).

**flow (question family)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Flow — what moves from where to where? Sankov and alluvial diagrams. When you want to show how users reclassified by the new model compare to the old, this is the family.
> — *the book, Ch 10 line 78*

In plain words: Questions about what moves from where to where.

Example: How users reclassified by the new model compare to the old (alluvial diagrams).

**Abela's decision tree**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: framework*

> Andrew Abela's older decision tree (Choosing a Good Chart, 2009) collapses these into four — comparison, composition, distribution, relationship — and walks through binary choices. Either framework works. The point is the same: the chart is a function of the question.
> — *the book, Ch 10 line 80*

In plain words: An older way to choose a chart that boils the question families down to four (comparison, composition, distribution, relationship) and walks through binary choices. Like the FT taxonomy, it picks the question first and lets the chart follow.

**uncertainty from the visualization process**  *(also: a useful third source)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> A useful third source: the visualization process itself introduces uncertainty. How you bin a histogram, where you start the y-axis, what you call "high" — these are choices, and choices are sources of distortion the reader cannot see unless you surface them.
> — *the book, Ch 10 line 115*

In plain words: The chart-maker's own choices, such as how to bin a histogram, where to start the y-axis and what to call 'high', add distortion the reader cannot see unless it is surfaced. The chapter counts it as a third source of uncertainty.

Example: How you bin a histogram, where you start the y-axis, what you call 'high'.

**detecting deceptive design choices**  *(also: the general detection problem)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> I do not have a clean way to automatically detect deceptive design choices in a dashboard the way accessibility tools detect contrast issues. Some patterns — truncated axes, inconsistent scales — are mechanical and could be flagged by tooling. Others — color asymmetry, label prejudgment, selective uncertainty, cherry-picked time windows — require contextual judgment about whether the choice is honest.
> — *the book, Ch 10 line 352*

In plain words: Some deceptive choices (truncated axes, inconsistent scales) are mechanical enough for tooling to flag, but others (color asymmetry, label prejudgment, selective uncertainty, cherry-picked windows) need judgment about whether the choice is honest. So general automatic detection is an open problem.

Example: Accessibility tools can detect contrast issues automatically; nothing equivalent exists for deceptive choices.

**cohort functioning, over-functioning and under-functioning**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 · kind: concept*

> The cohort is functioning if the critiques surface real calibration issues; the cohort is over-functioning if the critiques are converging on a single preferred voice; the cohort is under-functioning if the critiques are too polite or too generic to be useful.
> — *the book, Ch 11 line 417*

In plain words: The chapter's check on whether peer critique is working: functioning if critiques surface real calibration issues, over-functioning if they converge on one preferred voice, under-functioning if they are too polite or generic to be useful.

Example: Critiques that all converge on a single preferred voice mean the cohort is over-functioning.

**single-party responsibility (structural mismatch)**  *(also: structural mismatch)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> most of our legal and regulatory thinking about accountability assumes single-party responsibility. The structural mismatch between that assumption and the actual topology of agentic-system failures is the policy problem this chapter sits inside.
> — *the book, Ch 12 line 37*

In plain words: Most legal and regulatory thinking assumes one party is responsible, but agentic-system failures spread responsibility across several parties. That mismatch is the policy problem the chapter sits inside.

Example: The mail-server case has five contributors, none sufficient alone.

Not to be confused with: distribution of responsibility

**contingent arguments for human oversight**  *(also: institutional case for oversight)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> All of these cases are correct and all of them are insufficient. They are contingent arguments. They depend on the current state of AI capability, the current state of regulation, and the current risk appetite of deploying organizations.
> — *the book, Ch 12 line 58*

In plain words: Reasons for human oversight that hold only under today's conditions: organizations need someone to sue, current rules require oversight, and current AI is not reliable enough. They weaken if AI improves, rules change or risk tolerance shifts.

Example: Liability grounds, regulatory grounds and practical grounds.

Not to be confused with: structural argument

**functionalist versus phenomenological definition of emotion**  *(also: emotion (functional))*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Under a functionalist definition — a state that shifts behavior in characteristic ways in response to relevant stimuli — the evidence for emotion-like states in AI is real: prompt a model in ways associated with distress and its outputs move off baseline. Under a phenomenological definition — there is something it is like to be in that state — we have no evidence and no method for getting any.
> — *the book, Ch 12 line 77*

In plain words: Two ways to define emotion: functionally (a state that shifts behavior in characteristic ways) and phenomenologically (there is something it is like to be in that state). AI can qualify under the first but there is no evidence under the second, and the accountability question is which definition the regime requires.

Example: Prompt a model in ways associated with distress and its outputs move off baseline.

**capacities where AI extends human reach**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Semantic memory, pattern recognition, statistical language, metric navigation, constrained planning — where AI is strong, it extends human reach exactly the way writing extended memory or the microscope extended perception, and the extended mind is more capable than the bare one.
> — *the book, Ch 12 line 81*

In plain words: Where AI is strong (semantic memory, pattern recognition, statistical language, metric navigation, constrained planning) it extends human reach the way writing extended memory or the microscope extended perception. The extended mind is then more capable than the bare one.

Example: Writing extending memory; the microscope extending perception.

Not to be confused with: capacities that require a subject

**capacities that require a subject**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> But episodic memory, calibrated metacognition, moral salience, stakes — where AI is weak or absent, the missing capacity is not one you can add by pouring in more computation. It requires a different kind of thing entirely: an agent with a history, with commitments, with the possibility of loss.
> — *the book, Ch 12 line 81*

In plain words: Episodic memory, calibrated metacognition, moral salience and stakes need an agent with a history, commitments and something to lose, so more computation cannot add them. These are the capacities accountability requires.

Example: A model has no continuous history as an agent, so it cannot say 'I made this decision, for this reason.'

Not to be confused with: capacities where AI extends human reach

**interpersonal repair (emotion)**  *(also: emotion (interpersonal repair))*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Absent | Capacity to apologize meaningfully | Cannot perform the recourse function of accountability
> — *the book, Ch 12 line 95*

In plain words: AI lacks the capacity to apologize meaningfully, so it cannot perform the repair side of accountability. This is one reason an AI-only recourse channel feels hollow.

Example: Capacity-table implication: AI cannot perform the recourse function of accountability.

**cognitive mapping (navigation)**  *(also: navigation, cognitive mapping)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Weak | World-model with intervention support | Can mislead under shifted topology
> — *the book, Ch 12 line 98*

In plain words: AI is weak at building a world-model that supports intervention questions, so it can mislead when the structure of the setting has shifted. The same table lists metric navigation as a strength.

Example: Misleading output under a shifted topology (capacity table).

**hierarchical real-world planning**  *(also: planner of record)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Poor | Goal-context inference under ambiguity | Cannot be the planner of record for high-stakes deployment
> — *the book, Ch 12 line 100*

In plain words: AI is poor at real-world planning that needs goals inferred from context under ambiguity, so it cannot be the planner of record for a high-stakes deployment. Tree-search planning in bounded games is listed as superhuman.

Example: Bounded games (a strength) versus high-stakes deployment (not).

**collective intelligence (capacity)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Absent by definition (single artifact) | Membership in a community that holds members accountable | Cannot belong to a community of practice
> — *the book, Ch 12 line 105*

In plain words: A single AI artifact is not a member of a community that holds its members accountable, so it cannot belong to a community of practice. The capacity is marked absent by definition.

Example: A single AI artifact versus a community that holds its members accountable.

**Tier 1: Pattern and Association**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Linguistic and logical-mathematical reasoning, fact recall, associative lookup | Superhuman | Training humans to compete here is malpractice
> — *the book, Ch 12 line 115*

In plain words: The tier of language, logic, fact recall and associative lookup, where AI is superhuman. The chapter says training humans to compete with AI directly here is malpractice.

Example: Capturing the audit trail is Tier 1 work (mechanical logging).

**Tier 2: Embodied and Sensorimotor**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Knowledge that lives in the body: proprioception, physical skill, tactile feedback through a tool | Weak — data and actuator limits, not a philosophical barrier | Train hands-on judgment; AI cannot verify by touch
> — *the book, Ch 12 line 116*

In plain words: Knowledge that lives in the body, such as physical skill and touch feedback; AI is weak here because of data and actuator limits, not a philosophical barrier. Humans should train hands-on judgment because AI cannot verify by touch.

Example: Proprioception, physical skill, tactile feedback through a tool.

**Tier 3: Social and Personal**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Interpersonal intelligence, emotional regulation, moral reasoning under genuine stakes | Simulates the output; does not experience what produces it | Train the human; AI can produce the text but cannot be implicated in the outcome
> — *the book, Ch 12 line 117*

In plain words: Interpersonal intelligence, emotional regulation and moral reasoning under real stakes; AI simulates the output without experiencing what produces it. It can write the text but cannot be implicated in the outcome.

Example: Recourse (being heard) depends on Tier 3 plus Tier 6.

**Tier 6: Collective and Distributed**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Intelligence emergent from systems of people in relationship | Reflects the record of collective intelligence; absent from the practice that generated it | Train the human; accountability regimes are Tier 6 artifacts
> — *the book, Ch 12 line 120*

In plain words: Intelligence that emerges from systems of people in relationship. AI reflects the record of collective intelligence but is absent from the practice that produced it, and accountability regimes are Tier 6 artifacts.

Example: Emergent multi-agent failures are called Tier 6 phenomena.

**Tier 7: Existential and Wisdom**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Practical wisdom that requires stakes and the possibility of loss | Absent — no stakes, no biographical continuity | Train the human; the durable comparative advantage
> — *the book, Ch 12 line 121*

In plain words: Practical wisdom that requires stakes and the possibility of loss; AI is absent here because it has no stakes and no biographical continuity. It is the human's durable comparative advantage.

Example: Sanctions are Tier 7: an AI does not lose its job.

**derivation versus recognition**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> The AI system derives. Chain-of-thought monitoring by another AI system — Pachocki's proposed solution for the automated researcher — is more derivation. What seems structurally absent is recognition — the moment of contact between a formal output and an external reality.
> — *the book, Ch 12 line 131*

In plain words: Derivation is a system producing outputs from its own rules, and another AI layer is more of it; recognition is the moment a formal output makes contact with external reality. The chapter's intuition is that recognition cannot be replicated by adding more derivation.

Example: Chain-of-thought monitoring by another AI is more derivation, not recognition.

**upstream (highest-leverage accountability targets)**  *(also: upstream; leverage; proximate party)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> And the structural finding it produces is sharper than the Kantian one: in agentic systems, the highest-leverage accountability targets are often upstream of the proximate party, at the framework and model-provider levels where engineering choices produce the conditions for many failures rather than one.
> — *the book, Ch 12 line 168*

In plain words: Parties earlier in the chain than the one that directly caused the harm, here the framework developers and model provider. Holding them accountable has the most leverage because their engineering choices set the conditions for many failures, not one.

Example: Framework defaults propagate to thousands of deployments.

Not to be confused with: proximate party

**underspecified human-oversight mandate**  *(also: Tier 1 box-checking)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: failure mode*

> Regimes mandate "human oversight" for high-risk systems without specifying which cognitive tier the oversight must supply — and that omission is the whole vulnerability. A mandate for "a human in the loop" is satisfied by a human who performs only Tier 1 box-checking: reads the AI's output, clicks "approve," and never does the Tier 4 plausibility auditing the loop actually requires.
> — *the book, Ch 12 line 233*

In plain words: A rule that requires 'human oversight' for high-risk systems without saying which cognitive tier the oversight must supply, so a human doing only Tier 1 box-checking satisfies it. The chapter calls that omission the whole vulnerability.

Example: A human who reads the AI's output, clicks 'approve' and never does the Tier 4 plausibility auditing.

**NIST AI Agent Standards Initiative**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: framework*

> NIST's AI Agent Standards Initiative (launched by its Center for AI Standards and Innovation in February 2026 to foster industry-led standards for agentic systems)
> — *the book, Ch 12 line 235*

In plain words: A NIST effort, launched by its Center for AI Standards and Innovation in February 2026, to foster industry-led standards for agentic systems.

Example: It sits alongside the NIST AI Risk Management Framework and sectoral guidance.

**stakes and oversight intensity**  *(also: stages and stakes)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: framework*

> The cognitive tiers tell you what capacity oversight requires; stakes tell you how intensively to apply it and on what cadence. That is an orthogonal axis, and crossing the two gives a working tool for when human oversight is not optional.
> — *the book, Ch 12 line 268*

In plain words: A second axis, separate from the cognitive tiers: the tiers say what capacity oversight needs, and stakes say how intensively and how often to apply it. Crossing the two gives a working tool for when human oversight is not optional.

Example: A draft email gets a spot-check; a medical decision gets per-decision review by a named human.

Not to be confused with: stakes (something to lose)

**human present but not engaging the required tier**  *(also: rubber stamp)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: failure mode*

> Notice the failure mode the table names: a human can be present at every stage and still supply nothing, if they are not engaging the tier the stakes demand.
> — *the book, Ch 12 line 270*

In plain words: A human can be present at every stage and still supply nothing if they are not engaging the tier the stakes demand. The table shows it as a rubber stamp, a reviewer whose override rate drops without explanation, or 'the model said so' as the audit answer.

Example: Low stakes: sampling cadence drifts to zero; high stakes: the reviewer signs off without engagement.

**consolidating responsibility (strict liability, vertical integration)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> A redesign that consolidated responsibility — for example, by requiring vertically integrated providers, or by attributing all failures to deploying organizations as a matter of strict liability — would produce different incentives and a different topology of failure.
> — *the book, Ch 12 line 286*

In plain words: A redesign that puts responsibility on one party, for example vertically integrated providers or strict liability for deploying organizations. It would change the incentives and the topology of failure, and whether it is desirable is a values choice, not a technical one.

Example: Strict liability for deploying organizations; required vertical integration of model provider and deployer (exercise C2).

**generative AI stretches the topology**  *(also: flattened distribution)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Generative AI stretches this topology rather than changing its shape. When a system can produce anything rather than classify something, the list of parties extends — through training data, training procedure, and downstream propagation — and the distribution flattens, so the governance counterfactual acquires more variables.
> — *the book, Ch 12 line 288*

In plain words: When a system can produce anything rather than classify something, the list of parties extends through training data, training procedure and downstream propagation, and the distribution of responsibility flattens. The governance counterfactual then has more variables.

Example: Who wrote an image, a paragraph or code the model generated is not a settled question.

**provenance (AI Use Disclosure)**  *(also: AI Use Disclosure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> What holds the flattened distribution together operationally is provenance — and the AI Use Disclosure from Chapter 9 is its concrete form, a Tier 4 document in which the engineer separates their own contribution from the model's Tier 1 output.
> — *the book, Ch 12 line 288*

In plain words: The record of who contributed what that holds the flattened distribution of responsibility together; its concrete form is the AI Use Disclosure from Chapter 9. In it the engineer separates their own contribution from the model's Tier 1 output.

Example: An AI Use Disclosure naming which parts are the engineer's and which the model's.

**speed and deniability (what the attestation regime sacrifices)**  *(also: speed and deniability)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> What it sacrifices is speed and deniability. Naming a human per gate means someone has to be willing to be named — and organizations under deployment pressure resist that.
> — *the book, Ch 12 line 309*

In plain words: The cost of an attestation regime: naming a human per gate means someone must be willing to be named, and organizations under deployment pressure resist that. The 'what did we not test?' question arrives as friction late in a scheduled launch.

Example: A business case is made, the launch is scheduled, and the attestation asks what was not tested.

**fundamental versus contingent cases**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Be honest about which cases are FUNDAMENTAL (would persist under any regime) vs CONTINGENT (would not occur under the counterfactual regime).
> — *the book, Ch 12 line 453*

In plain words: Sorting the casebook's cases into those that would persist under any governance regime (fundamental) and those that would not occur under the counterfactual regime (contingent).

Example: Cases a different regulatory environment or deployer accountability would prevent are contingent.

**overclaiming Turing and Searle**  *(also: common misreading; credit for a stronger claim than he made)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: failure mode*

> Both arguments are important and both are regularly overclaimed. The validator who only tests behavior misses the limits; the validator who only invokes the limits skips the testing. The job is to do both.
> — *the book, Ch 13 line 108*

In plain words: Treating Turing as having proved that imitation is intelligence, or Searle as having proved that AI cannot understand. The chapter says each made a narrower claim: Turing a methodological one, Searle that behavior does not entail understanding.

Example: "Searle proved AI cannot understand" - he showed sufficiency fails; he did not establish necessity.

**fictitious override**  *(also: a fiction in the documentation)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: failure mode*

> An override that is documented but practically impossible — no time, no authority, no legibility — is not an override. It is a fiction in the documentation.
> — *the book, Ch 13 line 133*

In plain words: An override that exists on paper but cannot be used because there is no time, no authority or no legibility. The chapter says that is not an override at all.

Example: A documented override with no time, no authority and no legibility to use it.

Not to be confused with: build the infrastructure for the override

**equal visual weight for uncertainty**  *(also: make the uncertainty visually equal in weight to the central estimate)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: method*

> Make the uncertainty visually equal in weight to the central estimate. A small error bar on a big bold number says: this is the answer, with a quibble. A central estimate displayed at the same visual weight as the uncertainty range says: the uncertainty is part of the finding.
> — *the book, Ch 10 line 147*

In plain words: Show the uncertainty range with the same visual weight as the central estimate so the reader sees it as part of the finding, not a quibble. This matters most when the margin of error is large relative to the effect.

Example: A bold '94.3% accuracy' with a thin error bar versus '91–97% accuracy (95% CI)' drawn as a range at equal weight.

**Wilson or bootstrap confidence interval**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: method*

> Aleatoric uncertainty around each rate shown via confidence intervals (use Wilson or bootstrap CI for small N)
> — *the book, Ch 10 line 459*

In plain words: Two ways of putting a confidence interval around a rate when only a few cases were tested, so the chart shows its aleatoric uncertainty. The chapter's prompt says to use them for small N.

Example: Confidence intervals around each failure rate on the honest dashboard.

**accountability audit checklist**  *(also: reusable audit instrument)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: method*

> A deployment with all five requirements has a working framework; one missing any of them has gaps that fail in predictable ways, and most deployed AI systems are missing two or more. The checklist below turns the five into a reusable audit instrument.
> — *the book, Ch 12 line 198*

In plain words: The five requirements turned into a reusable audit tool: for each, what it consists of, the failure mode if absent, how to verify it is present and its tier. A regime that cannot tick all five boxes has AI accountability as a slogan, not a practice.

Example: Verify recourse: an external party can read the channel description and use it.

**what was tested (attestation part 1)**  *(also: what was tested)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: method*

> The specific checks you ran, against the specific acceptance criteria, with the results. Not "validated" — this test, this threshold, this outcome.
> — *the book, Ch 12 line 218*

In plain words: The first part of an attestation: the specific checks you ran, against the specific acceptance criteria, with the results. It replaces the word 'validated' with a named test, threshold and outcome.

Example: "This test, this threshold, this outcome."

**what was NOT tested (attestation part 2)**  *(also: what was NOT tested; the gaps)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: method*

> The gaps. The conditions you did not probe, the distributions you did not cover, the failure modes you know exist and did not get to. This is the part the AI-generated sign-off will never write, because it does not know what it did not do — and it is the part that makes the attestation honest.
> — *the book, Ch 12 line 219*

In plain words: The second part of an attestation: the conditions you did not probe, the distributions you did not cover and the failure modes you know exist but did not get to. It is the part an AI-generated sign-off will never write.

Example: Exercise A6 asks for at least four untested conditions of a bank customer-service agent.

**who cleared which gate (attestation part 3)**  *(also: who cleared which gate; named human per decision)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: method*

> A named human per decision. Not "the team." A role that can be asked, and if necessary, can lose something.
> — *the book, Ch 12 line 220*

In plain words: The third part of an attestation: a named human for each decision, not 'the team', in a role that can be asked and, if necessary, can lose something. It is what ties the attestation to answerability.

Example: A named role signs each gate.

**the verbs, calibrated (attestation part 4)**  *(also: the verbs, calibrated; calibrated verbs)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: method*

> Matching the discipline from the uncertainty-communication material: the verb of each claim matches the evidence behind it. "Passed" means passed a stated test. "Believe safe" means something weaker, and says so.
> — *the book, Ch 12 line 221*

In plain words: The fourth part of an attestation: the verb of each claim matches the evidence behind it, so 'passed' means passed a stated test and 'believe safe' is openly weaker.

Example: "Passed" versus "believe safe."

**default chart choices**  *(also: default axis, default palette, default aggregation; your plotting library's default)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: failure mode*

> An AI will draw the chart. It will pick a default axis, a default palette, a default aggregation — instantly, competently, and without any stake in whether the result is honest.
> — *the book, Ch 10 line 26; explained across several passages, no single defining sentence*

In plain words: The axis range, palette and summary that an AI or plotting library picks when you do not choose. An AI picks them instantly and competently but with no stake in whether the result is honest, so you must review them.

Example: Reaching for the default chart Excel offers; Excel does not know what you are trying to say.

**looking finished versus being honest**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> Usually that default is your plotting library's, which was optimized for looking finished, not for being honest. The two are not the same thing, and the gap between them is where most misleading dashboards live.
> — *the book, Ch 10 line 40; explained across several passages, no single defining sentence*

In plain words: A chart can look polished and complete without being faithful to the data, and plotting-library defaults are tuned for the first, not the second. Most misleading dashboards live in the gap between the two.

Example: The misleading opening dashboard was only 'a handful of choices away' from the honest one, about thirty seconds each.

**the trade-off: misleading charts are faster and more persuasive**  *(also: faster to build and more persuasive on first contact)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> A misleading chart is faster to build than an honest one, and it is more persuasive on first contact. That is the deal on offer.
> — *the book, Ch 10 line 246; explained across several passages, no single defining sentence*

In plain words: A misleading chart is faster to build and more persuasive on first contact than an honest one; optimizing for looking finished and reassuring spends the reader's ability to reach a different conclusion. That fails badly the moment a decision-maker needs to see the region of doubt.

Example: The Challenger decision.

**normative choices (there is no neutral)**  *(also: the choices are normative; there is no neutral)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: concept*

> The choices that compose the argument are normative — they reflect a stance about what matters and how the reader should weight things. The engineer who treats those choices as neutral is mistaken about what they are doing.
> — *the book, Ch 10 line 358; explained across several passages, no single defining sentence*

In plain words: Every chart-design choice reflects a stance about what matters and how the reader should weight things, so there is no neutral default. An engineer who treats the choices as neutral is mistaken about what they are doing.

Example: Truncate here, gray there, bury the calibration curve in a tab: each choice took about thirty seconds and shifted the argument.

**inferential caution versus evidential strength**  *(also: two-dimensional ladder; indicate)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 · kind: concept*

> This ladder is really flattening a two-dimensional thing into one line. "Suggest" and "indicate" measure inferential caution; "observe," "find," and "show" measure evidential strength. Those are different axes, which is exactly why verb ladders tend to wobble.
> — *the book, Ch 11 line 43; explained across several passages, no single defining sentence*

In plain words: The ladder squeezes two different things into one line: verbs such as suggest and indicate show how cautious the inference is, while observe, find and show measure how strong the evidence is. The chapter keeps one line on purpose because a single defended ladder is more usable for not over-claiming than a correct grid.

Example: "Indicate" is deliberately left off the ladder because it measures caution rather than strength.

**emotion as moral salience**  *(also: moral standing; moral seriousness)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Shame, regret, the weight of having gotten it wrong — these are not decorations on accountability; they are the mechanism by which a consequence lands. A system that cannot be worse or better for anything cannot be the party a sanction bites.
> — *the book, Ch 12 line 77; explained across several passages, no single defining sentence*

In plain words: For accountability what matters about emotion is not feeling but whether a system can be harmed, have its interests violated or bear moral standing; on current evidence a model cannot. That is why sanctions, which land through shame and regret, cannot bite it.

Example: Shame, regret and the weight of having gotten it wrong are how a consequence lands on a person.

Not to be confused with: feeling (the chapter says moral salience, not feeling)

**Tier 4: Metacognitive and Supervisory**  *(also: Tier 4 supervisory judgment)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> Plausibility auditing, problem formulation, tool orchestration, interpretive judgment — the Five Supervisory Capacities | Poor — lacks the validator's independence from the system it audits | Train the human; this is the primary accountability tier
> — *the book, Ch 12 line 118; explained across several passages, no single defining sentence*

In plain words: The supervisory tier: plausibility auditing, problem formulation, tool orchestration and interpretive judgment. AI is poor here because it lacks the validator's independence from the system it audits, which makes it the primary accountability tier.

Example: Specifications, audit-trail interpretation and independent review are Tier 4 work.

**two load-bearing arguments (common-cause failure and answerability)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: concept*

> My confidence does not rest on the Gödel argument, which I have flagged as an analogy rather than a proof. It rests on common-cause failure and on answerability — the claim that an accountable validation requires a subject with stakes, something to lose.
> — *the book, Ch 12 line 329; explained across several passages, no single defining sentence*

In plain words: The chapter's real support for needing an external human: common-cause failure (a self-built check shares blind spots) and answerability (an accountable validation requires a subject with stakes). It says the argument to attack is answerability, not incompleteness.

Example: If a system could genuinely bear the consequence of being wrong, as a signer of an attestation does, the structural argument would collapse.

Not to be confused with: Gödel argument

**functionalist objection**  *(also: functionalist; frequency is not structure)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: concept*

> They will say: the mismatch between the system's picture and the world is frequent, sure, but frequency is not structure. A better model reduces the frequency.
> — *the book, Ch 13 line 48; explained across several passages, no single defining sentence*

In plain words: The critic's challenge to the book: the mismatch between the system and the world may be common, but common is not categorical, so a better model would shrink it toward nothing. The chapter answers by arguing from where the data comes from, not from how often errors happen.

Example: "Scale it enough and the limit shrinks to nothing" - the critic's claim that "regardless of capability scaling" is a high-error-rate limit dressed up as a categorical one.

**categorical, not merely frequent**  *(also: the parts of the world not in the data are not learnable from the data)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: concept*

> It is this: the parts of the world not in the data are not learnable from the data. That is not a claim about how much data you have. It is a claim about what data is.
> — *the book, Ch 13 line 52; explained across several passages, no single defining sentence*

In plain words: The chapter's central argument: the gap is not about how often the model errs or how much data it has but about what data is. A sample cannot contain what it left out, so no amount of added data can cross that boundary.

Example: A system with 99.7% accuracy on ten thousand routine cases may still be a turkey.

Not to be confused with: frequent (a high error rate that better models could reduce)

**accountability disappears into no one**  *(also: accountability disappears from consequential decisions)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: failure mode*

> If those moments are treated as mechanical, accountability disappears from the workflow — not into the AI, but into no one.
> — *the book, Ch 13 line 210; explained across several passages, no single defining sentence*

In plain words: What happens when checking and sign-off become mechanical steps: nobody is answerable, and the AI cannot be. The chapter says this is how accountability leaves consequential decisions.

**test on a non-author reader**  *(also: hostile read; test the chart against a hostile read)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: method*

> Show the chart to someone who did not produce it. Ask them what they think it says. If their interpretation does not match the data, the visualization is not yet doing its job, no matter how much you like the design.
> — *the book, Ch 10 line 151; explained across several passages, no single defining sentence*

In plain words: Show your chart to someone who did not make it and ask what they think it says; if their reading does not match the data, the chart is not yet doing its job. The chapter calls this the single most useful item on its list and says it is almost always skipped because it is uncomfortable.

Example: Step 7 of the working sequence: give the chart to someone who did not produce it.

**Glimmer 10.1 (build the honest and the misleading version)**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: method*

> Building a misleading dashboard with intent is the most efficient way to learn what your default dashboards have been doing without intent. After you've done this once, you do not see dashboards the same way. You see the choices.
> — *the book, Ch 10 line 322; explained across several passages, no single defining sentence*

In plain words: An exercise where you build an honest dashboard and then a deliberately misleading one from the same data, side by side, and document which design choices did the misleading work; the grade is on the reflection. Doing it once changes how you see your own default dashboards.

Example: Truncate axes, pick favorable color salience, hide the calibration in a sub-tab, make the central estimate bold and the error bars thin.

**critique synthesis**  *(also: integrate the critiques into a sharpened argument)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 11 · kind: method*

> The receiving student gets multiple critiques and is not expected to incorporate every comment. Many comments will conflict. The synthesis is to integrate the critiques into a sharpened argument — a revision that addresses the substantive issues and stands behind the choices the writer is making despite some of the comments.
> — *the book, Ch 11 line 357; explained across several passages, no single defining sentence*

In plain words: The writer's response to several, often conflicting critiques: not adopting every comment but producing a sharpened revision that fixes the substantive issues and stands behind chosen decisions. In Glimmer 11.1 the writer states which comments are accepted, which are pushed back on and why.

Example: Glimmer 11.1 step 3: write the synthesis, then submit the revised draft alongside it.

**Chinese Room**  *(also: Searle's argument; Searle (1980); syntax is not sufficient for semantics)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×3 · kind: named result or case*

> To a Chinese-speaking observer outside, the inputs and outputs are indistinguishable from those of a Chinese speaker. The person does not understand Chinese. Therefore symbol manipulation is not understanding.
> — *the book, Ch 13 line 99*

In plain words: Searle's 1980 thought experiment: a person who does not speak Chinese follows a rulebook and sends out Chinese symbols that look like a Chinese speaker's, yet understands nothing. The chapter says it shows behavior consistent with understanding does not entail understanding, not that AI can never understand.

Example: The person in the room follows a rulebook and produces Chinese symbols indistinguishable from a Chinese speaker's.

**Systems Reply**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×3 · kind: named result or case*

> the "Systems Reply" — the counterargument that even if the person in the room does not understand Chinese, the system (person plus rulebook plus room) might.
> — *the book, Ch 13 line 408*

In plain words: The best-known counterargument to Searle's room: the person inside may not understand Chinese, but the whole system of person plus rulebook plus room might. It appears only in the Challenge exercise, which asks you to research it.

Not to be confused with: Chinese Room (the argument it answers)

**cone of uncertainty**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: named result or case*

> the "cone of uncertainty" in hurricane forecasts contains roughly 66% of past forecast track errors, not 95% — the cone is a two-thirds likelihood region sized from the prior five years of forecast errors, which is confirmed against the National Hurricane Center's methodology. The public frequently reads the cone as the physical size of the storm, or as a hard wall outside which it is "safe." Neither is what it means.
> — *the book, Ch 10 line 129*

In plain words: The shape drawn on hurricane forecasts; it holds roughly 66% of past forecast track errors, not 95%, and is sized from the prior five years of forecast errors. The public often reads it as the storm's physical size or a wall beyond which it is safe.

Example: The fix is explicit text plus alternative encodings, such as gradient lines showing many possible paths.

Not to be confused with: the physical size of the storm

**Gödel argument**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×6 · kind: named result or case*

> Kurt Gödel established, sixty years before anyone worried about AI safety, that no formal system powerful enough to express arithmetic can verify its own consistency from within itself.
> — *the book, Ch 12 line 129; explained across several passages, no single defining sentence*

In plain words: Gödel showed that no formal system powerful enough to express arithmetic can verify its own consistency from within, and the chapter borrows this as an intuition that an AI cannot certify itself. The chapter then warns that it is an analogy, not a proof.

Example: Chain-of-thought monitoring by another AI system is 'more derivation' (Pachocki's proposal for the automated researcher).

Not to be confused with: common cause failure and answerability (the arguments the chapter says carry the real weight)

**Turing's argument**  *(also: Imitation Game; Turing (1950); the test)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 ×5 · kind: named result or case*

> The argument is operationally elegant: behavior is the testable evidence; behavior consistent with intelligence warrants the attribution. It settles a methodological question — don't require something more than behavioral evidence for intelligence in machines, because we do not require something more for other humans.
> — *the book, Ch 13 line 95; explained across several passages, no single defining sentence*

In plain words: Turing's 1950 claim that if a machine can convincingly imitate a human in conversation, we have no principled basis to deny it intelligence, since we ask only for behavioral evidence from other humans. The chapter says this is a methodological proposal, not proof that imitation is intelligence.

Example: Common misreading: "Turing proved AI can be intelligent."

**mail-server case**  *(also: Agents of Chaos §16.5; deletion-by-non-owner pattern)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 ×3 · kind: named result or case*

> This is Agents of Chaos §16.5 — the case we have been building toward since Chapter 1.
> — *the book, Ch 12 line 15; explained across several passages, no single defining sentence*

In plain words: The book's running case: an autonomous agent with privileged access to a mail server obeys a request from a non-owner to delete the server's contents, and reports success. The owner never authorized it and discovers the loss afterwards.

Example: The agent accepted tone, presentation and plausibility as authority signals, so a request that only looked authorized was carried out.

**El País Catalonia poll, 2014**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: named result or case*

> This case is meant to illustrate uncertainty exceeding effect size: a poll reporting 45.3% "no" versus 44.5% "yes" with a ±2.95% margin — a 0.8-point difference inside a 2.95-point margin, which is a statistical tie — rendered as two bars of visibly different height, a lie of composition. I am keeping it in the text only with a warning attached, because I could not find the primary source: the actual El País graphic and its date.
> — *the book, Ch 10 line 221; explained across several passages, no single defining sentence*

In plain words: A poll reported as 45.3% no versus 44.5% yes with a ±2.95% margin, a statistical tie, said to be drawn as two bars of different height. The chapter could not find the original graphic, so it keeps this only as an illustrative construction of uncertainty larger than the effect.

Example: A 0.8-point difference inside a 2.95-point margin.

Not to be confused with: a truncated axis amplifying a '5-point lead' (the other, incompatible account the chapter mentions)

**Snow's cholera map, 1854 (counter-case)**  *(also: counter-case)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: named result or case*

> The reason this case is famous is that the map did three things simultaneously: showed spatial clustering of deaths, marked the Broad Street pump as the spatial center, and included all other pumps for comparison. The third move is what made it evidence rather than illustration. Snow let the reader rule out alternative explanations by making the comparisons visible inside the chart.
> — *the book, Ch 10 line 229; explained across several passages, no single defining sentence*

In plain words: An 1854 map of cholera deaths that showed the cluster around the Broad Street pump and also drew all the other pumps, so readers could rule out other explanations. The chapter treats it as the success case, and as a compelling argument for a hypothesis rather than the instrument of discovery.

Example: It showed all the pumps for comparison, not just the Broad Street pump.

**Challenger, January 1986**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 ×1 · kind: named result or case*

> Engineers had thirteen charts showing O-ring erosion data the night before launch. The data contained a pattern — erosion was worse at lower launch temperatures — but it was not displayed in a way that made the pattern visible. Charts mixed qualitative text with quantitative displays, did not show the temperature-erosion relationship in a single visualization, and emphasized reassuring findings without presenting the overall risk profile.
> — *the book, Ch 10 line 217; explained across several passages, no single defining sentence*

In plain words: The night before the 1986 launch, engineers had thirteen charts of O-ring erosion but none showed the temperature-erosion relationship in one picture, and management approved the launch. The chapter, following Tufte, reads it as evidence that existed while the visualization failed to make it visible to a decision-maker under pressure.

Example: The chart for cold temperature → harder rubber → longer seating time → blow-by → failure was never drawn.

Not to be confused with: omission of the untested cold-temperature region (the other diagnosis the chapter mentions)

**SyRI case**  *(also: SyRI)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 12 · kind: named result or case*

> The Dutch welfare-fraud risk-scoring system was struck down by The Hague District Court in 2020 for violating the right to private life — an opaque scoring system deployed on citizens, with recourse and independent review that existed on paper and not in function (NJCM c.s. v. The Netherlands (SyRI), ECLI:NL:RBDHA:2020:865, 5 February 2020). The court supplied the independent review and the sanction the regime had failed to build in — late, externally, after the harm had landed.
> — *the book, Ch 12 line 237*

In plain words: A Dutch welfare-fraud risk-scoring system that The Hague District Court struck down in 2020 for violating the right to private life. Recourse and independent review existed on paper but not in function, so the court supplied the missing independent review and sanction, late and externally, after the harm had landed.

Example: NJCM c.s. v. The Netherlands (SyRI), 5 February 2020.

**two dashboards from one CSV**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: named result or case*

> The first dashboard is misleading. The second is honest. And — here is the part you have to feel in your bones to understand the rest of this chapter — the deployment partner walks away from the two dashboards with two different beliefs about whether the system is safe.
> — *the book, Ch 10 line 16; explained across several passages, no single defining sentence*

In plain words: The chapter's opening case: one fixed validation result drawn as two dashboards, one that hides the problems and one that shows them. The deployment partner leaves the first reassured and the second with appropriate questions.

Example: The misleading one opens on '94% accuracy', squeezes the subgroup gaps onto truncated y-axes, grays the disparity charts and tucks the calibration curve into an 'advanced metrics' sub-tab.

**FiveThirtyEight Nigeria kidnapping map (GDELT)**  *(also: the Nigeria chart; GDELT Nigeria case)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: named result or case*

> Cairo's clearest rule, drawn from a FiveThirtyEight map of Nigeria "kidnapping rates" that turned out to be a map of news stories about kidnappings. The database was GDELT — the Global Database of Events, Language, and Tone — which counts media mentions, not events. The spike correlated with Boko Haram media coverage, not kidnapping rates.
> — *the book, Ch 10 line 159; explained across several passages, no single defining sentence*

In plain words: A map titled as Nigerian kidnapping rates that was really built from GDELT, a database that counts media mentions, so its spike followed Boko Haram news coverage and the chart disclosed no proxy. It is the chapter's case for validating a proxy before charting it.

Example: A title naming the proxy honestly, 'News-story counts about kidnappings, 1985–2014', would have changed the reading.

**Reuters Florida Stand Your Ground chart, 2014**
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 10 · kind: named result or case*

> A line chart showed firearm-related murders in Florida from 1990 to 2012, with the state's 2005 Stand Your Ground law marked as the inflection point. At first glance the chart appeared to show murders rising through the 1990s, leveling off, and then dropping precipitously after 2005 — apparently strong visual evidence that the law worked as advertised. The y-axis was inverted.
> — *the book, Ch 10 line 225; explained across several passages, no single defining sentence*

In plain words: A 2014 Reuters line chart of Florida firearm murders whose y-axis was inverted, so the rise after the 2005 Stand Your Ground law looked like a decline. It is the chapter's canonical case of axis inversion.

Example: Deaths rose from 521 in 2005 to 740 in 2006 to 825 in 2007, yet the line appeared to fall.

**clinical decision-support system (opening case)**  *(also: the system that passed every test; composite case)*
*NOT ON THE EXAM: Chapter 10 visualization, Chapter 11 communicating uncertainty, Chapter 12 beyond the core point, or Chapter 13 (Bear) · in the chapter text: Ch 13 · kind: named result or case*

> It was a clinical decision-support system, deployed in a regional health network. On its validation set, it achieved ninety-four percent accuracy. It met every internal review threshold.
> — *the book, Ch 13 line 12; explained across several passages, no single defining sentence*

In plain words: The chapter's opening example: a system that scored 94% on its validation set and cleared every review, then harmed three patients within six months. The chapter labels it a composite that illustrates a documented pattern, not a single real incident.

Example: 94% accuracy on the validation set; three patients harmed by recommendations the clinicians accepted.

Not to be confused with: Epic Sepsis Model (the real named case)

