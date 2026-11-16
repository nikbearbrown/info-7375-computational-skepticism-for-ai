# SAVE-STATE — claude-liam-pick-your-pebble
_Timestamp: 2026-07-30_

## 1. Primary Request and Intent
Build the reel "Pick Your Pebble" (Video 1 of the Agentic Casebook series) using the ai-explainer skill, channel claude-liam (Liam voice, Kokoro am_onyx, free). Build folder: `books/computational-skepticism-for-ai/youtube/claude-liam-pick-your-pebble/`. Source: `books/computational-skepticism-for-ai/assignments/agentic-casebook-red-team.md` (Step 1 only). The reel teaches ONE thing: how to pick the agentic system to red-team and write its Dossier.

**Specified arc**: COLD OPEN (ClaudeComposerAsk) → THE FAST FILTER (FormBCard 4-up) → FASTEST PATH TO DONE (Manim) → WHY CARING HELPS (Manim) → THE DOSSIER (FormACard + FormBCard 3-up + FormBCard 3-up) → THE ONE DISCIPLINE (Manim) → VERDICT (ClaudeVerdictArtifact) → YOUR TURN (ClaudeComposerAsk) → OUTRO (ClaudeTitleOutro)

**Session locks**: nopunt on FormBCard icon cards; Manim for movement; PANTRY-FIRST; NEVER doodle; STOP AT GATE P (slate previz only); spend NOTHING on audio (Kokoro is free/not gated); never publish; STOP at slate cut and write CHECKS-REPORT.md.

## 2. Key Technical Concepts
- Beat structure: B00(ClaudeComposerAsk,20s), B01(FormBCard 4-up,22s/actual), B02(Manim,16.66s actual), B03(Manim,12.74s actual), B04(FormACard,7.40s actual), B05(FormBCard 3-up,7.68s actual), B06(FormBCard 3-up,10.69s actual), B07(Manim,11.80s actual), BVDT(ClaudeVerdictArtifact,6.83s actual), BHTF(ClaudeComposerAsk YourTurn,14.63s actual), BOUT(ClaudeTitleOutro,~8s/null)
- B02 and B03 Manim scenes pass GATE B; B07 fix applied but not yet confirmed
- Calibrated cueFrames: B01=[144,225,300,375]; B05=[15,45,105]; B06=[18,84,255]
- `ART_FACTS=0` used to bypass FACTCHECK.md gate for previz
- PEDAGOGY.md written with `VERDICT: PASS`
- All 10 MP3s generated (BOUT has no narration)
- B02.mp4 and B03.mp4 rendered and media-filled

## 3. Current Work
The last B07 layout fix (SUCCESS REPORT at y=1.1 sz=26, LIES? at y=0.42 sz=48, ✓ at y=-0.15 sz=38) was applied to `scenes.py` and the art run was kicked off as a background task (just completed, exit code 0).

## 4. Pending
- Check layout_audit.md to confirm B07 passes (0 errors)
- If pass: full slate compile is done; run GATE T (type_check.py), GATE V (visual QC), write CHECKS-REPORT.md, STOP for Bear review
- If fail: read error, fix B07 again
