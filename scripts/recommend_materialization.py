#!/usr/bin/env python3
import argparse

ORDER = ["evidence-note", "curated-memory", "checklist", "template", "script", "skill", "code-config-change"]


def recommend(gap: str, recurrence: int, risk: str, cross_project: bool, deterministic: bool):
    if risk == "high":
        if gap in {"safety_gap", "scope_gap"}:
            return "checklist", "High-risk gaps should default to bounded guidance or validation before heavier automation."
        return "curated-memory", "High risk with uncertain blast radius should start as reviewed durable guidance."

    if gap == "validation_gap":
        if recurrence >= 3 and deterministic:
            return "script", "Repeated validation failures with deterministic checks justify an executable validator or helper script."
        return "checklist", "Validation gaps usually improve first through explicit checks and claim-vs-evidence review."

    if gap == "retrieval_gap":
        return "curated-memory", "Retrieval gaps usually mean the right knowledge exists but is not stably surfaced."

    if gap == "workflow_gap":
        if recurrence >= 3 and deterministic:
            return "script", "A repeated deterministic workflow is a good candidate for scripting."
        if recurrence >= 2:
            return "checklist", "Workflow inconsistency usually hardens first as a checklist or ordered template."
        return "evidence-note", "One-off workflow issues should stay lightweight until recurrence is proven."

    if gap == "behavior_gap":
        if recurrence >= 2:
            return "checklist", "Behavior gaps usually improve through explicit decision rules before heavier packaging."
        return "curated-memory", "A first behavior miss is often best captured as durable guidance."

    if gap == "tooling_gap":
        if deterministic and recurrence >= 2:
            return "script", "Tooling gaps with stable transformations usually benefit from executable helpers."
        return "template", "Tooling gaps often benefit from a stable reusable setup or invocation template."

    if gap == "capability_gap":
        if cross_project and recurrence >= 3:
            return "skill", "Cross-project recurring capability gaps justify a reusable skill."
        if deterministic and recurrence >= 3:
            return "script", "Recurring deterministic capability gaps often become scripts before full skills."
        return "template", "Capability gaps should usually mature through a reusable pattern before full packaging."

    if gap == "safety_gap":
        return "checklist", "Safety gaps should harden behavior and review paths before heavier implementation changes."

    if gap == "scope_gap":
        return "curated-memory", "Scope gaps usually need stronger boundary rules, not new automation."

    return "evidence-note", "Default to the smallest durable artifact when confidence is low."


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gap", required=True, choices=[
        "capability_gap", "behavior_gap", "validation_gap", "retrieval_gap",
        "workflow_gap", "safety_gap", "tooling_gap", "scope_gap"
    ])
    p.add_argument("--recurrence", type=int, default=1)
    p.add_argument("--risk", choices=["low", "medium", "high"], default="medium")
    p.add_argument("--cross-project", action="store_true")
    p.add_argument("--deterministic", action="store_true")
    args = p.parse_args()

    recommendation, rationale = recommend(args.gap, args.recurrence, args.risk, args.cross_project, args.deterministic)
    print(f"recommendation: {recommendation}")
    print(f"rationale: {rationale}")
    print("promotion-order:", ", ".join(ORDER))


if __name__ == "__main__":
    main()
