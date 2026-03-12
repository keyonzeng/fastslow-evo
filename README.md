# FastSlow Evo

**FastSlow Evo is a dual-loop self-evolution system for AI agents.**

It helps an agent improve through two iterative loops:

- **Fast loop**: rapid local adaptation for small, repeated, low-risk mistakes
- **Slow loop**: cautious long-term promotion for patterns that have proven stable and worth keeping

FastSlow Evo is not a logging system, not a Python rule engine, and not a black-box self-modification tool.

Its purpose is to help an agent decide:

- what should be fixed quickly
- what should be promoted slowly
- what should stay under observation
- what should be ignored
- what should be explicitly rejected

In OpenClaw, FastSlow Evo works by combining:

- **real evidence** from incidents, corrections, and repeated wins
- **host-model semantic judgment**
- **markdown protocols** for review discipline, convergence, validation, and rollback

The result is a self-evolution workflow that avoids both failure modes:

- **under-evolution**: useful experience never becomes capability
- **over-evolution**: local noise hardens into bad long-term policy

### Core idea

FastSlow Evo does not treat every problem equally.

Some issues should stay local:
- a tone correction
- a missed detail in one summary
- a small validation miss

Some issues deserve durable review:
- repeated omissions across similar tasks
- stable failure patterns across contexts
- workflow-level gaps that local fixes no longer contain

That is why FastSlow Evo uses two loops.

### In one sentence

**FastSlow Evo is a judgment-driven dual-loop system that routes experience into fast local adaptation or slow durable promotion, so an agent can evolve without either forgetting useful lessons or overfitting to noise.**

---

## What is included

- `SKILL.md` — operating instructions for OpenClaw
- `references/` — protocols, rubrics, reading order, examples, and usable workflow
- `assets/` — markdown templates
- `specs/` — example durable artifacts

Python helpers have been removed from the default design.
FastSlow is now protocol-first and model-driven.

---

## Default usable workflow

Read:
- `references/runtime-core/minimal-usable-workflow.md`

That file is the shortest path to a usable FastSlow workflow.

If you need the full protocol stack, read:
- `references/runtime-optional/openclaw-judgment-first.md`
- `references/runtime-core/protocol-reading-order.md`
- `references/runtime-branches/evidence-protocol.md`
- `references/runtime-core/review-protocol.md`
- `references/runtime-core/evaluation-rubric.md`
- `references/runtime-core/review-output-format.md`
- `references/runtime-branches/candidate-protocol.md`
- `references/runtime-branches/heartbeat-protocol.md`

---

## Quick start in OpenClaw

### When a new correction or incident appears
1. Write one evidence markdown file from the template.
2. Preserve full context and raw signal.
3. Let OpenClaw review it using the protocol files.
4. Choose one state:
   - fast
   - slow-candidate
   - observe
   - ignore
   - reject
5. Apply the smallest justified next step.

### When reviewing a candidate
1. Read the candidate protocol and checklist.
2. Read linked evidence.
3. Judge whether the candidate should:
   - merge
   - stay separate
   - split
   - supersede
   - create
   - do nothing
4. Write back the review using the standard review output format.

### When doing heartbeat review
1. Read the heartbeat protocol.
2. Review recent evidence and current candidates.
3. Output either:
   - no-action
   - update existing candidate
   - create one candidate
   - split candidate
   - reject candidate

---

## Example files

Start with:
- `references/examples/example-fast.md`
- `references/examples/example-slow-candidate.md`
- `references/examples/example-reject.md`

These cover the three highest-value review paths:
- when to keep a fix local
- when to create or update one durable candidate
- when to reject or roll back a weak candidate

Older worked examples remain in `references/` for maintenance and deeper study.

---

## What FastSlow Evo is not

It is not:
- a Python rule engine
- a file spammer that turns every event into a candidate
- a shortcut for promoting weak evidence
- an excuse for uncontrolled self-modification

---

## Philosophy

**Fast where local adaptation is enough. Slow only when durable promotion is earned.**
