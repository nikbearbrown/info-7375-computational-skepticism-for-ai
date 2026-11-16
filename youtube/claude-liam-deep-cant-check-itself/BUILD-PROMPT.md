# BUILD-PROMPT — You Can't Check a Model With Itself
`claude-liam-deep-cant-check-itself`

Paste this into a fresh Claude Code session from `books/` to continue or rebuild this reel.

---

## What this is

A `deep-explainer` in the Liam persona (Teardown register) for the `computational-skepticism-for-ai` book, built from Bear's thesis brief on model self-verification. ~7 minutes. 6 acts, 29 body beats, 5 VOX pantry stills.

**Title:** You Can't Check a Model With Itself  
**Slug:** claude-liam-deep-cant-check-itself  
**Reel folder:** `books/computational-skepticism-for-ai/youtube/claude-liam-deep-cant-check-itself/`  
**Voice:** Kokoro am_onyx (free)  
**Channel:** @NikBearBrown

---

## Thesis arc (Bear's argument — do not replace with benchmark framing)

1. A model can't check itself — self-review reflects the same priors that produced the errors.
2. More samples, more effort doesn't escape the same distribution.
3. Family resemblance: errors cluster within model families. Stronger models may cluster tighter.
4. The human is the least-correlated verifier — different priors, different blind spots.
5. The Icon Incident: false premise + phantom workstream + output gate all-clear = the premise gate doesn't exist.
6. Single-vendor = availability bet. Keep families warm. Use the second model adversarially, not as a co-signer.

---

## Gate state to resume from

- [x] PLAN — beat_sheet.json written  
- [x] FACTCHECK.md — complete (4 UNSOURCED claims, all stated qualitatively)
- [ ] **GATE P** — show Bear the narration on animated slates; get approval before audio spend

## To compile a slate previz (after GATE P approval)

```bash
cd books
./brutalist-art/art run computational-skepticism-for-ai/youtube/claude-liam-deep-cant-check-itself
```

## After audio lock — Gate D2

Run pantry_search.py for each VOX beat before writing SHOPPING.md:

```bash
python3 brutalist-art/runtime/scripts/pantry_search.py "feedback loop closed system diagram"   # A2V
python3 brutalist-art/runtime/scripts/pantry_search.py "person monitor reviewing screen"        # A4V
python3 brutalist-art/runtime/scripts/pantry_search.py "checklist shopping list"                # A5V
python3 brutalist-art/runtime/scripts/pantry_search.py "library archive shelf files"            # A5V2
python3 brutalist-art/runtime/scripts/pantry_search.py "branching network diversity paths"      # A6V
```

## Key flags for the builder

- A5SH (shell beat): ClaudeCodeBeat pattern, dark surface. Verify the pattern supports multi-line terminal output props. If not, escalate to BUILD-LOG.md and make the skin extension before continuing.
- A3M (two-bar viz): bars carry NO numeric values — qualitative shape only. Do not add numbers.
- A1R / BASK modelLabel: "Fable 5 (speculative)" — retain the label; this is intentional factcheck compliance.
- OUTRO-LOCK: BOUT must use ClaudeTitleOutro with exact title restate, hardcoded @NikBearBrown, NO subline.

---

## Laws that govern this build (read before touching files)

- `brutalist-art/DESIGN-PRINCIPLES.md` — design grammar, polarity, card forms, icon resolution
- `brutalist-art/VOICE-LOCK.md` — am_onyx only, no random voice picks
- `brutalist-art/OUTRO-LOCK.md` — outro card spec
- `brutalist-art/skills/make/deep-explainer/SKILL.md` — beat-mix quota, vox-run contract, Gate D1/D2
- `brutalist-art/skills/make/ai-explainer/SKILL.md` — inherited laws (COLD OPEN, ASK→RESULT, ILLUSTRATE, HANDOFF, etc.)
