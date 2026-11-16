# BUILD-LOG — claude-liam-pick-your-pebble

**Status:** GATE P — awaiting Bear review of beat sheet + narration  
**Date:** 2026-07-30  
**Channel:** claude-liam (@NikBearBrown, Kokoro am_onyx, free)  
**Playlist:** Doubt It When It Looks Right — The Agentic Casebook (Video 1)

---

## What this reel teaches

ONE thing: how to pick the agentic system you will red-team, and write its Dossier.
Source: `books/computational-skepticism-for-ai/assignments/agentic-casebook-red-team.md` Step 1.

Scope exclusions: prediction-lock, case-writing, lens selection, attestation — those are Videos 2–6.

---

## Beat inventory (11 beats, all pipeline-buildable)

| Beat | Act | Visual type | Scene | Status |
|------|-----|-------------|-------|--------|
| B00 | cold open | ClaudeComposerAsk | — | SLATE |
| B01 | THE FAST FILTER | FormBCard (4-up) | — | SLATE |
| B02 | FASTEST PATH TO DONE | Manim | B02_FastestPath | SLATE |
| B03 | WHY CARING HELPS | Manim | B03_HonestyFloor | SLATE |
| B04 | THE DOSSIER intro | FormACard | — | SLATE |
| B05 | THE DOSSIER · 1–3 | FormBCard (3-up) | — | SLATE |
| B06 | THE DOSSIER · 4–6 | FormBCard (3-up) | — | SLATE |
| B07 | THE ONE DISCIPLINE | Manim | B07_ArtifactVsWorld | SLATE |
| BVDT | VERDICT | ClaudeVerdictArtifact | — | SLATE |
| BHTF | YOUR TURN | ClaudeComposerAsk | — | SLATE |
| BOUT | OUTRO | ClaudeTitleOutro | — | SLATE |

**Total estimated duration:** 135s (≈ 2:15)

---

## Design decisions logged

### HARD CONSTRAINTS honored
- **4 filter criteria** (B01) and **6 Dossier bullets** (B05, B06) are FormBCard icon-reveal beats — not prose cards. ✓
- **Icons from library only** — all six icons (zap, shield-alert, lock, ruler, tag, frame, hand, target, crosshair, clipboard-list) confirmed present in `runtime/remotion/public/form-b-icons/`. ✓
- **NEVER doodle** — no DoodleScene or DoodleChart anywhere. ✓
- **PANTRY-FIRST, no gen-AI fallback** — all 11 beats are pipeline-buildable (Remotion + Manim). Zero pantry items. ✓
- **STOP AT GATE P** — no audio generated, no art run invoked. ✓

### ASK → RESULT LAW
The Manim beats (B02, B03, B07) are concept-illustration scenes, not Claude-generated outputs being demonstrated. No ASK→RESULT micro-beats are inserted before them. If Bear wants ASK→RESULT wrappers on any Manim beat, add ClaudeComposerAsk micro-beats before B02, B03, and B07 — each costs ~5s and 3-4 words.

### Register
Teardown (Feynman × MKBHD), not Pragmatist. The cb-01 sibling used Pragmatist; this reel uses Teardown per the ai-explainer default. Update metadata.register if Bear prefers Pragmatist for this series.

### Greeting
`Merhaba, Liam.` (Turkish) — cb-01 sibling used `Ciao`, so this reel differs. The slug-sum mod-10 Wagwan rule does not apply to Liam.

### Dossier split
The 6 Dossier bullets exceed FormBCard max (N=5), so they are split across two beats:
- B05 (3-up): Name / Architecture / Tool Surface
- B06 (3-up): Deployment Context / Candidate Failure Mode / Access Constraints

### IN-FOR-BEAR LAW
Honored at both ends:
- B00 narration opens: "Merhaba — this is Liam, in for Bear."
- BHTF narration closes: "Liam, in for Bear."

---

## Manim scenes to write (scenes.py)

Three scenes needed. All `white_background=True` equivalent (cream canvas), ink strokes, terracotta accent for ONE moment per scene.

### B02_FastestPath
Y-fork diagram. Two branches (DOG-FOOD IT in teal, RECONSTRUCT A PUBLIC CASE in ink) converge at terracotta circle labeled YOUR PEBBLE. Sequential draw-on animation.

### B03_HonestyFloor  
Two-zone split. ARTIFACT left (document "SUCCESS REPORT ✓"), WORLD right (folder "ACTUAL SENT FOLDER"), gap labeled "THE HONESTY FLOOR". Two animated arrows: crimson (stops at artifact) then teal (crosses to world).

### B07_ArtifactVsWorld  
Two blocks with gap. ARTIFACT left ("SUCCESS REPORT" with check, "LIES?" overlay in terracotta). Center separator labeled "THE ONE DISCIPLINE". WORLD right (magnifying glass "ACTUAL STATE"). Serif annotation: "Your hunch names the gap."

---

## Pantry shopping list

**Empty. All 11 beats are pipeline-buildable.**

| Beat | Pantry item needed | Source |
|------|-------------------|--------|
| — | none | — |

No gen-AI clips, no human-supplied media, no Higgsfield spend.

---

## Next steps (after Bear approves at GATE P)

1. Run `./brutalist-art/art keys` to validate Kokoro is live.
2. Generate audio: `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py computational-skepticism-for-ai/youtube/claude-liam-pick-your-pebble/`
3. Calibrate FormBCard cueFrames to actual MP3 durations (rough estimates in beat sheet).
4. Write `scenes.py` with B02_FastestPath, B03_HonestyFloor, B07_ArtifactVsWorld.
5. Run `./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-pick-your-pebble/` for slate previz.
6. GATE V (visual QC) — sample frames, read PNGs, check 9-point rubric.
7. GATE T (type-lock) — run `scripts/type_check.py`.
