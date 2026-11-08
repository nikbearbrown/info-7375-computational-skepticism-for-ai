# INFO 7375 Computational Skepticism for AI: exams

**Status: DRAFT, built 2026-11-08. Nothing here is signed off by the instructor.** It is a snapshot of the question bank in `interview-bank/info-7375-computational-skepticism-for-ai`; that copy is the source of truth, and `interview-bank/scripts/build_exam_folders.py` rebuilds this folder from it.

## Executive summary

**What is here.** 480 multiple-answer questions (a bank by chapter), 6 ready-made practice exams of 20 questions each (120 different questions, no question repeated across forms), their answer keys with a reason for every statement, and a cheat sheet.

**How to use it.** Take a practice exam cold, mark it against the matching `-KEY` file, then follow the Why lines for anything you missed. Use the cheat sheet for the terms; the glossary has every term the bank tests.

**What the questions test.** Precise use of the course's terms, so you can tell a language model or an engine exactly what to do. Format: five statements per question; check the ones that are true. Each statement is 1 point, true or false on its own.

**What is not here yet.** Chapters outside the bank's scope (see the bank README), essay questions (retired), and the predict-the-prompt exams (pilot; see below).

## The exam: case-based, written on paper in class

The exam is a **100-point, case-based exam**. There are no multiple-answer questions on the exam itself.

- **Format.** Each question is one case from [`case-exam/`](case-exam/readme.md): a scenario, the instruction given to an AI agent, the agent's output with one flaw in it, and four probes worth 10 points. Each question is an **essay-style answer** written **in class**.
- **Materials.** Paper, pencil or pen only. **No laptop, no phone.**
- **Coverage.** The book has 13 chapters, and a 100-point exam of 10-point cases fits **10 cases**. So **10 of the 13 chapters are examined, chosen at random** by the instructor. You will not know in advance which three are left out, so prepare all 13.
- **Grading.** Teaching assistants grade by the fixed 10-point rubric in `case-exam/readme.md`; the exact use of the course's terms is what earns the points, not polish or length.
- **Practice.** The multiple-answer bank and practice exams below are for studying the terms. They are not the exam format.

## Contents

| Path | What |
|---|---|
| `question-bank/` | 17 markdown files by chapter and topic; `questions.json` (keys and explanations as data); `INDEX.md` (counts) |
| `practice-exams/exam-01.md` to `exam-06.md` | student forms, no answers |
| `practice-exams/exam-01-KEY.md` to `exam-06-KEY.md` | keys with reasons |
| `GLOSSARY-jargon-midterm.md` | every tested term with a one-line meaning |
| cheat sheet | [CHEAT-SHEET.md](CHEAT-SHEET.md) |

## Caveats

- Forms are random draws stratified across sections (seeded: same seed, same forms). They are practice, not a calibrated exam: difficulty is not balanced.
- Keys come from the bank. A statement you think is wrong is a bug in the bank, not in you: report it.
