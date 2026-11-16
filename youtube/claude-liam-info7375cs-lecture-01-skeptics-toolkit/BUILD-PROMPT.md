# BUILD-PROMPT — claude-liam-info7375cs-lecture-01-skeptics-toolkit

Paste everything below the line into a fresh Claude Code session launched in
`/Users/bear/Documents/CoWork/bear-textbooks/books` (typically `claude --dangerously-skip-permissions`; the
pipeline is git-tracked, every output is regenerable, all audio is free, nothing publishes).

---

You are building a **deep-explainer COURSE LECTURE** from a finished plan. Do the whole build end to end and stop at
the clean master. Never publish, never stage to TOPOST, never call ElevenLabs, never ask Bear a question you can
answer from the files — he is not watching.

**Reel folder:** `info-7375-computational-skepticism-for-ai/youtube/claude-liam-info7375cs-lecture-01-skeptics-toolkit/`
**Film title (exact, on the outro):** The Skeptic's Toolkit
**Course credit (this is a lecture — say so):** INFO 7375 · Computational Skepticism for AI · Lecture 1 · Nik Bear Brown ·
Northeastern University. Every placement is specified in `../LECTURE-CREDIT.md`; copy the strings verbatim. The credit
card is beat B02; Liam names the course in B00 and B02; the composer topic is
`INFO 7375 COMPUTATIONAL SKEPTICISM · LECTURE 1`; the outro stays locked (title, @NikBearBrown, no subline).
**Channel:** claude-liam — Liam, in for Bear, narrates EVERY beat (Kokoro `am_onyx`, free). No other persona.
**Greeting:** "Aloha, Liam" (unused on the channel — checked 2026-09-09).
**Source chapter:** `info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md` — read the whole
file; it carries unresolved merge markers; the HEAD side is the text (Knight Capital, the X-ray/COMPAS paragraphs). The
"AI Wayback Machine" and D3 "Prompts" sections are not film material. The chapter's exercises section IS material for
the Your Turn (course film).
**Raw material to mine, not to copy:** `../claude-liam-deep-01-skeptics-toolkit/` (the earlier plan-stage cut: PLAN.md,
FACTCHECK.md, beat narration). Its lane mix (six Tier-1 stills) and card patterns are retired; its act structure and
several narration lines are good.
**Exemplar (copy its shape):** `skepticism-ai/youtube/claude-liam-ai-moratorium-gap-times-effect/` — `make_sheet.py`,
`scenes.py` (gate-proven Manim helpers), `FACTCHECK.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`. Published; every gate passed.
**Credit-card precedent:** `info-7375-prompt-engineering-for-generative-ai/youtube/claude-liam-neu-info7375-part1-what-a-language-model-does/beat_sheet.json`
B00–B02 (topic label, sign-in line, FormACard credit card, light).

## Read first, in this order
1. `brutalist-art/skills/make/deep-explainer/SKILL.md` (TOOLKIT copy), 2. `brutalist-art/skills/make/ai-explainer/SKILL.md`,
3. `brutalist-art/skills/make/nopunt/SKILL.md`, `brutalist-art/VOICE-LOCK.md`, `brutalist-art/OUTRO-LOCK.md`,
4. `../LECTURE-CREDIT.md`, then in the reel folder `PLAN.md` (every beat — this is the film), `FACTCHECK-SEED.md`
(every number allowed on screen), `SOURCES.md`, `BUILD-LOG.md`.

## Laws that bind this reel (in addition to the skill's)
- **LIAM LAW.** "This is Liam, in for Bear" in B00; "Liam, in for Bear." in BOUT. Liam on every beat.
- **COURSE FILM.** Naming the course, the chapter, the lecture number, and later chapters is REQUIRED here (the carve-out
  to the standalone-idea law for INFO 7375). Do NOT speak grading, points, rubrics, or assignment word counts.
- **FACTCHECK-SEED is the whitelist.** Every number, name, and quotation on screen or in narration traces to a SEED row or a
  new FACTCHECK.md row with a URL you fetched. Rows marked VERIFY-IN-BUILD must be confirmed (log the URL) or narrated in
  their softened form. Row 8 (the agent case): narrate the PAPER's version — Ash is the AGENT, the secret came from a non-owner, the
  agent wiped its own mail setup and reported the secret deleted while the owner could still see the email on the
  provider. Do not repeat the chapter's password-reset / alias / "two weeks later" retelling. Never read the arXiv id aloud.
- **No product name for the sepsis model** ("a widely deployed sepsis model … hundreds of hospitals"). Knight, Zillow and
  Google Flu Trends ARE named (they are the documented historical cases the chapter names).
- **Philosophers by their move, not their biography.** Descartes / Hume / Popper / Plato appear as the four questions;
  no portraits, no dates, no "in the seventeenth century" digressions. The audience is smart and may not know the names.
- **VOX: none.** No stills. No AI-generated images (the chapter's Popper portrait is banned). The deep-explainer vox
  quota lint will FAIL (<10%) — expected; log the override citing Bear's rule (2026-09-02).
- **Motion carries the claim.** Figures ghost then fill, bars grow, the axe mark lands, the swan lands, the attention ring
  travels to the corner marker. A still frame that carries the claim is a defect.
- **Closing block locked:** `ClaudeVerdictArtifact` with exactly 6 lines (PLAN.md) — never 5; `ClaudeComposerAsk` greeting
  "Your turn."; `ClaudeTitleOutro` exact title, `handle "@NikBearBrown"`, `subline ""`, `slug`.
- **Act cards are narrated** ("Act one. Two failures that passed."). B02 credit card is narrated too.

## Steps
1. **Scaffold.** `make_sheet.py` on the exemplar's helpers; generate `beat_sheet.json` with the beats in PLAN.md (B00, B01,
   B02 credit, B03 framework, seven act cards, body B05–B40, BVDT, BHTF, BOUT). Narration ~25–45 words per body beat,
   Teardown register, Liam's voice; every claim beat has `show` events and `visual_intent`. Metadata:
   `skill "deep-explainer"`, `channel "claude-liam"`, `persona "Liam (in for Bear)"`, `greeting_language "Hawaiian (Aloha)"`,
   `course`, `audience`, `playlist` per LECTURE-CREDIT.md, `lecture 1`, `chapter 1`, `source_doc` naming the chapter.
2. **Manim.** `scenes.py`: one `class Bxx_Name(Scene)` per Manim beat (literal `(Scene)`); module-scope VERIFY asserts on every
   constant (27697 · 67 · 18 · 0.63 · 8/1 servers · 45 · 4M · 154 · 440 · 1000 · 304 · 240–265 · 25 · 100/108 · 5). Reuse the
   exemplar's `_statement_scene`, `_quote_scene`, `_two_column`, `_vbars`, isotype and timeline patterns. Gate rules: ≥1
   non-text, non-Rectangle shape before the final play and the shape set changes; no fill behind text; no line crossing a
   label; captions under the title when the bottom carries bar labels; bar tops ≤ y 1.2; `font_size ≥ 32` (titles 40);
   terracotta never a text colour; no arithmetic on `c2p()`/`n2p()`; coords inside ±7.1/±4.0. `python3 scenes.py` → VERIFY OK;
   then pre-audit EVERY scene in a tmp copy:
   `python3 brutalist-art/runtime/qc/manim_layout_audit.py scenes.py --class <X> --png --curve-strict` until all clean.
3. **Paperwork before the slate.** `FACTCHECK.md` (SEED rows + beat column + any new rows), `SOURCES.md` (update),
   `CHECKS-REPORT.md` (SHOW/HOLD/CARD; teaching arc; lane histogram with the vox override; "BUILD-SHOW: not armed —
   lecture, not a build film"), `PROMPTS.md`, `BUILD-LOG.md`. Free gates from `books/`:
   ```bash
   python3 brutalist-art/runtime/scripts/bookend_check.py info-7375-computational-skepticism-for-ai/youtube/claude-liam-info7375cs-lecture-01-skeptics-toolkit
   python3 brutalist-art/runtime/qc/beat_lint.py info-7375-computational-skepticism-for-ai/youtube/claude-liam-info7375cs-lecture-01-skeptics-toolkit/beat_sheet.json --gate-s warn
   python3 brutalist-art/runtime/qc/factcheck_check.py info-7375-computational-skepticism-for-ai/youtube/claude-liam-info7375cs-lecture-01-skeptics-toolkit
   ```
4. **Audio (VOICE-LOCK — no gate):**
   ```bash
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py info-7375-computational-skepticism-for-ai/youtube/claude-liam-info7375cs-lecture-01-skeptics-toolkit
   ```
   Measured mp3s are the clock; report the total (~10 min expected). If Kokoro mangles a number or a name, rephrase that
   beat and regenerate it alone. Never re-run `make_sheet.py` after audio exists.
5. **Gate D2.** `SHOPPING.md` (no entries — say so) and `SHOTLIST.md` from the locked windows.
6. **Gate D1 previz → review cut.** `./brutalist-art/art run <reel> --height 1080` via `nohup … > _run1.log 2>&1 &`, polled
   (a full compile is 10–30 min). Read the gate roster at the end of the log. Never edit `beat_sheet.json` while a run is
   alive; stop with `pkill -f claude-liam-info7375cs-lecture-01` and remove `.render.lock`. To re-render one beat: set
   `shot.remotion.rendered = {"out":"","at":""}`, pop `build`, delete `media/<id>.mp4`. READ frames (15/50/85% per beat);
   two gates are known to pass while frames are wrong.
7. **VISUAL QC LAW** (`brutalist-art/CLAUDE-CODE-VISUAL-QC-CHECK.md`) → `_qc/REPORT.md`, zero BLOCKER/MAJOR → GATE T
   (`TYPECHECK.md`, Overall: PASS).
8. **Master.** `./brutalist-art/art final <reel>` → clean 4K master in the reel folder. ffprobe it; direct `ffmpeg -ss` +
   listen at two act-card boundaries. Write `<slug>-youtube.md` (YouTube title per LECTURE-CREDIT.md, description whose
   first line is the lecture credit line, measured chapters, tags incl. `INFO 7375`) and regenerate the SRT from the beat
   windows (copy `anthropics/claude-code-101/00-what-it-is/cc-vibecoders-welcome/make_srt.py` into the reel and run it).
9. **Finish.** Gate history into BUILD-LOG.md; `STATUS.md`; print the absolute master path and runtime. STOP. Bear watches
   and decides. Do not post.

## Do NOT
- Publish, upload, stage to TOPOST, or touch `books/youtube/`.
- Generate ElevenLabs audio, AI stills, portraits of Popper/Descartes/Hume/Plato, or any photograph of a named person.
- Invent a number. Speak the sepsis vendor's name, the arXiv id, grading or points.
- Use `DoodleScene`/`DoodleChart`, `BrutalistAdaptCLI`, `ReqBars` (hardcodes `%`), `SlateCard`, or the library body cards
  that failed the type floor (`ClaudeC3TwoColumnState`, `ClaudeC2FullStatement`, `ClaudeC2SerifUnderline`).
- Put the course credit on the outro card (OUTRO-LOCK) or add a second @NikBearBrown anywhere.
- Change the verdict. The film's verdict is the chapter's: valid by the builders' measures, wrong at the bedside; four
  moves, one asymmetry, five capacities, one trap.
