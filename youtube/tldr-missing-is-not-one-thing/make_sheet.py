#!/usr/bin/env python3
"""make_sheet.py — writes beat_sheet.json for tldr-missing-is-not-one-thing.

tldr skill (brutalist.art/skills/make/tldr). Section S2 "Missing Is Not One Thing"
of chapter 3 (youtube/tldr-sections-03-data-validation.md). The chapter states one
number for the case (income, 18% missing, blanks co-occurring with age < 25 —
exercise 8) and the MNAR example ("high earners suppress their income"). The table
the film draws is CONSTRUCTED (world.py, captioned on screen); every relation the
film shows is asserted there at import. No dollar figure is spoken or shown — the
film shows DIRECTION only. FACTCHECK.md carries the rows.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import world as W

SLUG = "tldr-missing-is-not-one-thing"
TITLE = "Missing Is Not One Thing"
COURSE = "INFO 7375 · Computational Skepticism · Chapter 3"

# the numbers the narration uses, asserted against the constructed world
assert W.N == 50 and W.K == 9 and round(100 * W.K / W.N) == 18
assert W.N - W.K == 41                                         # "the forty-one you can see"
assert W.GAP[("mar", "column")] > 0 and abs(W.GAP[("mar", "band")]) < 1      # A: column fill high, band fill on the truth
assert W.GAP[("mnar", "column")] < -10 and W.GAP[("mnar", "band")] < -10     # B: both fills low
assert abs(W.GAP[("mcar", "column")]) < 1 and abs(W.GAP[("mcar2", "column")]) < 1
assert W.is_block("truth", W.MNAR) and not W.is_block("age", W.MNAR) and not W.is_block("city", W.MNAR)
assert all(W.rank_of("age", i) < 12 for i in W.MAR)

def beat(bid, act, narration, shot, role=None, section=None, learn=None, lane="manim", proof="SHOW", **extra):
    b = {"beat_id": bid, "act": act, "lane": lane, "proof_gate": proof}
    if section is not None: b["section"] = section
    if role: b["role"] = role
    if learn: b["learn"] = learn
    b.update({"narration_text": narration, "estimated_duration_s": round(len(narration.split()) / 2.5, 1),
              "voice": "am_onyx", "engine": "kokoro", "shot": shot})
    b.update(extra); return b

def manim(cls, intent, show, claim):
    return {"type": "GRAPHIC", "source": "own", "visual_intent": intent, "show": show, "manim": {"class": cls}, "motion_claim": claim}

def remotion(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show, "remotion": {"pattern": pattern, "props": props}}

beats = []

beats.append(beat("B00", "tldr · what",
    "Vanakkam. This is Liam, in for Bear, with chapter three of INFO 7375, Computational Skepticism for AI, at Northeastern. "
    "This film is about blank cells. The reason a value is missing decides whether filling it in is safe. "
    "Sort the rows by what you can see, and some blanks line up. Some never will. "
    "The trap: the worst kind of missing looks exactly like the harmless kind.",
    remotion("ClaudeTldrWhat", {
        "eyebrow": "TL;DR", "heading": "What This Film Is About", "greeting": "Vanakkam, Liam", "topic": COURSE,
        "question": "Two columns are each 18% blank. Why is one safe to fill in and the other a trap?",
        "lines": ["The reason a value is missing decides whether filling it in is safe.",
                  "Sort the rows by what you can see: some blanks line up. Some never will.",
                  "The trap: the worst kind of missing looks exactly like the harmless kind."],
        "cues": [1.5, 11.0, 16.0, 20.5], "durationSeconds": 26, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "'TL;DR.' wordmark; 'Vanakkam, Liam'; the course line; heading"},
         {"at": 0.06, "event": "the question writes on"},
         {"at": 0.42, "event": "line 1 lands on 'the reason a value is missing'"},
         {"at": 0.62, "event": "line 2 lands on 'sort the rows'"},
         {"at": 0.8, "event": "line 3 lands on 'the trap'"}]),
    lane="bookend"))

beats.append(beat("B01", "tldr · why",
    "Why should you care? Every dataset you inherit has blanks, and the first fix anyone reaches for is the average. "
    "When the reason is harmless, the average lands on the truth. "
    "When the people who left it blank are different, it drifts in a direction you cannot measure. "
    "Knowing the three kinds tells you which question no plot can answer for you.",
    remotion("ClaudeTldrWhy", {
        "eyebrow": "TL;DR", "heading": "Why You Should Care", "topic": COURSE,
        "lead": "Every dataset you inherit has blanks, and the first fix anyone reaches for is the average.",
        "lines": ["When the reason is harmless, the average lands on the truth.",
                  "When the people who left it blank are different, it drifts where you cannot measure.",
                  "Knowing the three kinds tells you which question no plot can answer."],
        "cues": [1.0, 7.5, 11.0, 16.0], "durationSeconds": 21, "folderLabel": "@NikBearBrown"},
        [{"at": 0.0, "event": "page turn: same header, heading 'Why You Should Care'"},
         {"at": 0.06, "event": "the stake writes on"},
         {"at": 0.36, "event": "dash 1 on 'harmless'"},
         {"at": 0.55, "event": "dash 2 on 'the people who left it blank'"},
         {"at": 0.78, "event": "dash 3 on 'the three kinds'"}]),
    lane="bookend", qc={"sparse_by_design": True, "sparse_reason": "TL;DR card two — text lands on cues by design."}))

beats.append(beat("B02", "the question",
    "The real question: before I fill them in, should I ask why it is missing? "
    "How much is missing is identical here: eighteen percent, both times. The count cannot tell them apart. The reason can.",
    remotion("BrutalistHesitantWriter", {
        "text": "Two income columns, 18% blank each.\nBefore I fill them in, should I ask\nhow much is missing?",
        "triggerWords": "how much is missing", "replacementWords": "why it is missing",
        "fontSize": 60, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1, "mistakeRate": 5, "jitter": 20,
        "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types 'Two income columns, 18% blank each.'"},
         {"at": 0.35, "event": "types the question; backspaces 'how much is missing' → 'why it is missing'"},
         {"at": 0.85, "event": "caret holds on the corrected question"}]),
    lane="bookend", lead_silence_s=0.8,
    motion_claim="The writer types the naive question (how much) and corrects the phrase into the real one (why).",
    qc={"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}))

beats.append(beat("B03", "terms",
    "Three words you'll hear. A missingness matrix: every row a thin line, every column a stripe, dark where a value is absent. "
    "Impute: fill a blank with an estimate, such as the average of the values you can see. "
    "And a subgroup: rows that share a trait, such as everyone under twenty-five.",
    remotion("ClaudeDefinitions", {
        "title": "Terms In This Film",
        "terms": [{"term": "missingness matrix", "meaning": "rows as thin lines, columns as stripes, dark where a value is absent"},
                  {"term": "impute", "meaning": "fill a blank with an estimate, such as the average of the values you can see"},
                  {"term": "subgroup", "meaning": "rows that share a trait, such as everyone under 25"}],
        "durationSeconds": 17, "folderLabel": "@NikBearBrown"},
        [{"at": 0.12, "event": "'missingness matrix' lands, terracotta"}, {"at": 0.5, "event": "'impute' lands; first settles"},
         {"at": 0.78, "event": "'subgroup' lands"}]),
    lane="bookend", proof="CARD",
    qc={"sparse_by_design": True, "sparse_reason": "TERMS card: prerequisites only — MCAR / MAR / MNAR are earned in B17."}))

# ── LEARN section 1 (B10–B19) ────────────────────────────────────────────────
beats.append(beat("B10", "learn 1",
    "Two tables of the same fifty people. In each, the income column is eighteen percent blank: nine rows out of fifty. "
    "Look at the dark cells. Scattered, in both. Same count, same look. "
    "Fill both with the average income you can see. One fill lands on the truth. The other lands somewhere else. Which is which?",
    manim("B10_TwoTables",
          "Two missingness matrices, 'table A' and 'table B', draw row by row (stripes: age · city · income; 50 thin rows); nine dark cells scattered in each income stripe; '9 of 50 blank · 18%' under each; the question 'fill with the average: which is safe?' at right; a small dim caption 'constructed table'.",
          [{"at": 0.0, "event": "matrix A draws row by row"}, {"at": 0.2, "event": "matrix B draws"},
           {"at": 0.4, "event": "nine dark cells land in each income stripe"}, {"at": 0.7, "event": "'which fill is safe?' lands"}],
          "The key case, unsolved: two matrices with the same 18% that look the same."),
    role="HOOK", section=1,
    learn={"question": "Two columns, both 18% blank: which is safe to fill with the average?",
           "action": "Draw both missingness matrices in file order.",
           "observation": "The blanks look equally scattered in both.",
           "inference": "Nothing on screen yet separates them.",
           "next_question": "What does an average fill do when the blanks carry no reason at all?"}))

beats.append(beat("B11", "learn 1",
    "Start with the easy case: a third table, where nine income cells were wiped at random, a coin flip, nothing to do with the person. "
    "Fill the nine with the average of the forty-one you can see. We built this table, so we can reveal the true average. "
    "The fill lands right on it. Wipe a different nine at random: it lands on it again. Random loss shrinks your sample. It does not tilt it.",
    manim("B11_RandomWipe",
          "Matrix 'random' at left, nine scattered dark cells; at right an income axis (no numbers, 'lower' / 'higher'); the nine blanks fill grey (imputed) and a fill dot slides onto the axis; the ink 'truth' tick rises under it; then the dark cells move to a second random nine, the fill re-runs and the dot lands on the tick again.",
          [{"at": 0.1, "event": "blanks fill grey; fill dot slides onto the axis"}, {"at": 0.45, "event": "truth tick revealed under the dot"},
           {"at": 0.65, "event": "the blanks move to a new random nine"}, {"at": 0.8, "event": "the dot lands on the truth again"}],
          "The first instance, varied and replayed: random blanks, fill on target."),
    role="INSTANCE", section=1,
    learn={"question": "What does a mean fill do when blanks are pure chance?",
           "action": "Fill two different random wipes with the visible average and compare to the known truth.",
           "observation": "Both fills land on the truth.",
           "inference": "Random loss costs rows, not direction.",
           "next_question": "What if the blanks are not random?"}))

beats.append(beat("B12", "learn 1",
    "Now table A. Same fill, same average of the visible rows. This time the dot lands to the right of the truth. Too high. "
    "Something about who is blank pulled it. Look along the age stripe, beside each dark cell: every blank row belongs to someone under twenty-five. "
    "In this table the young earn less, and they are the ones who skipped the question.",
    manim("B12_TableA",
          "Matrix A at left with the age stripe shaded: under-25 rows grey; the nine income blanks fill; the fill dot lands right of the truth tick ('too high'); the under-25 age cells darken, a terracotta dot beside the age header.",
          [{"at": 0.1, "event": "blanks fill; dot lands right of the truth"}, {"at": 0.4, "event": "'too high'"},
           {"at": 0.6, "event": "the age cells beside the blanks darken: all under 25"}, {"at": 0.85, "event": "caption: the young skipped it"}],
          "The second instance: the same fill, a tilted result, and a visible column that correlates with the blanks."),
    role="INSTANCE", section=1,
    learn={"question": "Does the same fill work on table A?",
           "action": "Fill A's blanks with the visible average; read the age stripe beside them.",
           "observation": "The fill lands high; every blank is under 25.",
           "inference": "Blanks tied to a visible column tilt the average.",
           "next_question": "Can we fix it with the column we can see?"}))

beats.append(beat("B13", "learn 1",
    "The natural fix: fill each blank with the average of its own age group. Do it for table A, and the dot slides back onto the truth. "
    "Now do exactly the same thing for table B, whose blanks look just as scattered. The dot barely moves. It stays low. "
    "And nothing in the table tells you why.",
    manim("B13_AgeGroupFill",
          "Matrix A with its dot high: the age-group fill runs and the dot slides back onto A's truth tick. Matrix B slides in beside it with its own axis: the column fill, then the age-group fill — the dot stays well left of B's truth tick; a terracotta X beside B's dot.",
          [{"at": 0.1, "event": "A: age-group fill; dot slides onto the truth"}, {"at": 0.45, "event": "B: same fill; dot stays low"},
           {"at": 0.75, "event": "X beside B's dot"}, {"at": 0.9, "event": "caption: nothing here says why"}],
          "The natural wrong turn: the fix that works for A fails for B, with no visible reason."),
    role="NAIVE", section=1,
    learn={"question": "Does filling by age group fix both tables?",
           "action": "Run the age-group fill on A, then on B.",
           "observation": "A lands on the truth; B stays low.",
           "inference": "B's blanks are not explained by age — or by anything on screen.",
           "next_question": "How could we SEE what the blanks depend on?"}))

beats.append(beat("B14", "learn 1",
    "Here's the move. Stop reading the matrix in file order. Sort the rows by a column you can see, and watch where the blanks go. "
    "Sort table A by age: the nine dark cells slide together, all inside the under-twenty-fives. "
    "Sort table B by age: still scattered. By city: scattered. A block means the blanks depend on something you can see.",
    manim("B14_SortTheRows",
          "Matrices A and B side by side; A's rows glide into age order and its nine blanks gather in the top band (under 25, bracketed); B's rows glide into age order — blanks stay scattered — then into city order — scattered; caption: a block = depends on a visible column.",
          [{"at": 0.15, "event": "A sorts by age: blanks gather in the under-25 band"}, {"at": 0.5, "event": "B sorts by age: scattered"},
           {"at": 0.7, "event": "B sorts by city: scattered"}, {"at": 0.88, "event": "caption lands"}],
          "The representation: sort rows by a column and watch whether the blanks line up."),
    role="SHIFT", section=1,
    learn={"question": "What do the blanks depend on?",
           "action": "Re-sort each matrix's rows by each visible column.",
           "observation": "A's blanks form a block under age; B's never do.",
           "inference": "Sorting by a column tests whether missingness depends on it.",
           "next_question": "B depends on nothing visible — so what does it depend on?"}))

beats.append(beat("B15", "learn 1",
    "Table B stays scattered under every column it has. So here is the one column it doesn't have: each person's true income, the value that was never written down. "
    "Before I sort by it, commit. Where will table B's nine blanks go? And the random table's?",
    manim("B15_Predict",
          "Matrix B (city order) and the random matrix; a ghost stripe of horizontal bars grows beside each — 'true income, never recorded' — bar length per row; everything holds; 'commit' with a terracotta dot; caption: true income, never recorded.",
          [{"at": 0.15, "event": "the unrecorded true-income bars grow beside both matrices"}, {"at": 0.55, "event": "HOLD — nothing moves on 'commit'"}],
          "The predict-before-reveal beat: the hidden column arrives, unsorted."),
    role="INSTANCE", section=1, predict=True,
    learn={"question": "If we could sort by the value itself, where would B's blanks go?",
           "action": "Add the never-recorded true-income bars; hold.",
           "observation": "The viewer commits.",
           "inference": "A prediction makes the sort evidence.",
           "next_question": "Sort."}))

beats.append(beat("B16", "learn 1",
    "Sort. Table B's blanks slide into one block at the very top: the nine highest earners. The random table's stay scattered. "
    "From inside the data, those two looked identical.",
    manim("B16_TheHiddenSort",
          "Both matrices re-sort by the true-income bars (bars form a descending staircase): B's nine dark cells glide into one block at the top beside the longest bars; the random table's stay scattered; a terracotta dot beside B's block; 'B: the top nine' · 'random: scattered'.",
          [{"at": 0.05, "event": "both sort by the hidden bars"}, {"at": 0.35, "event": "B's blanks: one block at the top"},
           {"at": 0.55, "event": "random: still scattered"}, {"at": 0.75, "event": "caption: from inside, they looked the same"}],
          "The aha: the blanks line up only under the column the matrix cannot draw; narration short."),
    role="TRANSFORM", section=1,
    learn={"question": "Where do B's blanks go under the hidden sort?",
           "action": "Sort both matrices by the true, never-recorded income.",
           "observation": "B's blanks are the top nine; the random table's stay scattered.",
           "inference": "B's missingness depends on the missing value itself — invisible from inside the data.",
           "next_question": "Name the three kinds."}))

beats.append(beat("B17", "learn 1",
    "These deserve names, and they come from Donald Rubin's work on missing data. "
    "Missing completely at random: the chance of a blank depends on nothing. Missing at random: it depends on something you can see, like age. "
    "Missing not at random: it depends on the missing value itself. The first two, a sort can show you. The third, no sort you can run ever will.",
    manim("B17_ThreeNames",
          "The three matrices shrink into one row (random · A · B) in their revealing sorts; under each its name lands (MCAR · MAR · MNAR) with one line: depends on nothing · on what you can see · on the missing value itself; B's hidden bars fade to ghost; a terracotta dot beside MNAR; small dim credit: after Rubin (1976).",
          [{"at": 0.1, "event": "three matrices slide into one row"}, {"at": 0.3, "event": "MCAR — depends on nothing"},
           {"at": 0.5, "event": "MAR — on what you can see"}, {"at": 0.7, "event": "MNAR — on the value itself; its bars fade"}],
          "The abstraction arrives as the name for three things watched; each label beside the matrix that earned it."),
    role="ABSTRACTION", section=1,
    learn={"question": "What are these three behaviours called?",
           "action": "Name each matrix by what its blanks depend on.",
           "observation": "Nothing · something visible · the value itself.",
           "inference": "The kind of missingness, not the amount, decides whether a fill is safe.",
           "next_question": "If no sort can show MNAR, how does anyone find it?"}))

beats.append(beat("B18", "learn 1",
    "Same shape, different table. A study's final measurement, blank for the patients who left before the end. "
    "Sort by anything recorded: scattered. The sort that would line them up is who got sicker, which is the very thing that's missing. "
    "So you don't find this kind with a plot. You find it by asking: who would not report this, and why?",
    manim("B18_WhoWouldNotReport",
          "Matrix B's stripes relabel (visit 1 · visit 2 · final); it sorts by visit 1 — scattered; a ghost stripe 'got sicker, never recorded' grows and the rows sort into a block again; the question 'who would not report this, and why?' lands at right with a terracotta dot; small dim caption: constructed.",
          [{"at": 0.1, "event": "stripes relabel: a study's final measurement"}, {"at": 0.35, "event": "sorted by a recorded column: scattered"},
           {"at": 0.6, "event": "the unrecorded 'got sicker' sort: one block"}, {"at": 0.85, "event": "the question lands"}],
          "Post-shift instance: the same invariant in a new table; the detector is a question, not a plot."),
    role="INSTANCE", section=1,
    learn={"question": "How do you find MNAR if no plot shows it?",
           "action": "Relabel the matrix as a study with dropouts; sort by recorded vs unrecorded columns.",
           "observation": "Only the unrecorded sort lines the blanks up.",
           "inference": "MNAR is found by reasoning about who would not report, not by a diagnostic.",
           "next_question": "Back to tables A and B."}))

beats.append(beat("B19", "learn 1",
    "Back to the two tables. Both eighteen percent blank, both scattered in file order. Sort by age: table A lines up, so fill within the age group and you land on the truth. "
    "Table B never lines up, and its average sits low, biased in exactly the direction you cannot measure. "
    "Not taught here: how to choose an imputation method, or rows a join dropped before any matrix could see them.",
    manim("B19_Payoff",
          "The HOOK's two matrices return in file order; both sort by age: A gathers, B stays scattered; A's dot on its truth tick, B's dot low with an X beside it; labels MAR / MNAR under each; dim boundary caption: not taught here: choosing a fill.",
          [{"at": 0.05, "event": "the HOOK state returns"}, {"at": 0.25, "event": "both sort by age"},
           {"at": 0.5, "event": "A: dot on truth · B: dot low, X"}, {"at": 0.9, "event": "boundary caption"}],
          "The HOOK's objects resolve; the boundary names what was left out."),
    role="PAYOFF", section=1,
    learn={"question": "So — which fill is safe?",
           "action": "Sort both hook tables by age and fill within the group.",
           "observation": "A lands on the truth; B stays low.",
           "inference": "Safe depends on why, not how much.", "next_question": ""}))

beats.append(beat("BVDT", "verdict",
    "Let's recap with Claude. Missing is not one thing. If the blanks depend on nothing, an average fill lands on the truth. "
    "If they depend on something you can see, like age, sort by it, fill within the group, and you recover it. "
    "If they depend on the missing value itself, every fill drifts, and no plot can show you. For that kind, ask who would not report, and why.",
    remotion("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": TITLE,
        "artifactLines": ["Same 18% blank, different reasons — the reason decides whether a fill is safe.",
                          "Blanks that depend on nothing (MCAR): an average fill lands on the truth.",
                          "Blanks that depend on a column you can see (MAR): sort by it, fill within the group.",
                          "Blanks that depend on the value itself (MNAR): no plot shows it. Ask who would not report, and why."]},
        [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "four verdict lines land"}]),
    lane="bookend", lead_silence_s=0.5, qc={"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}))

YT = ("A clinic dataset has a column pain_score that is 18% blank, and the missingness matrix shows the blanks cluster in evening appointments. "
      "Before writing any code, predict: MCAR, MAR, or MNAR? "
      "Then give me one story under which it really is MAR, and one under which it is actually MNAR. "
      "For each story, say which way an average fill would move the mean pain score, "
      "and name one question I should ask the clinic that no plot of this data could answer.")
beats.append(beat("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + YT + " "
    "Two things to look for. Did it commit to a prediction before it reached for code? "
    "And does its MNAR story name who would not report, and why, instead of recommending a fancier fill?",
    remotion("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "INFO 7375 · YOUR TURN", "segment": "Ask Why It Is Missing",
        "command": YT, "runningText": "paste this into Claude…",
        "output": ["Check: it predicted before it reached for code.",
                   "Check: its MNAR story names who would not report, and why."],
        "folderLabel": "@NikBearBrown", "modelLabel": "Fable 5", "effortLabel": "High"},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"}, {"at": 0.1, "event": "the prompt types in full"}, {"at": 0.8, "event": "two rubric lines land"}]),
    lane="bookend"))

beats.append(beat("BOUT", "outro", f"{TITLE}. At Nik Bear Brown.",
    remotion("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": "@NikBearBrown", "subline": ""},
             [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'. No jingle."}]),
    lane="bookend", kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad into the mp3); no jingle (OUTRO-LOCK §Voice)"))

sheet = {"metadata": {
    "slug": SLUG, "title": TITLE, "topic": "INFO 7375 · TL;DR", "skill": "tldr", "style_preset": "tldr",
    "channel": "claude-liam", "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "learn_canvas": "cream", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "INFO 7375 students validating a dataset they did not build, and anyone who has filled a blank with the average",
    "course": "INFO 7375 Computational Skepticism for AI · Nik Bear Brown · Northeastern University",
    "source_doc": "chapters/03-data-validation-reconstructing-the-epistemic-frame-behind-a-dataset.md, §'The procedural EDA pass' ¶Missingness (+ Rubin footnote), Figure 3.2, failure-table row MNAR, exercise 8; section S2 of youtube/tldr-sections-03-data-validation.md",
    "sections": [{"n": 1, "title": "Missing Is Not One Thing", "key_case": "income 18% blank (9 of 50, constructed): table A's blanks are under-25s (MAR), table B's are the top earners (MNAR); a random wipe (MCAR) as the baseline"}],
    "greeting_language": "Tamil (Vanakkam)",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "playlist": "Claude & Agentic AI", "chapter_number": 0,
    "outro_policy": "OUTRO-LOCK §Voice: spoken title + 'At Nik Bear Brown', 1.0 s silent tail padded into the mp3, no jingle.",
    "bookloop_policy": "Course film: carries the INFO 7375 course credit (spoken in B00, on the cards' course line).",
    "tags": ["missing data", "MCAR", "MAR", "MNAR", "imputation", "data validation", "missingness matrix", "INFO 7375",
             "3Blue1Brown style", "Claude", "Nik Bear Brown"]},
    "beats": beats}
out = HERE / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print(f"{len(beats)} beats → {out}")
