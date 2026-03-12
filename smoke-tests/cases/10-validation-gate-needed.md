# 10 — Repeated regression means a validation gate is needed

## Real-source anchor
- Kinde article: "Running Prompt & Agent Regression Tests in GitHub Actions"
- https://www.kinde.com/learn/ai-for-software-engineering/ai-devops/ci-cd-for-evals-running-prompt-and-agent-regression-tests-in-github-actions/

## Scenario
A certain class of agent error has already been fixed multiple times, but it keeps coming back.
Manual reminders are no longer enough.
The real missing piece is a validation or regression gate.

## Evidence pack
- Evidence A: error fixed once
- Evidence B: same class of regression returns later
- Evidence C: another local fix works briefly, then the regression returns again

## What this case is testing
- whether the skill can recognize when repeated fast fixes are no longer sufficient
- whether it can route toward validation materialization

## Expected route
- `slow candidate`

## Expected good write-back
- recognizes that repeated recurrence justifies durable validation
- proposes materialization into a validation or regression spec
- explains why more local reminders are not enough

## Failure signals
- stays in fast forever
- says only "watch it" despite repeated regressions
- does not surface the need for a durable gate
