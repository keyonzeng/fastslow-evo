#!/usr/bin/env python3
from pathlib import Path
import argparse
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

ALIASES = {
    "配置 fastslow evo": "setup",
    "启用 fastslow evo": "setup",
    "启用 fastslow evo heartbeat": "setup",
    "setup fastslow evo": "setup",
    "enable fastslow evo": "setup",
    "enable fastslow evo heartbeat": "setup",
}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("command", nargs="?", default="setup")
    args = p.parse_args()
    cmd = ALIASES.get(args.command.strip().lower(), args.command.strip().lower())
    if cmd != "setup":
        print(f"Unsupported command: {args.command}")
        sys.exit(2)
    script = ROOT / "scripts" / "setup_runtime.py"
    subprocess.run([sys.executable, str(script)], check=True)


if __name__ == "__main__":
    main()
