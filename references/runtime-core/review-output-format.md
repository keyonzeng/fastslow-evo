# FastSlow Review Output Format

Use this format when the OpenClaw host model reviews evidence or candidates.

The goal is to make judgment explicit, comparable, and auditable.
Do not answer with vague approval language.
State the decision and its reasoning directly.

## Required Output Sections

### 1. What Happened
State the concrete issue in plain language.
Avoid abstraction before grounding.

### 2. Why It Matters
Explain the practical consequence:
- quality
- trust
- workflow reliability
- memory / boundary handling
- validation failure
- repeated friction

### 3. Pattern Judgment
State one:
- same-pattern
- related-but-distinct
- split-needed
- unclear

Explain why.
Focus on root cause, task goal, user intent, and failure location.
Do not rely on keyword overlap alone.

### 4. Convergence Action
State one:
- merge-into-existing-candidate
- keep-separate
- split-candidate
- supersede-candidate
- create-new-candidate
- no-action

Explain why this is the lightest justified convergence move.

### 5. State Decision
State one:
- fast
- slow-candidate
- observe
- ignore
- reject

Explain why this state fits better than the nearest alternative.

### 6. Proposed Next Step
State the smallest justified next step, such as:
- checklist tweak
- template refinement
- memory rule
- validation rule
- candidate update
- candidate rejection
- no write

### 7. Validation / Rollback
State:
- how to validate the next move
- what would count as regression
- what would cause rollback, split, or rejection later

## Compact Template

```md
## Review Result
- What happened:
- Why it matters:
- Pattern judgment:
- Pattern rationale:
- Convergence action:
- Convergence rationale:
- State decision:
- State rationale:
- Proposed next step:
- Validation path:
- Regression / rollback trigger:
```

## Final Rule

A review is not complete unless another reader can understand:
- what was judged
- why it was judged that way
- what should happen next
- what would prove the judgment wrong
