# Capability Spec: cap-plan-before-act

## Summary
The agent can separate goal understanding, planning, action ordering, and completion checks so that external side effects do not occur before prerequisites are verified.

## In Scope
- Clarifying objective before action
- Sequencing dependent steps correctly
- Checking completion against explicit criteria
- Deferring side effects until prerequisites pass

## Out of Scope
- Perfect planning in all ambiguous domains
- Acting on unclear objectives without confirmation
- Treating partial progress as task completion

## Preconditions
- User goal can be represented explicitly
- Plan steps can be ordered and inspected
- Validation criteria exist for the final outcome

## Known Failure Modes
- wrong objective chosen
- invite/email/send action happens before prerequisite checks
- one success step is mistaken for full completion
- plan order violates task dependencies

## Success Definition
- objective is explicit
- dependent steps execute in correct order
- side effects happen only after required checks
- completion is tied to acceptance criteria, not effort spent

## Validation Refs
- validations/val-plan-before-act.example.md
