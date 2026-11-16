# BUILD-LOG — tldr-gru-validated-not-attempted

**What happened.** Built 2026-09-24 from the Gru persona Bear pasted ("TLDR video explaining Liam persona Gru"). 17 beats, 288.8 s, 3840×2160 at 24 fps. Master cut at 13:48 on the second render pass; every gate PASS. Not staged, not published — awaiting Bear.

**Master.** `exports/landscape/tldr-gru-validated-not-attempted.mp4` · sha256 `1a6debc2a7a8b1cb6439ce36c2956d0b47eb4a0a92dd572de4112cd06081f023`.

## Gates
| Gate | Result |
|---|---|
| S (sections) | `../tldr-sections-gru-persona.md`: S1 picked by Bear's request; S2 deferred (already published as the Gru/Minion Split, 2026-09-15) |
| F (facts, shotlist, prompts) | PASS — FACTCHECK.md, 22 rows; SHOTLIST.md; PROMPTS.md |
| BOOKEND | PASS |
| A (static stub) / B (layout, pixel-true) | PASS, all ten scenes, both passes |
| V (frame QC) | pass 1: 3 MAJOR underfill (B11, B12, B16) → persistent Gate-4 caption, B15 question held into B16 → pass 2: 0/0 |
| T (type) | PASS, 17 beats |

## What changed between passes
Contact-sheet review after pass 1: "3 principles" and "4 components" touched, and the need's label crowded the phase row. The phase row was widened (2.2 → 2.4 units per phase) and the lower half dropped 0.15; all scenes re-rendered from a cleared cache.

## Open for Bear
- The pasted Gru and the repo's `recipes/gru.md` are different versions (phase order differs); the paste also contradicts itself on which phase holds the needs. See SOURCES.md. The film follows the paste's gate list.
- Facts not yet signed off.

## Published — 2026-09-24
Bear: "looks good" + the publish procedure; facts signed off. Existing 4K master reused (sha 1a6debc2…, every beat clip 3840×2160). `stage_publish.py` → `build_srt.py` (75 full-text cues) → `art post --no-topaz`: staged.json 3840x2160, all_beats_4k true, markers_clean true, gate_t pass, status staged, topaz.ran false. TOPOST description rewritten (the generated one cut the blurb and the Your Turn prompt mid-sentence; 14 chapters from the staged caption clock, beats under 10 s merged). Dry run: OAuth valid as Nik Bear Brown, playlist "Claude & Agentic AI" found (PLHUltjHuvAK4). Upload: TOPOST GATE + sha assert PASS → https://youtu.be/UCLJD1A3Jmo, unlisted, playlist position 0; captions attached on the second attempt. The master moved to `books/youtube/TOPOST/`.
