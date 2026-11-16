# SHOW-TELL THREE MOVES — brief for three course films

## Executive summary
**What this is.** The standing brief for three short show-tell films Bear ordered on 2026-09-27, one for each move in Chapter 1 of *Computational Skepticism for AI*: radical doubt (Descartes), induction (Hume), and falsifiability (Popper). A fourth film, on Plato, comes later and is not part of this batch.
**Why.** Each move gets its own film, so each can make the point Bear cares about: doubt in proportion to risk; induction is powerful until the system changes; and a claim, test or agent that can't fail isn't checking anything.
**Result.** Each film ends as a gated 4K master in its own reel folder in this course's `youtube/`. Nothing is staged or published.

## Bear's words (2026-09-27, dictated; lightly cleaned)
> Make individual show-tell films on radical doubt, induction and falsifiability. Mention the philosophers they are associated with; they are in the chapter.
>
> **Radical doubt.** Talk about Descartes. Talk about how you can't doubt everything, and add risk to that: you should doubt the things that are important to doubt. You can't doubt everything, but you should doubt what your job depends on — health, important things.
>
> **Induction.** Talk about induction and Hume, in another film. Also mention that if the state of the system changes — if the system's ergodicity has changed — then its history is no longer likely to hold up. Don't say induction isn't useful. It's very useful. When induction doesn't hold up, it's because the system has changed: we've had COVID or something, and the way people buy is now fundamentally different because the world has changed. But before that, buying patterns held up. So induction is very powerful, but it can be wrong.
>
> **Falsifiability.** Talk about Karl Popper. You need to frame a question beforehand in a way that it can be wrong. If your test always passes, it's not a test. If your agent always succeeds no matter what it does, it's just doing stuff. If we don't design things beforehand so they could be wrong, we're essentially asserting that they'll always work no matter what.

## Read first, in full
1. `brutalist.art/skills/make/show-tell/SKILL.md` — the doctrine. Read ALL of it.
2. `anthropics/youtube/SHOW-TELL-BATCH.md` — the standing builder brief: spine, rules, batch-2 extra rules (shared scratchpad, whisper-check the greeting, fact-check against RAW primary sources).
3. The sibling course film, built the same day and gated: `info-7375-computational-skepticism-for-ai/youtube/show-tell-skepticism-is-a-method/` — its `make_sheet.py`, `scenes.py`, `FACTCHECK.md`, `build_srt.py`, `BUILD-LOG.md`. Copy its shape, its course-credit placement, and its pronunciation fixes. Don't repeat its body beats: it already did Knight Capital, the turkey, Google Flu Trends, the swans, the sepsis model and the load-tested beam in one pass each. Your film goes deeper on ONE move and should mostly use fresh pictures.
4. Chapter 1: `info-7375-computational-skepticism-for-ai/chapters/01-the-skeptics-toolkit.md`, section "What I mean by skepticism" (lines 33–97). It has Bear's UNCOMMITTED edits: READ ONLY, never modify, never stage anything in that repo.

## Shared spec (all three films)
- **Course film.** Liam, in for Bear, says in the opening (BIDEA): "…with a short film for INFO seventy-three seventy-five, Computational Skepticism for AI." (respelled for Kokoro; captions map it back to "INFO 7375"). On screen: BDEFS title "INFO 7375 · Terms In This Film" and BHTF topic "INFO 7375 COMPUTATIONAL SKEPTICISM · YOUR TURN". The outro stays OUTRO-LOCK: exact title, @NikBearBrown, no subline. Never say "Lecture N".
- **Name the philosopher**, aloud and once on screen, with the work the move comes from. Keep it to the move, not a biography. No portraits: draw objects, not faces.
- **Spine:** BIDEA hesitant writer (greeting + naive question corrected into the real one) → BDEFS (2–4 terms) → drawn isometric Manim beats (ShowTellCard beats only where they pass the card test) → BHTF Your Turn (a concrete prompt read in full, then two checks) → BOUT spoken outro. No length cap: as long as the idea needs and no longer.
- **Pronunciation:** Kokoro says "Descartes" as "discards"; narrate "Day-cart" and map it back in `build_srt.py` (the sibling film does this). Whisper-check "Hume", "Popper", "ergodic", "stationary", "falsifiable", and your greeting; respell only where needed, in the narration, with the caption script mapping it back.
- **Fact-check against primary sources** (FACTCHECK rows PASS / CORRECTED / EXEMPT). Philosophers' positions are stated as their texts state them, with the work named in the row. Every number traces to a primary. Illustrations that aren't data are EXEMPT.
- **Rules:** never stage, post, publish, commit or push; don't edit anything under `brutalist.art/`; touch no other reel; delete nothing (superseded files go to `<reel>/_superseded/`); scratch and renders only under your own scratchpad subfolder (named in your task) or your reel folder, each manim render with its own `--media_dir`; heavy 4K renders run in the background and are polled. Another session's show-tell batch and a sibling builder share this machine.
- **Gates:** A, B, W, V, GATE T, F and bookend all PASS; pre-audit every scene from a scratch copy; look at the frames yourself.
- **Paperwork:** SOURCE.md (the relevant chapter lines verbatim plus Bear's words from this brief), FACTCHECK.md, SOURCES.md, SHOTLIST.md, PROMPTS.md, README.md (executive summary first), BUILD-PROMPT.md, BUILD-LOG.md, build_srt.py.
- **Stop at** `./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape`.

## Film 1 — radical doubt (Descartes)
- **Reel:** `info-7375-computational-skepticism-for-ai/youtube/show-tell-doubt-what-matters/` · **Title:** "Doubt What Your Work Depends On" · **Greeting:** Salaam · **Scratch:** `st-cs-doubt/`
- **The point:** Descartes' method is to ask what would have to be true for a claim to be wrong. But you can't doubt everything — doubt costs time, and a person who doubts everything can't act. So aim the doubt with **risk**: doubt in proportion to what it costs if the claim is wrong. The chair you sit on: don't doubt it. The triage score, the medication dose, the number your job or someone's health depends on: doubt it hard.
- **Useful primary support (verify it in the text):** Descartes himself did not live by total doubt. In *Discourse on the Method* (1637), Part 3, he adopts a provisional moral code for acting while he doubts, including the traveler lost in a forest who should walk straight in one direction rather than wander. In the *Meditations* (1641), doubt is a once-in-a-lifetime exercise for inquiry. Use these only as the texts say.
- **Show risk visually:** a simple likelihood × consequence picture (a grid or a scale), with claims placed on it: most claims sit in the "just act" corner; a few land where being wrong is costly, and those get the doubt. Label it as a way of thinking, not a measured model.
- **Your Turn idea:** list five claims your work relied on this week, mark what it would cost if each were wrong, and run the "what would make this wrong?" move only on the top one or two.

## Film 2 — induction (Hume)
- **Reel:** `info-7375-computational-skepticism-for-ai/youtube/show-tell-induction-until-it-changes/` · **Title:** "Induction Works Until the World Changes" · **Greeting:** Konnichiwa · **Scratch:** `st-cs-induction/`
- **The point:** induction — expecting the future to resemble the past — is very useful, and most of the time it works. Hume's point (*An Enquiry Concerning Human Understanding*, 1748, sections IV–V) is that the past gives no logical guarantee, and yet custom, as he calls it, is how we live. Induction holds while the process that produced the history stays the same. It fails when the system changes.
- **The example Bear gave:** buying patterns held for years; then COVID changed how people buy, and forecasts built on the old history broke. Find a primary number for the shift (for example the US Census Bureau's quarterly e-commerce share of retail sales, 2020) and show it as a history line that breaks. If a number isn't verified from its primary, don't show it.
- **The technical words, used correctly.** A process whose statistical rules don't change over time is *stationary*; that is the property induction quietly relies on. Bear used the word *ergodic*: include it only if it can be said correctly in one line (roughly: whether one history tells you what the whole system does — the average over time matches the average across all the cases), and log in BUILD-LOG how it was handled. Don't let either term become a lecture.
- **The balance matters:** never imply induction is useless. The honest rule: trust the pattern while the system that produced it is the same; when the world changes, go back and check.
- **Your Turn idea:** pick one pattern your team or model relies on, write down what would have to change in the world for it to stop holding, and name a signal that would tell you the change had happened.

## Film 3 — falsifiability (Popper)
- **Reel:** `info-7375-computational-skepticism-for-ai/youtube/show-tell-a-test-that-cant-fail/` · **Title:** "A Test That Can't Fail Isn't a Test" · **Greeting:** Namaste · **Scratch:** `st-cs-falsify/`
- **The point:** Karl Popper (*The Logic of Scientific Discovery*, German 1934, English 1959; *Conjectures and Refutations*, 1963): a claim is scientific only if some possible result could prove it wrong. Frame the question *before* you look, in a form that can fail. A test that always passes isn't testing anything. An agent that "succeeds" no matter what it does is just doing stuff. If we don't design things beforehand so they could be wrong, we're asserting they'll always work, no matter what.
- **Pictures to consider:** a test that passes whether the code is right or wrong (a checkmark that lights up for everything); the same test rewritten with a stated fail condition; an agent that grades its own work; a claim rewritten from "the system is robust" to one with a number, a window and a threshold (the chapter has a table of these — the rows are its own illustrative examples, EXEMPT). Popper's black swan is fine but was used in the sibling film; if you use it, do something new with it.
- **Your Turn idea:** take one claim, test or agent success check you rely on, and write the specific result that would prove it wrong — before you run it. If you can't name one, it isn't a check yet.
