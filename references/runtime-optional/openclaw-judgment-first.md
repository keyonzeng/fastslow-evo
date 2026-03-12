# OpenClaw Judgment-First Design

FastSlow Evo should be judgment-first in OpenClaw.
That means the host model does the thinking, and markdown protocols make that thinking disciplined and reviewable.

## Principle

All meaningful FastSlow decisions should be made by the OpenClaw host model.
This includes:
- pattern extraction
- pattern sameness assessment
- merge vs split judgment
- fast / slow / observe / ignore / reject routing
- candidate convergence
- promotion recommendation

## What Markdown Should Do

Markdown should:
- preserve evidence context
- tell the model what questions to answer
- constrain output structure
- make review traceable
- make bad reasoning easier to spot

Markdown should not pretend to replace model judgment.
It should guide it.

## What Scripts Should Do

Scripts may still help with:
- setup
- directory initialization
- file creation
- review packet assembly
- synthetic testing

No external runtime layer should be the place where FastSlow intelligence lives.

## Success Criterion

If FastSlow is working properly in OpenClaw, you should be able to inspect the markdown trail and see:
- what evidence existed
- how the model judged it
- why items were merged or split
- why something stayed local or became promotable
- what would trigger rollback or rejection

That is what makes the system cumulative instead of noisy.
