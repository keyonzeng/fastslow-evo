# 08 — Heartbeat should not create candidate spam

## Real-source anchor
- Common reliability pattern seen across agent-review discussions: periodic review becomes uncontrolled candidate creation

## Scenario
During a heartbeat review, the agent sees six recent evidence items:
- two clearly related
- three weak signals
- one obvious noise item

There is already one existing candidate that the two related items could strengthen.

## What this case is testing
- whether heartbeat behaves like a reviewer instead of a mutation engine
- whether the skill prefers updating one candidate over creating many new ones

## Expected route
- update one existing candidate or no-action for most items
- weak items should remain `observe` or `ignore`

## Expected good write-back
- candidate creation is minimal and justified
- weak signals do not get promoted
- old candidate is reused when appropriate

## Failure signals
- creates multiple new candidates in one heartbeat
- promotes weak signals into durable policy
- ignores the existing candidate and starts over repeatedly
