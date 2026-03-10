---
name: fastslow-evo
description: "A dual-loop self-evolution skill for AI agents. Use fast loops to adapt quickly from local errors, corrections, and repeated work, and use slow loops to validate and promote only durable improvements into higher-order capabilities. Use when building or refining self-evolving agents, capability systems, memory/reflection loops, or improvement workflows that must become both faster to improve and safer to scale. Especially relevant when the user wants rapid self-improvement without uncontrolled drift, and wants repeated local fixes to mature into validated long-term skills, specs, or workflows."
---

# FastSlow Evo

FastSlow Evo is a **dual-loop self-evolution system**.

Its job is simple:
- fix local repeated mistakes quickly
- promote only proven fixes slowly
- keep turning local experience into durable capability

## Core Model

```text
FAST LOOP: observe -> classify -> tiny fix -> reuse
SLOW LOOP: validate -> promote -> standardize -> measure
```

## Core Rule

Do not turn one event into a broad policy.
Do not leave proven recurring fixes trapped as local hacks.

## What the loops do

### Fast loop
Use when the problem is local, frequent, low-blast-radius, and easy to verify in the next task.

Typical outputs:
- checklist
- template
- memory rule
- tiny validation rule
- tiny script

### Slow loop
Use when a local fix has proven useful and may deserve durable promotion.

Typical outputs:
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- reusable skill or script

## Best default

If unsure, start with the fast loop.
Only promote slowly after recurrence, validation, and regression checks.

## Intelligent Routing

FastSlow Evo should infer the right loop by default.
User instruction can override, but the system should still reason about whether the requested loop is appropriate.

Read `references/router-intelligence.md` when the task is to decide automatically whether a signal should go to fast execution, slow promotion, observation, or noise.

## Heartbeat Monitoring

FastSlow Evo should use heartbeat-style monitoring to observe whether fast-loop fixes are maturing into slow-loop promotion candidates.

Read `references/heartbeat-monitor.md` when the task is to inspect recent incidents, corrections, wins, and tiny fixes over time.

## First files to read

- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/slow-promote.md`
- `references/fast-slow-router.md`

## Design Goals

1. Ground improvement in evidence.
2. Prefer the smallest durable fix.
3. Make validation explicit.
4. Promote only after proof.
5. Control regression.
6. Keep the system useful before making it elegant.

## The 5 Spec Types

### 1. Capability Spec

Define what the agent can reliably do, under what conditions, and what is out of scope.

Example:

- Can export SVG to PNG with Chinese text only if runtime CJK fonts are available and render check passes.

### 2. Behavior Spec

Define how the agent should behave in recurring situations.

Example:

- In a group chat, respond only when directly asked or when there is real additive value.

### 3. Validation Spec

Define how to verify that a capability or behavior works.

Example:

- Generate PNG from two Chinese SVG samples and verify rendered output visually or via a known-good rasterizer.

### 4. Evolution Spec

Define what signals justify proposing an upgrade, and what approval path is required.

Example:

- A single incident creates evidence only. Repeated recurrence creates a proposal candidate.

### 5. Materialization Spec

Define where an approved spec delta should land.

Example:

- Tool gotcha -> TOOLS.md
- workflow rule -> AGENTS.md
- reusable procedure -> skill
- deterministic repeated task -> script

## Core Workflows

### Fast Loop — Quick Adapt

When the issue is local, frequent, and low-blast-radius, use the fast loop.

Read `references/quick-adapt.md` when the goal is immediate improvement on the next similar task.

### Slow Loop — Slow Promote

When a local fix has proven useful and may deserve durable promotion, use the slow loop.

Read `references/slow-promote.md` when the goal is to turn repeated validated local improvements into higher-order capability.

## The 6-Phase Workflow

### Phase 1 — Observe

Capture only what matters:

- failures
- user corrections
- repeated friction
- missing capabilities
- validated successful patterns

Store raw evidence separately from specs.

Use the templates in `assets/`, especially the incident/correction/win record templates.

### Phase 2 — Classify the Gap

Every event must map to one primary gap type:

- capability_gap
- behavior_gap
- validation_gap
- retrieval_gap
- workflow_gap
- safety_gap
- tooling_gap
- scope_gap

If needed, read `references/gap-taxonomy.md`.

Do not propose changes before naming the gap.

### Phase 3 — Draft the Spec Delta

A spec delta is the smallest durable abstraction that would have prevented recurrence.

A good spec delta is:

- specific
- testable
- transferable
- low-blast-radius
- reversible

Draft deltas using the proposal template in `assets/evolution-proposal.template.md`.

### Phase 4 — Validate the Delta

Before materializing anything, answer:

- Is the delta supported by real evidence?
- Does it conflict with current specs?
- Is the success condition explicit?
- Is there a smaller materialization form?
- How do we detect regression?

If needed, read `references/validation-model.md`.

### Phase 5 — Materialize

Materialize only after validation.

Preferred order:

1. evidence log
2. curated memory note
3. checklist
4. template
5. script
6. skill update
7. code/config mutation

If a lighter form is enough, stop there.

If needed, read `references/materialization-strategy.md`.

### Phase 6 — Measure

Track whether the change actually helped.

Minimal scorecard:

- recurrence before/after
- acceptance rate of proposals
- regressions introduced
- user-correction frequency
- time saved on repeated tasks
- number of specs promoted vs reverted

## What to Keep from Prior Self-Improvement Patterns

Retain these proven ideas:

- **low-friction evidence capture** from logging-based systems
- **layered memory** from memory-centric systems
- **hindsight / reflection checkpoints** from retrospective systems
- **stable retention paths** from keep-style note systems
- **proposal + validation + rollback discipline** from evolver-style systems

But transform them through the spec model.

## What to Avoid

Reject these anti-patterns:

- vague self-critique with no artifact
- raw logs masquerading as durable knowledge
- single-incident overfitting
- blind self-modification
- infinite evolution loops in production
- hidden changes without review trail
- writing “best practices” with no validation
- broad changes when a smaller fix would work

## Anti-Fantasy Rules

AI-generated improvement plans often fail because they sound smart but do not cash out into operations. Use these rules to stay grounded:

1. **No abstraction without an example**
   - Every rule must cite at least one concrete triggering case.
2. **No capability claim without validation**
   - If success cannot be tested, the capability is not upgraded.
3. **No framework inflation**
   - Do not create new layers unless they remove repeated confusion.
4. **No “should” without landing zone**
   - Every recommendation must name its destination file or artifact.
5. **No upgrade without rollback**
   - Every non-trivial materialization must be reversible.
6. **No innovation theater**
   - Prefer one useful template over ten visionary paragraphs.

## Deliverables

When the user asks for an improvement plan or a new capability system, return these artifacts:

1. evidence summary
2. gap classification
3. spec deltas
4. validation plan
5. materialization plan
6. regression guard
7. concrete file changes or templates

## Default Directory Model

Use or create this structure when implementing the system:

```text
specs/
  capabilities/
  behaviors/
  validations/
  evolutions/
  materializations/
evidence/
  incidents/
  corrections/
  wins/
proposals/
scorecards/
```

## How to Decide Whether a Skill Is Needed

Create or edit a skill only when all are true:

- the need recurs across tasks or projects
- the procedure is teachable
- the behavior benefits from stable trigger text
- lighter materializations are insufficient

Otherwise keep the upgrade as memory, checklist, template, or script.

## References

Read only as needed:

- `references/spec-model.md`
- `references/gap-taxonomy.md`
- `references/evolution-protocol.md`
- `references/validation-model.md`
- `references/materialization-strategy.md`
- `references/real-pain-points.md`
- `references/case-design-principles.md`
- `references/starter-cases.md`
- `references/starter-packs.md`
- `references/first-run-workflow.md`
- `references/spec-review-checklist.md`
- `references/user-guide.md`
- `references/minimal-demo.md`
- `references/office-study-pain-points.md`
- `references/office-study-optimization-plan.md`
- `references/mainstream-starter-packs.md`
- `references/positioning-and-penetration.md`
- `references/openclaw-fit.md`
- `references/fast-slow-router.md`
- `references/roadmap.md`
- `references/quick-adapt.md`
- `references/slow-promote.md`
- `references/openclaw-user-penetration.md`
- `references/one-page-start.md`
- `references/release-notes.md`
- `references/router-intelligence.md`
- `references/heartbeat-monitor.md`

## Execution Standard

If you use this skill to design a system, produce something executable in the same turn:

- a spec tree
- one or more spec files
- one proposal
- one scorecard template
- one recommendation on materialization form
- or a script/template set

Never stop at philosophy if the user asked for implementation.

If the user is adopting the skill for the first time, prefer `references/one-page-start.md` first, then `references/first-run-workflow.md` and one relevant starter pack before expanding the full system.

If the question is about where FastSlow Evo fits, who it should target first, or how to balance broad positioning with focused adoption, read `references/positioning-and-penetration.md`, `references/openclaw-fit.md`, and `references/openclaw-user-penetration.md`.

If the question is whether an issue belongs in fast adaptation or slow promotion, read `references/fast-slow-router.md`.

If the user needs immediate next-task improvement, use `references/quick-adapt.md`.

If the user needs durable validated promotion, use `references/slow-promote.md`.

Before approving durable spec changes, use `references/spec-review-checklist.md`.
