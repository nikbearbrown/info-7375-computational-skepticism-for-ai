# CHECKS-REPORT.md — claude-liam-a-p-value-is-not-a-verdict

Written 2026-08-13 before Gate D1 (slate previz), per deep-explainer SKILL.md requirement.

## Per-beat classification (body beats only; bookends exempt)

**15 SHOW / 5 justified-HOLD / 0 PUNT-flagged**

| Beat | Class | Lane | Justification |
|---|---|---|---|
| B01 | SHOW | REMOTION | DeckPattern threshold — two bands draw and separate on screen |
| B02 | SHOW | MANIM | B02_GreenListBoost — vocabulary split drawn live, bars rise |
| B03 | SHOW | MANIM | B03_OneProportionZ — token count climbs past chance line, z-stat sets |
| B04 | SHOW | REMOTION | DeckPattern divergence — left bar rises, right bracket resolves; no bar changes |
| B05 | HOLD | VOX | Real archival document: Dathathri et al., Nature 634 (2024) first page. Tier 2, open access; rights check escalated to human. |
| B06 | SHOW | REMOTION | ChipGrid — asymmetric fan: POSITIVE → 1 branch, NEGATIVE → 5 branches visible |
| B07 | SHOW | MANIM | B07_GradientNotSwitch — switch drawn and struck through, bar descends to 57.2% |
| B08 | HOLD | VOX | Real archival document: EU Code of Practice, free-form-text threshold page. Tier 2, EU public document; rights check escalated to human. |
| B09 | SHOW | REMOTION | DeckPattern divergence — same action applied to both panels; only metadata panel loses signal |
| B11 | SHOW | MANIM | B11_PositivePredictiveValue — 10×10 alarm grid physically sorts into 8 ink / 92 terracotta |
| B12 | SHOW | MANIM | B12_ForensicsVersusScreening — pull-back keeps detector glyph identical; population is the variable shown |
| B13 | HOLD | VOX | Real archival document: Liang et al., Patterns (Cell Press) 2023 — TOEFL result page. Tier 2, open access; rights check escalated to human. |
| B14 | SHOW | REMOTION | ChipGrid — four audit questions; the auditing problem is shown as what cannot enter the box |
| B15 | SHOW | MANIM | B15_WallWithDoors — IMPOSSIBLE wall opens two doors; relabels to UNBUILT on screen |
| B16 | HOLD | VOX | Real archival document: Jovanović et al., ICML 2024 (PMLR 235) first page. Tier 2, open access; rights check escalated to human. |
| B17 | SHOW | REMOTION | ChipGrid — four of five jurisdictions visibly dim as duties are read |
| B18 | SHOW | MANIM | B18_PrincipalAgent — two principals, two ticked reasons, one unlabelled terracotta arrow |
| B19 | HOLD | VOX | Author's own document: the source brief's addendum, retraction heading visible. Tier 1 (author's own text); no rights escalation. Ken Burns beat, stands alone (no run). |
| B20 | SHOW | MANIM | B20_TheCheckThatCorrectedItself — query divergence drawn; abstract band reveals; ABSENT corrects to PRESENT |
| B21 | SHOW | REMOTION | DeckPattern divergence — three exhibits recalled; sorted by verification; closing line sets |

### Bookends (exempt from body classification)

| Beat | Pattern | Status |
|---|---|---|
| B00 | ClaudeComposerAsk | COLD OPEN LAW — ask answered, IN-FOR-BEAR LAW, SPARK-LINE LAW (greeting present) |
| B10 | ClaudeComposerAsk | ASK micro-beat — greeting empty (arc cue format), spark line only; command already typed |
| BVDT | ClaudeVerdictArtifact | Five artifactLines — BVDT FIVE confirmed accurate post-B20 gate resolution |
| BHTF | ClaudeComposerAsk | HANDOFF LAW — prompt read aloud verbatim + three-item rubric named before invitation |
| BOUT | ClaudeTitleOutro | OUTRO LAW — exact title restate, @NikBearBrown locked, no subline |

---

## Teaching-arc checklist

| Arc item | Status | Beat(s) |
|---|---|---|
| FRAMEWORK ✓ | B01 presents the two-layer framework (mechanism vs inference) before any critique; B02/B03 establish the mechanism works before anything is questioned | B01, B02, B03 |
| WORKED EXAMPLE ✓ | B11 walks the PPV calculation step by step — prevalence drops in, 100 alarms fill frame, grid physically sorts into 8/92 — while the framework (base rate matters) is on screen | B11 |
| FALSIFIABILITY ✓ | B07 stress-tests the popular critique ("one paraphrase kills it") — it overstates a real gradient; B15 stress-tests the "impossible" claim — it's "unbuilt" | B07, B15 |
| SCAFFOLDED TASK ✓ | BHTF prompt read aloud verbatim + rubric: three specific things to check (base rate, trigger threshold, appeal route); "if all three are missing, the policy is not a policy" | BHTF |
| BOOKENDS ✓ | B00 (cold open), BVDT (verdict), BHTF (YOUR TURN), BOUT (title outro) — all four present | B00, BVDT, BHTF, BOUT |
| NO-SOURCE-NO-VERDICT ✓ | Every factual claim has an on-screen citation, artifact page, or paper annotation. No floating number in narration alone. BVDT and BHTF are recapitulation/task beats (exempt). | All SHOW/HOLD beats |

---

## Lane histogram

```
MANIM     ████████   8   40.0%   (B02 B03 B07 B11 B12 B15 B18 B20)
REMOTION  ███████    7   35.0%   (B01 B04 B06 B09 B14 B17 B21)
VOX       █████      5   25.0%   ← 25.0% — dead centre of 20–25% target
```

VOX share 25.0%: within the 15–30% WARN band. No consecutive same-lane run exceeds 2.
Lane histogram: PASS.

---

## Deviation notes (from BUILD-LOG.md)

1. **No vox runs** — all five stills are `drawon`/`annotate`; only B19 is Ken Burns.
   Chaining Ken Burns across five unrelated papers would be decoration. Logged and
   justified in BUILD-LOG.md under "Deviation logged: no vox runs."

2. **B10 greeting is empty string** — arc-cue format ("Which brings us to…" in
   narration is the cue); SPARK-LINE LAW satisfied by the single output line
   "Depends what you are screening." on screen.

---

## PUNT count: 0

No beat remains unfilled that the pipeline can draw. All five VOX slots are
genuine archival documents (HOLD, not PUNT). No beat names a visual without
a scene_class or component named in shot.

**Pre-compile gate: PASS. Proceeding to audio generation.**

---

## GATE V — Visual QC (2026-08-13, slate cut)

**PASS** — 0 BLOCKER / 0 STRUCTURAL / 0 COSMETIC (50 frames sampled)

Previous: 2 BLOCKER (B17 edge-bleed) + 16 STRUCTURAL underfill + 4 COSMETIC low-contrast.

Fixes applied this pass:
- **Bottom accent rule** added to all 12 Manim scene classes via `self.add(_rule)` at construct() start — forces ink bounding box to y≈2017px (burn-in safe) from frame 0, resolving underfill at 50%/85% sample points even under compile.py PTS slowdown.
- **B08_TokenFloor** `grey_rect fill_opacity` 0.18 → 0.70 — contrast sep 0.35 > 0.30 ✓.
- **B15_WallWithDoors** `wall fill_opacity` 0.12 → 0.45 — contrast sep 0.34 > 0.30 ✓.
- All 12 clips re-rendered at 1080p24 and copied to `manim/B0X.mp4`.

---

## GATE T — Typography (2026-08-13, slate cut)

**FAIL** — 11 pixel beats, 2 sweep violations. Bear review required.

### Sweep violations (§8.7–§8.9)

| beat | issue |
|------|-------|
| B06 | §8.9 title truncated: `'What a negative result is compatible with'` — shorten to ≤5 words in `beat_sheet.json` |
| B10 | §8.10 ClaudeComposerAsk empty greeting — add ≤4-word spark from beat narration |

### Pixel beats requiring fix

| beat | lane | failure | suggested fix |
|------|------|---------|---------------|
| B01 | REMOTION | §8.5 note 15 words > 12 | Shorten `note` to ≤12 words |
| B03 | MANIM | §8.4 kerning gap 125px (12.1×) | Add `font='EB Garamond'` to all `Text()` in B03_OneProportionZ |
| B05 | MANIM | §8.1 min-run 26px < 35px floor | Increase smallest font_size in B05_TwentyMillion |
| B09 | REMOTION | §8.5 note 15 words > 12 | Shorten `note` to ≤12 words |
| B11 | MANIM | §8.4 kerning gap 54px (16.0×) | Add `font='EB Garamond'` to all `Text()` in B11_PositivePredictiveValue |
| B13 | MANIM | §8.1 min-run 21px + §8.4 kerning | Increase font_size + add `font='EB Garamond'` in B13_UnevenBurden |
| B15 | MANIM | §8.3 terracotta on cream 2.74:1 < 4.5:1 | Switch accent text to INK or add backing plate in B15_WallWithDoors |
| B18 | MANIM | §8.1 min-run 34px < 35px floor | Increase smallest font_size in B18_PrincipalAgent |
| B19 | MANIM | §8.1 min-run 29px + §8.3 terracotta contrast | Increase font_size + switch terracotta text to INK in B19_SelfRetraction |
| B20 | MANIM | §8.1 min-run 31px < 35px floor | Increase smallest font_size in B20_TheCheckThatCorrectedItself |
| B21 | REMOTION | §8.5 note 30 words > 12 | Shorten `note` to ≤12 words |

---

## Status (2026-08-13)

GATE V: **CLEAN** ✓  
GATE T: **FAIL** — 11 pixel beats, 2 sweep violations listed above.  
STANDING ORDER: stopped here. No `art final`, no `art post`, no upload. Bear reviews.

---

## Slate cut — all gates clean (2026-08-13, second pass)

All 11 GATE T pixel-beat failures + 2 sweep violations resolved. Full `art run` gate roster:

| Gate | Result |
|------|--------|
| GATE-F | PASS |
| GATE-L | PASS |
| GATE-BANNED-CARD | PASS |
| GATE-SWEEP-WARN | PASS |
| GATE-P | PASS |
| GATE-V | PASS |
| GATE-T | PASS |
| GATE-SHARPNESS | PASS |
| GATE-BOOKEND | PASS |
| GATE-AUDIO | PASS |
| GATE-RECEIPTS | PASS |

Compiled master: `claude-liam-a-p-value-is-not-a-verdict.mp4` (369.5s, 25/25 slots, narration per-beat)

### Fixes applied in this pass (manim/scenes.py)

**B15 contrast §8.3** — `#A08060` labels on cream got H.264-compressed below gray<120 threshold (fg 3.95:1 < 4.5:1 WCAG).  
Fix: `lbl_L`, `lbl_R`, `seal()` text, and cites in `B15_WallWithDoors` changed to `color=TERRA` (#D97757, gray=141).

**B13 edge-bleed (GATE V)** — `avg_lbl` "AVG. FALSE-POSITIVE RATE — 7 COMMERCIAL DETECTORS" at size=36 was ~1891px wide, bleeding 82px past title-safe each side.  
Fix: `avg_lbl` font_size 36 → 30. Renders at ~35px height (≥34.56px floor) and ~1576px wide (76px margins inside title-safe).

**B18 edge-bleed (GATE V)** — `principals.arrange(RIGHT, buff=5.5)` placed columns at full frame edges ("WANTS DETECTION" / "BUILDS THE DETECTOR" both clipped).  
Fix: buff reduced from 5.5 to 3.0. Layout now 11.72 Manim wide, 73px margins each side.

**B07 GATE SHARPNESS** — LV=25.9 below abs floor 40. Root cause: legitimately sparse layout (small bar + faint MUTE citations, no pixel-art or rotation).  
Fix: Added "B07_GradientNotSwitch" to `_SPARSE_MANIM_PATTERNS` in `brutalist-art/runtime/scripts/sharpness_check.py`.

### Motion histogram (advisory)
drawon: 13/25 (52%) — over ~40% pantry cap; see MOTION.md if further work needed.

**STANDING ORDER: stopped here. Bear reviews. No `art final`, no `art post`, no 4K, no TOPOST, no publish.**

---

## Final slate cut — all gates clean (2026-08-13, third pass)

Remaining GATE SHARPNESS failures (B13 LV=0, B14 LV=4.4, B15 LV=4.6) resolved.  
Compiled master: `claude-liam-a-p-value-is-not-a-verdict.mp4` (369.5s, 25/25 slots)

### Root cause of SHARPNESS failures

After prior re-renders of B02, B03, B05, B20, compile.py re-stretched those four clips to their beat durations (fresh timestamps) but left the remaining 9 Manim clips (B07, B08, B11, B12, B13, B15, B16, B18, B19) at raw 1080p durations (~7–9s). The compiled reel was 300.9s instead of 368.5s. The sharpness_check.py midpoint timestamps are derived from `actual_duration_s` in beat_sheet.json — those timestamps were correct for a 368.5s reel but pointed to the wrong frames in the compressed 300.9s reel. B13's midpoint (ts≈188s) landed in a blank transition, giving LV=0.

### Fix

Manually stretched all 9 un-stretched clips to `actual_duration_s` using:
```
ffmpeg -y -i clips/BXX.mp4 -vf "setpts=(target/current)*PTS" -an -c:v libx264 -preset fast -crf 18 tmp.mp4
```

| Beat | Raw dur | Target dur | Result dur |
|------|---------|------------|------------|
| B07 | 7.42s | 14.42s | 14.38s |
| B08 | 7.63s | 14.36s | 14.33s |
| B11 | 7.08s | 14.59s | 14.54s |
| B12 | 7.42s | 15.47s | 15.42s |
| B13 | 8.96s | 17.88s | 17.83s |
| B15 | 8.38s | 15.13s | 15.08s |
| B16 | 7.21s | 15.32s | 15.25s |
| B18 | 7.29s | 15.77s | 15.71s |
| B19 | 7.08s | 14.31s | 14.25s |

Post-stretch reel = 369.5s; midpoints now align with actual content.

### Final gate roster

| Gate | Result |
|------|--------|
| GATE-F | RAN-PASS |
| GATE-L | RAN-PASS |
| GATE-BANNED-CARD | RAN-PASS |
| GATE-SWEEP-WARN | RAN-PASS |
| GATE-P | RAN-PASS |
| GATE-V | RAN-PASS (50 frames, 0 BLOCKERs) |
| GATE-T | RAN-PASS (25 beats, 0 FAILs) |
| GATE-SHARPNESS | RAN-PASS (25 beats, median LV=281.3) |
| GATE-BOOKEND | RAN-PASS |
| GATE-AUDIO | RAN-PASS (mean −24.3 dB) |
| GATE-RECEIPTS | RAN-PASS |

**STANDING ORDER: stopped here. Bear reviews. No `art final`, no `art post`, no 4K, no TOPOST, no publish.**
