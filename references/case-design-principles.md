# Case Design Principles

Use these rules when creating examples or starter cases for this skill.

## 1. Prefer platform-agnostic pain points

Choose cases that show up across ecosystems:
- tool execution drift
- memory poisoning
- retrieval failure
- weak termination
- plan/order failure
- response unfaithfulness

Do not overfit to one product unless the mechanism generalizes.

## 2. Prefer cases with visible user pain

A good case should hurt in a way users immediately feel:
- wrong answer after apparent success
- repeated need to restate context
- runaway spend/time
- unsafe or embarrassing action
- agent says it did something it never did

## 3. Prefer cases with clear evidence artifacts

A good case should have inspectable evidence such as:
- missing tool records
- contradictory output
- repeated retries
- poisoned memory entry
- unbounded call chain

## 4. Prefer cases that produce reusable specs

A case is good only if it can generate:
- one capability spec
- one behavior spec
- one validation spec
- one evolution rule
- one materialization decision

## 5. Prefer cases with a smallest durable fix

Do not choose cases that force a giant framework response if a checklist or validation spec would solve it.

## 6. Ensure broad user relevance

Starter cases should map to common agent-builder concerns:
- support agents
- workflow agents
- coding agents
- research agents
- internal ops agents

## 7. Make failure and success both concrete

Each case must define:
- what failure looks like
- what evidence proves failure
- what success looks like
- what evidence proves success
