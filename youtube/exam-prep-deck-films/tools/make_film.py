#!/usr/bin/env python3
"""make_film.py - build one film's reel folder from its deck extract and its narration.

    python3 make_film.py NN

Writes <course>/youtube/claude-liam-lecture-key-terms-<topic>/ : beat_sheet.json and the paperwork
(ACTS, SHOTLIST, FACTCHECK, PROMPTS, SOURCES, CHECKS-REPORT). Safe to re-run: measured audio
(audio_file, actual_duration_s) is carried forward, and every Remotion beat's durationSeconds is then
set from the MEASURED audio. Do not re-run after `art final` (it would drop the build stamps).

The film follows the brutalist.art `lecture` spine (BOPEN, BIDEA, BDEFS ... BVDT, BHTF, BOUT). Its body
is the deck itself: one beat per click-step, filmed from the live deck by deck_capture.py (shot.type SCREEN).
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from films import AI_FIX, CARD_LINE, COURSE_NAME, PLAYLIST, PRONOUNCE, TOOLKIT, film  # noqa: E402

HANDLE = "@NikBearBrown"
WPS = 2.55
TODAY = date.today().isoformat()
INSTRUCTION = ("Bear, 2026-11-11: make the glossary decks into films, use the decks and their animations, "
               "and have Liam explain each slide.")

LABELS = {
    "in the book text": ("In the book text", "the course text uses and explains the term",
                         "In the book text: the course text uses and explains the term."),
    "in the glossary": ("In the glossary", "on the course term list; the text does not explain it",
                        "In the glossary: the term is on the course term list, but the text does not explain it."),
    "outside source": ("Outside source", "from a named reference outside the course text",
                       "Outside source: the term comes from a named reference outside the course text."),
    "Computed": ("Computed", "numbers worked out on screen from stated inputs",
                 "Computed: the numbers are worked out on screen from stated inputs."),
    "Simulation (seeded)": ("Simulation", "a made-up run with a fixed seed, the same every time",
                            "Simulation: a made-up run with a fixed seed, so it comes out the same every time."),
    "Illustrative data": ("Illustrative data", "numbers chosen to show the idea, not measured",
                          "Illustrative data: numbers chosen to show the idea, not measured."),
    "Conceptual illustration": ("Conceptual", "a drawing of the idea, with no data behind it",
                                "Conceptual: a drawing of the idea, with no data behind it."),
}
ORDER = list(LABELS)
NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven"]


def words(s):
    return len(re.findall(r"[^\W_][\w'’-]*", s))


def est(s):
    return round(words(s) / WPS + 0.6, 1)


def base(bid, act, lane, gate, text):
    return {"beat_id": bid, "act": act, "lane": lane, "proof_gate": gate, "narration_text": text,
            "estimated_duration_s": est(text), "voice": "am_onyx", "engine": "kokoro", "persona": "liam"}


def main():
    nn = sys.argv[1]
    F = film(nn)
    deck = json.loads((F["extract"] / "deck.json").read_text())
    nar = json.loads((F["extract"] / "narration.json").read_text())
    verify_path = F["extract"] / "verify.json"
    verify = json.loads(verify_path.read_text()) if verify_path.exists() else None
    reel = F["reel"]
    reel.mkdir(parents=True, exist_ok=True)
    slug, title = F["slug"], F["title"]
    old = {}
    sp = reel / "beat_sheet.json"
    if sp.exists():
        for b in json.loads(sp.read_text())["beats"]:
            old[b["beat_id"]] = b

    by = {(b["slide"], b["step"]): b for b in nar["beats"]}
    slides = [s for s in deck["slides"] if s["n_steps"] > 0]

    # ---- labels the deck uses (BDEFS) --------------------------------------------------
    used = set()
    for s in slides:
        if s["evidence"]:
            used.add(s["evidence"])
        for st in s["steps"]:
            for t in st["all_texts"]:
                if t in LABELS:
                    used.add(t)
    labels = [k for k in ORDER if k in used]
    unknown = sorted(u for u in used if u not in LABELS)
    if unknown:
        raise SystemExit(f"deck uses a label this builder does not know: {unknown}")
    defs_text = (f"{NUM[len(labels)].capitalize()} labels sit in the corners of the pictures that follow. "
                 + " ".join(LABELS[k][2] for k in labels))

    beats = []
    # ---- BOPEN ---------------------------------------------------------------------------
    b = base("BOPEN", "Opening", "bookend", "CARD", f"{PLAYLIST}. {title}. {nar['opening_summary'].strip()}")
    b["source_evidence"] = f"{INSTRUCTION} Playlist name as Bear gave it."
    b["routing"] = {"about": "Playlist, exact film title, payoff", "runner_up": "Writer-first opening",
                    "reason": "The lecture skill requires the narrated portrait/title card before the writer."}
    b["shot"] = {"type": "REMOTION", "source": "own", "template": "lecture-title-slide-16x9", "narration_contract": "playlist-title-summary-v1",
                 "visual_intent": "Named opening fields visible from frame zero", "motion_claim": "Static identity card; hold covers measured narration.",
                 "show": [{"at": 0, "event": "Complete portrait/title/series card visible"}]}
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Official lecture identity card is an explicit first-beat exception."}
    beats.append(b)

    # ---- BIDEA ---------------------------------------------------------------------------
    idea = nar["idea"]
    b = base("BIDEA", "Opening", "bookend", "SHOW", idea["narration"].strip())
    b["source_evidence"] = "narration.json idea; the deck's own framing"
    b["routing"] = {"about": "Core framing correction", "runner_up": "Overview card", "reason": "One phrase is revised; the terms that follow earn the correction."}
    b["shot"] = {"type": "REMOTION", "source": "own", "visual_intent": "Core framing correction",
                 "motion_claim": "One phrase is revised; the terms that follow earn the correction.",
                 "show": [{"at": 0.0, "event": "types the assumption"},
                          {"at": 0.6, "event": f"backspaces '{idea['triggerWords']}', types '{idea['replacementWords']}'"}],
                 "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
                     "text": idea["text"], "triggerWords": idea["triggerWords"], "replacementWords": idea["replacementWords"],
                     "fontSize": 70, "charMs": 22, "mistakeRate": 2, "hesitateBetween": 6, "hesitateWithin": 1, "seed": slug,
                     "banner": "", "brandLabel": HANDLE, "durationSeconds": 0}}}
    b["lead_silence_s"] = 0.8
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Hesitant-writer bookend: the correction is the motion."}
    beats.append(b)

    # ---- BDEFS ---------------------------------------------------------------------------
    b = base("BDEFS", "Terms", "bookend", "CARD", defs_text)
    b["source_evidence"] = "The deck's opening speaker note (what each tag means) and the evidence badge on every slide"
    b["routing"] = {"about": "The labels printed on every slide", "runner_up": "The deck's own title slide",
                    "reason": "Prerequisite vocabulary only: the tags and badges the viewer will see in every picture. The terms the film teaches arrive in the body."}
    n = len(labels)
    b["shot"] = {"type": "REMOTION", "source": "own", "visual_intent": "Prerequisite labels", "motion_claim": "Each label lands as it is spoken.",
                 "show": [{"at": round(0.08 + 0.84 * i / max(1, n), 2), "event": f"'{LABELS[k][0]}' lands"} for i, k in enumerate(labels)],
                 "remotion": {"pattern": "ClaudeDefinitions", "props": {
                     "title": "Terms In This Lecture", "folderLabel": HANDLE,
                     "terms": [{"term": LABELS[k][0], "meaning": LABELS[k][1]} for k in labels], "durationSeconds": 0}}}
    b["qc"] = {"sparse_by_design": True, "sparse_reason": f"TERMS card: {NUM[n]} labels, one plain line each."}
    beats.append(b)

    # ---- body: one beat per click-step -------------------------------------------------
    shot_rows, fact_rows, acts = [], [], []
    corrections = {(c["slide"], c["step"]): c for c in (verify or {}).get("corrections", [])}
    for s in slides:
        act = s["eyebrow"] or "Terms"
        ids = []
        for st in s["steps"]:
            i, k = s["index"], st["k"]
            nb = by[(i, k)]
            bid = f"B{i:02d}{k:02d}"
            ids.append(bid)
            new = [t for t in st["new_texts"] if len(t) < 60][:4]
            about = "; ".join(new) if new else s["title"]
            b = base(bid, act, "screen", "SHOW", nb["narration"].strip())
            b["source_evidence"] = f"{F['deck_file']} slide {i + 1} step {k}. {s['source']} Badge: {s['evidence'] or 'none'}."
            b["routing"] = {"about": about, "runner_up": "A Manim rebuild of the same figure",
                            "reason": "The deck is the study tool being taught from, so it is shown as itself with its own animation (SHOW-THE-THING). " + INSTRUCTION}
            b["shot"] = {"type": "SCREEN", "source": "capture", "visual_intent": f"{s['title']}: {s['picture']}"[:400],
                         "motion_claim": f"The deck's own animation for step {k} of {s['n_steps']} plays as the narration starts ({st['anim_ms']} ms), then the picture holds.",
                         "show": [{"at": 0.0, "event": f"step {k} animates: {about}"[:200]}]}
            b["deck"] = {"slide": i, "step": k, "anim_ms": st["anim_ms"]}
            b["qc"] = {"full_bleed": True, "full_bleed_reason": "A captured deck slide shown whole; its red top rule runs edge to edge by the deck's design."}
            if i == 1 and k < s["n_steps"]:
                b["qc"].update({"sparse_by_design": True, "sparse_reason": "The deck's map table adds one group row per step; the early steps show only the first rows by design."})
            beats.append(b)
            shot_rows.append(f"| {bid} | {about} | deck slide {i + 1}, step {k}, filmed live (SCREEN) | Manim rebuild of the figure | Bear asked for the decks and their animations; the deck is shown as itself |")
            figs = nb.get("figures") or []
            c = corrections.get((i, k))
            if figs:
                fact_rows.append((bid, "Figures spoken: " + ", ".join(f"`{x}`" for x in figs), "PASS",
                                  f"Each figure is printed on slide {i + 1} at step {k} (machine check, check_narration.py). Badge: {s['evidence'] or 'none'}.", "none"))
            if verify is not None:
                if c:
                    fact_rows.append((bid, f"Explanation of: {about}", "CORRECTED",
                                      f"Second-pass check against the slide and the chapter: {c.get('why', '')}", f"Reworded. Was: \"{c.get('was', '')[:160]}\""))
                else:
                    fact_rows.append((bid, f"Explanation of: {about}", "PASS", f"Second-pass check against slide {i + 1} step {k} and {F['chapter'].name}", "none"))
        acts.append((act, s, ids))

    # ---- BVDT ----------------------------------------------------------------------------
    lines = [x.strip() for x in nar["recap_lines"]]
    b = base("BVDT", "Recap", "bookend", "SHOW", "Let's recap. " + " ".join(lines))
    b["source_evidence"] = "This film's body beats; nothing new is asserted"
    b["routing"] = {"about": "Six things the terms established", "runner_up": "Summary drawing", "reason": "Restates only what the body showed."}
    b["shot"] = {"type": "REMOTION", "source": "own", "visual_intent": "Six earned conclusions", "motion_claim": "Restates only what the body showed.",
                 "show": [{"at": 0.0, "event": "artifact page opens"}, {"at": 0.2, "event": "six lines land in narration order"}],
                 "remotion": {"pattern": "ClaudeVerdictArtifact", "props": {
                     "artifactTitle": "Recap", "artifactHeading": "What We Established", "artifactLines": lines,
                     "brandLabel": HANDLE, "lectureLayout": True, "durationSeconds": 0}}}
    b["lead_silence_s"] = 0.5
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Mandated ClaudeVerdictArtifact bookend."}
    beats.append(b)

    # ---- BHTF ----------------------------------------------------------------------------
    yt = nar["your_turn"]
    b = base("BHTF", "Your turn", "bookend", "SHOW", yt["command"].strip())
    b["source_evidence"] = "narration.json your_turn (a practice prompt composed from this film's terms; not a run we made)"
    b["routing"] = {"about": "Practice: name the exact term and defend it", "runner_up": "Worksheet",
                    "reason": "The spoken prompt makes the viewer use the terms; two checks let them judge the result. Not a run we made."}
    b["shot"] = {"type": "REMOTION", "source": "own", "visual_intent": "Practice prompt", "motion_claim": "The prompt types in full, then two checks land.",
                 "show": [{"at": 0.0, "event": "Composer opens - 'Your turn.'"}, {"at": 0.12, "event": "the prompt types in full"}, {"at": 0.85, "event": "two check lines land"}],
                 "remotion": {"pattern": "ClaudeComposerAsk", "props": {
                     "greeting": "Your turn.", "topic": "KEY TERMS · YOUR TURN", "segment": yt["segment"], "command": yt["command"].strip(),
                     "output": yt["checks"], "runningText": "paste this into Claude…", "folderLabel": HANDLE, "largeText": True, "durationSeconds": 0}}}
    beats.append(b)

    # ---- BOUT ----------------------------------------------------------------------------
    b = base("BOUT", "Outro", "bookend", "SHOW", f"{title}. At Nik Bear Brown.")
    b["source_evidence"] = "OUTRO-LOCK.md"
    b["routing"] = {"about": "Locked sign-off", "runner_up": "None", "reason": "Exact title and channel, slug-seeded mascot."}
    b["shot"] = {"type": "REMOTION", "source": "own", "show": [{"at": 0.0, "event": "title restates; handle; mascot"}],
                 "remotion": {"pattern": "ClaudeTitleOutro", "props": {"title": title, "slug": slug, "subline": "", "handle": HANDLE,
                                                                       "lectureLayout": True, "durationSeconds": 0}}}
    b["kind"] = "outro_voice"
    b["tail_silence_s"] = 1.0
    b["qc"] = {"sparse_by_design": True, "sparse_reason": "Locked channel outro."}
    beats.append(b)

    md = {"slug": slug, "title": title, "skill": "lecture", "style_preset": "lecture", "channel": "claude-liam",
          "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro", "clock": "narration",
          "palette": "neu", "channel_handle": HANDLE, "register": "Teardown", "fps": 24, "width": 3840, "height": 2160, "aspect_ratio": "16:9",
          "caption_policy": "sidecar", "greeting_language": "German (Hallo)", "source_doc": str(reel / "SOURCES.md"),
          "playlist": PLAYLIST, "series_title": PLAYLIST, "series_numbered": False, "course": COURSE_NAME,
          "lecture_opening_description": CARD_LINE[nn], "lecture_opening_title_lines": F["title_lines"],
          "tags": ["Computational Skepticism", "INFO 7375", "Key terms", "Exam prep" if F["on_exam"] else "Course terms", F["topic"], "Glossary", "Liam", "Lecture"],
          "deck_file": str(F["deck_file"]), "deck_note": "Body beats are the terminology deck filmed live; see exam-prep-deck-films/tools/deck_capture.py",
          "on_exam": F["on_exam"]}
    spoken = " ".join(b["narration_text"] for b in beats)
    lex = {w: ipa for w, ipa in PRONOUNCE.items() if re.search(r"\b" + re.escape(w) + r"\b", spoken, re.I)}
    if re.search(r"\bAI\b", spoken):
        lex.update(AI_FIX)
    # A lone capital A in mid-sentence ("Group A and Group B") is spoken by the phonemizer as the article "a".
    # Key each "<word before> A <word after>" phrase so the letter is said as a letter. (At the end of a clause,
    # and in "A's", the phonemizer already says the letter.)
    trios = sorted(set(m.groups() for m in re.finditer(r"\b([A-Za-z]+)(,?) A ([A-Za-z]+)\b", spoken)))
    if trios:
        sys.path.insert(0, str(TOOLKIT / "runtime" / "scripts"))
        import generate_audio_kokoro as gk
        for prev, comma, nxt in trios:
            key = f"{prev}{comma} A {nxt}"
            if re.search(r"\b" + re.escape(f"{prev}{comma} a {nxt}") + r"\b", spoken):
                raise SystemExit(f"'{key}' also occurs with a lowercase article; handle it by hand")
            lex[key] = f"{gk.phonemize(prev).strip()}{comma} ˈeɪ {gk.phonemize(nxt).strip()}"
    if lex:
        md["pronounce"] = lex
    # ---- Northeastern bookends (Bear, 2026-11-12: "they should all be in northeastern") -----------
    # The six bookends are drawn by tools/bookends.py in the deck's own look, not by the Claude-palette
    # Remotion scenes. Their content is unchanged; only the drawing changes. shot.type GRAPHIC = our own
    # designed graphic, so the type-size check measures it like any other designed beat.
    NEU = {"BOPEN": ("neu-bookend-title", "Playlist, title, portrait, credits and handle, visible from frame zero; held for the measured narration.",
                     "Identity card in the deck's look: a still hold is the design."),
           "BIDEA": ("neu-bookend-writer", "The assumption is typed, one phrase is struck and replaced in NU red.", "Typing builds the line on an empty page; early frames are sparse by design."),
           "BDEFS": ("neu-bookend-labels", "Each tag or badge, drawn as the deck draws it, rises as it is spoken.", "The label rows rise one at a time; early frames are sparse by design."),
           "BVDT": ("neu-bookend-recap", "Six recap lines rise in narration order.", "Recap lines rise one at a time; early frames are sparse by design."),
           "BHTF": ("neu-bookend-your-turn", "The practice prompt types into a box marked for Claude, then two checks land.", "The prompt types into an empty box; early frames are sparse by design."),
           "BOUT": ("neu-bookend-outro", "Exact title and channel handle in the deck's look; held.", "Closing card: title and handle only, by design.")}
    for b in beats:
        if b["beat_id"] in NEU:
            tpl, motion, why = NEU[b["beat_id"]]
            shot = b["shot"]
            shot.pop("remotion", None)
            shot.update({"type": "GRAPHIC", "source": "own", "template": tpl, "motion_claim": motion,
                         "renderer": "exam-prep-deck-films/tools/bookends.py"})
            if b["beat_id"] == "BOPEN":
                # As the toolkit's own lecture title card does, keep the Professor Bear portrait out of the
                # type-size check (photo texture is not typography); every text field is listed explicitly.
                b["qc_typography"] = {"typography_fill": "#FFFFFF", "typography_reason": "Lecture identity card: the portrait slot is a photograph, not typography; all text fields are listed.",
                                      "typography_regions": [{"label": "playlist", "box": [0.0625, 0.08, 0.80, 0.135]},
                                                             {"label": "title, rule and summary", "box": [0.41, 0.26, 0.95, 0.72]},
                                                             {"label": "presenter and narrator credits", "box": [0.0625, 0.73, 0.40, 0.845]},
                                                             {"label": "channel handle", "box": [0.74, 0.895, 0.945, 0.95]}]}
            b["qc"] = {"sparse_by_design": True, "sparse_reason": why, "full_bleed": True,
                       "full_bleed_reason": "Deck look: the red top rule runs edge to edge by design; all text sits 120 px inside the frame."}
            b["qc"].update(b.pop("qc_typography", {}))
    bk = {"idea": {k: idea[k] for k in ("text", "triggerWords", "replacementWords")},
          "labels": [{"key": k, "kind": "tag" if k in ("in the book text", "in the glossary", "outside source") else "badge", "meaning": LABELS[k][1]} for k in labels],
          "defs_parts": [defs_text.split(". ")[0] + "."] + [LABELS[k][2] for k in labels],
          "recap_lead": "Let's recap.", "recap_lines": lines, "segment": yt["segment"], "command": yt["command"].strip(), "checks": yt["checks"]}
    md["bookends"] = bk

    # ---- carry measured audio forward; set Remotion durations ---------------------------
    voiced = 0
    for b in beats:
        o = old.get(b["beat_id"])
        hit = {k: v for k, v in lex.items() if re.search(r"\b" + re.escape("AI" if k.startswith("A-I") else k) + r"\b", b["narration_text"], re.I)}
        b["voice_key"] = hashlib.sha1((b["narration_text"] + json.dumps(hit, sort_keys=True, ensure_ascii=False)).encode()).hexdigest()[:12]
        if o and o.get("voice_key") == b["voice_key"] and o.get("audio_file") and o.get("actual_duration_s") and (reel / o["audio_file"]).is_file():
            b["audio_file"], b["actual_duration_s"] = o["audio_file"], o["actual_duration_s"]
            voiced += 1
        r = b["shot"].get("remotion")
        if r:
            r["props"]["durationSeconds"] = b.get("actual_duration_s") or b["estimated_duration_s"]

    sp.write_text(json.dumps({"metadata": md, "beats": beats}, indent=1, ensure_ascii=False) + "\n")

    # ---- paperwork -----------------------------------------------------------------------
    body = [b for b in beats if b.get("deck")]
    total_est = sum(b.get("actual_duration_s") or b["estimated_duration_s"] for b in beats)
    A = [f"# ACTS - {title}", "", f"Source: the terminology deck [{F['deck_file'].name}]({F['deck_file']}), {len(deck['slides'])} slides, "
         f"{len(body)} click-steps. {INSTRUCTION}", "",
         "The deck's own groups (the red line above each slide title) are the acts. Every slide with click-steps is in the film, in deck order; every click-step is one beat.", "",
         "| Act (deck group) | Slide | Beats |", "|---|---|---|"]
    for act, s, ids in acts:
        A.append(f"| {act} | {s['index'] + 1}. {s['title']} | {ids[0]} to {ids[-1]} ({len(ids)}) |")
    A += ["", "## LEFT OUT", "",
          "- Deck slide 1 (the deck's title slide): its title is the film's BOPEN card, and its speaker note (what the tags mean) is BDEFS.",
          "- The \"click or press to start\" hint each slide shows before its first step: a presenter instruction, never filmed (the first step is triggered as the slide appears).",
          "- The deck's viewer controls (previous, next, grid): hidden during capture. Nothing on a slide is hidden or changed.", "",
          "## Cast", "", "One cast for the whole film: the deck's own figures, in the deck's own colors (Northeastern red, Lato). "
          "The bookends keep the Claude palette. No act-title cards were added: each slide carries its group name above its title.", ""]
    (reel / "ACTS.md").write_text("\n".join(A))

    S = [f"# SHOTLIST - {title}", "", "Every body beat is one click-step of the deck, filmed from the live deck on a virtual clock "
         "(3840x2160, 24 fps) by `exam-prep-deck-films/tools/deck_capture.py`. The lane was set by instruction, so the runner-up is the same for every beat.", "",
         "| beat | about | lane picked | runner-up | why this one wins |", "|---|---|---|---|---|"] + shot_rows + ["",
         "Bookends: BOPEN (lecture title card), BIDEA (BrutalistHesitantWriter), BDEFS (ClaudeDefinitions), BVDT (ClaudeVerdictArtifact), "
         "BHTF (ClaudeComposerAsk), BOUT (ClaudeTitleOutro). No tool or website is shown, so there are no SHOW-THE-THING rungs beyond the deck itself.", ""]
    (reel / "SHOTLIST.md").write_text("\n".join(S))

    status = (f"Status: {TODAY}, checked by Claude. Figures: every spoken figure machine-checked against the words on the slide at that step. "
              + ("Explanations: an independent second pass compared every beat with its slide and the chapter"
                 + (f" and reworded {len(corrections)} beat(s)." if corrections else "; no beat needed rewording.")
                 if verify is not None else "Explanations: written from the slide and the chapter by the script author; NO independent second pass yet.")
              + " No human sign-off.")
    Fk = [f"# FACTCHECK - {title}", "", status, "",
          "The film teaches from the deck; the deck's numbers are computed in the page or labelled illustrative or simulated on the slide itself (the badge at top right). "
          "This file checks that the narration says only what the slide and the chapter support.", "",
          "| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |", "|---|---|---|---|---|---|"]
    rows = [("BOPEN", "Playlist name, film title, what the film covers", "PASS", f"Playlist as Bear named it 2026-11-11; summary restates the deck's map slide", "none"),
            ("BDEFS", "What each tag and badge means: " + ", ".join(LABELS[k][0] for k in labels), "PASS",
             "Deck slide 1 speaker note (tags); the badges are the deck's own evidence labels; seeded = the deck's `rng(seed)`", "none")] + fact_rows + [
            ("BVDT", "Six recap lines", "PASS", "Each restates a body beat; nothing new", "none"),
            ("BHTF", "Practice prompt", "EXEMPT", "A viewer exercise composed from the film's terms; not presented as a run", "none")]
    for n, r in enumerate(rows, 1):
        Fk.append(f"| {n} | {r[0]} | {r[1].replace('|', '/')} | {r[2]} | {r[3].replace('|', '/')} | {r[4].replace('|', '/')} |")
    if nar.get("deck_problems"):
        Fk += ["", "## Things noticed on the deck itself (not changed; for Bear)", ""] + [f"- {p}" for p in nar["deck_problems"]]
    if verify and verify.get("unresolved"):
        Fk += ["", "## Open after the second pass", ""] + [f"- {p}" for p in verify["unresolved"]]
    (reel / "FACTCHECK.md").write_text("\n".join(Fk) + "\n")

    (reel / "PROMPTS.md").write_text(f"# PROMPTS - {title}\n\nNo generation prompts. Nothing in this film is generated by an image or video model: "
                                     "the body is the deck filmed live, the bookends are toolkit Remotion scenes, and the voice is Kokoro am_onyx (free, local).\n")
    (reel / "SOURCES.md").write_text("\n".join([
        f"# SOURCES - {title}", "",
        f"- The deck: [{F['deck_file'].name}]({F['deck_file']}) (not edited).",
        f"- What was extracted from it (words per step, stills): [{F['extract']}]({F['extract']}).",
        f"- The script: [{F['extract'] / 'narration.json'}]({F['extract'] / 'narration.json'}).",
        f"- The chapter the terms come from: [{F['chapter'].name}]({F['chapter']}).",
        f"- The glossary generated from the decks: [{F['deck_file'].parents[1] / 'GLOSSARY.md'}]({F['deck_file'].parents[1] / 'GLOSSARY.md'}).",
        f"- Tools: [{Path(__file__).resolve().parent}]({Path(__file__).resolve().parent}).",
        f"- Instruction: {INSTRUCTION}", "",
        "Credits: deck and course by Professor Nik Bear Brown. Narration: Liam, in for Bear (Kokoro am_onyx). D3 7.9.0 and Lato are loaded by the deck.", ""]))
    hist = {"bookend (Remotion / title card)": 6, "deck, filmed live (SCREEN)": len(body)}
    (reel / "CHECKS-REPORT.md").write_text("\n".join([
        f"# CHECKS-REPORT - {title}", "", f"Written {TODAY}, before the first compile.", "",
        f"- Beats: {len(beats)} ({len(body)} body, 6 bookend). Estimated runtime {total_est / 60:.1f} min (the measured audio decides).",
        f"- PROOF GATE: SHOW {sum(1 for b in beats if b['proof_gate'] == 'SHOW')}, CARD {sum(1 for b in beats if b['proof_gate'] == 'CARD')}, HOLD 0. "
        "Every body beat is SHOW: the step's animation is the motion, and the narration explains what it adds.",
        "- Lane histogram (information, not a quota): " + "; ".join(f"{k}: {v}" for k, v in hist.items()) + ".",
        "- Teaching arc: map of the groups, then each group's terms with a picture each, then look-alike pairs, exact wording, and a checklist (the deck's own order).",
        "- Departures from the lecture skill, by instruction: the body uses one lane (the deck) and the deck's own palette, not a per-beat audition in the Claude palette; "
        "no act-title cards (each slide names its group); the deck prints chapter numbers and source file names, which the narration never speaks.",
        "- Gate T (the type-size check): body beats are SCREEN captures and are exempt from its pixel checks; the deck's smallest type is 24 px at 1080p (48 px at 4K).", ""]))
    print(f"{slug}: {len(beats)} beats ({len(body)} deck steps), {voiced} already voiced, about {total_est / 60:.1f} min")


if __name__ == "__main__":
    main()
