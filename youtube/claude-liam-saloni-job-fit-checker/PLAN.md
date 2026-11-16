# PLAN — Claude, Skeptical (Professor Bear's notes on Saloni's job-fit checker)

**Slug:** `claude-liam-saloni-job-fit-checker` · **Channel:** claude-liam (Liam, Kokoro `am_onyx`, free) · **Register:** Teardown
**Framing:** Liam asks Claude what feedback Professor Bear would give the student. **First name only** — "Saloni", "Professor Bear" / "Bear". Never the surname.
**One idea:** *In Computational Skepticism the skepticism has to be load-bearing, not decorative — the test of Saloni's checker is whether it names its target, gates work authorization instead of scoring it, breaks under realistic perturbation, and shows its own uncertainty.*

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "What would Professor Bear tell Saloni about her Job Application Priority Checker?" → ask answered, Liam signs in
ACT I    The Reasonable Trap    a good pitch that skips the hard problems          (B01 PredictCard, B02 Manim three-problems)
ACT II   Name the Target        "prioritize" by what? + explicit weighted score    (B03 Manim divergence, B04 VOX, B05 ask→ B06 Onda code, B07 Manim mechanism-vs-posthoc)
ACT III  A Gate, Not a Feature  work-auth = hard eligibility gate + data confidence (B08 Manim threshold, B09→B10 VOX run R1, B11 ask→ B12 Onda code, B13 Manim grade-source)
ACT IV   Make It Break          real robustness tests                              (B14 Manim near-threshold, B15 ChipGrid, B16 VOX drawon)
ACT V    Honest Pictures        false precision + show weights/uncertainty         (B17 Manim false-precision, B18 illustration)
ACT VI   Load-Bearing Skepticism transparent ≠ correct; Reallocation-Engine nod    (B19 illustration)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (five notes)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — the reviewer prompt, read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — "Claude, Skeptical"
```

## Lane histogram (body beats only; bookends + ask micro-beats exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 4 | 17.4% | 20–25% | passes the hard vox lint (15–30% clear); toward low end |
| MANIM | 7 | 30.4% | 25–40% | ✓ |
| REMOTION | 6 | 26.1% | 30–45% | slightly light — a builder may promote one segment card to a REMOTION spark-illustration |
| CARD | 6 | 26.1% | remainder | 6 segment cards (one per act) |

Body beats: 23 · ASK micro-beats B05/B11 precede the two Onda code blocks (ASK→RESULT). Est. runtime ≈ 5:00 (measured audio is the only clock).

## ASK→RESULT pairs
- B05 → B06: ask for `priority_score` → the Onda code-block.
- B11 → B12: ask for the sponsorship gate → the `sponsorship_compatibility` Onda code-block.

## Vox run
- **R1 (B09→B10):** the OPT/eligibility clock → the ranking it quietly corrupts. One continuous move; handoff block authored in the sheet.

## Honesty / DOUBLE-CHECK
- Real code only in the Onda blocks (the two functions from the source, lightly tidied). No invented metrics.
- Immigration terms (F-1, OPT/CPT/STEM OPT, H-1B, USCIS) carried as the *mechanism* of the eligibility gate — the point of the episode — not as datable trivia.
- Rudin (2019) "Stop Explaining Black Box ML Models" underlies B07/B19 (mechanism > post-hoc); cited in SOURCES.md, not name-dropped on screen.
- **First name only** enforced across every beat; no student surname anywhere.

## Gates — UNATTENDED slate-cut run
Author authorizes the gates in advance. Target deliverable = **Gate D1 full-length SLATE PREVIZ** (real Kokoro audio, real Manim/Remotion, slates in the 4 vox slots B04/B09/B10/B16), `--review` burn-in, watchable MP4. Stop there for review — no pantry sourcing, no `final`, never publishes.
