#!/usr/bin/env python3
"""
Add narration + Remotion ClaudeCodeBeat content to B08 in all 13 claude-liam-cli-* reels.
B08 was "optional extra b-roll" with no audio_file → whole video compiled silent.
Fix: add a brief call-to-action narration so the full audio concat succeeds.
"""
import json, pathlib

BASE = pathlib.Path(__file__).parent
TS = "2026-07-19T13:00:00"

NARRATION = (
    "The complete source is in the video description. "
    "Fork it, swap in your own data, and see what you find. "
    "If your numbers break the pattern, that is the interesting result."
)
CODE = (
    "# FORK IT\n"
    "#\n"
    "# → clone the source (link in description)\n"
    "# → swap in your own data\n"
    "# → run it\n"
    "# → the interesting result is when your numbers break the pattern"
)

for slug_dir in sorted(BASE.glob("claude-liam-cli-*")):
    bs_path = slug_dir / "beat_sheet.json"
    if not bs_path.exists():
        print(f"SKIP  {slug_dir.name}")
        continue

    data = json.loads(bs_path.read_text())

    # Pull segment label from B00
    segment = slug_dir.name.replace("claude-liam-cli-", "").replace("-", " ").upper()
    for b in data["beats"]:
        if b["beat_id"] == "B00":
            seg = b.get("shot", {}).get("remotion", {}).get("props", {}).get("segment", "")
            if seg:
                segment = seg
            break

    for b in data["beats"]:
        if b["beat_id"] != "B08":
            continue

        b["narration_text"] = NARRATION
        b["audio_file"] = "mp3/beat-B08.mp3"
        b["estimated_duration_s"] = 12
        b["shot"] = {
            "type": "GRAPHIC",
            "source": "remotion",
            "motion": "fade",
            "remotion": {
                "pattern": "ClaudeCodeBeat",
                "props": {
                    "title": "fork_it.md",
                    "code": CODE,
                    "sparkLine": segment
                },
                "rendered": {"out": "media/B08.mp4", "at": ""}
            }
        }
        b["build"] = {"status": "NEEDS-RENDER", "src": None, "filled_by": None, "at": TS}
        break

    bs_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"UPDATED  {slug_dir.name}")

print("\nDone. Run build_all_13.sh then final_all_13.sh.")
