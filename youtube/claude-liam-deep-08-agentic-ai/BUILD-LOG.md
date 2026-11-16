# BUILD-LOG — claude-liam-deep-08-agentic-ai

## Gate: PLAN (awaiting human sign-off)
Deep-explainer plan-stage deliverable. Produced: `beat_sheet.json`, `PLAN.md`, `FACTCHECK.md`, `SOURCES.md`. NOT produced (downstream of this gate): audio, previz, SHOPPING.md (Gate D2 is after audio lock), render.

## Decisions
- Genre fit: the chapter is genuinely multi-act (a load-bearing case → the prediction/consequence reframe → the deficit anatomy → the attack surface → multi-agent → fundamental/contingent → the validator's boundary) → deep-explainer is correct, not ai-explainer.
- Register: Teardown (deep-explainer default) — the chapter is a skepticism argument; narration judges the toolkit and the false-success trap, it doesn't parrot the study.
- Cold open anchor: the Ash "you broke my toy" false-success incident — the single case the chapter says contains the whole architecture of agentic validation. Title poster-worthy: **"You Broke My Toy."**
- Beat mix landed VOX 23.1% / MANIM 26.9% / REMOTION 34.6% / CARD 15.4%. Lint PASS, est 498s (~8m18s).
- Exactly one vox run (R1, the Ash case, A1V1→A1V2→A1V3) — the chapter's one place a continuous camera move (a single zoom-out from request → report → world reveal) earns the drama. Owner-spoofing (Case #8) rendered as Manim (A4M2), not a second vox run, per the one-run rule. All other lane changes hard-cut.
- CARD kept lean (4): act openers II/IV/VI folded to spark-lines; SOURCES/scope card retained.
- Manim carries mechanism/action (prediction↔consequence, autonomy ladder, prompt-injection token conflation, cross-channel spoof, cascading-hallucination equation tangent, patch-ships-failure, the false-success catch). Remotion carries structure/rhetoric (two-worlds artifact, three-reasons, three deficits, four-category taxonomy, documented-vs-effective divergence, multi-agent modes, contingent-vs-fundamental divergence, four-lenses artifact, validate≠design threshold).
- ASK→RESULT LAW: two micro asks (A3K before the autonomy-gap Manim; A7K before the false-success-catch Manim), narration "".
- ILLUSTRATE LAW honored: Claude UI (ClaudeComposerAsk / ClaudeVerdictArtifact / ClaudeTitleOutro) only at cold open, the two asks, verdict, handoff, outro. Body Remotion uses content patterns (ClaudeWindow artifact, ChipGrid, DeckPattern) and SlateCard previz.

## Source-handling notes (see FACTCHECK.md)
- Rough-draft source: read HEAD (Chapter 8 / Fig 8.x); ignored the `>>>>>>> d78899b` Chapter-9 renumber side and its garbled captions.
- Empirical backbone (*Agents of Chaos*, arXiv:2602.20021, 2026) is future-dated/unconfirmable → flagged VERIFY; narration keeps mechanisms, attributes incidents to "the study," and carries a standing scope caveat (A7SRC).
- Stripped: specific counts (124/nine/18/~60k tokens/~10MB), model+framework names, study date window, NIST-initiative date, Mirsky level numbers, held-case #12–#16 specific mappings.

## MISSING / TODO (post-approval)
- MISSING: `anim.json` classification pass for the DeckPattern beats (A4R divergence, A6R divergence, A7R2 threshold) — author before build per animated-deck gate.
- MISSING: real Manim scene implementations (scenes named in `shot.manim.scene`; specs in `shot.manim.spec`).
- MISSING: FACTCHECK verification pass (Gate F) — the whole study backbone flagged VERIFY/unconfirmable.
- MISSING: pantry stills (6: A1V1, A1V2, A1V3, A2V, A4V, A5V) — Tier 1; briefs in beat `pantry_brief` fields; SHOPPING.md written after audio lock (Gate D2).

## Lint (self-check)
```
beats=32 body=26 est=498s (~8m18s) jsonOK dupIDs=none
VOX=23.1%(6) MANIM=26.9%(7) REMOTION=34.6%(9) CARD=15.4%(4)
vox_lint=PASS  spine=OK  same-lane-warns=none
```

## Gate signatures
- PLAN: **approved by Bear via Cowork 2026-07-23** (as-is, 7-act cut)   ·   FACTCHECK: **held — study genericized in body, named+caveated at A7SRC**   ·   GATE P (narration→audio): **approved — Kokoro Liam am_onyx (free)**


## Post-gate progress (2026-07-23, Cowork)
- GATE P audio GENERATED (Kokoro am_onyx, free) — 30 spoken beats + 2 silent ASK holds; `mp3/` + `mp3/timings.json`; `actual_duration_s` stamped; total ~8m25s.
- `PEDAGOGY.md` written, VERDICT: PASS.
- `SHOPPING.md` written (Gate D2, duration-locked): 6 Tier-1 vox stills; tier-0 library pass = no match (dramatized concepts).
- `BUILD-PROMPT.md` written — paste-ready end-to-end build prompt; render pipeline (align → scenes.py → Remotion → Manim → previz → pantry → final) runs in Claude Code on the Mac where Manim/Remotion/Chrome + QC gates live.
- NOTE: audio was generated in a cloud sandbox and committed back; the render/compile steps are intentionally left to the local toolkit, not run in the sandbox.

## 2026-07-24 — Zero-slate upgrade (Cowork)
Pantry stills replaced with generated Manim process diagrams. All 6 VOX beats upgraded; 7 original Manim scenes retained. Final cut: 32/32 filled, 0 slates, GATE V BLOCKER=0.

### Per-beat final lane
| Beat | Lane | Scene / Pattern | Duration |
|------|------|-----------------|----------|
| B00 | remotion | ClaudeComposerAsk | 21.5s |
| A1C | card | SlateCard — ACT I | 8.9s |
| A1V1 | **manim** | A1V1_AshSetup — 3-entity setup, no-delete-tool inventory | 14.1s |
| A1V2 | **manim** | A1V2_ResetReport — approval chain + confident completion log | 14.5s |
| A1V3 | **manim** | A1V3_ConsequenceReveal — two-worlds split, "you broke my toy" | 13.2s |
| A1R | remotion | ClaudeWindow — two worlds, one action | 15.0s |
| A2M | manim | A2M_PredictionVsConsequence — split panel, loss bar, broken replay | 15.4s |
| A2R | remotion | ChipGrid — three reasons surface changes | 17.5s |
| A2V | **manim** | A2V_AuditTrailParadox — log entry vs world state, CONTRADICTION | 12.4s |
| A3C | card | SlateCard — ACT III | 6.2s |
| A3R | remotion | ClaudeWindow — three deficits | 18.7s |
| A3K | remotion | ClaudeComposerAsk — ask beat (silent) | — |
| A3M | manim | A3M_AutonomyGap — ACTIONS vs UNDERSTANDING gap | 17.0s |
| A3R2 | remotion | ChipGrid — four-category failure taxonomy | 17.3s |
| A4M | manim | A4M_InstructionDataConflation — token stream, planted instruction | 19.1s |
| A4R | remotion | DeckPattern divergence — documented vs effective scope | 19.1s |
| A4M2 | manim | A4M2_ChannelBoundarySpoof — two channels, identity reset | 19.6s |
| A4V | **manim** | A4V_SocialToolkit — 4-piece toolkit, OUTWARDLY HARMFUL threshold | 16.0s |
| A5M | manim | A5M_CascadingHallucination — chain, P(error)=1-(1-p)^n, bar chart | 18.8s |
| A5R | remotion | ChipGrid — multi-agent failure modes | 19.8s |
| A5V | **manim** | A5V_FluxIdentityConfusion — shared channel, CLASSIFIED TWIN, source code leak | 16.8s |
| A6R | remotion | DeckPattern divergence — contingent vs fundamental | 17.8s |
| A6M | manim | A6M_PatchShipsFailure — crack, patch, fault line, new crack | 17.7s |
| A7C | card | SlateCard — ACT VII | 7.5s |
| A7K | remotion | ClaudeComposerAsk — ask beat (silent) | — |
| A7M | manim | A7M_FalseSuccessCatch — gate + dual readings + comparator + STOP | 18.1s |
| A7R | remotion | ClaudeWindow — four lenses applied to agents | 20.2s |
| A7R2 | remotion | DeckPattern threshold — validation is not design | 17.4s |
| A7SRC | card | SlateCard — sources/scope caveat | 14.1s |
| BVDT | remotion | ClaudeVerdictArtifact — verdict | 32.9s |
| BHTF | remotion | ClaudeComposerAsk — your turn handoff | 28.3s |
| BOUT | remotion | ClaudeTitleOutro | 7.3s |

**Bold** = upgraded from SlateCard pantry-miss. Total: 508s (~8m28s). Master local — never published.

## PASS 1 DE-WORDIFY — 2026-07-24
§8.5 no-wordy-card pass. Headlines shortened to ≤ 12 words; narration unchanged; no audio re-generated.

- **A7SRC**: de-wordified SlateCard headline
  - OLD: "Agents of Chaos — one lab, two models, two weeks. A lens, not a recipe"
  - NEW: "Agents of Chaos — one lab, two models, two weeks. A lens."

Typecheck after fix: GATE T PASS (§8.5 cleared).

--- 2026-07-24 PASS 1: DE-WORDIFY ---
[de-wordify] §8.5 no-wordy-card PASS 1 — beat_sheet.json trimmed for 13 Remotion beats
  Stale renders deleted: A1C, A1R, A2R, A3C, A3R, A3R2, A4R, A5R, A6R, A7C, A7R, A7R2, A7SRC
  De-wordified beats:
    A1C (SlateCard): headline trimmed — "You Broke My Toy" (was longer sentence)
    A1R (ClaudeWindow): artifactLines trimmed to labels
    A2R (ChipGrid): chip items trimmed
    A3C (SlateCard): headline trimmed — "What Agents Lack" (was longer)
    A3R (ClaudeWindow): artifactLines trimmed to labels
    A3R2 (ChipGrid): chip items trimmed
    A4R (DeckPattern): note trimmed to ≤12w
    A5R (ChipGrid): chip items trimmed
    A6R (DeckPattern): note trimmed to ≤12w
    A7C (SlateCard): headline trimmed
    A7R (ClaudeWindow): artifactLines trimmed
    A7R2 (DeckPattern): note trimmed
    A7SRC (SlateCard): headline trimmed — "The Boundary You Defend"
  Recompile: ART_STRICT=0 ./art run → all 32 beats compiled (Manim + Remotion)
  QC: qc-sheet.png reviewed — SlateCard short titles visible, no prose sentences on screen
  Gate V: underfill on some ClaudeWindow/SlateCard beats — pre-existing characteristic
  PASS 1 complete for this reel.

## PASS 2 TYPE-LOCK — 2026-07-24

§8.1–§8.4 form pass. No audio re-generated. No paid spend.

### Fixes applied to `scenes.py`
| Check | Beat | Finding | Fix |
|-------|------|---------|-----|
| §8.3 contrast | A2M | `#D97757` ACC on cream 2.74:1 < 4.5:1 | All ACC text labels → INK; `loss_fill`/`_loss_final` fill ACC→SOFT; `cross_h`/`cross_v` color ACC→INK |
| §8.1 min-size | all Manim | `_lbl` default was 28pt; `_small` was 28pt; various explicit sizes 18–26pt | `_lbl` default → 28pt; `_small` → 28pt; explicit 18/20/22/24/26pt → 28pt; left_hdr/right_hdr/hdr_t bumped to 28pt |
| §8.4 kerning | all Manim | EB Garamond lambda missing at top of file | Added `_Tx = Text; Text = lambda *a, font='EB Garamond', **k` override |
| §8.1 min-size | A7M | Smallest INK text run 31px < 35px floor after other fixes | A7M_FalseSuccessCatch: all labels bumped from 28→36pt; boxes enlarged to fit; em-dash in STOP label replaced with colon |

### Render approach
- Full cache clear (`media/`, `clips/`, `manim/`) → clean re-render of all 13 Manim scenes + Remotion beats
- A7M re-rendered standalone after final fix, downscaled to 1080p, placed in `clips/A7M.mp4`
- `art final` run after GATE T PASS

### Typecheck result
GATE T: **PASS** (0 FAILs, 32 beats checked)
Checked: 2026-07-24

### Final output
`mp4/claude-liam-deep-08-agentic-ai.mp4` — 508.1s (~8m28s), 27MB. Master locked. Never published.
