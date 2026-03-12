# Validation Suite

Use this suite to test whether FastSlow Evo behaves like a real dual-loop self-evolution system rather than a pile of documentation.

## What to validate

Validate four things:

1. **Routing quality**
   - Does it send the right cases to fast, slow, observe, or ignore?
2. **Fast-loop usefulness**
   - Do tiny fixes improve the next similar task?
3. **Slow-loop discipline**
   - Does promotion happen only when evidence is strong enough?
4. **Heartbeat judgment**
   - Does monitoring nominate the right promotion and rollback candidates?

## Validation philosophy

Do not ask whether the system "sounds intelligent."
Ask whether it:
- routes correctly
- reduces recurrence
- promotes carefully
- avoids making the system worse

## Core test packs

### Pack A — Fast-loop cases
Expected result: `fast`

- one-off but clearly reusable tone correction
- summary missing one action item
- tool output misread once

### Pack B — Slow-loop cases
Expected result: `slow`

- same issue repeated 3+ times
- repeated stable fix across contexts
- boundary-level or workflow-level improvement

### Pack C — Observe-only cases
Expected result: `observe`

- weak evidence
- one ambiguous complaint
- unstable or mood-dependent preference signal

### Pack D — Ignore-as-noise cases
Expected result: `ignore`

- clear one-off annoyance
- no durable lesson
- no practical fix worth keeping

## Success thresholds

### Router
- At least 80% of test cases should route to the expected bucket.

### Fast loop
- At least one measurable improvement after applying the tiny fix.

### Slow loop
- No promotion should happen without recurrence + validation path.

### Heartbeat
- Candidates should be plausible and explainable.
- Noise should not dominate promotion suggestions.

## Recommended workflow

1. Build sample cases.
2. Run router scoring.
3. Review decisions manually.
4. Run heartbeat monitor on a synthetic evidence set.
5. Compare recommendations against human judgment.

## Final question

A real self-evolution system should be able to answer:
- what changed?
- why did it change?
- why was that worth keeping?
- what would make us undo it?
