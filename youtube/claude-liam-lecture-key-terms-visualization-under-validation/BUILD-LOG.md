# BUILD-LOG - Key Terms: Visualization Under Validation

Built end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).

## 2026-11-11 22:49 - stages: sheet, voice, pad, whisper, resheet, card, capture

`python3 make_film.py 10 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 0 already voiced, about 15.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-visualization-under-validation --only ...` exit 0, 248 s
- voiced 56 beat(s); all 56 beats have audio, 740.5 s
`python3 pad_audio.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 4 s
- pad_audio: 14 beat(s) padded; total 744.7 s
`python3 whisper_check.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 72 s
- whisper: 56 beats, 0 flagged, lowest 0.89
`python3 make_film.py 10 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 12.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 build.py --out opening-title-card ...` exit 0, 9 s
- BOPEN card built for 16.19 s; portrait: ['/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg']
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 183 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
- stages done: sheet, voice, pad, whisper, resheet, card, capture

## 2026-11-12 00:04 - stages: capture, review, final, checks

`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 6 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 645 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 0, 342 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: 0.98  ← ADVISORY
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:50  remotion:6
- [art] SKIN LINT: BOPEN: palette=claude but the cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk
- [art] build stamp → beat_sheet.json (56/56 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/exports/landscape/claude-liam-lecture-key-terms-visualization-under-validation.mp4  (745.9s, audio: per-beat timeline (source a
- [art] slots: 56/56 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VI
- bookend_check exit 0: [bookend] PASS — four bookends correct for claude-liam-lecture-key-terms-visualization-under-validation
- loudness_check exit 0: [loud] checking 56 beats for per-beat silence … | [loud] PASS  -24.40 LUFS  tp=-2.82 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/exports/landscape/claude-liam-lecture-key-terms-visualization-under-validation.mp4: 3840x2160 at 24/1, 745.92 s (12.4 min); sum of audio 744.72 s; difference +1.20 s; 52 MB
- stages done: capture, review, final, checks

## 2026-11-12 01:13 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks


## 2026-11-12 02:26 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 10 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 24 already voiced, about 21.2 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-visualization-under-validation --only ...` exit 0, 178 s
- voiced 32 beat(s); all 56 beats have audio, 1017.2 s
`python3 pad_audio.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 4 s
- pad_audio: 10 beat(s) padded; total 1021.7 s
`python3 whisper_check.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 122 s
- whisper: 56 beats, 0 flagged, lowest 0.89
`python3 make_film.py 10 ...` exit 0, 5 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 17.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 63 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
- removed 21 stale clip(s): B0201, B0202, B0301, B0302, B0402, B0403, B0501, B0502, B0503, B0601, B0602, B0603 ...
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 235 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 617 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 2, 15 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0704: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/TYPECHECK.md
```

## 2026-11-12 02:47 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 10 ...` exit 0, 6 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 17.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 69 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 7 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 383 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 2, 12 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0704: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/TYPECHECK.md
```

## 2026-11-12 04:37 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 10 ...` exit 0, 4 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 17.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 43 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 2 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 215 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 2, 9 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0704: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/TYPECHECK.md
```

## 2026-11-12 05:24 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 10 ...` exit 0, 4 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 17.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 43 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 2 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 214 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 2, 9 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0704: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/TYPECHECK.md
```

## 2026-11-12 06:19 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 10 ...` exit 0, 5 s
- claude-liam-lecture-key-terms-visualization-under-validation: 56 beats (50 deck steps), 56 already voiced, about 17.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 61 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 4 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 613 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 2, 11 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
[typecheck] §8.10 B0604: SKIP
[typecheck] §8.10 B0701: SKIP
[typecheck] §8.10 B0702: SKIP
[typecheck] §8.10 B0703: SKIP
[typecheck] §8.10 B0704: SKIP
[typecheck] §8.10 B0801: SKIP
[typecheck] §8.10 B0802: SKIP
[typecheck] §8.10 B0803: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/TYPECHECK.md
```

## 2026-11-12 07:35 - stages: card, capture, review, final, checks

`python3 bookends.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 60 s
- bookends: BOPEN: 1 drawn frames, 16.21 s; BIDEA: 271 drawn frames, 16.00 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 451 drawn frames, 21.88 s; BHTF: 471 drawn frames, 20.88 s; BOUT: 1 drawn frames, 4.83 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-149.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-visualization-under-validation ...` exit 0, 5 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/media
`art run claude-liam-lecture-key-terms-visualization-under-validation --height ...` exit 0, 506 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-visualization-under-validation --local ...` exit 0, 435 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:50  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (56/56 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/exports/landscape/claude-liam-lecture-key-terms-visualization-under-validation.mp4  (1022.8s, audio: per-beat timeline (source 
- [art] slots: 56/56 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 56 beats for per-beat silence … | [loud] PASS  -24.57 LUFS  tp=-2.78 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-visualization-under-validation/exports/landscape/claude-liam-lecture-key-terms-visualization-under-validation.mp4: 3840x2160 at 24/1, 1022.75 s (17.0 min); sum of audio 1021.74 s; difference +1.01 s; 67 MB
- stages done: card, capture, review, final, checks
