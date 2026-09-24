# Gru turn 18-phase1-gate-s1-inventory

## Professor Bear typed

```
Flag 1, the prototype, named honestly:
- repo_scan: reads the repo's structure (languages, top-level layout, key files and their first headings, declared commands, runnable modules, tests, CI, docs, existing skills, TODO markers, recent commits), writes a JSON and a Markdown report, skips .env files, and records environment variable names only. It does NOT do D22: nothing claim-anchored, no term search, no method tags, no redaction of secret-shaped values in files it reads. It's a structural pass only, so it serves U3 in part and U2 not at all yet.
- The gate-state tracker: sections move draft to confirmed, and confirming requires a named person; gates record who and when. No prompt hash (D12). Serves U4 and B1 in part.
- Checker one, the SDD shape: /v0 is one sentence; /v2 has 3–4 principles with honors, violates, failure state and a collision test; /v3 has three flows and no "the system processes the request"; /v4 has 5–8 needs with pass/fail conditions; /s1 components have their parts and a Need; open questions have an owner and status; a share of paragraphs carry labels. But it checks the old three labels, not DOC/CODE/STUDENT/GRU, and no excerpts. Serves U1 and B1 in part.
- Checker two, the Score's format: step headers, a capacity label and action on human steps, a prompt, expected output and a testable handoff on Claude steps, and summary counts that match, including the zero-capacity flag. It doesn't check labels inside prompts. Serves U5 in part.
- The skills: a hub, scan, v0, and intake, written against the superseded three-label scheme. None of the others exist.
So every prototype piece maps to a Need, and none of them meets it yet. That's the honest state.

Flag 2: tie it to U4. The menu has to be truthful about what exists.
Flag 3: (b). The section path, /v0 through /p5, /g1 and /claude, plus /help and /list. Everything else shows "not in this version," like the deferred commands.

With those answers: yes, the Phase 1 gate reflects what I'm building toward. Confirmed. Go to /s1.
```

## Gru replied (verbatim, unedited)

The Phase 1 gate is confirmed. Systems and architecture start now.

**Logged:**
- **D28:** The "not in this version" line serves U4. The menu has to be truthful about what exists.
- **D29:** v1 scope is /v0 through /p5, /g1, /claude, /help and /list. Every other command shows "not in this version."
- **Prototype audit:** every piece maps to a Need, and none of them meets its Need yet. I'll hold /s1 to that. Each component below is documented against its Need, not against what the prototype currently does. The prototype's gap then shows up as a difference between the two, not as the design itself.

Two things in your prototype description conflict with locked decisions, plus one gap in scope:

**1. Checker one requires "a share of paragraphs" to carry labels. P2 says *every claim*.** A threshold is exactly how P2 would erode: 80% labelled means one in five claims has no source. It also shows that we never defined what a *claim* is. Is it a paragraph, a sentence, or a bullet? Until that's defined, "every claim" can't be tested, and it will stay a percentage. This goes to /d1's shared vocabulary as the first term to define. For now I'm logging it as **OQ11**. It must close before checker one's rules are specified in /s1.

**2. The gate-state tracker records "a named person," and D11 makes that file reviewable in a team repo that may be public.** B1 needs to show that *she* confirmed each gate. It doesn't need her full name in git history. Options:
- her git identity (`user.name`), whatever she has set
- a handle she chooses at install
- a role ("design author") plus a git-signed commit

Logging this as **OQ12**. It must close before /s3.

**3. /g1 is in scope but maps to no Need.** Scope (b) includes it, and the component filter has nothing for it. The natural mapping is U6. The compiled SDD is what a reviewer reads in the pull request. Confirm or correct that.

---

**/s1: Before a single component is documented**

OQ4 (codes or aliases for skill folder names) was due to close before /s1. Before you answer it, it rests on an assumption I want to make explicit. It assumes **one skill folder per command**. Under D29, that's 17 section commands plus /g1, /claude, scan, and the hub, so about 21 folders. Each one points into the same verbatim prompt, and each one could drift from it.

What changes from one command to the next is **the section of the prompt**, not the machinery. Every section command does the same four things: scan, ask with labelled claims, handle CONFLICTs, then write the section and gate it. So the more basic question is how many skills there should be:

| Option | Shape | Cost |
|---|---|---|
| **(i) One per command** | `gru-v0` … `gru-p5`, `gru-g1`, `gru-claude`, `gru-scan`, hub. About 21 folders. | 21 things to keep aligned with one prompt file. OQ4 matters a lot. |
| **(ii) One per job** | `gru` (hub, routing, self-check), `gru-scan`, `gru-section` (runs any /v0 to /p5 command against its prompt section), `gru-compile` (/g1), `gru-score` (/claude), `gru-share`. Six folders. | `gru-section` has to handle /v0's hard gate and /v1's one-question-at-a-time rule as prompt-driven behavior, not code. |
| **(iii) Hub only** | One skill. Everything else is scripts. | Claude Code sees one large instruction file. Discovery is simplest, and the context load is heaviest. |

My recommendation is **(ii)**. It follows your own rule that skills point into the prompt and never paraphrase it. It keeps the number of places that can drift to six. And OQ4 mostly goes away, because the job names (`section`, `score`, `share`) are neither codes nor aliases.

The cost is honest. Your prototype's `v0` and `intake` skills would become two sections run by `gru-section`, not two folders. They're being rewritten for the new labels anyway, so the rework is small.

---

**Proposed /s1 component inventory under (ii), in documentation order**

| # | Component | Serves | Prototype |
|---|---|---|---|
| 1 | `gru-scan`: layered relevance, method tags, P4 skip and redaction, read log, excerpts | U2, U3, U1 | Structural pass only. Missing D22 and redaction. |
| 2 | `gru-section`: runs any section command, labelled claims, CONFLICT as next question, section file with pushback in order | U1, U2, U4, B1 | `v0` and `intake` skills on old labels |
| 3 | State tracker: gates, confirmer, prompt hash, SHA, folder name | U4, O2, B1 | Gates plus who and when. No hash. |
| 4 | `decisions.md` writer: D and OQ numbers, raised, decided, applied | U4, B1 | none |
| 5 | `gru` hub: translation layer, truthful menu, self-check, gate enforcement, drift and hash announcements | All, O1, O2, U4 | Hub on old labels |
| 6 | `gru-score`: labels survive, CONFLICTs become human tasks | U5 | none |
| 7 | `gru-compile` (/g1) | U6 (pending confirmation) | none |
| 8 | `gru-share` with the secret check | U6 | none |
| 9 | `./gru` shim: install, uninstall, doctor | O1 | Unknown. Does the prototype have an entry script? |
| 10 | Checker one: SDD shape, all claims labelled, excerpts, answers present | U1, B1 | Shape checks. Old labels, threshold, no excerpts. |
| 11 | Checker two: Score format, labels inside prompts, no CONFLICT used as fact | U5 | Format only |

The scan goes first because U2 depends on it most and the prototype is furthest from it. Everything downstream consumes its read log and its claims.

---

**To start documenting:**
1. Skill architecture: (i), (ii), or (iii)? If (i), answer OQ4 as well.
2. /g1 mapped to U6: confirm or correct?
3. Does the prototype include the `./gru` entry script, and what does it do today?
4. Is the inventory and its order right? Is anything missing?

OQ11 and OQ12 don't block component 1. They block components 10 and 3 respectively, and we'll close each one before documenting that component.
