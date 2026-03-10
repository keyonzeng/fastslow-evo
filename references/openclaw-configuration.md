# OpenClaw Configuration

Use this note to wire FastSlow Evo into OpenClaw practice.

## What to configure right now

FastSlow Evo does not need a special daemon or plugin.

The practical setup is:
1. keep the skill installed and ready
2. keep evidence files in the workspace
3. use heartbeats to review adaptation patterns periodically
4. treat promotion as reviewable, not silent

## Minimal operating pattern

### A. Day-to-day
Use normal conversations and corrections to generate:
- incidents
- corrections
- wins
- tiny fixes

### B. Heartbeat review
Use heartbeat turns to inspect:
- repeated incidents
- repeated corrections
- repeated successful tiny fixes
- candidate promotions
- rollback candidates

### C. Promotion review
When heartbeat finds good candidates:
- generate promotion candidate
- review validation path
- decide whether to stay fast or promote slow

## What "configured" means in practice

The most important configuration is procedural, not technical:
- corrections must be captured
- tiny fixes must be visible
- heartbeat must occasionally review the pattern stream
- promotions must remain reviewable

## Validation rule

If heartbeat never produces plausible promotion candidates, the system is not yet evolving.
If it promotes everything, it is overfitting.
