# FastSlow Heartbeat Protocol

This protocol defines how heartbeat-style FastSlow review should work in OpenClaw.

## Purpose

Heartbeat is a review pass, not an autonomous mutator.
Its job is to inspect recent evidence and current candidates, then recommend the smallest justified next move.

## Core Rule

Heartbeat does not get to promote by default.
Heartbeat reviews, compares, nominates, updates, or stays quiet.

## Default Review Order

1. Read recent evidence.
2. Read current candidates.
3. Judge whether any evidence belongs to an existing candidate.
4. Judge whether any candidate should be split, updated, superseded, rejected, or left alone.
5. Decide whether there is any meaningful fastslow output worth writing now.
6. If not, stay quiet.

## What Heartbeat Should Evaluate

- repeated incidents
- repeated corrections
- repeated wins
- whether a tiny fix reduced recurrence
- whether a candidate is converging or over-merging
- whether any candidate lacks enough support and should be rejected or observed

## Allowed Outputs

- no-action
- update existing candidate
- create one candidate
- split candidate
- reject candidate
- nominate slow promotion for review

## Forbidden Behaviors

- writing many timestamp-based candidates from the same pattern
- treating file count as recurrence proof
- using keyword overlap as the main dedup rule
- silently hardening raw evidence into durable policy

## Heartbeat Success Criterion

A good heartbeat run produces one of two outcomes:
- a small number of explainable review actions
- or no action at all

If heartbeat produces lots of new objects without better judgment, it is failing.
