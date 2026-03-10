#!/usr/bin/env python3
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = ROOT / 'scripts'

CMDS = {
    'install': SCRIPTS / 'install_openclaw.py',
    'setup': SCRIPTS / 'setup_runtime.py',
    'capture': SCRIPTS / 'capture_runtime.py',
    'capture-text': SCRIPTS / 'capture_from_text.py',
    'route': SCRIPTS / 'route_runtime.py',
    'heartbeat': SCRIPTS / 'heartbeat_runtime.py',
    'candidate': SCRIPTS / 'build_promotion_candidate.py',
}


def main():
    p = argparse.ArgumentParser(prog='fastslow.py')
    p.add_argument('command', choices=CMDS.keys())
    p.add_argument('args', nargs=argparse.REMAINDER)
    ns = p.parse_args()
    cmd = [sys.executable, str(CMDS[ns.command]), *ns.args]
    raise SystemExit(subprocess.run(cmd).returncode)


if __name__ == '__main__':
    main()
