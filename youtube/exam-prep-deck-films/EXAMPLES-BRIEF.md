# Example pass: every abstract term gets a concrete example

You are revising the narration of ONE narrated film made from a terminology slide deck for the course INFO 7375, Computational Skepticism for AI (Professor Nik Bear Brown). The film plays the deck step by step while a narrator, Liam, explains each term. Students use it for exam prep; the exam is built from case studies.

COURSE = `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai`
FILMS = `COURSE/youtube/exam-prep-deck-films`
Your deck number NN is in your task.

## What Bear asked for (2026-11-12, dictated)

"It's fine for these to be longer, but we need some examples. [You] can['t] just say contingent failure and this and that without giving an example. So feel free to use examples. It's fine the way it is in terms of saying things abstractly; once you say something abstractly, then give it an example. Try to keep the examples to things related to job search and what we're doing with the [course]."

So: keep each beat's abstract definition as it is, then follow it with one concrete example. Examples come from **job search** and the **AI tools for job search** the course works with: a job seeker, a résumé, a cover letter, job listings, an application, an interview, a recruiter, an applicant-tracking system that screens résumés, an AI agent that finds listings, scores them for fit, tailors a résumé, drafts a cover letter, fills in applications or sends them, a model that predicts who gets an interview, a salary estimate, a job-market report.

## Read first

1. `FILMS/NARRATION-BRIEF.md`: all voice and honesty rules still apply (numbers as words, no symbols, no "this chapter", "slide" or "click" as presenter talk, etc.). One exception: the word cap, below.
2. `FILMS/extract/NN/narration.json`: the current script. It has already been checked, and some beats carry changes Bear asked for (listed in your task). Keep those.
3. `FILMS/extract/NN/deck.json`: the words on screen at every step, and each slide's notes and evidence badge. Stills are in `FILMS/extract/NN/stills/`; look at them when you need to know what is on screen. If `FILMS/decks/` holds a film copy of your deck, that copy is what the film shows.
4. The chapter named in your task, for what each term means in this course. It has some merge-conflict markers; ignore them. Never open a folder named `4TAs`.
5. For the bar Bear wants, read the finished example pass in `FILMS/extract/01/narration.json` (beats on slides 2 to 10). Those examples are not all job-search ones; yours should be.

## The rules for an example

- **Every term gets one.** For each beat that introduces a term (a step that adds a term entry; check `new_texts` in deck.json), the beat ends with one concrete example of that term, introduced with "For example," or "Picture ...". A beat that adds two terms gives one short example for each, or one example that shows both.
- **Concrete** means a specific situation a student can picture: a person, a document, a decision, a tool doing a particular thing. "A résumé-screening model trained on last year's hires" is concrete; "a system in some domain" is not.
- **Job search first.** Use job search and AI job-search tools wherever the term allows. If a term truly cannot be shown honestly with a job-search case, use the plainest everyday case instead, and say so in your final report. Do not twist a term to fit.
- **True to the term.** The example must be a real instance of the term as the slide entry and the chapter define it, and must not fit the slide's look-alike (its TELL THESE APART box) better than the term itself. This is the most important rule: a vivid example of the wrong term teaches the wrong answer on an exam.
- **Vary them.** Do not reuse the same situation for every term; a student should meet many different job-search moments.
- **Keep the slide.** Keep what each beat says about the picture on screen and the exact term. Trim words elsewhere if needed. If the slide already shows a concrete real case (a named case from the chapter), it may serve as the example only if it is clearly an instance of the term; otherwise add one.
- **No invented facts.** No numbers in an example unless that exact figure is on the slide at that step (and then list it in `figures`). No named companies, studies, people or dates unless they are on the slide or in the chapter. A plain made-up situation ("a job seeker", "a recruiter", "an agent that sends applications") is fine.
- Beats on the map slide (slide 1), the look-alike pairs, "Say it exactly" and the closing checklist do not need new examples unless a term in them is left abstract. Leave recap_lines, idea, opening_summary and your_turn alone unless the task says otherwise.

## Length

Set `"body_max": 90` at the top level of narration.json (if it already has a larger value, keep the larger one). Term beats will typically land between 50 and 85 words.

## Finish

Back up the current script first to `FILMS/extract/NN/narration.before-job-examples.json`. Then run:

```
python3 FILMS/tools/check_narration.py FILMS/extract/NN
```

and fix until it prints PASS. Read each changed beat aloud in your head: plain, short sentences for the ear.

Write only `FILMS/extract/NN/narration.json` (and the backup). Final message: the checker's PASS line, then one line per changed beat, "slide.step term: the example", and a list of any term you could not give a job-search example (with the example you used instead).
