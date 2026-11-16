# SHOTLIST — tldr-features-entering-a-room
Typed work order per slot. Every slot is pipeline-owned: **zero human media, zero pantry, zero gen-AI** (tldr rule 6). Every number is the chapter's own (constructed worked example) or recomputed from it, asserted in `make_sheet.py` / `scenes.py`.

| Beat | Role | Type × source | Owner | What it is |
|---|---|---|---|---|
| B00 | TL;DR · WHAT | REMOTION own (bookend) | pipeline | ClaudeTldrWhat — "Kumusta, Liam"; the question writes on; three numbered lines land on their clauses |
| B01 | TL;DR · WHY | REMOTION own (bookend) | pipeline | ClaudeTldrWhy — the stake writes on; three dashed consequences land |
| B02 | THE QUESTION | REMOTION own (bookend) | pipeline | BrutalistHesitantWriter — "How much did income add" → "What is income's fair share" (phrase trigger) |
| B03 | TERMS | REMOTION own (card) | pipeline | ClaudeDefinitions — feature · prediction · baseline · coalition |
| B10 | HOOK | GRAPHIC own | Manim `B10_OneApplicant` | prediction line 0.55 → 0.72; the ghost span "0.17 to split"; three feature names; "how much of the 0.17 is income's?"; "constructed example" caption |
| B11 | INSTANCE | GRAPHIC own | Manim `B11_IncomeFirst` | the room ledger opens; income arrives first: dot 0.55 → 0.63, bump bar +0.08; row one records it |
| B12 | NAIVE | GRAPHIC own | Manim `B12_DropItAndSee` | full room 0.72, income out → 0.66: bump +0.06 = income last (row six); "+0.08 or +0.06?" with an X |
| B13 | INSTANCE | GRAPHIC own | Manim `B13_MiddleSeats` | rows three and four: after debt +0.07, after zip +0.09 |
| B14 | SHIFT · predict | GRAPHIC own | Manim `B14_EveryOrder` | rows two and five complete all 3! = 6 orders; the line clears to the span "0.17 to split ?"; hold, commit |
| B15 | TRANSFORM | GRAPHIC own | Manim `B15_AverageThem` | six table bars merge into one 0.073 bar that lands on the span; debt 0.062 and zip 0.035 grow on; they stop at 0.72 |
| B16 | ABSTRACTION | GRAPHIC own | Manim `B16_NameIt` | the table folds into 2/6·0.08 + 1/6·0.07 + 1/6·0.09 + 2/6·0.06 = 0.073; the Shapley formula writes; the bar labels morph into the efficiency sum; title "The Shapley Value" |
| B17 | TANGENT | GRAPHIC own | Manim `B17_ReadTheFormula` | Shapley formula on top; LHS/RHS/"=" sentences; glossary φᵢ, S, F, v(S); worked weight 1!·1!/3! = 1/6, 0!·2!/3! = 2/6 |
| B18 | TANGENT | GRAPHIC own | Manim `B18_ReadTheSum` | efficiency sum on top; sentences; glossary f̂(x), E[f̂]; 0.073 + 0.062 + 0.035 = 0.17 = 0.72 − 0.55 written over the bars |
| B19 | PAYOFF | GRAPHIC own | Manim `B19_Payoff` | the question returns; first-in +0.08 and last-in +0.06 ghosts fold into 0.073; dot to zip's bar; boundary caption |
| BVDT | VERDICT | REMOTION own (bookend) | pipeline | ClaudeVerdictArtifact — four lines |
| BHTF | YOUR TURN | REMOTION own (bookend) | pipeline | ClaudeComposerAsk "Your turn." — build a three-feature v(S), predict, enumerate, check efficiency, say what zip's share does not tell you |
| BOUT | OUTRO | REMOTION own (bookend) | pipeline | ClaudeTitleOutro — spoken title + "At Nik Bear Brown", 1.0 s tail, no jingle |
