# FastSlow Candidate Protocol

This protocol defines what a promotion candidate is and how the OpenClaw host model should handle candidate convergence.

## Core Rule

A candidate is a model-reviewed convergence object.
It is not a raw log fragment.
It is not approved durable policy.
It is the current best attempt to represent one underlying pattern for review.

## What a Candidate Must Contain

### 1. Canonical Problem
A plain-language statement of the underlying pattern the candidate claims to represent.

### 2. Linked Evidence
The incidents, corrections, and wins that support the candidate.
Also keep track of excluded evidence when needed.

### 3. Dedup Decision
State one of:
- same-pattern
- related-but-distinct
- split-needed
- pending-review

### 4. Why This Is One Pattern
Explain why the linked evidence belongs together.
If the explanation is weak, the candidate is weak.

### 5. Promotion Logic
Explain:
- why local handling is no longer enough
- what durable artifact is proposed
- why it is the lightest durable next step

### 6. Validation and Rollback
State:
- how the proposed promotion would be validated
- how regression would be noticed
- how rollback would work

## Convergence Rules For OpenClaw

Before creating or updating a candidate, the host model should decide whether the new evidence should:
- merge into an existing candidate
- stay separate as a related-but-distinct pattern
- split an over-merged candidate
- supersede an outdated candidate
- create one new candidate
- create nothing

## Anti-Patterns

Do not:
- create one candidate per evidence file
- merge records only because the wording looks similar
- keep a candidate open when its merge logic is weak
- promote a candidate just because recurrence sounds high

## Candidate Quality Test

A good candidate can answer clearly:
1. what happened repeatedly
2. why these records belong together
3. why local handling is no longer enough
4. what durable step is being proposed
5. how we would know the promotion worked or failed
