# Starter Cases

These are not copied from any single source. They are synthesized, reusable starter cases built from recurring real-world pain patterns.

## Case 1 — Phantom Tool Success

### User pain
The agent says it fetched, sent, checked, or updated something, but the tool was never actually called or the record of the call is missing.

### Why users care
This destroys trust fast. It creates a fake sense of competence while silently skipping execution.

### Primary gap
`validation_gap`

### Secondary gaps
`retrieval_gap`, `workflow_gap`

### Design target
Make execution evidence first-class and require response faithfulness to execution evidence.

### Good materializations
- validation spec for tool execution proof
- checklist for “claim vs evidence” verification
- script or middleware that persists tool-call evidence

---

## Case 2 — Agent Amnesia vs Memory Bloat

### User pain
The agent either forgets everything useful or remembers too much irrelevant/noisy material and starts drifting.

### Why users care
Users have to repeat themselves, while the agent also gets less reliable over time.

### Primary gap
`capability_gap`

### Secondary gaps
`retrieval_gap`, `scope_gap`

### Design target
Define what belongs in working, episodic, semantic, and procedural memory, with expiry and retrieval rules.

### Good materializations
- capability spec for memory policy
- validation spec for retrieval relevance
- scorecard for precision/recall of recalled facts

---

## Case 3 — Runaway Loop / No Hard Stop

### User pain
The agent gets stuck retrying, reformatting tool calls, delegating recursively, or waiting forever on a hung step.

### Why users care
It burns time, money, and patience.

### Primary gap
`safety_gap`

### Secondary gaps
`workflow_gap`, `behavior_gap`

### Design target
Make budgets, stop criteria, retry ceilings, and fallback behavior explicit.

### Good materializations
- behavior spec for retries and stop conditions
- validation spec for bounded execution
- script or policy for budget enforcement

---

## Case 4 — Memory Poisoning / Long-Horizon Drift

### User pain
The agent behaves strangely over time because a malicious or low-quality memory entry keeps influencing future actions.

### Why users care
The system becomes persistently wrong and hard to debug.

### Primary gap
`safety_gap`

### Secondary gaps
`validation_gap`, `retrieval_gap`

### Design target
Treat memory as untrusted by default and require provenance, validation, and revocation paths.

### Good materializations
- evolution spec governing what can be written to durable memory
- validation spec for memory ingestion
- quarantine workflow for suspicious memory entries

---

## Case 5 — Correct Tool Output, Wrong Final Answer

### User pain
The agent gets valid tool output but produces a contradictory or fabricated summary.

### Why users care
This looks polished while being wrong, which is worse than an obvious failure.

### Primary gap
`validation_gap`

### Secondary gaps
`behavior_gap`

### Design target
Check final-answer faithfulness, not just tool invocation success.

### Good materializations
- validation spec for answer-to-evidence consistency
- checklist for contradiction detection
- scorecard for tool-faithful answer rate

---

## Case 6 — Goal Misread / Wrong Plan Order

### User pain
The agent works hard on the wrong objective or performs steps in a harmful order.

### Why users care
Time is wasted and external side effects can happen too early.

### Primary gap
`behavior_gap`

### Secondary gaps
`workflow_gap`, `scope_gap`

### Design target
Separate goal confirmation, planning, execution ordering, and completion criteria.

### Good materializations
- behavior spec for objective confirmation
- validation spec for completion criteria
- workflow template for multi-step execution

---

## Case 7 — Unsafe Generalization from One Incident

### User pain
The agent overreacts to one failure and turns a local workaround into a global rule.

### Why users care
The system becomes brittle and weirdly overfit.

### Primary gap
`evolution_gap` 

Note: map this to `workflow_gap` or `scope_gap` in the current taxonomy until a dedicated evolution-gap type is added.

### Design target
Require evidence thresholds and regression checks before durable promotion.

### Good materializations
- evolution spec for promotion thresholds
- regression checklist
- scorecard comparing before/after recurrence
