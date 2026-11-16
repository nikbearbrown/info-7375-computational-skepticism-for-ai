# BUILD-PROMPT: claude-liam-why-a-resume-in-json

Stage two of two. The layout is done; this is the mechanical build. Run from `books/` (/Users/bear/Documents/CoWork/bear-textbooks/books).

## Read first, in this order
1. /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/skills/make/ai-explainer/SKILL.md, completely. Every law in it binds.
2. /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/films/why-a-resume-in-json/LAYOUT.md: the beats, what each shows, the narration drafts, the questions still open.
3. /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/films/why-a-resume-in-json/SOURCES.md: what each claim rests on. Do not add a claim that is not in it.
4. The real evidence files in /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/films/why-a-resume-in-json: `skills_trace_check.py` (run it; its printout is B06), `select_view.py` and `select_view_output.txt` (its printout is B09), and the record itself, /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/fall-2026/nik-bear-brown/facts/professor-bear-cv.json (B08 shows its real header lines).

## What is NOT done
No `beat_sheet.json`, no `make_sheet.py`, no scene code, no audio, no render. Author the sheet from the layout in this folder: metadata `channel: claude-liam`, voice Kokoro `am_onyx`, register Teardown, footer `@NikBearBrown`, playlist "Professor Bear Does His Assignments". Every body beat carries a `show` block (SHOW-DON'T-TELL). Beat 2 is `BrutalistHesitantWriter` with `lead_silence_s: 0.8` and the correction `a document you keep editing` -> `a record you keep, and a document made from it`. Run `./brutalist.art/art scenes "<what the beat needs>"` before authoring a beat (GATE L). Apply the Professor Bear law (a person is a portrait, never an icon) and the logo law (a company is shown by its logo).

## Do not change
The claims and the order of the beats. Where a beat needs wording, keep to the layout's draft and the SOURCES.md limits. In particular: no claim about "watermarking" (open question); the hallucination line is limited to what the survey is and gives no venue or year on screen; B03's student stories are Professor Bear's own, told as his, no names; B02 and B03 are constructed illustrations and are captioned as such.

## Commands (from books/)
`python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-why-a-resume-in-json` then `./brutalist.art/art run /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-why-a-resume-in-json`, then every gate to PASS (GATE T, fact-check, visual QC with the frames actually read), then `./brutalist.art/art final /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai/youtube/claude-liam-why-a-resume-in-json --height 2160`. Log fixes in BUILD-LOG.md.

## Stop
Do not publish, stage or upload. Report the master's absolute path, runtime, and any gate that did not pass. Professor Bear signs off before any `post`.
