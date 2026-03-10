# Validation Spec: val-action-item-completeness

## Target
Action extraction from meetings, classes, or discussions should capture who needs to do what, by when, and any blockers or dependencies.

## Preconditions
- Source notes or transcript contains action-oriented content
- Output format supports structured actions

## Test Inputs
- meeting notes with decisions and owners
- lecture/project notes with next steps

## Procedure
1. Identify all explicit and strongly implied action items.
2. Check whether each item includes owner, action, and time signal when available.
3. Check whether blockers or dependencies are preserved.
4. Compare extracted actions to the original source.

## Pass Criteria
- major action items are captured
- owners and deadlines are preserved when present
- blockers are not dropped

## Fail Signals
- action item missing
- owner missing despite source clarity
- follow-up presented without dependency context

## Fallback
Ask for a structured action review instead of a single freeform summary.
