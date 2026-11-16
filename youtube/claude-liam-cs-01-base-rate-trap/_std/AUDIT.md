# AUDIT — claude-liam-cs-01-base-rate-trap
**Date:** 2026-07-25
**Law:** SHOW-DON'T-TELL retrofit

## Beat-by-Beat Classification

| beat_id | narration_gist | current_visual | classification | planned_fix |
|---|---|---|---|---|
| B01 | "Your 99%-accurate test just came back positive — and you're almost certainly fine." | SLATE (title card, B01_Title) | TELLS | Manim: title text animates in with scan-line sweep, terracotta accent flash |
| B02 | "10,000 people enter a clinic. 1 is sick. Test flags 1 true + 99 false positives. 100 flagged. Odds you're sick: 1%." | SLATE (B02_PopulationGridSweep) | TELLS | Manim: 10K dot grid, sweep flags 1 gold + 99 crimson, bucket fills to show ratio |
| B03 | "When a rare condition meets a high-accuracy test, what does a positive result actually tell you?" | VIDEO (SlateCard Remotion) | EXEMPT | Already rendered question card |
| B04 | "1% error × 9,999 healthy = ~100 false flags. 1 true + 99 false = 1% chance after positive." | SLATE (B04_FlaggedBucketFill) | TELLS | Manim: error count grows, bucket fills crimson with 1 teal dot visible |
| B05 | "Accuracy describes per-person behavior. Base rate describes pre-test prevalence. They live in separate equations." | SLATE (B05_RarityNoiseDivergence) | TELLS | Manim: two number tracks separate — accuracy track vs base rate track diverge |
| B06 | "The base rate is the number the test's accuracy is multiplied against — when tiny, a great test drowns in false alarms." | VIDEO (SlateCard Remotion) | EXEMPT | Already rendered mechanism card |
| B07 | "10K dot grid. 1 gold dot (sick). Sweep flags it teal. 99 crimson false positives. Bucket is overwhelmingly crimson." | SLATE (B07_DotGridSweepAndBucket) | TELLS | Manim: animated dot grid sweep — gold flagged teal, 99 healthy flagged crimson, bucket fills |
| B08 | "Not a test flaw. Flaw is how we read '99% accurate.' Accuracy ≠ P(sick | positive). Bucket depends on starting population." | SLATE (B08_AccuracyMisreadHighlight) | TELLS | Manim: wrong equation struck through, correct reading types in as contrast |
| B09 | "Fraud detection: 99% accurate model, fraud = 1/10,000. Positives queue swamped with noise. Analysts clear false alarms." | SLATE (B09_FraudQueueNoise) | TELLS | Manim: fraud queue fills — 1 real fraud vs 99 false alarms — analysts overwhelmed |
| B10 | "Accuracy is wrong metric in rare-event domains. Ask: of all flagged positives, what fraction actually positive?" | SLATE (B10_PositivePrecisionHighlight) | TELLS | Manim: metric label morphs from ACCURACY → PRECISION, precision formula appears |
| B11 | "Fix is not a better model — it's asking base rate question BEFORE build. 99% accurate + 1-in-10K base = 99 false per hit." | SLATE (B11_BaseRateCheckFix) | TELLS | Manim: checklist — base rate question → precision math → false alarm count revealed |
| B12 | "Hospital sepsis model: 98% accurate, 3/1,000 base rate. 35 flags/day, 2 real + 33 false. Nurses start ignoring queue." | SLATE (B12_HospitalSepsisExample) | TELLS | Manim: hospital flag queue builds (35 flags), 2 teal + 33 crimson; nurses deprioritize bottom |
| B13 | "Recap: rarity manufactures noise. Accuracy misleads in rare domains. Audit precision. Ask base rate before deploy." | VIDEO (SlateCard Remotion) | EXEMPT | Already rendered recap card |
| B14 | "Part of the Computational Skepticism for AI series." | VIDEO (OutroSeries Remotion) | EXEMPT | Series outro bookend |
| B15 | "Like and subscribe for more." | VIDEO (OutroCTA Remotion) | EXEMPT | CTA bookend |

## Summary
- TELLS beats: B01, B02, B04, B05, B07, B08, B09, B10, B11, B12 (10 beats)
- EXEMPT beats: B03, B06, B13, B14, B15 (5 beats — already rendered Remotion or bookends)
- SHOWS beats: none (no pre-existing animations)

## Rebuild Plan
All 10 TELLS beats → Manim scenes written in scenes.py
Terracotta moment: B07 (the dot grid bucket fill — highest impact visual)
One terracotta moment per video maximum.

## QC
- scenes.py written: 2026-07-25
- Render: pending (requires manim on host)
