# Computational Skepticism exam notes, 2026-11-19

**Executive summary.** Professor Bear made several calls today. First, a scope call: students must know what model explainability and model observability mean. They do not need specific techniques such as SHAP and LIME. Explainability, and leaving out SHAP and LIME, were already in the exam materials. Observability was on no exam list, although the book defines it in its two opening agent chapters, so today it was added to the term lists, the practice prompt and both prep guides. One question is open for Bear: his description of explainability ("to be able to know how it works") is closer to what the book calls interpretability. Second, two new films, on model explainability and model observability, go before the Shapley-heavy Key Terms: Model Explainability film, and a third film covers the impossibility theorem. Third, the impossibility theorem and rungs 1 and 2 of Pearl's ladder are on the exam. Fourth, an exam-writing rule: at least one case is a bias case in which students name which of Chapter 6's ten ways in it is; the ten ways in now have their own section on the student cheat sheet. Fifth, one multiple-answer question shows a fitted model, such as a regression line, and asks whether and where there is bias.

## Bear's words

*"More notes, I think this is more notes for computational skepticism. I think you already have this, but students need to know what model explainability means. That is to be able to know how it works. Model observability, that we're measuring things. They don't necessarily have to know particular techniques like SHAP and LIME, but they have to know what model explainability is and model observability is."*

(Dictated as "Model notes"; corrected to "More notes".)

## Scope call

| Topic | On this exam? | Bear's words |
|---|---|---|
| What model explainability is | **Yes, required** | *"students need to know what model explainability means. That is to be able to know how it works."* |
| What model observability is | **Yes, required** | *"Model observability, that we're measuring things."* |
| SHAP, LIME and other specific techniques | Not required | *"They don't necessarily have to know particular techniques like SHAP and LIME"* |

## What the book says

- **Explainability** (Ch 5 line 289): "Explainability is a property of outputs. An explainable output is one accompanied by a reason. SHAP, LIME, and counterfactuals are explainability tools."
- **Interpretability** (Ch 5 line 291): "An interpretable system is one a human can build a working mental model of, sufficient to predict the system's behavior in novel cases."
- **Observability** (Agents: Understanding Before Delegating, chapter file `00a`, line 190): "Observability is the ability to investigate behavior using the signals a system exposes. More logging is not automatically better observability."
- **Observability is not evaluation** (Agentic Loops, chapter file `00b`, line 127): "Observability helps us reconstruct what the running system did." Evaluation applies a criterion to that behavior; a complete trace can document a failure without making it a success.
- **The model-monitoring version** (Ch 2 line 396, detecting drift): a model looks equally confident while the world shifts, so dashboards of its outputs stay green; detection means watching the inputs, the outputs and above all the real outcomes. The chapter does not use the word observability here, but it is the same idea for a deployed model.

## What was already there

- **Explainability** was on the exam: in the compact term list and the shortlist (with transparency, interpretability and counterfactual explanation), in the practice prompt ("Explainability versus interpretability"), in both prep guides as a look-alike pair, and in the case checklist ("Chapter 5 ... On the exam, except LIME and SHAP").
- **SHAP and LIME** were already marked "learn them, not on the exam" in the compact list and in Part D of the shortlist. The practice prompt said not to test them "until the instructor resolves the conflicting scope documents".
- **Observability** was on no exam list.

## What changed today

- `docs/Exam terms - compact list.md` and `docs/Exam terms - shortlist.md`: **observability** added to the explainability group (now five terms) with the book's sentence; Bear's priority terms go from 115 to 116; the compact list's chapter table gets a row for the two opening agent chapters.
- `fall-2026-exam/EXAM-GENERATOR-PROMPT.md`: observability added to the working scope and as a starter note; the SHAP and LIME line now states Bear's call (the ideas are required, the techniques are not) in place of "until the instructor resolves the conflicting scope documents".
- `fall-2026-exam/HOW-TO-PREPARE.md` and `fall-2026-exam/EXAM-PREP-GUIDE.md`: one more look-alike pair, observability / evaluation, the book's own contrast.

## Two new films before Key Terms: Model Explainability

Bear, right after the scope call: *"Current video is all about Shapley value, which is great. We should still keep it, but we need one before that, specifically at a higher level around model explainability. What is it? Model observability, measuring things. What is that? How do we measure things? How do we interpret things? How do we explain things? That may be two films. Let's do a film on model explainability and one on model observability."*

- The current film is **Key Terms: Model Explainability** (https://youtu.be/qEouGybOFsE), in the exam-prep playlist. Most of its 18 minutes is SHAP and Shapley mechanics, which are not on the exam. It stays.
- Two new films go before it in the playlist: **model explainability** (what it is; how we interpret and explain a model) and **model observability** (what it is; what we measure and how). Neither is built yet.
- A third film, on **the impossibility theorem**. Bear: *"Let's make another film just on the impossibility theorem, particularly around the idea of that the world is imperfect and sometimes we need to make payoffs, trade-offs, but you as the human being have to judge which is the trade-off you want. So that's an irreducibly human task. You have to decide what you are trading off for what."* Not built yet.

## Scope call: the impossibility theorem and Pearl's ladder

Bear: *"Impossibility theorem, first two rungs of Pearl's ladder are part of the exam."* (Dictated as "Possibility theorem, first two rings of Perl's ladder"; corrected.)

| Topic | On this exam? |
|---|---|
| The impossibility theorem: when base rates differ across groups, calibration parity, equal false-positive rates and equal false-negative rates cannot all hold (Ch 7, also Ch 6) | **Yes** |
| Pearl's ladder, rung 1: association, seeing what goes with what | **Yes** |
| Pearl's ladder, rung 2: intervention, doing, what happens if we set X | **Yes** |
| Pearl's ladder, rung 3: counterfactual, imagining | Not named; to confirm |

- **Already on the lists:** the impossibility theorem and base-rate difference (compact list, Ch 6 and 7); Pearl's ladder, association, intervention, counterfactual and Rung 1. The case checklist's Chapter 6 asks "Rung 1 or rung 2: did anyone set X, or only watch it?". Chapter 6 itself teaches only rungs 1 and 2 ("Pearl's Ladder — Rungs 1 and 2").
- **Changed today:** the practice prompt's starter notes now have an impossibility-theorem note and a Pearl's-ladder note (rungs 1 and 2). Before, it had neither.

## Exam-writing rule: one multiple-answer question shows a fitted model

Bear: *"One of the multiple answers questions should show a fit of a model, like a linear regression fit, and ask, is there bias? Where is there bias?"*

- At least one of the ten multiple-answer questions shows a fitted model, such as a straight regression line drawn through data points, and its statements ask whether there is bias and where.
- What "bias" means here: systematic error, a prediction that misses in one direction on average. This is Chapter 6's definition (bias is the gap between what an estimator returns on average and the true value) applied to a fitted line. Where the fit is unbiased, the points scatter on both sides of the line. Where it is biased, the residuals (actual minus fitted) have a pattern: a straight line through curved data sits above the points in one stretch and below them in another, or one group of points sits consistently above the line.
- Good statements to judge: a high R² does not rule out bias in a region; random scatter around the line is not bias; more data of the same kind does not remove bias from the wrong model form; bias in one range of x or one group can hide inside a good overall fit.
- **Source note:** Chapter 6 defines bias for an estimator but never shows a fitted line. Reading bias from a residual pattern is in the stats cheat sheet (`decks/STATS-PROBABILITY-CHEAT-SHEET.md`, section 13, marked as added standard material) and in its section 16 on bias and variance. Bear to confirm this reading is the one he means.
- **Changed today:** the practice prompt now requires this question in every full practice exam and has a starter note on reading bias from a fit. On paper the question shows a plot; the practice coach, which may not draw, can give a small table of x, actual y and fitted y instead.

## Exam-writing rule: one case is a bias case

Bear: *"For one of the case questions, bias needs to be part of it, and having students identify the kind of bias that this is so they can appropriately identify the issue should be part of the problem."*

Then: *"In the cheat sheet, make a recommendation for the 10 ways in to be part of that cheat sheet. And that should be part of the question that I just presented to you in terms of the case study."*

- At least one of the five cases turns on a bias, and the case asks students to name **which kind of bias** it is, using the **ten ways in**: Chapter 6's ten entry points, the "Ten ways in" slides of the Bias deck. Naming the kind is how they identify the issue correctly; "it is biased" is not enough. This matches the case checklist's Chapter 6 line: say it exactly, not "it is biased".
- In the case format this is guided question 2 (the taught concept that names the defect, 2 points): in the bias case it asks which kind of bias, and how the case facts show it.
- The kinds Chapter 6 teaches (from the exam term list): selection bias and its special case sampling bias; dataset bias; label bias; biased measurement; observer bias; data-coding, data-entry and self-report bias; implicit and confirmation bias; publication bias; historical bias; structural bias; and bias in the statistical sense (an estimator's average miss). Survivorship bias is Bear's addition; the book does not use it.
- The case's facts should point to one kind, so the kind can be told apart. The checklist's deciding question is "Does it live in the sample, the labels or the structure?": who got in depended on what happened to them (selection); the labels record a biased past decision (label); the data faithfully records an unequal world (historical or structural).
- **Changed today:** the practice prompt now requires a bias case in every full practice exam, with question 2 asking which of the ten ways in it is, and its starter notes list the ten. The student cheat sheet (`interview-bank/info-7375-computational-skepticism-for-ai/ma-exams/CHEAT-SHEET.md`) has a new "Ten ways in" section, recommended for students' sheets, with each way in, where it enters and its tell. Bear's cheat-sheet notes (`decks/CHEAT-SHEET-NOTES.md`, local) have the matching entry C18.
- **Not changed:** practice exams 01 and 02 still use the older seven-case format; the word "bias" appears in exam 01 but not in exam 02.

## Also today

Claude IEU found a mistake in the practice prompt's short commands: a one-word answer to a multiple-answer question, such as "ACE", was treated as an unknown word and got the help list instead of a grade. Fixed and pushed earlier the same day.

## Still open

- **Pearl's ladder, rung 3 (counterfactual).** Bear named rungs 1 and 2. The compact list still has counterfactual as a priority term. Does rung 3 stay on the exam?

- **The 2026-11-16 rules are still not in the practice prompt:** the accuracy-claim case, phase gates, the probability-and-likelihood rule, EDA, and the robustness scope. Today's observability and bias rules are in it.

- **What "explainability" means on the exam.** Bear said explainability is *"to be able to know how it works."* The book splits this: explainability is a reason attached to an output, and interpretability is a person's working understanding of how the system behaves. "Knowing how it works" is closer to the book's interpretability. The exam materials keep the book's split for now (the practice prompt tests explainability versus interpretability). Bear to say whether to keep the split or to treat explainability in the broader sense.
- **Model observability and agent observability.** The book defines observability in its agent chapters; Ch 2's drift detection is the version for a single deployed model. These notes treat them as one idea: measuring and recording what a running system does so you can investigate it.
