# BUILD-LOG — tldr-where-the-human-steps-fall

## Executive summary
This is a `tldr` film of INFO 7375 Computational Skepticism, chapter 9, section S3, "Where the Human Steps Fall". It uses the chapter's worked Research Paper Summarizer and its six-step Boondoggle Score: the AI owns parse, extract and format; a human owns taxonomy, audit and sign-off.

The film opens with two TL;DR cards, the hesitant writer ("look like the most work" → "are cheap to check and undo") and four prerequisite terms. Then come ten pure-Manim LEARN beats:
- six step boxes with schematic "looks like work" bars; the humans get the three short bars;
- step 3's check is a string search;
- step 4 catches five dropped words, "on the training set only";
- "just glance" lets the qualifier reach the reader;
- five questions replace the bars, and the viewer is asked to commit;
- the collision: every effort bar morphs into its five-cell risk column, and the dark columns land exactly under the human boxes;
- the two AI → human seams;
- the name: the five Boondoggle questions;
- the missing Step 7 and the instrument's own limit.

Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Bula, Fijian). The master is 5:13 and all gates PASS. Verdict pending; not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick on 2026-09-23 (the 13 first picks).
- **Greeting:** Bula (Fijian), assigned centrally by the coordinator after parallel builders collided on Vanakkam and Kumusta. The Wagwan rule does not fire (slug char-sum mod 10 = 4).
- **The one representation:** under each step, a five-row grid (verification · stakes · distribution · reversibility · audit trail). A light cell is a small dim square and a dark cell is a large ink square. It replaces the "looks like work" bar. The `_Stage` state factory carries the boxes, bars and columns across B10–B19.
- **Figures 9.2–9.3** have captions only (no image files), so the six-step timeline was rebuilt from the captions and the STEP 1–6 text (REBUILD LAW).
- **Our reading, marked:** the chapter prints the five questions and one justification per step, but no per-step grid. Every cell is the film's reading of the chapter's own step text. FACTCHECK rows 16–20 cite the source for each dark cell. The screen carries "cells: our reading of the text" (Gate W's W7 refused "…of the chapter"). The effort bars are captioned "schematic". The B11 paper sentence is constructed around the chapter's quoted words and captioned "constructed sentence".
- **LOW, not HIGH:** the worked entry is tagged LOW, following the chapter's own Disclosure ("2 LOW-confidence entries reviewed and corrected (Methods: AI dropped … qualifier)"). The HIGH spot-check (1 in 5) is shown separately.
- **No equation lands**, so there is no TANGENT. The tenth slot is B17, a post-shift INSTANCE (the two AI → human seams).
- **Overtrust:** the film makes no prevalence claim. The body refuses "the dominant failure mode"; Exercise 9 misstates the body.
- **Left out:** the Disclosure's model name ("GPT-4 API"), because it is datable.
- **Course credit** is spoken in B00 and shown on the cards' course line.
- **Helpers reused:** `lock_cards.py` (from tldr-both-audits-were-right, new anchors) and the `_until(phrase)` pacing helper. `lock_cards.py` must be re-run after any `make_sheet.py` run.

## Gate history
- `bookend_check.py`: PASS at sheet time and after every sheet change.
- Gate F content (`factcheck_check.py`): clean, 31 rows.
- Audio: 17 mp3s, 311.4 s + BOUT pad. The BOUT mp3 was apad-padded by 1.0 s, so `actual_duration_s` = 4.2 (ffprobe). `lock_cards.py` set:
  - B00 cues 1.5 / 8.92 / 14.38 / 17.86;
  - B01 cues 0.8 / 5.81 / 9.47 / 13.39;
  - B00/B01/B03 `durationSeconds` from the measured audio.
- Gate A ×10 clean. Gate W: 9 clean, and B14 failed W7 (the word "chapter" in a caption). The caption was reworded and B14 is now clean.
- Layout audit (`--curve-strict`): errors in B10, B11, B16 (terracotta dots touching words) and B12 (the HIGH text running into its squares), plus a B17 warning (a label past the safe area). Dots moved and text re-placed, then 10/10 CLEAN.
- Low-res contact sheet (25/50/60/92%), fixes made:
  - B17's two seam labels collided, so they were re-centred and set in regular weight;
  - B11 "citation" touched its quote, so the panel moved right (PX −4.35);
  - B11 "· LOW" touched the claim, so it moved to x 1.8;
  - B11's check landed after the beat ended, so it now lands on "Seconds";
  - `_finish` minimum hold went from 1.0 to 0.3 s (scenes had overrun their audio by 0.5–0.8 s).
- `art run` #1: 17/17 slots, **Gate V 2 MAJOR `underfill`** (B10 at 50%: 24%; B11 at 50%: 52%). Fixes: B10's bars now grow with each box as it is named; B11's panel labels and caption land at the start.
- `art run` #2: Gate V 0 / 0.
- `art final` #1: **GATE T PASS**. Master frame check: B00 at 50% shows only line 1, and at 90% all three lines. B01 at 50% shows dash 1, and at 90% all three dashes. B16 at 95% shows every column filled, with the dark columns under the ink boxes. **B02 at 90% FAILED review:** the writer was still typing "look". The Remotion writer holds each keystroke for at least one frame (≈ 42 ms at 24 fps), so charMs 22 effectively runs at about 42. Fix: dropped the first line ("One summarizer, six steps."); the text is now "Hand the AI the steps that / look like the most work?". B02 was re-rendered.
- `art run` #3: Gate V 0 BLOCKER / 0 MAJOR, 17/17 slots. `art final` #2: **GATE T PASS** (0 FAIL; §8.10 advisories on B00/B01, where the cards recite the narration by design). Master frames at B02 60% and 90% both read "Hand the AI the steps that are cheap to check and undo?".

## Manuscript notes (for Bear — not fixed in the chapter)
- **Exercise 9 vs the body:** Exercise 9 says "the chapter claims that overtrust is the dominant failure mode". The body explicitly refuses that claim.
- **Qualifier wording:** STEP 4 quotes the dropped qualifier as "on the training set only", but the Disclosure's Step 3 entry says "on training data only". The film uses the STEP 4 wording.
- **No per-step grid:** the Boondoggle Score gives each step a capacity label and a justification but no per-question scoring. A reader cannot see which of the five questions pushed Step 1, 4 or 6 to a human without reconstructing it, as this film does.
- **Missing figures:** Figures 9.2–9.4 are referenced but have no image files in `images/`.

## MISSING / open
- Human sign-offs pending: FACTCHECK (GATE F) and the watch-the-cut verdict.

## MASTER — 2026-09-23 15:01
`exports/landscape/tldr-where-the-human-steps-fall.mp4`: 3840×2160, 24 fps, H.264 + AAC, 312.7 s (5:13), sha256 38ccb1c79ea3b06a…. Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
