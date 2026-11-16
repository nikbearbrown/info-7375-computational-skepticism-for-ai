# BUILD-LOG — Probability and the Confidence Illusion (Lecture 2 of 13)

**What.** Running log of the build of one whole-chapter lecture film (lecture skill, Liam, claude-liam, greeting Hola).
**Why.** Resumable: usage limits cut earlier builders off mid-render.
**Found.** See the dated entries; the closing entry is written before `art final`.

## 2026-10-10
- Read the brief, lecture SKILL and all borrowed skills, the whole chapter, the deck skeleton, and the Model × Effort lecture as the shape to copy. First session ended after reading; second session resumed.
- **Gate F first.** Fetched Wong (JAMA IM), Guo (arXiv abstract), Rabanser (arXiv), DeGrave (abstract via PSNet/medRxiv), and secondary accounts of Casscells and the interval-overconfidence literature. Seven corrections/qualifications in FACTCHECK.md (Casscells plurality; DeGrave mechanism; the 0.4–0.6 intervals; the triage reason; 1/101 versus 1/102; 18% of hospitalizations; Rabanser).
- **Evidence.** `evidence/evidence.py` (seeded) and `evidence/bayes_run.py` run; stdout kept. Simulated calibration: seed 7, 20,000 cases, accuracy 0.746, fitted T 2.19.
- **Structure.** 10 acts, 66 body beats, 6 bookends; BOPEN narrated; no composer cold open. Estimated runtime from the sheet is information only.
- **Library asked** (`./art scenes`) for the mechanisms; nothing registered carries these numbers, so beats are drawn in Manim.
- **Toolkit edits:** none. No new registered scene.
- **Pronunciation:** liam.json untouched (brief forbids edits under brutalist.art); any needed respelling goes in the narration and is mapped back in `build_srt.py`.

## Build rounds (2026-10-10)
1. Stills first: low-res last frames of all 75 Manim scenes on contact sheets, looked at; 30 layout fixes (overlapping labels, off-card bars, the coin run now exactly 7 heads in 20, stray marks). Remotion beats looked at at 25/50/95% (`_qc/`).
2. `art run` rounds: Gate A clean; Gate B stopped three scenes (B38 label crossed by crosses, B48 and B61 labels past the safe area), fixed; Gate V flagged 3 MAJOR low-contrast frames (B15, B26 pale fills), fixed with darker fills (clips moved to `_superseded/round1/`); Gate V then 164 frames, 0 BLOCKER, 0 MAJOR.
3. `art final` first BLOCKED on GATE T (4 FAILs: B08, B21, B37, B45, ink box outlines read as text runs); box strokes changed to grey; GATE T PASS, 0 FAILs.
4. Pronunciation: no edit to liam.json (brief forbids edits under brutalist.art). "Cauchy" respelled "Koshee" and "ICML" "I C M L" in the narration, mapped back in `build_srt.py`. Whisper heard "Hola" as "Ola" (correct sound).
5. Narration trims after Gate F: B26, B39, B46, B66 shortened; B26 stays 16 s because of the four names.
- Lane histogram: Manim 65 body + 10 act titles, CCPlainShell 1, bookends 6 (BOPEN card, BIDEA, BDEFS, BVDT, BHTF, BOUT). Estimated 15.3 min; measured 15:20 (919.7 s of narration).
- Known small items: manim clips B23 (+0.19 s), B27, A8, A10 run slightly past their audio, so the compiler trims them from both ends; nothing on screen is lost beyond silent frames.

## Closing entry
Master: `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-probability-and-the-confidence-illusion/exports/landscape/claude-liam-lecture-probability-and-the-confidence-illusion.mp4`, 3840x2160, 24 fps, 921.33 s (narration sum 919.66 s; 1.61 s silent tail). sha256 c4fc5a63acd058226696c5377d1c24c2138e93abd59a926e98bd91a5adfc6c21. Gates: F, A, B, W, V (0 BLOCKER, 0 MAJOR), T (Overall PASS, 0 FAILs), PROOF GATE, bookend PASS. Not staged, not published, not committed.
