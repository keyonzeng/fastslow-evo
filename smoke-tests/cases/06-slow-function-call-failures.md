# 06 — Slow candidate for mistimed or hallucinated function calls

## Real-source anchor
- Reddit / LLMDevs discussion on hallucinated and mistimed function calls in production agents

## Scenario
Across multiple workflow runs, the agent sometimes skips a required function call and sometimes hallucinates a call that should not happen.
The result is a broken process rather than a one-off wording problem.

## Evidence pack
- Evidence A: required function never called
- Evidence B: invalid function call hallucinated
- Evidence C: wrong call order breaks the workflow

## What this case is testing
- whether the skill recognizes a workflow-level problem
- whether it demands validation rather than only advice

## Expected route
- `slow candidate`

## Expected good write-back
- describes the pattern as durable enough for candidate review
- proposes validation conditions
- does not reduce the issue to "be more careful"

## Failure signals
- gives only a local reminder
- fails to mention validation or rollback
- mistakes the issue for a style correction
