#!/usr/bin/env python3
from pathlib import Path
import argparse
from datetime import datetime

TEMPLATE = """# Promotion Candidate: {candidate_id}

## Source Pattern
- Related incidents: {incidents}
- Related corrections: {corrections}
- Related wins: {wins}
- Current tiny fix: {tiny_fix}

## Why this is a candidate
- Recurrence: {recurrence}
- Stability across contexts: <fill>
- Reuse evidence: <fill>
- Why local treatment may now be insufficient: <fill>

## Proposed Promotion
- Target loop: slow
- Proposed artifact: {artifact}
- Why this is the lightest durable promotion: <fill>

## Validation
- Validation path: <fill>
- Success criteria: <fill>
- Regression risks: <fill>

## Recommendation
- stay-fast | promote | rollback | observe
"""

def main():
    p = argparse.ArgumentParser()
    p.add_argument("title")
    p.add_argument("--incidents", default="<fill>")
    p.add_argument("--corrections", default="<fill>")
    p.add_argument("--wins", default="<fill>")
    p.add_argument("--tiny-fix", default="<fill>")
    p.add_argument("--recurrence", default="3")
    p.add_argument("--artifact", default="validation-spec")
    p.add_argument("--out", default="proposals")
    args = p.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    candidate_id = f"promote-{stamp}-{args.title.replace(' ','-')}"
    path = out_dir / f"{candidate_id}.md"
    path.write_text(TEMPLATE.format(candidate_id=candidate_id, **vars(args)), encoding="utf-8")
    print(path)

if __name__ == "__main__":
    main()
