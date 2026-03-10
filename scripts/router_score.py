#!/usr/bin/env python3
import json
import argparse
from pathlib import Path

MAP = {
    "low": 1,
    "medium": 2,
    "moderate": 2,
    "high": 3,
    "easy": 1,
    "hard": 3,
}


def route(case):
    recurrence = int(case.get("recurrence", 1))
    blast = MAP.get(case.get("blast_radius", "low"), 1)
    validation = MAP.get(case.get("validation", "easy"), 1)
    risk = MAP.get(case.get("risk", "low"), 1)
    reuse = MAP.get(case.get("reuse", "low"), 1)
    corr = MAP.get(case.get("correction_density", "low"), 1)

    if recurrence >= 3 and (blast >= 2 or risk >= 2 or reuse >= 2):
        return "slow"
    if recurrence <= 2 and blast == 1 and risk == 1 and validation == 1:
        return "fast"
    if recurrence == 1 and reuse == 1 and validation >= 3 and corr == 1:
        return "ignore"
    return "observe"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cases_json")
    args = p.parse_args()
    cases = json.loads(Path(args.cases_json).read_text())
    total = len(cases)
    correct = 0
    for c in cases:
        got = route(c)
        expected = c.get("expected")
        ok = got == expected
        correct += int(ok)
        print(json.dumps({"id": c.get("id"), "expected": expected, "got": got, "ok": ok}, ensure_ascii=False))
    print(json.dumps({"total": total, "correct": correct, "accuracy": round(correct/total, 3)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
