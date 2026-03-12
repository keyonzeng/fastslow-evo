---
name: fastslow-evo
description: "Judge whether agent experience should remain a local adaptation or become a reviewed durable improvement through a fast/slow dual-loop evolution model. Use when the user wants the agent to remember a correction, review repeated mistakes, evaluate recurring incidents, decide whether something should stay local or become durable, or run heartbeat-style evolution review without turning every event into a rule or allowing unsafe autonomous self-modification."
---

# FastSlow Evo

FastSlow Evo is a fast/slow dual-loop self-evolution skill for AI agents.

Its job is to judge whether a signal should:
- stay as a local adaptation in the fast loop
- become a reviewed durable improvement in the slow loop
- remain under observation
- be ignored as noise
- be rejected or rolled back

In OpenClaw, FastSlow Evo is judgment-first and markdown-first:
- the host model performs semantic judgment
- markdown protocols provide structure and reviewability
- scripts are optional helpers, not the decision-maker

## Core model

Use two loops:
- **Fast loop**: local fix, short feedback cycle, near-term reuse
- **Slow loop**: durable promotion, explicit validation, reviewed standardization

Default routing states:
- `fast`
- `slow candidate`
- `observe`
- `ignore`
- `reject`

## 30-second operating path

If the task is:
- **heartbeat review** -> read `references/runtime-core/protocol-reading-order.md`, `references/runtime-branches/heartbeat-protocol.md`, `references/runtime-core/review-protocol.md`, `references/runtime-core/evaluation-rubric.md`, relevant evidence/candidates, then `references/runtime-core/review-output-format.md`
- **new evidence review** -> read `references/runtime-core/protocol-reading-order.md`, `references/runtime-branches/evidence-protocol.md`, `references/runtime-core/review-protocol.md`, `references/runtime-core/evaluation-rubric.md`, relevant evidence, existing candidates only if sameness is in question, then `references/runtime-core/review-output-format.md`
- **candidate review** -> read `references/runtime-core/protocol-reading-order.md`, `references/runtime-branches/candidate-protocol.md`, `references/runtime-core/review-protocol.md`, `references/runtime-core/evaluation-rubric.md`, `references/runtime-branches/candidate-review-checklist.md`, linked evidence/candidate files, then `references/runtime-core/review-output-format.md`

Then:
1. read only the required protocol files
2. inspect the smallest relevant evidence/candidate set
3. choose exactly one primary routing outcome
4. write back using `references/runtime-core/review-output-format.md`
5. prefer updating one good candidate over creating many weak ones

If `references/runtime-core/minimal-usable-workflow.md` is enough, use it and stop expanding.

## Standard workflow

1. Preserve evidence before policy.
2. Judge the signal using recurrence, blast radius, validation availability, risk, reuse potential, and correction density.
3. Choose exactly one primary route.
4. Apply the smallest justified action.
5. Revisit only when new evidence or recurrence justifies it.

## Routing guidance

Use:
- `fast` for local, low-risk, near-term verifiable fixes
- `slow candidate` for stable cross-context patterns with explicit validation and rollback
- `observe` for thin or unstable evidence
- `ignore` for noise or one-off events with no reusable lesson
- `reject` for weak candidates, wrong merges, or misleading patterns

## Heartbeat stance

Heartbeat review is a reviewer path, not an autonomous mutation path.

During heartbeat review:
1. inspect recent evidence, repeated corrections, repeated incidents, repeated wins, and tiny fixes
2. review current candidates before creating new ones
3. update an existing candidate when possible
4. nominate only a small number of good candidates
5. stay quiet when there is no meaningful evolution signal

Do not let heartbeat silently harden weak local noise into durable policy.

## Output discipline

The output should explain:
- what happened
- why it matters
- whether this is the same underlying pattern as prior evidence
- why the next action is `fast`, `slow candidate`, `observe`, `ignore`, or `reject`

Always write back the smallest justified result.

## Repository boundary

Do not treat repository or distribution files as the runtime path by default.
Prefer `SKILL.md` plus the relevant protocol files under `references/`.

Runtime evidence, candidates, and review artifacts belong under workspace-level `fastslow/`, not inside the skill directory.

## Anti-patterns

Do not:
- turn one correction into a global rule
- promote without validation
- treat file count as recurrence proof
- confuse repeated annoyance with a worthy slow candidate
- create many timestamp-based variants of the same candidate
- use scripts or external helpers as the semantic judge
- let heartbeat silently mutate durable behavior without review
- stuff raw incidents directly into long-term policy files

## Reference map

Read the smallest set that fits the task.

### Default runtime references
- `references/runtime-core/protocol-reading-order.md`
- `references/runtime-core/minimal-usable-workflow.md`
- `references/runtime-core/review-protocol.md`
- `references/runtime-core/evaluation-rubric.md`
- `references/runtime-core/review-output-format.md`

### Task-specific references
- `references/runtime-branches/evidence-protocol.md`
- `references/runtime-branches/candidate-protocol.md`
- `references/runtime-branches/heartbeat-protocol.md`
- `references/runtime-branches/candidate-review-checklist.md`

### Optional runtime references
Read only when the current task explicitly needs them:
- `references/runtime-optional/openclaw-judgment-first.md`
- `references/runtime-optional/quick-adapt.md`
- `references/runtime-optional/slow-promote.md`
- `references/runtime-optional/heartbeat-monitor.md`
- `references/runtime-optional/validation-suite.md`
- `references/examples/example-fast.md`
- `references/examples/example-slow-candidate.md`
- `references/examples/example-reject.md`

### Skill-maintenance references
Do not read these on the default runtime path:
- `references/maintenance/one-page-start.md`
- `references/maintenance/fast-slow-router.md`
- `references/maintenance/router-intelligence.md`
- `references/maintenance/spec-review-checklist.md`
- `references/maintenance/skill-first-architecture.md`
- `references/maintenance/seven-skills-essence.md`
- positioning, roadmap, release notes, repo navigation, distribution, and product-strategy files

## Final principle

FastSlow Evo should keep the agent between two failure modes:
- **under-evolution**: useful experience never becomes capability
- **over-evolution**: local noise hardens into bad policy

Its job is to keep fast feedback useful and slow promotion disciplined.
