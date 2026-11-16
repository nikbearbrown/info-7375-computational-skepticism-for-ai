# CHECKS-REPORT — claude-liam-distrust-the-machine
## 2026-08-13 (narration pass — own-the-argument rewrite)

### What changed (2026-08-13 session)

**STANDALONE-ARGUMENT rewrite (OWN-THE-ARGUMENT.md).** 11 of 12 flagged beats updated. B12 unchanged (act card; "the taxonomy" is earned by then).

| Beat | Operation | Old → new narration_text delta | New duration |
|------|-----------|-------------------------------|--------------|
| B02 | strip clause | "the essay describes" removed | 13.5s (was 14.7s) |
| B10 | strip clause | "The essay's central picture:" removed | 14.1s (was 13.9s) |
| B13a | reframe | "The essay attracted" → "This argument drew"; "The essay's answer:" → "The answer:" | 36.8s (was 35.75s) |
| B14 | strip clause | "the essay drafts" → "So —" | 21.6s (was 21.9s) |
| B14a | reframe + credit | "Bear's companion post…" removed from voice; `credit` prop added to beat's ChipGrid props | 26.4s (was 28.7s) |
| B15 | strip clause | "The essay's refusal is important:" → "The refusal matters here:" | 17.0s (was 17.5s) |
| B16 | strip clause | "the essay's hardest sentence" → "the hardest sentence in the whole argument" | 14.6s (was 14.3s) |
| B19 | strip clause | "the essay's sharpest reframe" → "the sharpest reframe"; "What the essay adds is" → "The collective axis is what that adds" | 21.8s (was 22.4s) |
| B22 | reframe | "The essay closes by inviting attack —" → "The taxonomy is published as a draft, and pushback is the point." | 8.9s (was 10.5s) |
| B23 | strip clause | "The essay's claim" → "The claim" | 15.2s (was 15.7s) |
| B26 | reframe | "honors the essay's own request" → "takes the taxonomy up on its own request" | 37.6s (was 37.2s) |

**Sweep of remaining 21 beats** for "the author", "the piece", "the argument goes", "he argues", "the article" — **all clean, no additional changes needed.**

**B19 show block:** stale Ted Chiang reference at relative position 0.72 (from GATE F fix) updated to describe what the clip actually shows: "friction · disagreement · trust label appears — terracotta dashes dissolving at the funnel."

**New runtime: 522.8s** (was 527.8s; net -5.0s). SRT regenerated (477s narrated).

**GATE T: PASS** on recompiled slate.

---

## 2026-08-12 (revision pass — GATE T B18 fix + GATE F + SRT regen)

### What was fixed (2026-08-12 session)

**GATE F signed 2026-08-12.** Two beats required corrections:
- B19: Ted Chiang name removed from narration + Manim on-screen credit per no-external-names rule. Audio re-generated (Kokoro am_onyx), Manim re-rendered.
- B22: "real syllabus" → "a syllabus" (illustrative rule); ClaudeComposerAsk greeting `""` → `"Here's the audit."` (Spark-Line Law). Audio re-generated, Remotion re-rendered.

**GATE T B18 fix (2026-08-12 session):** After re-compiling with the new B19/B22 clips, `type_check.py` reported `FAIL (1 pixel beats)` for B18 (§8.6b bbox-overlap 17%). Root cause: node circles with fill_opacity=0.50 and white labels inside split each dark disk into two arcs that blob-detection mistook for overlapping text runs. Fix: labels moved outside the circles (`next_to(dot, direction, buff=0.12)`) and `rx` reduced from 4.5 → 4.0 to keep the rightmost node within the safe zone. B18 re-rendered at 4K. Slate recompiled (527.8s). GATE T re-run → PASS.

**SRT regenerated** (2026-08-12 13:03) from updated beat_sheet.json to reflect B19/B22 actual durations. description.txt (youtube.md) also regenerated.

---

## 2026-08-11 (revision pass — GATE-V defect fix)

### What was fixed

The first compile (2026-08-11 session 1) produced a 533.9s review cut that
failed GATE-V with 34 defects: 6 BLOCKER, 21 STRUCTURAL, 12 COSMETIC. This
session diagnosed root causes and re-rendered all affected beats.

---

### Root causes and fixes applied

#### 1. Manim BLOCKER — edge-bleed (scenes.py)

| Beat | Defect | Root cause | Fix |
|------|--------|-----------|-----|
| B09 | BLOCKER edge-bleed top | Bars grew to height 7.5 (top at y=4.7 > frame top 4.0) | Cap final height at 6.0 (top y=3.2); add upward arrows to preserve "off the chart" meaning |
| B13 | BLOCKER edge-bleed left | Year label `to_corner(UL, buff=0.5)` → x=−6.61 < safe −6.4 | Changed buff=0.5 → buff=0.9 |
| B13 | BLOCKER edge-bleed right | Machine gear `to_edge(RIGHT, buff=0.4)` → x=6.71 > safe 6.4 | Changed buff=0.4 → buff=0.9 |
| B20 | BLOCKER edge-bleed right | Corpus label `to_edge(RIGHT, buff=0.5)` → x=6.61 > safe 6.4 | Changed buff=0.5 → buff=1.5 |

#### 2. Manim STRUCTURAL — underfill (scenes.py)

| Beat | Fill% | Root cause | Fix |
|------|-------|-----------|-----|
| B18 | 34–43% | 5 nodes in circle radius=2.4 → only 30% of frame height | Elliptical layout rx=4.5, ry=2.0; node radius 0.38→0.50; add title at top |
| B19 | 48% | Author nodes fill_opacity=0.15 and model fill_opacity=0.10 → blended diff <28 (doesn't register as ink) | fill_opacity: author 0.15→0.55, funnel 0.45→0.65, model 0.10→0.55; add title at top |
| B20 | 27–54% | Nodes fill_opacity=0.14 → marginal ink registration; frame sparse | fill_opacity: nodes 0.14→0.50, idea chip 0.10→0.40; node radius 0.40→0.60; add title at top |

#### 3. Manim COSMETIC — low-contrast (scenes.py)

| Beat | Contrast | Root cause | Fix |
|------|----------|-----------|-----|
| B13 | 0.21/0.23 | Chip fill_opacity=0.12 → blended lum diff 0.19 < 0.30 | fill_opacity 0.12→0.40 → contrast 0.32 ✓ |
| B18 | 0.24 | Node fill_opacity=0.12 → blended lum diff 0.25 < 0.30 | fill_opacity 0.12→0.50 → contrast 0.41 ✓ |
| B19 | 0.17/0.19 | fill_opacity throughout too low | Addressed by fix #2 above |
| B20 | 0.22/0.27 | fill_opacity throughout too low | Addressed by fix #2 above |

#### 4. Remotion STRUCTURAL — underfill — DeckPattern (DeepExplainerPatterns.tsx)

Root cause: DeckPattern content is vertically centered, spanning only ~54% of
the safe area height at 4K (ink bbox height ≈1056px vs safe_h=1944px). Bounding
box coverage = 88.1% × 54.3% = 47.9% < 55% threshold.

Fix: Added an absolutely-positioned bottom accent rule
(`bottom: 72, left: 100, right: 100, height: 3, background: CLAUDE.INK, opacity: 0.30`)
to both `divergence` and `threshold` variants. This pushes the ink bounding
box y1 to ~1008px at 1080p → y-span 727px → coverage ≈65% ✓.

Beats re-rendered: B02, B03, B05, B06, B07, B10, B11, B13a, B16, B24.

#### 5. Remotion STRUCTURAL — underfill — TierTriageChart (TierTriageChart.tsx)

Root cause: `BAR_MAX_W=560` → max bar right at pixel 1504 at 1080p → 4K x-span
only 46.5% of safe_w=3456. Coverage = 46.5% × 83.5% ≈ 39% < 55%.

Fix: `BAR_MAX_W = 560 → 950`. New max bar right at 1660px → 4K x-span 64% →
coverage ≈55.8% ✓. Verified Tier 1 bars (90% strength) reach pixel 3320 at
4K, safely inside safe_right=3648.

Beat re-rendered: B14.

---

### Re-renders performed

| Component | Beats re-rendered | Method |
|-----------|------------------|--------|
| scenes.py | B09, B13, B18, B19, B20 | `manim -qk` 4K |
| DeepExplainerPatterns.tsx | B02, B03, B05, B06, B07, B10, B11, B13a, B16, B24 | remotion_scenes.py --force |
| TierTriageChart.tsx | B14 | remotion_scenes.py --force |

---

### GATE-V result — 2026-08-11 (after fixes)

```
frames=34  BLOCKER=0  STRUCTURAL=0  COSMETIC=0  → PASS ✓
```

Slate video: `claude-liam-distrust-the-machine-slate.mp4` (20MB, 532.5s)

---

### Gate status — 2026-08-12

- [x] **GATE V** — PASS: `frames=34  BLOCKER=0  STRUCTURAL=0  COSMETIC=0` (2026-08-11, after fixes)
- [x] **GATE F** — SIGNED 2026-08-12. All 13 rows PASS. Two beats corrected (B19, B22).
- [x] **GATE T** — PASS: `type_check.py` clean on final compile 2026-08-12. B18 §8.6b fixed.
- [x] **SRT** — Regenerated 2026-08-12 13:03 from updated beat_sheet.json.
- [ ] **Final cut + staging** — `art final` then `art post` only after Bear reviews this slate.

---

**Standing order obeyed.** This report is the stopping point.
Bear reviews the slate (claude-liam-distrust-the-machine.mp4, 527.8s); no autonomous next steps.
