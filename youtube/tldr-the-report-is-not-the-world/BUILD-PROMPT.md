# BUILD-PROMPT — tldr-the-report-is-not-the-world

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 8's Case #1 (*Agents of Chaos*) from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-08-agentic-ai.md`.

**Why.** An agent's completion report is a reading of what its own tools can see. The film shows it on two ledgers — the agent's and the world's — and lands the chapter's false-success catch: the report is one datum, independent observation of the world is the other.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-the-report-is-not-the-world
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (WIPES the audio lock)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_audio.py                                          # actual_duration_s, card durations, B00/B01 cues on the spoken clauses
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

After ANY re-run of `make_sheet.py`, run `lock_audio.py` again (the sheet is rewritten without the audio fields). Do not re-pad BOUT twice. Changing a scene: delete `$R/manim/<B>.mp4` and `rm -rf "$R/media/videos/scenes/2160p24/partial_movie_files"` (no globs in the same rm).

Then LOOK at frames: B00/B01 at ~50% and ~90% (lines land on their clauses), B02 at ~90% (the corrected "according to the world?" on screen), B16 at 50% (window empty, server still holding the email). Fix at the source, never by hand-timing. To stage (Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory (`reset()` moves every object from before to after). Course credit spoken in B00. OUTRO-LOCK. Chapter `[verify]` items stay out.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
