# Step-by-Step User Guide

Read `one-page-start.md` first if you want the shortest path.

This guide is for real first use, not for framework study.

## What this skill is

`fastslow-evo` helps you improve an agent quickly without letting it drift into vague self-modification.

It does this with two loops:
- a fast loop for small local fixes
- a slow loop for validated durable promotion

Together they turn repeated problems into:
- evidence
- gap classification
- tiny fixes
- spec deltas
- validated improvements

## What to expect

You do **not** need to adopt the whole system on day one.

The best first run is:
- one starter pack
- one or two real incidents
- one proposal
- one small improvement

## Step 1 — Pick your starter pack

Choose the closest fit:

### Coding agent
Use if your agent writes code, runs tools, or delegates technical tasks.

### Workflow automation agent
Use if your agent sends messages, updates systems, moves data, or runs business flows.

### Support / concierge agent
Use if your agent handles user context, preferences, or repeated support interactions.

### Research agent
Use if your agent reads sources, summarizes information, or cites evidence.

Start with only 3-5 artifacts from that pack.

## Step 2 — Initialize a working tree

Run:

```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

This creates:
- `specs/`
- `evidence/`
- `proposals/`
- `scorecards/`

## Step 3 — Install your first safety layer

Before trying “self-improvement”, add these first:

1. one validation spec
2. one bounded execution or memory-safety behavior spec
3. one promotion-threshold rule

Recommended defaults:
- `specs/validations/val-tool-faithfulness.example.md`
- `specs/behaviors/beh-bounded-execution.example.md`
- `specs/evolutions/evo-promotion-thresholds.example.md`

## Step 4 — Record a real problem

When the agent fails, gets corrected, or succeeds in a reusable way, record it.

### Fast path

Run:

```bash
python3 scripts/new_gap_entry.py "agent claimed tool success without evidence" --gap validation_gap --source review --task "automation run" --out ./my-agent-specs/evidence/incidents
```

### Manual path

Use one of these templates:
- `assets/incident-record.template.md`
- `assets/correction-record.template.md`
- `assets/win-record.template.md`

## Step 5 — Classify the gap

Choose one primary gap type:
- capability_gap
- behavior_gap
- validation_gap
- retrieval_gap
- workflow_gap
- safety_gap
- tooling_gap
- scope_gap

If you are unsure, read:
- `references/gap-taxonomy.md`

Do not skip this step. Most messy fixes come from solving the wrong gap.

## Step 6 — Draft the smallest spec delta

Ask:
- what rule would have prevented this?
- does it belong in capability, behavior, or validation?
- what is the lightest durable fix?

Then draft a proposal.

Run:

```bash
python3 scripts/build_evolution_proposal.py "tool-faithfulness-hardening" --gap validation_gap --cases 2 --recurrence 2 --spec-type validation --artifact checklist --review L1 --out ./my-agent-specs/proposals
```

## Step 7 — Decide how heavy the fix should be

Do **not** jump straight to a new skill or code change.

Use the recommender:

```bash
python3 scripts/recommend_materialization.py --gap validation_gap --recurrence 2 --risk medium
```

Typical outputs:
- checklist
- curated-memory
- script
- skill

## Step 8 — Review before promotion

Before making the change durable, use:
- `references/spec-review-checklist.md`

Check:
- is it evidence-backed?
- is it testable?
- is it too heavy?
- is rollback practical?

## Step 9 — Apply one small durable improvement

Good first improvements are:
- a validation checklist
- a memory rule
- a behavior rule
- a script for a repeated deterministic task

Bad first improvements are:
- rewriting the whole system
- adding many specs at once
- self-modifying automation in production

## Step 10 — Measure if it actually helped

Use:
- `assets/scorecard.template.md`

Track:
- recurrence before/after
- user corrections before/after
- regressions introduced
- time saved

If the metric does not improve, do not add more structure. Fix the weak spec.

## Good adoption pattern

Week 1:
- 3-5 evidence records
- 1 starter pack
- 1 proposal
- 1 small durable fix

Week 2:
- review recurrence
- add one more validation or behavior spec if needed
- only then consider scripts or a skill-level upgrade

## Common mistakes

- adopting the full framework immediately
- promoting one-off incidents into permanent rules
- treating fluent text as proof of execution
- storing untrusted content as durable memory
- skipping rollback planning
- adding a skill when a checklist would solve it

## Rule of thumb

If the system feels heavy, you are probably promoting too much too early.

The point of `fastslow-evo` is not to make agent evolution look impressive.
It is to make it fast where it should be fast, and slow where it must be slow.
