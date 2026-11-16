# CHECKS-REPORT.md — Gate D1 Slate Previz (UPDATED)

Reel: `claude-liam-two-models-twice-the-price`  
Updated: 2026-07-29  
Final build: run 12 (ART_STRICT=0, --height 1080)  
Original build: run 6 (2026-07-28)

---

## Gate summary — build 12 (final)

| Gate | Result | Notes |
|------|--------|-------|
| **GATE T** (type-lock) | **PASS** | 41 beats, 0 FAILs — contrast, kerning, min-size, overflow all clean |
| **GATE V** (frame QC) | non-blocking | BLOCKER=0, MAJOR=58 (cosmetic advisories only) |
| **GATE SHARPNESS** | **PASS** | 41 beats, median LV=370.1 |
| **GATE BOOKEND** | **PASS** | 4 bookends correct (B00, BVDT, BHTF, BOUT) |
| **GATE BANNED-CARD** | **PASS** | No SlateCard or banned ClaudeWindow usage |
| **GATE F** (factcheck) | **PASS** | 14 rows, 22 beats covered, 0 uncovered |

---

## Slot fill

41/41 beats filled. No slates, no gen-AI, no pantry items.

| Lane | Beats | Fill type |
|------|-------|-----------|
| BOOKEND | 4 | Remotion (rendered) |
| CARD | 4 | Remotion (rendered) |
| REMOTION | 17 | Remotion (rendered) |
| MANIM | 20 | Manim (rendered) — 9 original + 11 new from pilot fix |

---

## Pilot fix summary (2026-07-29)

11 violation beats rewritten — see AUDIT.md for full before→after log.

- 9 gen-AI STILL beats → Manim drawn diagrams
- 2 FormACard withheld-show beats → Manim drawn diagrams

GATE T iteration required 4 extra builds (8–12) to resolve:
- 6 ACC-as-text-on-cream contrast violations in new scenes
- 1 font_size=20 below 34px floor at 4K (B13 `flag_label`)
- 2 ACC SurroundingRectangle box outlines detected as text blobs (w/h 3.7–4.5)

All resolved without changing any content or pedagogy — only color assignments on
strokes and labels.

---

## What is confirmed

- Audio: Kokoro am_onyx throughout — no ElevenLabs, no re-synthesis
- Outro: ClaudeTitleOutro · @NikBearBrown · no subline ✓
- No gen-AI imagery anywhere in the reel ✓
- No real model names, no real benchmark numbers — all data illustrative ✓
- All 20 Manim scenes gating-clean ✓
- All 4 bookends correct ✓

---

## What is NOT done (requires Bear's review before proceeding)

1. **FACTCHECK.md** — existing open items; no new claim-bearing beats were added
2. **Bear's visual review** — watch the compiled mp4 and flag any aesthetic issues
3. No `art final`, no 4K, no TOPOST, no publish — STOP here.

---

## Review cut location

`claude-liam-two-models-twice-the-price.mp4` — compiled slate master (1080p, beat labels)
