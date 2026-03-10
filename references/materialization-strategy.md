# Materialization Strategy

Convert an approved spec delta into the lightest artifact that solves the problem.

## Preferred Order

1. evidence note
2. curated memory
3. checklist
4. template
5. script
6. skill edit/new skill
7. code/config change

## Selection Heuristics

### Use a curated memory note when
- the lesson is stable
- retrieval was the main problem
- no executable artifact is required

### Use a checklist when
- errors come from missed steps
- the workflow is stable
- human or agent review remains useful

### Use a template when
- repeated outputs share structure
- consistency matters more than automation

### Use a script when
- the same deterministic transformation keeps recurring
- correctness benefits from executable logic

### Use a skill when
- the need recurs across projects
- trigger phrases are stable
- a reusable procedure improves model performance

### Use code/config mutation only when
- lighter forms are insufficient
- validation is strong
- rollback is clear
- blast radius is understood

## Design Rule

Do not materialize to a heavier layer just because it feels more sophisticated.
