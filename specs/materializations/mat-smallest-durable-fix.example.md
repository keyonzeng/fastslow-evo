# Materialization Spec: mat-smallest-durable-fix

## Source Delta
An approved spec delta derived from repeated evidence.

## Chosen Form
Select the lightest artifact that prevents recurrence.

## Target Paths
- evidence/ for raw incidents
- specs/ for durable policy
- proposals/ for pending changes
- workspace guidance or scripts only after review

## Rationale
Heavier materializations create more maintenance surface and larger blast radius. Prefer smaller durable fixes first.

## Validation Needed
- confirm the lighter artifact actually changes behavior or retrieval
- confirm recurrence drops after adoption

## Rollback Method
Remove or revert the promoted artifact and preserve the evidence trail.
