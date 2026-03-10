#!/usr/bin/env python3
from pathlib import Path
import json, re, argparse
from datetime import datetime

HOME = Path.home()
BASE = HOME / '.openclaw' / 'workspace' / 'fastslow'
PROPOSALS = BASE / 'proposals'


def read_recurrence(path: Path):
    text = path.read_text(encoding='utf-8', errors='ignore').lower()
    m = re.search(r'recurrence[_ -]?hint:\s*(\d+)', text)
    return int(m.group(1)) if m else 1


def classify(f: Path):
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
    return {'file': str(f), 'state': state, 'recurrence': rec}


def write_candidate(item):
    PROPOSALS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    stem = Path(item['file']).stem
    out = PROPOSALS / f"candidate-{stamp}-{stem}.md"
    out.write_text(f"# Promotion Candidate\n\n- Source: {item['file']}\n- State: {item['state']}\n- Recurrence: {item['recurrence']}\n", encoding='utf-8')
    return str(out)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--write-candidates', action='store_true')
    args = p.parse_args()
    out = []
    for folder in [BASE/'evidence'/'incidents', BASE/'evidence'/'corrections', BASE/'evidence'/'wins']:
        if not folder.exists():
            continue
        for f in sorted(folder.glob('*.md')):
            if f.name.startswith('_'):
                continue
            item = classify(f)
            if args.write_candidates and item['state'] == 'promote-candidate':
                item['candidate_file'] = write_candidate(item)
            out.append(item)
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
