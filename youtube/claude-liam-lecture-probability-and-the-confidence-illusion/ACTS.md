# ACTS — Probability and the Confidence Illusion (Lecture 2 of 13)

**What.** The coverage map of the whole chapter into ten acts, with the cast per act, every merge-conflict decision, the deck-versus-chapter differences and what was left out.
**Why.** WHOLE-SOURCE LAW: every section is in an act or in LEFT OUT with a reason; nothing is dropped silently.
**Found.** All of the chapter's teaching prose is covered. Six unresolved merge blocks, all resolved to the HEAD side (one teaching point lost: Alice's Markov chain). Five facts in the chapter needed correction or qualification (FACTCHECK.md).

Source (read only, never edited): `/Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md` (731 lines).

## Coverage map

| Source section | Act | Beats | Treatment |
|---|---|---|---|
| Opening (the 0.94 column) and "Why this chapter" | I · A Number That Looks Like a Fact | A1, B01–B05 | The column of scores drawn, the "formatted to look like facts" point, the gap between radiated and earned confidence, plausibility auditing defined in one sentence, the three tools |
| What probability actually is; The three axioms; Classical and frequentist probability | II · Probability Is a Degree of Belief | A2, B06–B14 | Bit becomes dial; two engineers (Professor Bear portraits); die sample space; axioms as MathTex; coin-frequency convergence from a seeded run; Bayesian as belief updating |
| Conditional probability; The multiplication rule; the agent tool-call chain; the independence paragraph; The total probability theorem; the fleet's error rate | III · Conditioning and the Chain | A3, B15–B24 | Venn shrink; the triage log (0.30 / 0.76 recomputed); chain tree 0.612; independence 0.729; partition strip 3.2% |
| The test that is 99% accurate | IV · The Ninety-Nine Percent Test | A4, B25–B30 | Predict beat; Casscells study; the 10,000-dot grid; false positives; 1 in 101; wrong direction |
| Bayes' theorem; The inference interpretation; factory/fleet revisited; the precision note (HEAD, block 3) | V · Bayes Runs Backward | A5, B31–B35 | Formula; the real script run; the 98-fold lift; sensitivity versus specificity; the fleet inverted (25/28/47) |
| The false-positive structure is everywhere; Glimmer 2.3 | VI · Rare Events Everywhere | A6, B36–B40 | PPV against base rate (computed); domains; alert fatigue; the sepsis external validation (Wong et al.) |
| From Boolean to probabilistic | VII · Every Number Is a Claim | A7, B41–B42 | Output as conditional claim; the three conditions on 0.87 |
| Hume's induction problem, re-translated as distribution shift | VII | B43–B47 | Hume; training set as past; blind confidence; DeGrave et al. (corrected); the track-record question |
| Calibration; Glimmer 2.4; The calibration baseline | VIII · Calibration | A8, B48–B57 | 700 of 1,000; reliability diagram; our own seeded simulation; Guo et al.; temperature scaling and the fitted T; separability; staleness; the reject condition; human 90% intervals |
| When the Central Limit Theorem politely declines to help; Glimmers 2.1–2.2; Exercise 10 | IX · When Averages Stop Settling | A9, B58–B63 | CLT's two requirements; Gaussian versus Cauchy running means (seeded); constructed loss costs; tail-aware metrics; the admission that tails cannot be estimated up front |
| Synthesis (four questions); What would change my mind | X · Four Questions | A10, B64–B66 | Interpretation errors; the four questions; the open edge (Rabanser et al.) |
| Chapter summary | BVDT | recap | Six bare lines, nothing new |
| LLM Exercise (Agentic Red-Team Casebook) | BHTF | Your Turn | Not covered as itself: a different, pasteable audit prompt that uses the lecture's main idea (see LEFT OUT) |

## Cast per act (recurring objects)

| Act | Cast |
|---|---|
| I | the column of scores; a ruler stamp; a radiated bar and an earned bar |
| II | a bit that opens into a dial; a die and its tray of six tiles; two portraits |
| III | a hundred case squares; the probability tree; the 40/30/30 strip |
| IV, V | the 10,000-dot grid (one sick dot, ringed); the positive pool; the same strip for the fleet |
| VI | the PPV curve with its marker; alert tiles |
| VII | a plate on three supports; two bell curves (past, future); the confidence readout |
| VIII | the diagonal and the five bins; the T knob |
| IX | two running-mean traces; ten-dollar blocks and one huge block |
| X | four marks, one from each earlier tool |

## SOURCE CONFLICTS (six merge blocks; the chapter file is never edited)

| # | Lines | HEAD says | Other side (d78899b "Update chapters 1-14") says | Used | Why |
|---|---|---|---|---|---|
| 1 | 158–177 | The independence mistake: independent steps at 0.9 give 0.729 against the honest 0.612, "twelve points of unearned confidence", failures cluster so the error is optimistic | A card-drawing chain 39/52 · 38/51 · 37/50 ≈ 0.413 with a different Figure 2.2 caption, then a short independence definition | HEAD | Real conflict. HEAD is the course-layer version, agrees with the figure above the block (the agent tree) and with Exercise-style text; the card chain contradicts that figure. The independence definition appears in HEAD too, so nothing is lost |
| 2 | 205–234 | "3.2% of outputs are wrong"; hold the partition, run it backward later | "Overall, 3.2% defective", then Alice's two-state Markov chain (P(U2)=0.72, P(U3)=0.688, Figure 2.4) | HEAD | Real conflict. HEAD lacks the Markov-chain worked example. It is a preview ("you will see it again") that no later passage uses, and the fleet framing in HEAD is the one Exercise 14 builds on. Markov chains are logged under LEFT OUT |
| 3 | 258–266 | A precision note: "99% accurate" is doing double duty as sensitivity and specificity; full Figure 2.5 caption | Only a truncated Figure 2.5 caption ("…10,000 dots arranged as a") | HEAD | HEAD has a teaching point the other side lacks (B34) |
| 4 | 391–395 | Figure 2.7 caption: the model does not update its confidence when the world moves | Caption "Two overlapping bell curves on a shared x-axis" | HEAD | Differ only in a figure caption: not teaching prose. The beat (B45) draws both ideas |
| 5 | 457–461 | Figure 2.9 caption: the next observation can move the average dramatically | Caption "Two distributions overlaid on the same x-axis" | HEAD | Differ only in a figure caption: not teaching prose |
| 6 | 637–731 | "Preview of next chapter": the next chapter is a Data Frame Audit | A different preview (bias, causal graphs), then the "AI Wayback Machine" (Frank Ramsey, a Run-this prompt), and the D3 figure "Prompts" block | HEAD | End matter, not teaching prose; none of it is spoken. Ramsey's account of subjective probability is a related aside that HEAD lacks; it is optional and its inclusion would add a historical claim to verify, so it is left out and logged here for Bear |

**Leftovers from the other side outside the blocks.** "Worked example — factory revisited" (machine A/B/C, "from the manufacturing example above") sits in HEAD territory but is the other side's wording; the numbers are identical to HEAD's fleet (40/30/30; 2/3/5). The film uses the HEAD framing (three model versions in a fraud-screening pipeline). The term table prints the posterior as 0.0099 while the formula prints 0.0098: the film shows both and says why (B32).

**For Bear to resolve in the chapter:** blocks 1 and 2 (whether the card-drawing chain and Alice's Markov chain stay), and the factory/fleet naming drift; the film does not decide for the chapter.

## DECK vs CHAPTER

The Lecture 2 deck folder holds no deck: `deck_plan.starter.json` is a regex skeleton (58 slides, 156 TODOs), a packet and a pool of the chapter's figures. It was used for section order only.

| The skeleton had | The chapter has | Film |
|---|---|---|
| Section order: objectives, prerequisites, why, probability, conditional, multiplication, total probability, 99% test, Bayes, Boolean to probabilistic, Hume, calibration, CLT, calibration baseline, synthesis, what would change my mind, connections, summary | the same order | followed |
| "This exercise returns in Chapters 8 and 14" | "Chapters 4 and 13" | neither spoken (cross-references are banned) |
| Figures 2.1–2.11 as candidate assets | the same figures | rebuilt as moving beats; none pasted |

## LEFT OUT (with reasons)

| Item | Reason |
|---|---|
| Learning objectives, prerequisites, "Connections forward", Chapter summary as a section | Navigation and apparatus, no independent teaching; the summary becomes BVDT |
| The classical/frequentist/Bayesian table's "key limitation" column | Said in the narration of B12–B14 in one clause; not a table beat |
| Alice's two-state Markov chain | Other side of block 2; a preview the chapter never uses |
| Frank Ramsey / AI Wayback Machine, D3 "Prompts" | Optional end matter, other side of block 6 |
| The base-rate-by-domain table's numeric ranges (~0.1–1% etc.) | The chapter gives them without a source; not spoken or shown as facts (B37 names the domains only) |
| Glimmers 2.1–2.4, the calibration-baseline exercise, Exercises 1–16, the LLM Exercise (Red-Team Casebook) | Practice and apparatus. Their computations are folded in as worked beats where they teach the main idea (Cauchy run, PPV against base rate, the T fit, intervals). The Red-Team Casebook depends on an earlier project, so the Your Turn is a self-contained audit prompt instead |
| "Ash" case and Chapter-1 references (plausibility auditing is defined in one sentence in B04; the triage system, fluency trap and the Epic product name are not used) | SELF-CONTAINED LAW |
