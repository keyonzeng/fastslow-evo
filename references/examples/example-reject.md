# Example: Reject or rollback a weak candidate

## Situation

A candidate was created after one vivid incident and a few loosely similar files.
Later review shows:
- the files are not strongly the same pattern
- recurrence was inferred mainly from keyword overlap or file count
- validation and rollback were never stated clearly

## What happened

The candidate looks more confident than the evidence supports.
The stored object is now more likely to mislead future review than help it.

## Why it matters

Weak candidates are dangerous because they create false memory pressure:
- later reviewers may treat them as established patterns
- weak merges can harden noise into policy
- cleanup becomes harder over time

## Sameness judgment

Do not preserve this candidate just because several evidence files mention similar words.
Preserve it only if the underlying behavioral pattern is demonstrably the same.
If not, reject it or split it.

## Route

`reject`

## Smallest justified action

- explicitly mark the candidate unsupported or rolled back
- point to the missing justification: weak sameness, weak recurrence, unclear validation, or unclear rollback
- keep the useful evidence files if they may support future review under a different pattern

## Why not observe

`observe` is for thin but still plausible patterns.
Use `reject` when the current candidate itself is misleading enough that leaving it alive would distort future judgment.

## Example write-back

- outcome: `reject`
- rationale: candidate built on weak sameness and file-count inference rather than stable recurrence
- action: close or roll back the candidate; preserve raw evidence separately if still useful
