# Rebuild prompt
Run from /Users/bear/Documents/CoWork/bear-textbooks/books/. Use the `lecture` skill (brutalist.art/skills/make/lecture/SKILL.md), Liam in for Bear (Kokoro am_onyx), spec: info-7375-computational-skepticism-for-ai/youtube/LECTURES-FIRST-THREE-BRIEF.md (Film 1).
1. narration.py (every spoken line) -> make_sheet.py -> generate_audio_kokoro.py <reel> (then pad BOUT +1.0 s, write 4.008 back, re-run make_sheet.py) -> BOPEN card via skills/make/lecture/templates/title-slide-16x9/build.py --sheet.
2. scenes_act1..6.py + kit.py -> assemble_scenes.py -> scenes.py; build_docs.py.
3. ./brutalist.art/art run <reel> --height 2160 ; ./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape ; bookend_check.py. Never stage/publish/commit/push.
