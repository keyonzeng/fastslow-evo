# 03B — Slow candidate after repeated tool-overload failures

## Real-source anchor
- Langflow blog: "Top 3 Mistakes I Made While Building AI Agents"
- https://www.langflow.org/blog/top-three-mistakes-building-agents

## Scenario
After the first tool-overload incident, two more similar failures appear in different tasks.
The exact tools differ, but the underlying pattern is the same: too many tools, weak step control, skipped validation, broken flow.

## Evidence pack
- Evidence A: wrong tool selected, missing validation
- Evidence B: step skipped after tool handoff
- Evidence C: multiple tools available, agent chose the wrong branch and returned incomplete work

## What this case is testing
- whether the skill can detect convergence across different surface forms

## Expected route
- `slow candidate`

## Expected good write-back
- explains why the underlying pattern is now stable enough
- proposes one candidate around tool-selection / workflow discipline
- avoids splitting by superficial tool names

## Failure signals
- still stays in observe despite clear recurrence
- merges unrelated issues into one oversized candidate
- creates separate candidates for each tool name
