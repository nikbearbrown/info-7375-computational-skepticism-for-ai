# BUILD-LOG — You Can't Check a Model With Itself
`claude-liam-deep-cant-check-itself` | 2026-07-28

---

## Gate state

- [x] PLAN written (beat_sheet.json)
- [x] FACTCHECK.md complete
- [ ] GATE P — Bear reviews narration on animated slate; approves audio spend
- [ ] Audio (Kokoro am_onyx, free by default)
- [ ] Audio lock → word clock
- [ ] Gate D2 — SHOPPING.md written from locked durations (after audio lock)
- [ ] Gate D1 — slate previz compiled (`./art run`)
- [ ] Pantry fill (Bear drops stills)
- [ ] Review cut + VISUAL QC + TYPECHECK
- [ ] `./art final`

---

## Decisions log

**2026-07-28 — Plan authored**

Source: Bear's brief (thesis arc on model self-verification). Not a chapter — thematic bonus to the claude-liam-deep series.

Hook: opens on the Fable 5 vs Opus "overthinking" framing, reframes fast — the wrong question is which model, the right question is whether any model can check itself.

Title: "You Can't Check a Model With Itself" — declarative, thesis in the title, Teardown register. Tested against the OUTRO-LOCK requirement: exact restate at BOUT.

Slug: `claude-liam-deep-cant-check-itself` — no episode number (this is a thematic bonus, not a chapter map video).

Beat mix (29 body beats): VOX 17.2% / MANIM 27.6% / REMOTION 34.5% / CARD 20.7% — LINT PASS, all lanes in band.

Vox run: R1 = A5V + A5V2 (Icon Incident pantry pair). 2 beats, max 3, does not cross act boundary. Handoff block in A5V.

All narration: am_onyx / kokoro. No ElevenLabs spend. VOICE-LOCK compliant.

Polarity: ~70% light (6 FormACard dark=false, 2 dark=true for A1R2 and A3R2 + 1 dark=false for A4R2). Shell skin at A5SH is diegetic-dark (terminal surface). Compliance: weighted light per DESIGN-PRINCIPLES.

OUTRO-LOCK: BOUT uses ClaudeTitleOutro with title restate, @NikBearBrown hardcoded, no subline, slug-seeded mascot/polarity/jingle.

"Fable 5": labeled speculative in narration and in modelLabel. No benchmark scores claimed.

**Icon Incident worked example**: the incident is the session that commissioned this video. Sourcing: VERIFIED-OBSERVED. The beat sequence (A5V → A5V2 → A5R → A5SH → A5M) carries the full arc: false premise accepted → phantom workstream → output gate all-clear → what the manifest should have said → quality gate definition.

**A5SH shell skin**: ClaudeCodeBeat pattern specified for the terminal manifest display. This is a dark-surface diegetic beat — real terminal surface, not a generic card. 

MISSING/FLAG: ClaudeCodeBeat may not natively support a multi-line terminal-output prop (its design is typically for a single command + response). The builder should: (1) check whether ClaudeCodeBeat's `lines` prop supports pre-rendered terminal history, OR (2) use NikBearBrownTerminalAsk adapted for output display, OR (3) add a ShellOutput variant to the shell skin library. Do not fake the interface with a card.

**A3M viz**: two-bar Manim concept chart for within-vs-across family correlation. Bars carry NO numeric values — qualitative shape only. Labeled "Within family" (tall, terracotta) / "Across families" (short, ink). The UNSOURCED direction of the stronger-model effect is noted in the scene description. If Bear can source this, the annotation can be confirmed; until then, the bar annotation reads "stronger model →" as a directional arrow, not a measured value.

**No FormBCard beats**: no icon library entries needed for this video. All card beats are FormACard. If the thesis points were to be enumerated in a FormBCard, icons would be needed — but that's not the design.

**No gen-AI clips**: DESIGN-PRINCIPLES §1 compliance. Every beat is Manim, Remotion, VOX pantry still, or CARD. No AI-generated video anywhere in the body.

---

## Pantry shopping (pre-GATE-D2 notes — formal SHOPPING.md after audio lock)

Five VOX pantry stills needed. All Tier 1 (generic illustrative — no real people, no specific real objects, no rights escalation):

| Beat | Description | Tier | Motion |
|---|---|---|---|
| A2V | Circular feedback loop or closed-system diagram | 1 | kenburns, focus [0.5, 0.4] |
| A4V | Abstract person-at-monitor (no identifiable individual) | 1 | kenburns, focus [0.55, 0.45] |
| A5V | Checklist / shopping list with new item being added | 1 | kenburns, focus [0.5, 0.5] |
| A5V2 | Library / archive of items already on shelf | 1 | kenburns, focus [0.5, 0.55] |
| A6V | Abstract branching / diversity diagram (no logos) | 1 | kenburns, focus [0.5, 0.5] |

Tier 0 library pass (pantry_search.py) must run before writing formal SHOPPING.md. These notes are pre-search estimates only.

---

## Open questions for Bear at GATE P

1. Is the "stronger models cluster tighter within family" claim one Bear can source? If so, provide the paper — the A3M viz can carry the citation and the bars can get an approximate scale.
2. A5SH shell skin: should this use ClaudeCodeBeat as-is, or does it need a ShellOutput extension? Bear decides before the review cut.
3. Episode numbering: this video is filed as a bonus (no episode number in series). If Bear wants it numbered, assign an episode number and update metadata.
