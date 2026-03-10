# First-Run Workflow

Use this on the first real adoption of the skill.

## Goal

Get a user from zero to a working spec-driven improvement loop in one short setup session.

## Step 1 — Pick a starter pack

Choose one:
- coding agent
- workflow automation agent
- support / concierge agent
- research agent

Do not start by adopting the whole framework.
Start with 3-5 artifacts from the closest starter pack.

## Step 2 — Initialize the spec tree

Run:

```bash
python3 scripts/init_spec_tree.py <target-path>
```

This creates the minimal folders for specs, evidence, proposals, and scorecards.

## Step 3 — Install the first protection layer

Before any sophisticated evolution, install these first:

- one validation spec
- one bounded-execution or memory-safety behavior spec
- one promotion-threshold evolution spec

This prevents “self-improvement” from becoming uncontrolled drift.

## Step 4 — Capture real evidence for 3-7 days

Do not promote aggressively in the first hour.

For the first few days:
- record incidents
- record corrections
- record successful repeated patterns
- classify primary gap type

Use:
- `assets/incident-record.template.md`
- `assets/correction-record.template.md`
- `assets/win-record.template.md`
- `scripts/new_gap_entry.py`

## Step 5 — Draft only small spec deltas

During the first iteration window, prefer:
- curated memory
- checklist
- validation spec

Avoid starting with:
- heavy scripts
- new skill creation
- code/config mutation

unless the evidence is already strong.

## Step 6 — Run one weekly review

At the end of the first cycle:
- identify top recurring gap
- draft one evolution proposal
- run one regression review
- choose the smallest durable materialization

Use:
- `assets/evolution-proposal.template.md`
- `assets/regression-checklist.template.md`
- `scripts/recommend_materialization.py`

## Step 7 — Measure before scaling

Use `assets/scorecard.template.md`.

If recurrence is not dropping, do not add more framework.
Fix the weakest current spec first.

## First-Run Rule

If a user is new to this skill, optimize for:
- fast trust
- visible pain reduction
- minimal ceremony

The first version should feel useful in a day, not impressive in a slide deck.
