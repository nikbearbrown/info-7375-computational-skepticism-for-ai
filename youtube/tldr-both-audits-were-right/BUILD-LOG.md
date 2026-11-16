# BUILD-LOG — tldr-both-audits-were-right

## Executive summary
This is a `tldr` film of INFO 7375 Computational Skepticism, chapter 6, section S3, "Both Audits Were Right". It covers COMPAS, where ProPublica and Northpointe reached opposite verdicts and both did correct arithmetic.

The film has two TL;DR cards, the hesitant writer ("Which audit got it wrong?" → "How can both be right?"), four prerequisite terms, ten pure-Manim LEARN beats and the your-turn close. The LEARN beats run in this order:
- forty dots, which are a constructed population at the chapter's base rates of 30% and 50%, sorted by a calibrated two-box score;
- ProPublica's count redone on the same dots;
- the same dots read through two filters (divide by the box, divide by the outcome);
- a predict beat;
- four dots moved: the false-positive gap nearly closes while the high box climbs from 60% to 82%;
- the chapter's identity v/(1−v) = p/(1−p)·t/f, then its tangent;
- the two headlines back, both checked.

Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Filipino "Kumusta"). The master is 5:23 and passes every gate. Verdict pending; not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick 2026-09-23 (the 13 first picks).
- **Representation:** forty people as dots. Ink means reoffended and dim means did not. Each group is sorted into HIGH and LOW boxes by a calibrated score. The film reads those boxes two ways: Northpointe divides by the box and ProPublica divides by the outcome. The `_Stage` state factory carries the dots across B11–B16, and B19 rebuilds the HOOK's dots and headlines.
- **Constructed numbers:** the chapter gives only the base rates and the calibration claim. The film builds 20 people per group:
  - group 1: high box 3 of 5, low box 3 of 15;
  - group 2: high box 9 of 15, low box 1 of 5;
  - so FPR is 2/14 vs 6/10 and the misses are 3/6 vs 1/10.

  The caption "constructed · 20 per group" is on the stage. Every rate is asserted with exact fractions in `make_sheet.py` and `scenes.py`, including the identity on both groups and the B16 sequence (60/64/69/75/82% and 20→11%).
- **Collision (B16):** the move that equalizes the errors is the move that breaks calibration. The narration says "nearly closes" because 2/10 ≠ 2/14.
- **AUDIT side only:** the film stays on the audit side, as the brief asked. Chapter 7's "Hold One Fair, Watch the Other Break" owns the pin-and-choose framing. Here, "which to hold" is only the boundary caption, and "re-arrest, not crime" is one spoken line.
- **Greeting:** Kumusta. It is unused by any tldr-* sheet; the film avoided Vanakkam, Ahoj, Merhaba, Ciao, Hola and Hej.
- **Merge conflicts:** everything the film uses sits outside the conflict blocks, apart from Figure 6.5's caption. The HEAD side was used there, and no figure was rebuilt from it.
- **Pacing:** the exemplar's `_TARGET` block plus a new `_until(phrase)` helper. Each reveal waits for the phrase's character share × the measured duration, so motion lands on the spoken word.
- **`lock_cards.py`** was copied from tldr-robust-against-what with new anchors. It must be re-run after any `make_sheet.py`.

## Gate history
- `bookend_check.py`: PASS at sheet time and after the final.
- Audio: 17 mp3s. BOUT was apad-padded by 1.0 s, so `actual_duration_s` = 4.05. `lock_cards.py` set:
  - B00 cues 1.5 / 10.29 / 15.18 / 17.74;
  - B01 cues 0.8 / 4.74 / 7.88 / 12.57;
  - B00/B01/B03 `durationSeconds` from the measured audio.
- Gate F content (`factcheck_check.py`): clean (26 rows). B15 was added to row 10 after an FC-4 advisory.
- Pre-audit: Gate A ×10 clean, Gate W ×10 clean, layout audit (`--curve-strict`) ×10 CLEAN.
- Low-res contact sheet (25/60/92%), fixes made:
  - B18 "no audit chose it" collided with the next zone, so the zones were re-spaced;
  - B17 now uses full-size \frac{3}{7} and the label "ProPublica's number" (no bare "f" as Text);
  - terracotta dots were moved off their captions in B10, B13, B14, B17 and B19.
- `art run` #1: Gate B clean and 17/17 slots, but Gate V had **5 MAJOR `underfill`** findings (B10 at 50/85%, B11 at 50/85%, B17 at 50%). B14 also overran its audio by 2 s (the compiler center-cut it). Fixes:
  - B10/B19: the hook dot rows are wider and lower (±5.2, y −1.85/−2.3), and the question moved up.
  - B11: the waiting group stays grey (DIM, as in the hook) instead of ghost, and the constructed caption lands at the start.
  - B17: the group labels, the separator and the caption land together with the equation.
  - B14: the last two plays were merged.
  - B19: "both right" moved up and the connectors fade out.
- `art run` #2: Gate V 0 BLOCKER / 0 MAJOR. The contact sheet showed B18's fraction symbols stacking tight, so the zones were re-spaced again (2.05 / 1.0 / −0.2 / −1.1 / −1.9).
- `art run` #3: Gate V 0 / 0, 17/17 slots.
- `art final`: **GATE T PASS** (FAILs: 0). SKIN LINT notes that ClaudeTldrWhat is not the composer; that is expected for tldr, and bookend_check accepts it.
- Frame check on the master:
  - B00 at 50%: only line 1 is on screen.
  - B00 at 90%: all three lines are on screen, with numeral 3 in terracotta.
  - B01 at 90%: all three dashes.
  - B02 at 90%: "How can both be right?" is on screen.
  - B16 at 95%: 82% with the X, and FP 2 of 10.
  - B18 at 95%: all five zones and both escapes.

## Manuscript notes (for Bear — not fixed in the chapter)
- The chapter says "For a calibrated score, positive predictive value v relates to … by v/(1−v) = p/(1−p)·t/f". That identity holds for ANY binary classifier (it is Bayes' rule in odds form). Calibration enters only when v is held equal across groups. The film makes that step explicit.
- The plain-language paragraph says equal FPR "would need to draw the threshold in a different place for each group". That is one face of the constraint. The film shows the other face (one rule, people moved, calibration breaks) and does not claim that different thresholds are the only remedy.
- The chapter prints no COMPAS rates, only the direction of the error pattern. The film attributes no rate to the real tool.
- Figure 6.5's caption sits in a merge-conflict block (HEAD "6.5" vs d78899b "3.4" and "3.2"). The chapter's 8 conflict blocks are untouched.

## Master — 2026-09-23 13:50
`exports/landscape/tldr-both-audits-were-right.mp4` — 3840×2160 · 24 fps · H.264 + AAC · 323.5 s (5:23) · sha256 c3b0321bc5d5d2ef… Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
