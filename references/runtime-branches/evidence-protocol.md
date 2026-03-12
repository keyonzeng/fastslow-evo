# FastSlow Evidence Protocol

This protocol defines how FastSlow evidence should be written and how the OpenClaw host model should read it.

The purpose of evidence is not to pre-classify reality.
The purpose is to preserve enough context for later semantic judgment.

## Core Rule

Evidence is raw review material.
It is not already a pattern.
It is not already a candidate.
It is not already approved learning.

## What Every Evidence Record Should Preserve

### 1. Summary
A short plain-language summary of what seemed to happen.
This is only an entry point, not the whole truth.

### 2. Source
Where the signal came from:
- user
- runtime
- tool
- review
- external content
- system

### 3. Context
A short situational explanation.
Enough to orient review quickly.

### 4. Full Context
Preserve the details needed for model judgment, such as:
- task goal
- user intent
- surrounding dialogue
- prior agent behavior
- tool outputs
- environmental constraints
- what the user actually reacted to

### 5. Raw Signal
Preserve the original wording or the closest faithful excerpt.
Do not over-compress it.
Differences in wording may matter for later merge or split decisions.

### 6. Notes
Keep only lightweight metadata, such as:
- tentative gap label
- recurrence hint
- created_at

These notes are hints, not final truth.

## What Evidence Must Not Pretend To Know

Evidence should not pretend to know:
- the final underlying pattern
- whether it definitely matches earlier records
- whether promotion is warranted
- whether the correct next state is already settled

Those are review judgments for the host model.

## Evidence Review Questions For OpenClaw

When reading an evidence file, the host model should ask:
1. What actually happened?
2. What part is concrete versus inferred?
3. Is the context sufficient to judge the issue well?
4. Is this likely reusable, or mostly noise?
5. Does this look like the same underlying pattern as prior evidence?
6. What should happen next: fast, slow candidate, observe, ignore, or reject?

## Evidence Writing Principle

Preserve enough context to enable later judgment.
Do not force judgment too early.

That is the whole discipline.
