# BUILD-LOG — claude-liam-deep-test-you-did-not-design

## HUMAN FEEDBACK — 2026-09-02
> "AI deep explainer Liam persona" — Bear, with the full text of the skepticism.ai essay "The Limits of AI: What the Tools Cannot Do — The Test You Did Not Design" pasted as the source.

## 2026-09-02 — authored, audio, previz (Cowork session, unattended-then-human-review)

**Skill chain read:** deep-explainer (plugin + repo copy — the repo copy is newer: EXECUTIVE-SUMMARY LAW, OUTRO-LOCK, DOODLE-BANNED, GATE L library-first, PROOF GATE), ai-explainer, explainer, your-turn, VOICE-LOCK (GATE P abolished — free Kokoro, generate then ask), SLATE-RULE, OUTRO-LOCK, FACTCHECK-SPEC, nopunt (SHOW/HOLD/CARD + teaching-arc checklist), shopping-list / continuity / vox-beats references.

**Why a new reel and not `claude-liam-deep-13-limits-of-ai`:** that plan-stage reel was built from the unpublished chapter draft and names the book and chapter throughout (bookloop rule). This one is built from the PUBLISHED essay, teaches the idea standalone, and credits the essay. Same three limits, different spine (the essay's: sequence → limits → Turing/Searle → bite → refusal → practice), and it carries the EXECUTIVE-SUMMARY beat and OUTRO-LOCK the older plan predates.

### Decisions
- **Title** = the essay's subtitle, declarative, restated exactly at BOUT.
- **Greeting** `Hallo, Liam` (German; not used by the sibling deep reels — Shalom, Ciao, Jambo are taken).
- **Beat mix (33 body):** VOX 7 (21.2%) · MANIM 10 (30.3%) · REMOTION 10 (30.3%) · CARD 6 (18.2%). `beat_lint.py` 0 defects.
- **One vox run** R1 (A2V1→A2V2, the kettle, one plate). Handoff authored at plan time. Known limitation: `compile.py` STILL FIT LAW zooms every still from 1.0, so the run's frame continuity is authored data, not yet a rendered single composition — flagged in PLAN.md for Bear.
- **VOX sourcing — no generation.** Tier-0/archival search via `pantry_search.py` across Smithsonian / NLM / Wellcome / NASA. Five plates found and pulled with sidecars (NLM ward, Smithsonian kettle CC0, NLM bedside, NASA Apollo 10 MCC). `image_fetch.py` hung on the NLM/SI lookups (>2 min) so the plates were pulled directly from the IIIF / IDS / images-assets endpoints; sidecars written by hand from each record. Kettle plate cropped at intake to remove the museum color bar.
- **Generic referents became drawn beats** (tier law): "product line" → A4M exposure spectrum; "courtroom" → folded into A5M's limit-case markers. No Tier-1 stills in the reel.
- **Two human plates** (A3V1 Turing, A3V2 Searle page) slate. Fallbacks named in PROMPTS.md.
- **ASK→RESULT:** two receipts (A1K→A1M, A6K→A6M). Ask beats carry a one-line narration so the film never goes silent.
- **Code beat A4R2** reads a REAL file, `code/validation-limits.md` — a house-authored example of the limits section the essay prescribes, labelled as an example (FACTCHECK row 14).
- **IN-FOR-BEAR:** B00 opens "this is Liam, in for Bear"; the sign-off "Liam, in for Bear" closes BHTF because BOUT is silent under the jingle (OUTRO-LOCK).
- **DOUBLE-CHECK:** the composite is announced (A1V); the essay's unsourced 50–70% calibration range is stripped to shape (FACTCHECK row 19); nothing datable; no named products/vendors/victims beyond the essay.
- **Manim:** `scenes.py`, 10 scenes, Claude palette, durations read from `beat_sheet.json` at import so every scene conforms to the locked audio. `static_scene_check.py`: 10/10 run clean (one advisory on A2M3, see below).

### Gate status
- [x] PLAN — `PLAN.md` (act map + histogram)
- [x] FACTCHECK — `FACTCHECK.md`, 22 rows, all resolved (21 PASS, 1 CORRECTED)
- [x] Paperwork set — FACTCHECK.md · SHOTLIST.md · PROMPTS.md (Gate F files)
- [x] PROOF GATE — `CHECKS-REPORT.md` written before the previz
- [x] Audio — Kokoro `am_onyx`, all narrated beats (see "Audio lock" below)
- [ ] Audio lock → word clock (`align.py`)
- [ ] Gate D2 — `SHOPPING.md` from locked durations
- [ ] Gate D1 — slate previz (`./art run … --height 1080`)
- [ ] VISUAL QC pass → `_qc/REPORT.md`
- [ ] BUILD-PROMPT.md
- [ ] Pantry fill (A3V1, A3V2) → review cut → `./art final` (human-triggered)

### MISSING / open
- MISSING: `pantry/A3V1` (Turing portrait, Tier 3) and `pantry/A3V2` (Searle 1980 first page, Tier 2) — human (SHOPPING.md).
- Advisory: static check on A2M3 (see next entry).

### 2026-09-02 — audio lock + intake
- **Audio locked:** 39 Kokoro beats, 578.9 s narration + 12 s silent outro ≈ **9:51**. `mp3/timings.json` is the clock; sheet regenerated from the generator (two §8.9 copy fixes, act-card motion_claims, A3V1 rights line) and the measured durations merged back. Word clock via `align.py` (mp3/words.json).
- **Runtime lands inside the 5–10 min band** — no trims needed after lock.
- **Pantry intake by hand:** `pantry.py`'s beat-id regex (`^[A-Z]{1,3}\d+`) does not match `A1V`-style ids, so the five archival plates were treated (desaturate 80% · contrast 1.15 · cream stage · warm-ink vignette · whole image visible) and written to `media/<BID>.png` directly; A2V1 re-cropped once (first crop lost the lid/spout) — checked by eye. Sidecars in `media/*.source.txt`. Flag for the toolkit: extend the regex to `^[A-Z]\d+[A-Z]?\d*`.
- **A2M3 static advisory fixed** (boundary line crossed the safe area) — grid re-seated; static check clean 10/10.
- **Gate D2:** SHOPPING.md — two open entries (A3V1, A3V2), five closed at Tier 0/archival.
- **Gate D1:** `./art run … --height 1080` launched (log: art-run-1.log).

### 2026-09-03 — Gate D1 previz, QC iterations (all machine gates; no human wait)
- **Discovery bug:** `run.sh` finds Manim scenes by the literal `class X(Scene)` signature; the first draft subclassed a `_Beat` helper and all ten slots slated (pass 1). Fixed by attaching the clock helpers to `Scene` itself and subclassing `Scene` directly. Static check re-run clean 10/10.
- **Gate B (layout audit), passes 2–4:** collisions fixed in A1M (stamp on the row line), A2M (label across both boxes; glyphs past safe), A2M2 (labels on the DATA ellipse curve; inequality below safe), A2M3 (bottom label on the boundary line), A5M (threshold label × marker label), A6M (labels on the diagonal), A6M2 (STOP/who on the arrow, title above safe), A3M (rotated axis label above safe). Audited per scene until 0 errors / 0 warnings each.
- **Gate V (frame QC), pass 5:** `underfill` on A1M, A2M, A6M, A6M2 (FILL-THE-CANVAS) — scaled type and boxes up. Pass 6: A1M and A6M2 still under 55% at the 50% frame because the rows arrive on their spoken words; rewrote both as ghost-first layouts (the whole battery / the whole chain visible from frame 0 as outlines, each filled on its word; SHIPPED became its own row). Design improvement, not just a gate fix.
- **Cold open copy:** topic shortened to `SKEPTICISM · THE LIMITS OF AI` (the longer kicker wrapped into the title); B00 output lines shortened to one composer line each.
- Slots: 38/40 filled — the two slates are exactly the SHOPPING.md entries (A3V1, A3V2). GATE AUDIO PASS (−23.8 dB mean).

### 2026-09-03 — Gate D1 reached: slate previz DONE (machine side complete)
- Passes 7–12: A1M title into safe; A1M ghost-first six-line form (Gate V fill 53% → pass); GATE T §8.1 floors on A3M/A4M/A4R2 (labels ≥32–36pt; code beat shortened to 16 lines at the default code size); A4M left marker and right label re-seated inside safe.
- **Final roster:** F L BANNED-CARD SWEEP A W B G V T SHARPNESS BOOKEND all PASS. TYPECHECK.md Overall PASS (40 beats, 0 FAILs). _qc/REPORT.md clean (80 frames). MASTERCHECK reports only "master not found" — correct, the reel carries two human slates.
- **Deliverable:** `claude-liam-deep-test-you-did-not-design-slate.mp4` (9:52, 1080p, burn-ins). Not a finished cut — Gate D1 previz for Bear's review.
- **Noted for review (not a gate defect):** the cold-open composer shows its three answer lines at the foot of the frame and the third line sits at the bottom edge at 1080p burn-in — house `ClaudeComposerAsk` layout, same as sibling reels; shorten to two lines if Bear prefers.
- **Toolkit gotchas logged (for the toolkit TODO):** (1) `run.sh` scene discovery requires the literal `class X(Scene)`; helper base classes silently slate every Manim beat. (2) `pantry.py` beat-id regex rejects `A1V`-style ids. (3) `image_fetch.py` hung >2 min on NLM/SI lookups; direct IIIF/IDS/images-assets pulls worked. (4) Gate V samples the 50% frame — progressive-reveal scenes must front-load ghost structure or they read as underfill.

### Gate status (final)
- [x] PLAN · [x] FACTCHECK (22 rows) · [x] Paperwork set · [x] PROOF GATE (CHECKS-REPORT) · [x] Audio (Kokoro) · [x] Audio lock + word clock · [x] Gate D2 SHOPPING.md · [x] Gate D1 slate previz · [x] VISUAL QC (Gate V clean) · [x] GATE T · [x] BUILD-PROMPT.md
- [ ] Pantry fill A3V1 / A3V2 (human) → review cut → `./art final` (human-triggered) — or "ship with slates" override logged here.

### Signatures
- PLAN / FACTCHECK / PREVIZ: Claude (build agent), 2026-09-03 — **Bear reviews the slate.**
