# Starter Packs

Use these as practical entry points so users do not have to design a whole spec system from scratch.

## 1. Coding Agent Starter

Prioritize:
- phantom tool success
- bounded execution
- plan-before-act
- validation of final answer against tool/output evidence

Recommended initial artifacts:
- `cap-tool-execution-proof.example.md`
- `beh-bounded-execution.example.md`
- `val-tool-faithfulness.example.md`
- `val-execution-proof.example.md`
- `evo-promotion-thresholds.example.md`

## 2. Workflow Automation Agent Starter

Prioritize:
- plan-before-act
- side-effect ordering
- weak termination
- execution proof for sends/updates/deletes

Recommended initial artifacts:
- `cap-plan-before-act.example.md`
- `val-plan-before-act.example.md`
- `beh-bounded-execution.example.md`
- `cap-tool-execution-proof.example.md`

## 3. Support / Concierge Agent Starter

Prioritize:
- memory policy
- memory ingestion safety
- response faithfulness
- scope boundaries

Recommended initial artifacts:
- `cap-memory-policy.example.md`
- `beh-memory-ingestion-safety.example.md`
- `val-memory-ingestion-safety.example.md`
- `val-tool-faithfulness.example.md`

## 4. Research Agent Starter

Prioritize:
- source faithfulness
- retrieval quality
- citation discipline
- memory boundaries between evidence and inference

Recommended initial artifacts:
- `cap-memory-policy.example.md`
- `val-tool-faithfulness.example.md`
- `val-memory-ingestion-safety.example.md`
- `mat-smallest-durable-fix.example.md`

## Rule

A starter pack is successful if a user can adopt 3-5 artifacts immediately without redesigning the whole framework.
