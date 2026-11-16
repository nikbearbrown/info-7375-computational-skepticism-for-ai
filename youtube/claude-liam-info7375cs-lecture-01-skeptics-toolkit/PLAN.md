# PLAN — claude-liam-info7375cs-lecture-01-skeptics-toolkit
deep-explainer · claude-liam · Liam in for Bear (Kokoro am_onyx) · Claude skin · Teardown register · COURSE FILM
Written 2026-09-09. GATE: Bear approves by launching BUILD-PROMPT.md.

**Film title (exact, restated on the outro):** The Skeptic's Toolkit
**Course credit:** per `../LECTURE-CREDIT.md` — Lecture 1 · INFO 7375 · Computational Skepticism for AI · Nik Bear Brown ·
Northeastern University. Card at B02; spoken in B00 and B02; composer topic `INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1`.
**Slug / folder:** `claude-liam-info7375cs-lecture-01-skeptics-toolkit/` (supersedes `claude-liam-deep-01-skeptics-toolkit/`,
whose seven-act cut and staged claims this plan inherits)
**Source:** `chapters/01-the-skeptics-toolkit.md` (HEAD side of the merge markers)
**Greeting:** "Aloha, Liam" — unused across the tree on 2026-09-09.
**Runtime:** an output; ~10 min expected (≈ 46 beats). Bear accepts ~10.
**Audience:** INFO 7375 students (Fall 2026) — smart, may not know the philosophy names; every name is earned on screen
by its MOVE, never by biography.

## The misconception → correction (B01 hesitant writer, ≤ 4 lines)
```
A sepsis model missed two of every three patients.
So the model was broken.
It passed every test its builders chose.
The test was the thing that failed.
```
`triggerWords: "broken"`, `replacementWords: "working"` — line 2 becomes "So the model was working." on Liam's spoken
correction. mistakeRate 5, charMs 32, hesitateBetween 8, hesitateWithin 1, fontSize 64, seed = slug.

## Framework (B03, before Act I)
The gap: **statistically valid → wrong about the question that mattered.** Drawn as ARTIFACT | WORLD with a slot
labelled RELATIONSHIP between them; the four moves are four questions that probe the slot; the five capacities are who
asks them. Returns in Act V (the cave) and Act VII (capacities) as worked examples.

## Act map (lanes: manim unless noted; act cards are FormACard, narrated "Act one. …")

| Beat | Act | Lane | What the viewer watches | SEED |
|---|---|---|---|---|
| B00 | cold open | remotion ClaudeComposerAsk | "Aloha. This is Liam, in for Bear, with lecture one of Computational Skepticism for AI." Ask: *A sepsis model ran in hundreds of hospitals and passed every test. Then someone checked it against the patients. What went wrong?* Output: "Nothing, by the builders' measures." / "It missed two of every three." / "The gap between those sentences is the course." | 2–6 |
| B01 | BLUF | remotion BrutalistHesitantWriter | the four lines; broken → working | — |
| B02 | credit | **card FormACard (light)** | `INFO 7375 · Computational Skepticism for AI` / `Lecture 1 — The Skeptic's Toolkit` / meta `Nik Bear Brown · Northeastern University`; Liam: "This is lecture one of INFO 7375, Computational Skepticism for AI, at Northeastern University. The reading is chapter one." | 1 |
| B03 | framework | manim | ARTIFACT / WORLD / RELATIONSHIP slot; four question-marks land; "who asks" row | — |
| B04 | I card | card | Act I — Two Failures That Passed | — |
| B05 | I | manim isotype | 27,697 patients; three figures, two ghosted: missed 67% ("two of every three") | 2, 3 |
| B06 | I | manim bars | alerts on 18% of all hospitalized patients; AUC 0.63 as a dial that barely leaves 0.5 | 4, 5 |
| B07 | I | manim two-column | "By every measure the builders chose: succeeded" vs "At the bedside: missed two of three" — the title of the film's problem | 2–6 |
| B08 | I | manim | the agent case, as the paper tells it: an agent named Ash is asked to delete an email holding a secret → it has no delete tool → it runs a "nuclear" reset of its own mail setup → REPORTS "reset completed", secret deleted → the owner opens the mailbox on the provider and the email is still there. Four tiles: ASKED · DID · REPORTED · STATE; the report/state gap flashes; caption "You broke my toy." | 7, 8 |
| B09 | I | manim | one patient, a composite: score LOW-ACUITY lands; the wait; the clot moves (schematic body outline, one terracotta dot travelling leg → lung) — "this is what one missed case looks like from the inside" | 9 |
| B10 | I | manim statement | Statistically valid. **Wrong about the question that mattered.** | — |
| B11 | II card | card | Act II — Descartes: What Would Have to Be True? | — |
| B12 | II | manim | the move as a checklist: "training data underweighted cases like this" / "input features miss the signal" / "deployment context ≠ validation context" — three checkboxes land on the spoken conditions | 23 |
| B13 | II | manim | Knight Capital: 8 server tiles, 7 update, 1 does not; a flag flips; "Power Peg" wakes; a 45-minute bar fills; 4 million executions · 154 stocks · ≈ $440M | 10, 11 |
| B14 | II | manim statement | "Deployment succeeded." ≠ **"The system is doing what we intend."** | — |
| B15 | III card | card | Act III — Hume: The Turkey With a Spreadsheet | — |
| B16 | III | manim line | the turkey: confidence rises for 999 days; day 1,000 the line drops to zero — one axe mark | 12 |
| B17 | III | manim | correlation vs mechanism: the model learned the pattern, not the cause; population shifts, a new pathogen, a changed neighbourhood — three arrows the model cannot see | 23 |
| B18 | III | manim bars | Zillow: Q3 write-down ≈ $304M + $240–265M expected → "more than half a billion"; ~25% of staff; "thousands of homes" | 13, 14 |
| B19 | III | manim | Google Flu: 108 week cells, 100 lit — over-predicted in 100 of 108; "big data hubris" quote card line | 15, 16 |
| B20 | III | manim statement | The model's confidence is a property of the model. **Not of the world.** | — |
| B21 | IV card | card | Act IV — Popper: Try to Break It | — |
| B22 | IV | manim | white swans accumulate on the left forever; one black swan on the right ends it — the asymmetry drawn | 23 |
| B23 | IV | manim two-column | rhetoric → engineering: "the system is robust" → the threshold sentence (four rows, tagged *illustrative thresholds*) | 19 |
| B24 | IV | manim | the test the sepsis model never got: internal validation (white swans, counted) vs external validation (the black-swan test, run by another health system) — "unrefuted is not validated" | 2–6 |
| B25 | V card | card | Act V — The Cave, and the Fluency Trap | — |
| B26 | V | manim | the three questions land in the framework slot: what is the artifact · what is the world · what is the relationship | — |
| B27 | V | manim | X-ray shortcut: a radiograph outline; the model's attention ring lands on the corner marker, never the lungs; "appear accurate, but fail when tested in new hospitals" | 17 |
| B28 | V | manim two-column | COMPAS in the same anatomy: artifact = a number · world = a person's future · relationship = arrest data shaped by who gets policed | 18 |
| B29 | V | manim | the fluency trap, two stages: fluency → confidence in the output → confidence in your own evaluation; a second arrow that should not exist takes the accent | 22 |
| B30 | V | manim | form vs content: two sliders that move independently — "a sentence can be maximally fluent and maximally wrong" | 22 |
| B31 | V | manim statement | Do not let fluency do epistemic work. **Specify the wrong answer before you read.** | — |
| B32 | VI card | card | Act VI — Cheap to Produce, Expensive to Verify | — |
| B33 | VI | manim bars (schematic, no numerals) | classic asymmetry (factor: hard / multiply-check: easy) flips to the AI deployment asymmetry (produce: milliseconds / verify: an hour of senior labor) | 20 |
| B34 | VI | manim statement | If you do not budget for verification, you will not get verification. **"Automate the checking" is another model, one layer up.** | — |
| B35 | VII card | card | Act VII — Five Ways to Watch | — |
| B36 | VII | manim rows | the five capacities land on the spoken names with a one-line "what failure looks like" each | 21 |
| B37 | VII | manim | problem formulation, the load-bearing one: "what is the statistical category?" (answered well) vs "does this patient have a life-threatening condition?" (never asked) | 21 |
| B38 | VII | manim | skepticism as architecture: the workflow with the moves written into the checklist, the dashboard, the handoff — "where in the workflow, by whom, seeing what" | — |
| B39 | VII | manim | Ash returns — the agent from Act I is the shape of every agentic failure: a report true about the local machine, false about the system. The pebble: the agent YOU will red-team, dropped in lecture one, rippled through every lens by lecture thirteen (chapter numbers spoken; course film) | 7, 8, 24 |
| B40 | VII | manim statement | Four moves. One asymmetry. Five capacities. **One trap.** | — |
| BVDT | verdict | remotion ClaudeVerdictArtifact (6 lines) | heading `INFO 7375 · Lecture 1`: *Valid by the builders' measures; wrong at the bedside.* · *Doubt: what would have to be true for this to be wrong?* · *Induction: confidence belongs to the model, not the world.* · *Falsify: a claim that cannot fail is not a claim.* · *Cave: artifact, world, relationship.* · *Verification is the budget. Fluency is the trap.* | — |
| BHTF | your turn | remotion ClaudeComposerAsk "Your turn.", topic `INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1` | the chapter's exercise, compressed: *Help me pick one agentic AI system to red-team across this course — it must take real actions, be something I can run or study from primary sources, have a real blast radius, and be safe to poke. For one observed interaction, run the four moves: what would have to be true for its report to be wrong; what in deployment differs from training; what observation would falsify its claim; what is the artifact versus the world. Then name which of the five supervisory capacities its failure would most need.* Output lines: "Prediction-lock before you observe." / "Write the System Dossier paragraph." / "Bring the agent to lecture two." | 24 |
| BOUT | outro | remotion ClaudeTitleOutro | `The Skeptic's Toolkit` · @NikBearBrown · no subline | — |

Lane histogram (body B03–B40, 38 beats): manim 31 (82%) · card 7 (18%) · vox 0 · remotion body 0.
VOX: none — no still in this chapter IS the evidence (the paper first pages and the AI-generated Popper portrait are
decoration or banned). Quota lint FAILs by design; log the override (Bear's rule 2026-09-02).

## Teaching arc (CHECKS-REPORT before the slate)
FRAMEWORK B03 ✓ · WORKED EXAMPLES B24 (Popper on the sepsis model), B27/B28 (the cave on two cases) ✓ · FALSIFIABILITY
B23 (rhetoric→engineering) + the chapter's own "what would change my mind" carried into the verdict's last line ✓ ·
SCAFFOLDED TASK BHTF (the course exercise) ✓ · BOOKENDS ✓ · NO-SOURCE-NO-VERDICT: every number beat has a SEED row ✓.

## Quote budget
≤ 15 words per quote card: "appear accurate, but fail when tested in new hospitals" (row 17); "big data hubris" (row 15);
"reported successful completion … while the underlying system state contradicted its claims" (row 7, trimmed to ≤ 15).
