# Example 1: Meeting Summary Missed Action Items

## Evidence Example

```md
# Incident Record: inci-example-meeting-actions

## Summary
The meeting summary omitted the action items and owners.

## Source
- user

## Context
Weekly project sync summary review.

## Full Context
- task: produce a concise meeting summary with decisions and follow-ups
- user-intent: get a usable summary, not just a narrative recap
- surrounding-dialogue: user asked for summary and next steps
- prior-agent-behavior: produced a polished recap but omitted concrete actions
- tool-results: none
- environment-signals: repeated meeting-summary use case

## Raw Signal
- "这次总结没把 action items 和 owner 拉出来，还是不能执行。"

## Notes
- gap: validation_gap
- recurrence_hint: 2
- created_at: <fill>
```

## Expected Review Result

```md
## Review Result
- What happened: The summary captured discussion content but omitted action items and owners.
- Why it matters: The output looks polished but is operationally incomplete, so it reduces workflow reliability.
- Pattern judgment: same-pattern
- Pattern rationale: This matches prior evidence where summaries were acceptable narratively but failed to preserve executable follow-ups.
- Convergence action: merge-into-existing-candidate
- Convergence rationale: The root failure is the same underlying summary-quality gap, so a new candidate would duplicate review work.
- State decision: slow-candidate
- State rationale: The issue is recurring and affects a repeated workflow, so local handling alone is no longer enough.
- Proposed next step: update one candidate for meeting-summary action completeness and propose a validation rule.
- Validation path: Check the next similar summaries for action item, owner, and follow-up completeness.
- Regression / rollback trigger: If later evidence shows the omissions come from different task types with different root causes, split the candidate.
```
