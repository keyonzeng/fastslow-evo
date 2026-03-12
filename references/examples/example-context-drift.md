# Example: Context drift in a long task

## Situation

Across several long tasks, the agent repeatedly drops earlier constraints after multiple tool steps or long intermediate reasoning chains.
The surface mistakes differ, but the failure shape is similar:
- earlier delivery constraint is forgotten later
- a corrected assumption reappears near the end of the task
- a required boundary or formatting rule disappears after several intermediate actions

## What happened

The likely shared pattern is context drift during long workflows, not three unrelated local mistakes.

## How to judge it

Use `observe` if:
- there are too few examples
- the shared root cause is still speculative
- the surface errors do not yet line up cleanly enough

Use `slow candidate` if:
- recurrence is now clear across multiple long tasks
- the same failure shape appears after extended workflow length or step count
- a durable mitigation can be stated, validated, and rolled back

## What not to do

Do not:
- merge every kind of forgetting into one giant candidate
- use file count as the main proof
- promote just because three files exist

## Example write-back: observe

- outcome: `observe`
- rationale: plausible context-drift pattern, but root-cause confidence is still limited
- action: keep evidence small and collect one or two more aligned cases

## Example write-back: slow candidate

- outcome: `slow candidate`
- rationale: repeated long-task constraint loss now forms a stable pattern with meaningful reuse potential
- action: create or update one candidate around long-workflow constraint retention with explicit validation and rollback
