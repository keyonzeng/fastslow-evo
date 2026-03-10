#!/usr/bin/env python3
from pathlib import Path
import json

HOME = Path.home()
WORKSPACE = HOME / '.openclaw' / 'workspace'
HEARTBEAT = WORKSPACE / 'HEARTBEAT.md'
FASTSLOW = WORKSPACE / 'fastslow'

START_MARK = "# FastSlow Evo"
END_MARK = "# End FastSlow Evo"
HEARTBEAT_BLOCK = """# FastSlow Evo
- Review `fastslow/evidence/` for repeated incidents, corrections, and wins.
- If a pattern looks stable and recurrence is 3+, run `python3 ~/.openclaw/workspace/skills/fastslow-evo/scripts/heartbeat_runtime.py --write-candidates`.
- If there are no meaningful candidates or rollbacks, stay quiet.
# End FastSlow Evo
"""

README = """# FastSlow Runtime

This directory stores FastSlow Evo runtime artifacts.
"""

DIRS = [
    FASTSLOW / 'evidence' / 'incidents',
    FASTSLOW / 'evidence' / 'corrections',
    FASTSLOW / 'evidence' / 'wins',
    FASTSLOW / 'proposals',
    FASTSLOW / 'scorecards',
    FASTSLOW / 'specs' / 'capabilities',
    FASTSLOW / 'specs' / 'behaviors',
    FASTSLOW / 'specs' / 'validations',
    FASTSLOW / 'specs' / 'evolutions',
    FASTSLOW / 'specs' / 'materializations',
]

def main():
    for d in DIRS:
        d.mkdir(parents=True, exist_ok=True)
    (FASTSLOW / 'README.md').write_text(README, encoding='utf-8')

    existing = HEARTBEAT.read_text(encoding='utf-8') if HEARTBEAT.exists() else "# HEARTBEAT.md\n\n"
    if START_MARK in existing and END_MARK in existing:
        before = existing.split(START_MARK, 1)[0]
        after = existing.split(END_MARK, 1)[1]
        existing = before.rstrip() + "\n\n" + HEARTBEAT_BLOCK + after
    elif START_MARK in existing:
        before = existing.split(START_MARK, 1)[0]
        existing = before.rstrip() + "\n\n" + HEARTBEAT_BLOCK
    else:
        if not existing.endswith('\n'):
            existing += '\n'
        existing += '\n' + HEARTBEAT_BLOCK
    HEARTBEAT.write_text(existing, encoding='utf-8')

    print(json.dumps({
        'runtime': str(FASTSLOW),
        'heartbeat': str(HEARTBEAT),
        'heartbeat_configured': True,
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
