# 09 — Structural problem, not just a prompt tweak

## Real-source anchor
- PromptEngineering discussion that some LLM failures are not really prompt failures
- reinforced by Langflow and Galileo examples where architecture and workflow matter more than prompt wording

## Scenario
Several failures look like prompt issues on the surface, but across cases the deeper problem is workflow design:
- wrong tool order
- weak state handling
- missing validation step

## Evidence pack
- Evidence A: prompt changed, but failure repeated in a tool chain
- Evidence B: wording updated, but state loss still breaks execution
- Evidence C: better phrasing helps briefly, then the workflow fails again

## What this case is testing
- whether the skill can identify structural recurrence instead of staying at prompt level

## Expected route
- `slow candidate`

## Expected good write-back
- explains why a prompt tweak alone is insufficient
- frames the issue as workflow or validation discipline
- proposes a durable route, not only another wording tweak

## Failure signals
- keeps suggesting local prompt edits forever
- does not recognize the structural layer
- avoids durable promotion despite clear recurrence
