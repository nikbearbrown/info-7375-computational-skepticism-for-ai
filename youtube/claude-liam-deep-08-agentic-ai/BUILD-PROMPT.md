# BUILD-PROMPT — claude-liam-deep-08-agentic-ai · "You Broke My Toy"

Paste-ready end-to-end build prompt. Run this in **Claude Code, from `books/`**, on the
Mac (Manim + Remotion + Chrome + QC gates live there). The reel is a **deep-explainer**
and most of the phase-gated work is already done — this prompt drives it from *audio-locked*
to *final cut*. Do not re-plan, do not re-run audio.

---

## STATE (already complete — do not redo)
- **PLAN gate:** signed (7-act cut, 32 beats). See `PLAN.md`.
- **FACTCHECK gate:** held — study genericized in the body, named + scope-caveated at A7SRC. See `FACTCHECK.md`.
- **GATE P:** passed — `PEDAGOGY.md` VERDICT: PASS.
- **Audio:** GENERATED and LOCKED. Kokoro `am_onyx` (free), 32/32 beats in `mp3/`,
  `mp3/timings.json` written, `actual_duration_s` stamped into `beat_sheet.json`.
  Total ~8m25s. **The measured audio is the master clock — never hand-tune timings.**
  (Two silent ASK micro-beats A3K/A7K carry 1.4s anullsrc holds by design.)
- **SHOPPING.md:** written (Gate D2), duration-locked, 6 Tier-1 vox stills.

## THE REEL
`computational-skepticism-for-ai/youtube/claude-liam-deep-08-agentic-ai`

## WHAT'S LEFT (build order)

1. **Word clock (align).** Run `align.py` over the locked `mp3/` so on-word reveals in the
   Remotion/Manim beats key correctly. Audio is the clock; this only writes the word grid.

2. **Author `scenes.py` (Manim, 7 beats).** `run.sh` REFUSES without a per-reel `scenes.py`
   (the shared `animated_graphics.py` holds only the electoral-college fixture). Write one
   `Scene` per Manim beat, using `shot.manim.spec` in the beat sheet:
   - A2M prediction↔consequence split · A3M autonomy–competence ladder gap ·
     A4M instruction/data token conflation (prompt injection) · A4M2 cross-channel spoof ·
     A5M cascading hallucination (equation tangent P(error)=1−(1−p)^n) ·
     A6M patch-ships-the-failure · A7M the false-success catch (gate + independent world check).
   - Claude skin: cream `#FAF9F5`, warm ink `#3D3929`, terracotta `#D97757` as the ONE accent, EB Garamond.

3. **Remotion beats (19).** `python3 brutalist-art/runtime/scripts/remotion_scenes.py <reel>`
   — renders each beat carrying `shot.remotion.pattern` to `media/<BID>.mp4`. Bookends
   (B00 ClaudeComposerAsk, BVDT ClaudeVerdictArtifact, BOUT ClaudeTitleOutro), cards, and the
   C2/C3 rhetorical patterns. Author the MISSING `anim.json` classification for the DeckPattern
   beats (A4R, A6R, A7R2) first. **Render foreground, `--concurrency=1`, via the script only.**

4. **Manim render + slot + recompile.** `./brutalist-art/art run <reel>` — Gate A (pre-flight)
   + Gate B (post-render pixel audit) are wired as hard gates; renders pending `scenes.py`
   scenes to `manim/<BID>.mp4`. Needs the paperwork set (`FACTCHECK.md` ✓ · add `SHOTLIST.md`
   + `PROMPTS.md`, or `ART_FACTS=0` for a previz-only pass).

5. **Gate D1 previz.** `./brutalist-art/art run <reel>` then review the compiled cut:
   vox beats show as slates (id + narration + pipeline pointer), Manim/Remotion render for real,
   real audio. **Watch it end to end for pacing.** Verify by LOOKING at a frame + `qc-sheet.png`.

6. **Pantry fill (6 vox stills).** Work `SHOPPING.md`. All Tier 1 — AI-generate or stock, no
   rights escalation. Drop each into `pantry/<BID>.png`; the `pantry` command intakes → treats
   (desaturate ~80%, contrast ~1.15, cream stage `#F2F0E9`, film grain, warm-ink vignette,
   terracotta as the one accent) → renames to `media/<BID>.png`; set `shot.focus`. Rerun compile
   — only changed slots recompile. The R1 run (A1V1→A1V2→A1V3) is the one continuous zoom-out:
   author as one plate at three crops (or three plates pinned to the handoff frames).

7. **Review cut → VISUAL QC LAW pass → final.** `./brutalist-art/art final <reel>` →
   `<slug>-cut.mp4` (clean 4K master, no review label). Closing block is the `your-turn`
   standard (verdict recap → YOUR TURN prompt read in full → title re-read). **Never publish —
   public is a manual Studio flip.**

## STANDING RULES (bind every step)
Standing rules #1–#4 in `brutalist-art/EXAMPLES-CAMPAIGN.md`: log human feedback first;
verify renders by LOOKING at a frame + `qc-sheet.png`; render Remotion only via
`remotion_scenes.py`, foreground; match Remotion props to each component's zod schema.
Audio-first; one kebab-case folder; `brutalist-art/` is self-contained (never reach to
`../vox/` or absolute `books/…` paths — log `MISSING:` and stop that thread).

## ONE-LINE KICKOFF
> Read `computational-skepticism-for-ai/youtube/claude-liam-deep-08-agentic-ai/BUILD-PROMPT.md` and continue the build from step 1 (align). Audio and gates are done — do not re-plan or re-run audio.
