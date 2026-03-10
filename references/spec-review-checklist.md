# Spec Review Checklist

Use this before approving a spec delta or promotion.

## Evidence
- Is there at least one concrete triggering case?
- Is the primary gap type named correctly?
- Are we solving the root gap, not just the visible symptom?

## Spec Quality
- Is the delta specific?
- Is it testable?
- Is it smaller than a full framework rewrite?
- Does it avoid copying raw incident language into durable policy?

## Validation
- Is there an explicit validation path?
- Does success mean more than “the file exists” or “the model said so”?
- Are partial success and failure both defined?

## Materialization
- Is this the lightest artifact that can prevent recurrence?
- Would a note, checklist, or template be enough?
- If this becomes a script or skill, is recurrence actually proven?

## Regression
- Could this broaden scope unintentionally?
- Could this create false confidence?
- Could it increase token/cost/runtime burden noticeably?
- Could it worsen safety or privacy posture?

## Governance
- Is the required review level correct?
- Is rollback practical?
- Is the target path explicit?
- Is the change traceable back to evidence?

## Final Gate
Only approve if the delta is:
- evidence-backed
- validated
- proportionate
- reviewable
- reversible
