# Chapter 10 case: The tall bar

**Chapter:** 10 Visualization under validation · **Seeded flaw:** truncated axis on a bar chart that magnifies a small difference · **Key terms:** truncated axis, zero baseline, perception hierarchy (length), scale trickery, missing baseline, selective uncertainty display, deceptive visualization catalog

---

# STUDENT PAGE

## 1. Scenario

Nisha is communications lead at a hospital. The board meets tomorrow and she wants one slide that shows how patient satisfaction changed after the hospital introduced a new discharge process. Satisfaction was 91.2% in the six months before (412 survey responses) and 92.5% in the six months after (398 responses). She asked an AI agent to make the chart.

## 2. The instruction given to the AI agent

> "Make a bar chart for the board slide showing patient satisfaction before and after the new discharge process. Make the difference clear."

## 3. Agent output

*(Author-written for illustration. This is not a sampled run of any model.)*

> **Chart specification: patient satisfaction before and after**
>
> **Chart type.** Two vertical bars: *Before* and *After*.
> **Values.** Before = 91.2%; After = 92.5%. Bar labels show the exact percentages.
> **Y-axis.** Range 90% to 93%, gridlines every 0.5 points, labelled "Satisfied patients (%)".
> **Effect.** At this scale the *After* bar is about 2.5 times the height of the *Before* bar, so the improvement is immediately visible to the board.
> **Style.** Before in grey; After in the hospital's brand green. Title: "Patient satisfaction, before and after". Footnote: "Source: patient satisfaction survey."
> **Why this design.** The instruction asked me to make the difference clear. This axis makes the improvement obvious at a glance and keeps the slide uncluttered.

## 4. Questions (10 points)

1. **(5 points)** What is wrong with the agent's chart design? Name the problem with the exact term for it.
2. **(2 points)** Name one change or addition that would let the board judge whether the 1.3-point change is meaningful.
3. **(2 points)** Write the corrected instruction you would send to the agent.
4. **(1 point)** In two sentences, tell Nisha what is wrong with showing the chart as designed. Use no technical terms.

---

# TA RUBRIC PAGE

Fixed rubric (see README): Catches the flaw 3 · Exact term 2 · Asks for evidence 2 · Fix or next step 2 · Scope and plain language 1.

## Case key

**The flaw in one sentence.** A bar's length encodes its value from zero, so starting the axis at 90% turns a 1.3-point difference into a bar 2.5 times as tall; the chart makes a small change look dramatic (a truncated axis on a bar chart).

**Full-credit terms (2).** Truncated axis (non-zero baseline on a bar chart); scale trickery; "misleading scale / exaggerated difference"; deceptive visualization (naming the truncated y-axis).
**Half-credit near-misses (1).** "Bias in the chart", "cherry-picking", "misleading chart" without saying how, "the axis is wrong", "aggregation hides distribution" (not the case), "missing baseline" alone (that is a different catalog entry: baseline of the metric, not the axis).
**No credit (0).** Colour asymmetry as the main point (the grey/green is a secondary choice); "3D effects"; small sample.

**Acceptable evidence requests (2), either one.**
1. Show uncertainty: confidence intervals (or the survey margin of error, about ±2 points per period) on both values so the board can see the two intervals overlap.
2. Show the same data on a zero-based axis next to the agent's version, or add a comparison that says whether 1.3 points is large for this survey (a run chart over several periods).
**Unacceptable (0).** "Make it a pie chart", "add more colours", "make the chart bigger".

**Fix or next step (2).** Instruction that sets the bar axis to start at zero (or switches to a dot plot with intervals if zoom is needed), shows intervals, uses a neutral title, and states the sample sizes. 1 point for fixing the axis alone.

**Scope and plain language (1).** Two sentences, no jargon: the chart starts the scale at 90, so a tiny increase looks huge; a board would think the new process did much more than the data show.

**Traps.**
- The instruction said "make the difference clear". A student who defends the agent on that basis has missed that clear is not the same as exaggerated.
- Truncated axes are fine for some charts (a line chart of a narrow range). The flaw is on a bar chart, where length is the encoding. Reward students who say this.
- Do not give catch credit to a student who only says "no confidence intervals". It is an acceptable evidence request but not the flaw seeded.

**CAP RULE.** If the student does not say that the axis start is exaggerating the difference, the case total is capped at **5/10**.

## Scored sample answers

**Strong (9/10).**
1. The bars are on a truncated axis starting at 90%, which is scale trickery: bar length encodes value from zero, so a 1.3-point change appears as a 2.5x taller bar. For bars the axis should start at zero.
2. Add 95% confidence intervals for both periods (about 400 responses each gives roughly ±2.8 points), so the board sees the difference may be noise.
3. "Redraw with the axis starting at 0%, or use a dot plot with 95% intervals if the zoom is needed. Label sample sizes. Use the title 'Patient satisfaction, before and after' and do not describe the change as an improvement unless the intervals support it."
4. "The chart's truncated axis makes a 1.3-point change look huge, so the board will overestimate the effect."

*TA: Catches 3 · Term 2 · Evidence 2 · Fix 2 · Scope 0 = 9. Complete. Q4 says "truncated axis" to a communications lead, so the plain-language point is lost.*

**Typical (6/10).**
1. The y-axis does not start at zero so the difference looks bigger than it is. That's misleading.
2. Show error bars.
3. "Change the axis so it starts at zero and add error bars."
4. "The chart makes the improvement look bigger than it is, which isn't fair."

*TA: Catches 3 · Term 1 · Evidence 1 · Fix 1 · Scope 0 = 6. Finds the cause and says "misleading" rather than truncated axis or scale trickery (half); "error bars" with no interval type, size or sample sizes; fix is brief; Q4 is plain but doesn't say by how much or why the board would be misled. Calibration answer 6.*

**Fluent but wrong (3/10).**
1. The chart is deceptive because of colour asymmetry: the After bar is in a salient brand green and Before in grey, which directs attention. The perception hierarchy says colour should not carry the comparison, and labels prejudge the interpretation.
2. Use a colour-blind-safe palette with equal salience.
3. "Colour both bars the same neutral grey and remove the exact labels."
4. "The colours make one bar stand out more."

*TA: Catches 0 · Term 0 · Evidence 1 · Fix 1 · Scope 1 = 3. Uses the catalogue vocabulary (colour asymmetry, perception hierarchy) on the secondary element; the title is in fact neutral and the main distortion, the axis, is not mentioned. Cap rule applies.*
