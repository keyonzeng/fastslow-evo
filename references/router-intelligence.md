# Router Intelligence

FastSlow Evo should not depend only on explicit user commands like "use the fast loop" or "use the slow loop".

Its core ability is to **infer the right loop by default**, while still allowing user override.

## Purpose

Route incoming signals into one of four buckets:

1. **fast-loop execution**
2. **slow-loop promotion candidate**
3. **observe only**
4. **ignore as noise**

## Primary Signals

Use these signals to score the routing decision.

### 1. Recurrence
- Has the same issue appeared before?
- Is the same correction repeated?
- Is the same workaround being reused?

### 2. Blast radius
- Is this local to one task?
- Does it affect multiple contexts, channels, or users?
- Does it alter memory, behavior, privacy, or workflow boundaries?

### 3. Validation difficulty
- Can success be checked in the next task?
- Does it require several uses or cross-context comparison?
- Is the effect mostly subjective or operationally testable?

### 4. Risk
- Could a bad fix create confusion, leakage, drift, or false confidence?
- Is the issue style-level, workflow-level, or boundary-level?

### 5. Reuse potential
- Is this a one-off annoyance?
- Does it look broadly reusable?
- Does it affect repeated patterns of work?

### 6. Correction density
- How often does the user correct the same class of output?
- Are multiple corrections pointing to the same hidden pattern?

## Routing Defaults

### Route to Fast Loop by default when:
- recurrence is low to moderate
- blast radius is low
- validation is easy in the next task
- risk is low
- the likely output is a checklist, template, memory rule, tiny validation rule, or tiny script

### Route to Slow Loop candidate when:
- recurrence is 3+
- the fix seems stable across contexts
- the issue affects broader behavior, memory, capability, or workflow
- validation can be defined
- regression risk matters

### Route to Observe Only when:
- evidence is too thin
- recurrence is unclear
- the issue may be noise or mood-dependent
- a fix now would likely overfit

### Route to Ignore as Noise when:
- the event is clearly one-off
- there is no durable lesson
- the correction does not generalize
- no practical change would improve future work

## Decision Heuristic

Use this order:

1. Is a local next-task fix obvious and low risk?
   - yes -> fast loop
2. Is the problem repeated enough to justify durable promotion?
   - yes -> slow-loop candidate
3. Is there not enough evidence yet?
   - yes -> observe only
4. Is this mostly noise?
   - yes -> ignore

## User Override Rule

User instruction always matters, but the system should still reason about whether the requested loop is appropriate.

- If user asks for slow loop on one thin incident, warn and de-escalate.
- If user keeps manually asking for fast loop on a recurring stable issue, suggest promotion.

## Success Criterion

The router reduces both:
- premature promotion
- repeated under-promotion
