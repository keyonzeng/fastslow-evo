# Capability Spec: cap-memory-policy

## Summary
The agent maintains useful cross-session memory without treating the prompt window as memory and without persisting low-confidence or untrusted content as durable truth.

## In Scope
- Distinguishing working, episodic, semantic, and procedural memory
- Persisting stable facts, durable preferences, validated lessons, and reusable patterns
- Expiring or deprioritizing stale transient context

## Out of Scope
- Storing every conversation turn forever
- Treating unverified external content as durable memory
- Guaranteeing perfect recall of all past context

## Preconditions
- Memory write path exists
- Memory entries support source/provenance metadata
- Retrieval path can rank by relevance and freshness

## Known Failure Modes
- important tool evidence omitted from memory
- stale preferences override current instructions
- over-storage degrades retrieval quality
- poisoned or untrusted memory persists across sessions

## Success Definition
- useful prior context is retrieved when relevant
- noisy or stale context does not dominate decisions
- durable memory writes are traceable and reviewable

## Validation Refs
- validations/val-memory-retrieval-quality.example.md
- validations/val-memory-ingestion-safety.example.md
