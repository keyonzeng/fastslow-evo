# 03A — Observe on first tool-overload signal

## Real-source anchor
- Langflow blog: "Top 3 Mistakes I Made While Building AI Agents"
- https://www.langflow.org/blog/top-three-mistakes-building-agents

## Scenario
In one complex task, an agent confuses multiple tools, skips a step, and returns a broken flow.
This is the first clearly recorded incident of this type.

## Evidence pack
- Evidence A: the agent mixed a URL-reading step with a document-editing step and skipped an intermediate validation step

## What this case is testing
- whether the skill avoids overfitting on a single workflow failure

## Expected route
- `observe`

## Expected good write-back
- preserves the incident as meaningful evidence
- does not overstate recurrence
- explains why more evidence is needed before durable promotion

## Failure signals
- creates a slow candidate immediately from one incident
- calls it noise and throws it away
- invents a broad workflow rule without recurrence
