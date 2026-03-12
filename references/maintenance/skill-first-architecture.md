# Skill-First Architecture

FastSlow Evo should be built as a **skill-first, model-first** system.

## Core Principle

Do not move primary intelligence away from the host model when the host environment already provides strong judgment.

In OpenClaw, Claude Code, Cursor, OpenCode, and similar environments:
- the host model should do semantic routing and evolution judgment
- the skill should provide the framework, discipline, and evaluation lens
- markdown protocols should constrain and structure the judgment
- installation and file setup should remain mechanical only

## Three Layers

### 1. Skill / Model Layer
This is the real core.

Responsibilities:
- detect meaningful signals
- distinguish fast / slow / observe / ignore / reject
- evaluate recurrence and stability
- decide whether to preserve, promote, defer, split, or ignore
- review heartbeat signals
- recommend promotion and rollback paths

### 2. Governance Layer
This is the discipline layer.

Responsibilities:
- evidence-writing rules
- convergence rules
- promotion thresholds
- validation expectations
- regression control
- rollback awareness
- anti-overfitting rules

This layer should live in:
- `SKILL.md`
- `references/`
- templates and review rules

### 3. Utility Layer
This is the utility layer.

Responsibilities:
- install
- runtime directory init
- markdown template copying
- simple operational setup

This layer should live in:
- `install.sh`
- templates
- workspace layout

## Anti-Pattern

Do not let the project drift into:
- a Python rule engine with a skill wrapper
- a mechanical utility layer pretending to be the judgment layer
- a logging system pretending to be evolution

## FastSlow Evo's Distinct Role

FastSlow Evo is not trying to win by being:
- the best logger
- the best memory store
- the heaviest evolver

It wins by being the judgment layer that decides how experience should move between logging, reflection, memory, and durable promotion.
