# FastSlow Evo

**A dual-loop self-evolution system for AI agents.**

FastSlow Evo helps agents improve at the right speed:

- **Fast loop** for local, repeated mistakes that should be fixed immediately
- **Slow loop** for proven improvements that deserve promotion into durable capability

Instead of turning every failure into a broad framework rewrite—or leaving every useful fix trapped as a local hack—FastSlow Evo routes experience through two loops:

```text
FAST LOOP: observe -> classify -> tiny fix -> reuse
SLOW LOOP: validate -> promote -> standardize -> measure
```

For the Chinese version, see [README.zh-CN.md](./README.zh-CN.md).

---

## What is FastSlow Evo?

FastSlow Evo is a dual-loop self-evolution system.

Its core is **not** a Python rule engine.
Its core is a **skill-driven judgment layer** that helps the host model decide:
- what deserves a fast local fix
- what deserves slow durable promotion
- what should stay under observation
- what should be ignored as noise

Its job is simple:
- fix local repeated mistakes quickly
- promote only proven fixes slowly
- keep turning local experience into durable capability

---

## Why this exists

Most “self-improving agent” systems get one piece right but miss the whole:
- some log incidents but never turn them into capability
- some keep memory but do not know what deserves promotion
- some reflect but never produce reusable artifacts
- some jump too quickly into unsafe self-modification

FastSlow Evo focuses on one harder and more useful question:

> **What should be fixed quickly, and what should be promoted slowly?**

---

## Core idea

### Fast loop — Quick Adapt

Use when the issue is:
- local
- frequent
- low-blast-radius
- easy to verify in the next task

Typical outputs:
- checklist
- template tweak
- memory rule
- tiny validation rule
- tiny script

### Slow loop — Slow Promote

Use when a local fix has proven useful and may deserve durable promotion.

Typical outputs:
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- reusable skill or script

### Intelligent routing

FastSlow Evo should not rely only on users explicitly saying "use the fast loop" or "use the slow loop".

The host model should infer:
- what deserves a tiny fast fix
- what should stay under observation
- what is mature enough for slow-loop promotion
- what is just noise

### Heartbeat-based promotion monitoring

FastSlow Evo should also use heartbeat-style review to monitor recent fast-loop outputs over time and detect when they are becoming promotion candidates.

That means heartbeat-like review should inspect:
- repeated incidents
- repeated corrections
- repeated wins
- reuse of tiny fixes
- cross-context stability
- regression signals

A validation suite is included so you can test whether this behavior is actually plausible instead of just sounding smart.

## Architecture

FastSlow Evo is designed as:
- **skill / model layer** for semantic judgment
- **references / governance layer** for promotion discipline and review rules
- **scripts / utility layer** for installation, persistence, candidate writing, and fallback tooling

Scripts are helpers, not the primary intelligence.

### When helpers should be used

Use scripts when you need to:
- install or configure the runtime
- persist a signal that has already been judged meaningful
- write a promotion candidate after heartbeat or review
- test or validate the loop mechanically

Do not use scripts as a substitute for semantic judgment.

---

## What FastSlow Evo is good for

### Agent builders and power users
- reduce repeated mistakes without overreacting
- decide when a tiny fix should stay local vs become durable
- build safer self-improvement loops
- turn corrections and repeated work into reusable assets

### Office / study workflows
- improve summaries, follow-ups, and action extraction
- prevent polished but untrustworthy output
- improve note workflows and active recall
- create fast visible wins before introducing heavier automation

---

## What is included

- **Quick Adapt** workflow
- **Slow Promote** workflow
- **Fast/Slow Router**
- **Incident / correction / win templates**
- **Starter guides and demos**
- **Validation examples**
- **Scripts** to initialize a spec tree, capture incidents, draft proposals, and recommend materialization

---

## Directory overview

```text
fastslow-evo/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── assets/
├── references/
├── scripts/
└── specs/
```

---

## Installation

### Option 1 — One-command install for OpenClaw (recommended)

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git && cd fastslow-evo && ./install.sh
```

What it does:
- installs the skill into `~/.openclaw/workspace/skills/fastslow-evo` or confirms it in place
- creates a runtime workspace under `~/.openclaw/workspace/fastslow/`
- copies starter templates for incidents, corrections, wins, proposals, and scorecards
- appends a FastSlow review block to `~/.openclaw/workspace/HEARTBEAT.md`

Then verify:

```bash
openclaw skills info fastslow-evo
```

### Option 2 — Install with `npx skills add`

```bash
npx skills add https://github.com/keyonzeng/fastslow-evo --skill fastslow-evo
```

This is similar to:

```bash
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

### Option 3 — Install from an OpenClaw chat window

In an OpenClaw channel conversation, send:

```text
安装 https://github.com/keyonzeng/fastslow-evo
```

### Option 4 — Manual OpenClaw install

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git ~/.openclaw/workspace/skills/fastslow-evo
```

### Option 5 — Local clone for scripts only

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git my-fastslow-evo
cd my-fastslow-evo
```

> Note: local files alone are not the same as a full OpenClaw install.
---

## Quick start

Read:
- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/fast-slow-router.md`

Then run one real issue through the fast loop.

### 4-line getting-started path

```bash
./install.sh
python3 fastslow.py capture-text "This reply is too formal. Next time make it sound more natural."
python3 fastslow.py route --latest
python3 fastslow.py heartbeat --write-candidates
```

### Unified runtime commands

These commands are **utility helpers**. They are not the core intelligence of FastSlow Evo.
Use them to persist signals, inspect state, and validate behavior.

Capture a real runtime signal:

```bash
python3 fastslow.py capture incident "summary missed action items across two meetings" --gap validation_gap --recurrence 2 --context "meeting summaries"
```

Capture directly from a natural-language correction:

```bash
python3 fastslow.py capture-text "This reply is too formal. Next time make it sound more natural."
```

Route the latest runtime signal:

```bash
python3 fastslow.py route --latest
```

Run heartbeat-style monitoring over runtime evidence:

```bash
python3 fastslow.py heartbeat --write-candidates
```

### One-command setup / chat-style setup

Command line:

```bash
python3 fastslow.py setup
python3 scripts/chat_setup.py "enable fastslow evo heartbeat"
```

Equivalent natural-language chat intent:

```text
配置 FastSlow Evo
启用 FastSlow Evo heartbeat
记住这个修正
以后这种情况这样做
这个问题老是重复
你判断该 fast 还是 slow
```

---

## How to use it in OpenClaw

FastSlow Evo is not a separate app you launch.
It is a skill that gets used when you ask the agent to improve through the fast loop or slow loop.

### The 3 easiest trigger phrases

Use these directly in an OpenClaw chat:

1. **"Run this through the fast loop and give me the smallest fix."**
2. **"This pattern keeps recurring — run the slow loop."**
3. **"You decide whether this should go fast or slow, then execute."**

### Typical fast-loop requests

- "Next time handle this case like this — use the fast loop."
- "This summary missed an action item. Fix it through the fast loop."
- "The tone is too formal. Add a tiny fix through the fast loop."
- "You misread the tool result. Apply the smallest durable fix."

### Typical slow-loop requests

- "This issue has happened several times. Run the slow loop."
- "Promote this repeated fix into a durable rule."
- "This pattern is stable now. Turn it into longer-term capability."

---

## Common use cases

### 1. Meeting summaries miss action items

Say:

```text
This summary missed action items. Run the fast loop and add the smallest fix.
```

Expected result:
- tighter summary template
- action-review checklist
- tiny validation rule

### 2. Replies sound too formal or generic

Say:

```text
This reply is too formal. Use the fast loop so next time it sounds more natural.
```

Expected result:
- tone adjustment
- style memory rule
- smaller writing template tweak

### 3. Tool output was misread

Say:

```text
You misread the tool result. Apply the smallest durable fix through the fast loop.
```

Expected result:
- claim-vs-evidence check
- tiny validation improvement
- safer summary behavior next time

### 4. The same issue keeps happening

Say:

```text
This issue has happened repeatedly. Run the slow loop and promote the fix.
```

Expected result:
- capability / behavior / validation spec
- durable workflow rule
- reusable skill or script candidate

### 5. You are not sure which loop to use

Say:

```text
Use FastSlow Evo to decide whether this should go fast or slow, and then act.
```

Expected result:
- router decision
- either a tiny local fix or a durable promotion path

---

## Example workflow

1. Capture one issue  
   Example: the agent missed an action item in a meeting summary.
2. Route it  
   Local, frequent, low-risk, easy to verify next time? → Use **Quick Adapt**
3. Apply the smallest fix  
   Add an action-review checklist, tighten a summary template, or add a tiny validation rule.
4. Reuse it  
   If the next few summaries improve, keep it.
5. Promote slowly if needed  
   If the pattern recurs across contexts and survives validation, promote it.

---

## Scripts

### Initialize working structure
```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

### Record a gap / incident
```bash
python3 scripts/new_gap_entry.py "agent claimed tool success without evidence" --gap validation_gap --source review --task "automation run" --out ./my-agent-specs/evidence/incidents
```

### Draft a promotion proposal
```bash
python3 scripts/build_evolution_proposal.py "tool-faithfulness-hardening" --gap validation_gap --cases 2 --recurrence 2 --spec-type validation --artifact checklist --review L1 --out ./my-agent-specs/proposals
```

### Recommend materialization
```bash
python3 scripts/recommend_materialization.py --gap validation_gap --recurrence 2 --risk medium
```

---

## Best fit

FastSlow Evo is broadly portable, but especially well suited to environments where agents have:
- repeated usage
- persistent context
- clear correction signals
- recurring workflows
- room to evolve without losing safety

---

## What it is not

FastSlow Evo is **not**:
- a full autonomous self-modification engine
- a generic office productivity wrapper
- a vague reflection system with no artifacts
- a justification for turning every annoyance into a new skill

---

## Philosophy

**Fast where local adaptation is enough. Slow where durable promotion must be earned.**

That is the whole system.

---

## Suggested GitHub topics

- ai-agents
- self-improving-agents
- agent-memory
- agent-workflows
- prompt-engineering
- evaluation
- openclaw
- skill-design
- reflective-systems
- ai-productivity

---

## License

MIT
