# BUILD-LOG — tldr-robust-against-what

## Executive summary
A `tldr` film of chapter 4 of INFO 7375 Computational Skepticism for AI, section S4 "Robust Against What?". Two TL;DR cards, the hesitant writer ("Is the model robust?" → "Robust against what?"), four terms, then ten pure-Manim LEARN beats: the chapter's template disclosure table fills one row at a time (clean 94 fixed; robust 71 white-box ε = 0.03, 58 transfer, 87 natural shift). The rows fold into the single word "robust" and the numbers disappear. They unfold again as separate axes. A predict beat, then row three lands above both, and the word turns into two blank form fields. The budget moves and the number expires. Only then does the film name it: a profile, not a number. The film closes on your-turn. Narration: Liam in for Bear (Kokoro `am_onyx`), greeting Turkish "Merhaba". Master 5:02, all gates PASS. Not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick 2026-09-23 (the 13 first picks).
- **Resumed build:** a previous attempt stopped at a usage limit after `make_sheet.py` and `build_srt.py`. `make_sheet.py` was re-read against the chapter and fixed:
  - B12 no longer says "the stranger did more damage than the insider". The chapter's transfer row gives a surrogate model, not an ε, so 58 and 71 are not at a comparable budget.
  - B16's "told you nothing" was an overstatement. It became "does not guarantee … or the reverse", which is Figure 4.5 plus the chapter's "somewhat, but not as much as you'd like".
  - B15 now asks whether the attack rows could have told you.
  - B00 and B02 were trimmed to their word budgets (68 and 35 words).
  - "Template" is spoken in B00, B12 and B16.
- **Template values:** the dim caption "template values — illustrative" stays on the stage from B11 through B19. "ResNet-50" and "Q4 2023 vs Q1 2024" are left off screen (model names and datable content).
- **Representation:** the table as the one persistent object (`_Table` state factory). Clean bars are dim (the foil) and robust bars are ink. Each scene has one terracotta dot or X.
- **Collision (B16):** row three grows past the 58 and 71 guide ticks. A copy of the claim's own "robust" glyphs then morphs into the two blank fields ("2 · residual risk", "3 · monitoring trigger").
- **B17:** ε = 0.06 is shown with "?" as its value. No number is invented.
- **Course credit** is spoken in B00 and shown on the cards' course line.

## Gate history
- Bookend check PASS (at sheet time and before each compile).
- Audio: 17 mp3s. `lock_cards.py` puts B00/B01 cues on the spoken clauses and sets B00/B01/B03 `durationSeconds` from measured audio. BOUT is apad-padded 1.0 s, and `actual_duration_s` = 4.05 from ffprobe.
- Gate A ×10 clean. Gate W ×10 clean.
- Low-res contact sheet, round 1: in B13 the merged word sat on a clean bar, so the fold moved into the empty row-three band. Dots touched the % labels (offset 0.85 → 1.0). The B15 question sat too close to the tick labels (→ y −2.2). The B19 X touched the closing quote (→ x −0.55). B13's "which number?" touched the X (→ x 3.9).
- 4K `art run` #1: layout audit CLEAN, Gate V 0/0, 17/17 slots.
- `art final` #1: GATE T FAIL on B03, §8.1: the "ε" glyph in the term "perturbation budget ε" and in its meaning measured 38px, under the 41px floor. Fix: the term is now "perturbation budget", and ε stays spoken and appears in the B11 scene.
- `art final` #2: GATE T PASS.
- Frame check: B00 at 50% shows only line 1 and at 90% all three lines. B01 at 90% shows all three dashes. B02 at 90% FAILED review: the writer ran long, so the correction ("Robust against what") began only in the last ~0.5 s of the 9.7 s beat. Fix: dropped the "A vendor's slide says:" line, charMs 26 → 22, hesitateBetween 8 → 6, mistakeRate 5 → 2, fontSize 70. B02 was re-rendered and the corrected question is now on screen from ~6 s.
- `art run` #3 + `art final` #3: bookends PASS, Gate V 0 BLOCKER / 0 MAJOR, **GATE T PASS**, 17/17 slots. Master frame at 50.1 s (B02 at 90%) shows "Robust against what?".

## Manuscript notes for Bear (not fixed in the chapter — not ours to resolve)
- In the disclosure template, the transfer row's "Perturbation budget used" cell names a surrogate ("Surrogate: ResNet-50") instead of a budget. A reader cannot compare its 58% against the white-box 71% at ε = 0.03. In the literature a white-box attack at the same budget is usually at least as strong as a transfer attack, so the template's ordering reads oddly unless the transfer budget is stated.
- There are 13 unresolved merge-conflict blocks. The HEAD side was used; this card's material is all on the HEAD or unconflicted side.

## Master — 2026-09-23 12:43
`exports/landscape/tldr-robust-against-what.mp4` — 3840×2160 · 24 fps · AAC · 301.6 s (5:02) · sha256 c8f97913c0619cb5… Verdict pending. Not staged, not published. To stage on Bear's word: `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
