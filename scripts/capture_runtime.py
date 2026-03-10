#!/usr/bin/env python3
from pathlib import Path
import argparse
from datetime import datetime

HOME = Path.home()
BASE = HOME / '.openclaw' / 'workspace' / 'fastslow'
KIND_DIR = {
    'incident': BASE / 'evidence' / 'incidents',
    'correction': BASE / 'evidence' / 'corrections',
    'win': BASE / 'evidence' / 'wins',
}

TEMPLATE = """# {kind_title}: {record_id}

## Summary
{summary}

## Source
- {source}

## Context
{context}

## Notes
- gap: {gap}
- recurrence_hint: {recurrence}
- created_at: {created_at}
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument('kind', choices=['incident','correction','win'])
    p.add_argument('summary')
    p.add_argument('--source', default='runtime')
    p.add_argument('--context', default='<fill>')
    p.add_argument('--gap', default='unknown')
    p.add_argument('--recurrence', default='1')
    args = p.parse_args()

    out_dir = KIND_DIR[args.kind]
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    record_id = f"{args.kind[:4]}-{ts}"
    path = out_dir / f"{record_id}.md"
    path.write_text(TEMPLATE.format(
        kind_title=args.kind.capitalize(),
        record_id=record_id,
        created_at=datetime.now().isoformat(timespec='seconds'),
        **vars(args)
    ), encoding='utf-8')
    print(path)

if __name__ == '__main__':
    main()
