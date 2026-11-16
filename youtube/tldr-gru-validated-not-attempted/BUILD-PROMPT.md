# BUILD-PROMPT — tldr-gru-validated-not-attempted

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) explaining Gru's phase gates, from the Gru persona Bear pasted on 2026-09-24. Section S1 of `../tldr-sections-gru-persona.md`.

**Why.** A design with words in every section looks finished. Gru's rule — no valid output from the next phase until this one is validated, not attempted — is what makes a component's "why" survive to 2 a.m. The film shows a vague need as a fog any trace can land in, and the gate collapsing it.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-gru-validated-not-attempted
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # durations from audio, B00/B01 cues on the spoken clauses
find $R/manim $R/media -name "*.mp4" -delete
./brutalist.art/art run   $R --height 2160                        # background it: Manim 4K + Gate B + Remotion + review compile + Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T + clean master
```

Re-run `lock_cards.py` after ANY re-run of `make_sheet.py`. To stage (Bear's word only): `python3 brutalist.art/runtime/scripts/stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
