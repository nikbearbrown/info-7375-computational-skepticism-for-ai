# CHECKS-REPORT — The Test You Did Not Design.
`claude-liam-deep-test-you-did-not-design` | 2026-09-02 | Gate: PROOF GATE (written before the slate previz; render ledger appended after)

## Per-beat classification (nopunt § SHOW / HOLD / CARD)

**31 SHOW / 2 justified-HOLD / 0 PUNT** across the 33 body beats.

| Class | Beats |
|---|---|
| SHOW (Manim) | A1M A1M2 A2M A2M2 A2M3 A3M A4M A5M A6M A6M2 |
| SHOW (Remotion illustration pattern) | A1R A2R A2R2 A3R A3R2 A4R A4R2 A5R A5R2 A6R |
| SHOW (VOX archival plate in pantry, sidecar written) | A1V A2V1 A2V2 A4V A5V |
| HOLD (real archival photograph / document — human) | A3V1 `hold_reason: real named person — archival photograph, rights check is the human's` · A3V2 `hold_reason: specific real document — the item's rights statement governs` |
| CARD (act dividers, ≤5 s, motion_claim present) | A1C A2C A3C A4C A5C A6C |

Bookends / asks (exempt, all SHOW): B00 B01 A1K A6K BVDT BHTF BOUT.

## Teaching arc (nopunt § Whole-sheet checklist)

| Item | Status | Where |
|---|---|---|
| FRAMEWORK beat before examples | ✓ | A2R (the three limits, on screen) precedes every worked instance; A1R sets the two-questions frame before the battery |
| WORKED EXAMPLE using the framework on screen | ✓ | A1M battery + A2M3 six-at-the-boundary walk the composite case through the frame; A4R2 walks the engineering response as a real limits section |
| FALSIFIABILITY / edge case | ✓ | A2R2 (the embeddings objection, taken seriously) and A3R/A3R2 (what Turing and Searle do NOT settle) |
| SCAFFOLDED viewer task | ✓ | BHTF: the prompt is read verbatim, then two checks the viewer applies to Claude's answer (lock-before-analysis; limits section must not read as a disclaimer) |
| Four bookends | ✓ | B00 ClaudeComposerAsk · BVDT ClaudeVerdictArtifact · BHTF "Your turn." · BOUT ClaudeTitleOutro (`bookend_check.py` PASS) |
| No source, no verdict | ✓ | every factual/structural claim has an on-screen artifact or citation chip; FACTCHECK.md 22 rows, all resolved |

## Machine gates run at authoring (pre-render)

| Gate | Result |
|---|---|
| beat_lint (GATE L / S) | 0 defects · 6 staging advisories (5 s act cards; each carries a motion_claim) |
| banned_card_check | PASS |
| bookend_check | PASS |
| content_check | PASS (40 beats, no placeholders / foreign defaults) |
| type sweep §8.7–8.9 | 0 issues after two copy fixes (B00 output line; A6R chip) |
| static_scene_check (10 Manim scenes) | 10/10 run clean; 1 advisory (A2M3) |
| placeholder_check | 2 unfilled STILLs, both HOLD (A3V1, A3V2) |
| lane_check | pre-render FAIL expected (pipeline beats not yet rendered) — re-run after `art run` |

## Render ledger
_(appended after the previz compile — see below)_

## Render ledger — slate previz (12 compile passes, 2026-09-03)

`claude-liam-deep-test-you-did-not-design-slate.mp4` — 591.9 s (9:52), 1080p review cut with beat burn-ins. 38/40 slots filled; the two slates are exactly the SHOPPING.md entries (A3V1, A3V2).

Gate roster on the final pass: F ✓ · L ✓ · BANNED-CARD ✓ · SWEEP ✓ · A ✓ · W ✓ · B ✓ · G ✓ · **V ✓ (0 defects, 80 frames)** · **T ✓ (0 FAILs, 40 beats)** · SHARPNESS ✓ · BOOKEND ✓ · MASTER — not run (no clean master by design: two human slates) · LANE — reports A3V1/A3V2 as human-owned slates (expected until the pantry fills).

| Beat | Lane | Slot | Locked window |
|---|---|---|---|
| B00 | BOOKEND | VIDEO | 21.2s |
| B01 | BOOKEND | VIDEO | 12.2s |
| A1C | CARD | VIDEO | 4.1s |
| A1R | REMOTION | VIDEO | 14.3s |
| A1K | ASK | VIDEO | 2.8s |
| A1M | MANIM | MANIM | 15.2s |
| A1V | VOX | STILL | 15.3s |
| A1M2 | MANIM | MANIM | 14.6s |
| A2C | CARD | VIDEO | 5.9s |
| A2R | REMOTION | VIDEO | 14.2s |
| A2M | MANIM | MANIM | 17.8s |
| A2R2 | REMOTION | VIDEO | 16.0s |
| A2V1 | VOX | STILL | 11.3s |
| A2V2 | VOX | STILL | 16.6s |
| A2M2 | MANIM | MANIM | 18.4s |
| A2M3 | MANIM | MANIM | 13.7s |
| A3C | CARD | VIDEO | 4.2s |
| A3V1 | VOX | SLATE | 15.4s |
| A3R | REMOTION | VIDEO | 14.8s |
| A3V2 | VOX | SLATE | 16.6s |
| A3R2 | REMOTION | VIDEO | 17.5s |
| A3M | MANIM | MANIM | 16.6s |
| A4C | CARD | VIDEO | 5.5s |
| A4M | MANIM | MANIM | 23.4s |
| A4V | VOX | STILL | 13.9s |
| A4R | REMOTION | VIDEO | 16.9s |
| A4R2 | REMOTION | VIDEO | 16.0s |
| A5C | CARD | VIDEO | 5.7s |
| A5R | REMOTION | VIDEO | 16.5s |
| A5V | VOX | STILL | 16.4s |
| A5M | MANIM | MANIM | 18.8s |
| A5R2 | REMOTION | VIDEO | 16.7s |
| A6C | CARD | VIDEO | 4.8s |
| A6K | ASK | VIDEO | 2.5s |
| A6M | MANIM | MANIM | 15.6s |
| A6R | REMOTION | VIDEO | 17.3s |
| A6M2 | MANIM | MANIM | 18.8s |
| BVDT | CLOSING | VIDEO | 29.3s |
| BHTF | CLOSING | VIDEO | 42.2s |
| BOUT | CLOSING | VIDEO | 12s |
