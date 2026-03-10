#!/usr/bin/env python3
from pathlib import Path
import argparse
from datetime import datetime

TEMPLATE = """# Evolution Proposal: {title}

## Evidence
- Triggering cases: {cases}
- Primary gap type: {gap}
- Recurrence count: {recurrence}

## Proposed Spec Delta
- Spec type: {spec_type}
- Summary: <fill>
- Why this is the smallest durable fix: <fill>

## Validation
- Validation level target: V2
- Checks:
  - <fill>
- Success criteria:
  - <fill>

## Materialization
- Proposed artifact: {artifact}
- Target paths:
  - <fill>

## Regression Guard
- Risks introduced:
  - <fill>
- How to detect regression:
  - <fill>

## Rollback
- Undo path: <fill>
- Preservation needs: <fill>

## Review
- Review level: {review}
- Status: draft
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("title")
    parser.add_argument("--gap", default="workflow_gap")
    parser.add_argument("--cases", default="1")
    parser.add_argument("--recurrence", default="1")
    parser.add_argument("--spec-type", default="capability")
    parser.add_argument("--artifact", default="checklist")
    parser.add_argument("--review", default="L1")
    parser.add_argument("--out", default="proposals")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = out_dir / f"evolution-{stamp}.md"
    path.write_text(TEMPLATE.format(**vars(args)), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
