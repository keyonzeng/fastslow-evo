#!/usr/bin/env python3
from pathlib import Path
import argparse
from datetime import datetime

GAPS = {
    "capability_gap",
    "behavior_gap",
    "validation_gap",
    "retrieval_gap",
    "workflow_gap",
    "safety_gap",
    "tooling_gap",
    "scope_gap",
}

TEMPLATE = """# Incident Record: {incident_id}

## Summary
{summary}

## Source
- {source}

## Triggering Task
{task}

## Observed Failure
<fill>

## Evidence
- logs:
- tool outputs:
- screenshots/files:
- user feedback:

## Primary Gap Type
- {gap}

## Secondary Tags
- 

## Impact
- trust
- cost
- time
- safety
- quality

## Immediate Mitigation
<fill>

## Candidate Spec Delta
<fill>

## Notes

"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("summary")
    p.add_argument("--gap", required=True, choices=sorted(GAPS))
    p.add_argument("--source", default="system")
    p.add_argument("--task", default="<fill>")
    p.add_argument("--out", default="evidence/incidents")
    args = p.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    incident_id = f"inc-{stamp}"
    path = out_dir / f"{incident_id}.md"
    path.write_text(TEMPLATE.format(incident_id=incident_id, **vars(args)), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
