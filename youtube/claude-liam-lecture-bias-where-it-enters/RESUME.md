# RESUME — Lecture 6, "Bias: Where It Enters and Who Is Responsible"

**What.** State of the Film 3 build (INFO 7375 Computational Skepticism for AI, Video 6 of 13, greeting Namaste).
**Why.** Usage limits and stops have cut builders off mid-build; this file says where to pick up.
**Found.** 2026-10-10: reel folder created; spec = ../LECTURES-FIRST-THREE-BRIEF.md; all reading of the skill, nopunt, show-tell, tldr, deep-explainer, your-turn, MATH-TYPESETTING, EXECUTABLE-EVIDENCE, liam.json and the model precedent is DONE. Nothing else is written yet.

## Status
- [x] ACTS.md  [x] SHOTLIST.md (by make_sheet.py)  [x] FACTCHECK.md  [x] SOURCES.md  [x] PROMPTS.md  [ ] README.md  [x] BUILD-LOG.md (in progress)  [ ] CHECKS-REPORT.md  [ ] BUILD-PROMPT.md  [ ] build_srt.py
- [x] make_sheet.py  [~] scenes.py (B01-B47 written; B48-B82 TODO)  [x] audio first pass (99 beats, 23.0 min; B10 narration edited after voicing -> re-voice with --only B10)  [ ] pad_audio (BIDEA lead .8, BVDT lead .5, BOUT tail 1.0; copy pad_audio.py from the model-times-effort precedent)  [ ] whisper check  [ ] BOPEN card  [ ] stills  [ ] art run  [ ] art final  [ ] bookend_check

## Precedent to copy (read it, do not re-derive)
/Users/bear/Documents/CoWork/bear-textbooks/books/professor-bears-claude-notebook/youtube/claude-liam-lecture-model-times-effort/ : make_sheet.py, scenes.py (pacing helpers until/finish), pad_audio.py, whisper_check.py, BUILD-PROMPT.md (exact command order).

## Next command
Write ACTS.md from chapters/06-bias-where-it-enters-and-who-is-responsible.md (8 conflict blocks at lines 48-56, 99-106, 114-122, 211-219, 242-250, 285-293, 310-318, 531-613).

## Progress log
- 2026-10-10 evidence/evidence.py + evidence.json + evidence.stdout.txt written and run (A bias-vs-n, B IPW, C kappa, D funnel, E reweight, F impossibility 0.2/0.4667, G constructed graph paths).
- captures/: propublica.png (real FP/FN table, ring [0.236,0.125,0.527,0.155]), kleinberg.png (arXiv abstract), aoc-p20.png (Agents of Chaos p.20 rendered from PDF). NYDFS page blocked by Cloudflare (403): NOT bypassed; beat B54 quotes the regulator on a drawn card (text fetched via WebFetch 2026-10-10).
- Facts verified in-session: AoC Case #6 (Quinn, Kimi K2.5, 'unknown error', PDF p.20); ProPublica 44.9/23.5, 47.7/28.0; DFS press release 2026-03-23 quotes; Kleinberg abstract; Squire 1988 (2,376,523 ballots; Gallup 50,000 NOT verified -> stripped).
- Plan: 11 acts, body B01-B82 (Manim + 3 BrowserCaptures + 2-3 CCPlainShell + 1-2 LectureEvidenceTable), act cards = Remotion FormACard. Next: write make_sheet.py (copy structure of the model-times-effort precedent), then audio.
- 2026-10-10 later: scenes.py has B01-B47 (stills viewed on contact sheets _qc/c1-c3.png; fixes applied). render_one.sh <Class> renders a last-frame still into scratch; contact.py makes sheets. Remaining Manim scenes: B48 is a capture (no scene); B49,B50,B52,B53,B54,B56-B63,B65-B74,B76-B82 still to write (see make_sheet.py for class names: f"{bid}_{Name}").
- Next command: write remaining scenes (append to scenes.py), then python3 make_sheet.py, pad_audio, whisper check, BOPEN (lecture template build.py --sheet), art run.
- 2026-10-10 (after audio+scenes): ALL 82 Manim scenes written in scenes.py; stills viewed (_qc/c1..c7.png). pad_audio.py run; BOPEN built (opening/, media/BOPEN.mp4). NEXT: Gate A/B pre-audit (scratch folder with only scenes.py + beat_sheet.json: runtime/qc/static_scene_check.py ; manim_layout_audit.py --curve-strict), whisper check, CHECKS-REPORT.md, README.md, BUILD-PROMPT.md, build_srt.py run, then `./brutalist.art/art run <reel> --height 2160`.
- 2026-10-10: Gate A (static, all 74 classes clean) and Gate B (layout, all clean after fixes) pre-audited; whisper check done (WHISPER-CHECK.md, all beats heard right; BOPEN order series->title->summary OK). README/CHECKS-REPORT/BUILD-PROMPT/build_srt written. LAUNCHED `art run` (review cut at 4K) in background: log = art-run.log. NEXT: when it finishes read art-run.log, fix GATE V/T failures (move old clips to _superseded/ before re-render), look at _qc frames + qc-sheet.png, then `art final`, bookend_check, master verification (ffprobe 3840x2160, duration = sum of audio, silent tail, .verified.json), append sha256 to BUILD-LOG, report.
- 2026-10-10: first `art run` compiled the full cut; GATE V FAILED (1 BLOCKER B42 edge-bleed, 17 MAJOR low-contrast/empty). Fix applied: KRAFT/BAR3 colours pulled within 28/channel of the stage (Gate V counts them as ground), B29 chips shown at start, B42 shifted, go()/finish() now clamp to the beat's audio (B01/B09/B42 had overshot). Old Manim clips in _superseded/round1/. Re-running `art run` (log art-run2.log). Remotion clips (25) are kept in media/ and not re-rendered.
- round2: B42 question row shifted (edge-bleed); re-running art run (art-run3.log)
- round3: evidence stdout shortened (B10/B51 shell lines), B48/B75 capture camera fixed; B10,B48,B51,B75 re-rendered (art-run4.log)
- round4: B07,B18,B66-B71 redrawn (layout); art run (art-run5.log) then art final
- art run clean (Gate V PASS). Launched art final (final-build.log).
- round5: GATE T first run: 37 FAILs (dark node outlines read as a second text run §8.6b; ring on B43; B75 zoom; B81 overflow). Fix: box strokes grey (GREYLINE), B43 ring padded, B75 scale 1.3, B81 claim narrower. Re-rendering all Manim (art-run6.log), then art final.
- round6: only B43 failed GATE T (ring -> FP row only), B82 Gate V contrast; re-running (art-run7.log + final)
- DONE 2026-10-10: master built and verified: exports/landscape/claude-liam-lecture-bias-where-it-enters.mp4 (sha256 783c55ce…bfe, 3840x2160, 1386.17 s). All gates PASS (Gate V, GATE T, bookend, A, B, F, PROOF). Nothing left to run except Bear's listening verdict. Do NOT re-run make_sheet.py (it wipes build stamps); if anything changes, re-run `art run` then `art final`.
