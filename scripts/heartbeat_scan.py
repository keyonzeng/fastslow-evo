#!/usr/bin/env python3
import json
import argparse
from pathlib import Path


def classify(p):
    incidents = int(p.get("incidents", 0))
    corrections = int(p.get("corrections", 0))
    wins = int(p.get("wins", 0))
    cross = bool(p.get("cross_context", False))
    regressions = int(p.get("regressions", 0))

    if regressions >= 2:
        return "rollback-candidate"
    if incidents >= 3 and wins >= 2 and cross and regressions == 0:
        return "promote-candidate"
    if wins >= 1 and regressions == 0:
        return "stay-fast"
    return "noise"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("evidence_json")
    args = p.parse_args()
    data = json.loads(Path(args.evidence_json).read_text())
    patterns = data.get("patterns", [])
    for item in patterns:
        got = classify(item)
        expected = item.get("expected")
        print(json.dumps({"id": item.get("id"), "expected": expected, "got": got, "ok": got == expected}, ensure_ascii=False))


if __name__ == "__main__":
    main()
