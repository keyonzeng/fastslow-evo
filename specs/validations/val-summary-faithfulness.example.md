# Validation Spec: val-summary-faithfulness

## Target
Summaries must stay faithful to source material and remain short enough to be useful.

## Preconditions
- Source text, notes, or transcript is available
- Summary can be compared against source evidence

## Test Inputs
- meeting transcript or notes
- lecture notes
- article or reading excerpt

## Procedure
1. Compare the summary against the source.
2. Check whether key decisions, actions, and constraints are preserved.
3. Flag invented facts, omitted critical points, and misleading compression.
4. Check whether the output length is usable for the target context.

## Pass Criteria
- no invented facts
- no loss of critical action or decision items
- concise enough to review quickly

## Fail Signals
- fabricated details
- missing crucial actions, dates, or decisions
- summary too long to reduce workload

## Fallback
Use a structured template with headings and re-run with source-grounded constraints.
