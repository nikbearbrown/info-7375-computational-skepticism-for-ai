# Computational Skepticism exam notes, 2026-11-19

**Executive summary.** Professor Bear made one scope call. Students must know what model explainability and model observability mean. They do not need specific techniques such as SHAP and LIME. Explainability, and leaving out SHAP and LIME, were already in the exam materials. Observability was on no exam list, although the book defines it in its two opening agent chapters, so today it was added to the term lists, the practice prompt and both prep guides. One question is open for Bear: his description of explainability ("to be able to know how it works") is closer to what the book calls interpretability.

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

## Also today

Claude IEU found a mistake in the practice prompt's short commands: a one-word answer to a multiple-answer question, such as "ACE", was treated as an unknown word and got the help list instead of a grade. Fixed and pushed earlier the same day.

## Still open

- **What "explainability" means on the exam.** Bear said explainability is *"to be able to know how it works."* The book splits this: explainability is a reason attached to an output, and interpretability is a person's working understanding of how the system behaves. "Knowing how it works" is closer to the book's interpretability. The exam materials keep the book's split for now (the practice prompt tests explainability versus interpretability). Bear to say whether to keep the split or to treat explainability in the broader sense.
- **Model observability and agent observability.** The book defines observability in its agent chapters; Ch 2's drift detection is the version for a single deployed model. These notes treat them as one idea: measuring and recording what a running system does so you can investigate it.
