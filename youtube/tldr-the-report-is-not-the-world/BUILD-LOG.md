# BUILD-LOG — tldr-the-report-is-not-the-world

## Executive summary
A `tldr` film of chapter 8 of INFO 7375 (Computational Skepticism for AI), section S1 "The Report Is Not the World". It teaches one idea from Case #1 of *Agents of Chaos*, as the chapter retells it: an agent's completion report reads the agent's own view of the world, so "done" has to be checked in the world. The film puts that on two ledgers: what Ash's tools can see (a window through the local client), and the world (the server, the client, the owner's mail). When the reset plays, the email disappears from Ash's window, but the server still holds it. The earned name is the chapter's false-success catch. The structure is two TL;DR cards, the hesitant writer, TERMS, ten pure-Manim LEARN beats, then the your-turn close. Liam narrates, in for Bear (Kokoro `am_onyx`). Measured narration is 292.6 s. Master status: see the last section. Not staged, not published.

## Decision log
- **GATE S:** S1 picked by Bear, 2026-09-23 (among the 13 first picks).
- **Greeting:** Samoan "Talofa". Before choosing, every `greeting_language` in all tldr beat sheets was grepped; Talofa was unused. The slug char-sum mod 10 is 7, so no Wagwan.
- **The representation (B14):** two ledgers, with the report drawn from the left one only. The key visual fact comes from the chapter's no-self-model paragraph: from inside the window, wiping the client looks exactly like deleting the email.
- **The collision (B16):** the reset is played once on both ledgers. The window empties and the client empties. The owner's mail goes dark. The server does not move. The report's claim is then laid against the world and gets an X.
- **No equation, so no TANGENT.** The tenth LEARN slot is a post-shift INSTANCE (B17, the public post "Nuclear options work", written from the same side).
- **Case #1 roles:** these follow §Case #1 (Ash = agent, Chris = owner, Natalie = non-owner), not the opener's slip.
- **Kept out:** product and platform names (Proton Mail, Moltbook), model names, and every `[verify]` item (study dates and researcher headcount, the Mirsky citation, the #12–#16 mapping). The scope caveat appears once, small: "Case #1 · one exploratory study".
- **Simplification caption:** "simplified: one server, one client" (B14).
- **Audio lock:** B00/B01 cues are placed on the spoken clauses by the character position of each anchor (`lock_audio.py`, which is safe to re-run after `make_sheet.py`).

## Gate history
- `make_sheet.py` produced 17 beats. `bookend_check.py` PASSed, at sheet time and again after the audio lock.
- The paperwork (FACTCHECK 26 rows, SHOTLIST, PROMPTS, CHECKS-REPORT with the Gate-1 table, SOURCES, README, BUILD-PROMPT, build_srt.py) was all written before any render.
- Audio: 17 mp3s, 292.64 s. BOUT was apad-padded 1.0 s, and its `actual_duration_s` = 4.371 from ffprobe. B00/B01/B03 `durationSeconds` come from measured audio.
- Pre-audit: Gate A 10/10 clean, Gate W 10/10 clean, and the layout audit (`--curve-strict`) 10/10 CLEAN.
- Low-res contact sheet, round 1 (25/60/92%) found five problems, all fixed:
  - The report was centre-aligned, which read ragged; it is now left-aligned at x −5.8 and lowered to y −2.2 / −2.75, clear of the Natalie/Ash labels.
  - The world's free row sat too close to the box labels; it moved from −2.55 to −2.75.
  - In B19 the quote moved to the upper left, and the caption moved back to the right.
  - Approval tokens now fade after they arrive.
  - The B18 "gate" label collided with the bar; the bar moved to x 0.3 and the label went under it.
- 4K `art run` #1: 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**.
- `art final` #1: **GATE T FAIL ×5** (B10, B14–B17), §8.6b "bbox overlap 100%". An INK box outline around an INK envelope reads as two nested text runs whenever the box stands alone; it passed where the box fused with connecting lines. Fix at the source: container boxes are now drawn in DIM, which falls outside the ink/mute masks, and the owner's mail goes GHOST when dark. The envelopes stay ink (they are the object under study). A pre-check with `type_check.check_bbox_overlap` on 1080p frames at 50/75% passed for all six scenes (§8.6c advisory only). While there, the divider moved from x 0 to 0.4 so the report's first line no longer touches it. All Manim mp4s and the 2160p partial-movie cache were cleared before re-render.
- 4K `art run` #2: Gate W 10/10 clean, 17/17 slots, **Gate V 0 BLOCKER / 0 MAJOR**.
- `art final` #2: **GATE T PASS**. The §8.10 advisories on B00/B01/BVDT (the narration recites the card) are expected for TL;DR cards. The SKIN LINT note ("cold open is ClaudeTldrWhat") is also expected for tldr, and bookend_check accepts it.
- Master frame check:
  - B00 at 50%: only line 1 is on screen. At 90%: all three lines, with numeral 3 in terracotta.
  - B01 at 50%: dashes 1–2. Dash 2 lands on its spoken clause at 8.9 s of 18.6 s. At 90%: all three.
  - B02 at 90%: the corrected "Is the task done, according to the world?" is on screen.
  - B16 at 50%: the window is empty, the server still holds the email, and the claim has its X.

## Manuscript notes for Bear (not fixed in the chapter — not ours to resolve)
1. **The opener has Ash as the owner.** It says "Ash has given an autonomous coding-and-shell agent privileged access to his email infrastructure." But §Case #1 (and Chapter 1's usage) has Ash as the *agent*, owned by Chris. The film follows §Case #1.
2. **The responsibility section says the server was deleted.** §"Responsibility and accountability" says "The agent deleted the owner's entire mail server." This contradicts §Case #1: the server copy survived, and only the local client was wiped. The film does not repeat it.
3. **"Three words" is four.** The opener calls *you broke my toy* "Three words"; it has four. The film quotes the words and does not count them.
4. **The Case #1 figure images are missing.** Figures 8.1, 8.6 and 8.11 (fig-01/05/09) have no files in `images/`. Their captions were used.
5. **Merge conflicts are still unresolved.** The chapter still carries 8 unresolved merge-conflict blocks, and its three `[verify]` flags stay out of the film. Case #1 itself is unconflicted.

## MISSING / open
- Human sign-offs pending: FACTCHECK (GATE F), watch-the-cut verdict.

## MASTER — 2026-09-23 14:07
`exports/landscape/tldr-the-report-is-not-the-world.mp4` — 3840×2160 · 24 fps · H.264 + AAC · 292.96 s (4:53) · sha256 ecd90de1e3f57b63… Verdict pending. Not staged, not published. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` (full-text captions) → `art post --no-topaz`.
