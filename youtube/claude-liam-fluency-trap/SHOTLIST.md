# SHOTLIST — claude-liam-fluency-trap
# Typed work order per beat. Gate F closed; audio locked (8:20). Pass 1.

## OPEN — BOOKEND / OPEN (B00)

B00 · ClaudeComposerAsk · 16.46s
  source: own (Remotion)
  action: render FluencySegmentCard → media/B00.mp4
  pattern: ClaudeComposerAsk
  props: greeting="Merhaba, Liam", command="Why do I trust well-written
         things more — and should I still?", runningText="weighing the
         polish…", output=["Fluency was a proxy for effort and competence.",
         "The proxy broke. The feeling didn't.", "That gap is the trap."]
  show: ask types → running indicator → output lands (0.75)
  status: RENDERABLE (no missing deps)

## ACT I — The Cheap Bet (B01–B04)

B01 · FluencySegmentCard · 7.58s
  source: own (Remotion reel-local)
  action: render → media/B01.mp4
  props: title="The Cheap Bet", index="I"
  status: RENDERABLE

B02 · VOX SLATE · 11.76s  [R1 beat 1/2]
  source: archive (SHOPPING.md — pantry/B02.png not yet supplied)
  action: slate with R1 handoff data; kenburns event at t=0, label at t=0.6
  motion: kenburns, focus [0.50, 0.42], 2.0× tight open
  handoff: camera {x:0.50, y:0.42, scale:2.0}, objects [{id:athens-plate}]
  status: SLATE — awaiting pantry/B02.png

B03 · VOX SLATE · 12.84s  [R1 beat 2/2]
  source: archive (same plate as B02)
  action: slate; camera eases OUT from R1 handoff to full fresco
  motion: kenburns, focus [0.50, 0.50]
  status: SLATE — same plate as B02; both resolve when B02.png lands

B04 · FluencyDivergence · 14.78s
  source: own (Remotion reel-local)
  action: render → media/B04.mp4
  props: a="the polish (still cheap to read)", b="the thought (no longer required)"
  show: two chips linked → link severs at t=0.5 on "snapped" → reader-eye
        tracks POLISH; terracotta ring on the eye at t=0.85
  status: RENDERABLE

## ACT II — The Feeling of Ease (B05–B09)

B05 · FluencySegmentCard · 6.24s
  props: title="The Feeling of Ease", index="II"
  status: RENDERABLE

B06 · MANIM · 13.25s
  class: B06_EaseDial (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B06_EaseDial
          mv → manim/B06.mp4
  show: two claim cards → ease meter fills for clean → TRUE/TRUST dials
        tick up → "content held constant" stamp at t=0.85
  status: RENDERABLE (scenes.py authored)

B07 · FluencyThreshold · 11.74s
  source: own (Remotion reel-local)
  action: render → media/B07.mp4
  props: axis="cue influence", gate="awareness",
         note="structural fixes beat willpower — the cue dies when named"
  show: unlabeled ease cue flows at full strength → label snaps on at t=0.55
        → stream thins on "discount"
  status: RENDERABLE

B08 · VOX SLATE · 12.50s
  source: ai (SHOPPING.md — pantry/B08.png not yet supplied)
  action: slate; kenburns push toward marked page at t=0; halo label t=0.55;
          terracotta ring on grade at t=0.85
  motion: kenburns, focus [0.45, 0.50]
  status: SLATE — awaiting pantry/B08.png

B09 · MANIM · 13.80s
  class: B09_TwoHalos (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B09_TwoHalos
          mv → manim/B09.mp4
  show: one author mark → two essay cards fan out → judge marks rate author
        twice → polished lifts, rough sinks → "the bet was good. once."
  status: RENDERABLE

## ACT III — The Honest Signal (B10–B15)

B10 · FluencySegmentCard · 5.74s
  props: title="The Honest Signal", index="III"
  status: RENDERABLE

B11 · MANIM · 15.24s
  class: B11_SpenceCurves (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B11_SpenceCurves
          mv → manim/B11.mp4
  show: two cost curves rise at t=0 → gap shaded at t=0.6 →
        "the asymmetry IS the machine" in terracotta
  note: schematic axes, no invented units
  status: RENDERABLE

B12 · FluencySourceFlow · 15.94s
  source: own (Remotion reel-local)
  action: render → media/B12.mp4
  props: stages=["talent / practice / hours", "fluent prose",
                 "the reader's inference"], note="the proxy earns its keep"
  show: three feeder chips → PROSE chip glows at t=0.6 → reader-mark
        reads it instead of feeders
  status: RENDERABLE

B13 · VOX SLATE · 9.94s
  source: ai (SHOPPING.md — pantry/B13.png not yet supplied)
  action: slate; kenburns push toward page in platen; "the price was the
          proof" label at t=0.6
  motion: kenburns, focus [0.50, 0.48]
  status: SLATE — awaiting pantry/B13.png

B14 · MANIM · 14.06s
  class: B14_Pooling (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B14_Pooling
          mv → manim/B14.mp4
  show: two Spence curves return → steep flattens onto shallow at t=0 →
        separating point vanishes at t=0.5 → $26 card with citation at t=0.8
  note: $26 figure with "Freelancer.com study, 2025" citation on screen
  status: RENDERABLE

B15 · MANIM · 15.53s
  class: B15_Quintiles (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B15_Quintiles
          mv → manim/B15.mp4
  show: five quintile bars at old rates → top drops -19% on "nineteen" →
        bottom rises +14% on "fourteen" → terracotta arrow on top at t=0.7
  note: figures with persistent citation line from B14
  status: RENDERABLE

## ACT IV — The Breakdown (B16–B23)

B16 · FluencySegmentCard · 4.87s
  props: title="The Breakdown", index="IV"
  status: RENDERABLE

B17 · MANIM · 16.42s
  class: B17_CoinFlip (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B17_CoinFlip
          mv → manim/B17.mp4
  show: 49.9 bar beside 50 coin-flip line → they align → second bar 56
        with "high agreement" band → "confidently wrong together" serif
  note: both figures cited on screen (systematic review)
  status: RENDERABLE

B18 · ScaleComparison · 13.70s
  source: own (Remotion — registered composition)
  action: render → media/B18.mp4
  props (ScaleComparison schema):
    data: {
      slideMeta: "UK psychology-modules exam study, cited on screen",
      axis: {min: 0, max: 100, unit: "%"},
      band: {from: 0, to: 6, label: "flagged / detected"},
      items: [
        {label: "Undetected (94%)", value: 94},
        {label: "Scored higher", value: 100}
      ]
    }
  OVERRIDE: treat as illustrative — use FluencyScale reel-local for correct
  props semantic; see beat_sheet.json for updated pattern
  status: RENDERABLE

B19 · ClaudeComposerAsk (micro ask) · 9.96s
  source: own (Remotion)
  action: render → media/B19.mp4
  props: greeting="", segment="Measure what, exactly?",
         command="Write the naive AI-text detector: score a text by low
         burstiness, low perplexity, low sentence-length variance — the
         standard recipe.", runningText="writing the detector…", output=[]
  status: RENDERABLE

B20 · NikBearBrownCodeBlock · 16.22s
  source: own (Remotion — Onda code block)
  action: render → media/B20.mp4
  props: filename="naive_ai_score.py", topic="FLUENCY TRAP",
         segment="NAIVE DETECTOR", code=<content of code/naive_ai_score.py>
  show: code reveals with voice → trailing comment block highlights at t=0.65
  note: real file; comment block is the beat's point
  status: RENDERABLE

B21 · MANIM · 19.15s
  class: B21_FalseFlag (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B21_FalseFlag
          mv → manim/B21.mp4
  show: bar rises to 61.3 with citation at t=0 → three writer marks slide
        under same signature bracket at t=0.55 → "punished for being
        atypical" in terracotta at t=0.85
  note: 61.3% figure cited (Stanford study); neurodivergent extension
        NOT quantified on screen
  status: RENDERABLE

B22 · FluencyVerdictStamps · 16.46s
  source: own (Remotion reel-local)
  action: render → media/B22.mp4
  props: (no data props — scene is hardcoded per real-person care)
  show: essay card + three stamps (100% AI · HUMAN · HUMAN) → institution
        sides with AI stamp at t=0.55 → gavel; citation card
        "Newby v. Adelphi Univ., 2026" at t=0.85 (name on card only)
  status: RENDERABLE

B23 · FluencyDivergence · 15.17s
  source: own (Remotion reel-local)
  action: render → media/B23.mp4
  props: a="the verified version", b="the viral version (same polish)",
         note="ties to the provenance-cap rule in the epistemology episode"
  show: two identical citation cards → checkmark trail lands on one;
        other strikes through but loses no polish at t=0.5 →
        "fluency is not provenance" at t=0.85
  status: RENDERABLE

## ACT V — Where It Bites (B24–B27)

B24 · FluencySegmentCard · 5.42s
  props: title="Where It Bites", index="V"
  status: RENDERABLE

B25 · FluencyChipGrid · 16.18s
  source: own (Remotion reel-local)
  action: render → media/B25.mp4
  props: chips=["grading", "hiring", "disclosure", "peer review"],
         foundation="assumes polish is costly"
  show: four chips light up in narration order at t=0 → one foundation bar
        under all four → cracks at t=0.7
  status: RENDERABLE

B26 · VOX SLATE · 15.02s  [R2 beat 1/2]
  source: ai (SHOPPING.md — pantry/B26.png not yet supplied)
  action: slate with R2 handoff data; tight on salutation at t=0;
          "the tell is gone" label at t=0.65
  motion: kenburns, focus [0.50, 0.45], 1.7× open
  handoff: camera {x:0.50, y:0.45, scale:1.7}, objects [{id:letter-plate}]
  status: SLATE — awaiting pantry/B26.png

B27 · VOX SLATE · 14.93s  [R2 beat 2/2]
  source: ai (SHOPPING.md — pantry/B27.png not yet supplied)
  action: slate; camera eases OUT from R2 handoff to room of letters
          "cheap to send · expensive to answer" label at t=0.7
  motion: kenburns, focus [0.50, 0.55]
  status: SLATE — same family as B26; resolves when B27.png lands

## ACT VI — What Survives (B28–B32)

B28 · FluencySegmentCard · 11.04s
  props: title="What Survives", index="VI"
  status: RENDERABLE

B29 · FluencySourceFlow · 18.65s
  source: own (Remotion reel-local)
  action: render → media/B29.mp4
  props: stages=["outline", "messy draft", "revision", "what-changed notes"],
         note="track milestone artifacts", banned="keystroke / pause telemetry"
  show: SourceFlow chips → keystroke-timeline strip appears and gets struck
        through at t=0.55 → burst-writer's gap-then-spike shown inside
        struck strip at t=0.85
  status: RENDERABLE

B30 · FluencyDivergence · 16.68s
  source: own (Remotion reel-local)
  action: render → media/B30.mp4
  props: a="tests understanding", b="tests performance (the halo, relocated)"
  show: question chip probes decision chip at t=0 → smooth-talker mark
        scores high on delivery, flat on understanding at t=0.5 →
        safeguard chips land at t=0.85
  status: RENDERABLE

B31 · MANIM · 17.52s
  class: B31_RubricDemotion (scenes.py)
  action: manim -qh --fps 24 -r 1920,1080 scenes.py B31_RubricDemotion
          mv → manim/B31.mp4
  show: four rubric rows + score dials at t=0 → mechanics dial replaced by
        binary pass/fail toggle at t=0.55 → polish lever tugs rubric;
        terracotta ring on disconnected linkage at t=0.85
  status: RENDERABLE

B32 · FluencyThreshold · 16.44s
  source: own (Remotion reel-local)
  action: render → media/B32.mp4
  props: axis="what passes", gate="traceable + disclosed",
         note="callback: gettier-risk / provenance-cap from episode 1"
  show: "traceable" claim passes gate at t=0; "merely confident" waits
        outside → disclosure chip passes cleanly; detector chip greys out
        with 61.3 echo at t=0.6
  status: RENDERABLE

## CLOSE (B33–B35)

B33 · ClaudeVerdictArtifact · 20.66s
  source: own (Remotion)
  action: render → media/B33.mp4
  props: artifactTitle="Polish pays nothing", artifactLines=[
    "Fluency is felt ease — evidence of nothing, until named.",
    "It was honest only while polish was costly.",
    "The cost hit zero; the signal died, the feeling didn't.",
    "Detectors relocate the harm onto atypical humans.",
    "Score what stays expensive: process, depth, defensibility."
  ]
  show: five lines land with the voice; 0.5s lead silence
  status: RENDERABLE

B34 · ClaudeComposerAsk (YOUR TURN) · 35.78s
  source: own (Remotion)
  action: render → media/B34.mp4
  props: greeting="Your turn.", runningText="paste this into Claude…",
         command=<full prompt from beat_sheet.json>
  show: prompt typed as Liam reads it aloud
  status: RENDERABLE

B35 · ClaudeTitleOutro · 2.93s
  source: own (Remotion)
  action: render → media/B35.mp4
  props: title="The Fluency Trap", handle="@NikBearBrown",
         subline="Computational Skepticism for AI"
  status: RENDERABLE

---

## Summary

| Lane | Count | Status |
|---|---|---|
| VOX (vox beats) | 6 (B02 B03 B08 B13 B26 B27) | SLATE — awaiting pantry |
| MANIM | 8 (B06 B09 B11 B14 B15 B17 B21 B31) | RENDERABLE — scenes.py authored |
| REMOTION reel-local | 9 (B01 B04 B05 B07 B10 B16 B22 B23 B24 B25 B28 B29 B30 B32) | RENDERABLE — FluencyTrap.tsx |
| REMOTION shared | 7 (B00 B18 B19 B20 B33 B34 B35) | RENDERABLE — registered compositions |
| BOOKEND | 3 (B33 B34 B35) | ↑ included above |

Pass 1 expects exactly 6 slates (the SHOPPING.md beats).
All other beats should render to media/ or manim/.
