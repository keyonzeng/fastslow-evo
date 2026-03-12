# FastSlow Evo

**FastSlow Evo 是一个面向 AI Agent 的双循环自我进化系统。**

它通过两个不同时间尺度的循环，让智能体在真实使用中持续变好：

- **快循环**：处理局部、小而高频、低风险、容易验证的问题
- **慢循环**：处理重复出现、跨上下文稳定、值得长期沉淀的问题

FastSlow Evo 不是日志系统，不是 Python 规则引擎，也不是黑箱式自我修改工具。

它的核心任务是帮助智能体判断：

- 什么该马上修
- 什么该慢慢升
- 什么该继续观察
- 什么该忽略
- 什么该明确驳回

在 OpenClaw 中，FastSlow Evo 依赖：

- 来自 incident / correction / win 的真实 evidence
- OpenClaw 主模型的语义判断
- markdown 协议提供的审查纪律、收敛规则、验证要求和回滚约束

它的目标，是避免两种常见失败：

- **under-evolution**：有价值经验没有沉淀成能力
- **over-evolution**：局部噪音被过早固化成长期规则

### 一句话说明

**FastSlow Evo 是一个以判断为中控、以双循环为机制、以自我进化为目标的 Agent 能力系统。**

---

## 仓库现在包含什么

- `SKILL.md` —— OpenClaw 的操作说明
- `references/` —— 协议、rubric、阅读顺序、示例、最小可用工作流
- `assets/` —— markdown 模板
- `specs/` —— 示例化的长期工件

Python helper 已经从默认设计里移除。
现在的 FastSlow 是 protocol-first、model-driven。

---

## 默认可用工作流

先读：
- `references/runtime-core/minimal-usable-workflow.md`

这份文件就是最短可用路径。

如果要看完整协议栈，再读：
- `references/runtime-optional/openclaw-judgment-first.md`
- `references/runtime-core/protocol-reading-order.md`
- `references/runtime-branches/evidence-protocol.md`
- `references/runtime-core/review-protocol.md`
- `references/runtime-core/evaluation-rubric.md`
- `references/runtime-core/review-output-format.md`
- `references/runtime-branches/candidate-protocol.md`
- `references/runtime-branches/heartbeat-protocol.md`

---

## 在 OpenClaw 中怎么快速使用

### 新 correction / incident 出现时
1. 按模板写一份 evidence markdown。
2. 保留 full context 和 raw signal。
3. 让 OpenClaw 按协议完成审查。
4. 在以下状态中选一个：
   - fast
   - slow-candidate
   - observe
   - ignore
   - reject
5. 执行最小必要下一步。

### 审查 candidate 时
1. 先读 candidate protocol 和 checklist。
2. 再读 linked evidence。
3. 判断 candidate 应该：
   - merge
   - keep separate
   - split
   - supersede
   - create
   - no-action
4. 按统一 review output format 写回判断。

### 做 heartbeat review 时
1. 先读 heartbeat protocol。
2. 审查 recent evidence 和 current candidates。
3. 只允许输出：
   - no-action
   - update existing candidate
   - create one candidate
   - split candidate
   - reject candidate

---

## 示例文件

优先看这几个：
- `references/examples/example-fast.md`
- `references/examples/example-slow-candidate.md`
- `references/examples/example-reject.md`

这三个例子覆盖最高价值的三条路径：
- 什么情况下只该做局部修补
- 什么情况下该创建或更新一个 durable candidate
- 什么情况下应该 reject / rollback 弱候选

旧的 worked examples 仍保留在 `references/` 下，供维护和深入理解时使用。

---

## FastSlow Evo 不是什么

它不是：
- Python 规则引擎
- 把每条记录都变成 candidate 的文件喷射器
- 用弱证据硬做 promotion 的借口
- 不受治理的自我修改系统

---

## 核心哲学

**局部适应足够时就快，长期晋升必须被证明时才慢。**
