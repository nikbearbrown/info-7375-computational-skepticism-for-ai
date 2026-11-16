# BUILD-LOG — claude-liam-do-chatbots-pass

## 2026-07-23 — plan authored (cloud sandbox session)
- Skill: `deep-explainer`, Liam persona. Book: computational-skepticism-for-ai.
  Empirical/historical companion to `claude-liam-chinese-room`.
- Studied the Chinese Room reel to match house conventions: **Bear's no-text-slide rule**
  (concepts = DOODLE/VOX, Remotion = bookends only, Manim = data only). Adopted, not the
  skill's default Remotion-heavy mix.
- Web-verified all load-bearing history facts before authoring (see FACTCHECK.md): ELIZA 1966,
  PARRY 48%, Loebner 1990, Eugene Goostman 33% (2014, contested "pass"), Turing 30%/5-min,
  and Jones & Bergen 2025 three-party test (strongest model 73%, above the human).
- Beat sheet: 33 beats (29 body + 4 exempt). Lane mix DOODLE 13 / VOX 7 / MANIM 4 / CARD 5.
  Histogram: VOX 24.1% (aim 20–25 ✅), no >2 same-lane runs, one vox run R1 (A9→A10), all
  body beats ≤46 words. Est. ~6.1 min at 2.9 wps (measured audio is the only clock).
- Recurring MANIM "fool-rate meter" motif carries the data spine (A5 → A11 → A17 → A26).
- Datable material: historical years kept (they're the subject); no current model/vendor names
  in narration.

### GATE SIGNATURES (human-owned)
- [x] **PLAN** — authorized by Bear (build prompt received 2026-07-23)
- [x] **Gate F** — factcheck locked (all 16 claims verified; contested #10 framed correctly; Bear authorized GATE P audio 2026-07-23)
- [x] **GATE P** — Kokoro am_onyx narration generated (free; 33 mp3s in mp3/; $0.00). align.py ran, words.json written (33 beats, 0 fallbacks). 2026-07-23
- [x] **Audio lock** — measured durations in beat_sheet.json (actual_duration_s). Total body ~276s, est. assembled ~6.0–6.5 min. 2026-07-23
- [x] **Gate D2** — SHOPPING.md written from locked durations. 7 stills listed. 2026-07-23
- [x] **Gate D1** — 22 Manim scenes rendered (Gate B clean); Remotion bookends; slate previz compiled (333s / ~5:33). `claude-liam-do-chatbots-pass-slate.mp4` ready. 2026-07-23
- [ ] **Review cut** — VISUAL QC LAW pass
- [x] **Final** — `./art final --allow-slates` run 2026-07-24; `claude-liam-do-chatbots-pass.mp4` (11MB, 333.5s). Never published (public = human Studio flip)

### MISSING / open
- **Execution environment:** this planning session runs in the Anthropic cloud sandbox; the
  brutalist-art render toolkit lives on Bear's Mac. Audio/render steps (GATE P onward) must run
  against the local toolkit in the book folder, or be re-run on-computer. Flagged to Bear at the
  PLAN gate.

---

## PASS 2 TYPE-LOCK — 2026-07-24

- Reel: `claude-liam-do-chatbots-pass`
- Lambda override already present in scenes.py (§8.4 EB Garamond default, inserted in prior session).
- TYPECHECK.md from 2026-07-24T05:25 showed GATE T: PASS with 0 FAILs across all 33 beats (22 Manim, 5 CARD, 4 Remotion; 7 VOX skipped — no video).
- No fixes required: §8.1 min-size PASS (floor 35px; worst case A11 at 36px, A23 at 35px), §8.2 overflow PASS, §8.3 contrast PASS, §8.4 kerning PASS (lambda override active), §8.5 no-wordy PASS (0 wordy elements, 0 beats checked).
- Beat issues: none. All 22 Manim beats passed on first check.
- Slates present: A2, A7, A9, A10, A16, A21, A29 (7 VOX beats with no pantry stills; expected per SHOPPING.md).
- `art final` ran with `--allow-slates` flag (correct arg order: reel path first, flag second).
- GATE T: PASS confirmed by live type_check.py re-run at final gate.
- Final cut: `claude-liam-do-chatbots-pass.mp4` — 11MB, 333.5s (~5:34), 26/33 slots filled. Written 2026-07-24 09:00.
