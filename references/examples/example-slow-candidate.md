# Example: Slow candidate for a stable recurring pattern

## Situation

Across multiple tasks, the agent repeatedly delivers work in the wrong final form:
- the technical work is often correct
- the result is not returned in the user's working surface
- the user repeatedly has to ask for direct delivery instead of local-file-only completion

The issue has appeared across different task types, not just one narrow case.

## What happened

This is no longer a one-off delivery mistake.
It is a recurring workflow pattern that affects usability and completion quality.

## Why it matters

The blast radius is broader than one task:
- it affects many task categories
- it creates repeated user friction
- the lesson is likely reusable across future work

## Sameness judgment

Treat this as the same underlying pattern when the repeated issue is:
- work completed technically
- delivery path chosen poorly
- user must ask again to receive the result where they actually work

Do not merge unrelated issues such as tone problems or tool-selection mistakes into this candidate.

## Route

`slow candidate`

## Smallest justified action

- create or update one candidate about delivery-surface discipline
- define explicit validation: future tasks should default to current-chat delivery when safe
- define rollback conditions: reject if the rule overfires or causes inappropriate channel behavior

## Why not fast

- the pattern has already crossed multiple tasks
- recurrence is strong enough to justify reviewable durable promotion
- a single local fix is no longer enough

## Example write-back

- outcome: `slow candidate`
- rationale: repeated cross-context delivery mismatch with clear reuse potential
- action: update one delivery-discipline candidate with validation and rollback criteria
