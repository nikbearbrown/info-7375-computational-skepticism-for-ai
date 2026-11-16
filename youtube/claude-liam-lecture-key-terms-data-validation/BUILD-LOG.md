# BUILD-LOG - Key Terms: Data Validation

Built end to end by Claude Code with `exam-prep-deck-films/tools/build_film.py` (Bear asked for the films, 2026-11-11).

## 2026-11-11 22:06 - stages: sheet, voice, pad, whisper, resheet, card, capture

`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 0 already voiced, about 16.7 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-data-validation --only ...` exit 0, 454 s
- voiced 55 beat(s); all 55 beats have audio, 808.9 s
`python3 pad_audio.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 6 s
- pad_audio: 14 beat(s) padded; total 813.6 s
`python3 whisper_check.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 82 s
- whisper: 55 beats, 0 flagged, lowest 0.88
`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 55 already voiced, about 13.6 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 build.py --out opening-title-card ...` exit 0, 9 s
- BOPEN card built for 15.81 s; portrait: ['/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-32.jpg']
`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 311 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
- stages done: sheet, voice, pad, whisper, resheet, card, capture

## 2026-11-11 23:22 - stages: capture, review, final, checks

`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 3 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
`art run claude-liam-lecture-key-terms-data-validation --height ...` exit 0, 742 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=110 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-data-validation --local ...` exit 0, 237 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: 0.97  ← ADVISORY
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:49  remotion:6
- [art] SKIN LINT: BOPEN: palette=claude but the cold open is 'un-annotated' — COLD OPEN LAW wants ClaudeComposerAsk
- [art] build stamp → beat_sheet.json (55/55 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4  (814.8s, audio: per-beat timeline (source audio preserved), drawtext: no 
- [art] slots: 55/55 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VIDEO B0603:VI
- bookend_check exit 0: [bookend] PASS — four bookends correct for claude-liam-lecture-key-terms-data-validation
- loudness_check exit 0: [loud] checking 55 beats for per-beat silence … | [loud] PASS  -24.52 LUFS  tp=-2.92 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4: 3840x2160 at 24/1, 814.75 s (13.6 min); sum of audio 813.65 s; difference +1.10 s; 57 MB
- stages done: capture, review, final, checks

## 2026-11-12 01:09 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 54 already voiced, about 13.7 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 2 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-data-validation --only ...` exit 0, 21 s
- voiced 1 beat(s); all 55 beats have audio, 813.2 s
`python3 pad_audio.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 6 s
- pad_audio: 0 beat(s) padded; total 813.2 s

## 2026-11-12 01:20 - stages: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 25 already voiced, about 22.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 2 s
- factcheck_check.py exit 0 (0 clean, 1 advisories, 2 blocker)
`python3 generate_audio_kokoro.py claude-liam-lecture-key-terms-data-validation --only ...` exit 0, 403 s
- voiced 30 beat(s); all 55 beats have audio, 1094.9 s
`python3 pad_audio.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 6 s
- pad_audio: 12 beat(s) padded; total 1099.2 s
`python3 whisper_check.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 203 s
- whisper: 55 beats, 0 flagged, lowest 0.88
`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 55 already voiced, about 18.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 69 s
- bookends: BOPEN: 1 drawn frames, 15.79 s; BIDEA: 283 drawn frames, 17.38 s; BDEFS: 520 drawn frames, 24.79 s; BVDT: 422 drawn frames, 20.92 s; BHTF: 456 drawn frames, 20.17 s; BOUT: 1 drawn frames, 4.04 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-32.jpg
- removed 18 stale clip(s): B0201, B0202, B0301, B0401, B0402, B0403, B0501, B0502, B0601, B0602, B0701, B0702 ...
`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 392 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
`art run claude-liam-lecture-key-terms-data-validation --height ...` exit 0, 1835 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=110 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-data-validation --local ...` exit 0, 835 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:49  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (55/55 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4  (1100.4s, audio: per-beat timeline (source audio preserved), drawtext: no
- [art] slots: 55/55 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VIDEO B0603:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 55 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.80 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4: 3840x2160 at 24/1, 1100.38 s (18.3 min); sum of audio 1099.20 s; difference +1.17 s; 72 MB
- stages done: sheet, voice, pad, whisper, resheet, card, capture, review, final, checks

## 2026-11-12 03:50 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 55 already voiced, about 18.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 45 s
- bookends: BOPEN: 1 drawn frames, 15.79 s; BIDEA: 283 drawn frames, 17.38 s; BDEFS: 520 drawn frames, 24.79 s; BVDT: 422 drawn frames, 20.92 s; BHTF: 456 drawn frames, 20.17 s; BOUT: 1 drawn frames, 4.04 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-32.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 2 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
`art run claude-liam-lecture-key-terms-data-validation --height ...` exit 0, 226 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=110 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-data-validation --local ...` exit 0, 219 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:49  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (55/55 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4  (1100.4s, audio: per-beat timeline (source audio preserved), drawtext: no
- [art] slots: 55/55 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VIDEO B0603:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 55 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.80 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4: 3840x2160 at 24/1, 1100.38 s (18.3 min); sum of audio 1099.20 s; difference +1.17 s; 72 MB
- stages done: resheet, card, capture, review, final, checks

## 2026-11-12 05:56 - stages: resheet, card, capture, review, final, checks

`python3 make_film.py 03 ...` exit 0, 0 s
- claude-liam-lecture-key-terms-data-validation: 55 beats (49 deck steps), 55 already voiced, about 18.3 min
`python3 -c import json,jsonschema,sys;jsonschema.validate(json.load(open(sys.argv[1])),json.load(open(sys.argv[2]))) beat_sheet.json ...` exit 0, 1 s
`python3 bookends.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 47 s
- bookends: BOPEN: 1 drawn frames, 15.79 s; BIDEA: 283 drawn frames, 17.38 s; BDEFS: 520 drawn frames, 24.79 s; BVDT: 422 drawn frames, 20.92 s; BHTF: 456 drawn frames, 20.17 s; BOUT: 1 drawn frames, 4.04 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-32.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 3 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
`art run claude-liam-lecture-key-terms-data-validation --height ...` exit 0, 608 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=110 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-data-validation --local ...` exit 2, 12 s
```
[typecheck] §8.10 B0504: SKIP
[typecheck] §8.10 B0601: SKIP
[typecheck] §8.10 B0602: SKIP
[typecheck] §8.10 B0603: SKIP
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
[typecheck] §8.10 B1001: SKIP
[typecheck] §8.10 B1002: SKIP
[typecheck] §8.10 B1003: SKIP
[typecheck] §8.10 B1004: SKIP
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
[art final] See: /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/TYPECHECK.md
```

## 2026-11-12 06:55 - stages: card, capture, review, final, checks

`python3 bookends.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 52 s
- bookends: BOPEN: 1 drawn frames, 15.79 s; BIDEA: 283 drawn frames, 17.38 s; BDEFS: 520 drawn frames, 24.79 s; BVDT: 422 drawn frames, 20.92 s; BHTF: 456 drawn frames, 20.17 s; BOUT: 1 drawn frames, 4.04 s; portrait: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/remotion/public/professor-bear/professor-bear-1x1-32.jpg
`python3 deck_capture.py claude-liam-lecture-key-terms-data-validation ...` exit 0, 3 s
- captured 49 deck beats into /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/media
`art run claude-liam-lecture-key-terms-data-validation --height ...` exit 0, 542 s
- [run] GATE L — beat-mix lint
- [run] GATE SHAPE — finance chart-shape enforcement
- [run] GATE V — frame-level visual QC on the compiled reel
- [gate-v] frames=110 BLOCKER=0 MAJOR=0 → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/_qc/REPORT.md
- [run] done → /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation  (QC gates: on)
`art final claude-liam-lecture-key-terms-data-validation --local ...` exit 0, 458 s
- [typecheck] §8.10 B1305: SKIP
- [typecheck] §8.10 B1306: SKIP
- [typecheck] §8.10 BVDT: SKIP
- [typecheck] §8.10 BHTF: SKIP
- [typecheck] §8.10 BOUT: SKIP
- [typecheck] GATE T: PASS
- [typecheck] (Gate T is the type-size check: it measures the smallest text in each beat of the finished film and fails any beat whose text is too small to read on a screen. TYPECHECK.md lists which beats and why.)
- [art] motion histogram: screen:49  graphic:6
- [art] SKIN LINT: NO RENDERABLE BEATS: no beat carries a shot.remotion.pattern or Manim annotation — the pipeline will render NOTHING and every slot becomes a YOU-slate. The sheet was authored without the scene contract.
- [art] build stamp → beat_sheet.json (55/55 filled)
- [art] wrote /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4  (1100.4s, audio: per-beat timeline (source audio preserved), drawtext: no
- [art] slots: 55/55 filled — BOPEN:VIDEO BIDEA:VIDEO BDEFS:VIDEO B0101:VIDEO B0102:VIDEO B0103:VIDEO B0104:VIDEO B0201:VIDEO B0202:VIDEO B0203:VIDEO B0301:VIDEO B0302:VIDEO B0401:VIDEO B0402:VIDEO B0403:VIDEO B0404:VIDEO B0501:VIDEO B0502:VIDEO B0503:VIDEO B0504:VIDEO B0601:VIDEO B0602:VIDEO B0603:VI
- bookend structure (Northeastern bookends; toolkit bookend_check not applicable): PASS
- loudness_check exit 0: [loud] checking 55 beats for per-beat silence … | [loud] PASS  -24.53 LUFS  tp=-2.80 dBTP
- master /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-key-terms-data-validation/exports/landscape/claude-liam-lecture-key-terms-data-validation.mp4: 3840x2160 at 24/1, 1100.38 s (18.3 min); sum of audio 1099.20 s; difference +1.17 s; 72 MB
- stages done: card, capture, review, final, checks
