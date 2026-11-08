# INFO 7375 Computational Skepticism for AI: Fall 2026 exam

## Executive summary

The Fall 2026 exam is worth **100 points** in two parts: **7 case questions at 10 points each (70)** and **6 multiple-answer questions at 5 points each (30)**. It tests one skill: using the course's exact terms to **direct** an AI analyst and to **audit** what it hands back. Each case shows an AI analyst's confident output with **one planted flaw**; you find it, name it with the right term, say what evidence would settle it, and write a better instruction. Two practice exams are in this folder, each with a **separate answer file** so you cannot see answers while you work. Practice exams are practice only: **the real exam uses different cases and different questions.**

## What the exam tests

Whether you can use the course's terms precisely. A vague worry ("the model might be biased") earns little. The exact term ("selection bias", "target leakage", "covariate shift", "demographic parity is not equalized odds") shows you could tell an AI analyst exactly what to check, and could tell when its answer does not check out. Polish does not matter: grammar, spelling and length earn nothing, so short plain answers are fine.

The exam draws on the whole course: the foundations (probability and statistics) and chapters 1 to 13. The multiple-answer part draws on the question bank, which covers the foundations and chapters 1 to 7. Prepare all of it; you will not be told in advance which topics appear.

## Format

| Part | Questions | Points each | Total | About how long |
|---|---:|---:|---:|---|
| A. Cases | 7 | 10 | 70 | 7 minutes a case, about 50 minutes |
| B. Multiple-answer | 6 | 5 | 30 | 3 minutes a question, about 18 minutes |
| | | | **100** | about 70 minutes of writing |

The times are estimates for planning your practice, not a stated exam length. The exam room rules (what you may bring) come from your instructor; practise with no notes and no AI tool.

## What a case looks like (Part A)

Every case has four pieces:

1. **A scenario.** Someone has a decision to make and asked an AI analyst for help.
2. **The instruction** that person gave the AI analyst, word for word.
3. **The analyst's output.** It reads like a confident report. It contains **one planted flaw** on an idea from the course. (In the practice exams the outputs are author-written for illustration, not real model runs.)
4. **Four questions** worth 10 points together:
   1. What is wrong, and what is the exact term for it? (5 points)
   2. What one check, test or comparison would turn the claim into evidence? (2 points)
   3. Write the corrected instruction you would send the analyst. (2 points)
   4. Explain the problem to the decision-maker in two sentences, with no jargon. (1 point)

## Multiple-answer questions (Part B)

Each question has a short setup and **five statements, A to E**. Each statement is true or false **on its own**. You check the ones that are true.

- Each statement is worth **1 point**: checked and true, or left blank and false.
- Any number of the five can be true, from none to all five.
- Read each statement by itself. A strong word such as "always" or "proves" is often what makes a statement false, but a statement is not false just for sounding strong.

## How cases are scored

| What | Points | You earn it by |
|---|---:|---|
| Catches the flaw | 3 | Saying, in any words, what is actually wrong with the analyst's claim or method |
| Uses the exact term | 2 | Using the course's precise term (a near-miss earns 1) |
| Asks for evidence | 2 | Naming a check, test or comparison that could show the claim true or false |
| Gives a fix or next step | 2 | Writing a corrected instruction the analyst could follow: specific, uses the term, says what to report |
| Keeps scope and plain language | 1 | Two plain sentences a non-expert could act on, saying what the claim supports and what it does not |

**If you miss the planted flaw, the case is capped at 5 out of 10.** A fluent list of correct-sounding terms aimed at the wrong problem cannot pass. Credit is given by line wherever it appears on your answer sheet, so a good check named in question 3 still counts for evidence. Concepts count, not names or dates: you are never required to remember who said something or when.

## How to practise

1. Pick a practice exam and do it **cold**: no notes, no cheat sheet, no AI tool. Write the short answers the exam asks for.
2. Only then open the matching answer file and score yourself line by line.
3. For every line you missed, ask which term you were missing and look it up in the glossary.
4. Wait a few days and redo the cases you missed from memory.

| File | What |
|---|---|
| [practice-exam-01.md](practice-exam-01.md) | Practice exam 1: 7 cases and 6 multiple-answer questions, no answers |
| [practice-exam-01-KEY.md](practice-exam-01-KEY.md) | Answers for practice exam 1: for each case the flaw, the terms that earn credit, near-misses, acceptable evidence requests and a sample answer; for each statement true or false with a reason |
| [practice-exam-02.md](practice-exam-02.md) | Practice exam 2: a different 7 cases and 6 questions, no answers |
| [practice-exam-02-KEY.md](practice-exam-02-KEY.md) | Answers for practice exam 2 |

The two practice exams share no case and no multiple-answer question. Together they cover every case area in the course (foundations and chapters 1 to 13), one case each.

**Practice exams are practice only.** The real exam uses different cases and different questions, and may put different chapters in the 7 cases. Doing these exams well tells you about your habits, not about what will appear.

## What to study

- **[CHEAT-SHEET.md](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/CHEAT-SHEET.md):** the terms on one page.
- **[GLOSSARY-jargon-midterm.md](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/GLOSSARY-jargon-midterm.md):** every tested term with a one-line meaning.
- **[question-bank/](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/question-bank/INDEX.md):** the multiple-answer bank by chapter, with keys and reasons in `questions.json`.
- **[practice-exams/](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/practice-exams/):** six more multiple-answer practice exams of 20 questions each, with separate `-KEY` files. These are the Part B format only.
- **The chapters** in [chapters/](../chapters/) for anything the glossary leaves unclear.

## A note on the chapter scope

The exams folder's README describes an earlier plan, in which every question was a case and 10 of 13 chapters were chosen. The exam described here, 7 cases plus 6 multiple-answer questions, is the Fall 2026 format. Rely on this README for the format and on your instructor for anything it does not say.
