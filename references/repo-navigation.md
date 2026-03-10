# Repository Navigation

Use this file to keep the repository mentally clean.

## Primary Path

These files define what FastSlow Evo fundamentally is:
- `SKILL.md`
- `README.md`
- `README.zh-CN.md`
- `references/skill-first-architecture.md`
- `references/seven-skills-essence.md`
- `references/one-page-start.md`

These should answer:
- what FastSlow Evo is
- why dual-loop evolution matters
- how the host model should use fast and slow loops
- how to start without misunderstanding the architecture

## Governance Path

These files define review and promotion discipline:
- `references/quick-adapt.md`
- `references/slow-promote.md`
- `references/fast-slow-router.md`
- `references/router-intelligence.md`
- `references/heartbeat-monitor.md`
- `references/spec-review-checklist.md`
- `references/validation-suite.md`

These should answer:
- how to route signals
- how to review recurrence
- when to promote
- when to roll back

## Helper Path

These files and scripts support operation but are not the core intelligence:
- `install.sh`
- `fastslow.py`
- `scripts/install_openclaw.py`
- `scripts/setup_runtime.py`
- `scripts/capture_runtime.py`
- `scripts/capture_from_text.py`
- `scripts/route_runtime.py`
- `scripts/heartbeat_runtime.py`
- `scripts/build_promotion_candidate.py`

These exist to:
- install
- initialize runtime state
- persist signals
- write candidate files
- validate and debug

## Fallback / Test Path

These are useful, but should not be mistaken for the main product identity:
- helper scripts that simulate routing
- sample evidence files
- validation fixtures
- synthetic benchmark cases

If someone starts explaining FastSlow Evo mainly through these files, they are probably drifting away from the skill's real center of gravity.

## Rule of Interpretation

When describing the project:
1. start from the skill
2. then explain the governance model
3. only then mention the helper scripts

Do not present the helper layer as the product itself.
