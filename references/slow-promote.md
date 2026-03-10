# Slow Promote

Use the slow loop when a local fix has proven useful and may deserve durable promotion.

## When to use

Use Slow Promote when:
- a fast-loop fix recurs 3+ times
- the same pattern appears across tasks or channels
- the local fix has remained stable
- the change affects broader behavior, memory, workflow, or capability
- the blast radius is too large for ad hoc promotion

## Inputs

- repeated evidence
- prior tiny fix or local pattern
- validation path
- rollback path

## Output

A **durable promotion**, chosen from:
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- reusable skill or script

## Workflow

1. Gather recurrence evidence.
2. Check whether the pattern is stable across contexts.
3. Define explicit validation.
4. Define regression guard and rollback.
5. Promote to the lightest durable higher-order artifact.
6. Measure before/after recurrence and regressions.

## Rule

Slow promotion exists to prevent fast-loop overfitting from turning into bad policy.

## Success Criterion

A proven local fix becomes a reusable long-term improvement without increasing fragility, confusion, or safety risk.
