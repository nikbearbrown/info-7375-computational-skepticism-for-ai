# BUILD-LOG - Key Terms: Model Explainability

Built end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).

## 2026-11-11 22:20 - stages: sheet, voice, pad, whisper, resheet, card, capture

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 0 already voiced, about 16.7 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-model-explainability --only ...` exit 0, 354 s
- voiced 56 beat(s); all 56 beats have audio, 832.8 s
`python3 pad_audio.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 6 s
- pad_audio: 13 beat(s) padded; total 837.1 s
`python3 whisper_check.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 46 s
- whisper: 56 beats, 0 flagged, lowest 0.88
`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 14.0 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 build.py --out opening-title-card ...` exit 0, 8 s
- BOPEN card built for 16.26 s; portrait: ['/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg']
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 367 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
- stages done: sheet, voice, pad, whisper, resheet, card, capture

## 2026-11-11 23:39 - stages: capture, review, final, checks

`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 3 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 682 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 0, 232 s
- [typecheck] §8.10 B1205: SKIP
- [typecheck] §8.10 B1206: SKIP
- [typecheck] §8.10 BVDT: 0.97  ← ADVISORY
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:50  remotion:6
- [art] SKIN LINT: BOPEN: palette=claude but the cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk
- [art] build stamp → beat_sheet.json (56/56 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/exports/landscape/claude-liam-lecture-key-terms-model-explainability.mp4  (838.2s, audio: per-beat timeline (source audio preserved), dra
- [art] slots: 56/56 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0304:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VI
- bookend_check exit 0: [bookend] PASS — four bookends correct for claude-liam-lecture-key-terms-model-explainability
- loudness_check exit 0: [loud] checking 56 beats for per-beat silence … | [loud] PASS  -24.46 LUFS  tp=-2.84 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/exports/landscape/claude-liam-lecture-key-terms-model-explainability.mp4: 3840x2160 at 24/1, 838.17 s (14.0 min); sum of audio 837.10 s; difference +1.07 s; 57 MB
- stages done: capture, review, final, checks

## 2026-11-12 01:20 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 24 already voiced, about 22.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 2 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-model-explainability --only ...` exit 0, 394 s
- voiced 32 beat(s); all 56 beats have audio, 1100.2 s
`python3 pad_audio.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 6 s
- pad_audio: 9 beat(s) padded; total 1103.7 s
`python3 whisper_check.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 243 s
- whisper: 56 beats, 0 flagged, lowest 0.88
`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 77 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
- removed 22 stale clip(s): B0201, B0202, B0203, B0301, B0302, B0303, B0401, B0402, B0403, B0501, B0502, B0503 ...
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 435 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 1740 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 2, 19 s
```
[typecheck] §8.10 B0502: SKIP
[typecheck] §8.10 B0503: SKIP
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
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1105: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1206: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/TYPECHECK.md
```

## 2026-11-12 02:09 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 89 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 16 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 832 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 2, 10 s
```
[typecheck] §8.10 B0502: SKIP
[typecheck] §8.10 B0503: SKIP
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
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1105: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1206: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/TYPECHECK.md
```

## 2026-11-12 04:08 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 44 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 2 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 227 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 2, 9 s
```
[typecheck] §8.10 B0502: SKIP
[typecheck] §8.10 B0503: SKIP
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
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1105: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1206: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/TYPECHECK.md
```

## 2026-11-12 05:04 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 44 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 2 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 226 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 2, 9 s
```
[typecheck] §8.10 B0502: SKIP
[typecheck] §8.10 B0503: SKIP
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
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1105: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1206: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/TYPECHECK.md
```

## 2026-11-12 05:57 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 05 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-model-explainability: 56 beats (50 deck steps), 56 already voiced, about 18.4 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 50 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 5 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 618 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 2, 11 s
```
[typecheck] §8.10 B0502: SKIP
[typecheck] §8.10 B0503: SKIP
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
[typecheck] §8.10 B0804: SKIP
[typecheck] §8.10 B0901: SKIP
[typecheck] §8.10 B0902: SKIP
[typecheck] §8.10 B0903: SKIP
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
[typecheck] §8.10 B1101: SKIP
[typecheck] §8.10 B1102: SKIP
[typecheck] §8.10 B1103: SKIP
[typecheck] §8.10 B1104: SKIP
[typecheck] §8.10 B1105: SKIP
[typecheck] §8.10 B1201: SKIP
[typecheck] §8.10 B1202: SKIP
[typecheck] §8.10 B1203: SKIP
[typecheck] §8.10 B1204: SKIP
[typecheck] §8.10 B1205: SKIP
[typecheck] §8.10 B1206: SKIP
[typecheck] §8.10 BVDT: SKIP
[typecheck] §8.10 BHTF: SKIP
[typecheck] §8.10 BOUT: SKIP
[typecheck] GATE T: FAIL (1 pixel beats, 0 sweep, 0 shape)
[typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
[art final] GATE T BLOCKED: the type-size check found text too small to read. TYPECHECK.md lists each one — fix before final cut.
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/TYPECHECK.md
```

## 2026-11-12 06:57 - stages: card, capture, review, final, checks

`python3 bookends.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 65 s
- bookends: BOPEN: 1 drawn frames, 16.25 s; BIDEA: 264 drawn frames, 16.12 s; BDEFS: 420 drawn frames, 20.54 s; BVDT: 474 drawn frames, 23.17 s; BHTF: 490 drawn frames, 21.75 s; BOUT: 1 drawn frames, 4.25 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-206.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-model-explainability ...` exit 0, 11 s
- captured 50 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/media
`art run claude-liam-lecture-key-terms-model-explainability --height ...` exit 0, 521 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=112 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability  (QC gates: on)
`art final claude-liam-lecture-key-terms-model-explainability --local ...` exit 0, 492 s
- [typecheck] §8.10 B1205: SKIP
- [typecheck] §8.10 B1206: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:50  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (56/56 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/exports/landscape/claude-liam-lecture-key-terms-model-explainability.mp4  (1104.8s, audio: per-beat timeline (source audio preserved), dr
- [art] slots: 56/56 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0204:VIDEO B0301:VIDEO B0302:VIDEO B0303:VIDEO B0304:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 56 beats for per-beat silence … | [loud] PASS  -24.49 LUFS  tp=-2.78 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-model-explainability/exports/landscape/claude-liam-lecture-key-terms-model-explainability.mp4: 3840x2160 at 24/1, 1104.75 s (18.4 min); sum of audio 1103.70 s; difference +1.05 s; 72 MB
- stages done: card, capture, review, final, checks
