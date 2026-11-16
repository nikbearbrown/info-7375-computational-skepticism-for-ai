# RESUME — Lecture 1, "The Skeptic's Toolkit" (Hallo, Video 1 of 13)

Spec: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/LECTURES-FIRST-THREE-BRIEF.md (Film 1 column).
Reel: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-the-skeptics-toolkit/
Run everything from /Users/bear/Documents/CoWork/bear-textbooks/books/. Never stage/publish/commit/push. Scratch: /private/tmp/claude-501/-Users-bear-Documents-CoWork/9430e172-7c13-46d9-987f-7a913f7e069f/scratchpad/lecture-1/

## State (update after every step)
- [x] Session 2 start 2026-10-10: reel folder created, all docs/skill/chapter/deck/seed material READ (skill, nopunt, show-tell, tldr, deep-explainer, your-turn, MATH, EVIDENCE, liam.json, chapter 1, deck, FACTCHECK-SEED, show-tell FACTCHECKs).
- [ ] ACTS.md / SOURCES.md / README.md written (stubs exist)
- [x] narration.py written (65 body beats, ~12.9 min est)
- [ ] Gate F primaries re-verified (Ash/arXiv 2602.20021, SEC 34-70694 local copy, Lazer, Wong, Zillow, DeGrave, ProPublica)
- [ ] make_sheet.py + beat_sheet.json
- [x] Kokoro audio voiced, BOUT padded (4.008 s), total 756.5 s; AI respelled eigh-eye in BOPEN/BIDEA
- [x] BOPEN card built (media/BOPEN.mp4, opening/)
- [ ] scenes (kit.py + scenes_actN.py via assemble_scenes.py), stills looked at
- [ ] art run, gates, art final, master verified

## Scaffolding to copy (proven)
/Users/bear/Documents/CoWork/bear-textbooks/books/csye-7270-building-virtual-environments/youtube/claude-liam-lecture-blender-to-godot/ : kit.py assemble_scenes.py preflight.sh gate_probe.py still_remotion.py frames.py build_docs.py make_sheet.py narration.py BUILDER-BRIEF.md
BOPEN helper pattern: /Users/bear/Documents/CoWork/bear-textbooks/books/hpc/youtube/add_bopen.py

## Next command
Adapt make_sheet.py (BOPEN, lanes), voice audio, dispatch act builders.

## Status 2026-10-10 (update)
- Six builder agents launched (groups 1-6, see BUILDER-BRIEF.md) producing scenes_act1..6.py, lanes/act1..6.json, factcheck/act1..6.md. If they are missing when you resume, re-dispatch per group.
- After builders: python3 make_sheet.py; python3 assemble_scenes.py (writes scenes.py); build_docs.py; build_srt.py (TODO write); art run <reel> --height 2160 (background, one at a time); Gate T/V fixes; README + BUILD-LOG closing entry; art final; verify; append sha256.
- 2026-10-10: groups 1,2,3,5,6 reported done (Gate A/layout clean, low-res). Group 4 lanes present; awaiting its report. Narration softened/fixed and re-voiced: B01, B26 (soften), B51, B53 (falsification conditions / canonical shape). All beats voiced; make_sheet shows 0 pending.
- NEXT: python3 assemble_scenes.py ; build_docs.py ; then `./brutalist.art/art run <reel> --height 2160` in background (from books/), one at a time.
- 2026-10-10: ALL six groups done and merged; scenes.py assembled; build_docs.py writes SHOTLIST/FACTCHECK/CHECKS-REPORT (158 rows). B33 re-voiced (17.56 s). Total audio 762.0 s.
- NEXT: Gate A pre-audit already per group; run `./brutalist.art/art run <reel> --height 2160` from books/ in background; read _qc/ frames; fix; then README/BUILD-LOG, art final.
- art run started in background 00:49 -> art-run.log (re-run same command if interrupted; check ps first)
- 2026-10-10 01:21 art run done: Gate V FAILED 22 MAJOR (see _qc/REPORT.md). Fix scenes (scenes_actN.py), move manim/<B>.mp4 + clips to _superseded, rm -rf media/videos partial_movie_files, re-run.
- 2026-10-10 01:30 fixes for Gate V (sparse waivers, B13/B28/B34 edits, BOUT waiver); re-running art run (log art-run2.log)
- 01:45 Gate V PASS on run 2; BVDT paging fixed (lecturePageFrames); re-running art run -> art-run3.log
- 02:10 art run 3 done, Gate V PASS (0 major). README + BUILD-LOG closing written. NEXT: `./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape` from books/ (background; ~long), then verify master, bookend_check, append sha256 to BUILD-LOG.
- 02:30 GATE T failed 9 beats (bbox-overlap ink cards -> DIM, B45 terracotta arrow, B47 safe area, B51 min size); fixed in scenes_act*.py; re-running art run (art-run4.log) then art final
- 02:50 GATE T left B47,B51; fixed; re-running run5+final
- 03:10 B51 still failed min-size (tiny check glyph) + stale pacing phrase fixed; rerun run6+final
- 03:30 B51: arrow in handoff icon was the 35px blob; replaced by line; rerun run7+final (art-final5.log)
- DONE: master built and verified, sha in BUILD-LOG.md. Only the hand-off report remains. Nothing staged/published/committed.
