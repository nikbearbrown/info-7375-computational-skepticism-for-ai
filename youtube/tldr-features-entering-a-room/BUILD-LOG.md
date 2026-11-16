# BUILD-LOG — tldr-features-entering-a-room

## Executive summary
This is a `tldr` film of chapter 5 of INFO 7375 Computational Skepticism for AI, section S1, "Features Entering a Room". It opens with two TL;DR cards. Then the hesitant writer turns "How much did income add?" into "What is income's fair share?", and four terms land. After that come ten pure-Manim LEARN beats built on the chapter's constructed worked example:
- one applicant sits 0.17 above the average, with three features;
- income walks into an empty room (+0.08);
- "drop it and see" gives a different answer (+0.06);
- the middle seats give +0.07 and +0.09;
- all six arrival orders go into one ledger, and the viewer is asked to commit;
- the six bumps merge into 0.073, and the three bars (0.073 + 0.062 + 0.035) fill the gap exactly to 0.72;
- only then do the names arrive: the Shapley value and efficiency, each read in its own tangent;
- back to her score, with the boundary: zip code's 0.035 is about the model, not the world.

The film closes on your-turn. Narration is Liam in for Bear (Kokoro `am_onyx`), greeting Filipino "Kumusta". The master runs 5:19 and every gate passes. Not staged, not published.

## Decision log
- **GATE S:** Bear signed the pick on 2026-09-23 (the 13 first picks).
- **Greeting:** Kumusta (Filipino). Sibling greetings were grepped first (Merhaba, Vanakkam, Ahoj are in use in this book, and Ciao, Hola, Hej, Merhaba are excluded). The Wagwan rule does not apply: the slug char-sum mod 10 is 3.
- **Constructed example:** the chapter writes "Suppose…" and "Say…". A dim "constructed example" caption stays on the LEARN stage from B10 through B19.
- **Honest levels:** only the v(S) levels that the chapter's inputs fix appear on the prediction line: 0.55, 0.63 = 0.55 + 0.08, 0.66 = 0.72 − 0.06, and 0.72. The middle-seat bumps (+0.07, +0.09) are shown as bumps only. φ_debt and φ_zip are the chapter's stated values ("the same six-order average"); no tables were invented for them.
- **Representation:** the room ledger, one row per arrival order, above a prediction line whose ghost span the bars must fill. The state factory is `_Stage(scene, "Bxx")`, which rebuilds the stage as it stands at the end of each beat.
- **Two equations, two tangents:** B16 lands the Shapley formula, which the table folds into first as 2/6·0.08 + 1/6·0.07 + 1/6·0.09 + 2/6·0.06 = 0.073. B16 also lands the efficiency sum, morphed from the bar labels. B17 is the tangent for the formula (worked value: W4's 1!·1!/3! = 1/6). B18 is the tangent for the sum (plugged in over the bars).
- **Hesitant writer:** a phrase trigger ("How much did income add" → "What is income's fair share").
- **Course credit** is spoken in B00 and shown on the cards' course line.

## Gate history
- Bookend check: PASS at sheet time and again before the final.
- Audio: 17 mp3s with 317 s of measured narration. BOUT was apad-padded by 1.0 s, and `actual_duration_s` = 4.2 from ffprobe. `lock_cards.py` (from the sibling `tldr-robust-against-what`) set the B00/B01/B03 `durationSeconds` and placed the B00/B01 cues on the spoken clauses.
- Gate A ×10: one error on the first pass. B10 called `add_foreground_mobjects`, which the stub lacks, so the call was removed (the span and the dot never overlap). Clean after that. Gate W ×10 clean.
- Layout audit (`--curve-strict`): the first pass flagged 14–18% text-on-text overlaps in the ledger rows. The seats were widened (−5.9 / −4.45 / −3.0) and the rows re-spaced to 0.46. Clean ×10.
- Low-res contact sheets:
  - Round 1: seat words were fused ("incomedebt"). The bar labels crowded the ledger's last row, so the prediction line and bars moved down 0.35. The zip label collided with debt's, so it now sits past the bar end. The B16 dot touched "0.073". The B17 right-column sentence touched the separator, so it was shortened.
  - Round 2: the words in a row sat at different heights, because descenders in "zip" and "nobody" lifted the centred words. Row words are now top-aligned.
- 4K `art run` #1: layout audit CLEAN ×10, 17/17 slots, Gate V 0 BLOCKER / 0 MAJOR.
- `art final` #1: **GATE T PASS** on the first try. One advisory: §8.10 B01 narration recites the card (0.95), left as is.
- Frame check of master #1: B00 at 50% shows only line 1, and at 90% all three lines. B01 at 50% shows dash 1, and at 90% all three dashes. B02 at 90% showed the correction, but it only completed about 1.2 s before the cut. Fix: dropped the "Score 0.72. Average 0.55." line, set fontSize 78, hesitateBetween 6 → 5, mistakeRate 2 → 0, and re-rendered B02 only. The corrected question is now on screen from about 4 s of the 9.1 s beat.
- `art run` #2 (B02 only) → Gate V 0/0. `art final` #2 → **GATE T PASS**, bookends PASS. The master frame at 46.7 s (B02 at about 85%) reads "What is income's fair share?".

## Manuscript notes for Bear (not fixed in the chapter; not ours to resolve)
- Every figure caption and some back matter still carry unresolved merge-conflict blocks (HEAD 5.x vs d78899b 6.x). The HEAD side was used, and all of this card's material is on the HEAD or unconflicted side.
- The worked example gives the six-ordering table for income only. φ_debt = 0.062 and φ_zip = 0.035 are "Suppose" values. They are consistent: a value function exists that produces all three, since φ_income is fixed at 0.0733 and the other two only need v({debt}) − v({zip}) ≈ 0.037. But the chapter never shows it. A reader doing W5 can't reproduce φ_debt independently.
- φ_income = 0.44/6 = 0.07333, printed as 0.073, and the Efficiency check 0.073 + 0.062 + 0.035 = 0.170 holds only on the rounded values. That is fine, but the chapter says "sum exactly".
- The three-family table's "Income contributed +0.18" and W3's "+0.3" are different illustrative numbers from the worked example's 0.073. A careful student may ask which applicant these are.

## Master — 2026-09-23 13:55
`exports/landscape/tldr-features-entering-a-room.mp4` — 3840×2160 · 24 fps · h264 + AAC · 318.5 s (5:19) · sha256 9b775ebf57dddfca… Verdict pending. Not staged, not published. To stage on Bear's word: `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.
