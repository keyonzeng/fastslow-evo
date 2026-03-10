# Gap Taxonomy

Use one primary gap type per incident.

## capability_gap
The agent lacks a needed durable capability.

Example:
Cannot consistently render Chinese SVG to PNG.

## behavior_gap
The agent chooses the wrong action despite having the tools.

Example:
Speaks too often in group chats.

## validation_gap
A task appears done, but there is no reliable way to verify correctness.

Example:
File generated successfully, but final Chinese rendering was never checked.

## retrieval_gap
Useful prior knowledge existed but was not found or reused.

Example:
A prior font workaround existed but was not consulted.

## workflow_gap
The steps are not standardized, so quality depends on luck.

Example:
Different handling each time for the same export problem.

## safety_gap
The current path risks data leakage, destructive edits, or overreach.

Example:
Autonomous self-modification proposed in a production environment.

## tooling_gap
The current tools or setup do not support the needed result reliably.

Example:
Rasterizer lacks CJK font support.

## scope_gap
The task was attempted despite being out of current capability boundary.

Example:
Agent implied guaranteed OCR quality without validation path.

## Classification Rules

1. Pick the first cause, not the final symptom.
2. If verification is missing, prefer `validation_gap`.
3. If the agent knew but did not retrieve, prefer `retrieval_gap`.
4. If the process is inconsistent, prefer `workflow_gap`.
5. If the action should not have been attempted as-is, consider `scope_gap` or `safety_gap`.
