# Draft sets: prompting and causation (rungs 1 and 2)

**Status: DRAFT, built 2026-11-08. Nothing here is signed off by the instructor, and no person has checked the new questions.**

## Executive summary

**What is here.** Two 20-question practice sets in the same five-statement format as the six statistics exams, each with a key and a reason for every statement: a **prompting exam** and a **causation set** limited to association, intervention and why the difference matters. Plus a list of six bank questions that go beyond rungs 1 and 2.

**Why.** The six existing exams are good for statistics but draw 107 of 120 questions from the bank's Foundations sections and have nothing on prompting. The instructor said causation needs only rungs 1 and 2 and why they matter, and that the glossary lists what students should know over time, not what is on this week's exam.

**What is not done.** No person has reviewed these. The new questions are written from chapters 2, 5 and 6 and the bank's jargon-rewrite questions, not from an instructor's list. Chapters 8 to 13 still have no questions.

## Files

| File | What |
|---|---|
| `prompting-exam.md`, `prompting-exam-KEY.md` | 20 new questions on writing prompts that can be checked |
| `causation-rungs-1-2.md`, `causation-rungs-1-2-KEY.md` | 10 questions from the bank (`MA-ch06.52` to `.86`) and 10 new, on rungs 1 and 2 |
| `CAUSATION-FLAGS.md` | six chapter-6 bank questions past the instructor's scope |
| `new_questions.py`, `build.py` | the new questions as data; `python3 build.py` rebuilds both sets (seeded) |

## What the prompting exam covers
Make a vague request exact (name the metric, data and baseline); specify the direction of a conditional and supply the base rate; say what is missing instead of guessing; ground truth outside the model; ask for work that can be checked (shown steps, code you run, stated assumptions); rewrite bias, fairness, interval, data-check and shift requests with exact terms; split a compound task; predict before you run; change one thing at a time; check against an outside source; ask for the falsifier and rival explanations; delegate to an agent with limits and an independent check; keep the test set untouched; name the baseline for a score.

## What the causation set covers
Rung 1 as a conditional probability from records; why association is not enough for a decision; decisions as interventions; randomization as the route to rung 2; confounders; why attribution tools and predictive models live on rung 1; sorting questions into association and intervention; a skeptic's check on a vendor's causal claim; and prediction models used to choose actions. No counterfactuals, potential outcomes, colliders or mediators.

## Caveats
- The bank's source of truth is `interview-bank/info-7375-computational-skepticism-for-ai`; the new questions live only here. If you keep them, add them to the bank.
- The number of true statements per question varies from 1 to 4, as in the bank. A reader may still find patterns; shuffle when you finalize.
- Some prompting statements encode good practice rather than a fact from a chapter (for example asking a model to show its steps). Check that each matches what you teach before using them.
- A question you think is wrong is a bug in the draft; the Why lines say what each statement is meant to test.
