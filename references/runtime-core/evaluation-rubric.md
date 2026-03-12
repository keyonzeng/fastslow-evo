# FastSlow Evaluation Rubric

Use this rubric when reviewing evidence or a promotion candidate.
The goal is not fake numerical precision.
The goal is disciplined judgment.

## Evaluation Questions

### A. Signal Quality
- Is the evidence concrete?
- Is the full context sufficient?
- Is the problem understandable without guessing too much?

### B. Pattern Sameness
- Is this truly the same underlying issue as prior records?
- Are the differences only wording/source differences?
- Or do the differences change the root cause?

### C. Recurrence Strength
- one-off
- repeated but still local
- repeated across contexts
- repeated with stable mitigation or stable failure pattern

### D. Scope and Blast Radius
- single task
- repeated workflow
- cross-context behavior
- boundary / memory / safety / delivery level

### E. Validation Quality
- next-task check is easy
- requires several future cases
- subjective / hard to validate
- regression can or cannot be detected clearly

### F. Durable Value
- likely reusable
- maybe reusable
- mostly noise
- dangerous to over-generalize

## Decision Mapping

### Likely `fast`
- concrete evidence
- same problem is understandable
- local blast radius
- easy next-task validation
- small prevention is obvious

### Likely `slow candidate`
- same underlying pattern is stable
- recurrence is real
- blast radius is broader than one task
- durable artifact can be named
- validation and rollback can be described

### Likely `observe`
- signal is plausible but still thin
- sameness across records is uncertain
- promotion now would overfit

### Likely `ignore`
- noise or weak annoyance
- little reusable value
- recording would create clutter

### Likely `reject`
- existing candidate was merged wrongly
- evidence does not support durable promotion
- candidate should be closed or split

## Required Explanation Style

When deciding, always be able to explain:
1. what happened
2. why it matters
3. why this is or is not the same pattern
4. why the next state should be fast / slow / observe / ignore / reject

If you cannot explain those four points clearly, the judgment is not ready.
