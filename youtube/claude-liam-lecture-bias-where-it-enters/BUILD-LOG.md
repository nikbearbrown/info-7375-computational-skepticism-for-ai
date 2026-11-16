# BUILD-LOG — Bias: Where It Enters and Who Is Responsible (Lecture 6)

**What.** Film 3 of the first three INFO 7375 lecture films, built with the `lecture` skill, Liam in for Bear, Kokoro am_onyx, @NikBearBrown outro.
**Why.** Bear's dictated instruction of 2026-10-10 (see `../LECTURES-FIRST-THREE-BRIEF.md`).
**Found.** (updated as the build proceeds; the closing entry is written before `art final`.)

## 2026-10-10
- First session was stopped before any file was written; restarted from the brief. Read the lecture skill and its borrowed lanes, nopunt, show-tell, tldr, deep-explainer, your-turn, MATH-TYPESETTING, EXECUTABLE-EVIDENCE, liam.json, the two CLAUDE.md files and the model-times-effort precedent.
- Decision: the third film is Lecture 6 / Chapter 6 (the `03-bias…` deck folder pre-dates the 2026-07-02 renumbering); the deck folder is empty.
- Facts first (Gate F): primaries fetched; Gallup's 50,000 stripped; Case #6 verified from the paper's page 20.
- DFS press release: capture attempt returned a Cloudflare 403. Not bypassed (bot-detection). The regulator's sentences (fetched as text) are quoted on a drawn card.
- Evidence first: `evidence/evidence.py` run; the first version of the graph had the model on 6 of 8 paths (it contradicted the parable's point if read as leverage); rebuilt a 10-path graph with a deployment-context branch and narrated honestly: counting paths is not measuring bias.
- Narration lengths: many beats run 40–55 words (over the 20–40 guide); long ones are split only if audio exceeds ~20 s.
- Whisper check (faster-whisper small.en): BOPEN heard in order (playlist, film title, summary); numbers, "Namaste", the course credit, Kleinberg/Mullainathan/Raghavan/Chouldechova heard right (whisper spells the names its own way; the voice says them correctly). B10 was re-voiced after its narration was corrected ("seventeen and a half percent"). `pad_audio.py` makes lead/tail silences real (BIDEA +0.8 s, BVDT +0.5 s, BOUT +1.0 s).
- Opening card: portrait `professor-bear-1x1-200` (slug-seeded), lines "Bias: Where It Enters" / "and Who Is Responsible", description "Find where bias lives, then who owns the fix", "Video 06 / 13", entry pointer "Video 1 · The Skeptic's Toolkit". Looked at: renders cleanly.
- Gate A (static) all 74 scenes clean (needed the evidence JSON embedded in scenes.py: Gate A copies only that file); Gate B (layout, --curve-strict) clean after fixes (label on a curve, safe-area warnings, node widths).

## Build rounds
1. Review cut 1: 99/99 slots; GATE V FAILED (B42 edge-bleed; 17 MAJOR: low contrast / one empty mid-frame). Cause: the kraft and ghost fills were more than 28/channel from the stage, so Gate V counted them as pale "ink". Fix: KRAFT and BAR3 pulled within 28 of the stage; B29's chips shown from the start; B42's question row moved in. Also three clips ran past their audio (B01, B09, B42): `go()` and `finish()` now clamp to the beat's audio. Old clips in `_superseded/round1/`, `round2/`.
2. Review cut 3: GATE V PASS (198 frames, 0 BLOCKER, 0 MAJOR).
3. Looked at the compiled cut (late frames of all 74 Manim beats, mid frames of every Remotion beat): fixed B10/B51 (shell lines were cut by an ellipsis or the wrong lines; the evidence stdout was reshaped into lines under 60 characters and chosen by block), B48/B75 (capture camera; page 20 of the paper shows Case #5 above Case #6, so the ring now sits on the Case #6 summary), B07 (squeezed nodes), B18, B71 (a node text vanished under a fill), the causal graph layout (labels overlapping), tag overlap in B69/B70. `_superseded/round3/`, `round4/`.
4. Review cut (art-run5.log) then `art final`.

## Lane histogram and runtime (information)
Manim 74 body beats · BrowserCapture 3 · CCPlainShell 2 · LectureEvidenceTable 3 · FormACard 11 · bookends 6 = 99 beats. Estimated runtime 27.5 min at 2.6 words/s; measured narration 23.1 min (Kokoro am_onyx speaks about 3.0 words/s).

## Traps hit
- Gate A copies only scenes.py: data files must be embedded (`embed_evidence.py`).
- Manim text is wider than a 0.19-per-character guess: `node()` auto-sizes to the text width.
- Gate V counts any surface more than 28 per channel from the stage as ink, so pale fills lower the contrast average.
- The site dfs.ny.gov refuses automated browsers (Cloudflare 403): not bypassed.
- Whole-file `make_sheet.py` re-runs wipe build stamps; run it before `art run`, not after the final.

## Open items (honest)
- Bear has not watched or heard the cut. Not staged, not published.
- Several beats run 17–23 s (B54 22.9 s, B74 20.0 s, BVDT 22.5 s): over the 7–14 s guide; each carries one idea chain but a split would be cleaner.
- Cues are placed by character share of the narration, so a late cue can land a beat after its word (checked at 90% frames).
- The Your Turn composer chip shows the default `Fable 5 · High`.
- ACTS.md coverage table has one confusingly worded row (propensity score matching, LEFT OUT).

## Round 5–6 and the master (2026-10-10)
- GATE T first run: 37 FAILs. 35 were §8.6b (a dark node outline read as a second text run round its label): box strokes are now grey (`GREYLINE`), every Manim scene re-rendered. B43 (ring touched the dark table edge) now rings only the false-positive row; B75's capture was over-zoomed and is now at scale 1.3 on the Case #6 summary; B81's claim node narrowed. B82's venn circles darkened for Gate V contrast. Earlier clips are in `_superseded/round5/`.
- GATE T: **PASS** (TYPECHECK.md, Overall PASS, 0 FAILs; §8.10 advisory: BVDT narration recites its card, which is the recap's job). Gate V: PASS (198 frames, 0 BLOCKER, 0 MAJOR). Gate A, B, W, F, PROOF GATE, bookend: PASS.
- Master: `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-bias-where-it-enters/exports/landscape/claude-liam-lecture-bias-where-it-enters.mp4` — 3840×2160, 24 fps, 1386.17 s (23:06); measured narration sum 1384.46 s (the 1.75 s difference is per-beat frame rounding across 99 beats); 1.62 s silent tail present; sidecar `.verified.json` status ready.
- sha256: 783c55ce3f53a8e584b5e45731f876be3cb7fa2a419433a2c5e5904c187fbcfe
- Late frames of all 74 Manim beats and mid frames of every Remotion beat were looked at (`_qc/master-late-1..4.png`, `_qc/remotion-contact.png`, `_qc/master-final-frames.png`). Not staged, not published, not committed, not pushed.
