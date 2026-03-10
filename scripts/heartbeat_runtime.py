#!/usr/bin/env python3
from pathlib import Path
import json, re

HOME = Path.home()
BASE = HOME / '.openclaw' / 'workspace' / 'fastslow'


def read_recurrence(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore').lower()
    m = re.search(r'recurrence[_ -]?hint:\s*(\d+)', text)
    return int(m.group(1)) if m else 1


def main():
    out = []
    for folder in [BASE/'evidence'/'incidents', BASE/'evidence'/'corrections', BASE/'evidence'/'wins']:
        if not folder.exists():
            continue
        for f in sorted(folder.glob('*.md')):
            if f.name.startswith('_'):
                continue
            rec = read_recurrence(f)
            text = f.read_text(encoding='utf-8', errors='ignore').lower()
            if rec >= 3 and ('across' in text or 'multiple' in text or 'repeated' in text):
                state = 'promote-candidate'
            elif 'one-off' in text or 'isolated annoyance' in text:
                state = 'noise'
            elif rec >= 2 and 'regression' in text:
                state = 'rollback-candidate'
            else:
                state = 'stay-fast'
            out.append({'file': str(f), 'state': state, 'recurrence': rec})
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
