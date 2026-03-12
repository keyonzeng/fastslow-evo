# FastSlow Evo Release

## What it is

FastSlow Evo is a judgment-first, protocol-first skill for AI agents.
It routes experience into a fast loop for local adaptation and a slow loop for reviewed durable promotion.

## What's included

- `SKILL.md` runtime entry
- layered `references/` structure
- worked examples
- `smoke-tests/` suite
- `install.sh` for OpenClaw workspace install
- packaged release artifact: `fastslow-evo.skill`

## Key properties

- fast/slow dual-loop routing
- explicit `fast`, `slow candidate`, `observe`, `ignore`, `reject` states
- heartbeat as reviewer, not mutation engine
- validation and rollback discipline for durable promotion
- semantic sameness over keyword overlap

## Install

### OpenClaw workspace install
```bash
bash install.sh
```

### Packaged artifact
Use the generated `fastslow-evo.skill` release asset.

## Quick start

Read:
- `references/runtime-core/minimal-usable-workflow.md`

Then use the smoke tests if you want a quick capability check:
- `smoke-tests/README.md`
- `smoke-tests/results.md`

## Validation status

- smoke test suite passed strongly
- packaged successfully with Skill Creator tooling
- GitHub repository synchronized
