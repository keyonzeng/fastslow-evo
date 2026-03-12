# FastSlow Minimal Usable Workflow

This is the default usable workflow for FastSlow Evo in OpenClaw.

If you want FastSlow to be useful immediately, do this and nothing more.

## Case 1: A new correction / incident appears

### Step 1
Write one evidence markdown file.
Use the evidence template and preserve:
- summary
- source
- context
- full context
- raw signal
- notes

### Step 2
Read in this order:
1. `references/runtime-branches/evidence-protocol.md`
2. `references/runtime-core/review-protocol.md`
3. `references/runtime-core/evaluation-rubric.md`
4. the new evidence file
5. existing candidates only if sameness is in question
6. `references/runtime-core/review-output-format.md`

Optional: read `references/runtime-optional/openclaw-judgment-first.md` only if you need the broader OpenClaw stance.

### Step 3
Have the OpenClaw host model produce a review result.
Possible states:
- fast
- slow candidate
- observe
- ignore
- reject

### Step 4
Apply the smallest justified next step:
- fast -> local checklist / template / memory rule
- slow candidate -> create or update one candidate markdown file
- observe -> keep evidence only
- ignore -> no further write
- reject -> close or correct a weak candidate

## Case 2: Candidate review

### Step 1
Read in this order:
1. `references/runtime-branches/candidate-protocol.md`
2. `references/runtime-core/review-protocol.md`
3. `references/runtime-core/evaluation-rubric.md`
4. `references/runtime-branches/candidate-review-checklist.md`
5. linked evidence files
6. candidate file
7. `references/runtime-core/review-output-format.md`

Optional: read `references/runtime-optional/openclaw-judgment-first.md` only if you need the broader OpenClaw stance.

### Step 2
Decide one convergence action:
- merge-into-existing-candidate
- keep-separate
- split-candidate
- supersede-candidate
- create-new-candidate
- no-action

### Step 3
Decide one state:
- fast
- slow candidate
- observe
- ignore
- reject

## Case 3: Heartbeat review

Read:
1. `references/runtime-branches/heartbeat-protocol.md`
2. `references/runtime-core/review-protocol.md`
3. `references/runtime-core/evaluation-rubric.md`
4. recent evidence
5. current candidates
6. `references/runtime-core/review-output-format.md`

Optional: read `references/runtime-optional/openclaw-judgment-first.md` only if you need the broader OpenClaw stance.

Allowed outputs:
- no-action
- update existing candidate
- create one candidate
- split candidate
- reject candidate

## Default Rule

If you are about to let any mechanical layer decide pattern sameness or candidate convergence, stop.
That judgment belongs to the OpenClaw host model.
