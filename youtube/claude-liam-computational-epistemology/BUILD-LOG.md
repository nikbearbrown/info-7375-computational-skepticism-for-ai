# BUILD-LOG — claude-liam-computational-epistemology

## 2026-07-21 — authored (Cowork session, deep-explainer test build #1)

- Reel authored as the FIRST test of the new `deep-explainer` skill
  (`brutalist-art/skills/make/deep-explainer/`). Source: Bear's
  "Computational Epistemology" research doc (see SOURCES.md).
- Plan: 40 beats total — B00 cold open + 35 body beats across six acts +
  the standard your-turn closing block (B37 verdict / B38 your-turn /
  B39 title outro). Estimated ~8.7 min at ~2.9 w/s — inside the 5–10 band;
  audio lock will give the real number.
- Lane histogram (body): vox 8 (22.9%) · manim 11 · remotion 10 · card 6 ·
  ask micro-beat 1 (exempt). Quota check PASSES (15–30% band).
- Vox runs: R1 = B14→B15 (ledger reveal, 2 beats), R2 = B27→B28→B29
  (Descartes → synthetic grid → Hume, 3 beats). Handoff blocks authored at
  plan time per reference/continuity.md. All other lane boundaries are cuts.
- Channel claude-liam (Kokoro am_onyx, free). Greeting: "Yassou, Liam"
  (Greek — chosen for the subject; not repeated within any batch this reel
  joins). IN-FOR-BEAR law satisfied in B00 and B39.
- DOUBLE-CHECK decisions logged in SOURCES.md (utility-belt cut as datable;
  no unsourced numbers on screen; 90/60 labeled illustrative).

## 2026-07-21 (later) — audio locked in Cowork session (free pipeline)

- HUMAN NOTE (logged first): Bear, in-session — "generate the audio and
  everything it can in the Liam persona while I fill the shopping list."
  Treated as the GATE P signature for the Kokoro (free) pass; no ElevenLabs
  anywhere. Any narration change from the still-open FACTCHECK rows
  regenerates only the affected beats (`--only`).
- Audio: all 40 beats via runtime's `generate_audio_kokoro.py` (am_onyx),
  model files staged from the toolkit's own `runtime/models/kokoro/`.
  Locked total **8:19** (498.8s) — inside the 5–10 band. `mp3/timings.json`
  + `actual_duration_s` written back; durations are ground truth.
- Gate D2: `SHOPPING.md` written from the LOCKED windows — 8 stills
  (6 entries; B14 serves R1's two beats, B22 is two layers). Three tier-3
  rights checks escalate to Bear (Gettier w/ authored fallback, Descartes,
  Hume). No motion assets this episode.
- Captions: `claude-liam-computational-epistemology.srt` generated from
  SOURCE TEXT on measured beat windows (129 cues) — publisher law, never
  auto-transcription. `description.txt` drafted with chapter timestamps
  from the locked clock.
- Generated in the Cowork cloud container (sandbox blocks the GitHub/HF
  model mirrors; the toolkit's local model files were staged instead —
  same files, same engine, byte-identical interface).

## 2026-07-21 (later still) — pass-1 prep (Cowork session)

- HUMAN NOTE (logged first): Bear — "I shop while everything else gets
  built and second pass adds in after I gather media; shopping list needs
  MUCH more detail with prompts and links." Process confirmed: one Claude
  Code paste per pass; the human runs no scripts.
- SHOPPING.md rewritten (v2): full generation prompts, real-archive search
  links, per-slot resolution floors from the camera plans, sidecar rules,
  the Gettier fallback chain (photo → 1963 paper page → re-typeset DOCUMENT
  plate).
- Committed for Gate F / code beats: SOURCE.md (the primary source doc, on
  disk at last — factcheck verifies against it) and code/ (gettier_check.py,
  reliabilist_verifier.py, consensus.py — verbatim from source; B10/B18/B24
  read these files).
- Pass 1 (Claude Code, machine-side, free): factcheck close-out → scenes.py
  (11 Manim scenes) + SHOTLIST.md + PROMPTS.md → art run → slate previz +
  QC. Pass 2 after pantry lands: intake → focus → rerun → QC → final.

## 2026-07-21 — GATE F closed + Pass 1 machine build (Claude Code session)

- HUMAN NOTE (logged first): standing rule #1 — this note precedes all actions.
- **GATE F CLOSED:** all 20 FACTCHECK.md rows verified against SOURCE.md;
  zero narration changes required; no audio regeneration needed.
- **scenes.py authored:** 11 Manim Scene classes, one per Manim-lane beat
  (B06_JTBStack · B08_TwoRails · B11_GettierCoefficient · B12_AxesApart ·
  B17_CalibrationGap · B20_Regress · B23_OneWitness · B25_LatentConfounder ·
  B31_ProvenanceCap · B33_CredenceDial · B35_Surprise). Claude palette
  (CREAM #F2F0E9, INK #3D3929, ACCENT #D97757). Durations read from
  timings.json. 90/60 pair in B17 labeled illustrative per DOUBLE-CHECK log.
- **beat_sheet.json restructured (critical):** `remotion` field moved from
  top-level beat siblings INTO `beat.shot.remotion` for all 21 Remotion beats —
  this is required for `remotion_scenes.py` which reads `beat["shot"]["remotion"]`.
  Old structure would have caused all Remotion beats to silently skip.
- **Pattern reconciliation (all 21 Remotion beats):**
  - `ClaudeComposerAsk` → direct (B00, B09, B38)
  - `ClaudeVerdictArtifact` → direct (B37)
  - `ClaudeTitleOutro` → direct (B39)
  - `SegmentCard` (unregistered) → `SlateCard` with {headline, eyebrow, topic}
    (B01, B05, B13, B19, B26, B32)
  - `deckPatterns/scale` (schema mismatch) → `SlateCard` pass-1 slate (B03)
  - `deckPatterns/divergence` → `DivergentFates` with full {data: FatesData}
    (B04, B16)
  - `deckPatterns/branch` → `BinaryBranch` with full {data: BranchData} (B34)
  - `deckPatterns/threshold` (unregistered) → `SlateCard` pass-1 slate (B36)
  - `illustrations/LayerStack` → `ClaudeScienceLayerStack` with {sparkLine,
    layers, caption} (B21; 1280×720 composition)
  - `illustrations/SourceFlow` → `ClaudeScienceSourceFlow` with {sparkLine,
    sourceLabel, feeds, destApp, destTitle, arcCaption, settleLine} (B30; 1280×720)
  - `code-block` → `ClaudeCodeBeat` with embedded code string; NOT file paths —
    gettier_check.py verbatim in B10, reliabilist_verifier.py in B18,
    consensus.py in B24.
- **SHOTLIST.md + PROMPTS.md written:** full work order and pantry prompts.
- **art run queued:** remotion_scenes.py renders all 21 Remotion beats;
  Manim renders all 11 scenes via scenes.py; 8 vox slots remain PANTRY.

## 2026-07-21 — Gate D1 closed + Visual QC (Claude Code session, continued)

- **Gate D1 CLOSED:** Pass 1 machine build complete. All 21 Remotion beats and
  all 11 Manim scenes rendered. Review cut compiled at 498.8s (8:19),
  32/40 beats filled. The 8 PANTRY slots render as expected slates.
- **Visual QC (9-point rubric):** 82 frames sampled. Four MAJOR defects found
  and fixed:
  1. B00/B09/B38 — `segment` prop missing from `ClaudeComposerAsk` beats;
     default "Photoelectric Effect" was showing as the large serif header.
     Fixed: added `segment` to each beat's props (Computational Epistemology /
     Gettier Check / Your Turn). Re-rendered all three.
  2. B37 — `ClaudeVerdictArtifact` props used wrong field name (`title` instead
     of `artifactTitle`); `artifactHeading` was absent. Fixed: renamed field;
     added `artifactHeading: "Know how you know"`. Re-rendered.
  - All four fixes verified via targeted frame grabs. Zero BLOCKER/MAJOR
    defects remain. Full rubric audit: `_qc/REPORT.md`.
- **Review cut path:** `mp4/claude-liam-computational-epistemology-slate.mp4`
  (498.8s — 8:19 · 1920×1080 · review mode labels visible).
- **Slot ledger (32/40):** B00:VIDEO · B01:VIDEO · B02:SLATE · B03:VIDEO(slate)
  · B04:VIDEO · B05:VIDEO · B06:MANIM · B07:SLATE · B08:MANIM · B09:VIDEO ·
  B10:VIDEO · B11:MANIM · B12:MANIM · B13:VIDEO · B14:SLATE · B15:SLATE ·
  B16:VIDEO · B17:MANIM · B18:VIDEO · B19:VIDEO · B20:MANIM · B21:VIDEO ·
  B22:SLATE · B23:MANIM · B24:VIDEO · B25:MANIM · B26:VIDEO · B27:SLATE ·
  B28:SLATE · B29:SLATE · B30:VIDEO · B31:MANIM · B32:VIDEO · B33:MANIM ·
  B34:VIDEO · B35:MANIM · B36:VIDEO(slate) · B37:VIDEO · B38:VIDEO · B39:VIDEO

## Gate status

- [x] GATE F — CLOSED 2026-07-21; all 20 rows verified; zero narration edits.
- [x] GATE P — signed by Bear in-session 2026-07-21 (Kokoro/Liam, free).
- [x] Audio lock — 8:19; timings.json is the clock.
- [x] Gate D2 SHOPPING.md — written from locked durations; Bear filling.
- [x] Gate D1 previz — CLOSED 2026-07-21; all 21 Remotion + 11 Manim rendered;
      review cut at 498.8s; zero BLOCKER/MAJOR after QC fixes.
- [ ] Pantry fill / pass 2 / final — pending (Bear shopping).

## MISSING / open questions for Bear

- MISSING: `ClaudeScienceLayerStack` (B21) and `ClaudeScienceSourceFlow` (B30)
  are 1280×720 compositions (registered at 1280×720 in Root.tsx). Verify they
  scale acceptably in the 1920×1080 timeline; if not, flag in QC and note here.
- MISSING: `Threshold` composition not registered in Root.tsx; B36 uses SlateCard
  as pass-1 placeholder. If the threshold-gate visual is important for the final
  cut, author a reel-local Remotion scene or request the composition for Root.tsx.
- Tier-3 portrait rights checks (Descartes, Hume, Gettier) escalate to
  human per shopping-list law; B07 has an authored fallback (1963 paper
  title plate) if no cleared Gettier photograph exists.

--- 2026-07-21 topic-prop fix + recompile ---
[fix] Patched missing topic props on B09 (COMPUTATIONAL EPISTEMOLOGY) and B38 (COMPUTATIONAL EPISTEMOLOGY)
[remotion] Re-rendered B09, B38 --force with corrected topic annotations
[final] art final --allow-slates → claude-liam-computational-epistemology.mp4 (498.8s)
[qc] PASS — B09 top-left reads "COMPUTATIONAL EPISTEMOLOGY"; B38 confirmed clean

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json content trimmed
  Method: em-dash rule → take first clause; sentence rule → first sentence; fallback → first 11 words
  B01 (SlateCard): verdict card → headline compressed to ≤12w: 'The Flood'
  B02 (SlateCard): verdict card → headline compressed to ≤12w: 'Seminar room — 19th-century lecture hall'
  B03 (SlateCard): verdict card → headline compressed to ≤12w: 'One Checker vs. The Flood'
  B05 (SlateCard): verdict card → headline compressed to ≤12w: 'Lucky Truths'
  B07 (SlateCard): verdict card → headline compressed to ≤12w: 'Edmund Gettier · 1963'
  B13 (SlateCard): verdict card → headline compressed to ≤12w: 'Show Your Work'
  B14 (SlateCard): verdict card → headline compressed to ≤12w: 'The ledger — tight on ink entries'
  B15 (SlateCard): verdict card → headline compressed to ≤12w: 'The ledger — wide reveal'
  B19 (SlateCard): verdict card → headline compressed to ≤12w: 'The Web and the Bedrock'
  B22 (SlateCard): verdict card → headline compressed to ≤12w: 'The string wall — conspiracy board'
  B26 (SlateCard): verdict card → headline compressed to ≤12w: 'The Demon Ships'
  B27 (SlateCard): verdict card → headline compressed to ≤12w: 'René Descartes portrait'
  B28 (SlateCard): verdict card → headline compressed to ≤12w: 'Synthetic face grid — the demon ships'
  B29 (SlateCard): verdict card → headline compressed to ≤12w: 'David Hume portrait'
  B32 (SlateCard): verdict card → headline compressed to ≤12w: 'Belief as a Number'
  B36 (SlateCard): verdict card → headline compressed to ≤12w: 'Threshold → Abstain'
  NOTE: some beats have stale renders — delete and re-run art run before final cut
  type_check.py §8.5: PASS after trimming
  PASS 1 complete (JSON updated; recompile when audio is ready)
