# Second-pass check of one film's narration

A narrated film is being made from ONE terminology slide deck for the course INFO 7375, Computational Skepticism for AI. Another writer wrote the narration. Students will study for an exam from it, so a wrong definition does real harm. You are the independent second reader: check every spoken sentence against the slide and the course chapter, and correct what is wrong. You did not write it; do not assume it is right.

COURSE = `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai`. Your deck number NN is in your task.

## Read first

1. `COURSE/youtube/exam-prep-deck-films/NARRATION-BRIEF.md`: the rules the narration had to follow (how the film works, the voice rules, the output format).
2. `COURSE/youtube/exam-prep-deck-films/extract/NN/narration.json`: the narration under review.
3. `COURSE/youtube/exam-prep-deck-films/extract/NN/deck.json`: for every slide and click-step, `new_texts` (what the step adds), `all_texts` (everything on screen after it), the slide's `notes`, `evidence` badge and `picture`.
4. The stills `extract/NN/stills/sSS-kK.jpg` (Read tool). Look at one whenever the words alone do not settle what is on screen.
5. The chapter (path in your task) for what a term means in this course. It has some merge-conflict markers; ignore them. Never open a folder named `4TAs`.

## What to check, beat by beat

For every body beat `(slide, step)`:

- **True to the slide.** Every number, label and relationship spoken is on the slide at that step. Nothing is said about a later step's content as if it were visible now.
- **True to the course.** The term means what the slide entry and the chapter say it means. Watch for a definition that has drifted into a neighbouring term (the decks exist because these terms are easy to confuse), a direction reversed (which way a rate, a bias or an inequality runs), a cause and effect swapped, "always" where the chapter says "can", or a general claim the chapter makes only for one case.
- **Honest about evidence.** Numbers from a slide badged Illustrative data or Simulation (seeded) are not presented as real measurements. Scope limits in the slide's `notes` (a composite case, an unverified source, one lab, one framework) are respected.
- **No invention.** No study, person, date, example or number that is not on the slide, in its note, or in the chapter. (The expansion of a standard acronym is allowed.)
- **Brief rules.** No "this chapter", "the book", "slide", "click", no chapter or video numbers. In decks 10 and 13 nothing says or implies the terms are on the exam.

Also check `opening_summary`, `idea` (after the swap, is the sentence true and is it this film's point?), the six `recap_lines` (each must restate something the body said; nothing new), and `your_turn` (the terms it names are terms this film teaches).

## What to do about a problem

Fix it in `narration.json` yourself, changing as little as possible: one sentence, one number, one word. **Do not rewrite for style, rhythm or taste.** A beat that is correct and merely plain stays as it is. Keep every voice rule (numbers as words, no symbols, the `figures` list still accurate) and keep the checker passing:

```
python3 COURSE/youtube/exam-prep-deck-films/tools/check_narration.py COURSE/youtube/exam-prep-deck-films/extract/NN
```

If you cannot tell whether something is right (the slide and the chapter disagree, or neither settles it), do not guess: leave the beat, and list it under `unresolved`.

## Output

Write `COURSE/youtube/exam-prep-deck-films/extract/NN/verify.json`:

```json
{
  "deck": "NN",
  "beats_checked": 50,
  "corrections": [
    {"slide": 4, "step": 2, "was": "the full old narration", "now": "the full new narration", "why": "one sentence: what was wrong and what settles it (slide text or chapter passage)"}
  ],
  "bookend_corrections": [{"field": "recap_lines[3]", "was": "...", "now": "...", "why": "..."}],
  "unresolved": ["slide 9 step 3: the slide says X, the chapter says Y; narration follows the slide"]
}
```

Empty lists are a fine result if the narration holds up; do not manufacture corrections. Your final message: the checker's last line, the number of corrections, and each correction and unresolved item in one line.
