#!/usr/bin/env python3
"""
Fill B01/B06/B07 SLATE beats in all 13 claude-liam-cli-* reels
with Remotion renders (ClaudeComposerAsk for B01/B07, ClaudeCodeBeat for B06).
B08 stays SLATE (optional placeholder).
"""
import json, pathlib, re, textwrap

BASE = pathlib.Path(__file__).parent
TS = "2026-07-19T12:00:00"

def wrap_comment(text, width=70):
    """Wrap text into # comment lines."""
    words = text.split()
    lines = []
    current = []
    for w in words:
        if sum(len(x) + 1 for x in current) + len(w) > width:
            lines.append("# " + " ".join(current))
            current = [w]
        else:
            current.append(w)
    if current:
        lines.append("# " + " ".join(current))
    return "\n".join(lines)

def first_n_sentences(text, n=3):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(sentences[:n])

def extract_steps(narration):
    """Pull numbered action items from narration; fall back to sentences."""
    # Look for explicit numbered steps in visual_intent or narration
    # e.g. "1) ..., 2) ..., 3) ..."
    steps = re.findall(r'\d+\)\s+([^,;]+)', narration)
    if steps:
        return [s.strip() for s in steps[:4]]
    # Fall back: split on 'then'/'and' boundaries
    sentences = re.split(r'(?<=[.!?])\s+', narration.strip())
    return sentences[:3]

for slug_dir in sorted(BASE.glob('claude-liam-cli-*')):
    bs_path = slug_dir / 'beat_sheet.json'
    if not bs_path.exists():
        print(f"SKIP  {slug_dir.name}  (no beat_sheet.json)")
        continue

    data = json.loads(bs_path.read_text())
    slug = slug_dir.name
    changed = False

    # Pull segment label from B00
    topic_segment = slug_dir.name.replace("claude-liam-cli-", "").replace("-", " ").upper()
    for b in data['beats']:
        if b['beat_id'] == 'B00':
            seg = b.get('shot', {}).get('remotion', {}).get('props', {}).get('segment', '')
            if seg:
                topic_segment = seg
            break

    for b in data['beats']:
        bid = b['beat_id']
        shot = b.get('shot', {})

        # Only fill beats that are still source=null
        if shot.get('source') is not None:
            continue

        narration = b.get('narration_text', '')
        visual_intent = b.get('visual_intent', '')

        # ── B01 PROBLEM ──────────────────────────────────────────────────────
        if bid == 'B01':
            # Key phrase: strip "title card: " prefix and quote marks
            raw = visual_intent.split(';')[0]
            key_phrase = re.sub(r"^title card:\s*'?", "", raw, flags=re.I).rstrip("'").strip()
            if not key_phrase:
                key_phrase = first_n_sentences(narration, 1)

            shot['source'] = 'remotion'
            shot['remotion'] = {
                "pattern": "ClaudeComposerAsk",
                "props": {
                    "command": key_phrase,
                    "topic": "COMPUTATIONAL SKEPTICISM",
                    "segment": topic_segment,
                    "greeting": "",
                    "runningText": "framing the problem…",
                    "output": [],
                    "folderLabel": "@NikBearBrown",
                    "modelLabel": "Fable 5",
                    "effortLabel": "High"
                },
                "rendered": {"out": "media/B01.mp4", "at": ""}
            }
            b['build'] = {"status": "NEEDS-RENDER", "src": None, "filled_by": None, "at": TS}
            changed = True

        # ── B06 SUMMARY/lesson ───────────────────────────────────────────────
        elif bid == 'B06':
            summary_text = first_n_sentences(narration, 3)
            # Pull insight from visual_intent (after ';' or the whole thing)
            parts = visual_intent.split(';')
            insight = parts[-1].strip().strip("'").strip() if len(parts) > 1 else visual_intent.strip()

            code_lines = ["# KEY LESSON", "#"]
            code_lines.append(wrap_comment(summary_text))
            code_lines += ["#", f"# → {insight}"]
            code = "\n".join(code_lines)

            shot['source'] = 'remotion'
            shot['remotion'] = {
                "pattern": "ClaudeCodeBeat",
                "props": {
                    "title": "lesson.md",
                    "code": code,
                    "sparkLine": topic_segment
                },
                "rendered": {"out": "media/B06.mp4", "at": ""}
            }
            b['build'] = {"status": "NEEDS-RENDER", "src": None, "filled_by": None, "at": TS}
            changed = True

        # ── B07 NEXT STEPS ───────────────────────────────────────────────────
        elif bid == 'B07':
            # Extract numbered steps from visual_intent first, then narration
            steps = extract_steps(visual_intent) or extract_steps(narration)

            code_lines = ["# YOUR MOVE", "#"]
            for i, step in enumerate(steps[:4], 1):
                step_clean = step.strip().rstrip(',').rstrip('.')
                code_lines.append(f"# {i}. {step_clean}")
            code_lines += ["#", "# → run it  →  audit the gap  →  report what you find"]
            code = "\n".join(code_lines)

            shot['source'] = 'remotion'
            shot['remotion'] = {
                "pattern": "ClaudeCodeBeat",
                "props": {
                    "title": "next_steps.md",
                    "code": code,
                    "sparkLine": "YOUR MOVE"
                },
                "rendered": {"out": "media/B07.mp4", "at": ""}
            }
            b['build'] = {"status": "NEEDS-RENDER", "src": None, "filled_by": None, "at": TS}
            changed = True

        # B08 stays SLATE (optional b-roll — leave for human)

    if changed:
        bs_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
        print(f"UPDATED  {slug}")
    else:
        print(f"SKIP     {slug}  (nothing to fill)")

print("\nDone. Re-run build_all_13.sh to compile.")
