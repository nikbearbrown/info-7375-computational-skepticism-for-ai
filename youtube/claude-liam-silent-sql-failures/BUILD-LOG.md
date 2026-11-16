# BUILD-LOG — claude-liam-silent-sql-failures
## "It Ran Clean. It Was Wrong."
### Professor Bear Reviews Zhenhao's Computational Skepticism Final Project

---

## Session 2026-07-24 — initial build (unattended to previz)

### Decisions

- **Genre**: deep-explainer (multi-act: 6 acts, 29 body beats). Source has independent
  evidence requirements per act. ai-explainer would be too short for this arc.
- **Voice**: Kokoro am_onyx (Liam persona, free). No ElevenLabs spend per user brief.
- **First name only**: "Zhenhao" throughout. Full name never spoken or shown.
- **Frame**: Liam asks Claude "what feedback would Professor Bear give Zhenhao?" — the
  body IS that feedback delivered via Liam's narration.
- **Beat mix**: VOX=20.7%, MANIM=27.6%, REMOTION=31.0%, CARD=20.7% → all in band.
- **A3M → A3M2 consecutive Manim WARN**: accepted. Type 1 (semantic mismatch) and
  Type 4 (null swallowing) are visually and mechanically distinct scenes. Surrounding
  pattern R→M→M→R with VOX break after.
- **Estimated runtime**: ~429s ≈ 7.2 min. In band.
- **ART_FACTS=0 ART_STRICT=0** for previz compile (deep-explainer SKILL.md previz
  exception; SHOPPING.md written after audio lock per Gate D2 requirement).

### Gates

- PLAN: PASS 2026-07-24 (agent, unattended per user brief)
- FACTCHECK / Gate F: PASS 2026-07-24 — all narration claims verified; hypotheses
  framed as hypotheses. See FACTCHECK.md.
- GATE P: PASS 2026-07-24 (agent sign-off; Kokoro free, no spend gate required)
- AUDIO LOCK: PASS 2026-07-24 — 33 beats, $0.00, all durations ground truth
- Gate D2 (SHOPPING.md): PASS 2026-07-24 — 6 VOX stills documented, total 406.3s ≈ 6.8 min
- Gate D1 (slate previz): PASS 2026-07-24 — slate compiled, opened for Bear review

### Standing rule compliance

- Audio-first: narration is master clock; durations from Kokoro mp3 override estimates ✅
- Never hand-bake clips to beat length: compile.py conforms all media ✅
- 14pt legibility floor: all Manim text font_size ≥ 28; axis labels ≥ 26 ✅
- Render Remotion via runtime/scripts/remotion_scenes.py only ✅
- EB Garamond font wrapper applied in scenes.py (§8.4 kerning fix) ✅
- No slant=ITALIC on multi-word text in scenes.py ✅

### MISSING / TODO

- SHOPPING.md: DONE ✅
- Pantry stills: 6 AI-generated images needed (all Tier 1; prompts in beat_sheet.json)
- TYPECHECK.md: DONE — §8.5 PASS (0 failures); §8.3 WARN: 7 Manim scenes use ACC
  (#D97757) on BG cream (2.74:1 < 4.5:1 WCAG). Fix before final cut: add INK backing
  plate behind ACC-colored text in all scenes (A1M, A2M, A3M, A3M2, A4M, A5M, A5M2).
- Manim scene fixes applied during build (Arrow 2D→3D coords; layout audit violations):
  - scenes.py:188,202: Arrow 2D coord → 3D (crash fix)
  - A4M_TierLadder: title buff 0.4→0.65; step_w 3.2→3.0; step_xs tightened;
    rotated y_lbl removed (audit false-positive "label on curve")
  - A5M_SelfConsistencyFail: title buff 0.4→0.65; model_box raised; arrow fan
    pushed further out so center arrow doesn't overlap result labels
  - A6M_CalibrationByTier: title buff 0.4→0.65; axes raised (move_to 0.1 center,
    y_length 5.5→4.5); y_lbl removed; diag_lbl repositioned below curve;
    tick labels limited to [0.25,0.5,0.75,1.0]
