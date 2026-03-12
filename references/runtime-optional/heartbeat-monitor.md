# Heartbeat Monitor

FastSlow Evo should use heartbeats to monitor whether fast-loop outputs are maturing into promotion candidates.

## Purpose

A heartbeat should not only check inboxes, calendars, or notifications.
It can also check the state of recent adaptation.

## What heartbeat should inspect

### 1. Recent evidence
Look for recent additions in:
- incident records
- correction records
- win records
- proposals

### 2. Fast-loop outputs
Check whether recent tiny fixes exist, such as:
- new checklist items
- new template tweaks
- new memory rules
- tiny validation rules
- tiny local fixes expressed as markdown rules, checklists, or templates

### 3. Recurrence trends
Ask:
- did the same problem recur after the fix?
- did recurrence drop?
- did the user still correct the same type of issue?
- did the same workaround succeed repeatedly?

### 4. Cross-context spread
Ask:
- is this showing up in different task types?
- is it appearing across channels or surfaces?
- is it no longer local?

## Heartbeat Outputs

A heartbeat should classify each watched pattern as one of:

- **stay-fast**
- **promote-candidate**
- **rollback-candidate**
- **noise / no-action**

## Promotion Candidate Conditions

A pattern becomes a promotion candidate when:
- recurrence reaches 3+
- the tiny fix has been reused successfully
- the fix appears stable across contexts
- a validation path exists
- promotion would likely reduce future friction materially

## Rollback Candidate Conditions

A pattern becomes a rollback candidate when:
- the tiny fix did not reduce recurrence
- it created new friction or confusion
- it increased user corrections elsewhere
- the fix overfit one narrow case

## Heartbeat Rule

Do not promote directly during heartbeat unless explicitly authorized.
Heartbeat should primarily:
- observe
- summarize
- nominate candidates
- recommend next action

## Recommended Cadence

Good default:
- light scan every day or every few days
- deeper promotion review weekly

## Success Criterion

Heartbeat makes FastSlow Evo feel cumulative over time, not reactive one turn at a time.
