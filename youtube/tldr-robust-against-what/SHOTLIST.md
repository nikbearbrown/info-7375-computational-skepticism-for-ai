# SHOTLIST — tldr-robust-against-what
Typed work order per slot. Every slot is pipeline-owned: **zero human media, zero pantry, zero gen-AI** (tldr rule 6). Every number is the chapter's own template value, asserted in `make_sheet.py` / `scenes.py`.

| Beat | Role | Type × source | Owner | What it is |
|---|---|---|---|---|
| B00 | TL;DR · WHAT | REMOTION own (bookend) | pipeline | ClaudeTldrWhat — "Merhaba, Liam"; the question writes on; three numbered lines land on their clauses |
| B01 | TL;DR · WHY | REMOTION own (bookend) | pipeline | ClaudeTldrWhy — the stake writes on; three dashed consequences land |
| B02 | THE QUESTION | REMOTION own (bookend) | pipeline | BrutalistHesitantWriter — "Is the model robust" → "Robust against what" (phrase trigger) |
| B03 | TERMS | REMOTION own (card) | pipeline | ClaudeDefinitions — clean accuracy · perturbation budget ε · transfer attack · distribution shift |
| B10 | HOOK | GRAPHIC own | Manim `B10_TheSlide` | the vendor sentence; the 94 bar grows; a dot beside "robust" — no bar for the word |
| B11 | INSTANCE | GRAPHIC own | Manim `B11_WhiteBox` | the bar slides into row one of a table; white-box, ε = 0.03; robust bar grows to 71; "template values — illustrative" caption |
| B12 | INSTANCE | GRAPHIC own | Manim `B12_Transfer` | row two: transfer, surrogate model; clean 94, robust 58 |
| B13 | NAIVE | GRAPHIC own | Manim `B13_OneWord` | the two robust bars merge into one bar labelled only "robust"; X beside the word |
| B14 | SHIFT | GRAPHIC own | Manim `B14_UnfoldRows` | the merged bar splits back into rows; row three (natural shift) opens with a "?" |
| B15 | INSTANCE · predict | GRAPHIC own | Manim `B15_Commit` | guide ticks at 58 and 71 on row three; hold; commit |
| B16 | TRANSFORM | GRAPHIC own | Manim `B16_RowThreeLands` | row three grows to 87 past both ticks; the claim's word morphs into two empty fields (residual risk, monitoring trigger) |
| B17 | INSTANCE | GRAPHIC own | Manim `B17_MoveTheBudget` | row one's ε → 0.06: the 71 drains to "?"; back to 0.03, it refills |
| B18 | ABSTRACTION | GRAPHIC own | Manim `B18_NameIt` | the form's three sections labelled; a rail joins them; "a profile, not a number" |
| B19 | PAYOFF | GRAPHIC own | Manim `B19_Payoff` | the slide's sentence returns; a dot walks 94 → 71 → 58 → 87 → the blanks; boundary caption |
| BVDT | VERDICT | REMOTION own (bookend) | pipeline | ClaudeVerdictArtifact — four lines |
| BHTF | YOUR TURN | REMOTION own (bookend) | pipeline | ClaudeComposerAsk "Your turn." — exercise 6 read in full |
| BOUT | OUTRO | REMOTION own (bookend) | pipeline | ClaudeTitleOutro — spoken title + "At Nik Bear Brown", 1.0 s tail, no jingle |
