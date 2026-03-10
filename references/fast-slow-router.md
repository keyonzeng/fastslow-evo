# Fast / Slow Router

Use this router to decide whether an issue belongs in the fast loop or the slow loop.

## Route to Fast Loop when the issue is:

- local rather than systemic
- frequent rather than rare
- low-blast-radius rather than high-blast-radius
- easy to verify in the next task
- likely solvable by checklist, template, memory rule, or tiny script

### Typical fast-loop cases
- wording or tone drift
- missing action item in summaries
- repeated formatting mistake
- local tool-result misread
- small workflow omission
- user says “next time do it this way”

### Typical fast-loop outputs
- checklist
- template
- memory rule
- tiny validation rule
- tiny script

## Route to Slow Loop when the issue is:

- cross-task rather than local
- boundary-changing rather than stylistic
- safety- or privacy-relevant
- difficult to validate from one case
- likely to affect memory, behavior, workflows, or reusable capability broadly

### Typical slow-loop cases
- durable memory policy
- group/private context boundary
- capability claims and validation boundaries
- workflow promotion to a skill
- recurring pattern that appears across tasks or channels

### Typical slow-loop outputs
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- skill promotion

## Escalation Rule

A fast-loop fix should be considered for slow-loop promotion when:
- it recurs 3+ times
- it proves stable across contexts
- it survives validation
- it reduces recurrence without introducing regressions

## De-escalation Rule

A proposed slow-loop change should be pushed back to the fast loop when:
- evidence is thin
- blast radius is unclear
- a lighter fix would probably work
- the change sounds more impressive than useful
