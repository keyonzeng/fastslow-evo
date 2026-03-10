# FastSlow Evo

**一个面向 AI Agent 的双环自我进化系统。**

FastSlow Evo 帮助 Agent 用正确的速度进化：

- **快环**：快速修正局部、重复出现的问题
- **慢环**：把经过验证的改进晋升为长期能力

它既避免把每次失败都升级成大而重的规则系统，也避免把每次有效修复都困在本地 hack 里。

```text
FAST LOOP: observe -> classify -> tiny fix -> reuse
SLOW LOOP: validate -> promote -> standardize -> measure
```

英文版请看 [README.md](./README.md)。

---

## FastSlow Evo 是什么？

FastSlow Evo 是一个双环自我进化系统，核心任务很简单：
- 快速修正局部、重复出现的问题
- 只把经过验证的修复慢速晋升
- 持续把局部经验转化为长期能力

---

## 为什么要做这个项目？

大多数“自我改进 agent”系统只做对了一部分：
- 有些只会记录问题，却不会沉淀成能力
- 有些有记忆，却不知道什么值得晋升
- 有些会反思，却产不出可复用工件
- 有些又太快走向不安全的自我修改

FastSlow Evo 聚焦一个更有价值的问题：

> **什么应该快速修正，什么必须慢速晋升？**

---

## 核心思想

### 快环 — Quick Adapt

适用于：
- 局部问题
- 高频问题
- 影响面小
- 下一次就容易验证

常见产物：
- checklist
- 模板微调
- memory rule
- 小型验证规则
- 小脚本

### 慢环 — Slow Promote

适用于：
- 某个局部修复已经被证明有效
- 同类模式跨任务重复出现
- 涉及更广泛的行为、能力或工作流边界

常见产物：
- capability spec
- behavior spec
- validation spec
- evolution rule
- workflow rule
- 可复用 skill 或脚本

### 智能判断

FastSlow Evo 不应该只依赖用户显式说“走 fast loop”或“走 slow loop”。

它应该默认具备判断能力：
- 什么只值得一个 tiny fast fix
- 什么应该继续观察
- 什么已经成熟到值得进入 slow loop
- 什么其实只是噪音

### 基于 heartbeat 的晋升监控

FastSlow Evo 还应该持续监控 fast loop 的产物，看它们是否正在成熟为 promote 候选。

也就是 heartbeat 不只看消息或任务，还应该看：
- 重复 incident
- 重复 correction
- 重复 win
- tiny fix 的复用情况
- 跨场景稳定性
- regression 信号

仓库里现在已经附带了 validation suite，用来验证这些判断是不是靠谱，而不是只会说概念。

---

## 它适合解决什么问题？

### 对 Agent Builder 和重度用户
- 减少重复错误，但不过度反应
- 判断小修补该留在本地，还是升级为长期能力
- 建立更安全的自我进化闭环
- 把纠正和重复工作转化为可复用资产

### 对办公 / 学习场景
- 优化摘要、跟进、行动项提取
- 避免“看起来很像回事但不可信”的输出
- 改善笔记和主动回忆流程
- 先创造立刻可见的小收益，再引入更重的自动化

---

## 仓库包含什么？

- **Quick Adapt** 工作流
- **Slow Promote** 工作流
- **Fast/Slow Router**
- **incident / correction / win 模板**
- **starter guides 和 demo**
- **validation 示例**
- **脚本**：初始化 spec 树、记录问题、生成提案、推荐落地形式

---

## 目录结构

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

## 安装方式

### 方式 1 —— 用 `npx skills add` 安装

如果你走 Skills 安装流，建议直接这样装：

```bash
npx skills add https://github.com/keyonzeng/fastslow-evo --skill fastslow-evo
```

它和下面这种写法是同一路子：

```bash
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

### 方式 2 —— 在 OpenClaw 对话窗口直接安装

如果你的 OpenClaw 支持在聊天里安装 skill，直接发这句话：

```text
安装 https://github.com/keyonzeng/fastslow-evo
```

这是最自然、最傻瓜的路径。

### 方式 3 —— 手动安装到 OpenClaw

如果你想手动装，把仓库 clone 到 OpenClaw skill 目录：

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git ~/.openclaw/skills/fastslow-evo
```

或者放到 workspace skill 目录：

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git ~/.openclaw/workspace/skills/fastslow-evo
```

然后验证：

```bash
openclaw skills info fastslow-evo
```

同时它还会准备好 FastSlow runtime 目录，并把 FastSlow 的 review block 追加到 `~/.openclaw/workspace/HEARTBEAT.md`。

### 方式 4 —— 只在本地拿文件和脚本

如果你只是想先拿到文件和脚本：

```bash
git clone https://github.com/keyonzeng/fastslow-evo.git my-fastslow-evo
cd my-fastslow-evo
```

然后直接使用里面的脚本：

```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

> 注意：只把文件 clone 到本地，不等于已经安装成 OpenClaw skill。
---

## 快速开始

建议先读：
- `references/one-page-start.md`
- `references/quick-adapt.md`
- `references/fast-slow-router.md`

然后拿一个真实问题，先跑一遍快环。

### Runtime 命令

记录一个真实运行信号：

```bash
python3 scripts/capture_runtime.py incident "summary missed action items across two meetings" --gap validation_gap --recurrence 2 --context "meeting summaries"
```

对最新 runtime 信号做路由判断：

```bash
python3 scripts/route_runtime.py --latest
```

运行 heartbeat 风格的监控扫描：

```bash
python3 scripts/heartbeat_runtime.py
```

---

## 在 OpenClaw 里怎么用

FastSlow Evo 不是一个单独启动的 app。
它是一个 skill：当你要求 agent 通过 fast loop / slow loop 来改进时，它就会被调用。

### 最简单的 3 句触发话术

你在 OpenClaw 对话里直接说：

1. **“这次走 fast loop，给我最小修复。”**
2. **“这个模式一直重复，走 slow loop。”**
3. **“你判断该走 fast 还是 slow，并直接执行。”**

### 常见 fast loop 说法

- “以后这种情况这样处理，走 fast loop。”
- “这个摘要漏了 action item，走 fast loop 修掉。”
- “这个回复太官方了，走 fast loop 调整。”
- “你把工具结果读错了，给我最小修复。”

### 常见 slow loop 说法

- “这个问题已经反复出现，走 slow loop。”
- “把这个重复修复晋升成长期规则。”
- “这个模式已经稳定了，升级成长期能力。”

---

## 常见使用场景

### 1. 会议摘要总漏 action item

你说：

```text
这个摘要漏了 action item，走 fast loop，给我最小修复。
```

预期结果：
- 更紧的摘要模板
- action-review checklist
- 一个小型验证规则

### 2. 回复太官方、太像 AI

你说：

```text
这个回复太官方了，走 fast loop，让下次更自然。
```

预期结果：
- 语气调整
- 风格 memory rule
- 模板微调

### 3. 工具结果读错了

你说：

```text
你把工具结果读错了，走 fast loop，给我最小修复。
```

预期结果：
- claim-vs-evidence 检查
- 小型验证增强
- 下次总结更保守、更准

### 4. 同类问题反复出现

你说：

```text
这个问题已经重复出现很多次了，走 slow loop，把修复升级。
```

预期结果：
- capability / behavior / validation spec
- 长期 workflow rule
- reusable skill 或脚本候选

### 5. 你不知道该走哪条环

你说：

```text
用 FastSlow Evo 判断这个该走 fast 还是 slow，然后直接执行。
```

预期结果：
- router 判断
- 给出 tiny fix 或 durable promotion 路径

---

## 示例流程

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

## 脚本

### 初始化工作结构
```bash
python3 scripts/init_spec_tree.py ./my-agent-specs
```

### 记录问题或事件
```bash
python3 scripts/new_gap_entry.py "agent claimed tool success without evidence" --gap validation_gap --source review --task "automation run" --out ./my-agent-specs/evidence/incidents
```

### 生成晋升提案
```bash
python3 scripts/build_evolution_proposal.py "tool-faithfulness-hardening" --gap validation_gap --cases 2 --recurrence 2 --spec-type validation --artifact checklist --review L1 --out ./my-agent-specs/proposals
```

### 推荐落地形式
```bash
python3 scripts/recommend_materialization.py --gap validation_gap --recurrence 2 --risk medium
```

---

## 最适合谁？

FastSlow Evo 具有一定可移植性，但尤其适合这类环境：
- agent 被反复使用
- 有持续上下文
- 用户纠正信号明确
- 存在重复工作流
- 需要在不失控的前提下持续进化

---

## 它不是什么？

FastSlow Evo 不是：
- 全自动自我修改引擎
- 泛化办公 productivity 包装器
- 没有产物的空泛反思系统
- 把每个烦恼都升级成 skill 的借口

---

## 核心哲学

> **局部适应足够时就快，长期晋升必须被证明时就慢。**

这就是整套系统的核心。

---

## 建议 GitHub Topics

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

## 许可证

MIT
