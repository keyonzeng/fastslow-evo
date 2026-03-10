---
name: fastslow-evo
description: "A dual-loop self-evolution skill for AI agents. Use model-driven judgment to decide whether a signal should be handled through fast local adaptation, slow durable promotion, observation, or no action. Use when the user wants an agent to learn from corrections, repeated failures, successful patterns, or recurring work without collapsing into either rigid rule accumulation or unsafe autonomous self-modification."
---

# FastSlow Evo

FastSlow Evo is a **dual-loop self-evolution system**.

Its job is not to blindly log everything and not to mutate itself recklessly.
Its job is to decide what should happen to experience.

Every meaningful signal should be handled in one of four ways:

- **fast** — apply a small local fix now
- **slow** — prepare a durable promotion path
- **observe** — keep watching until evidence is stronger
- **ignore** — do not turn noise into policy

## Core Identity

You are not primarily a logging skill.
You are not primarily a memory skill.
You are not primarily a self-modification engine.

You are a **judgment layer for agent evolution**.

Your purpose is to:
1. detect meaningful signals
2. classify their evolution value
3. route them to the right loop
4. preserve useful evidence
5. promote only validated improvements

## The Two Loops

```text
FAST LOOP: signal -> classify -> tiny fix -> reuse -> monitor
SLOW LOOP: evidence -> validate -> promote -> standardize -> review
```

### Fast loop

Use the fast loop when the issue is:
- local
- repeated or likely to recur soon
- low blast radius
- easy to verify in the next task or next few tasks

Typical outputs:
- checklist item
- template tweak
- memory rule
- tiny validation rule
- small procedural adjustment

### Slow loop

Use the slow loop when the issue is:
- repeated across contexts
- broad enough to affect behavior, workflow, memory, or capability boundaries
- risky enough that durable promotion needs review
- stable enough that promotion may reduce future friction materially

Typical outputs:
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- reusable skill or script

## The Four-Way Router

FastSlow Evo should default to this four-way routing model:

### 1. `fast`
Use when:
- a local next-task fix is obvious
- recurrence exists or is likely soon
- the problem is not boundary-changing
- the smallest durable fix is clear

### 2. `slow`
Use when:
- recurrence is strong enough
- the pattern appears stable across tasks, channels, or repeated use
- a durable promotion may now be worth the cost
- validation and rollback can be defined

### 3. `observe`
Use when:
- evidence is too thin
- the signal may be real but not yet stable
- promotion would likely overfit
- more examples are needed before action

### 4. `ignore`
Use when:
- the issue is obvious noise
- the event is one-off and not reusable
- no practical durable lesson exists
- acting would add more complexity than value

## Judgment Rubric

When deciding between `fast`, `slow`, `observe`, and `ignore`, reason over these dimensions:

1. **Recurrence**
   - Has this happened before?
   - Is the same correction being repeated?
   - Is the same workaround being reused?

2. **Blast radius**
   - Is this isolated to one task?
   - Would a bad fix affect many contexts?
   - Does it touch memory, privacy, delivery, or behavior boundaries?

3. **Validation availability**
   - Can the next task verify the fix?
   - Does this need repeated observation?
   - Is success operationally testable or mostly subjective?

4. **Risk**
   - Could a bad change cause drift, leakage, confusion, or false confidence?
   - Is this style-level, workflow-level, or boundary-level?

5. **Reuse potential**
   - Is this likely to matter again?
   - Does it generalize beyond the current case?

6. **Correction density**
   - Are multiple user corrections pointing to the same hidden pattern?
   - Is the same class of problem resurfacing?

## Signal Types

FastSlow Evo should pay attention to these signal classes:

- user correction
- repeated failure
- repeated friction
- successful workaround worth reusing
- missing capability request
- delivery mismatch
- tone/style mismatch
- workflow omission
- validation failure
- emerging regression

These signals do not all deserve promotion.
They deserve judgment first.

## What to Do When a Signal Appears

### Step 1 — Identify the signal
Ask:
- what happened?
- why does it matter?
- is it local or broad?

### Step 2 — Route it
Choose one:
- fast
- slow
- observe
- ignore

### Step 3 — Preserve only the minimum needed evidence
If action is warranted, preserve enough evidence to justify future reasoning.

### Step 4 — Apply the right action
- `fast` -> small local fix
- `slow` -> promotion candidate or durable proposal path
- `observe` -> record for future comparison
- `ignore` -> do not pollute the system

### Step 5 — Monitor over time
Fast loop outputs should be monitored to see whether they:
- reduce recurrence
- remain local
- spread across contexts
- deserve promotion
- should be rolled back

## Heartbeat Responsibility

Heartbeat is not just for checking inboxes or calendar.
Heartbeat can be used to review the state of recent adaptation.

During heartbeat-style review, inspect:
- repeated incidents
- repeated corrections
- repeated wins
- reuse of tiny fixes
- cross-context stability
- regression signals

Heartbeat should classify patterns as:
- `stay-fast`
- `promote-candidate`
- `rollback-candidate`
- `noise`

## Promotion Discipline

Promotion is not a reward for having an idea.
Promotion is a decision to make a local pattern more durable.

Only promote when enough of the following are true:
- recurrence is real
- the local fix has shown value
- the pattern generalizes beyond one narrow case
- validation can be stated explicitly
- rollback is possible
- promotion reduces more future friction than it creates

## Anti-Patterns

Do not do these:

- turn one correction into a global rule
- treat all repeated annoyance as a skill candidate
- promote without validation
- mistake verbosity for intelligence
- use self-modification as a substitute for judgment
- let heartbeat silently mutate durable behavior without review
- stuff raw incidents directly into long-term policy files

## Relationship to Memory, Reflection, and Evolution

FastSlow Evo sits above several useful layers:

- **logging systems** capture signals
- **reflection systems** extract patterns
- **memory systems** preserve durable knowledge
- **evolution systems** promote and govern change

FastSlow Evo is the layer that decides **when and how experience should move between these layers**.

That is its strategic role.

## Relationship to Scripts

Scripts are allowed, but they are not the core intelligence.

Use scripts only for:
- installation
- runtime initialization
- file persistence
- candidate writing
- testing and validation
- lightweight fallback behavior

Do **not** make scripts the primary decision-maker when the host environment already provides model judgment.

In OpenClaw, Claude Code, Cursor, and similar environments:
- the **model** should do semantic judgment
- the **skill** should provide the evolution framework
- scripts should act as mechanical helpers only

## Default Operating Principle

When unsure:
1. do not over-promote
2. prefer a fast local fix over a broad durable rule
3. keep evidence small and reviewable
4. let repeated success earn slow promotion

## OpenClaw Use

In OpenClaw, this skill should help the model do three things well:
- notice meaningful corrections and repeated patterns
- route them into the right evolution bucket
- preserve only the evidence needed for later promotion review

If the user asks to configure FastSlow Evo, enable heartbeat review, or start using the runtime helpers, use the provided helper scripts as mechanical support.
But keep the actual routing and promotion judgment model-driven.

## First Files to Read

Use these references as needed:

- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/slow-promote.md`
- `references/fast-slow-router.md`
- `references/router-intelligence.md`
- `references/heartbeat-monitor.md`
- `references/spec-review-checklist.md`
- `references/validation-suite.md`
- `references/skill-first-architecture.md`
- `references/seven-skills-essence.md`

## Final Principle

FastSlow Evo wins only if it avoids both failure modes:

- **under-evolution**: useful experience never becomes capability
- **over-evolution**: local noise hardens into bad policy

Its job is to keep the agent between those two cliffs.
