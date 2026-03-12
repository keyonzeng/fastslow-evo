# Example 3: Looks Similar But Should Split

## Scenario
Two records both mention "missing action items," but they should not automatically merge.

### Record A
- task goal: summarize a meeting
- failure location: summary structure omitted next steps
- root issue: summary validation gap

### Record B
- task goal: generate a project plan
- failure location: planning logic never produced owners or dependencies
- root issue: planning completeness gap

## Correct Judgment

```md
## Review Result
- What happened: Two records both mention missing actions, but the failures occurred in different task types with different root causes.
- Why it matters: Merging them would hide the real cause and produce a weak candidate.
- Pattern judgment: related-but-distinct
- Pattern rationale: The symptom overlaps, but one is a summary-quality omission and the other is a planning-logic omission.
- Convergence action: keep-separate
- Convergence rationale: Separate candidates preserve cleaner validation and avoid over-merging.
- State decision: observe
- State rationale: Similarity is not enough; each pattern needs its own evidence trail before durable promotion.
- Proposed next step: maintain separate evidence threads and review again if either pattern stabilizes.
- Validation path: Observe whether future meeting-summary records align with A and future planning records align with B.
- Regression / rollback trigger: If later evidence shows a shared deeper root cause, review for merge then.
```
