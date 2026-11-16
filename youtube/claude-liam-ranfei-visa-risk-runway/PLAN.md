# PLAN — Claude, Recalibrated (Professor Bear's notes on Ranfei's Visa-Risk Runway Engine)

**Slug:** `claude-liam-ranfei-visa-risk-runway` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Framing:** Liam asks Claude what feedback Professor Bear would give the student. **First name only** — "Ranfei", "Professor Bear" / "Bear". Never the surname.
**One idea:** *Generalizing a working pipeline isn't adding rows — each new scope silently breaks an assumption the original was calibrated on; the skeptic re-derives confidence, thresholds, and the risk-clock for the new scope instead of porting them.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "What would Bear tell Ranfei about generalizing the engine, FAANG→broad pool + STEM OPT timing?" → ask answered, Liam signs in
ACT I    Two Problems, One Codebase   two changes, each breaks an assumption           (B01 PredictCard, B02 Manim branch)
ACT II   No History Isn't No          data-confidence: value ≠ confidence               (B03 Manim divergence, B04 VOX, B05 ask→ B06 Onda code, B07 Manim two-axis)
ACT III  A Different Clock            STEM extension = terminal clock; cap-gap changed   (B08 Manim two-state, B09→B10 VOX run R1, B11 ask→ B12 Onda code, )
ACT IV   Re-derive, Don't Port        recalibrate thresholds on the new pool             (B13 Manim threshold-on-new-pool)
ACT V    Make It Break                four generalization-specific robustness tests      (B14 ChipGrid, B15 VOX drawon regulatory-version)
ACT VI   Honest Colors                confirmed RED ≠ unknown; show the binding clock     (B16 Manim confirmed-vs-unknown, B17 illustration binding-clock, B18 Manim converge)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (five notes)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — the generalization pressure-test prompt, read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — "Claude, Recalibrated"
```

## Lane histogram (body beats only; bookends + ask micro-beats exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 4 | 18% | 20–25% | passes the hard vox lint (15–30% clear); toward low end |
| MANIM | 7 | 32% | 25–40% | ✓ |
| REMOTION | 5 | 23% | 30–45% | slightly light — a builder may promote one segment card to a REMOTION spark-illustration |
| CARD | 6 | 27% | remainder | 6 segment cards (one per act) |

Body beats: 22 · No same-lane run >2. ASK micro-beats B05/B11 precede the two Onda code blocks (ASK→RESULT). Est. runtime ≈ 5:20 (measured audio is the only clock).

## ASK→RESULT pairs
- B05 → B06: ask for `sponsorship_signal` → the Onda code-block (value vs confidence).
- B11 → B12: ask for `compute_risk_windows` → the Onda code-block (two clocks, terminal flag, cap-gap comment).

## Vox run
- **R1 (B09→B10):** the 24-month runway eroding during adjudication → the terminal STOP with no fallback. One continuous move; handoff block authored in the sheet.

## Honesty / DOUBLE-CHECK
- Real code only in the Onda blocks (the two functions from the source, tidied for screen width).
- **Verified:** H-1B Modernization Final Rule effective Jan 17 2025; cap-gap now runs to ~April 1 of the next calendar year (was: Sept 30). Carried as a *mechanism* — "the rule changed; verify current USCIS guidance" — not a timeless date. The code comment says "verify vs current USCIS guidance."
- **Dropped:** the single-source 90-day-vs-100-day gap-rate figure (source itself flagged it unverified). Not on screen, not in narration.
- **First name only** enforced across every beat; no student surname anywhere.

## Gates — UNATTENDED slate-cut run
Author authorizes the gates in advance. Target deliverable = **Gate D1 full-length SLATE PREVIZ** (real Kokoro audio, real Manim/Remotion, slates in the 4 vox slots B04/B09/B10/B15), `--review` burn-in, watchable MP4. Stop there for review — no pantry sourcing, no `final`, never publishes.
