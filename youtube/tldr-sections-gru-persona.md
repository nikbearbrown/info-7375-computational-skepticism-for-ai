# tldr sections — Gru, the phase-gated architect persona

**What this is.** Step one of the `tldr` skill run on the Gru persona prompt Bear pasted on 2026-09-24 (the "Phase Gates" note, the session-start menu, and the system prompt). The source is short, so it yields two learning sections. One is picked by Bear's request ("TLDR video explaining Liam persona Gru") and building; the other is deferred with a reason.

**Why it matters.** Gru is the course's conducting persona; the phase-gate rule is the part of it a student can test on their own design in one sitting.

Source: pasted by Bear, 2026-09-24 (saved verbatim as `tldr-gru-validated-not-attempted/SOURCE.md`) · read 2026-09-24 · 2 sections · 1 deferred

**Version note.** The pasted Gru differs from the repo's `the-reallocation-engine-fresh/recipes/gru.md` (sha256 d9c443c4…): the repo version starts at `/v0` (brief) and orders `/v1` intake → `/v2` principles → `/v3` flows → `/v4` needs → … → `/g1`. The paste runs `/v1` intake → `/v2` needs → `/v3` principles → `/v4` component mapping → `/v5` assembly. These cards follow the paste. The paste also contradicts itself once: behavioral rule 1 says components map to a need "from /v4", while its own gate list puts needs at `/v2`. The cards follow the gate list.

## S1 · Validated, Not Attempted: Gru's Phase Gates          tier: single-insight
- question:        What does Gru make you decide before Claude writes a design?
- key case:        a checkout design where every section has words, and a "we might as well add" recommendation widget that nobody can say why exists (constructed around the paste's own examples)
- naive:           ask Claude for the whole design in one pass and review the result — the needs come out as "improve user experience", every component traces to it, every check passes, the widget ships
- representation:  the five phases in a row with a gate in front of each; a vague need is a fog that any trace can land in, a validated need is one point
- abstraction:     a phase gate — no valid output from the next phase until this one is validated, not attempted
- boundary:        `silent` skips every gate; `/claude` (the Boondoggle Score) ignores them on purpose → BHTF runs the first two gates on the viewer's own system
- terms (prereq):  SDD, need, component, falsifiable
- equations:       none
- source span:     "Phase Gates — What They Are and Why They're Non-Negotiable" (all five gates, "What happens if you try to skip one", "The exception", "The one thing that ignores gates entirely"); session-start menu; behavioral rules 1, 3, 5
- status:          picked (Bear's request, 2026-09-24) → building `tldr-gru-validated-not-attempted`

## S2 · Gru Doesn't Build the Rocket: Boondoggling          tier: single-insight
- question:        If Claude writes faster than any human, what is left for the human to do?
- key case:        the minions execute exactly what they understood you to mean; the gap between meant and understood is where the damage lives
- naive:           "let Claude do everything and check the output"
- representation:  a build split into tasks, each assigned to Claude or a human with an explicit handoff condition between them
- abstraction:     boondoggling — conducting Claude by assigning, sequencing and handing off, across the five supervisory capacities
- boundary:        how the Boondoggle Score is computed
- terms (prereq):  solve–verify asymmetry, handoff
- equations:       none
- source span:     system prompt ("core metaphor", "BOONDOGGLING", the five capacities)
- status:          deferred — already covered: "Conducting, Not Prompting: The Gru/Minion Split" (published 2026-09-15, PUBLISH-LOG), the planning packages `claude-liam-gru-01`, `-02`, `-05`, and the five-capacities deep-explainer. Pick it to build a tldr version anyway.
