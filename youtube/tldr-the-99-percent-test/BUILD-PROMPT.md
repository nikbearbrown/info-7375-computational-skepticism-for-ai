# BUILD-PROMPT — tldr-the-99-percent-test

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 2 §"The test that is 99% accurate" + §"Bayes' theorem" from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-02-probability-confidence.md`.

**Why.** A 99% accurate test for a 1-in-10,000 disease turns a positive into about a 1% chance. The film counts 10,000 people so the viewer can see the positives come mostly from the healthy, then names the count Bayes' theorem.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-the-99-percent-test
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
python3 - <<'PY'                                                  # card lengths = measured audio, cues scaled
import json; p="info-7375-computational-skepticism-for-ai/youtube/tldr-the-99-percent-test/beat_sheet.json"; d=json.load(open(p))
for b in d["beats"]:
    if b["beat_id"] in ("B00","B01","B03"):
        pr=b["shot"]["remotion"]["props"]; old=pr["durationSeconds"]; new=round(b["actual_duration_s"],2)
        if "cues" in pr: pr["cues"]=[round(c*new/old,2) for c in pr["cues"]]
        pr["durationSeconds"]=new
json.dump(d,open(p,"w"),indent=2,ensure_ascii=False)
PY
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
# then set BOUT actual_duration_s from ffprobe of the padded mp3 (art refuses the compile otherwise)
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Then LOOK at frames (`_qc/`, `qc-sheet.png`; the B00/B01 cards at ~50% and ~90%; B02 at ~90% with the correction on screen; B17/B18 equations at their revealed states). Fix at the source, never by hand-timing. To stage: `python3 brutalist.art/runtime/scripts/stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz` — the full-text SRT before post, always.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory (patient, rail and knob persist; the grid and the pile are built by the same helpers in every scene). Course credit spoken in B00. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
