# 07 — Reject a weak candidate built on keyword overlap

## Real-source anchor
- Failure-analysis thinking reflected in research and discussion around recurrence metrics for code agents

## Scenario
A candidate already exists, but on review the evidence looks weak.
The files share similar wording, but the underlying behavioral pattern is not clearly the same.
Validation and rollback were never defined.

## Evidence pack
- Existing candidate: broad claim about "agent forgetfulness"
- Evidence A: formatting omission
- Evidence B: wrong tool call timing
- Evidence C: delivery mismatch

## What this case is testing
- whether the skill can reject a misleading stored candidate
- whether it resists preserving weak structure just because it already exists

## Expected route
- `reject` or split, with strong justification

## Expected good write-back
- points out weak sameness
- explains why file-count or keyword overlap is insufficient
- closes or rolls back the candidate cleanly if needed

## Failure signals
- preserves the candidate just because it exists
- uses recurrence metrics without semantic sameness
- refuses to reject unsupported structure
