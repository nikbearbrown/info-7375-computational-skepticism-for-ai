# CHECKS-REPORT — claude-liam-watermarks-remover
Generated: 2026-08-14

## Build state

- Slate cut: `claude-liam-watermarks-remover.mp4` — 10m11s, 41/41 filled
- Audio: 40 beats generated (Kokoro am_onyx, $0.00)
- GATE F: PASS (19 rows, all ✓ PASS / CORRECTED / EXEMPT)
- GATE L: PASS (no lane violations)
- GATE V: **FAIL — 6 BLOCKERs, 16 STRUCTURAL**

---

## GATE V BLOCKERs (must fix before final)

| Beat | Issue | Pattern | Fix |
|---|---|---|---|
| B02 | edge-bleed left/right | `GitHubRepoHero` | Reduce horizontal overflow — tighten padding or shrink hero content |
| B21 | edge-bleed top | `GitHubCodeViewer` | Code viewer overflows title-safe top — reduce font size or line count |
| B33 | edge-bleed left/right | Manim `B33_DependencyCount` | Manim bar chart overflows safe area — reduce bar width or add margins in `scenes.py` |

---

## GATE V STRUCTURAL (underfill < 55%)

These are section-rail beats with one short narration line — visually sparse by design.
All use `GitHubSectionRail`. Bear to decide: (a) accept as-is (rail design is intentionally
minimal), or (b) add a second body line to each to lift fill.

| Beat | Fill % | Narration (why it's sparse) |
|---|---|---|
| B01 | 32% | "Four days. No dependencies. That is the thesis." |
| B05 | 32% | "What are the files?" |
| B10 | 29% | "How do the scripts connect?" |
| B15 | 32% | "When was it built?" |
| B20 | 32% | "The scope document." |
| B28 | 32% | "The binary guard." |
| B32 | 32% | (section rail — check beat sheet) |
| B12 | 51% | Manim ImportFan — just under 55% threshold |

---

## GATE F advisory (not blocking)

8 beats with numeric claims not covered by a FACTCHECK row:
B03, B08, B29, B30, B31, B33, B35, BSRC.
Bear to confirm these are editorial (not raw claims) or add rows.

---

## GATE L advisory (not blocking)

19 `card-over-runtime` warnings: FormACard beats with narration >8s and no `motion_claim`.
These are long narration beats over a static card — deliberate in this reel's git-explainer
style. Bear to confirm or add `motion_claim` to each.

## Next step (Bear decides)

1. Fix the 3 BLOCKER patterns (B02 GitHubRepoHero, B21 GitHubCodeViewer, B33 Manim)
2. Decide on underfill for the 8 section-rail beats
3. Re-run `art run` after fixes
