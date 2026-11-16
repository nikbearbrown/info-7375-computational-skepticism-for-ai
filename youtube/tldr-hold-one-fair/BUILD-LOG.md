# BUILD-LOG — tldr-hold-one-fair

## Executive summary
This is a `tldr` film of INFO 7375 Computational Skepticism for AI, chapter 7, section S1 "Hold One Fair, Watch the Other Break". It covers calibration (equal PPV) and equalized odds (equal TPR and FPR). When base rates differ, you cannot have both. The film shows this with the chapter's own two constructed tables and stays on the CHOICE side; there is no COMPAS.

It has two TL;DR cards, the hesitant writer ("if we just tune it harder" → "when base rates differ"), four terms, ten pure-Manim LEARN beats on the 3Blue1Brown template, and the your-turn close. Liam narrates, in for Bear (Kokoro `am_onyx`, greeting Filipino "Kumusta"). The master is 5:04 and passed every gate. Verdict is pending. It has not been staged or published.

## Decision log
- **GATE S:** S1 was picked on 2026-09-23 (Bear, the 13 first picks). The folder was built fresh.
- **Greeting:** Kumusta (Filipino). Earlier tldr films have used Ciao, Hola, Hej, Merhaba, Sawubona, Jambo, Namaste, Konnichiwa, Salut, Bonjour, Kia ora, Ahoj, Vanakkam and Wagwan. The Wagwan rule does not fire: the slug's char-sum mod 10 is 6.
- **The representation:** each group is a unit square. The positive column is as wide as the base rate (0.6 or 0.3). The flags fill the columns from the bottom: TPR in ink, FPR in grey. The flagged people are gathered into a horizontal "pile" whose dark share is PPV. The pile's dark:grey ratio is the width ratio (the world) times the height ratio (the model). That is the odds identity v/(1−v) = p/(1−p)·t/f, read straight off the squares.
- **Arc:**
  - HOOK: the two asks.
  - INSTANCE: A at 0.60/0.30 → PPV 0.75.
  - INSTANCE: B with A's rates → PPV 0.46. This value is derived from the chapter's inputs, not stated in the chapter.
  - NAIVE: "a better model", 0.70/0.15 in both groups → 0.88 vs 0.67, and the gap survives.
  - SHIFT: widths × heights (7 = 1.5 × 4.67, 2 = 0.43 × 4.67).
  - PREDICT: to hold B at 0.75, do its false alarms go up or down?
  - TRANSFORM: the columns move to the calibration table, the piles align at 0.75 and the heights split (2 vs 7). Release, then re-pin.
  - ABSTRACTION: the identity, plus the two exits.
  - TANGENT: (3/7)·7 = 3 and 1.5·2 = 3 ⇒ 0.75.
  - PAYOFF: the same squares swing between the tables. Equal yes-rates (0.48/0.28, then 0.48/0.32) fails in both. "One must give: you choose."
- **Tier:** the card said "standard". The film landed one equation, which makes it single-insight. The cross-group ratio is folded into words and the 2-vs-7 heights.
- **Constructed:** "the chapter's constructed numbers" is captioned once, in B10.
- **Kept out:** COMPAS (the parallel chapter-6 film owns the audit side), the chapter's threshold labels (see the manuscript notes), and the KMR three-way proof (named as the boundary).
- **Merge conflicts:** the HEAD side is used throughout. Nothing comes from `d78899b`.

## Gate history
- GATE BOOKEND: PASS, at sheet time and again after edits.
- Audio: 17 mp3s, 303.8 s. `lock_cards.py` (reused from tldr-robust-against-what) sets B00/B01/B03 `durationSeconds` from measured audio and places the B00/B01 cues on the spoken clauses. BOUT was apadded 1.0 s; `actual_duration_s` = 4.75 from ffprobe.
- Gate F: 22 rows, clean. Gate A ×10 clean. Gate W ×10 clean. Layout audit (`--curve-strict`) ×10 clean after fixes.
- Low-res contact sheets, two rounds. Fixes:
  - The TPR·FPR readouts of the two squares ran together, so they were stacked on two lines.
  - The "A:"/"B:" labels collided with the odds lines, so the labels moved to x 1.7 and the lines to 40pt.
  - The B17 fraction pieces touched.
  - The B19 bold line went past the safe edge, so it moved to 32pt.
  - The B19 order was changed to match the narration (swing first, then ask 3 and the yes-rates).
  - B11 now fades B10's extras, so the join is continuous.
- 4K `art run` #1: Gate V 0/0, 17/17 slots.
- `art final` #1: GATE T FAIL §8.1 on B14/B16/B17. The lone "=", "×" and "·" MathTex pieces read as sub-floor text runs (36px < 41px). Fix: each operator now rides with its number or fraction in a single MathTex.
- `art final` #2: GATE T FAIL on the same three beats, still at 36px. The remaining small runs were the width DoubleArrows' tips (the arrows were created in B14 and carried by B15–B17). B16 also had §8.6b: the 0.75 tick line through both piles fused them into one blob. Fix:
  - The width arrows were removed, so the squares and their "world" and "model" labels carry the idea.
  - The through-pile tick was replaced by a small ink pointer triangle under the piles.
  - B14–B17 were re-rendered (`manim/B1x.mp4` and `partial_movie_files` cleared).
- `art run` #3: Gate V 0 BLOCKER / 0 MAJOR, 17/17. `art final` #3: **GATE T PASS**. §8.10 advisories on B01/BVDT (narration recites the card) are expected for TL;DR cards.
- Frame check on the master:
  - B00 at ~50% (10.0 s): only the question is on screen; line 1 lands at 10.65 s.
  - B00 at ~90%: all three lines, numeral 3 in terracotta.
  - B01 at ~50%: dash 1 only. At ~90%: all three dashes.
  - B02 at ~90%: "Can one model pass both tests when base rates differ?", so the correction is on screen.

## Manuscript notes for Bear (not fixed in the chapter)
- **The two tables do not reconcile as "same model, different threshold choices."** Both tables list group A at threshold 0.5, yet group A's TPR/FPR is 0.60/0.30 in one and 0.70/0.15 in the other. The same model at the same threshold cannot give both. The film shows the tables as two constructed settings, without thresholds.
- The equalized-odds table rounds B's positive-prediction rate 0.315 up to 0.32 (half-up). That is fine, but it is worth a footnote if the chapter is ever audited.
- "Calibration-satisfying" is used for a binary flag with equal PPV. The chapter says so ("for a binary score, forces equal PPV"), but a reader might expect a full score-level calibration check.
- There are seven unresolved merge-conflict blocks (the Figure 7.1 caption among them). Only HEAD was used.

## Master — 2026-09-23 13:56
`exports/landscape/tldr-hold-one-fair.mp4`: 3840×2160, 24 fps, H.264 + AAC, 304.1 s (5:04), sha256 ef4f09b0cc94e5f5…. Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
