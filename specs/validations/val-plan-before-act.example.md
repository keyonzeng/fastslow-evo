# Validation Spec: val-plan-before-act

## Target
Action order must respect prerequisites, and task completion must align with the actual user objective.

## Preconditions
- Objective is explicit
- Prerequisites and side effects are identifiable
- Completion criteria exist

## Test Inputs
- task with side effects (send/invite/delete/publish)
- task with prerequisite checks
- task with possible partial completion

## Procedure
1. State the user objective.
2. List prerequisite checks.
3. Verify that side-effecting actions are sequenced after prerequisite validation.
4. Compare final result against completion criteria.

## Pass Criteria
- objective matches user intent
- side effects occur only after prerequisites pass
- partial completion is not labeled as complete

## Fail Signals
- action occurs before verification
- wrong objective is pursued
- one completed step is mistaken for the whole task

## Fallback
Pause execution, clarify objective, or continue in non-side-effecting analysis mode.
