# Correction Record: <correction-id>

## Summary

## Source
- user | review | runtime

## Context

## Full Context
- task:
- user-intent:
- surrounding-dialogue:
- prior-agent-behavior:
- correction-signal:

## Raw Signal
- paste the exact correction or closest verbatim wording here

## Notes
- gap:
- recurrence_hint:
- created_at:

## Model Review Instructions
This file is raw evidence, not a stable rule by itself.
Use `references/runtime-branches/evidence-protocol.md`, `references/runtime-core/review-protocol.md`, and `references/runtime-core/evaluation-rubric.md` before judging it.
Write conclusions using `references/runtime-core/review-output-format.md`.
The OpenClaw host model should use the full context to decide:
- what the user actually corrected
- whether this is the same underlying issue as prior corrections/incidents
- whether it belongs in an existing candidate or should remain local/observed
- whether the correct state is fast / slow-candidate / observe / ignore / reject
