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

FastSlow Evo is a dual-loop self-evolution system. Its job is simple:
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

### Option 1 — Install with `npx skills add`

If you use the Skills installer flow, install from GitHub like this:

```bash
npx skills add https://github.com/keyonzeng/fastslow-evo --skill fastslow-evo
```

This is similar to:

```bash
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

### Option 2 — Install from an OpenClaw chat window

In an OpenClaw channel conversation, send:

```text
安装 https://github.com/keyonzeng/fastslow-evo
```

If your OpenClaw setup supports skill installation from chat, this is the most natural path.

### Option 3 — Manual OpenClaw install

If you prefer manual installation, clone the repo into an OpenClaw skill directory:

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git ~/.openclaw/skills/fastslow-evo
```

Or place it in your workspace skill directory:

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git ~/.openclaw/workspace/skills/fastslow-evo
```

Then verify:

```bash
openclaw skills info fastslow-evo
```

### Option 4 — Local clone for scripts only

If you only want the files and scripts locally:

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git my-fastslow-evo
cd my-fastslow-evo
```

Then run the included scripts directly:

```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

> Note: using the files locally is not the same as installing the skill into OpenClaw.
---

## Quick start

Read:
- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/fast-slow-router.md`

Then run one real issue through the fast loop.

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
