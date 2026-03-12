# Step-by-Step User Guide

Read `one-page-start.md` first if you want the shortest path.
If you want the most directly usable path, read `minimal-usable-workflow.md` first.

This guide is for real first use, not framework admiration.

## What this skill is

`fastslow-evo` helps you improve an agent quickly without letting it drift into vague self-modification.

It does this with two loops:
- a fast loop for small local fixes
- a slow loop for validated durable promotion

Together they turn repeated problems into:
- evidence
- review judgments
- tiny fixes
- candidate convergence
- validated improvements

## What to expect

You do **not** need to adopt the whole system on day one.

The best first run is:
- one or two real evidence records
- one review pass
- one small improvement
- one candidate only if justified

## Step 1 — Prepare the working shape

If you are using the OpenClaw install path, run:

```bash
./install.sh
```

That prepares:
- runtime evidence folders
- proposals
- scorecards
- durable specs
- starter templates

## Step 2 — Preserve one real signal

When the agent fails, gets corrected, or succeeds in a reusable way, preserve that signal.

Use the markdown templates.
The important point is that the signal becomes reviewable instead of disappearing into chat history.

## Step 3 — Read the review stack before judging

For a normal evidence review, read:
1. `references/runtime-optional/openclaw-judgment-first.md`
2. `references/runtime-branches/evidence-protocol.md`
3. `references/runtime-core/review-protocol.md`
4. `references/runtime-core/evaluation-rubric.md`
5. the evidence file
6. `references/runtime-core/review-output-format.md`

If candidate sameness is in question, also read:
- `references/runtime-branches/candidate-protocol.md`
- `references/runtime-branches/candidate-review-checklist.md`

## Step 4 — Make the judgment explicitly

Choose one state:
- fast
- slow-candidate
- observe
- ignore
- reject

Do not skip the reasoning.
Explain:
- what happened
- why it matters
- why this is or is not the same pattern as prior evidence
- what should happen next

## Step 5 — Apply the smallest justified next step

Good first improvements are:
- a validation checklist
- a memory rule
- a behavior rule
- a template refinement
- one candidate update

Bad first improvements are:
- rewriting the whole system
- adding many specs at once
- promoting thin evidence into durable policy

## Step 6 — Review again only when needed

If more evidence appears, review again.
If not, do not force extra structure.

## Good adoption pattern

Week 1:
- 2-5 evidence records
- 1-2 clear review passes
- 1 small durable fix
- at most 1 candidate if clearly justified

Week 2:
- review recurrence
- split or reject weak candidates if needed
- only then consider heavier durable artifacts

## Common mistakes

- promoting one-off incidents into permanent rules
- treating fluent text as proof of execution
- treating symptom overlap as proof of same-pattern
- skipping rollback planning
- adding a heavy artifact when a checklist would solve it

## Rule of thumb

If the system feels heavy, you are probably promoting too much too early.

The point of `fastslow-evo` is not to make agent evolution look impressive.
It is to make it fast where it should be fast, and slow where it must be slow.
