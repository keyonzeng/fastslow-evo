# FastSlow Evo Smoke Test Results

## Summary

The current smoke test run passed strongly.

- Total score: **98/100**
- Average score: **9.8/10**

## Case results

| Case | Expected | Judged | Score | Result |
|---|---|---:|---:|---|
| 01-fast-local-correction | `fast` | `fast` | 10/10 | Pass |
| 02-slow-delivery-discipline | `slow candidate` | `slow candidate` | 10/10 | Pass |
| 03a-observe-tool-overload | `observe` | `observe` | 10/10 | Pass |
| 03b-slow-tool-overload-convergence | `slow candidate` | `slow candidate` | 10/10 | Pass |
| 04-context-drift-pattern | `observe` or `slow candidate` | `slow candidate` | 9/10 | Pass |
| 05-boundary-memory-write | repeated pattern should move toward `slow candidate` | `slow candidate` | 10/10 | Pass |
| 06-slow-function-call-failures | `slow candidate` | `slow candidate` | 10/10 | Pass |
| 07-reject-weak-candidate | `reject` or split | `reject` | 10/10 | Pass |
| 08-heartbeat-candidate-spam | update existing candidate; weak items `observe`/`ignore` | same | 9/10 | Pass |
| 09-structure-not-prompt | `slow candidate` | `slow candidate` | 10/10 | Pass |
| 10-validation-gate-needed | `slow candidate` | `slow candidate` | 10/10 | Pass |

## Strongest areas

- clear routing across `fast`, `slow candidate`, `observe`, `ignore`, and `reject`
- strong resistance to over-promotion from one correction or one file
- good semantic sameness judgment instead of keyword overlap
- good heartbeat discipline: reviewer, not mutation engine
- good validation / rollback instinct for slow promotion
- correct handling of boundary and memory risk as higher-stakes issues

## Weakest areas found during the run

1. Reading-order guidance had small inconsistencies around whether `openclaw-judgment-first.md` was default-first or optional.
2. Heartbeat mixed-output cases deserved a more explicit worked example.
3. Context-drift cases deserved a worked example to reduce route ambiguity.
4. Historical route spelling still needed normalization toward `slow candidate`.

## Follow-up fixes applied after this run

The repository was updated to address those findings:
- normalized reading order so branch protocol files come first on the default runtime path
- made `openclaw-judgment-first.md` explicitly optional in minimal workflow guidance
- added `references/examples/example-heartbeat-mixed-review.md`
- added `references/examples/example-context-drift.md`
- normalized `slow candidate` spelling in minimal runtime workflow

## Overall evaluation

`fastslow-evo` passed this smoke suite as a strong runtime judgment skill.
Its main remaining work is packaging/release polish, not core routing quality.
