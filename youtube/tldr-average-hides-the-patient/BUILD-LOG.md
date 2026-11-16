# BUILD-LOG — tldr-average-hides-the-patient

## Executive summary
This is a `tldr` film of INFO 7375 Computational Skepticism for AI, chapter 11, section S2 "Where the Average Hides the Patient". It asks how a model can have a calibration error of 0.018 overall and 0.103 on 95 rare-disease patients, both true at once.

The film has two TL;DR cards, the hesitant writer ("calibrated for every patient?" → "calibrated group by group?"), four terms, ten pure-Manim LEARN beats and the your-turn close. The LEARN beats run in this order:
- the chapter's table, drawn as columns;
- the naive "average of the rows" (0.053, the wrong number);
- the columns resize to patient counts, so the rare row becomes a sliver;
- a predict beat;
- the sliver pours into a hairline (it can never move the global by a hundredth), then is lifted onto its own 95 at 0.103;
- only then the name, subgroup calibration error (ECE_g), and its tangent.

Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Salaam, as assigned). Measured narration is 5:48. Master status: see the last section. Not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick 2026-09-23 (the 13 first picks).
- **The one representation:** width = patients, height = error, area = how loudly a row speaks in the global. The `_Stage` state factory has three width modes: `one` (the report's single bar), `equal` (the rows as the table prints them) and `patients`. The same five columns persist from B10 to B19, and B19 re-splits the hook's bar.
- **The collision (B16):** the rare row's area poured over all 12,955 patients is a film 0.0008 thick. At the worst possible error it is 0.0073, still under a line one hundredth above the global. Divided by its own 95, it is 0.103. The worst-case bound is our derivation (triangle inequality, same bins), asserted in code and marked "derived" in FACTCHECK.
- **Illustrative table:** the chapter's subgroup table cites no dataset. It is captioned once on screen ("an illustrative table", B10) and never tied to the sepsis model. The sepsis case (Wong et al. 2021) appears only in B01, as "a widely used sepsis alert", with no product named.
- **Kept out:** the global base rate (does not reconcile, below), MCE, the chapter's two `[verify]` items (ECE thresholds; "overconfidence dominant in LLMs"), AUC/PPV.
- **Pooled vs weighted:** the patient-weighted mean of the rows is 0.028, but the global prints 0.018. This is explained in one tangent line: with shared bins the pooled number can only sit at or below that mean, because opposite gaps cancel. The film says "can", since the chapter does not state its binning.
- **Greeting:** Salaam (Arabic/Farsi), assigned. No tldr sheet had used it.
- **Course credit** is spoken in B00 and shown on the cards' course line. Gate W forbids "chapter" on a Manim slide, so on-screen captions say "an illustrative table" and "the flag: above twice global".
- **Merge conflicts:** everything used sits outside the chapter's seven conflict blocks, so no side needed choosing.

## Gate history
- `make_sheet.py` → 17 beats; `bookend_check.py` PASS.
- Paperwork (FACTCHECK 29 rows, SHOTLIST, PROMPTS, CHECKS-REPORT with the Gate-1 table, SOURCES, README, BUILD-PROMPT, build_srt.py) was written before any render. `factcheck_check.py` is clean.
- Audio: 17 mp3s, 347.3 s. BOUT was apad-padded 1.0 s, so `actual_duration_s` = 4.58 from ffprobe. `lock_cards.py` (copied from tldr-both-audits-were-right with new anchors) set B00/B01/B03 `durationSeconds` and put the cues on the spoken clauses: B00 1.5 / 6.71 / 16.14 / 21.62, B01 0.8 / 7.21 / 11.17 / 17.77.
- Pre-audit:
  - Gate A ×10 clean.
  - Gate W: W7 CHAPTER-ON-SLIDE on B10/B11/B12 captions, reworded, then clean ×10.
  - Layout audit (`--curve-strict`): two dots touching bold text (B10, B19), moved, then clean ×10.
- Low-res contact sheets, two rounds. Fixes:
  - Seams in the fused one-bar were hidden with a 1 px same-colour stroke.
  - Early notes were added to B10/B11/B14 so no midpoint frame is underfilled.
  - Every text reveal was moved clear of its clip's 50% frame (B15, B17 and B18 use a longer `_until` lead; B19 was reordered).
  - B17's stray parked square became the rare sliver, which then flies into the underline under N_g.
  - B17 "every bin" collided with "the group's own size" and was re-staggered.
  - B18's right-column worked weights were re-spaced.
- 4K `art run` #1: 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**. B02 at 90% reads "Is the model calibrated group by group?", so the correction is on screen.
- `art final` #1: **GATE T FAIL §8.6b** on B12/B13/B14/B15/B19. The INK columns, joined by the INK axis and reference lines, formed one "text-run" blob whose bbox enclosed the value labels (a false 100% overlap). Fix at the source: columns are DIM (outside GATE T's INK/MUTE text mask); reference lines stay INK. All ten Manim beats were re-rendered after clearing `manim/B1?.mp4` and `partial_movie_files`. A 1080p pre-check of `check_bbox_overlap` on 18 frames (50/85/95% of the six affected beats) was all PASS.
- 4K `art run` #2: 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**.
- `art final` #2: **GATE T PASS** (0 FAIL). The §8.10 advisories on B00/B01/BVDT (narration recites the card) are expected for TL;DR cards. The SKIN LINT note ("cold open is ClaudeTldrWhat") is expected for tldr, and bookend_check accepts it. `bookend_check.py` PASS after the final.
- Frame check on the master:
  - B00 at ~50% (12.7 s): the question and line 1 only.
  - B00 at ~90%: all three lines, numeral 3 in terracotta.
  - B01 at ~50%: dash 1 only. At ~90%: all three dashes.
  - B02 at ~90% (55.4 s): "Is the model calibrated group by group?", so the correction is on screen.

## Manuscript notes for Bear (not fixed in the chapter; not ours to resolve)
- **Pediatric flag contradicts the table's own rule.** The table header says "Y if subgroup ECE > 2× global" (2 × 0.018 = 0.036), but it marks pediatric (0.029) **Y**. By the rule, only three of five rows are flagged. The sections card inherited "four of five", and the film says three.
- **Global base rate does not reconcile.** The printed 0.041 against the N-weighted rows gives 571.4 / 12,955 = 0.044. The film shows no base rate.
- **The global ECE (0.018) sits below the patient-weighted mean of the subgroup ECEs (0.028).** This is consistent only through within-bin cancellation (same bins). A one-line note in the chapter would pre-empt the obvious student question; the film says it in the tangent.
- The table cites no dataset and sits beside the Epic/Wong paragraph. A reader could take it for Epic's data, so the chapter might label it illustrative.
- The two in-body `[verify]` flags (ECE thresholds; overconfidence dominant in LLMs) are untouched and kept out of the film.
- Seven merge-conflict blocks remain (figure numbering 11.x vs 12.x). This film uses none of them.

## MASTER — 2026-09-23 15:07
`exports/landscape/tldr-average-hides-the-patient.mp4` — 3840×2160 · 24 fps · H.264 + AAC 48 kHz · 347.9 s (5:48) · sha256 735d98ef498fc398… Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
