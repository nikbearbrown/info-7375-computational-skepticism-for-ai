# BUILD-LOG — claude-liam-distrust-the-machine

## 2026-07-21 — authored + audio locked (Cowork session; deep-explainer episode 5)

- HUMAN NOTE (logged first): Bear — "next deep explainer" + his own
  Theorist.ai launch essay ("Knowing Enough to Distrust the Machine",
  skepticism.ai, 2026-03-13). Standing process: agent builds and locks
  Liam audio while Bear shops; one paste per pass; standing free-pipeline
  authorization = GATE P signature.
- Plan: 28 beats — B00 cold open + 23 body beats across six acts + closing
  block (B25 verdict / B26 your-turn / B27 title outro). Lane mix (body):
  vox 5 (21.7%) · manim 5 · remotion 7 · card 6 · ask 1 (exempt). Manim
  sits under the ~25–40% target band — accepted: this essay's body is
  argument-structure-heavy (chips, columns, thresholds), which is
  Remotion's lane; logged per the mix contract rather than padded.
- Vox run: R1 = B05→B06 (chalkboard drill tight → the whole room as
  designed, one plate). Single run this episode.
- Audio: all 28 beats, Kokoro am_onyx. Locked total **6:41** (401.3s) —
  the shortest episode of the five; the essay is one argument, not a
  survey, and padding it to 8 minutes would violate duration-planner
  doctrine (duration is an output). timings.json is ground truth.
- NOTE: the cloud workspace was recycled mid-build; model files and
  scripts were re-staged from the toolkit and generation re-run. No
  content was lost (episodes 1–4 were already committed to disk).
- Gate D2: SHOPPING.md — 4 files / 5 windows, all tier-1 (optional LOC
  archival swap for the classroom plate, sidecar required if used).
  Lightest shop of the series.
- Captions: claude-liam-distrust-the-machine.srt (104 cues, source text
  on measured windows). description.txt drafted with chapters + essay and
  theorist.ai links.
- FIRST-PARTY RULES (binding): tier names verbatim, tier content limited
  to the essay's own statements; the freeze student is a composite (no
  face on B02's plate); the B22/B23 syllabus triage is labeled
  illustrative, no real institution; B19 keeps the essay's "may be"
  hedge; Gardner (the one external claim) verifies independently.

## 2026-08-11 — GATE-V defect fix (Cowork session)

- First compile produced 533.9s review cut; GATE-V: 6 BLOCKER / 21 STRUCTURAL / 7 COSMETIC.
- Root causes diagnosed via frame extraction:
  - B09: bars exceeded Manim frame top (height 7.5 → y=4.7 > frame top 4.0). Fixed: cap at 6.0 + arrows.
  - B13: year label and machine gear outside title-safe. Fixed: buff=0.9 both.
  - B20: corpus label at right edge. Fixed: buff=1.5.
  - B18/B19/B20: fill_opacity too low (<28 ink_delta threshold); B18 also ellipse-too-small. Fixed: all opacities raised to 0.50–0.65; B18 elliptical layout rx=4.5 ry=2.0; titles added.
  - DeckPattern (B02/B03/B05/B06/B07/B10/B11/B13a/B16/B24): vertically centered content covers only 48% of 4K safe area. Fixed: bottom accent rule at bottom:72 in DeepExplainerPatterns.tsx.
  - TierTriageChart (B14): BAR_MAX_W=560 → x-coverage only 46%. Fixed: BAR_MAX_W=950.
- Re-rendered: 5 Manim scenes (manim -qk) + 11 Remotion beats (remotion_scenes.py --force).
- Recompiled: art run → slate 532.5s, 20MB.
- GATE-V pass 2: frames=34, BLOCKER=0, STRUCTURAL=0, COSMETIC=0. ✓
- See CHECKS-REPORT.md for full defect table and fix details.

## Gate status

- [ ] GATE F — FACTCHECK.md drafted (13 rows), all OPEN.
- [x] GATE P — standing authorization (free pipeline).
- [x] Audio lock — 8:52; timings.json is the clock. (Expanded from 6:41 per Bear additions.)
- [x] Gate D2 SHOPPING.md — written from locked durations; Bear shopping.
- [x] Gate D1 previz — pass 1 complete: scenes.py (5 Manim scenes), all Remotion patterns
      rendered, art run, GATE-V pass. See CHECKS-REPORT.md.
- [x] GATE-V — PASS (BLOCKER=0, STRUCTURAL=0, COSMETIC=0). 2026-08-11.
- [ ] GATE T — TYPECHECK.md not yet run on this revision.
- [ ] GATE F — FACTCHECK.md: 13 rows, all OPEN. (Gardner claims; MI empirical; Chiang credit.)
- [ ] Pantry fill — B23 syllabus-triage artifact pending Bear's pantry/ drop.
- [ ] Final cut + staging — `art final` then `art post` after Bear reviews slate.

## MISSING / open questions for Bear

- Standing pattern-id reconcile against Root.tsx at pass 1.
- 6:41 sits below the 5–10 band's midpoint but inside it; if you want it
  longer, the honest lever is adding an act (e.g. a worked triage of a
  SECOND syllabus), not padding beats — say so before pass 1 and I'll
  author it.
- Episode 5 of the series; the five your-turn prompts now form a coherent
  set (verify a claim / fix a rubric / test a correlation / audit a
  deployment / attack a taxonomy) — playlist-description note at publish.
