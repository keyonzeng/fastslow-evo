# FastSlow Evo

> **EN**: A dual-loop self-evolution system for AI agents.  
> **中文**：一个面向 AI Agent 的双环自我进化系统。

FastSlow Evo helps agents improve in the right way at the right speed:

- **Fast loop / 快环**: fix local, repeated mistakes immediately / 快速修正局部、重复出现的问题
- **Slow loop / 慢环**: promote proven improvements into durable capability / 将经过验证的改进晋升为长期能力

Instead of turning every failure into a big framework rewrite—or leaving every good fix trapped as a local hack—FastSlow Evo routes experience through two loops:

```text
FAST LOOP: observe -> classify -> tiny fix -> reuse
SLOW LOOP: validate -> promote -> standardize -> measure
```

---

## 1. What is FastSlow Evo? / FastSlow Evo 是什么？

**EN**  
FastSlow Evo is a dual-loop self-evolution system. Its job is simple:
- fix local repeated mistakes quickly
- promote only proven fixes slowly
- keep turning local experience into durable capability

**中文**  
FastSlow Evo 是一个双环自我进化系统，核心任务很简单：
- 快速修正局部、重复出现的问题
- 只把经过验证的修复慢速晋升
- 持续把局部经验转化为长期能力

---

## 2. Why this exists / 为什么会有这个项目？

**EN**  
Most “self-improving agent” systems get one piece right but miss the whole:
- some log incidents but never turn them into capability
- some keep memory but do not know what deserves promotion
- some reflect but never produce reusable artifacts
- some jump too quickly into unsafe self-modification

FastSlow Evo focuses on one harder and more useful question:

> **What should be fixed quickly, and what should be promoted slowly?**

**中文**  
大多数“自我改进 agent”系统只做对了一部分：
- 有些只会记录问题，却不会沉淀成能力
- 有些有记忆，却不知道什么值得晋升
- 有些会反思，却产不出可复用的工件
- 有些又太快走向不安全的自我修改

FastSlow Evo 聚焦一个更难但也更有价值的问题：

> **什么应该快速修正，什么必须慢速晋升？**

---

## 3. Core idea / 核心思想

### Fast loop — Quick Adapt / 快环：快速适应

**Use when / 适用场景：**
- local / 局部问题
- frequent / 高频问题
- low-blast-radius / 影响面小
- easy to verify next time / 下一次就容易验证

**Typical outputs / 常见产物：**
- checklist / 检查清单
- template tweak / 模板微调
- memory rule / 记忆规则
- tiny validation rule / 小型校验规则
- tiny script / 小脚本

### Slow loop — Slow Promote / 慢环：慢速晋升

**Use when / 适用场景：**
- a local fix has proven useful / 局部修复已被证明有效
- the pattern recurs across tasks / 问题跨任务重复出现
- broader behavior or capability is affected / 影响更广泛的行为或能力边界

**Typical outputs / 常见产物：**
- capability spec / 能力规范
- behavior spec / 行为规范
- validation spec / 验证规范
- evolution rule / 晋升规则
- workflow rule / 工作流规则
- reusable skill or script / 可复用 skill 或脚本

---

## 4. What FastSlow Evo is good for / 它适合解决什么问题？

### EN
For agent builders and power users:
- reduce repeated mistakes without overreacting
- decide when a tiny fix should stay local vs become durable
- build safer self-improvement loops
- turn corrections and repeated work into reusable assets

For office / study workflows:
- improve summaries, follow-ups, and action extraction
- prevent polished but untrustworthy output
- improve note workflows and active recall
- create fast visible wins before introducing heavier automation

### 中文
对 agent builder 和重度用户：
- 减少重复错误，但不过度反应
- 判断小修补该留在本地，还是升级为长期能力
- 建立更安全的自我进化闭环
- 把纠正和重复工作转化为可复用资产

对办公 / 学习场景：
- 优化摘要、跟进、行动项提取
- 避免“看起来很像回事但不可信”的输出
- 改善笔记和主动回忆流程
- 先创造立刻可见的小收益，再引入更重的自动化

---

## 5. What is included / 仓库包含什么？

- **Quick Adapt** workflow / 快速适应工作流
- **Slow Promote** workflow / 慢速晋升工作流
- **Fast/Slow Router** / 快慢环判断路由
- **Incident / correction / win templates** / 事件、纠正、成功模板
- **Starter guides and demos** / 启动指南与示例
- **Validation examples** / 验证规范示例
- **Scripts** to initialize a spec tree, capture incidents, draft proposals, and recommend materialization / 初始化结构、记录问题、生成提案和推荐落地形式的脚本

---

## 6. Directory overview / 目录结构

```text
fastslow-evo/
├── SKILL.md
├── README.md
├── assets/
├── references/
├── scripts/
└── specs/
```

---

## 7. Quick start / 快速开始

### EN
Read:
- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/fast-slow-router.md`

Then run one real issue through the fast loop.

### 中文
建议先读：
- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/fast-slow-router.md`

然后拿一个真实问题，先跑一遍快环。

---

## 8. Example workflow / 示例流程

### EN
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

### 中文
1. 抓一个真实问题  
   例如：会议摘要漏掉了 action item。
2. 路由判断  
   如果它是局部、高频、低风险、下次容易验证的问题 → 走 **Quick Adapt**。
3. 应用最小修复  
   例如：增加 action-review checklist、收紧摘要模板、补一个小型验证规则。
4. 复用  
   如果后面几次摘要明显变好，就保留。
5. 必要时慢速晋升  
   如果这个模式跨上下文重复出现，且验证通过，再慢慢晋升。

---

## 9. Scripts / 脚本

### Initialize working structure / 初始化工作结构
```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

### Record a gap / incident / 记录问题或事件
```bash
python3 scripts/new_gap_entry.py "agent claimed tool success without evidence" --gap validation_gap --source review --task "automation run" --out ./my-agent-specs/evidence/incidents
```

### Draft a promotion proposal / 生成晋升提案
```bash
python3 scripts/build_evolution_proposal.py "tool-faithfulness-hardening" --gap validation_gap --cases 2 --recurrence 2 --spec-type validation --artifact checklist --review L1 --out ./my-agent-specs/proposals
```

### Recommend materialization / 推荐落地形式
```bash
python3 scripts/recommend_materialization.py --gap validation_gap --recurrence 2 --risk medium
```

---

## 10. Best fit / 最适合谁？

**EN**  
FastSlow Evo is broadly portable, but especially well suited to environments where agents have:
- repeated usage
- persistent context
- clear correction signals
- recurring workflows
- room to evolve without losing safety

**中文**  
FastSlow Evo 具有一定可移植性，但尤其适合这类环境：
- agent 被反复使用
- 有持续上下文
- 用户纠正信号明确
- 存在重复工作流
- 需要在不失控的前提下持续进化

---

## 11. What it is not / 它不是什么

FastSlow Evo is **not / 不是**：
- a full autonomous self-modification engine / 全自动自我修改引擎
- a generic office productivity wrapper / 泛化办公 productivity 包装器
- a vague reflection system with no artifacts / 没有产物的空泛反思系统
- a justification for turning every annoyance into a new skill / 把每个烦恼都升级成 skill 的借口

---

## 12. Philosophy / 核心哲学

> **Fast where local adaptation is enough. Slow where durable promotion must be earned.**
>
> **局部适应足够时就快，长期晋升必须被证明时就慢。**

That is the whole system.  
这就是整套系统的核心。

---

## 13. Suggested GitHub topics / 建议 GitHub Topics

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

## 14. License / 许可证

Pick a license before publishing.  
发布前请选定许可证。

**Recommended / 建议：MIT**
