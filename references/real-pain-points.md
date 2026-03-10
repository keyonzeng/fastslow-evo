# Real Pain Points for Spec-Driven Evolution

This file distills recurring real-world agent pain points from public discussions, issue trackers, and security writeups into design targets for the skill.

## 1. Tool-call amnesia

Observed repeatedly in production systems:

- some agent memory systems store only user/assistant text, not tool messages
- agent later claims it used a tool when it did not
- positive chat outcomes contaminate future behavior if execution evidence is missing

Representative evidence:

- n8n issue #14361: tool usages not stored in memory, causing the model to repeat success patterns without actual tool execution
- multiple community reports of “hallucinated summaries even after the tool call succeeded” and “agent claiming it called a tool but didn’t”

Design implication:

A self-evolving agent must not treat natural-language success as proof of execution. Tool execution evidence needs its own spec and validation.

## 2. Memory overload, drift, and retrieval failure

Observed repeatedly:

- storing everything hurts quality and increases hallucination
- storing too little causes loops and re-learning
- larger context windows create the illusion of memory without durable state

Representative evidence:

- Oracle developer blog: bigger context windows are not memory; persistent evolving state is required
- Reddit/industry discussions: event-based memory with aggressive TTLs often works better than storing everything
- Microsoft and other surveys: memory retrieval and contextual validation are recurring failure points

Design implication:

Memory needs explicit spec boundaries: what to persist, what to expire, and how to validate retrieval relevance.

## 3. Infinite loops and weak termination

Observed repeatedly:

- agents hang in repair loops or tool loops
- malformed tool JSON and hung tools lead to repeated retries
- subordinate-agent recursion or delegation chains run unbounded

Representative evidence:

- agent-zero issue #1088: no hard stop for monologue/tool loops, missing budgets and guardrails
- related issues on loop repetition, runaway agent creation, and hanging tool interactions

Design implication:

Termination and budget policies must be first-class specs, not incidental implementation details.

## 4. Prompt injection and memory poisoning

Observed repeatedly:

- malicious content in external inputs or long-term memory can redirect future behavior
- threat is persistent and often silent across sessions
- prompt injection in agentic systems can cascade across tools and workflows

Representative evidence:

- Microsoft taxonomy and case study: corrupted agent memory can become a pivot point for data exfiltration
- Lakera: memory poisoning and long-horizon goal hijacks persist across sessions and workflows
- industry writeups and OWASP guidance consistently rank prompt injection and poisoning as top threats

Design implication:

Memory, retrieved content, and external tool output must be treated as untrusted until validated.

## 5. Tool hallucination and response inconsistency

Observed repeatedly:

- agent gets correct tool output but answers with contradictory content
- user sees a fluent but false final response
- verification often focuses on “was there a tool call?” but not “did the answer stay faithful to the tool?”

Representative evidence:

- awesome-agent-failures catalog: response hallucination and incorrect tool use are common production failure modes
- community complaints highlight hallucinated summaries after valid tool execution

Design implication:

Validation needs to cover both execution correctness and final-response faithfulness.

## 6. Goal misinterpretation and planning failures

Observed repeatedly:

- agent optimizes for the wrong user objective
- steps are executed in the wrong order
- partial completion is mistaken for success

Representative evidence:

- awesome-agent-failures catalog: goal misinterpretation, plan-generation failures, verification/termination failures

Design implication:

Capability evolution must include behavior and planning specs, not just memory or tooling specs.

## 7. Security and reliability are entangled

Observed repeatedly:

- a small tool mistake or injected content can trigger larger multi-step failures
- memory, tooling, planning, and autonomy amplify each other

Representative evidence:

- Microsoft taxonomy: failure modes need to be framed across both safety and security
- security coverage in 2025-2026 increasingly treats agent systems as high-blast-radius execution surfaces

Design implication:

Spec-driven evolution should always evaluate both utility gain and blast-radius increase.

## Bottom Line

The most useful real-world cases for this skill are not toy examples. They are recurring pain patterns where:

- the agent appears successful without verified execution
- memory becomes either too weak or too sticky
- autonomy outruns guardrails
- natural language hides broken state transitions
- safety and reliability fail together
