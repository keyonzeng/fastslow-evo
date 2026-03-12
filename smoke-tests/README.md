# FastSlow Evo Smoke Tests

This directory contains a practical smoke test suite for `fastslow-evo`.

The suite is designed using Skill Creator principles:
- use real-world failure patterns rather than toy prompts
- test the skill as a runtime entry, not just as a document
- verify routing quality across `fast`, `slow candidate`, `observe`, `ignore`, and `reject`
- verify that the skill resists over-promotion, weak sameness, and candidate spam

## What this suite tests

This suite checks whether a fresh agent can:
1. enter the correct protocol path quickly
2. judge pattern sameness semantically
3. choose the correct primary route
4. produce a small, clear, reviewable write-back
5. avoid premature durable promotion

## Structure

- `cases/01-fast-local-correction.md`
- `cases/02-slow-delivery-discipline.md`
- `cases/03a-observe-tool-overload.md`
- `cases/03b-slow-tool-overload-convergence.md`
- `cases/04-context-drift-pattern.md`
- `cases/05-boundary-memory-write.md`
- `cases/06-slow-function-call-failures.md`
- `cases/07-reject-weak-candidate.md`
- `cases/08-heartbeat-candidate-spam.md`
- `cases/09-structure-not-prompt.md`
- `cases/10-validation-gate-needed.md`
- `score-rubric.md`

## How to run

For each case:
1. Give the case file to a fresh agent together with `SKILL.md`.
2. Do not preload maintenance references.
3. Let the agent decide which runtime references to read.
4. Ask for:
   - route
   - rationale
   - whether this is the same pattern as prior evidence
   - smallest justified next action
5. Score the result using `score-rubric.md`.

## Minimum pass condition

A strong run should:
- select the expected route or a justified adjacent route
- avoid obvious over-promotion
- avoid weak candidate creation
- explain the decision in plain language

## Notes

These tests are smoke tests, not exhaustive evals.
They are designed to catch obvious routing, judgment, and discipline failures early.
