# FACTCHECK — tldr-gru-validated-not-attempted

**What this is.** Every claim the film speaks or shows, checked against the Gru persona Bear pasted on 2026-09-24 (saved verbatim as `SOURCE.md`). **Result:** PASS, with one source contradiction resolved in the gate list's favour and the constructed case labelled on screen.

Status: PASS (plan gate) · 2026-09-24 · checked by Claude (Opus 5.5) for Bear

Protocol: rows are SOURCE (the paste says it), PERSONA (Gru's own backstory or opinion — spoken as "in Gru's telling" / "in Gru's words", never as a fact about the world), or CONSTRUCTED (the film's illustration, built from the paste's own examples and captioned on screen).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Gru is a persona that conducts Claude through a software design | PASS (SOURCE) | System prompt: "You are Gru, a senior software architect and design documentation consultant"; "programming as conducting". | — |
| 2 | B00, BVDT | Five phases; no phase starts until the one before it is validated | PASS (SOURCE) | "The five gates"; each gate "Cannot start until /vN−1 is validated"; menu: "sequential — each phase gates the next". | — |
| 3 | B10, B14, BVDT | The five phases are problem, needs, principles, components, assembly (SDD) | PASS (SOURCE) | Gate list: /v1 Problem Intake, /v2 User & Business Needs, /v3 Architecture Principles, /v4 Component Mapping, /v5 SDD Assembly. Asserted in `scenes.py` (PHASES). | — |
| 4 | B01 | Claude will write a polished design even for the wrong problem | PASS (SOURCE, softened) | Gate 1: "Claude will happily write a beautiful SDD for the wrong problem and never tell you it's wrong." Film drops "never tell you" to keep the claim to what a viewer can test. | — |
| 5 | B01 | "In Gru's telling, the outage doesn't come from bad code. It comes from a decision nobody made explicitly." | PASS (PERSONA) | Session start: "the outage is never caused by bad code. It's caused by a decision nobody made explicitly." Attributed to Gru; "never" dropped. | — |
| 6 | B01 | Vague needs upstream turn into mush downstream | PASS (SOURCE) | Gate 2: "if they're mush, everything downstream inherits the mush." | — |
| 7 | B02 | "I'm not here to build your rocket faster." | PASS (SOURCE, verbatim quote, 9 words) | Session start, first sentence. | — |
| 8 | B11, B12, B16 | Every component must trace to a specific need from phase two; otherwise Gru asks which need it serves or calls it scope creep | PASS (SOURCE) | Gate 4: "Every component in the design must trace to a specific need from /v2. No orphans. … I stop and ask which need it serves — or I tell you it's scope creep." **Contradiction in the paste:** behavioral rule 1 says the need comes "from /v4"; the gate list and the menu both say /v2. The film follows the gate list. Logged for Bear in SOURCES.md. | — |
| 9 | B11 | "Reduce checkout abandonment caused by the three-step address form" is a need Gru offers as a good one | PASS (SOURCE, verbatim) | Gate 2: "… passes it." Asserted in `scenes.py` (SPEC). | — |
| 10 | B12 | "we might as well add" components | PASS (SOURCE) | Gate 4: "the 'well, we might as well add...' components". | — |
| 11 | B13, B14 | "Improve user experience" fails the needs gate | PASS (SOURCE, verbatim) | Gate 2: "'Improve user experience' fails this gate." | — |
| 12 | B14, B17, BVDT | No valid output from the next phase until this one is validated — not attempted; not mentioned earlier in the chat | PASS (SOURCE) | Opening: "you cannot get a valid output from phase N+1 until phase N has been validated — not just attempted. Not 'we talked about it.' Not 'I mentioned it earlier in the chat.'" | — |
| 13 | B14 | The needs gate asks whether a need could turn out to be wrong | PASS (SOURCE) | Gate 2: "Every need named here must be falsifiable — something you could be *wrong* about." | — |
| 14 | B17 | Skip a phase and Gru names exactly what's missing and holds the line | PASS (SOURCE) | "What happens if you try to skip one": "I name exactly what's missing, I don't proceed on the skipped phase"; menu: "I'll tell you what's missing and hold the line." | — |
| 15 | B17 | "a guess wearing a decision's clothes" | PASS (PERSONA, verbatim quote, 6 words) | "What happens if you try to skip one". Spoken as "in Gru's words". | — |
| 16 | B19 | Silent mode skips every gate; for when you know what you want and need output, not supervision | PASS (SOURCE) | "The exception": "`silent` skips all of this — no intake, no pushback, no gates … using me for output, not for supervision." | — |
| 17 | B19 | /claude, the boondoggle score, ignores the gates; scores whatever exists at any stage across the five supervisory capacities | PASS (SOURCE) | "The one thing that ignores gates entirely"; behavioral rule 7. | — |
| 18 | B19 | Neither exit is the default; the gates are the point | PASS (SOURCE) | "Use it deliberately, not by default. The gates are the point of hiring an architect instead of a stenographer." | — |
| 19 | BHTF | "restate my problem so that it could not describe ten other systems" | PASS (SOURCE) | Gate 1 and behavioral rule 3 ("could describe ten different systems"). | — |
| 20 | B10–B18 | A checkout design; a single-page address form; a recommendation widget; checkout breaking at 2 a.m.; "two months later" | EXEMPT (CONSTRUCTED) | Built around the paste's own examples (the 3-step address form need, "might as well add", "when something goes wrong at 2am"). Captioned "constructed example" in B10. Not a real incident. | — |
| 21 | B13 | "The needs section says what first drafts often say: improve user experience" | EXEMPT (CONSTRUCTED) | Illustrative; the paste names it as the failing example, not as a measured frequency. "Often" is the film's framing, not a statistic. | — |
| 22 | B13–B16 | The fog: a vague need is a target any trace can land in; a validated need is one point | EXEMPT (REPRESENTATION) | The film's picture of the paste's claim that downstream sections "inherit the mush". Not a claim about how Gru is implemented. | — |

## Not in the film
The persona's "20+ years" backstory, the Ada lineage, the artifact-window output rule, and behavioral rules 2, 4 and 6 (principles contradictions, "we'll figure it out in implementation", precision in language). Gate 3 (principles) and gate 5 (assembly) appear only as phases that close.
