# Computational Skepticism exam notes, 2026-11-16

**Executive summary.** Today Professor Bear started building a case-study checklist, the questions to ask of any case, which are also the questions to ask on a real job. He also set exam-writing rules and made scope calls for the robustness chapter. The checklist itself is in [`glossary/CASE-CHECKLIST.md`](../CASE-CHECKLIST.md): Bear's cross-chapter questions, then the six end-of-film checks for every chapter, 1 to 13, in order. Six film fixes were noted, all in the Key Terms films; none has been made yet. The exam scope is not final: more calls are coming.

## The exam format
- 100 points. Part A: five case questions, 10 points each. Part B: ten multiple-answer questions, 5 points each.
- Each case: a scenario, the instruction given to an AI analyst, the analyst's output with at least one real defect, and five guided questions scored 3/2/2/2/1 (the defect, the concept that names it, a check, a rewritten instruction, the consequence in plain words). No real defect identified caps the case at 5/10.
- Each multiple-answer question: five statements A to E, each true or false on its own, 1 point each. Any number from zero to five may be true.

## The case-study checklist
Bear: *"So what we're going to be building over this class and maybe two classes is sort of a checklist style list. And that is for things you should be looking at in these case studies, which is also the things you should be looking at in a real job. For when you're presented a real world problem, what issues to think about."*

### 1. What exactly are we measuring? What do we care about? What do we want?
Bear: *"Part of that checklist should be, what exactly are we measuring? And what do we care about? What do we want?"*
- Is the number being measured the thing we actually want, or a stand-in for it?
- **Goodhart's law, gaming the metric:** once a measure becomes the target, people game it. When résumés are screened by keyword, applicants add the keywords whether or not they mean anything.
- Course link: problem formulation, the second supervisory capacity; label bias (ch 6); a technically right answer to the wrong question (ch 1).

### 2. What are the checks, and who does them?
Bear: *"Phase gates, what AI should be checking and doing, what a human should be checking and doing will be integral throughout the exam. One thing definitely to check is what are the checks and who is doing the checks. Are the checks there? Are the checks appropriate? And is the appropriate thing AI or human doing the checking?"*
- Are the checks there at all? Are they the right checks? Is the right party, AI or human, doing each one?
- Could each check have come out wrong? A check that can't fail checks nothing (see the falsifiability fix below).
- **This runs through the whole exam:** phase gates, and what the AI should check and do versus what a human should.
- Course links: the solve-verify asymmetry (the AI saying it checked is not an independent check), tool orchestration, agent validation, delegation and trust, human accountability.

### 3. For an accuracy claim: how did you calculate that?
Bear: *"Look up the Pangram example. I'll give you that later, the details of it. But people cherry-picking stats to make a claim about accuracy. And so if there's an accuracy question, which there should be as one of the case questions, the first thing would be, how did you calculate that? And in this case, the scenario where people used a small data set, kept on adjusting the parameters until they got a statistic that they wanted, and didn't show all of the other times where the statistics were very different, nor did they show a confidence interval or calculate power."*
- **The exam should have a case about an accuracy claim.**
- What to look for: a small dataset; settings adjusted again and again until the number came out right; the other runs, where the number was very different, not shown; no confidence interval; no power calculation.
- The Pangram example: details to come from Bear.

## Exam-writing rules
1. **Probability questions use both probability and likelihood, with dice, a 52-card deck or coins.** Bear: *"Any multiple answers probability question should involve both probabilities and likelihoods, and they should use dice, 52 card decks, or coins."* Probability: what you expect given a model (a fair coin gives heads with probability 0.5). Likelihood: how well a model fits what you saw (the chance of the evidence if the hypothesis is true).
2. **No EDA case question, but "why EDA matters" is fair for multiple-answer.** Bear: *"So there will not be an EDA case study, but EDA, in terms of why EDA is important, is a legitimate multiple answers question. And why it's important is a large percentage of your brain is good at looking at stuff. And so nobody can look at an Excel sheet of 10,000 rows and know what's going on. It has to be visualized."*
3. **Past results are evidence; they don't guarantee the outcome.** A statement that past results "guarantee nothing" is wrong in the course's framing (from the induction fix below).

## Scope calls: Chapter 4, Robustness

| Topic | On this exam? | Bear's words |
|---|---|---|
| What robustness is, what an adversarial example is, what a perturbation is | **Yes, required** | *"So for robustness, what robustness is, what adversarial is, what a perturbation is, are required"* |
| Prompt injection; natural adversarial examples | **Yes** | *"So prompt injection. Adversarial, particularly a natural adversarial attack, need to be known."* |
| White-box (gradient-based), black-box (query-based), transfer and patch attacks | No, later | *"Query-based attack, the rest of them are for later, not for this exam."* |
| The rest of the deck: FGSM and the budget, boundary tilting, PGD and adversarial training, randomized smoothing, verification and adaptive attacks, Pearl's ladder | No, later (to confirm) | as above |

Bear pointed to the Key Terms: Robustness film, about 13 minutes in (https://youtu.be/ln-iCx_fsTQ): deck 04, slide 12, "Adversarial testing and the robustness profile", whose second step lists the six attack classes.

## Film fixes noted (none made yet)
**Key Terms: The Skeptic's Toolkit** (notes in its `REVISION-NOTES.md`):
1. **Goodhart's law** (3:00): add gaming a metric, with the résumé keyword example. Bear: *"Make a note to update the video, which talks about Goodhart's Law, also in the context of gaming metrics. That is, if people are using keywords as for the resume, people just start adding those keywords when they have no real meaning to the resume to game the metric."*
2. **Falsifiability** (3:44): rework Popper around tests. If a claim can't be wrong, it can't be tested; if a test can't fail, it isn't a test. Bear: *"Rework falsifiability in that as well as to, if it's not testable, if you cannot be wrong, then it's not a test. I think the video could use that example in Popperian falsifiability. The idea is tests. And if the test cannot be wrong, then it's not a test."*
3. **The limit of induction** (5:08): "past successes guarantee nothing about the next case" becomes "past successes are evidence, but they don't guarantee the next case". Bear: *"It's true that it guarantees nothing, but I don't think that sends the right message. If the entire history is something, that's evidence for it, as a Cartesian would say, but it doesn't guarantee the outcome. So I don't frame it as guaranteeing nothing. Rather, it does not guarantee the outcome."*

**Key Terms: Robustness** (notes in its `REVISION-NOTES.md`):
4. **Say what the panda case is** at its first mention (13:59, "Three rungs for the panda case"). Bear: *"Throughout the videos, when the panda case is mentioned, also because people forget what the panda case is, talk about misclassification. Just a quick mention of the panda case if it hasn't been discussed earlier in the video."* Of the seven films that mention the panda, this is the only one that doesn't explain it first.

## The checklist document
Bear: *"The priority checklists at the end of all the videos. Let's put all those checklists in order, chapter 1, chapter 2, chapter 3, in the checklist document."* Done: [`glossary/CASE-CHECKLIST.md`](../CASE-CHECKLIST.md), 78 checks across the 13 chapters, each chapter marked with how much of it is on the exam.

## Also today, across all three courses
Bear asked for one-word short commands (help, case, question, exam, drill, topics, hint, another) in the practice-exam prompts of all three courses. They are pushed: here in `fall-2026-exam/EXAM-GENERATOR-PROMPT.md`.

## Still open
- The Pangram example: details from Bear.
- Chapter 4: does "the rest of them are for later" cover the whole deck, or only the other attack classes?
- The practice prompt (`fall-2026-exam/EXAM-GENERATOR-PROMPT.md`) doesn't yet carry today's rules: the accuracy case, phase gates, the probability-and-likelihood rule, EDA, and the robustness scope. Update it once the scope is final.
- The stats and probability cheat sheet (`decks/STATS-PROBABILITY-CHEAT-SHEET.md`, in Bear's local course folder, not in this repo), line 87, says "Probability is the likelihood of one event", which blurs the probability-versus-likelihood distinction. Suggest "the chance of one event".
