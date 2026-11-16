#!/usr/bin/env python3
"""
fix_bookend_props.py — batch fix BHTF topic + BOUT slug/handle across all
claude-liam-* reels in computational-skepticism-for-ai/youtube/.

Per GATE BOOKEND requirements:
  - BHTF beat topic must contain "YOUR TURN"
  - BOUT beat props must have handle=channel_title and slug=reel-slug

Resets affected beats to SLATE and deletes their media/XX.mp4 so art run
will re-render them. Run with --dry-run to preview without modifying files.

Usage:
    python3 fix_bookend_props.py [--dry-run] [--reel <slug>]
"""

import json, os, sys
from pathlib import Path

BASE = Path(__file__).parent
DRY = '--dry-run' in sys.argv
ONLY = None
for i, a in enumerate(sys.argv):
    if a == '--reel' and i+1 < len(sys.argv):
        ONLY = sys.argv[i+1]

def fix_reel(reel_dir: Path) -> dict:
    bs_path = reel_dir / 'beat_sheet.json'
    if not bs_path.exists():
        return {}
    data = json.loads(bs_path.read_text())
    meta = data.get('metadata', {})
    slug = meta.get('slug', reel_dir.name)
    handle = (meta.get('channel_title') or '@NikBearBrown').strip() or '@NikBearBrown'
    title = meta.get('title', '')
    changed = {}

    for b in data['beats']:
        bid = b['beat_id']
        props = b.get('shot', {}).get('remotion', {}).get('props', {})
        pattern = b.get('shot', {}).get('remotion', {}).get('pattern', '')

        # Fix BHTF: topic must contain "YOUR TURN"
        if bid == 'BHTF' and 'topic' in props and 'YOUR TURN' not in props['topic']:
            old_topic = props['topic']
            # Derive a short label from metadata title (max ~60 chars after prefix)
            short = title.upper()[:55] if title else old_topic.upper()[:55]
            props['topic'] = f'YOUR TURN — {short}'
            if 'build' not in b:
                b['build'] = {}
            b['build']['status'] = 'SLATE'
            media_file = reel_dir / 'media' / f'{bid}.mp4'
            if media_file.exists() and not DRY:
                media_file.unlink()
            changed[bid] = f'topic → YOUR TURN — {short[:40]}…'

        # Fix BOUT: add slug + handle props
        if pattern == 'ClaudeTitleOutro' or bid in ('BOUT', 'C3'):
            bout_fixed = False
            if 'slug' not in props:
                props['slug'] = slug
                bout_fixed = True
            if 'handle' not in props:
                props['handle'] = handle
                bout_fixed = True
            elif props.get('handle') != handle:
                props['handle'] = handle
                bout_fixed = True
            if bout_fixed:
                if 'build' not in b:
                    b['build'] = {}
                b['build']['status'] = 'SLATE'
                media_file = reel_dir / 'media' / f'{bid}.mp4'
                if media_file.exists() and not DRY:
                    media_file.unlink()
                changed[bid] = f'slug={slug}, handle={handle}'

    if changed and not DRY:
        bs_path.write_text(json.dumps(data, indent=2))

    return changed


fixed_count = 0
reel_dirs = sorted(
    d for d in BASE.iterdir()
    if d.is_dir() and d.name.startswith('claude-liam-')
    and (ONLY is None or d.name == ONLY)
    and (d / 'beat_sheet.json').exists()
)

print(f'{"[DRY-RUN] " if DRY else ""}Scanning {len(reel_dirs)} reels...')

for reel_dir in reel_dirs:
    changes = fix_reel(reel_dir)
    if changes:
        fixed_count += 1
        prefix = '[DRY] ' if DRY else ''
        print(f'{prefix}{reel_dir.name}:')
        for bid, desc in changes.items():
            print(f'  {bid}: {desc}')

print(f'\n{"[DRY-RUN] " if DRY else ""}Fixed {fixed_count} reel(s).')
if DRY:
    print('Run without --dry-run to apply changes.')
