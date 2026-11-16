# CHECKS-REPORT — claude-liam-lm-watermarking-walkthrough
**Date:** 2026-08-12  **Session:** GATE P slate previz  **Runtime:** 576s (9:36)  **Audio:** silent (GATE P pending)

---

## Gate roster

| Gate | Result | Notes |
|---|---|---|
| GATE-F | **PASS** (2 advisories) | FC-5: no Status: line in FACTCHECK.md; FC-4: 9 beats uncovered (see below) |
| GATE-L | **PASS** (16 advisories) | 15 FormACard beats >8s with no motion_claim — see §Advisories |
| GATE-BANNED-CARD | **PASS** | — |
| GATE-G | **PASS** | — |
| GATE-RECEIPTS | **PASS** | — |
| GATE-SHARPNESS | **PASS** | median LV=323.2 |
| GATE-V | **FAIL** | 14 hard defects — see §Gate-V detail |
| GATE-T | **FAIL** | §8.10 advisory on 7 beats; 4 pixel beats failed — see §Gate-T detail |
| GATE-BOOKEND | **FAIL** | 3 structural issues — see §Gate-Bookend detail |
| GATE-AUDIO | **FAIL** | Expected: audio not generated (GATE P unsigned) |

---

## §Gate-V detail

**FIXED in this session:** B31_BinomialNull edge-bleed — `SCALE_Y` was inflated by a factor of STD_L (≈7) because the formula used the true normal density peak `1/(σ√2π)` but the parametric function peaks at `1/√2π` (σ-independent). Fix: `SCALE_Y = 0.80 * MAX_H / (1/√2π)`. Curves now fully within frame.

**Remaining hard defects (not fixed — Remotion component design):**

### BLOCKER: B24, B28 — GitHubCodeViewer edge-bleed (4 instances)
The GitHub-skin code viewer's breadcrumb bar reaches the very top edge of the frame (y≈0 px), crossing the title-safe boundary. This is a property of the Remotion `GitHubCodeViewer` component — it renders a full-bleed dark panel with no top margin. Fix requires either (a) adding a `paddingTop` prop to the component, or (b) adding a margin wrapper in the beat props. **Bear: accept as-is (component design), or request Remotion fix?**

### STRUCTURAL: B05, B10, B16, B19, B34 — GitHubSectionRail underfill (10 instances)
Section kicker cards (`GitHubSectionRail`) fill 31–40% of safe area. The component renders content left-aligned with a large faint GitHub octocat watermark on the right — by design for section separators. Gate V flags any frame <55% fill as structural. **Bear: accept underfill as section-card design, or add `body` content to push past 55%?**

---

## §Gate-T detail

### §8.10 — narration paraphrases card (7 advisory beats)

These beats have narration text whose words overlap heavily with the on-screen card text:

| Beat | Score | On-screen | Assessment |
|---|---|---|---|
| B29 | 1.00 | `scores[greenlist_mask] = scores[greenlist_mask] + greenlist_bias` | Intentional: narration reads the one-liner aloud |
| B33 | 1.00 | `scipy.stats.norm.sf(z) → a p-value` | Intentional: narration reads the detection formula |
| B37 | 0.88 | `+17 −15 · 'Documentation Updates'` | Intentional: narration recaps the key diff stat |
| B04 | 0.85 | `model output → LogitsProcessor → adjusted logits → sampler` | Intentional: narration reads the flow diagram |
| B38 | 0.80 | consequence chain `ignore_repeated_bigrams → z-score → verdict` | Debatable: narration should discuss, not read |
| B35 | 0.82 | commit bbe1fb8 metadata | Debatable |
| B01 | 0.81 | BLUF summary numbers | Debatable |

For B29, B33, B37, B04: reading aloud is the correct choice — the viewer sees the exact line of code while hearing it read. The §8.10 advisory is a false positive for code-walkthrough reels. For B38, B35, B01: Bear may want to rephrase narration to discuss rather than recite.

### Pixel checks — 4 beats failing
Gate T ran pixel analysis on rendered frames. The 4 failing pixel beats are in TYPECHECK.md. **Bear: review TYPECHECK.md for specifics.**

---

## §Gate-Bookend detail

Three structural issues with the bookend structure:

| Issue | Required | Current | Fix |
|---|---|---|---|
| Missing BVDT beat | `beat_id: "BVDT"` with `ClaudeVerdictArtifact` | B39 uses `FormACard` with `beat_id: "B39"` | Convert B39 to `ClaudeVerdictArtifact` and rename to `BVDT` |
| Missing BHTF beat | `beat_id: "BHTF"` on Your Turn beat | B40 `ClaudeComposerAsk` has `beat_id: "B40"` | Rename B40 → `BHTF` |
| Outro handle empty | `handle: "@NikBearBrown"` in B41 props | B41 `ClaudeTitleOutro` props has no `handle` field | Add `"handle": "@NikBearBrown"` to B41 props |

---

## §Gate-F advisories

- **FC-5**: FACTCHECK.md has no `Status:` line. Current sign-off line reads "FACTCHECK COMPLETE — 0 failures, 0 fabrications. Signed: Claude, 2026-08-12." The gate wants a `Status:` prefix.
- **FC-4**: 9 beats speak figures not covered by a FACTCHECK row: B01, B18, B24, B27, B28, B30, B31, B38, B40. These beats restate numbers already verified in adjacent beats (e.g., B28 restates the one-line mechanism from B24; B40 restates parameters). **Bear: either add FC rows for each or annotate FACTCHECK.md confirming these are restatements.**

---

## §Gate-L advisories (not blocking)

15 `FormACard` beats run >8s with no `motion_claim`. For a code-walkthrough reel, sustained card dwell is deliberate — viewers are expected to read the card. To silence advisories, add `"motion_claim": "lines stagger in as narration reads each; viewer reads along"` (or similar) to each affected beat.

Affected: B01, B02, B04, B12, B14, B15, B18, B20, B21, B25, B29, B33, B35, B37, B38, B39.

---

## Compile output

- **File:** `claude-liam-lm-watermarking-walkthrough.mp4` (4K, 576s, silent)
- **Slots:** 42/42 filled — 38 Remotion + 4 Manim (B09, B23, B27, B31)
- **Motion:** static:32 / type:6 / drawon:4 (76% static — advisory, not blocking)
- **Audio:** silent — GATE P must be signed by Bear before audio generation

---

## Bear's decisions needed

1. **Gate P sign-off** → generate Kokoro `am_onyx` audio, then recompile
2. **B24/B28 edge-bleed** → accept component design, or request GitHubCodeViewer Remotion fix
3. **B05/B10/B16/B19/B34 underfill** → accept section-card sparseness, or add body text
4. **Bookend: BVDT, BHTF, handle** → three quick JSON edits to bring into spec
5. **§8.10 B38/B35/B01** → rephrase narration to discuss, not recite, if desired
6. **FC-4** → confirm the 9 restatement beats are covered by prior rows, or add rows

**STOP. No art final, no art post, no upload. Awaiting Bear review.**
