# Spec Model

This skill uses five spec layers.

## 1. Capability Spec

Purpose:
Define what the agent can do reliably, with boundaries and prerequisites.

Fields:
- capability_id
- summary
- in_scope
- out_of_scope
- prerequisites
- known_failure_modes
- success_definition
- validation_refs

## 2. Behavior Spec

Purpose:
Define how the agent should choose actions in recurring contexts.

Fields:
- behavior_id
- context
- trigger
- required_actions
- forbidden_actions
- escalation_rule
- examples

## 3. Validation Spec

Purpose:
Define how success is checked.

Fields:
- validation_id
- target
- preconditions
- test_inputs
- procedure
- pass_criteria
- fail_signals
- fallback

## 4. Evolution Spec

Purpose:
Define when and how specs are allowed to change.

Fields:
- evolution_id
- eligible_signals
- minimum_evidence
- required_review_level
- allowed_targets
- forbidden_targets
- rollback_requirement

## 5. Materialization Spec

Purpose:
Map an approved spec delta to the correct artifact.

Fields:
- materialization_id
- source_delta
- chosen_form
- target_paths
- rationale
- validation_needed
- rollback_method

## Design Rule

Spec files should stay concise.

- capability specs define promise and boundaries
- behavior specs define decision policy
- validation specs define checks
- evolution specs define governance
- materialization specs define landing path

Do not overload one spec file with all five responsibilities.
