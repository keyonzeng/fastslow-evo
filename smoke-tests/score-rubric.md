# FastSlow Evo Smoke Test Scoring Rubric

Score each case out of 10.

## 1. Entry-path selection (2 points)
- 2: chooses the correct runtime path quickly
- 1: reaches the right path with unnecessary reading
- 0: chooses the wrong branch or wanders into maintenance material

## 2. Pattern judgment (3 points)
- 3: identifies the underlying pattern correctly
- 2: mostly correct but somewhat surface-level
- 1: weak sameness judgment
- 0: confuses unrelated signals or relies on keyword overlap

## 3. Route correctness (3 points)
- 3: chooses the expected route or a tightly justified adjacent route
- 2: partially defensible but not ideal
- 1: weak or unstable routing
- 0: clearly wrong route

## 4. Write-back quality (2 points)
- 2: clear, small, reviewable output with rationale and next action
- 1: understandable but vague, bloated, or weakly justified
- 0: unclear or non-actionable

## Common failure signals
- over-promotes one correction into a durable rule
- refuses to reject a weak candidate
- creates multiple timestamp-style candidates unnecessarily
- treats file count as recurrence proof
- ignores explicit boundary risk
- uses heartbeat as a mutation engine instead of a review path

## Interpretation
- 9-10: strong pass
- 7-8: acceptable but needs review
- 5-6: weak pass / unstable behavior
- below 5: fail
