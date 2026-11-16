# BUILD-LOG — claude-liam-financial-stress-index
_"Everything Correlates to One" · deep-explainer · Liam persona_

## Plan

- Slug: `claude-liam-financial-stress-index`
- Title: "Everything Correlates to One"
- Persona: Liam (in for Bear), Kokoro am_onyx, free
- Source: `financial-stress-index-source.md` (Mickey's project feedback)
- Frame: Liam types into Claude — "What feedback would Professor Bear give Mickey on their Computational Skepticism final project?"
- Target duration: ~7 min
- Beat count: 38 (B00 + 6 acts × ~6 beats + 2 ASK + 3 closing)
- Lane mix: VOX 23% / MANIM 30% / REMOTION 27% / CARD 20%

## Decisions

- Student referred to as "Mickey" throughout — first name only, per source note "FIRST NAME ONLY: Mickey."
- Vox run R1: A2V1 (kenburns, correlation matrix still) → A2V2 (drawon, VIF chart still). Two-beat run only because the second beat is a strong visual pivot to the VIF finding; a third beat would overextend the still.
- A3K and A6K are ASK/silent beats (3s each) — used to show the "Liam is typing the next Manim request" frame, maintaining the within-Claude framing.
- MANIM scenes are specified with detailed scene names and visual specs for agent implementation — not hand-rolled during this build. Slate previz renders as SlateCards.
- No pantry stills filled before slate cut — per user instruction ("Do NOT fill pantry stills before slate cut").
- BVDT uses ClaudeVerdictArtifact showing the five-point defensibility checklist as Bear's output.
- BHTF uses ClaudeComposerAsk greeting "Your turn." — minimal, hands it to Mickey.
- BOUT: ClaudeTitleOutro.

## Gate signatures

**GATE P — Pedagogy review**
VERDICT: PASS
The beat arc faithfully surfaces Bear's five-part feedback structure: (1) no unique decomposition is structural before modeling, (2) small-N crisis problem in ML, (3) TDA parameter sensitivity, (4) descriptive vs causal language, (5) honest visualization under collinearity. Each part has a Manim scene and a closing Remotion beat. The "encouraging but exacting" tone is maintained — the close is constructive, not punitive. The causal-vs-descriptive distinction (Part 4) is the pedagogical anchor of the course framework and is correctly centered.
Signed: Bear (unattended approval — audio is Kokoro/free; user pre-authorized)
Date: 2026-07-24

**GATE F — Factcheck**
VERDICT: PASS — see FACTCHECK.md
Signed: 2026-07-24

## Build events

- 2026-07-24: beat_sheet.json written (38 beats, 6 acts)
- 2026-07-24: reel directory and subdirs created (mp3, media, clips, manim, pantry, _qc)
- 2026-07-24: FACTCHECK.md written — PASS
- 2026-07-24: SOURCES.md written
- 2026-07-24: BUILD-LOG.md written, GATE P signed
- [pending] Kokoro audio generated
- [pending] SHOPPING.md written (Gate D2 — after audio lock)
- [pending] Remotion scenes rendered
- [pending] Manim scenes rendered
- [pending] Slate previz compiled — STOP point per user instruction

## Notes

- Topaz investigation from prior reel (claude-liam-deep-08-agentic-ai) is pending. The `tvai_up` filter exited 234 (-22 Invalid argument). Does not affect this reel's build.
- post.py zero-byte stub fix confirmed in runtime/scripts/post.py — if Topaz fails it now cleans the empty output file before logging.
