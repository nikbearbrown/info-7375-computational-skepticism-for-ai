#!/usr/bin/env python3
"""
fix_cs_new_rules.py — Convert all 124 comp-skepticism reels to the new rules.

Performs IN ORDER (per Bear's standing order):
  1. SlateCard body beats → FormACard  (BC-1)
  2. ClaudeWindow view=artifact body beats → FormACard  (BC-2)
  3. OutroSeries → BVDT (ClaudeVerdictArtifact)  (BC-4)
  4. OutroCTA → BHTF (ClaudeComposerAsk YOUR TURN)  (BC-4)
  5. Missing B00 → add ClaudeComposerAsk cold open at index 0
  6. Missing BOUT → add ClaudeTitleOutro at end
  7. Confirm voice = kokoro:am_onyx

NEVER silently rewrites: writes a DIFF REPORT to fix_cs_new_rules.md.
Creates beat_sheet.json.bak before modifying.
Deletes stale media/*.mp4 for changed beats (keeps audio, source).

Usage:
    python3 fix_cs_new_rules.py [--dry-run] [--reel <slug>]
"""

import json, os, re, sys
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent
DRY = '--dry-run' in sys.argv
ONLY = None
for i, a in enumerate(sys.argv):
    if a == '--reel' and i + 1 < len(sys.argv):
        ONLY = sys.argv[i + 1]

BOOKEND_IDS = frozenset({'B00', 'BVDT', 'BHTF', 'BOUT'})

WORLD_GREETINGS = [
    'Hola', 'Bonjour', 'Sawubona', 'Namaste', 'Jambo', 'Ciao', 'Olá',
    'Merhaba', 'Konnichiwa', 'Annyeong', 'Ni hao', 'Привет', 'Hej',
]


def world_greeting(slug: str) -> str:
    seed = sum(ord(c) for c in slug) % len(WORLD_GREETINGS)
    return WORLD_GREETINGS[seed]


def smart_split(headline: str, max_chars: int = 55) -> list:
    """Split a headline at natural break points if > max_chars."""
    if len(headline) <= max_chars:
        return [headline]
    # Try splitting at " — "
    if ' — ' in headline:
        parts = headline.split(' — ', 1)
        return [p.strip() for p in parts if p.strip()]
    # Try splitting at a conjunction near the middle
    words = headline.split()
    mid = len(words) // 2
    for split_word in ('and', 'but', 'or', 'so', 'yet', 'nor'):
        for i in range(max(0, mid - 3), min(len(words), mid + 4)):
            if words[i].lower() == split_word:
                line1 = ' '.join(words[:i])
                line2 = ' '.join(words[i:])
                if line1 and line2:
                    return [line1, line2]
    # Fallback: split at nearest space before max_chars
    if len(headline) > max_chars:
        cut = headline[:max_chars].rfind(' ')
        if cut > 0:
            return [headline[:cut].strip(), headline[cut:].strip()]
    return [headline]


def derive_bvdt_props(data: dict, title: str) -> dict:
    """Derive BVDT ClaudeVerdictArtifact props from the beat sheet."""
    beats = data.get('beats', [])
    # Find the last RECAP SlateCard (eyebrow contains 'RECAP' or 'CONCLUSION')
    recap_headline = ''
    for b in beats:
        rem = b.get('shot', {}).get('remotion') or {}
        if rem.get('pattern') == 'SlateCard':
            eyebrow = rem.get('props', {}).get('eyebrow', '').upper()
            if any(w in eyebrow for w in ('RECAP', 'CONCLUSION', 'VERDICT', 'TAKEAWAY', 'KEY')):
                recap_headline = rem.get('props', {}).get('headline', '')
    if not recap_headline:
        # Fall back to last SlateCard headline
        for b in reversed(beats):
            rem = b.get('shot', {}).get('remotion') or {}
            if rem.get('pattern') == 'SlateCard':
                recap_headline = rem.get('props', {}).get('headline', '')
                break

    # Extract 2-3 key narration sentences from the last few body beats
    narration_lines = []
    for b in reversed(beats):
        bid = b.get('beat_id', '')
        if bid in BOOKEND_IDS:
            continue
        narr = (b.get('narration_text') or '').strip()
        if narr and len(narr) > 20:
            # Split at sentence boundary, take first sentence up to 80 chars
            first_sent = re.split(r'(?<=[.!?])\s+', narr)[0]
            if 20 < len(first_sent) <= 90:
                narration_lines.append(first_sent)
        if len(narration_lines) >= 3:
            break

    heading = recap_headline[:80] if recap_headline else f'Key findings — {title}'
    # Build 2-3 lines: use narration sentences if available
    lines = narration_lines[:3]
    if not lines:
        lines = [heading]

    return {
        'artifactTitle': title[:60],
        'artifactHeading': heading[:80],
        'artifactLines': lines,
    }


def derive_bhtf_props(data: dict, title: str, slug: str) -> dict:
    """Derive BHTF YOUR TURN ClaudeComposerAsk props from the beat sheet."""
    meta = data.get('metadata', {})
    kicker = meta.get('kicker', '')
    # Derive the 'command' from the first body beat narration or kicker
    command = kicker if kicker else f'Ask Claude: {title}'
    # Truncate command to something reasonable
    if len(command) > 120:
        command = command[:117] + '...'

    topic_upper = title.upper()[:55]
    greeting = world_greeting(slug + 'ht')

    return {
        'topic': f'YOUR TURN — {topic_upper}',
        'segment': title[:60],
        'greeting': f'{greeting}, Liam.',
        'command': command,
        'runningText': 'running…',
        'folderLabel': '@NikBearBrown',
        'modelLabel': 'Fable 5',
        'effortLabel': 'Low',
    }


def derive_b00_props(data: dict, title: str, slug: str) -> dict:
    """Derive B00 ClaudeComposerAsk cold open props."""
    meta = data.get('metadata', {})
    kicker = meta.get('kicker', '')
    series = 'COMPUTATIONAL SKEPTICISM FOR AI'
    # Derive cold open question from kicker or first beat narration
    first_narr = ''
    for b in data.get('beats', []):
        narr = (b.get('narration_text') or '').strip()
        if narr and len(narr) > 20:
            first_narr = re.split(r'(?<=[.!?])\s+', narr)[0]
            break
    command = kicker if kicker else first_narr if first_narr else title
    if len(command) > 120:
        command = command[:117] + '...'

    greeting = world_greeting(slug)

    return {
        'topic': series,
        'segment': title[:60],
        'greeting': f'{greeting}, Liam.',
        'command': command,
        'runningText': 'analyzing…',
        'folderLabel': '@NikBearBrown',
        'modelLabel': 'Fable 5',
        'effortLabel': 'High',
    }


def derive_bout_props(data: dict, title: str, slug: str) -> dict:
    """Derive BOUT ClaudeTitleOutro props."""
    meta = data.get('metadata', {})
    handle = (meta.get('channel_title') or '@NikBearBrown').strip() or '@NikBearBrown'
    return {
        'title': title,
        'slug': slug,
        'handle': handle,
        'subline': '',
    }


def make_slate_beat(beat_id: str, pattern: str, props: dict,
                    narration: str = '', estimated_s: float = 12.0) -> dict:
    return {
        'beat_id': beat_id,
        'act': beat_id,
        'estimated_duration_s': estimated_s,
        'actual_duration_s': None,
        'narration_text': narration,
        'audio_file': f'mp3/beat-{beat_id}.mp3',
        'build': {'status': 'SLATE'},
        'shot': {
            'type': 'REMOTION',
            'remotion': {
                'pattern': pattern,
                'props': props,
                'rendered': {'out': '', 'at': ''},
            },
        },
    }


def fix_reel(reel_dir: Path) -> dict:
    """Returns a dict of changes made: {beat_id: description}. Empty = no changes."""
    bs_path = reel_dir / 'beat_sheet.json'
    if not bs_path.exists():
        return {}

    data = json.loads(bs_path.read_text())
    meta = data.get('metadata', {})
    slug = meta.get('slug', reel_dir.name)
    title = meta.get('title', slug)
    channel_handle = (meta.get('channel_title') or '@NikBearBrown').strip() or '@NikBearBrown'

    changes = {}
    beats = data.get('beats', [])
    beat_ids = {b['beat_id'] for b in beats}

    # 1+2. Convert banned card beats (SlateCard / ClaudeWindow artifact body)
    for b in beats:
        bid = b.get('beat_id', '')
        if bid in BOOKEND_IDS:
            continue
        rem = b.get('shot', {}).get('remotion') or {}
        pattern = rem.get('pattern', '')
        props = rem.get('props', {})

        if pattern == 'SlateCard':
            headline = props.get('headline', '')
            lines = smart_split(headline)
            new_props = {'lines': lines, 'dark': False}
            rem['pattern'] = 'FormACard'
            rem['props'] = new_props
            # Delete rendered marker so it re-renders
            rem['rendered'] = {'out': '', 'at': ''}
            if 'build' not in b:
                b['build'] = {}
            b['build']['status'] = 'SLATE'
            media_file = reel_dir / 'media' / f'{bid}.mp4'
            if media_file.exists() and not DRY:
                media_file.unlink()
            changes[bid] = f'SlateCard → FormACard(lines={lines})'

        elif pattern == 'ClaudeWindow' and props.get('view') == 'artifact':
            heading = props.get('artifactHeading', title)
            art_lines = props.get('artifactLines', [])
            lines = smart_split(heading)
            if art_lines:
                lines = [heading] + art_lines[:2]  # heading + up to 2 lines
            new_props = {'lines': lines, 'dark': False}
            rem['pattern'] = 'FormACard'
            rem['props'] = new_props
            rem['rendered'] = {'out': '', 'at': ''}
            if 'build' not in b:
                b['build'] = {}
            b['build']['status'] = 'SLATE'
            media_file = reel_dir / 'media' / f'{bid}.mp4'
            if media_file.exists() and not DRY:
                media_file.unlink()
            changes[bid] = f'ClaudeWindow[artifact] → FormACard(lines={lines[:1]}…)'

    # Detect vox-format reels (HANDOFF/OUTRO beats) — bookend addition is handled
    # by the REFACTOR skill, not this script. We still fix body beats (SlateCard →
    # FormACard) but skip the structural bookend injection.
    has_vox_structure = any(
        b.get('beat_id', '') in ('HANDOFF', 'OUTRO')
        or b.get('shot', {}).get('remotion', {}).get('pattern', '') in ('OutroSeries', 'OutroCTA')
        for b in beats
    )

    if has_vox_structure and any(
        b.get('beat_id', '') in ('HANDOFF', 'OUTRO') for b in beats
    ):
        # Vox-format reel: only do body fixes, flag as needs-refactor
        if changes:
            changes['_structure'] = 'NEEDS-REFACTOR: vox HANDOFF/OUTRO structure — bookend injection skipped; run REFACTOR skill'
        else:
            changes['_structure'] = 'NEEDS-REFACTOR: vox HANDOFF/OUTRO structure — no banned body beats found but bookend structure must be fixed with REFACTOR skill'
        if changes and not DRY:
            backup = bs_path.with_suffix('.json.bak-newrules')
            if not backup.exists():
                backup.write_text(bs_path.read_text())
            bs_path.write_text(json.dumps(data, indent=2))
        return changes

    # 3. OutroSeries → BVDT (ClaudeVerdictArtifact)
    for i, b in enumerate(beats):
        if b.get('shot', {}).get('remotion', {}).get('pattern') == 'OutroSeries':
            bvdt_props = derive_bvdt_props(data, title)
            old_id = b['beat_id']
            b['beat_id'] = 'BVDT'
            b['act'] = 'BVDT'
            rem = b.setdefault('shot', {}).setdefault('remotion', {})
            rem['pattern'] = 'ClaudeVerdictArtifact'
            rem['props'] = bvdt_props
            rem['rendered'] = {'out': '', 'at': ''}
            if 'build' not in b:
                b['build'] = {}
            b['build']['status'] = 'SLATE'
            media_file = reel_dir / 'media' / f'{old_id}.mp4'
            if media_file.exists() and not DRY:
                media_file.unlink()
            changes[f'{old_id}→BVDT'] = f'OutroSeries → ClaudeVerdictArtifact'

    # 4. OutroCTA → BHTF (ClaudeComposerAsk YOUR TURN)
    for i, b in enumerate(beats):
        if b.get('shot', {}).get('remotion', {}).get('pattern') == 'OutroCTA':
            bhtf_props = derive_bhtf_props(data, title, slug)
            old_id = b['beat_id']
            b['beat_id'] = 'BHTF'
            b['act'] = 'BHTF'
            rem = b.setdefault('shot', {}).setdefault('remotion', {})
            rem['pattern'] = 'ClaudeComposerAsk'
            rem['props'] = bhtf_props
            rem['rendered'] = {'out': '', 'at': ''}
            if 'build' not in b:
                b['build'] = {}
            b['build']['status'] = 'SLATE'
            media_file = reel_dir / 'media' / f'{old_id}.mp4'
            if media_file.exists() and not DRY:
                media_file.unlink()
            changes[f'{old_id}→BHTF'] = f'OutroCTA → ClaudeComposerAsk YOUR TURN'

    # 3b. Rename body beats that use bookend patterns but have non-standard beat_ids
    # e.g. B13=ClaudeVerdictArtifact → rename to BVDT; B01=ClaudeComposerAsk cold open → B00
    # This must run after the OutroSeries/OutroCTA rename so we don't double-rename.
    beat_ids = {b['beat_id'] for b in beats}

    if 'BVDT' not in beat_ids:
        for b in beats:
            bid = b.get('beat_id', '')
            if bid in BOOKEND_IDS or bid == 'B00':
                continue
            pattern = b.get('shot', {}).get('remotion', {}).get('pattern', '')
            if pattern == 'ClaudeVerdictArtifact':
                old_id = bid
                b['beat_id'] = 'BVDT'
                b['act'] = 'BVDT'
                media_file = reel_dir / 'media' / f'{old_id}.mp4'
                if media_file.exists() and not DRY:
                    media_file.unlink()
                changes[f'{old_id}→BVDT'] = 'renamed ClaudeVerdictArtifact body beat to BVDT'
                beat_ids = {b2['beat_id'] for b2 in beats}
                break

    # Rename ClaudeComposerAsk cold-open that's not named B00 (and there's no B00 yet)
    beat_ids = {b['beat_id'] for b in beats}
    if 'B00' not in beat_ids:
        first_beat = beats[0] if beats else None
        if first_beat and first_beat.get('beat_id', '') not in BOOKEND_IDS:
            pattern = first_beat.get('shot', {}).get('remotion', {}).get('pattern', '')
            props = first_beat.get('shot', {}).get('remotion', {}).get('props', {})
            # If it's ClaudeComposerAsk and NOT a YOUR TURN beat, treat as cold open
            if pattern == 'ClaudeComposerAsk' and 'YOUR TURN' not in props.get('topic', ''):
                old_id = first_beat['beat_id']
                first_beat['beat_id'] = 'B00'
                first_beat['act'] = 'B00'
                media_file = reel_dir / 'media' / f'{old_id}.mp4'
                if media_file.exists() and not DRY:
                    media_file.unlink()
                changes[f'{old_id}→B00'] = 'renamed ClaudeComposerAsk cold-open to B00'
                beat_ids = {b2['beat_id'] for b2 in beats}

    # Refresh beat_ids after potential renames
    beat_ids = {b['beat_id'] for b in beats}

    # 5. Add missing BOUT at end
    if 'BOUT' not in beat_ids:
        bout_props = derive_bout_props(data, title, slug)
        bout_beat = make_slate_beat('BOUT', 'ClaudeTitleOutro', bout_props, estimated_s=8.0)
        beats.append(bout_beat)
        changes['BOUT'] = f'added ClaudeTitleOutro(title={title[:40]})'

    # Refresh beat_ids
    beat_ids = {b['beat_id'] for b in beats}

    # 6. Add missing BVDT before BOUT (if still missing)
    if 'BVDT' not in beat_ids:
        bvdt_props = derive_bvdt_props(data, title)
        bvdt_beat = make_slate_beat('BVDT', 'ClaudeVerdictArtifact', bvdt_props, estimated_s=20.0)
        # Insert before BOUT
        bout_idx = next((i for i, b in enumerate(beats) if b['beat_id'] == 'BOUT'), len(beats))
        beats.insert(bout_idx, bvdt_beat)
        changes['BVDT'] = f'added ClaudeVerdictArtifact'

    # Refresh beat_ids
    beat_ids = {b['beat_id'] for b in beats}

    # 7. Add missing BHTF before BOUT (if still missing)
    if 'BHTF' not in beat_ids:
        bhtf_props = derive_bhtf_props(data, title, slug)
        bhtf_beat = make_slate_beat('BHTF', 'ClaudeComposerAsk', bhtf_props, estimated_s=15.0)
        bout_idx = next((i for i, b in enumerate(beats) if b['beat_id'] == 'BOUT'), len(beats))
        beats.insert(bout_idx, bhtf_beat)
        changes['BHTF'] = f'added ClaudeComposerAsk YOUR TURN'

    # Refresh beat_ids
    beat_ids = {b['beat_id'] for b in beats}

    # 8. Add missing B00 at index 0
    if 'B00' not in beat_ids:
        b00_props = derive_b00_props(data, title, slug)
        b00_beat = make_slate_beat('B00', 'ClaudeComposerAsk', b00_props, estimated_s=20.0)
        beats.insert(0, b00_beat)
        changes['B00'] = f'added ClaudeComposerAsk cold open'

    # 9. Confirm voice = kokoro:am_onyx
    voice = meta.get('voice', '')
    if voice and 'am_onyx' not in voice and 'onyx' not in voice:
        if not DRY:
            meta['voice'] = 'kokoro:am_onyx'
        changes['voice'] = f'fixed voice: {voice!r} → "kokoro:am_onyx"'
    elif not voice:
        if not DRY:
            meta['voice'] = 'kokoro:am_onyx'
        changes['voice'] = 'added voice: "kokoro:am_onyx"'

    if changes and not DRY:
        # Backup
        backup = bs_path.with_suffix('.json.bak-newrules')
        if not backup.exists():
            backup.write_text(bs_path.read_text())
        bs_path.write_text(json.dumps(data, indent=2))

    return changes


# ── Main ──────────────────────────────────────────────────────────────────────

reel_dirs = sorted(
    d for d in BASE.iterdir()
    if d.is_dir() and d.name.startswith('claude-liam-')
    and (ONLY is None or d.name == ONLY)
    and (d / 'beat_sheet.json').exists()
)

prefix = '[DRY-RUN] ' if DRY else ''
print(f'{prefix}Scanning {len(reel_dirs)} reels...')
print()

report_lines = [
    f'# fix_cs_new_rules — diff report',
    f'# Generated {datetime.now().strftime("%Y-%m-%d %H:%M")}',
    f'# {"DRY RUN — no files modified" if DRY else "APPLIED — beat sheets updated"}',
    '',
]

fixed_count = 0
for reel_dir in reel_dirs:
    changes = fix_reel(reel_dir)
    if changes:
        fixed_count += 1
        print(f'{prefix}{reel_dir.name}:')
        report_lines.append(f'## {reel_dir.name}')
        for bid, desc in sorted(changes.items()):
            print(f'  {bid}: {desc}')
            report_lines.append(f'  - {bid}: {desc}')
        print()
        report_lines.append('')

report_lines.append(f'## Summary')
report_lines.append(f'{prefix}Fixed {fixed_count}/{len(reel_dirs)} reel(s).')
if DRY:
    report_lines.append('Run without --dry-run to apply changes.')

report_text = '\n'.join(report_lines)
report_path = BASE / 'fix_cs_new_rules.md'
if not DRY:
    report_path.write_text(report_text)
    print(f'Report → {report_path}')
else:
    print(report_text)

print(f'\n{prefix}Fixed {fixed_count}/{len(reel_dirs)} reel(s).')
if DRY:
    print('Run without --dry-run to apply changes.')
