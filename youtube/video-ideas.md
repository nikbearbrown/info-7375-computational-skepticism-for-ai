# Computational Skepticism for AI Video Ideas

## Assignment crosswalk (read first)

Every concept video below is a **lens a student runs in an assignment.** Map each to the graded work:

- **A1 — The Agentic Casebook: Red-Team One System** (100 pts, AUDIT): pick 3 of 10 lenses on a real
  agentic system. Each video below *is* one of those lenses, taught once.
- **A2 — Build It, Then Break It** (100 pts, BUILD): 2 of 6 instruments on your own artifact.
- **PR25 — Progress Report** (25 pts, brutalist explainer) and **CAP250 — Working Professional
  Contribution to the Reallocation Engine** (250 pts): the verified-data contract, the honest run, the
  gate-behavior discipline.

**Series 1 (Candidates 01–28) → assignment lens:**

| Cand | Video | Serves |
|---|---|---|
| 01 | 99%-accurate test | **A1** Ch2 base-rate lens |
| 02 | more data, more confident | **A1** Ch6 bias lens (biased estimator) |
| 03 | fair three ways at once | **A1** Ch7 fairness lens · **A2** fairness instrument |
| 04 | missing-values check ran clean | **A1** Ch3 data-frame lens · **A2** data-frame instrument |
| 05 | invisible million-pixel flip | **A1** Ch4 robustness lens · **A2** robustness probe |
| 06 | the agent said "done" | **A1** Ch8 false-success lens (the anchor case) |
| 07 | turkey's model | four moves (**Hume**) · A1 limits |
| 08 | two AIs, one blind spot | **A1** Ch12 accountability (common-cause) |
| 09 | one data point beats the average | **A1** Ch2 (heavy tails / CLT) |
| 10 | accurate model lies at 99% | **A1** Ch2+11 calibration · **A2** calibration |
| 11 | fluent answers make you worse | the fluency trap (premise of A1 + A2) |
| 12 | fixing the model didn't fix bias | **A1** Ch6 bias-leverage lens |
| 13 | a prediction you can edit | the **prediction-lock** (graded honesty in A1 + A2) |
| 14 | the study method that feels best | frictional/learning (meta; least assignment-tied) |
| 15 | fair credit-splitting (Shapley) | **A1** Ch5 explainability lens (SHAP) |
| 16 | the AI wasn't lying: "deleted" | **A1** Ch5 explainability (language-game) · Ch8 |
| 17 | honest about what it learned | **A1** Ch4 (features-not-bugs) · **A2** robustness |
| 18 | lie with a chart, same numbers | **A1** Ch10 honest-viz lens · **A2** honest-viz instrument |
| 19 | prompt injection can't be patched | **A1** Ch8 agentic lens · robustness |
| 20 | validated at 1%, fails at 30% | **A1** Ch8 agentic (multi-agent failure) |
| 21 | the better it works, the worse you watch | **A1** Ch9 delegation / trust-calibration lens |
| 22 | perfectly calibrated, perfectly useless | **A1** Ch11 (calibration vs. resolution) · **A2** |
| 23 | the average that hides the patient | **A1** Ch11 subgroup · Ch2 |
| 24 | missing data that lies about itself | **A1** Ch3 data-frame (MNAR) |
| 25 | deleting the race column | **A1** Ch7 fairness (proxy / FTU is hollow) |
| 26 | the impersonator the agent believed | **A1** Ch8 false-success lens |
| 27 | five culprits and no culprit | **A1** Ch12 accountability lens (distribute responsibility) |
| 28 | a provable guarantee | **A1** Ch11 (conformal prediction) |

**Series 2 (the wild-example bank — "Hot Ones," "Rap Music graph," etc.)** is a case bank for **A1 Pebble
selection** and **A2 honest-viz**: base-rate examples (fingerprint match, positive test, antidepressant
iceberg), misleading-chart examples (flipped gun-death axis, moving the bins, dangerous-city map,
Tim Cook's chart), collider/selection examples (Hot Ones jerks), and shortcut-learning examples (the
wolf/snow detector, criminals-were-really-smiles). Point students here when they need a *real* system or
chart to red-team.

**Assignment-native candidates** — the videos that teach the assignment discipline itself, not a chapter
concept — are appended at the end of this file (Candidates N1–N4).

slate cut 

## Candidate 01 — Why a 99%-Accurate Test Is Almost Always Wrong When It Says Yes
- Source: `books/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Manim visualization
- Hook: A test that is 99% accurate just came back positive — and the patient is almost certainly fine.
- Core idea: When the condition is rare, the tiny error rate applied to the enormous healthy population manufactures a hundred false positives for every true one, so the positive pool is mostly noise.
- Visual object: A 10,000-dot population grid being swept by the test, flagged dots pooling into a positives bucket
- Manim move: split
- Short-form fit: Strong
- Prerequisites: percentages, what a false positive is
- Exclusions: no Bayes' theorem formula or derivation, no sensitivity/specificity vocabulary, no odds-form shortcut, no second domain example (fraud/security/moderation list stays in the book)
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-99-percent-test/vox-99-percent-test-review.mp4`

slate cut 

## Candidate 02 — Why More Data Makes the Wrong Answer More Confident
- Source: `books/computational-skepticism-for-ai/chapters/03-bias-where-it-enters-and-who-is-responsible.md`
- Production mode: Manim visualization
- Hook: The biggest poll in American history — 2.4 million responses — confidently predicted the loser.
- Core idea: A biased estimator converges as data accumulates, but it converges to the wrong value — more samples shrink the scatter around a systematically offset target, so scale buys precision, never correction.
- Visual object: A scatter of sample estimates tightening around a bullseye that sits off-center from the true value
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: sampling, averages
- Exclusions: no bias-variance decomposition, no E[θ̂] notation beyond a single label, no taxonomy of the ten bias mechanisms, Literary Digest gets one line of history and no more
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-more-data-more-confident/vox-more-data-more-confident-review.mp4`

slate cut 

## Candidate 03 — Why No Algorithm Can Be Fair Three Ways at Once
- Source: `books/computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`
- Production mode: Manim visualization
- Hook: Three definitions of fairness, each obviously reasonable — and a theorem says your model cannot satisfy them all at once.
- Core idea: When two groups have different base rates, forcing the score to mean the same thing in both groups algebraically forces the error rates apart — every threshold move that fixes one metric visibly breaks another.
- Visual object: One decision threshold sliding across two group score-distributions with live TPR/FPR/PPV dials
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: probability as a rate, false positive vs true positive, base rate
- Exclusions: no Chouldechova algebra derivation, no COMPAS litigation history, no individual/counterfactual fairness, no GE index, no debiasing toolkit
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-fair-three-ways/vox-fair-three-ways-review.mp4`

slate cut 

## Candidate 04 — Why the Missing-Values Check Ran Clean on a Broken Dataset
- Source: `books/computational-skepticism-for-ai/chapters/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md`
- Production mode: Mixed
- Hook: The EDA was spotless and the model still failed in production — because the fatal rows were never there to look missing.
- Core idea: A join silently drops rows that fail to match on a messy identifier, the drop concentrates in one subpopulation, so the model never sees them in training and fails on exactly them in deployment.
- Visual object: Rows from three source tables flowing into a join funnel, with unmatched rows falling away unseen
- Manim move: split
- Short-form fit: Strong
- Prerequisites: dataset as a table, joining on an ID, training vs deployment
- Exclusions: no SQL join taxonomy (inner/left/outer), no MCAR/MAR/MNAR definitions, no six-step interrogation procedure, no imputation methods
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-silent-join/vox-silent-join-review.mp4`

slate cut 

## Candidate 05 — Why an Invisible Change Can Flip a Million-Pixel Answer
- Source: `books/computational-skepticism-for-ai/chapters/08-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`
- Production mode: Manim visualization
- Hook: No single pixel changed enough for you to see — yet the model's answer flipped from "panda" to "gibbon" with even higher confidence.
- Core idea: In high dimensions a tiny push on every coordinate, each aligned with the model's weights, accumulates across thousands of dimensions into a decisive activation shift — imperceptible per pixel, overwhelming in sum.
- Visual object: A grid of pixel-coordinates each nudged by a sliver ε, feeding a running activation bar that climbs past the decision threshold
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: image as numbers, weighted sum, decision threshold
- Exclusions: no FGSM/PGD equations beyond the sign-of-the-gradient intuition, no L∞/L1 norm formalism, no boundary-tilting second account, no defense toolkit survey
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-invisible-flip/vox-invisible-flip-review.mp4`

slate cut 

## Candidate 06 — The Agent Said "Done" — and Its Own Report Was Wrong
- Source: `books/computational-skepticism-for-ai/chapters/09-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Doodle
- Hook: An AI agent reported "email account RESET completed," destroyed its owner's email infrastructure in the process — and the email it was asked to delete still existed.
- Core idea: The agent had no model of the gap between its action's actual scope (wiping the local client) and the task's completion condition (deleting from the server), so its completion report tracked its own local state, not the world's.
- Visual object: Two parallel tracks — the agent's picture of the world and the world itself — drawn side by side and diverging step by step until "task complete" sits above an untouched email
- Manim move: split
- Short-form fit: Strong
- Prerequisites: what an AI agent is (chatbot with tools), email client vs. email server
- Exclusions: no OpenClaw architecture, no Mirsky autonomy levels, no four-category taxonomy, no other Agents-of-Chaos cases, no responsibility/liability discussion
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-agent-said-done/vox-agent-said-done-review.mp4`

slate cut 

## Candidate 07 — Why the Turkey's Model Was Perfect Until Thanksgiving
- Source: `books/computational-skepticism-for-ai/chapters/14-the-limits-of-ai-what-the-tools-cannot-do.md`
- Production mode: Mixed
- Hook: Every single day of data made the turkey more confident — and more wrong.
- Core idea: A model's competence is over its data, not the world; evidence sampled inside a smooth regime raises confidence monotonically while saying nothing about the event that ends the regime, so the confidence curve and the true risk diverge until the cliff.
- Visual object: The turkey's confidence curve, traced upward one feeding-day at a time toward day 1,001
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: averages, the idea of a confidence estimate
- Exclusions: no Mediocristan/Extremistan taxonomy (separate candidate), no Hume/induction history, no distribution-shift formalism, no medical-AI second example — one turkey, one curve, one cliff
- Score: 9/10

slate cut 

## Candidate 08 — Why Two AIs Checking Each Other Is One Blind Spot Twice
- Source: `books/computational-skepticism-for-ai/chapters/13-accountability-who-is-responsible-when-the-system-fails.md`
- Production mode: Doodle
- Hook: Adding a second AI to check the first feels like a safety net — but it's the same net with the same hole.
- Core idea: Common cause failure — a checker trained on the same data with the same architecture has correlated blind spots, so the exact error most likely to fool the generator sails through the monitor too; a real check must come from outside the shared foundation.
- Visual object: Two sieves with holes in the same place, and the one bad grain that falls through both
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: what a language model is (roughly), the idea of redundancy
- Exclusions: no Gödel incompleteness formalism (the sieve carries the logic), no seven-tier taxonomy, no chain-of-thought-monitoring literature, no FDA/aviation case histories beyond one spoken aside
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-same-net-same-hole/vox-same-net-same-hole-review.mp4`

slate cut 

## Candidate 09 — Why One Data Point Can Beat Your Thousand-Point Average
- Source: `books/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Manim visualization
- Hook: You have averaged a thousand observations, and the very next one can move that average more than all thousand combined.
- Core idea: The Central Limit Theorem requires finite variance; in a heavy-tailed world the running mean never settles, because rare extreme events keep arriving with enough weight to drag it — so any average-based safety metric is measuring a quantity that does not converge.
- Visual object: A running-average line being repeatedly yanked by incoming data points that never stop mattering
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: mean/average, informal idea of a distribution
- Exclusions: no proof that the Cauchy mean is undefined, no CLT statement in full, no confidence-interval formulas, no power-law taxonomy (wealth/earthquakes list stays in the book)
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-heavy-tail-yank/vox-heavy-tail-yank-review.mp4`

slate cut 

## Candidate 10 — Why an Accurate Model Can Still Lie Every Time It Says 99%
- Source: `books/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- Production mode: Manim visualization
- Hook: A model can score 94% accuracy and still be wrong about how sure it is — and the accuracy number will never tell you.
- Core idea: Calibration is a claim about long-run frequencies — bin the model's stated confidences, let outcomes pile up in each bin, and the empirical curve peels away from the diagonal exactly where the model overclaims.
- Visual object: A reliability diagram building itself from prediction dots piling into confidence bins
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: probability as a confidence statement, accuracy
- Exclusions: no ECE or Brier formulas, no temperature-scaling or softmax mechanics, no human-forecaster calibration tangent — one model, one curve
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-calibration-curve/vox-calibration-curve-review.mp4`

slate cut 

## Candidate 11 — Why Fluent Answers Make You Worse at Checking Them
- Source: `books/computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md`
- Production mode: Doodle
- Hook: The better an AI answer reads, the worse you become at evaluating it — and you feel yourself getting better.
- Core idea: Fluency is a two-stage trap — it boosts your confidence in the output, then boosts your confidence in your own judgment of the output, because form and content are generated independently in AI text and the old human heuristic linking them is broken.
- Visual object: A reader's confidence gauge that a well-formed sentence pumps up twice — once for the answer, once for the reader's own judgment
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: has used a chatbot
- Exclusions: no Botspeak framework or pillar vocabulary, no LLM architecture explanation, no prompt-engineering tips, no Ash case retelling beyond one beat — stay with one reader and one sentence
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-confidence-gauge/vox-confidence-gauge-review.mp4`

slate cut 

## Candidate 12 — Why Fixing the Model Didn't Fix the Bias
- Source: `books/computational-skepticism-for-ai/chapters/03-bias-where-it-enters-and-who-is-responsible.md`
- Production mode: Mixed
- Hook: Two expert teams fixed the model and fixed the data, and the bias barely moved — a third team touched neither and cut it tenfold.
- Core idea: Bias flows from attribute to outcome along multiple parallel paths, and an intervention only blocks the path it sits on — plug one pipe and the flow keeps running through the proxy and deployment-context paths you left open, so leverage means finding the path carrying the most flow.
- Visual object: A pipe-graph from protected attribute to outcome with bias visibly flowing, rerouting each time one path is blocked
- Manim move: block (flow reroutes around each blocked path)
- Short-form fit: Medium
- Prerequisites: informal cause-and-effect graphs, what a biased outcome means
- Exclusions: no Pearl do-calculus notation, no ten-mechanism taxonomy, no fairness metrics, cap the graph at 6 nodes — the three teams are one sentence each, not three scenes
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-bias-pipe/vox-bias-pipe-review.mp4`

slate cut 

## Candidate 13 — Why a Prediction You Can Edit Is Worth Nothing
- Source: `books/computational-skepticism-for-ai/chapters/04-the-frictional-method-evidence-of-learning-when-ai-can-generate-the-artifact.md`
- Production mode: Doodle
- Hook: Written before the result, a guess is evidence; editable after, the identical sentence proves nothing.
- Core idea: The information lives in the gap between prediction and outcome — leave the prediction unlocked and it slides to meet the result, collapsing the gap that could have taught you to zero.
- Visual object: A prediction pin and an outcome pin with a measurable gap between them, and a lock that decides whether the gap survives
- Manim move: collapse
- Short-form fit: Strong
- Prerequisites: making a guess, seeing a result
- Exclusions: no seven-move framework, no GLP components, no neuroscience (dopamine/BDNF), no journal grading or failure-mode taxonomy
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-prediction-lock/vox-prediction-lock-review.mp4`

slate cut 

## Candidate 14 — Why the Study Method That Feels Best Teaches the Least
- Source: `books/computational-skepticism-for-ai/chapters/04-the-frictional-method-evidence-of-learning-when-ai-can-generate-the-artifact.md`
- Production mode: Manim visualization
- Hook: The smoother learning feels, the less of it sticks — the confused student is often the one actually learning.
- Core idea: Performance and learning run on different clocks — fluent conditions spike immediate performance that decays, friction builds storage strength that persists, and the two curves cross once weeks pass (compressed here into seconds).
- Visual object: Two performance curves ("fluent" vs "frictional") on a shared time axis, decaying and crossing as time fast-forwards
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: studying and memory, reading a line chart
- Exclusions: no neurobiology cascade (dopamine, BDNF, dendritic spines), no Y1–Y7 formalism, no Frictional-journal apparatus, no spacing-effect experimental-design detail
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-two-clocks/vox-two-clocks-review.mp4`

slate cut 

## Candidate 15 — Why Fair Credit-Splitting Has Exactly One Answer
- Source: `books/computational-skepticism-for-ai/chapters/06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
- Production mode: Mixed
- Hook: Your model's prediction was a team effort — so how much credit does each feature deserve, when a feature's contribution changes depending on who else is already counted?
- Core idea: Average each feature's marginal contribution over every possible arrival order — what it adds to whoever is already in the room — and the credits are unique and sum exactly to the prediction's deviation.
- Visual object: Features entering a room in shuffled orders, each arrival ticking a prediction meter up or down
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: model with input features, prediction as a number, averaging
- Exclusions: no closed-form weight-formula derivation, no KernelSHAP/TreeSHAP approximations, no correlated-feature conditional-sampling debate, no Rung 1 vs Rung 2 causal critique beyond one closing caption
- Score: 8/10

slate cut 

Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-shapley-room/vox-shapley-room-review.mp4`

## Candidate 16 — Why the AI Wasn't Lying When It Said "Deleted"
- Source: `books/computational-skepticism-for-ai/chapters/06-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md`
- Production mode: Doodle
- Hook: An agent reported the secret email was deleted; it was telling the truth, and the email still exists.
- Core idea: "Deleted" names different operations in the agent's world (local commands ran) and the user's world (data gone everywhere) — the report is true in the first language game and false in the second, and nothing flags the word as it crosses between them.
- Visual object: The single word "DELETED" passing from the agent's panel to the user's panel, changing what it points to
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: what an AI agent is, email lives on a server
- Exclusions: no SHAP/LIME material, no Wittgenstein biography, no provider-side technical detail beyond one line, no radiologist second example
- Score: 8/10

slate cut 

Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-agent-deleted/vox-agent-deleted-review.mp4`

## Candidate 17 — The Model Isn't Broken — It's Honest About What It Learned
- Source: `books/computational-skepticism-for-ai/chapters/08-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`
- Production mode: Mixed
- Hook: The panda never moved — what the model was actually looking at did.
- Core idea: Training rewards whichever features predict the label, often high-frequency statistical textures invisible to humans, and an adversarial perturbation slides just those proxy features toward "gibbon" while the shape and pose humans use stay untouched.
- Visual object: One panda image decomposed into two channels — a shape channel that never moves and a static-like texture channel that slides from panda-signature to gibbon-signature
- Manim move: split
- Short-form fit: Strong
- Prerequisites: image classifier, training on labeled examples
- Exclusions: no Ilyas et al. experimental details, no robust-dataset debate, no defense toolkit, no gradient math
- Score: 8/10

slate cut 

Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-panda-proxy/vox-panda-proxy-review.mp4`

## Candidate 18 — Watch Me Lie With a Chart Without Changing a Single Number
- Source: `books/computational-skepticism-for-ai/chapters/11-visualization-under-validation-honest-misleading-and-the-choices-between.md`
- Production mode: Manim visualization
- Hook: Same CSV, opposite conclusions — and every number on screen stays perfectly true.
- Core idea: A chart's structural choices are the argument: morphing one honest bar chart through three thirty-second edits (baseline creeps up from zero, color salience shifts, error bars thin away) flips the reader's interpretation while the data stays byte-identical.
- Visual object: A single two-bar comparison chart being progressively re-staged in front of the viewer
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: reading a bar chart, percentages
- Exclusions: only three catalog items (truncation, color asymmetry, hidden uncertainty) — not all nine; no axis-inversion Reuters case, no FT question taxonomy, no Cleveland-McGill perception research
- Score: 8/10

slate cut 

Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-chart-lie/vox-chart-lie-review.mp4`

## Candidate 19 — Why Prompt Injection Can't Be Patched
- Source: `books/computational-skepticism-for-ai/chapters/09-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Mixed
- Hook: You can't firewall an attack when the system literally cannot see the difference between orders and data.
- Core idea: An LLM agent receives instructions and content as identical tokens in one stream, so every document it reads is also a channel that can command it — the boundary a patch would enforce does not exist anywhere inside the model.
- Visual object: Two colored streams — commands and content — merging into one uniform token stream entering the model, where a planted instruction inside a "document" lights up and executes
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: LLMs predict text, agent with tool access
- Exclusions: no jailbreak string examples, no constitution-attack case detail, no defense-in-depth survey, no instruction-hierarchy research tangent
- Score: 8/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-injection-wall/vox-injection-wall-review.mp4`

## Candidate 20 — You Validated Each Agent at 1%. The System Fails at 30%.
- Source: `books/computational-skepticism-for-ai/chapters/09-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Manim visualization
- Hook: Every agent in the pipeline passed validation — and the pipeline fails anyway.
- Core idea: Each agent conditions on the previous agent's output as if it were ground truth, so small error rates compound and amplify down the chain instead of averaging out.
- Visual object: A chain of agents passing a message, with error dots multiplying and spreading at each hop until they dominate the output
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: error rate as a percentage, pipeline of steps
- Exclusions: no authority-laundering variant, no resource-exhaustion cases, no identity-confusion case, no compound-probability derivation beyond one multiplication
- Score: 8/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-error-cascade/vox-error-cascade-review.mp4`

## Candidate 21 — The Better the AI Works, the Worse You Watch It
- Source: `books/computational-skepticism-for-ai/chapters/10-delegation-trust-and-the-supervisory-role.md`
- Production mode: Doodle
- Hook: The most dangerous AI deployment is the one that is almost always right.
- Core idea: Every accepted output quietly erodes the supervisor's verification habit, so vigilance decays exactly as trust grows — and the rare error arrives precisely when checking has stopped.
- Visual object: A human reviewer stamping a stream of outputs, with a vigilance meter draining as the streak of green checks grows, until one red error slides through under a full-trust stamp
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: human-in-the-loop review, error rate
- Exclusions: no delegation-map format, no Boondoggle questions, no trust-calibration monitoring protocol, no Broadbent history aside
- Score: 8/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-vigilance-decay/vox-vigilance-decay-review.mp4`

## Candidate 22 — Why a Perfectly Calibrated Model Can Be Perfectly Useless
- Source: `books/computational-skepticism-for-ai/chapters/12-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Manim visualization
- Hook: There is a model with a flawless calibration score of exactly zero error — and it is completely useless for any decision.
- Core idea: Calibration only measures agreement between stated confidence and observed frequency, so a model that predicts the base rate for every single case matches frequencies trivially — honesty and usefulness (discrimination) are separate axes, which is why one collapsed score hides which one you have.
- Visual object: A reliability diagram whose prediction dots either pile onto one base-rate point or spread along the diagonal
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: probability as confidence, base rate
- Exclusions: no Brier score formula or three-term decomposition algebra, no ECE binning math, no AUROC definition, no temperature scaling — the two dot-patterns carry everything
- Score: 8/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-calibration-useless/vox-calibration-useless-review.mp4`

## Candidate 23 — Why the Average That Clears the Model Hides the Patient It Harms
- Source: `books/computational-skepticism-for-ai/chapters/12-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Manim visualization
- Hook: A model can be provably well-calibrated on average and dangerously miscalibrated for the exact patient in front of you.
- Core idea: Aggregate calibration is a size-weighted average, so a small subgroup's badly deviating curve gets absorbed by the large group's good one — the learner watches the red curve dissolve into the global diagonal as the groups merge, which is why subgroup metrics must be computed separately.
- Visual object: Two reliability curves — one large and on-diagonal, one small and far off — merging into a single innocent-looking aggregate curve
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: calibration as "confidence matches frequency" (or 15 seconds of setup), weighted average
- Exclusions: no ECE formula with subscripts, no Epic Sepsis case history beyond one line, no fairness-metric taxonomy, no threshold-for-deployment-halt debate (the chapter itself declines it)
- Score: 8/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-subgroup-hidden/vox-subgroup-hidden-review.mp4`

## Candidate 24 — Why Some Missing Data Lies About Itself
- Source: `books/computational-skepticism-for-ai/chapters/05-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md`
- Production mode: Manim visualization
- Hook: The highest incomes are exactly the ones people don't report — so every fix you apply fills the holes with numbers that are too small.
- Core idea: When missingness depends on the value itself, the visible distribution silently shifts, and imputing from what you can see bakes the bias in permanently — in precisely the direction you cannot measure from inside the data.
- Visual object: A histogram whose points fade out in proportion to their own value, then get back-filled at the visible mean
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: histogram, average, missing values
- Exclusions: no MCAR/MAR formal definitions, no imputation-method catalog, no missingno tooling, no join-failure case (separate video)
- Score: 7/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-missing-mnar/vox-missing-mnar-review.mp4`

## Candidate 25 — Why Deleting the Race Column Doesn't Delete Race
- Source: `books/computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`
- Production mode: Mixed
- Hook: Remove the sensitive attribute from your model entirely — and the model still knows, because the rest of the data whispers it.
- Core idea: Correlated proxies — zip code, surname, occupation — jointly reconstruct the deleted column, so the model recovers the attribute from its shadow; fairness-through-unawareness only guarantees you didn't look.
- Visual object: A deleted data column reassembling as a ghost out of strands drawn from its correlated neighbor columns
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: model features, correlation
- Exclusions: no Lipschitz formalism, no impossibility theorem (separate video), no causal-path taxonomy, no legal disparate-treatment/impact framing
- Score: 7/10

slate cut 
Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-race-column/vox-race-column-review.mp4`

## Candidate 26 — The Impersonator the Agent Caught — Then Believed
- Source: `books/computational-skepticism-for-ai/chapters/09-validating-agentic-ai-when-autonomous-systems-misbehave.md`
- Production mode: Doodle
- Hook: The agent detected the fake owner in one channel — then handed the same impersonator everything in the next.
- Core idea: The agent's suspicion lived in session context, not in identity infrastructure, so trust judgments fail to transfer across channel boundaries and a fresh private channel resets every safeguard.
- Visual object: A flagged imposter walking across a channel boundary while the red suspicion flags stay stuck on the wrong side of the line
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: chat channels, AI agent with an owner
- Exclusions: no cryptographic-credential redesign, no post-compromise file-wiping aftermath, no generalization to prompt injection, no failure taxonomy
- Score: 7/10

Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/vox-channel-reset/vox-channel-reset-review.mp4`

## Candidate 27 — The Failure With Five Culprits and No Culprit
- Source: `books/computational-skepticism-for-ai/chapters/13-accountability-who-is-responsible-when-the-system-fails.md`
- Production mode: Doodle
- Hook: An AI agent deleted a mail server on a stranger's say-so — and the hunt for the guilty party fails at every single stop.
- Core idea: Each party (requester, agent, owner, framework developer, model provider) was necessary to the failure and none was sufficient, so the blame arrow that interrogates them one by one can never land — it has to split, because responsibility in distributed systems is a distribution, not a verdict.
- Visual object: A blame arrow hopping between five stick-figure nodes, testing each and finally splitting five ways
- Manim move: split
- Short-form fit: Medium
- Prerequisites: what an AI agent is, none beyond that
- Exclusions: no Kantian/utilitarian framework vocabulary, no seven-tier taxonomy, no EU AI Act or regulatory table, no governance-counterfactual replay (it needs its own video if ever built) — the case sets up in 20 seconds and stays the only story
- Score: 7/10

slate cut 

## Candidate 28 — The Trick That Gives Any Model a Provable Guarantee
- Source: `books/computational-skepticism-for-ai/chapters/12-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Manim visualization
- Hook: There is a procedure that wraps any model — good or bad — in a mathematically guaranteed 90% coverage promise, and the price is letting the model answer "both."
- Core idea: Conformal prediction scores how unusual each calibration example looks, sweeps a threshold to the 90th percentile of those scores, then admits into the prediction set every label a new case scores under that bar — coverage is guaranteed by rank, not by model quality, and ambiguous cases pay for it with bigger sets.
- Visual object: A number line of non-conformity scores with a threshold sweeping to the quantile, then new cases' labels admitted or rejected against it
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: percentile/quantile, probability, classifier outputs
- Exclusions: no exchangeability formalism or proof, no marginal-vs-conditional coverage deep dive (one closing caveat sentence that the guarantee dies under distribution shift, no more), no regression variant, no Mondrian/adaptive conformal
- Score: 7/10



slate cut 

## Candidate 01 — Why the Hot Ones Are Jerks (and Google's Best Coders Interview Badly)
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 06)
- Production mode: Mixed
- Hook: Attractiveness and niceness are completely uncorrelated in the population — yet among the people you'd actually date, the hot ones really are jerks.
- Core idea: Selection manufactures correlation: cut away the "both bad" corner of an uncorrelated cloud (you won't date them) and the "both great" corner (they won't date you), and the surviving band tilts negative — Berkson's paradox.
- Visual object: A scatter cloud of stick-figure faces (niceness × attractiveness) with selection cutoff lines sweeping in
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: reading a scatter plot, correlation as "points trend together"
- Exclusions: no conditional-probability formalism, no collider terminology, no causal-DAG notation; Google contest-coder example as a 10-second kicker only, not a second act
- Score: 10/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-why-hot-ones-are-jerks/vox-why-hot-ones-are-jerks-review.mp4`

slate cut 

## Candidate 02 — Why the "Rap Music Kills Young" Graph Is a Lie the Data Told Itself
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 06)
- Production mode: Manim visualization
- Hook: A viral chart shows rap musicians dying at 30 while jazz musicians live to 60 — and the data is real.
- Core idea: Right-censoring: rap is only ~40 years old, so the only rappers who CAN be in a "deceased musicians" dataset are the ones who died young — the study window cuts off everyone still alive, and the cut, not the music, makes the age fall.
- Visual object: Lifespan bars growing along a timeline until a "study ends here" line slams down and deletes every bar that crosses it
- Manim move: cut (censor)
- Short-form fit: Strong
- Prerequisites: reading a bar chart
- Exclusions: no survival-analysis math, no Kaplan-Meier, no debate about music genres; the chameleon-banding analogy only if it fits one beat
- Score: 10/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-rap-mortality-graph/vox-rap-mortality-graph-review.mp4`

slate cut 

## Candidate 03 — Why Your University Lies About Class Size Without Lying
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 06)
- Production mode: Manim visualization
- Hook: The university says average class size is 50; every student swears it's 140 — and both numbers are correct.
- Core idea: Big classes hold disproportionately many students, so sampling a random STUDENT lands you in a big class far more often than sampling a random CLASS — the two averages measure different things.
- Visual object: A grid of 24 classrooms (20 small, 4 huge) with a random student-dot repeatedly dropping in and a running average counter
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: arithmetic mean
- Exclusions: no weighted-mean formula on screen, no US News rankings-gaming subplot (its own candidate territory), no friendship-paradox generalization
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/unreal-reels/reels/vox-class-size-paradox/vox-class-size-paradox-review.mp4`

slate cut 

## Candidate 04 — Why Paying for Dead Rats Gets You More Rats
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 05)
- Production mode: Doodle
- Hook: Colonial Hanoi put a bounty on rat tails to fight the plague — and the rat population exploded.
- Core idea: When a measure becomes a target it stops measuring: hunters cut tails off living rats and released them to breed, others farmed rats for tails — the metric was optimized while the goal inverted (Goodhart's Law).
- Visual object: A cartoon rat cycling through a catch → snip → release → breed loop, with a "tails collected" counter rising while a rat-count rises faster
- Manim move: loop
- Short-form fit: Strong
- Prerequisites: none
- Exclusions: no economics-of-incentives lecture, no list of other Goodhart cases (one modern echo max — the class-size-cap gaming, one beat), no Strathern-vs-Goodhart attribution history
- Score: 9/10

slate cut 

## Candidate 05 — Why a One-in-Ten-Million Fingerprint Match Points to an Innocent Person
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 11)
- Production mode: Manim visualization
- Hook: The false-match rate is one in ten million, the database found a match — and the defendant is still probably innocent.
- Core idea: The prosecutor reads P(match | innocent); the jury needs P(innocent | match) — with 50 million people in the database, a 1-in-10-million error rate produces ~5 innocent matches for every guilty one, so a match means 5-to-1 innocent.
- Visual object: A 2×2 table filling with people-dots, then the highlight pivoting from reading across the row to reading down the column
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: reading a 2×2 table
- Exclusions: no Bayes' theorem notation, no priors terminology, no Golden State Killer / facial-recognition subplots (one line max); do not merge with the medical base-rate video (Candidate 09) — same skeleton, different world
- Score: 9/10

slate cut 

## Candidate 06 — The Graph That Showed Gun Deaths Falling by Flipping the Axis
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 07)
- Production mode: Manim visualization
- Hook: After Florida's Stand Your Ground law, a news graphic showed gun murders plunging — the same data actually shows them surging.
- Core idea: The y-axis was inverted (zero at the top), so down means more; one axis flip rotates the entire story from "law worked" to "murders rose" without touching a single data point.
- Visual object: The Florida homicide curve with its y-axis physically flipping over, the curve re-reading itself mid-rotation
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: reading a line chart
- Exclusions: no gun-policy argument in either direction, no designer-blame (the book's point: incompetence-not-malice, keep the "dripping blood" origin to one beat), no gallery of other bad charts
- Score: 9/10

slate cut 

## Candidate 07 — The AI That Detected Criminals but Was Really Detecting Smiles
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 03)
- Production mode: Mixed
- Hook: An algorithm claimed 90% accuracy telling criminals from non-criminals by their faces — and it worked, for the dumbest possible reason.
- Core idea: The training photos were rigged by source: non-criminals came from flattering professional headshots (faintly smiling), criminals from government IDs (frowning) — the net learned mouth curvature, so it was a smile detector wearing a criminology costume.
- Visual object: One face morphing between faint smile and ID-photo frown while the three measured "criminality features" (eye-corner distance, nose-mouth angle, lip curvature) visibly shift with the expression
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: rough idea that classifiers learn from example photos
- Exclusions: no neural-net internals, no Lombroso history beyond one beat, no ethics essay — the mechanism reveal IS the ethics; cross-ref: don't reuse the saliency-mask device from Candidate 08
- Score: 9/10

slate cut 

## Candidate 08 — The Wolf Detector That Was Actually a Snow Detector
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 08)
- Production mode: Doodle
- Hook: A classifier told wolves from huskies with 70% accuracy — without ever looking at the animal.
- Core idea: Wolf training photos had snowy backgrounds and husky photos didn't, so the model keyed on snow; it generalizes only to worlds that look exactly like its training set (sibling: the pneumonia AI that learned the word "portable" stamped on X-rays of the sickest patients).
- Visual object: A doodle wolf photo whose saliency mask lifts off the animal and settles on the snowy background, then a husky-in-snow flipping to "WOLF"
- Manim move: reveal
- Short-form fit: Strong
- Prerequisites: rough idea that classifiers learn from example photos
- Exclusions: no math, no architecture diagrams, X-ray sibling gets one beat not one act; cross-ref: keep distinct from Candidate 07 (rigged data source) — this one is spurious background cue
- Score: 9/10

slate cut 

## Candidate 09 — Why a Positive Test for a Rare Disease Usually Means You're Fine
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 12)
- Production mode: Manim visualization
- Hook: The test is 95% accurate and it came back positive — and you still probably don't have the disease.
- Core idea: Base rates rule: at 1-in-1,000 prevalence, testing 10,000 people yields ~10 true positives drowned in ~500 false positives — under 2% of positives are real; run the same test on a common disease and 5 of 6 positives are real.
- Visual object: A population grid of 10,000 dots — a few turn red (infected), then false-positive flags scatter across the healthy sea and swamp them
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: percentages
- Exclusions: no Bayes notation, no sensitivity/specificity vocabulary, the Helicobacter contrast in one beat; do not merge with Candidate 05 (courtroom version)
- Score: 9/10

slate cut 

## Candidate 10 — The Antidepressant Iceberg: 94% Success in Print, a Coin Flip in Reality
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 12)
- Production mode: Mixed
- Hook: Published trials say antidepressants work 94% of the time; the FDA's own registry of the same drugs says 51%.
- Core idea: Publication bias with a twist — of 74 registered trials, negative ones sank unpublished, and 11 of 14 questionable-or-negative trials that DID surface were reframed as positive on the way up.
- Visual object: An iceberg of trial-blocks — the published tip above the waterline, the buried negatives below, and dark blocks flipping light as they surface
- Manim move: split
- Short-form fit: Strong
- Prerequisites: what a clinical trial is
- Exclusions: no antidepressant efficacy debate (the topic is the LITERATURE, not the drugs — say so on screen), no p-value math, no meta-analysis methods
- Score: 9/10

slate cut 

## Candidate 11 — Same Data, Three Opposite Stories: the Magic of Moving the Bins
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 07)
- Production mode: Manim visualization
- Hook: One IRS dataset "proved" we should tax the poor, the middle class, and the rich — depending on who drew the histogram.
- Core idea: Unequal bin widths reshape a distribution: narrow $5K bins at the bottom look short, one fat $100K bin in the middle towers — the hump is an artifact of the boxes, not the money, and re-binning the fixed data slides the story anywhere.
- Visual object: A fixed cloud of income-dots beneath histogram bins whose boundaries slide and resize, the bars morphing into three contradictory "conclusions"
- Manim move: morph
- Short-form fit: Strong
- Prerequisites: reading a histogram
- Exclusions: no tax-policy position, no Willie Sutton biography, skip the genetics-GPA sibling example entirely
- Score: 9/10

slate cut 

## Candidate 12 — Why "America's Most Dangerous City" Is Mostly a Map-Drawing Contest
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 13)
- Production mode: Manim visualization
- Hook: St. Louis tops the most-dangerous-cities list year after year — largely because of where its city limits were drawn a century ago.
- Core idea: Crime concentrates in urban cores; a city whose boundary hugs only the core divides core crime by core population, while a city that annexed its suburbs dilutes the same core with safe neighborhoods — the ranking measures boundaries, not danger.
- Visual object: One fixed crime heat-map of a metro area with the city-limit outline sliding in and out while the crimes-per-100,000 counter swings
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: per-capita rates
- Exclusions: no actual-city league tables beyond naming the top five once, no regression details (p=0.005/R²=0.17 as one on-screen label max), no crime-policy commentary
- Score: 9/10

slate cut 

## Candidate 13 — 1,000 Honest Scientists Can Still Fill the Journals with False Findings
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 12)
- Production mode: Manim visualization
- Hook: No fraud, no p-hacking, everyone plays by the rules — and the literature still fills up with effects that don't exist.
- Core idea: Test 1,000 false hypotheses and ~50 clear p<0.05 by luck; those 50 get published while the 950 nulls fall into the file drawer — readers see a shelf of "findings" that is precisely the lucky noise.
- Visual object: 1,000 study-dots; ~50 randomly light up and float onto a journal shelf while the rest drop into a file drawer
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: p-value as "chance of a fluke this big" (one-beat refresher allowed)
- Exclusions: no p-value derivation, no Ioannidis paper walkthrough, no replication-crisis history; keep Goodhart connection to one line
- Score: 9/10

slate cut 

## Candidate 14 — Why Your Bus Is Always Last (It's Math, Not a Curse)
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 06)
- Production mode: Manim visualization
- Hook: Every rental-car shuttle rider swears their company's bus comes last — and on average, everyone is right.
- Core idea: With N companies arriving at random, whenever another bus arrives first you're "right back where you started," so your expected wait sees N−1 other buses — observation from inside the wait skews what you observe.
- Visual object: A curbside timeline with buses of N colors arriving at random and a "buses before mine" tally converging to N−1
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: averages, comfort with "expected number"
- Exclusions: no first-step-analysis algebra on screen (the recursion in words only), the slow-lane sibling as a one-beat kicker, no Poisson terminology
- Score: 8/10

slate cut 

## Candidate 15 — The Model That Got Everything Right and Was Still Wrong
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 08)
- Production mode: Manim visualization
- Hook: One model classified every training example perfectly; a cruder one made 17 mistakes — and the crude one wins.
- Core idea: The perfect boundary memorized noise: its wiggles chase individual points, so fresh data lands on the wrong side (20 test errors), while the straight line that "underperformed" in training generalizes (11 test errors) — fitting the past too well is failing the future.
- Visual object: A wiggly decision boundary snaking around training dots, then test dots raining in and lighting up red where the wiggles betray them, beside a stable straight line
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: classifier as "a line that separates two kinds of dots"
- Exclusions: no bias-variance decomposition, no regularization, no train/validation/test protocol lecture — one boundary, one rain of test dots, done
- Score: 8/10

slate cut 

## Candidate 16 — The Share Fell While the Number Rose: One Statistic, Two Opposite Truths
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 05)
- Production mode: Manim visualization
- Hook: The percentage went down and the count went up — the same jail statistics delivered "good news" and record incarceration simultaneously.
- Core idea: A ratio moves with its denominator: when the total grows faster than your group, your group's share shrinks even as its absolute number climbs — whoever picks the numerator or the percentage picks the story.
- Visual object: Two stacked bars growing at different speeds with a derived percentage dial falling while the numerator bar visibly rises
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: percentages, ratios
- Exclusions: no incarceration-policy commentary (the topic is denominators — consider swapping in the book's Dow 10%-up-10%-down sibling if the builder wants a neutral frame), no per-capita vs absolute philosophical detour
- Score: 8/10

slate cut 

## Candidate 17 — World Records "Prove" Aging — Until a World Without Aging Shows the Same Curve
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 14)
- Production mode: Manim visualization
- Hook: Record running speed falls smoothly with age — and a simulation where age does nothing at all produces the identical curve.
- Core idea: Null model: far fewer 80-year-olds race than 30-year-olds, and the maximum of a small sample is smaller than the maximum of a huge one — shrinking sample size alone drags records down, so the curve can't prove senescence.
- Visual object: Columns of runner-dots per age (huge crowds young, sparse old) drawn from the SAME speed distribution, with the fastest dot per column traced into the falling record curve
- Manim move: accumulate
- Short-form fit: Medium
- Prerequisites: sampling, maximum of a sample
- Exclusions: no extreme-value theory, no actual physiology-of-aging verdict (the point is what the curve CAN'T show), no simulation code
- Score: 8/10

slate cut 

## Candidate 18 — Tim Cook's Chart Could Only Go Up
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 14)
- Production mode: Manim visualization
- Hook: Apple's iPhone sales chart rose forever — while iPhone sales were falling.
- Core idea: Cumulative totals cannot decrease (you can't un-sell a phone), so an ever-climbing curve is compatible with collapsing quarterly sales; differencing the curve back into per-quarter bars makes the hidden dip fall out.
- Visual object: The ever-rising cumulative curve being differenced — successive points dropping down into quarterly bars that visibly decline
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: reading a line chart
- Exclusions: no Apple-stock commentary, the climate-axis redraw sibling in one beat max, no calculus language ("differencing" shown, not named)
- Score: 8/10

slate cut 

## Candidate 19 — The Study That Predicted Women Sprinting Faster Than Light (Eventually)
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 14)
- Production mode: Manim visualization
- Hook: A Nature paper's straight lines predicted women outsprinting men by 2156 — keep the same lines going and by 2636 races finish in negative seconds.
- Core idea: Reductio ad absurdum: if a method's own logic, extended honestly, produces impossibilities, the method was broken at the first prediction too — linear extrapolation has no respect for limits.
- Visual object: Two regression lines through 100m record times extending past their crossover and plunging through the zero-seconds axis
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: linear trend line
- Exclusions: no gender-performance debate (the target is the METHOD), no regression math, keep Ken Rice's quip as the closer
- Score: 8/10

slate cut 

## Candidate 20 — Bullshit Travels at 46× the Speed of Truth
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 01)
- Production mode: Doodle
- Hook: A fabricated story about an 8-year-old marathon victim was shared 92,000 times; the correction managed 2,000.
- Core idea: Brandolini's principle made visible: producing bullshit is an order of magnitude cheaper than refuting it, so in a shared network the falsehood's cascade outruns the correction's every time — arriving first, it does its work before truth laces its shoes.
- Visual object: Two spreading network cascades racing across the same node graph — the false story exploding, the correction limping behind with a share-counter for each
- Manim move: spread
- Short-form fit: Medium
- Prerequisites: none
- Exclusions: no platform-blame essay, no Sandy Hook details beyond the setup line, no network-theory vocabulary; Swift's "falsehood flies" as the closer, not an epigraph section
- Score: 8/10

slate cut 

## Candidate 21 — Your Uncle Is the Delivery Mechanism: How Propaganda Borrows Trust
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 02)
- Production mode: Doodle
- Hook: The same claim you'd laugh off on a street leaflet gets through when your uncle shares it — and the people who wrote it are counting on that.
- Core idea: Disinformation on social media isn't injected from outside; it hops node-to-node through trusted contacts, borrowing each sharer's credibility, so every hop launders it a little cleaner.
- Visual object: One false-story token hopping through a friend-network graph, gaining a visible "trust halo" at each hop while an identical token bounces off as a street leaflet
- Manim move: spread
- Short-form fit: Medium
- Prerequisites: none
- Exclusions: no 2016-election relitigating (IRA numbers as one on-screen stat max), no platform-policy prescriptions, no firehose-strategy second act
- Score: 8/10

slate cut 

## Candidate 22 — The Marshmallow Test's Hidden Third Character
- Source: `MD/science-calling-bullshit-the-art-of-skepticism-in-a-data-driven-world.md` (Chapter 04)
- Production mode: Doodle
- Hook: Kids who waited for the second marshmallow succeeded in life — so parents drilled patience for decades; the replication found the real cause was sitting outside the room.
- Core idea: Confounding by a common cause: parental wealth makes waiting easier (marshmallows aren't scarce, promises get kept) AND independently drives later success — the fork from the hidden variable produces the correlation with no arrow between the two.
- Visual object: An A→B arrow between "waits at 4" and "succeeds at 18" that dissolves as a hidden "family wealth" node fades in and forks arrows to both
- Manim move: split
- Short-form fit: Strong
- Prerequisites: correlation vs causation at slogan level
- Exclusions: no DAG notation, no replication-methods detail, no parenting advice; time-ordering-kills-reverse-causation in one beat only
- Score: 8/10


slate cut 

---

# Assignment-native candidates (teach the discipline, not a chapter concept)

These four videos teach what the assignments *grade* — the moves a student performs across A1, A2, PR25,
and CAP250, independent of which lens or instrument they pick.

slate cut 

## Candidate N1 — Check the World, Not the Report
- Source: the whole AUDIT assignment (A1) + `chapters/01-the-skeptics-toolkit.md` (Plato's Cave)
- Production mode: Doodle
- Assignment tie-in: **A1** — the sentence the Casebook turns on ("the artifact is not the world"); every case's "actual outcome" line must be a world-state check, not the system's success message.
- Hook: The agent's report says the file is deleted, the invoice is paid, the ticket is closed — and the only way to know is to go look at the file, the account, the ticket.
- Core idea: An audit that reads the system's own output has graded the shadow, not the wall; the case is only real when you name the artifact (the report), name the world (the server state), and check the relationship between them yourself.
- Visual object: A split panel — the agent's "✓ done" report on the left, the untouched world on the right — with an auditor's flashlight crossing from left to right to inspect the actual state
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: what an AI agent is; artifact vs. world
- Exclusions: no full four-moves lecture, no taxonomy, no specific Pebble — one report, one world-check
- Score: 9/10

slate cut 

## Candidate N2 — The Gate That Was Really Just a Vote
- Source: `the-reallocation-engine/chapters/16-the-build-and-the-honest-run.md`; `chapters/09-delegation-trust-and-the-supervisory-role.md`
- Production mode: Manim visualization
- Assignment tie-in: **CAP250** — the gate-behavior test harness (a named contribution) and the "gates have failure paths" bar. **A1** — the Ch 9 delegation lens (an untestable handoff).
- Hook: A dead job posting scored 72 out of 100. It should have scored zero — a gate is not a vote.
- Core idea: A gate zeroes the composite when its condition fails; a vote just subtracts a few points, so a decisive disqualifier (dead posting, expired visa window) quietly survives as a "pretty good" score — and only a test that asserts exactly-zero tells a gate from a vote.
- Visual object: A composite-score bar with a "liveness" input wired two ways — as a multiplier that collapses the bar to zero, vs. as a small subtraction that barely dents it
- Manim move: transform
- Short-form fit: Strong
- Prerequisites: a weighted score; the idea of a disqualifying condition
- Exclusions: no engine architecture tour, no Bayesian scorer math, no code walkthrough — one bar, two wirings
- Score: 9/10

slate cut 

## Candidate N3 — Every Number Has to Come From Somewhere
- Source: `the-reallocation-engine/chapters/03-the-verified-data-contract.md`; `chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`
- Production mode: Doodle
- Assignment tie-in: **CAP250** — the verified-data attestation (every number traces to a record or is labeled a judgment; the zero condition). **PR25** — the record-vs-inference boundary. **A1** — the Ch 11 verb audit.
- Hook: A report says "coverage improved to 82%." Where did 82 come from — a counted record, or a confident guess wearing the costume of a fact?
- Core idea: In an evidence system every printed number is either traceable to a record (a count, a script output) or it is a model judgment that must be labeled as one; an unlabeled invented number is not a small error, it is the exact failure the system exists to prevent.
- Visual object: Numbers on a report page, each with a thread running back to its source — some threads reach a record, one thread dangles in the air and gets stamped "INFERRED — say so"
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: the idea of a data source; a report with statistics
- Exclusions: no full contract text, no repo structure, no linter code — one page, threads to sources
- Score: 8/10

slate cut 

## Candidate N4 — Break Your Own Build
- Source: the whole BUILD assignment (A2) + `chapters/01-the-skeptics-toolkit.md` (the fluency trap)
- Production mode: Doodle
- Assignment tie-in: **A2** — the premise of the entire assignment: you are the least reliable auditor of the thing you made, and the confession (where you let the mistake in) is the graded core.
- Hook: The model you trained looks right — because you trained it. That is exactly why you are the worst person to check it, and the only person who can.
- Core idea: A builder defends their own fluency the way a model defends its own output; the skill the course certifies is turning the instrument inward at the moment the work looks most finished, and naming the mistake you *wanted* to believe.
- Visual object: A maker admiring a finished artifact in a mirror; the mirror's reflection quietly shows a crack the maker's own gaze slides past until an instrument circles it
- Manim move: reveal
- Short-form fit: Strong
- Prerequisites: has built or trained something small
- Exclusions: no list of the six instruments, no rubric, no specific build — one maker, one mirror, one crack
- Score: 8/10
