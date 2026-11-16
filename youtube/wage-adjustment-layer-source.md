# Professor Bear's feedback — Atharva's Computational Skepticism final project
_Source for a deep-explainer reel. FIRST NAME ONLY: "Atharva." The reel is Bear's feedback
on the project idea below._

## The student's proposal (Atharva)
"A Local Wage-Adjustment Layer for ERP-to-AI Career Transitions." The Reallocation Engine
currently scores roles with national BLS wage data, hiding real pay differences across metros —
a gap the book calls out. Atharva builds a layer that adjusts national BLS figures using local
BLS + BEA data, giving a metro-level wage band instead of one flat national number. Scoped to
ERP pros (SAP, Oracle, Workday) exploring AI/ML roles (Data Scientist, ML Engineer), with an
O*NET skills crosswalk. Every number traces to a real BLS/BEA/O*NET record — nothing invented;
if local data is missing, the tool SAYS SO instead of guessing. Tested by deliberately trying to
break it (feed a no-data metro → confirm honest failure). Headline metric: coverage — how many
metro×role combos get a real adjusted number vs an honest "missing." All sources free/public.
Ships as an AI recipe + a human-readable card documenting failure modes. Scope disclaimer: it
estimates pay and skill overlap only — NOT hiring odds or whether a transition works for a person.

## The core problem
This is the most methodologically self-aware proposal this term — Atharva already built in the
thing most students must be pushed toward: deliberate break-testing, an explicit honest-failure
requirement, and a scope disclaimer. So the useful feedback isn't "add more skepticism" — it's
pointing at the TWO places where the proposal's own rigor ("every number traces to a real record")
could be quietly violated WITHOUT the tool ever technically lying:
1. conflating a NOMINAL BLS wage with a cost-of-living-ADJUSTED one when combining BLS + BEA;
2. an O*NET crosswalk that looks like real overlap but is dominated by generic soft-skills O*NET
   assigns to nearly every professional occupation.

## Part 1 — BLS + BEA combination needs an explicit, stated formula
BLS and BEA measure DIFFERENT things. BLS OEWS publishes NOMINAL wage levels by metro×occupation.
BEA doesn't publish occupation wages at all — its relevant product is Regional Price Parities
(RPPs): how much more/less expensive a metro is vs the national average. Combining them wrong
yields a technically-"sourced" figure that's a different CONCEPT than it appears.
- Reporting a NOMINAL metro wage (straight BLS OEWS) needs no BEA at all.
- Reporting a cost-of-living-ADJUSTED "real" wage (nominal ÷ local RPP, rescaled to national) is a
  materially different number — $120K in a high-RPP metro is less real purchasing power than the
  same figure in a low-RPP metro, so the adjusted figure differs from raw BLS for that reason alone.
Feedback angle: state EXPLICITLY, in the deliverable card, which of the two the tool produces — or
show both, labeled distinctly. "Traces to a real BLS/BEA record" is true either way, but a user
comparing metros must know whether they see raw pay or purchasing-power-adjusted pay (they can rank
metros differently). Extend the "honest missing" behavior to the RPP step: if RPP is missing,
null the adjusted field explicitly — don't silently relabel the nominal figure as adjusted.

## Part 2 — the O*NET crosswalk risks being dominated by GENERIC skills (the sharper issue)
O*NET assigns "Critical Thinking," "Complex Problem Solving," "Active Learning," "Systems Analysis"
to a huge fraction of professional occupations — both ERP and Data Scientist/ML Engineer. If overlap
is a similarity across the FULL skill vector, much of any ERP→AI "overlap" comes from these
near-universal categories, not from anything specifically transferable about ERP experience. That's
an honest failure mode distinct from fabrication: every number traces to a real O*NET record, and the
score is still misleading — it measures "both roles require critical thinking," not "ERP prepares you
for AI role X."
Feedback angle: split the O*NET vector into TIERS — generic professional skills (near-ceiling for any
white-collar comparison) vs role-specific technical/knowledge (Programming, Mathematics, Database
knowledge) — and report overlap SEPARATELY per tier. "92% overlap" driven by generic skills tells a
much weaker story than strong overlap in the technical tier, and users deciding whether to invest in a
transition deserve that distinction, not one blended number. Also flag O*NET's known update lag for
newer occupations (Data Scientist, ML Engineer are relatively new SOC categories) — a stated
limitation for the failure-mode card, not a disqualifier.

## Part 3 — stratify the coverage metric, don't just aggregate it
The coverage metric (% real vs honest "missing") is a good, honest choice — but an aggregate can look
strong while hiding a specific failure: if data sparsity for newer SOC codes concentrates in the
small/mid-size metros where much of the ERP workforce lives (vs dense coverage in a few tech hubs),
the tool could report ~80% overall while being least reliable exactly where its target users are.
Feedback angle: report coverage STRATIFIED by metro-size tier (or whatever correlates with the target
user population), not one aggregate. Strong in SF/NY but weak in mid-size metros is the more
decision-relevant fact, and it's easy to miss if only the aggregate is shown.

## Part 4 — data VINTAGE, not just data presence
The plan flags missing data. A distinct issue is STALE-BUT-PRESENT data: BLS OEWS lags ~6–12 months;
BEA RPPs have their own cadence. A number can be real, present, and out of date without ever
triggering "missing."
Feedback angle: each figure should carry its own visible "as of" vintage date — not a general
disclaimer buried in the card. A user comparing two metros should see if one figure is the latest
OEWS release and the other is older cached data — silently mixing vintages across a single comparison
is another way honest numbers mislead.

## Part 5 — what's already strong (preserve, don't re-litigate)
- The deliberate break-testing (feed a no-data metro → confirm honest failure) is exactly right and
  already applied — just EXTEND the same instinct to Parts 1 and 4: test RPP-missing-but-wage-present
  (and vice versa), and test data-exists-but-several-releases-old.
- The explicit scope disclaimer (pay + skill overlap only, not hiring odds) is the right honesty move —
  keep it prominent in the final card exactly as planned.

## Close: open questions
End with one or two questions for Atharva to resolve himself — how to define metro-size strata for the
coverage metric; whether to surface both nominal and adjusted wages by default or let the user toggle.
Tone: appreciative of already-strong instincts, precise about the two places (BLS/BEA conflation,
generic-skill-driven crosswalk inflation) where the honesty commitment could be quietly undermined
without any single number being fabricated.

## Reference lineage
BLS OEWS (nominal metro wages — confirm which SOC codes, e.g. Data Scientist 15-2051, have adequate
metro coverage given recent addition); BEA Regional Price Parities (the correct COL-adjustment series —
cite RPP specifically, not "BEA data"); O*NET Content Model (Skills/Knowledge/Abilities — the
generic-vs-specific tiering maps onto O*NET's own cross-functional-vs-occupation-specific distinction);
the Reallocation Engine's national-BLS-only wage scoring (the gap being addressed — cite the specific
passage); the course's skeptical-instruments framework — this is the term's strongest example of a
student applying break-testing unprompted; use as a positive model.
