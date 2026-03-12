# 02 — Slow candidate for repeated delivery-surface mismatch

## Real-source anchor
- Langflow blog: "Top 3 Mistakes I Made While Building AI Agents"
- https://www.langflow.org/blog/top-three-mistakes-building-agents

## Scenario
Across several different tasks, the agent completes the technical work but repeatedly fails to deliver the final result in the user's working surface.
The user keeps having to ask for the answer to be returned in chat instead of being left in a local file path.

## Evidence pack
- Evidence A: research summary finished locally but not returned in chat
- Evidence B: file edited successfully but no user-facing summary provided
- Evidence C: analysis completed, but the user had to ask again for the actual result

## What this case is testing
- whether the skill can identify a cross-context workflow problem
- whether it prefers one durable candidate over multiple weak ones

## Expected route
- `slow candidate`

## Expected good write-back
- identifies a recurring delivery-discipline pattern
- proposes creating or updating one candidate
- states validation and rollback explicitly

## Failure signals
- treats each case as unrelated
- keeps applying only fast fixes forever
- creates several timestamp-based delivery candidates
