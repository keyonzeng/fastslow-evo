# Validation Spec: val-study-grounding

## Target
Study outputs should improve understanding and recall, not just produce a polished summary.

## Preconditions
- source material exists
- learner goal is known

## Test Inputs
- lecture transcript
- chapter notes
- article or paper excerpt

## Procedure
1. Check whether the output distinguishes source facts from explanation.
2. Generate or review active-recall prompts, not just passive notes.
3. Verify that key terms and concepts remain grounded in the source.
4. Ask whether the learner could answer questions without rereading the summary.

## Pass Criteria
- output supports recall, not just recognition
- explanations stay grounded in source material
- active-recall prompts or self-test items are present

## Fail Signals
- passive summary only
- unsupported explanation or invented detail
- learner cannot self-test from the output

## Fallback
Convert the summary into quiz questions, flash prompts, or “explain in your own words” prompts.
