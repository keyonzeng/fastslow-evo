# FastSlow Review Protocol

This protocol defines how the OpenClaw host model should evaluate FastSlow evidence and candidates.

FastSlow should not judge quality by file existence, keyword overlap, or mechanical recurrence counts alone.
It should judge whether a signal is worth keeping, merging, promoting, deferring, or rejecting.

## Core Evaluation Principle

Evaluate in this order:

1. What actually happened?
2. Is this evidence meaningful or mostly noise?
3. Is this the same underlying pattern as prior evidence?
4. If yes, should it merge into an existing candidate?
5. If not, should it remain local, observed, ignored, or become a new candidate?
6. If it becomes a candidate, what is the lightest durable next step?

## Hard Rules

- Do not deduplicate by keyword overlap alone.
- Do not promote because multiple files exist.
- Do not treat one correction as a durable global rule by default.
- Do not collapse adjacent but distinct failures into one candidate unless the root cause is actually shared.
- Do not confuse a repeated symptom with a stable promotable fix.

## Evaluation Dimensions

### 1. Signal Strength
Ask:
- Is this a concrete correction, incident, or win?
- Does the record preserve enough context to understand the real problem?
- Would losing this record likely lose something reusable?

Default outputs:
- weak -> observe or ignore
- concrete -> continue review

### 2. Underlying Pattern Identity
Ask:
- Is the root problem the same as earlier records?
- Are wording differences superficial, or do they indicate a different failure mode?
- Are the task goal, user intent, and failure location materially the same?

Possible decisions:
- same-pattern
- related-but-distinct
- split-needed
- unclear-keep-observing

### 3. Recurrence
Ask:
- Has this happened before?
- Is the same correction being repeated?
- Is the same workaround reused successfully?

Important:
Recurrence is supportive evidence, not sufficient evidence by itself.

### 4. Blast Radius
Ask:
- Is this local to one task?
- Does it affect repeated workflow behavior?
- Does it touch memory, privacy, boundary handling, or delivery quality across contexts?

### 5. Validation Availability
Ask:
- Can the next similar task verify the fix?
- Is success measurable, or only vaguely preferable?
- Can regression be detected clearly?

### 6. Promotion Discipline
Ask:
- Is local handling still enough?
- Is there a candidate tiny fix already?
- Would durable promotion reduce future friction more than it adds complexity?
- Is rollback practical?

## Fast / Slow / Observe / Ignore / Reject

### Fast
Choose fast when:
- the issue is concrete
- a small next-task fix is obvious
- blast radius is low
- validation is easy soon

### Slow Candidate
Choose slow candidate when:
- recurrence is real
- the same underlying pattern appears stable
- local treatment is no longer enough
- a validation path can be stated
- a light durable artifact can be named

### Observe
Choose observe when:
- evidence is still thin
- sameness is unclear
- the signal may be real but not yet stable
- promoting now would likely overfit

### Ignore
Choose ignore when:
- the event is noise
- no durable lesson exists
- a stored record would add clutter without likely reuse

### Reject
Choose reject when:
- a candidate exists but should not continue
- the merge was wrong
- promotion logic was unsupported
- the evidence does not justify durable treatment

## Candidate Convergence Rule

A candidate is a convergence object, not a log fragment.
Before creating a new candidate, review existing candidates and decide whether the new evidence should:
- merge into one candidate
- split an over-merged candidate
- supersede an outdated candidate
- create one new candidate
- create nothing

## Why This Protocol Exists

FastSlow is meant to be the judgment layer between logging, reflection, memory, and promotion.
If it evaluates badly, it becomes either:
- noisy pseudo-learning
- or missed durable improvement

A good review should be explainable in plain language:
- what happened
- why it matters
- why this is or is not the same pattern
- what should happen next
