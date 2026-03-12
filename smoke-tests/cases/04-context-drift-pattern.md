# 04 — Context-drift pattern across long tasks

## Real-source anchor
- Galileo: "7 Types of AI Agent Failure and How to Fix Them"
- https://galileo.ai/blog/prevent-ai-agent-failure

## Scenario
In several long-running tasks, the agent repeatedly forgets constraints that were already established earlier in the same task.
The surface mistakes differ, but the underlying issue appears to be context drift.

## Evidence pack
- Evidence A: forgets delivery format halfway through a long workflow
- Evidence B: reintroduces a previously corrected assumption late in the task
- Evidence C: drops a key constraint after multiple intermediate tool steps

## What this case is testing
- whether the skill judges underlying sameness semantically
- whether it can distinguish real recurrence from superficial variation

## Expected route
- `observe` or `slow candidate`, depending on judgment quality

## Expected good write-back
- explicitly reasons about whether this is truly one pattern
- avoids using file count as the main proof
- gives a disciplined next step

## Failure signals
- auto-promotes only because there are three files
- treats all forgetting as one global candidate
- ignores the likely shared root cause
