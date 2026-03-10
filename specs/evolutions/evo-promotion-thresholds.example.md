# Evolution Spec: evo-promotion-thresholds

## Eligible Signals
- repeated incidents of the same gap type
- repeated user corrections with the same prevention rule
- repeated successful workaround using the same pattern

## Minimum Evidence
- 1 strong incident -> local evidence note only
- 2 similar incidents -> checklist or validation-spec candidate
- 3 recurring incidents -> script / workflow / skill candidate

## Required Review Level
- L1 for curated memory, checklists, templates
- L2 for scripts, skill edits, durable workflow rules
- L3 for code/config mutation or automation changes with meaningful blast radius

## Allowed Targets
- specs/
- evidence/
- proposals/
- scorecards/
- workspace guidance files after review

## Forbidden Targets
- secrets or .env
- unrelated session history
- self-rewriting evolution engine in production
- auto-publish flows

## Rollback Requirement
Any non-trivial promotion must name a practical rollback path and a regression signal.
