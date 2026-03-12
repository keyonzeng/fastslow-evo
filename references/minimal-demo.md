# Minimal Starter Demo

This demo shows the smallest practical loop.

## Scenario
A workflow agent repeatedly says it sent or updated something, but execution evidence is missing or partial.

## 1. Record the incident

Create an incident under:
- `evidence/incidents/`

Primary gap:
- `validation_gap`

## 2. Use existing example specs

Start with:
- `specs/capabilities/cap-tool-execution-proof.example.md`
- `specs/validations/val-execution-proof.example.md`
- `specs/evolutions/evo-promotion-thresholds.example.md`

## 3. Draft proposal

Goal:
Prevent “claimed success without execution proof”.

Likely first materialization:
- checklist or curated-memory

If recurrence continues and validation is deterministic:
- script

## 4. Review

Run through:
- `references/maintenance/spec-review-checklist.md`

## 5. Measure

Use:
- `assets/scorecard.template.md`

Success means recurrence drops and false completion claims fall.

## Why this demo matters

It is common, painful, and broadly reusable across coding, workflow, and support agents.
