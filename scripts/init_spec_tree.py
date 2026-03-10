#!/usr/bin/env python3
from pathlib import Path
import argparse

SUBDIRS = [
    "specs/capabilities",
    "specs/behaviors",
    "specs/validations",
    "specs/evolutions",
    "specs/materializations",
    "evidence/incidents",
    "evidence/corrections",
    "evidence/wins",
    "proposals",
    "scorecards",
]

README = """# Spec Tree

This directory was initialized by spec-driven-evolution.

Workflow:
1. capture evidence
2. classify gap
3. draft spec delta
4. define validation
5. materialize to the lightest sufficient artifact
6. measure outcomes
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    for rel in SUBDIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)

    readme = root / "specs" / "README.md"
    if not readme.exists():
        readme.write_text(README, encoding="utf-8")

    print(f"Initialized spec tree at {root}")


if __name__ == "__main__":
    main()
