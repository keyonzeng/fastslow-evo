# Validation Spec: val-tone-intent-fit

## Target
Drafted workplace writing should match the user's intent, audience, and level of formality without sounding generic or inauthentic.

## Preconditions
- target audience is known
- user intent is explicit
- draft text exists

## Test Inputs
- manager email
- peer follow-up
- customer-facing response

## Procedure
1. State the intended audience and purpose.
2. Check whether tone matches the relationship and context.
3. Remove empty polish, generic filler, or over-formality.
4. Confirm that the actual ask, accountability, and next step remain clear.

## Pass Criteria
- tone fits audience and purpose
- draft sounds accountable, not evasive
- next step is explicit

## Fail Signals
- generic AI-style phrasing
- tone mismatch
- polished but unclear ask
- wording that could reduce trust

## Fallback
Switch to a shorter draft with explicit purpose, ask, and deadline.
