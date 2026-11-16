# PLAN — Claude, Defensible (Professor Bear's notes on Yuqing's design-track sponsorship triage)

**Slug:** `claude-liam-yuqing-design-sponsorship-triage` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Framing:** Liam asks Claude what feedback Professor Bear would give the student. **First name only** — "Yuqing", "Professor Bear" / "Bear". Never the surname.
**One idea:** *A weights-profile is right only if the old signals stay valid proxies for the new sub-population; for design roles they don't — the real risk (does the role even qualify as a specialty occupation?) is a MISSING signal, not a coefficient.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "What would Bear tell Yuqing about extending the engine to design with a weights-profile?" → ask answered, Liam signs in
ACT I    Weights, or a New Signal?  reweighting assumes old signals still fit         (B01 PredictCard, B02 Manim branch)
ACT II   Does It Even Qualify?      specialty-occupation = a missing signal for design (B03 Manim settled-vs-contested, B04→B05 VOX run R1, B06 ask→ B07 Onda code, B08 illustration has-vs-would)
ACT III  Not All Three Transfer     per-signal: lag-adjust / disaggregate / re-baserate (B09 Manim, B10 VOX)
ACT IV   Thin Data                  small design dataset → overfitting                 (B11 Manim overfit)
ACT V    Make It Break              four extension-specific robustness tests            (B12 ChipGrid, B13 VOX drawon posting stress)
ACT VI   Honest Colors              surface defensibility + split sponsorship record    (B14 illustration, B15 illustration, B16 Manim converge)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (five notes)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — the reweight-for-a-new-group pressure-test prompt, read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — "Claude, Defensible"
```

## Lane histogram (body beats only; bookends + ask micro-beats exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 4 | 19% | 20–25% | passes the hard vox lint (15–30% clear); toward low end |
| MANIM | 5 | 24% | 25–40% | just under; acceptable |
| REMOTION | 6 | 29% | 30–45% | ✓ (essentially on target) |
| CARD | 6 | 29% | remainder | 6 segment cards (one per act) |

Body beats: 21 · No same-lane run >2. One ASK→RESULT pair. Est. runtime ≈ 5:15 (measured audio is the only clock).

## ASK→RESULT pair
- B06 → B07: ask for `specialty_occupation_defensibility` → the Onda code-block (team credential ratio + posting specificity → high/low/mixed).

## Vox run
- **R1 (B04→B05):** the credentialed design team (defensible) → the self-taught team (RFE risk). One continuous move across two teams; handoff block authored in the sheet.

## Honesty / DOUBLE-CHECK
- Real code only in the Onda block (the source's `specialty_occupation_defensibility`, tidied for screen width).
- **Verified:** design/UX H-1B roles face notably higher specialty-occupation scrutiny than SWE; the hiring team's credential composition + job-description specificity is the actual diagnostic; a "UX Designer" staffed by business/marketing grads doesn't survive scrutiny; vague "creative" roles draw denials (F1Jobs UX/UI-designer H-1B guide; specialty-occupation four-test / RFE practice). Carried as the *mechanism* of the missing signal, not as datable numbers.
- 8 CFR §214.2(h)(4) named as the regulatory anchor, framed as the definition of specialty occupation, not a timeless quote.
- **First name only** enforced across every beat; no student surname anywhere.

## Gates — UNATTENDED slate-cut run
Author authorizes the gates in advance. Target deliverable = **Gate D1 full-length SLATE PREVIZ** (real Kokoro audio, real Manim/Remotion, slates in the 4 vox slots B04/B05/B10/B13), `--review` burn-in, watchable MP4. Stop there for review — no pantry sourcing, no `final`, never publishes.
