#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re

HOME = Path.home()
BASE = HOME / '.openclaw' / 'workspace' / 'fastslow'


def detect(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore').lower()
    recurrence = 1
    m = re.search(r'recurrence[_ -]?hint:\s*(\d+)', text)
    if m:
        recurrence = int(m.group(1))
    risk = 'high' if any(k in text for k in ['privacy','boundary','shared/private','leak','unsafe']) else 'low'
    cross = any(k in text for k in ['across', 'multiple', 'repeatedly', 'channels'])
    if recurrence >= 3 and (cross or risk == 'high'):
        bucket = 'slow'
    elif recurrence == 1 and any(k in text for k in ['vague','ambiguous','felt off']) and not cross:
        bucket = 'observe'
    elif recurrence == 1 and any(k in text for k in ['one-off','isolated annoyance','no durable']) :
        bucket = 'ignore'
    else:
        bucket = 'fast'
    return {
        'path': str(path),
        'recurrence': recurrence,
        'risk': risk,
        'cross_context_hint': cross,
        'route': bucket,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--path', help='single markdown record path')
    p.add_argument('--latest', action='store_true')
    args = p.parse_args()

    if args.path:
        print(json.dumps(detect(Path(args.path)), ensure_ascii=False))
        return

    roots = [BASE/'evidence'/'incidents', BASE/'evidence'/'corrections', BASE/'evidence'/'wins']
    files = []
    for r in roots:
        files.extend(sorted(r.glob('*.md')))
    if not files:
        print(json.dumps({'error':'no runtime records found'}, ensure_ascii=False))
        return
    target = max(files, key=lambda p: p.stat().st_mtime) if args.latest else files[-1]
    print(json.dumps(detect(target), ensure_ascii=False))

if __name__ == '__main__':
    main()
