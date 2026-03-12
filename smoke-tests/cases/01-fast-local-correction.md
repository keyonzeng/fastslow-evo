# 01 — Fast route for repeated local correction

## Real-source anchor
- Nodeland blog: "Your Coding Agent Keeps Making the Same Mistakes. I Built a Fix"
- https://adventures.nodeland.dev/archive/your-coding-agent-keeps-making-the-same-mistakes

## Scenario
A user has already corrected the agent once for overly long replies with the conclusion buried too low.
In the next task, the agent again gives a technically correct answer but repeats the same delivery-style mistake.

## Evidence pack
- Evidence A: user says "Too long. Give the answer first."
- Evidence B: next day, similar task, user says "Still too much framing. I want the conclusion up front."

## What this case is testing
- whether the skill treats this as a local delivery mismatch
- whether it avoids over-promoting a style issue too early

## Expected route
- `fast`

## Expected good write-back
- identifies recurrence
- keeps the fix local
- proposes a tiny adjustment for concise-first delivery
- does not create a slow candidate

## Failure signals
- creates a durable candidate immediately
- describes this as a broad capability failure
- writes multiple new rules for a small style issue
