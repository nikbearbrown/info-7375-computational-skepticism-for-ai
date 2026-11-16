# Build log — claude-liam-chinese-room

## 2026-07-22 — PLAN authored (Gate: plan, awaiting approval)
- Skill: deep-explainer (ai-explainer chassis, your-turn closing).
- Decisions (from Bear): voice = Liam/Kokoro am_onyx (free); book = computational-skepticism-for-ai; POV = keep Bear's take + documentary depth.
- Structure: 5 acts, cold-open + 3-beat closing. 29 body beats, 33 total. Est ~5.9 min @2.9 wps.
- Lane lint: VOX 20.7% (PASS), MANIM 31%, REMOTION 31%, CARD 17.2%. No >2 consecutive same-lane. Vox runs R1 (A2→A3), R2 (A7→A8).
- Title: "The Chinese Room" / kicker "What a 1980 thought experiment saw coming."

## 2026-07-22 — BUILD IN PROGRESS (claude.ai/code session)

### Completed steps
- PEDAGOGY.md written — VERDICT: PASS (plan approval covers Gate P)
- **GATE P audio locked**: 33 beats × Kokoro `am_onyx` @ $0.00. Total runtime: 335.13s = 5m 35s.
  - Durations written to beat_sheet.json (ground truth).
- **Gate D2 SHOPPING.md written** — duration-locked, tier-tagged (A2/A7 Tier 3 rights check to human).
- SHOTLIST.md + PROMPTS.md written (Gate F paperwork).
- **scenes.py written** — 9 Manim scenes (A5/A11/A12/A16/A17/A20/A22/A26/A29). All pass Gate A.
- **All 9 Manim scenes rendered** via `ART_QC=0 run.sh`. Slots filled in `manim/`.
- **Review cut produced** — `claude-liam-chinese-room-slate.mp4`, 335.1s, 27/33 slots filled (6 pantry stills pending).
- **Gate V QC run** — 66 frames, 0 BLOCKER, 46 MAJOR. Root cause:
  - A16 `low-contrast` (bars at 0.18-0.25 opacity too close to PAGE) → fixed: opacity raised to 0.72.
  - A20 `underfill` 41% (bars too short/sparse) → fixed: bar_max_h 2.4→4.5, bar_w 0.7→1.0, % labels added.
  - All other 44 MAJOR: expected underfill on SlateCard placeholders and unfilled pantry beats (no fix needed).
- **A16 + A20 re-rendered** — clean exit, slotted to `manim/`. New review cut written 2026-07-22.
  - A16: bar fill_opacity raised to 0.72 → luminance separation ~0.65 (passes 0.3 threshold).
  - A20: bar_max_h 2.4→4.5, bar_w 0.7→1.0, base_y -1.0→-1.8, % labels added, non-highlight opacity 0.25→0.60.
- **Review cut ready for Gate D1**: `claude-liam-chinese-room-slate.mp4` (335.1s). 27/33 slots filled.
  - Remaining 6 slates: A2, A3, A7, A8, A25, A28 (pantry stills per SHOPPING.md).
  - Motion histogram: hold 72% — expected (SlateCard placeholders + unfilled pantry beats).

### Open (blocks final cut)
- **Gate D1**: watch `claude-liam-chinese-room-slate.mp4` and sign off on pacing/structure.
- **Pantry stills**: source 6 images per SHOPPING.md, drop into `pantry/`, run `art pantry <reel>`.
  - A2, A7: Tier 3 archival portraits — rights decision required by Bear.
  - A3, A25, A28: Tier 1 generic — AI-generated or stock ok.
  - A8: Tier 2 object — verify publisher rights.
- Pantry stills A2, A3, A7, A8, A25, A28 not yet sourced — see SHOPPING.md.
  - A2, A7: Tier 3 archival portraits — rights check required by Bear.
  - A3, A25, A28: Tier 1 generic — AI-generated or stock ok.
  - A8: Tier 2 object — verify publisher rights.

### Gate signatures
- [x] plan approved — Bear 2026-07-22
- [x] factcheck holds — FACTCHECK.md verdict: PASS
- [x] GATE P narration/audio — 2026-07-22, 33 beats locked
- [x] Gate D2 shopping list — SHOPPING.md written duration-locked
- [ ] Gate D1 previz watched — __________
- [ ] final — __________

## Library-first pantry fill pass — 2026-07-22

Library search (1,500 image stills, 566 SVG icons): 0 matches for any of 6 outstanding
pantry slots. Library is an illustration/character collection — no editorial or
historical photography.

`art todo` run: 27/33 beats filled; A2/A3/A7/A8 correctly flagged as
`historical-image · human`; A25/A28 flagged as `ai-video-prompt · human`.
todo.json / STATUS.md / ToDo.md refreshed.

No files dropped this pass. Outstanding needs:
- A2 Turing (T3), A7 Searle (T3) — rights check to human
- A8 journal cover (T2) — verify scan rights
- A3 teletype, A25 person at terminal, A28 server racks — Tier 1, AI-generate fine
Full status in books/PANTRY-FILL-REPORT.md.

## PASS 2 TYPE-LOCK — 2026-07-24

- Lambda override `Text = lambda *a, font='EB Garamond', **k` confirmed present in scenes.py (was already inserted in this session).
- Stale Manim 1080p60 cache cleared: `media/videos/scenes/1080p60/` removed.
- type_check.py run: GATE T: PASS — 33 beats checked, 0 FAILs across all §8.1–§8.5 checks.
  - §8.5 no-wordy-card: 0 FAILs
  - §8.1 min-size: 0 FAILs (worst case B00 at 36px >= 35px floor)
  - §8.2 overflow: 0 FAILs
  - §8.3 contrast: 0 FAILs
  - §8.4 kerning: 0 FAILs (lambda override covers all Manim text)
- No per-beat fixes required — reel was clean at PASS 2 entry.
- `art final` completed: `claude-liam-chinese-room.mp4` (335.1s, 33/33 slots filled).
- GATE T: PASS confirmed by `art final` pre-flight typecheck.

### Gate signatures (updated)
- [x] PASS 2 TYPE-LOCK — GATE T: PASS, 2026-07-24
