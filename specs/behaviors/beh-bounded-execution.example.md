# Behavior Spec: beh-bounded-execution

## Context
Long-running or multi-step autonomous tasks using tools, retries, or sub-agents.

## Trigger
A tool fails, hangs, returns malformed output, or the agent retries similar steps repeatedly.

## Required Actions
- Track iteration count, elapsed time, and retry count
- Apply bounded retries per failure class
- Escalate to fallback or review when thresholds are crossed
- Record the stop reason in evidence or logs

## Forbidden Actions
- Retry indefinitely
- Spawn unbounded subordinate chains
- Treat repeated malformed tool requests as progress

## Escalation Rule
When retry ceiling, runtime budget, or delegation depth budget is exceeded, stop autonomous execution and propose the smallest next safe action.

## Examples
- Tool hangs three times -> stop and surface fallback
- Malformed tool JSON repeats -> stop, preserve evidence, request review
