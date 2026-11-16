# BUILD-LOG - Key Terms: Fairness Metrics

Built end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).

## 2026-11-11 22:33 - stages: sheet, voice, pad, whisper, resheet, card, capture

`python3 make_film.py 07 ...` exit 0, 4 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 0 already voiced, about 17.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 2 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-fairness-metrics --only ...` exit 0, 469 s
- voiced 58 beat(s); all 58 beats have audio, 849.9 s
`python3 pad_audio.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 8 s
- pad_audio: 14 beat(s) padded; total 854.7 s
`python3 whisper_check.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 140 s
- whisper: 58 beats, 0 flagged, lowest 0.88
`python3 make_film.py 07 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 58 already voiced, about 14.2 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 build.py --out opening-title-card ...` exit 0, 9 s
- BOPEN card built for 14.78 s; portrait: ['/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-230.jpg']
`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 274 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
- stages done: sheet, voice, pad, whisper, resheet, card, capture

## 2026-11-11 23:55 - stages: capture, review, final, checks

`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 5 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
`art run claude-liam-lecture-key-terms-fairness-metrics --height ...` exit 0, 695 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=116 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics  (QC gates: on)
`art final claude-liam-lecture-key-terms-fairness-metrics --local ...` exit 0, 293 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: 0.98  ← ADVISORY
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:52  remotion:6
- [art] SKIN LINT: BOPEN: palette=claude but the cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk
- [art] build stamp → beat_sheet.json (58/58 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4  (855.9s, audio: per-beat timeline (source audio preserved), drawtext: n
- [art] slots: 58/58 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VI
- bookend_check exit 0: [bookend] PASS — four bookends correct for claude-liam-lecture-key-terms-fairness-metrics
- loudness_check exit 0: [loud] checking 58 beats for per-beat silence … | [loud] PASS  -24.44 LUFS  tp=-2.95 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4: 3840x2160 at 24/1, 855.88 s (14.3 min); sum of audio 854.72 s; difference +1.15 s; 56 MB
- stages done: capture, review, final, checks

## 2026-11-12 01:18 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 07 ...` exit 0, 4 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 28 already voiced, about 21.9 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-fairness-metrics --only ...` exit 0, 363 s
- voiced 30 beat(s); all 58 beats have audio, 1098.3 s
`python3 pad_audio.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 6 s
- pad_audio: 9 beat(s) padded; total 1102.5 s
`python3 whisper_check.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 168 s
- whisper: 58 beats, 0 flagged, lowest 0.88
`python3 make_film.py 07 ...` exit 0, 3 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 58 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 63 s
- bookends: BOPEN: 1 drawn frames, 14.79 s; BIDEA: 301 drawn frames, 18.50 s; BDEFS: 523 drawn frames, 24.75 s; BVDT: 534 drawn frames, 26.17 s; BHTF: 461 drawn frames, 20.38 s; BOUT: 1 drawn frames, 4.00 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-230.jpg
- removed 20 stale clip(s): B0201, B0202, B0301, B0302, B0401, B0403, B0503, B0601, B0602, B0603, B0701, B0702 ...
`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 196 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
`art run claude-liam-lecture-key-terms-fairness-metrics --height ...` exit 0, 1916 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=116 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics  (QC gates: on)
`art final claude-liam-lecture-key-terms-fairness-metrics --local ...` exit 0, 675 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:52  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (58/58 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4  (1103.6s, audio: per-beat timeline (source audio preserved), drawtext: 
- [art] slots: 58/58 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 58 beats for per-beat silence … | [loud] PASS  -24.47 LUFS  tp=-2.69 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4: 3840x2160 at 24/1, 1103.62 s (18.4 min); sum of audio 1102.52 s; difference +1.11 s; 68 MB
- stages done: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

## 2026-11-12 04:18 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 07 ...` exit 0, 2 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 58 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 48 s
- bookends: BOPEN: 1 drawn frames, 14.79 s; BIDEA: 301 drawn frames, 18.50 s; BDEFS: 523 drawn frames, 24.75 s; BVDT: 534 drawn frames, 26.17 s; BHTF: 461 drawn frames, 20.38 s; BOUT: 1 drawn frames, 4.00 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-230.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 2 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
`art run claude-liam-lecture-key-terms-fairness-metrics --height ...` exit 0, 233 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=116 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics  (QC gates: on)
`art final claude-liam-lecture-key-terms-fairness-metrics --local ...` exit 0, 219 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:52  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (58/58 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4  (1103.6s, audio: per-beat timeline (source audio preserved), drawtext: 
- [art] slots: 58/58 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 58 beats for per-beat silence … | [loud] PASS  -24.47 LUFS  tp=-2.69 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4: 3840x2160 at 24/1, 1103.62 s (18.4 min); sum of audio 1102.52 s; difference +1.11 s; 68 MB
- stages done: resheet, card, capture, review, final, checks

## 2026-11-12 06:08 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 07 ...` exit 0, 5 s
- claude-liam-lecture-key-terms-fairness-metrics: 58 beats (52 deck steps), 58 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 64 s
- bookends: BOPEN: 1 drawn frames, 14.79 s; BIDEA: 301 drawn frames, 18.50 s; BDEFS: 523 drawn frames, 24.75 s; BVDT: 534 drawn frames, 26.17 s; BHTF: 461 drawn frames, 20.38 s; BOUT: 1 drawn frames, 4.00 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-230.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 4 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
`art run claude-liam-lecture-key-terms-fairness-metrics --height ...` exit 0, 582 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=116 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics  (QC gates: on)
`art final claude-liam-lecture-key-terms-fairness-metrics --local ...` exit 2, 12 s
```
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B0904: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1301: SKIP
[typecheck] §8.10 B1302: SKIP
[typecheck] §8.10 B1303: SKIP
[typecheck] §8.10 B1304: SKIP
[typecheck] §8.10 B1305: SKIP
[typecheck] §8.10 B1306: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/TYPECHECK.md
```

## 2026-11-12 07:16 - stages: card, capture, review, final, checks

`python3 bookends.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 63 s
- bookends: BOPEN: 1 drawn frames, 14.79 s; BIDEA: 301 drawn frames, 18.50 s; BDEFS: 523 drawn frames, 24.75 s; BVDT: 534 drawn frames, 26.17 s; BHTF: 461 drawn frames, 20.38 s; BOUT: 1 drawn frames, 4.00 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-230.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-fairness-metrics ...` exit 0, 5 s
- captured 52 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/media
`art run claude-liam-lecture-key-terms-fairness-metrics --height ...` exit 0, 565 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=116 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics  (QC gates: on)
`art final claude-liam-lecture-key-terms-fairness-metrics --local ...` exit 0, 451 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:52  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (58/58 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4  (1103.6s, audio: per-beat timeline (source audio preserved), drawtext: 
- [art] slots: 58/58 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 58 beats for per-beat silence … | [loud] PASS  -24.47 LUFS  tp=-2.69 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-fairness-metrics/exports/landscape/claude-liam-lecture-key-terms-fairness-metrics.mp4: 3840x2160 at 24/1, 1103.62 s (18.4 min); sum of audio 1102.52 s; difference +1.11 s; 69 MB
- stages done: card, capture, review, final, checks
