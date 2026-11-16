# Narration brief: one terminology deck becomes one narrated film

You are writing the spoken script for ONE film in the YouTube playlist **Computational Skepticism, Exam Prep** (course INFO 7375, Computational Skepticism for AI, Professor Nik Bear Brown). The film plays a terminology slide deck, animation by animation, while a narrator named Liam explains what is on screen. You write the words Liam says. You do not render anything and you do not edit the deck.

Everything lives under
`/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/` (called COURSE below). Your deck number NN is given in your task.

## What you are given

- `COURSE/youtube/exam-prep-deck-films/extract/NN/deck.json`: every slide and every click-step of the deck. For each step: `new_texts` (the words that step adds to the picture), `all_texts` (all words on the picture after the step), `anim_ms`, and `still` (a 1920x1080 picture of the slide after the step). Each slide also has `title`, `eyebrow` (its group), `evidence` (the badge: Computed, Simulation (seeded), Illustrative data, Conceptual illustration), `notes` (the deck author's speaker note), `source`, and `picture` (a plain description of the drawing).
- `COURSE/youtube/exam-prep-deck-films/extract/NN/stills/sSS-kK.jpg`: the stills. **Look at them** (Read tool): at least the last step of every slide, and any step whose words alone do not tell you what the picture shows. You must know what the viewer is looking at to explain it.
- The deck itself: `COURSE/glossary/decks/NN <title>.html`. The term dictionary is the `var T = {...}` object; each `renderXxx(el, k, anim)` function draws one slide, and `k` is the step. Read the render function when a still is unclear.
- The chapter the terms come from, in `COURSE/chapters/` (the file whose name starts with your NN and matches the deck's topic; where two files share a number, take the one that matches the deck title). Use it to understand a term the slide states too briefly. The chapter files contain some unresolved merge-conflict markers; ignore them. **Never open anything in a folder named `4TAs`.**

## What the film is

One slide = a short run of beats. **One click-step = one beat = one narration.** When a beat starts, the step's animation plays (about half a second to four seconds), then the picture holds while Liam finishes. The deck's opening title slide (slide index 0, no steps) is not narrated; the film has its own title card.

So you write one narration for every `(slide, step)` pair in `deck.json` where the slide has steps. Nothing is skipped and nothing is merged.

## Who is speaking, and how

- **Liam, in for Professor Bear.** Liam is a stand-in narrator. He refers to the professor in the third person as "Professor Bear" and never claims to be him. He rarely needs to mention him at all.
- **Register: plain, direct, skeptical, calm.** Short sentences written for the ear. No hype, no cheerleading, no rhetorical flourishes, no "let's dive in". A student should be able to repeat the sentence in an exam answer.
- **Explain, do not read.** The slide already shows the term and a one-line meaning. Liam says what the term means in plain words, points at the picture ("the red line", "the six faces", "the bar on the right"), and where it helps says how to tell the term from its look-alike. Do not recite the slide's definition line word for word.
- **Say the exact term.** Each beat names the term or terms that step adds, spelled exactly as on the slide, at least once. The exam rewards the exact term.
- **Length:** 20 to 40 words for a normal beat, up to 55 for a step that adds two or more terms. Never under 16 or over 58 (the checker fails those).
- **The first step of each slide** starts with a few words that say what the picture is, so the viewer is oriented.
- **Self-contained.** The viewer may have read nothing and watched nothing else. Never say: this chapter, the chapter, the book, the deck, slide, click, "as we saw", last or next video, or any chapter or video number. If a term leans on another idea, say that idea in a clause.
- **Honest about the numbers.** If the slide's badge is Illustrative data or Simulation (seeded), do not present its numbers as measurements of the real world. Say "in this made-up example" or "in this simulated run" once per slide where numbers are spoken. If the deck's notes say a case or a label is a composite, unverified or of limited scope, respect that.
- **No new facts.** No study, name, date, example with numbers, or claim that is not on the slide, in its note, or in the chapter. A plain everyday rewording of the idea is fine.
- **Exam talk.** You may say that the exam expects the exact term. Do not describe the exam's format. Decks 10 and 13 cover chapters marked "not on the exam": in those two films never say or imply the terms are on the exam; treat them as terms of the course.

## Writing for a text-to-speech voice (Kokoro)

- **Spell every number as words**: "ninety-nine percent", "one in ten thousand", "zero point four seven", "five hundred thousand dollars". No digits anywhere in any narration field.
- **Only speak numbers that are on the slide at that step.** For each beat list them in `figures` exactly as they appear on the slide (a substring of one of the step's `all_texts`), for example `"figures": ["0.469", "1 in 10,000"]`. The checker verifies each one is on the slide. If you round ("about forty-seven percent" for 0.469), still list `"0.469"`. A beat that speaks no number has `"figures": []`.
- **No symbols**: none of `( ) [ ] | = % $ + / * < >` and no arrows or dashes of the long kind. Write "the probability of A given B", "does not equal", "divided by".
- **Acronyms**: write them as on the slide (PPV, ECE, SHAP, LIME, FGSM). The first time one is spoken, give its expansion in the same breath ("PPV, positive predictive value").
- Avoid words the voice reads two ways: past-tense "read" (write "looked at" or "saw"), "lead" (the metal or the verb), "live", "tear", "wind", "minute" as an adjective, "close" as an adjective next to a verb use. Prefer the unambiguous word.
- Hard names: add them to `pronunciations` with a plain respelling, capitals on the stressed syllable, for example `{"term": "Shapley", "say": "SHAP-lee"}`. Do not respell inside the narration.
- Commas and full stops only. No semicolons, no colons inside narration beats except in the recap lines and checks where the pattern below shows them.

## The other pieces you write

1. `opening_summary` (8 to 40 words, one or two sentences). It is spoken on the title card right after the playlist name and the film title, so do not repeat either. Say what the film covers and why that is useful. Numbers as words.
2. `opening_description` (at most 64 characters): the short line printed on the title card under the title. Digits are fine here. Example: "33 terms for reading a probability and a calibration curve."
3. `idea`: the second beat, where a writer types a sentence a newcomer believes and corrects one phrase of it.
   - `narration` (35 to 70 words) must begin exactly `Hallo. This is Liam, in for Bear.` Then the mistaken framing, the correction, and one sentence on what the film does about it (it goes through the terms, each one shown). Do not repeat the playlist or the title.
   - `text`: what the writer types, at most two lines (`\n`) and 70 characters. `triggerWords`: the phrase that gets deleted, verbatim inside `text`, no closing punctuation. `replacementWords`: what replaces it, no closing punctuation. After the swap the sentence must be true and must be the film's main point. Example: text `A confident number\nis evidence.`, triggerWords `is evidence`, replacementWords `is a claim to check`.
4. `recap_lines`: exactly six bare sentences (4 to 16 words, at most 84 characters each), in the deck's order, each restating one thing the film established. Nothing new. Numbers as words.
5. `your_turn`: a prompt the viewer can paste into Claude to practise this film's terms without the deck in front of them.
   - `command` (35 to 75 words): spoken aloud in full, so it obeys every voice rule above. It should make the viewer USE the terms, for example ask for short cases one at a time where the viewer must name the exact term and say why its look-alike is wrong, with the answer withheld until they reply. Name six to ten of the film's terms inside the prompt.
   - `checks`: exactly two lines, each starting `Check: `, at most 78 characters, that the viewer uses to judge the result.
   - `segment`: a Title Case label of at most 40 characters, for example `Name The Term, Defend It`.

## Output

Write `COURSE/youtube/exam-prep-deck-films/extract/NN/narration.json`:

```json
{
  "deck": "NN",
  "opening_summary": "...",
  "opening_description": "...",
  "idea": {"narration": "Hallo. This is Liam, in for Bear. ...", "text": "...", "triggerWords": "...", "replacementWords": "..."},
  "beats": [
    {"slide": 1, "step": 1, "narration": "...", "figures": []},
    {"slide": 1, "step": 2, "narration": "...", "figures": ["33"]}
  ],
  "recap_lines": ["...", "...", "...", "...", "...", "..."],
  "your_turn": {"segment": "...", "command": "...", "checks": ["Check: ...", "Check: ..."]},
  "pronunciations": [{"term": "...", "say": "..."}],
  "deck_problems": ["anything on a slide that looks wrong: a number that does not add up, a typo, a term defined two ways"]
}
```

Then run the checker and fix until it prints PASS:

```
python3 COURSE/youtube/exam-prep-deck-films/tools/check_narration.py COURSE/youtube/exam-prep-deck-films/extract/NN
```

Before you finish, reread every beat once against its still: does the sentence describe what is actually on screen at that step (not a later step), and would it sound right spoken aloud?

Write only `narration.json`. Do not edit the deck, the extract, the tools or anything else. Your final message: PASS or FAIL from the checker, the body word count it printed, and the `deck_problems` you found (or "none").
