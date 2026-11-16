# PROMPTS — claude-liam-train-the-teacher

Beat-prefixed prompts for open slots.

## There are no open slots.

This reel has **zero** pantry beats, zero archive slots and zero AI-generated
media. Every one of its 35 beats renders from a registered Remotion composition,
so there is nothing for a human or an image model to supply, and no prompt to
write.

That is a deliberate outcome of VOX LAW, not an omission: a still earns a beat
only when the still IS the evidence. The evidence in this film is statutes, cost
reports and effect sizes — text and numbers — so the correct number of stills is
none. See `SOURCES.md` -> "Media, assets and provenance" and
`author_sheet.py` -> `metadata.vox_rationale`.

## If that ever changes

A future edit that adds a pantry beat must, before the next render:

1. add its row to `SHOTLIST.md` with the slot owner set to the human;
2. write its `SHOPPING.md` entry **after** audio lock, with the tier
   (0/1/2/3), the measured duration requirement, and the rights position;
3. add the beat-prefixed prompt here, e.g.

   ```
   ## B14 — <what the still must prove, not what it should look like>
   Tier 2 (specific real object). Needs >= 17.6s of usable motion.
   Rights: verify THE ITEM's licence, not the hosting institution's.
   ```

A prompt that describes atmosphere rather than evidence is the failure this
file exists to prevent.
