# BUILD-PROMPT.md — claude-liam-silent-sql-failures

Paste into Claude Code from `books/`:

---

Build a deep-explainer reel. Slug: `claude-liam-silent-sql-failures`. Build into:
`computational-skepticism-for-ai/youtube/claude-liam-silent-sql-failures/`.
Source: `books/computational-skepticism-for-ai/youtube/silent-sql-failures-source.md`.

Frame: Liam asks Claude "What feedback would Professor Bear give Zhenhao on their
Computational Skepticism final project?" The body IS that feedback.
**FIRST NAME ONLY: always "Zhenhao", never the full name.**

Voice: claude-liam, Kokoro am_onyx, free. Never publish.

The beat sheet, scenes.py, PLAN.md, FACTCHECK.md, SOURCES.md, BUILD-LOG.md, and
PEDAGOGY.md are already written. Run:

1. Kokoro audio:
   `python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     computational-skepticism-for-ai/youtube/claude-liam-silent-sql-failures`

2. Write SHOPPING.md from timings.json (6 VOX beats: A1V, A2V, A3V, A4V, A5V, A6V).

3. Compile the slate previz:
   `ART_FACTS=0 ART_STRICT=0 ./brutalist-art/art run \
     computational-skepticism-for-ai/youtube/claude-liam-silent-sql-failures`

4. Open the slate: `open .../claude-liam-silent-sql-failures-slate.mp4`

5. Run type check and fix any §8.5 failures.

Standing rules: audio-first (never hand-bake clips); 14pt legibility floor on all
Manim labels; render Remotion only via runtime/scripts/remotion_scenes.py; EB Garamond
font wrapper in scenes.py active.
