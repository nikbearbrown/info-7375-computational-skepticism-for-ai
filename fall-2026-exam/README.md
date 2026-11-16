# INFO 7375 Computational Skepticism for AI: Fall 2026 exam

> **Format update, 2026-11-15:** Nik specified 5 case-style questions × 10 points = 50, plus 10 multiple-answer questions × 5 points = 50. Total: 100. Existing practice papers and their keys are preserved as historical 7-case/6-multiple-answer exercises, not current-format mock exams. The new [exam generator prompt](EXAM-GENERATOR-PROMPT.md) is a local draft with a representative independent assistant-agent check, not a live Claude Project test.

## Executive summary

The Fall 2026 exam is worth **100 points** in two parts: **5 case questions at 10 points each (50)** and **10 multiple-answer questions at 5 points each (50)**. It tests one skill: using the course's exact terms to **direct** an AI analyst and to **audit** what it hands back. Each case shows an AI analyst's confident output with **at least one planted flaw (there may be more)**; you find a real flaw (the planted one or another you can justify), name it with the right term, say what evidence would settle it, and write a better instruction. Two practice exams are in this folder, each with two files: an **exam** and a **key with the questions shown**. Practice exams are practice only: **the real exam uses different cases and different questions.**

## What the exam tests

Whether you can use the course's terms precisely. A vague worry ("the model might be biased") earns little. The exact term ("selection bias", "target leakage", "covariate shift", "demographic parity is not equalized odds") shows you could tell an AI analyst exactly what to check, and could tell when its answer does not check out. Polish does not matter: grammar, spelling and length earn nothing, so short plain answers are fine.

The exam draws on the whole course: the foundations (probability and statistics) and chapters 1 to 13. Every technical term on the exam, in both parts, is a term that the chapters or the probability-statistics lessons use and explain; a term that appears only in a glossary or a question bank is not on the exam. Prepare all of the book; you will not be told in advance which topics appear.

## Format

| Part | Questions | Points each | Total | About how long |
|---|---:|---:|---:|---|
| A. Cases | 5 | 10 | 50 | Allocate from the announced exam duration |
| B. Multiple-answer | 10 | 5 | 50 | Allocate from the announced exam duration |
| | | | **100** | Use the time stated on the examination |

The times are a pace for planning your practice. The real exam is planned to leave comfortable time beyond this pace for a prepared student, and the exam sheet states the time. The exam room rules (what you may bring) come from your instructor; practise with no notes and no AI tool.

## What a case looks like (Part A)

Every case has four pieces:

1. **A scenario.** Someone has a decision to make and asked an AI analyst for help.
2. **The instruction** that person gave the AI analyst, word for word.
3. **The analyst's output.** It reads like a confident report. It contains **at least one planted flaw** on an idea from the course (there may be more; find any real defect and justify it). (In the practice exams the outputs are author-written for illustration, not real model runs.)
4. **Five specific questions about that case**, worth 10 points together. They direct your analysis rather than ask for an open-ended essay. Each paper tailors these roles to the named claim, evidence and decision-maker:
   1. Which consequential claim or step is unsupported, and why do the case facts show a real defect? (3 points)
   2. Which precise course term names your chosen defect, and how does it apply here? (2 points)
   3. What concrete check, test or comparison would test this claim, and what result would support or defeat it? (2 points)
   4. How would you rewrite the relevant instruction to correct this analyst's work, including limits and what to report? (2 points)
   5. How would you explain the consequence to this case's decision-maker in one or two plain sentences? (1 point)

Use five short numbered answers; an essay is not required. Questions must refer to the actual case, not simply repeat a generic essay prompt. The five scoring rows below remain 3 + 2 + 2 + 2 + 1 = 10.

## Multiple-answer questions (Part B)

Each question has a short setup and **five statements, A to E**. Each statement is true or false **on its own**. You check the ones that are true.

- Each statement is worth **1 point**: checked and true, or left blank and false.
- Any number of the five can be true.
- Read each statement by itself. A strong word such as "always" or "proves" is often what makes a statement false, but a statement is not false just for sounding strong.

## How cases are scored

| What | Points | You earn it by |
|---|---:|---|
| Catches a real defect | 3 | Naming a real defect in the analyst's output **and** giving a reason that shows why it is a problem. The planted flaw(s) are the expected ones, but any real defect you can justify earns the same. 1 or 2 if the defect is real but your reason is thin or partly wrong |
| Uses the exact term | 2 | Using the course's precise term for the defect you chose (a near-miss earns 1) |
| Asks for evidence | 2 | Naming a check, test or comparison that could show your defect is real or the claim true or false |
| Gives a fix or next step | 2 | Writing a corrected instruction the analyst could follow that deals with your defect and says what to report |
| Keeps plain language | 1 | One or two sentences a non-expert could act on, saying specifically what is wrong, with no technical terms |

**The evidence and fix lines are scored against the defect you chose.** A check that does not address your own defect earns nothing on its line; one that does earns credit even if it differs from the sample answer. **If you name no real defect with a reason, the case is capped at 5 out of 10.** A bare statement such as "it is too strong" or "it cannot be trusted" is not a reason. A real but minor defect, one that could not change whether the analyst's conclusion is justified, earns 1 on the first line and at most 1 on each other line. Credit is given by line wherever it appears on your answer sheet. Concepts count, not names or dates: you are never required to remember who said something or when. Spelling, grammar, length and number of sentences earn nothing.

## How to practise

1. Pick a practice exam and do it **cold**: no notes, no cheat sheet, no AI tool. Write the short answers the exam asks for.
2. Only then open the matching key file and score yourself line by line.
3. For every line you missed, ask which term you were missing and read the "Covered in:" section named in the key.
4. Wait a few days and redo the cases you missed from memory.

## Two files for each practice exam

1. **The exam** (`practice-exam-01.md`, `practice-exam-02.md`). Questions only, no answers. This is the file to practise from: do it cold, with no notes and no AI tool.
2. **The key with the questions shown** (`-KEY.md`). Every case and every multiple-answer question is shown in full, with its key right under it. Open it after you have finished the exam, to score yourself, or use it to study how a good answer is built.

Every entry in the key ends with a **"Covered in:"** line. It names the chapter file and the section where the book teaches the idea, so you know where to read if you missed it. If the book does not teach part of an item, the line says so and names the terms the book does not use. The exam files carry no sources.

| File | What |
|---|---|
| [practice-exam-01.md](practice-exam-01.md) | Practice exam 1: 7 cases and 6 multiple-answer questions, no answers. Practise from this one |
| [practice-exam-01-KEY.md](practice-exam-01-KEY.md) | Practice exam 1 key: each case and question shown in full, then the flaw, the terms that earn credit, near-misses, acceptable evidence requests and sample answers; for each statement true or false with a reason; a "Covered in:" source for every entry |
| [practice-exam-02.md](practice-exam-02.md) | Practice exam 2: a different 7 cases and 6 questions, no answers |
| [practice-exam-02-KEY.md](practice-exam-02-KEY.md) | Practice exam 2 key, with the questions shown and a "Covered in:" source for every entry |

The question text in each key is copied from the exam file by [scripts/build-exam-with-key.py](../scripts/build-exam-with-key.py), so the two always match. Edit questions in the exam file only, then rerun the script.

The two practice exams share no case and no multiple-answer question. Together they cover every case area in the course (foundations and chapters 1 to 13), one case each.

**Practice exams are practice only.** The real exam uses different cases and different questions, and may put different chapters in the 5 cases. Doing these exams well tells you about your habits, not about what will appear.

## What to study

The book is the source: **[the chapters](../chapters/)** and the **[probability-statistics lessons](../probability-statistics/)**. The links below are study aids from outside the book. They can contain terms the book does not use, and those terms are not on the exam.

- **[CHEAT-SHEET.md](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/CHEAT-SHEET.md):** the terms on one page.
- **[GLOSSARY-jargon-midterm.md](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/GLOSSARY-jargon-midterm.md):** every tested term with a one-line meaning.
- **[question-bank/](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/question-bank/INDEX.md):** the multiple-answer bank by chapter, with keys and reasons in `questions.json`.
- **[practice-exams/](https://github.com/nikbearbrown/interview-bank/tree/main/info-7375-computational-skepticism-for-ai/ma-exams/practice-exams/):** six more multiple-answer practice exams of 20 questions each, with separate `-KEY` files. These are the Part B format only.
- **The chapters** in [chapters/](../chapters/) for every term: the exam uses only terms that the chapters and the probability-statistics lessons use.

## A note on the chapter scope

The exams folder's README describes an earlier plan, in which every question was a case and 10 of 13 chapters were chosen. The revised exam described here, 5 cases plus 10 multiple-answer questions, is the current instructor-specified format. Rely on this README for the format and on your instructor for anything it does not say.

## How to prepare

[HOW-TO-PREPARE.md](HOW-TO-PREPARE.md): a study guide for this exam: what the research says, a 14-day and a 3-day plan, how to practise the case questions and the multiple-answer questions, and the common mistakes.
