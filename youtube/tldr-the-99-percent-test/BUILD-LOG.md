# BUILD-LOG — tldr-the-99-percent-test

## Executive summary
A `tldr` film of chapter 2 of INFO 7375 Computational Skepticism for AI, section S1 "The Test That Is 99% Accurate". A 99% accurate test, a disease 1 person in 10,000 has, one positive result: the chance of disease is about 1%. The film earns that by counting 10,000 people as a grid and gathering every positive into one pile of 101 (1 sick, about 100 healthy), and only then names it Bayes' theorem, with the base rate on top. Structure: two TL;DR cards, the hesitant writer, TERMS, ten pure-Manim LEARN beats on the 3Blue1Brown template, then the your-turn close. Narration is Liam in for Bear (Kokoro `am_onyx`), greeting "Ahoj" (Czech). Master 5:04, all gates PASS. Not staged, not published; waiting on Bear's verdict.

## Decision log
- **GATE S:** Bear signed S1 on 2026-09-23 (in the 13 first picks). The reel folder was listed as existing but was missing on disk, so it was created fresh.
- **Greeting:** Ahoj (Czech), not used by any earlier tldr film (used so far: Ciao, Hola, Hej, Merhaba, Sawubona, Jambo, Namaste, Konnichiwa, Salut, Bonjour, Kia ora). The Wagwan rule does not fire: the slug's char-sum mod 10 is 4.
- **The representation (B14):** the population, counted: 100×100 squares, one per person. Figure 2.5 rebuilt. The grid is drawn as ten one-VMobject bands (10,000 Mobjects would crawl).
- **The collision (B16):** the sick square and 100 seeded false positives light up, then every lit square flies into the pen and packs into 101. The knob falls from '?' to ≈ 1%.
- **The 0.0098 vs 0.0099 question:** the chapter prints both values without reconciling them. B18 shows both and says why in one sentence: the count lets the test catch the sick person for certain.
- **Simplification marked once:** "one number, two jobs — simplified" (B12). This is the chapter's sensitivity/specificity note from the HEAD side of the line-258 merge block.
- **Scale shift (B19):** the sepsis-model external validation (18% alerted, two thirds missed), taken from the chapter's Wong et al. 2021 citation. The product name is kept off screen.
- **B19 lift:** Figure 2.6's before/after bars are rebuilt to scale, with a 98× taller after-bar.
- **Merge conflicts:** everything comes from the HEAD side. Nothing comes only from d78899b.
- **Numbers left out:** the chapter's domain base-rate table (fraud, security, moderation, jailbreak ranges given without sources). It was not needed.

## Gate history
- GATE BOOKEND: PASS (at sheet and at final).
- Audio: 17 mp3s, 304.2 s. B00/B01/B03 `durationSeconds` come from measured audio. B00/B01 cues are placed on the spoken clauses by char position (the first cue is on the question/lead). BOUT is apadded 1.0 s, and `actual_duration_s` = 5.267 from ffprobe.
- Gate F: FACTCHECK (22 rows), SHOTLIST, PROMPTS, CHECKS-REPORT (Gate-1 table), SOURCES, README, BUILD-PROMPT and build_srt.py were all written before any render.
- Gate A: B14–B17 failed once with a NameError on `np` (the stub does not export numpy), fixed with an explicit `import numpy as np`. After that, 10/10 clean. Gate W: 10/10 clean. Layout audit (`--curve-strict`): 10/10 CLEAN.
- Low-res contact sheet, round 1: the pen label collided with the facts line and the B17 denominator ran off the right edge. Fixes: facts leave at B15, the pen moved up, the B17 formula spans the full width over the pile, the rail leaves in B17, the B18 glossary meaning column moved right, and the dots moved clear of text.
- 4K run 1: Gate V had 8 MAJOR `low-contrast` findings on B12/B14/B15/B16, because the 10,000 pale squares pulled the mean ink luminance down. Fix: the unlit-person colour went from #CBC5B5 to #A39E8E. Only B11–B17 were re-rendered.
- 4K run 2: Gate V 0/0, 17/17 slots.
- `art final`: **GATE T PASS** (0 FAIL). There are three §8.10 advisories (B00/B01/BVDT narration recites the card). These are expected for TL;DR cards and match the exemplar.
- Master frame check: B00 at 50% shows only line 1 and at 90% shows all three lines. B01 at 50% shows only dash 1 and at 90% shows all three. B02 at 90% reads "…is a positive to mean disease?", so the correction is on screen.

## Master — 2026-09-23 12:47
`exports/landscape/tldr-the-99-percent-test.mp4`: 3840×2160, 24 fps, AAC 48 kHz, 304.5 s (5:04), sha256 48ae1e37c3bafd43… Not staged, not published. To stage: `stage_publish.py` → `build_srt.py` (full-text captions) → `art post --no-topaz`, on Bear's word only.


## Published — 2026-09-24
Bear: "Looks great" + publish runbook. Staged via `art post --no-topaz` (full-text SRT first), TOPOST gate + sha assert PASS, uploaded **unlisted** → https://youtu.be/xVxzt7rXEXA, playlist Claude & Agentic AI, captions attached. Logged in `books/youtube/PUBLISH-LOG.md`. Public flip: Bear, in Studio.
