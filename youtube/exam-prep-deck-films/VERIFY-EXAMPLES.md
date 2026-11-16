# Second-pass check of the job-search example pass

COURSE = `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai`; FILMS = `COURSE/youtube/exam-prep-deck-films`. Your deck number NN, its chapter file and anything specific are in your task. Never open a folder named `4TAs`.

Read `FILMS/VERIFY-BRIEF.md` and `FILMS/EXAMPLES-BRIEF.md`. A writer has just added a concrete job-search example after each term (Bear: "once you say something abstractly, then give it an example", examples from job search). The previous, already-checked version is `FILMS/extract/NN/narration.before-job-examples.json`; the new one is `FILMS/extract/NN/narration.json`. Compare them and check only what changed.

For every new example check, above all:
1. It is a TRUE instance of the term as the slide entry (`FILMS/extract/NN/deck.json`; stills in `FILMS/extract/NN/stills/`) and the chapter define it.
2. It does not fit the slide's look-alike term (its TELL THESE APART box) or a neighbouring term in the same deck better than the term itself. A vivid example of the wrong term teaches the wrong exam answer.
3. Any direction is right (which rate, which group, which way an effect or a failure runs).
4. It invents no numbers (only figures on the slide at that step), studies, companies or named people.
5. The abstract part of the beat and its description of the picture were not damaged, and changes Bear asked for earlier (named in your task) are intact.

Fix real errors with the smallest edit; do not rewrite for style or swap a good example for one you prefer. Keep the checker passing:

```
python3 FILMS/tools/check_narration.py FILMS/extract/NN
```

Overwrite `FILMS/extract/NN/verify.json` in VERIFY-BRIEF's format (`beats_checked` = number of changed beats). Then, only if the checker prints PASS, create the empty file `FILMS/extract/NN/READY` (that starts the film's build). Final message: the checker's last line, each correction in one line, each unresolved item in one line.
