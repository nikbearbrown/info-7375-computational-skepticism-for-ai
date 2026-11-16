# BUILD-LOG - Key Terms: Robustness

Built end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).

## 2026-11-11 22:06 - stages: sheet, voice, pad, whisper, resheet, card, capture

`python3 make_film.py 04 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 0 already voiced, about 17.8 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-robustness --only ...` exit 0, 458 s
- voiced 60 beat(s); all 60 beats have audio, 880.3 s
`python3 pad_audio.py claude-liam-lecture-key-terms-robustness ...` exit 0, 6 s
- pad_audio: 16 beat(s) padded; total 885.7 s
`python3 whisper_check.py claude-liam-lecture-key-terms-robustness ...` exit 0, 75 s
- whisper: 60 beats, 2 flagged, lowest 0.85
`python3 make_film.py 04 ...` exit 0, 9 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 60 already voiced, about 14.8 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 3 s
`python3 build.py --out opening-title-card ...` exit 0, 12 s
- BOPEN card built for 14.63 s; portrait: ['/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-25.jpg']
`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 330 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
- stages done: sheet, voice, pad, whisper, resheet, card, capture

## 2026-11-11 23:19 - stages: capture, review, final, checks

`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 7 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
`art run claude-liam-lecture-key-terms-robustness --height ...` exit 0, 699 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=120 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness  (QC gates: on)
`art final claude-liam-lecture-key-terms-robustness --local ...` exit 0, 316 s
- [typecheck] §8.10 B1505: SKIP
- [typecheck] §8.10 B1506: SKIP
- [typecheck] §8.10 BVDT: 0.97  ← ADVISORY
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:54  remotion:6
- [art] SKIN LINT: BOPEN: palette=claude but the cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk
- [art] build stamp → beat_sheet.json (60/60 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4  (886.8s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL over
- [art] slots: 60/60 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0601:VIDEO B0602:VIDEO B0603:VIDEO B0701:VI
- bookend_check exit 0: [bookend] PASS — four bookends correct for claude-liam-lecture-key-terms-robustness
- loudness_check exit 0: [loud] checking 60 beats for per-beat silence … | [loud] PASS  -24.50 LUFS  tp=-2.82 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4: 3840x2160 at 24/1, 886.79 s (14.8 min); sum of audio 885.66 s; difference +1.13 s; 63 MB
- stages done: capture, review, final, checks

## 2026-11-12 01:20 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 04 ...` exit 0, 10 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 26 already voiced, about 23.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 3 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-robustness --only ...` exit 0, 418 s
- voiced 34 beat(s); all 60 beats have audio, 1154.5 s
`python3 pad_audio.py claude-liam-lecture-key-terms-robustness ...` exit 0, 7 s
- pad_audio: 13 beat(s) padded; total 1159.1 s
`python3 whisper_check.py claude-liam-lecture-key-terms-robustness ...` exit 0, 285 s
- whisper: 60 beats, 1 flagged, lowest 0.86
`python3 make_film.py 04 ...` exit 0, 8 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 60 already voiced, about 19.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 2 s
`python3 bookends.py claude-liam-lecture-key-terms-robustness ...` exit 0, 96 s
- bookends: BOPEN: 1 drawn frames, 14.62 s; BIDEA: 259 drawn frames, 17.12 s; BDEFS: 441 drawn frames, 21.25 s; BVDT: 445 drawn frames, 22.42 s; BHTF: 462 drawn frames, 20.46 s; BOUT: 1 drawn frames, 3.79 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-25.jpg
- removed 20 stale clip(s): B0201, B0202, B0301, B0302, B0401, B0402, B0501, B0502, B0601, B0602, B0701, B0702 ...
`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 457 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
`art run claude-liam-lecture-key-terms-robustness --height ...` exit 0, 1759 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=120 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness  (QC gates: on)
`art final claude-liam-lecture-key-terms-robustness --local ...` exit 0, 825 s
- [typecheck] §8.10 B1505: SKIP
- [typecheck] §8.10 B1506: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:54  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (60/60 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4  (1160.3s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL ove
- [art] slots: 60/60 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0601:VIDEO B0602:VIDEO B0603:VIDEO B0701:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 60 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.74 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4: 3840x2160 at 24/1, 1160.29 s (19.3 min); sum of audio 1159.07 s; difference +1.22 s; 78 MB
- stages done: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

## 2026-11-12 03:59 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 04 ...` exit 0, 5 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 60 already voiced, about 19.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-robustness ...` exit 0, 43 s
- bookends: BOPEN: 1 drawn frames, 14.62 s; BIDEA: 259 drawn frames, 17.12 s; BDEFS: 441 drawn frames, 21.25 s; BVDT: 445 drawn frames, 22.42 s; BHTF: 462 drawn frames, 20.46 s; BOUT: 1 drawn frames, 3.79 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-25.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 2 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
`art run claude-liam-lecture-key-terms-robustness --height ...` exit 0, 242 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=120 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness  (QC gates: on)
`art final claude-liam-lecture-key-terms-robustness --local ...` exit 0, 235 s
- [typecheck] §8.10 B1505: SKIP
- [typecheck] §8.10 B1506: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:54  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (60/60 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4  (1160.3s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL ove
- [art] slots: 60/60 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0601:VIDEO B0602:VIDEO B0603:VIDEO B0701:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 60 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.74 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4: 3840x2160 at 24/1, 1160.29 s (19.3 min); sum of audio 1159.07 s; difference +1.22 s; 78 MB
- stages done: resheet, card, capture, review, final, checks

## 2026-11-12 05:57 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 04 ...` exit 0, 5 s
- claude-liam-lecture-key-terms-robustness: 60 beats (54 deck steps), 60 already voiced, about 19.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-robustness ...` exit 0, 49 s
- bookends: BOPEN: 1 drawn frames, 14.62 s; BIDEA: 259 drawn frames, 17.12 s; BDEFS: 441 drawn frames, 21.25 s; BVDT: 445 drawn frames, 22.42 s; BHTF: 462 drawn frames, 20.46 s; BOUT: 1 drawn frames, 3.79 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-25.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 6 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
`art run claude-liam-lecture-key-terms-robustness --height ...` exit 0, 634 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=120 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness  (QC gates: on)
`art final claude-liam-lecture-key-terms-robustness --local ...` exit 2, 12 s
```
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
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
[typecheck] §8.10 B1301: SKIP
[typecheck] §8.10 B1302: SKIP
[typecheck] §8.10 B1303: SKIP
[typecheck] §8.10 B1304: SKIP
[typecheck] §8.10 B1401: SKIP
[typecheck] §8.10 B1402: SKIP
[typecheck] §8.10 B1403: SKIP
[typecheck] §8.10 B1404: SKIP
[typecheck] §8.10 B1405: SKIP
[typecheck] §8.10 B1501: SKIP
[typecheck] §8.10 B1502: SKIP
[typecheck] §8.10 B1503: SKIP
[typecheck] §8.10 B1504: SKIP
[typecheck] §8.10 B1505: SKIP
[typecheck] §8.10 B1506: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/TYPECHECK.md
```

## 2026-11-12 06:56 - stages: card, capture, review, final, checks

`python3 bookends.py claude-liam-lecture-key-terms-robustness ...` exit 0, 56 s
- bookends: BOPEN: 1 drawn frames, 14.62 s; BIDEA: 259 drawn frames, 17.12 s; BDEFS: 441 drawn frames, 21.25 s; BVDT: 445 drawn frames, 22.42 s; BHTF: 462 drawn frames, 20.46 s; BOUT: 1 drawn frames, 3.79 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-25.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-robustness ...` exit 0, 8 s
- captured 54 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/media
`art run claude-liam-lecture-key-terms-robustness --height ...` exit 0, 571 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=120 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness  (QC gates: on)
`art final claude-liam-lecture-key-terms-robustness --local ...` exit 0, 512 s
- [typecheck] §8.10 B1505: SKIP
- [typecheck] §8.10 B1506: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:54  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (60/60 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4  (1160.3s, audio: per-beat timeline (source audio preserved), drawtext: no — PIL ove
- [art] slots: 60/60 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0601:VIDEO B0602:VIDEO B0603:VIDEO B0701:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 60 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.74 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-robustness/exports/landscape/claude-liam-lecture-key-terms-robustness.mp4: 3840x2160 at 24/1, 1160.29 s (19.3 min); sum of audio 1159.07 s; difference +1.22 s; 78 MB
- stages done: card, capture, review, final, checks
