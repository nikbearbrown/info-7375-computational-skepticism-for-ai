#!/usr/bin/env python3
"""DE-WORDIFY PASS 1 — shorten any prose element >12 words to label form.

For each failing reel:
  1. Run type_check (skip-pixels) → identify wordy beats
  2. For each beat: shorten ALL prose elements that exceed 12 words
  3. Write updated beat_sheet.json
  4. Recompile with art run
  5. Append results to BUILD-LOG.md

Shortening rule:
  - Strip articles and terminal phrases; keep core concept in ≤12 words
  - Truncate at natural breaks: em-dash (—), 'that'/'which' clause, trailing prep
  - If no break found: take first 11 words + end-punctuation trimmed

Usage: python3 dewordify.py [--slug SLUG] [--dry-run] [--check-only]
"""
import json
import re
import subprocess
import sys
import os
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent
BOOKS = BASE.parent.parent  # books/
ART = BOOKS / "brutalist-art/art"
TYPE_CHECK = BOOKS / "brutalist-art/runtime/scripts/type_check.py"

WORDY_MAX = 12  # words per element threshold

# Prose fields checked by type_check §8.5
TEXT_FIELDS = {"note", "headline", "artifactHeading", "sparkLine", "body", "text", "title"}
LIST_FIELDS = {"artifactLines", "chips", "output"}


def word_count(s: str) -> int:
    return len(str(s).split())


def shorten(text: str, max_words: int = 12) -> str:
    """Shorten text to ≤max_words using natural break points."""
    words = text.split()
    if len(words) <= max_words:
        return text

    # Strategy 1: split at em-dash — keep whichever half is ≤max_words
    for sep in [" — ", "—", " — "]:
        parts = text.split(sep, 1)
        if len(parts) == 2:
            left = parts[0].strip().rstrip(",;")
            right = parts[1].strip().rstrip(".")
            if word_count(left) <= max_words:
                return left
            if word_count(right) <= max_words:
                return right

    # Strategy 2: split at a middot bullet · — keep up to max_words worth of bullets
    if " · " in text:
        parts = text.split(" · ")
        result = parts[0]
        for p in parts[1:]:
            candidate = result + " · " + p
            if word_count(candidate) <= max_words:
                result = candidate
            else:
                break
        if word_count(result) <= max_words:
            return result.rstrip(" ·").rstrip(".,")

    # Strategy 3: cut at "that"/"which"/"where"/"when" subordinate clause
    for sub in [" that ", " which ", " where ", " when ", " who "]:
        idx = text.find(sub)
        if idx > 0:
            candidate = text[:idx].strip().rstrip(",;")
            if word_count(candidate) <= max_words:
                return candidate

    # Strategy 4: cut at ", " after word 8
    parts = text.split(", ")
    result = parts[0]
    for p in parts[1:]:
        candidate = result + ", " + p
        if word_count(candidate) <= max_words:
            result = candidate
        else:
            break
    if word_count(result) <= max_words and result != text:
        return result.rstrip(",;")

    # Strategy 5: hard truncate at max_words - strip trailing prepositions/articles
    w = words[:max_words]
    # Strip trailing filler words
    fillers = {"a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "of", "for", "with"}
    while w and w[-1].lower().rstrip(".,;:") in fillers:
        w = w[:-1]
    result = " ".join(w).rstrip(".,;:")
    return result


def fix_props(props: dict) -> tuple[dict, list[str]]:
    """Shorten all wordy prose elements in props. Returns (fixed_props, changes)."""
    changes = []
    fixed = dict(props)

    for field in TEXT_FIELDS:
        if field in fixed and isinstance(fixed[field], str):
            wc = word_count(fixed[field])
            if wc > WORDY_MAX:
                short = shorten(fixed[field])
                changes.append(f"  {field}: [{wc}w] '{fixed[field][:60]}...' → '{short}'")
                fixed[field] = short

    for field in LIST_FIELDS:
        if field in fixed and isinstance(fixed[field], list):
            new_list = []
            for i, item in enumerate(fixed[field]):
                wc = word_count(str(item))
                if wc > WORDY_MAX:
                    short = shorten(str(item))
                    changes.append(f"  {field}[{i}]: [{wc}w] '{str(item)[:60]}...' → '{short}'")
                    new_list.append(short)
                else:
                    new_list.append(item)
            fixed[field] = new_list

    # Check left/right nested objects
    for field in ("left", "right"):
        if field in fixed and isinstance(fixed[field], dict):
            note = fixed[field].get("note", "")
            if note and word_count(note) > WORDY_MAX:
                short = shorten(note)
                changes.append(f"  {field}.note: [{word_count(note)}w] '{note[:60]}...' → '{short}'")
                fixed[field] = dict(fixed[field])
                fixed[field]["note"] = short

    return fixed, changes


def process_reel(reel_dir: Path, dry_run: bool = False) -> dict:
    """Process one reel: fix wordy beats, return summary."""
    slug = reel_dir.name
    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        return {"slug": slug, "status": "SKIP", "reason": "no beat_sheet.json"}

    # Run type_check first to see what's failing
    tc_result = subprocess.run(
        [sys.executable, str(TYPE_CHECK), str(reel_dir), "--skip-pixels"],
        capture_output=True, text=True, cwd=str(BOOKS)
    )
    tc_out = tc_result.stdout + tc_result.stderr

    if "GATE T: PASS" in tc_out:
        return {"slug": slug, "status": "PASS", "wordy": 0, "fixed": 0, "changes": []}

    # Load beat_sheet
    with open(bs_path) as f:
        bs = json.load(f)

    all_changes = []
    beats_fixed = []
    beats_left = []

    for beat in bs["beats"]:
        bid = beat["beat_id"]
        shot = beat.get("shot", {})
        remotion = shot.get("remotion", {})
        if not remotion:
            continue

        pattern = remotion.get("pattern", "")
        props = remotion.get("props", {})
        if not props:
            continue

        # Check if any element exceeds limit
        needs_fix = False
        for field in TEXT_FIELDS:
            if field in props and word_count(str(props[field])) > WORDY_MAX:
                needs_fix = True
                break
        if not needs_fix:
            for field in LIST_FIELDS:
                if field in props:
                    for item in props[field]:
                        if word_count(str(item)) > WORDY_MAX:
                            needs_fix = True
                            break
        if not needs_fix:
            for side in ("left", "right"):
                if isinstance(props.get(side), dict):
                    note = props[side].get("note", "")
                    if note and word_count(note) > WORDY_MAX:
                        needs_fix = True

        if not needs_fix:
            continue

        fixed_props, changes = fix_props(props)

        # Check if we actually fixed everything
        still_bad = False
        for field in TEXT_FIELDS:
            if field in fixed_props and word_count(str(fixed_props[field])) > WORDY_MAX:
                still_bad = True
        for field in LIST_FIELDS:
            if field in fixed_props:
                for item in fixed_props[field]:
                    if word_count(str(item)) > WORDY_MAX:
                        still_bad = True

        if still_bad:
            beats_left.append(bid)

        if changes:
            beats_fixed.append(bid)
            all_changes.extend([f"Beat {bid}:"] + changes)
            if not dry_run:
                remotion["props"] = fixed_props

    if dry_run:
        return {
            "slug": slug, "status": "DRY-RUN",
            "beats_fixed": beats_fixed, "beats_left": beats_left,
            "changes": all_changes
        }

    if not beats_fixed:
        return {"slug": slug, "status": "NO-CHANGES", "wordy": 0, "fixed": 0, "changes": []}

    # Back up and write
    shutil.copy(bs_path, bs_path.with_suffix(".json.bak"))
    with open(bs_path, "w") as f:
        json.dump(bs, f, indent=2, ensure_ascii=False)
        f.write("\n")

    return {
        "slug": slug, "status": "FIXED",
        "beats_fixed": beats_fixed, "beats_left": beats_left,
        "changes": all_changes
    }


def compile_reel(reel_dir: Path) -> bool:
    """Run art run on the reel. Returns True if successful."""
    slug = reel_dir.name
    # reel path relative to BOOKS for art command
    rel = reel_dir.relative_to(BOOKS)
    result = subprocess.run(
        [str(ART), "run", str(rel)],
        cwd=str(BOOKS),
        capture_output=True, text=True,
        timeout=900  # 15 min max
    )
    if result.returncode == 0:
        print(f"  [compile] {slug}: OK")
        return True
    else:
        print(f"  [compile] {slug}: FAIL (exit {result.returncode})")
        print(result.stdout[-2000:] if result.stdout else "")
        print(result.stderr[-1000:] if result.stderr else "")
        return False


def verify_reel(reel_dir: Path) -> tuple[str, str]:
    """Re-run type_check after fix. Returns (gate_status, details)."""
    result = subprocess.run(
        [sys.executable, str(TYPE_CHECK), str(reel_dir), "--skip-pixels"],
        capture_output=True, text=True, cwd=str(BOOKS)
    )
    out = result.stdout + result.stderr
    last = out.strip().split("\n")[-1] if out.strip() else ""
    return ("PASS" if "PASS" in last else "FAIL"), last


def append_build_log(reel_dir: Path, summary: dict, gate: str):
    """Append de-wordify summary to BUILD-LOG.md."""
    log_path = reel_dir / "BUILD-LOG.md"
    slug = reel_dir.name
    now = datetime.now().strftime("%Y-%m-%d")

    entry = f"\n---\n\n## {now} — DE-WORDIFY PASS 1\n\n"
    entry += f"**GATE T after fix**: {gate}\n\n"

    if summary.get("beats_fixed"):
        entry += f"**Beats de-wordified**: {', '.join(summary['beats_fixed'])}\n\n"
        for line in summary.get("changes", []):
            entry += f"- {line.strip()}\n"
    else:
        entry += "No beats needed de-wordifying.\n"

    if summary.get("beats_left"):
        entry += f"\n**Beats still failing**: {', '.join(summary['beats_left'])} (manual review needed)\n"

    with open(log_path, "a") as f:
        f.write(entry)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="DE-WORDIFY PASS 1")
    parser.add_argument("--slug", help="Process only this slug")
    parser.add_argument("--dry-run", action="store_true", help="Show fixes without applying")
    parser.add_argument("--check-only", action="store_true", help="Only run type_check, no fixes")
    parser.add_argument("--no-compile", action="store_true", help="Fix beat_sheet only, skip compile")
    args = parser.parse_args()

    youtube_dir = BASE
    if args.slug:
        reels = [youtube_dir / args.slug]
    else:
        reels = sorted([d for d in youtube_dir.iterdir()
                        if d.is_dir() and (d / "beat_sheet.json").exists()])

    print(f"Processing {len(reels)} reels...")

    results = []
    for reel in reels:
        slug = reel.name
        print(f"\n{'='*60}")
        print(f"REEL: {slug}")

        if args.check_only:
            tc = subprocess.run(
                [sys.executable, str(TYPE_CHECK), str(reel), "--skip-pixels"],
                capture_output=True, text=True, cwd=str(BOOKS)
            )
            last = (tc.stdout + tc.stderr).strip().split("\n")[-1]
            print(f"  {last}")
            results.append({"slug": slug, "gate": "PASS" if "PASS" in last else "FAIL"})
            continue

        # Fix wordy beats
        summary = process_reel(reel, dry_run=args.dry_run)
        print(f"  Status: {summary['status']}")
        for c in summary.get("changes", []):
            print(f"    {c}")

        if args.dry_run or summary["status"] in ("PASS", "SKIP", "NO-CHANGES", "DRY-RUN"):
            results.append({"slug": slug, **summary})
            continue

        # Compile
        gate = "SKIP"
        if not args.no_compile:
            print(f"  Compiling {slug}...")
            compiled = compile_reel(reel)

            # Verify
            gate, gate_detail = verify_reel(reel)
            print(f"  GATE T after fix: {gate} — {gate_detail}")

        # Log
        append_build_log(reel, summary, gate)

        # Open cut if exists
        mp4_dir = reel / "mp4"
        cuts = list(mp4_dir.glob("*-slate.mp4")) if mp4_dir.exists() else []
        if cuts:
            subprocess.Popen(["open", str(cuts[0])])
            print(f"  Opened: {cuts[0].name}")

        results.append({"slug": slug, "gate": gate, **summary})

    # Final table
    print("\n" + "="*80)
    print("DE-WORDIFY PASS 1 — SUMMARY TABLE")
    print("="*80)
    print(f"{'Reel':<55} {'Found→Fixed':<15} {'Left':<10} {'Gate'}")
    print("-"*80)
    for r in results:
        fixed = len(r.get("beats_fixed", []))
        left = len(r.get("beats_left", []))
        gate = r.get("gate", r.get("status", "?"))
        found = fixed + left
        print(f"{r['slug']:<55} {found}→{fixed:<13} {left:<10} {gate}")


if __name__ == "__main__":
    main()
