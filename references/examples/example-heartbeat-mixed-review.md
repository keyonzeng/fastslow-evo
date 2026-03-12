# Example: Heartbeat mixed review output

## Situation

A heartbeat review sees six recent evidence items:
- two clearly strengthen an existing delivery-discipline candidate
- three are weak signals that may matter later but are not stable enough yet
- one is obvious noise

There is already one candidate that the two stronger items belong to.

## What happened

This is not a case for broad new candidate creation.
The main job is to review, update, and stay selective.

## Good heartbeat judgment

- update the existing candidate with the two strongly related items
- keep the three weak items under `observe`
- mark the obvious noise item as `ignore`
- create no new timestamp-based candidate burst

## Why it matters

Heartbeat should behave like a reviewer, not a mutation engine.
A good heartbeat run often produces mixed outcomes across items while still writing back only a small number of justified review actions.

## Example write-back

- primary action: update existing candidate
- secondary handling: three items remain under `observe`
- noise handling: one item `ignore`
- rationale: recurrence is meaningful for the existing candidate, but the remaining items do not justify new durable structure
