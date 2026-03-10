# Capability Spec: cap-tool-execution-proof

## Summary
The agent can distinguish between requested actions, attempted tool calls, successful tool execution, partial execution, and non-execution, and it will not present non-execution as completed work.

## In Scope
- Capturing tool invocation evidence
- Distinguishing execution states
- Surfacing uncertainty when evidence is partial
- Requiring execution proof before claiming completion

## Out of Scope
- Guaranteeing tool correctness in every external system
- Treating natural-language confidence as execution proof
- Hiding partial or failed execution behind fluent summaries

## Preconditions
- Tool layer emits inspectable call/result metadata
- Response generation can access execution evidence
- Validation path exists for execution-vs-claim checks

## Known Failure Modes
- tool was never called
- tool call failed but response implies success
- tool result exists but summary contradicts it
- tool evidence missing from stored memory

## Success Definition
- completion claims are evidence-backed
- failed or partial execution is surfaced explicitly
- missing evidence blocks strong completion claims

## Validation Refs
- validations/val-tool-faithfulness.example.md
- validations/val-execution-proof.example.md
