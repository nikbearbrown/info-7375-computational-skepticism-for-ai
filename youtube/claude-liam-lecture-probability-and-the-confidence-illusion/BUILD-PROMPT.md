# BUILD-PROMPT — Probability and the Confidence Illusion

**What.** The paste-ready instruction that rebuilds this film from its folder.
**Why.** A reel without its build prompt is unfinished.
**Found.** Everything is free and local; audio comes before the opening card, the opening card before `art run`.

Run from `/Users/bear/Documents/CoWork/bear-textbooks/books/`:

```
R=info-7375-computational-skepticism-for-ai/youtube/claude-liam-lecture-probability-and-the-confidence-illusion
python3 $R/evidence/evidence.py > $R/evidence/evidence.stdout.txt     # seeded; recomputes every worked number
python3 $R/evidence/bayes_run.py > $R/evidence/bayes_run.stdout.txt
python3 $R/make_sheet.py                                               # beat_sheet.json + SHOTLIST.md (keeps audio when narration is unchanged)
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R      # or --only <BIDs>
python3 $R/pad_audio.py && python3 $R/make_sheet.py                    # real lead/tail silences
python3 $R/whisper_check.py                                            # Hola, BOPEN order, names, numbers
python3 brutalist.art/skills/make/lecture/templates/title-slide-16x9/build.py --out $PWD/$R/opening --sheet $PWD/$R/beat_sheet.json --width 3840
cp $R/opening/example-opening-*.mp4 $R/media/BOPEN.mp4
./brutalist.art/art run $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
python3 brutalist.art/runtime/scripts/bookend_check.py $R
```

Never stage or publish from here.
