# Promotion Candidate: <candidate-id>

## Purpose
This markdown is a model-reviewed convergence object.
It should represent one underlying pattern only after the OpenClaw host model has inspected the linked evidence files.
Do not create or update this file from keyword overlap alone.
Do not create one candidate per evidence file.

## Candidate Identity
- Status: open | reviewing | observing | approved | rejected | superseded | split
- Canonical-Problem:
- Pattern-Signature:
- Dedup-Decision: same-pattern | related-but-distinct | split-needed | pending-review
- Why-This-Is-One-Pattern:

## Linked Evidence
- Incidents:
- Corrections:
- Wins:
- Excluded Evidence:

## Review Result
- What happened:
- Why it matters:
- Pattern judgment: same-pattern | related-but-distinct | split-needed | unclear
- Pattern rationale:
- Convergence action: merge-into-existing-candidate | keep-separate | split-candidate | supersede-candidate | create-new-candidate | no-action
- Convergence rationale:
- State decision: fast | slow-candidate | observe | ignore | reject
- State rationale:
- Proposed next step:
- Validation path:
- Regression / rollback trigger:

## Why this is a candidate
- Recurrence:
- Stability across contexts:
- Reuse evidence:
- Why local treatment may now be insufficient:

## Proposed Promotion
- Target loop: slow
- Proposed artifact: capability-spec | behavior-spec | validation-spec | workflow-rule | skill | script
- Why this is the lightest durable promotion:

## Review Instructions For OpenClaw Model
Review the linked markdown evidence files using their full context.
Use `references/runtime-branches/candidate-protocol.md`, `references/runtime-core/review-protocol.md`, `references/runtime-core/evaluation-rubric.md`, and `references/runtime-branches/candidate-review-checklist.md` as the evaluation lens.
Write conclusions using `references/runtime-core/review-output-format.md`.
Decide:
- whether the linked records are truly the same underlying problem
- whether any record should be removed from this candidate
- whether this candidate should merge into another one or be split apart
- whether this candidate deserves stay-fast / observe / promote / rollback / reject
- how you would explain the decision in plain language: what happened, why it matters, why this is or is not one pattern, and what should happen next
