# BUILD-PROMPT — Bias: Where It Enters and Who Is Responsible (Lecture 6)

**What.** The paste-ready instruction that rebuilds this film from its folder.
**Why.** A reel without its build prompt is unfinished.
**Found.** Everything is free and local; the order that matters is evidence, audio, opening card, `art run`.

Run from `/Users/bear/Documents/CoWork/bear-textbooks/books/`:

```
R=info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-bias-where-it-enters
python3 $R/evidence/evidence.py && python3 $R/embed_evidence.py        # worked numbers, embedded in scenes.py for Gate A
python3 $R/capture.py                                                  # only to refresh public captures (no sign-in); re-check FACTCHECK.md
python3 $R/make_sheet.py                                               # beat_sheet.json + SHOTLIST.md (keeps measured audio when narration is unchanged)
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R      # or --only <BIDs>
python3 $R/pad_audio.py && python3 $R/make_sheet.py                    # BIDEA +0.8 s lead, BVDT +0.5 s lead, BOUT +1.0 s tail
python3 brutalist.art/skills/make/lecture/templates/title-slide-16x9/build.py --out $PWD/$R/opening --sheet $PWD/$R/beat_sheet.json --width 3840
cp $R/opening/example-opening-*.mp4 $R/media/BOPEN.mp4
./brutalist.art/art run $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 $R/whisper_check.py && python3 $R/build_srt.py
```

Never stage, publish, commit or push from here.
