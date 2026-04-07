# AI 快速启动指南 (Quick Start for AI)

**对象**: 新的对话、Copilot、Cursor 和其他 AI 工具使用本仓库时的快速启动指南  
**用途**: 5分钟内熟悉仓库结构和可用资源  
**更新**: 2026-04-08

---

## ⚡ 30秒快速启动

```
问题来了？按照这个顺序：

1. 检查问题类型 → 去 Step 2
2. 打开 /knowledge/googleads/TASK_ROUTER.yaml
3. 找到你的问题所属的 task_type
4. 跳转到相应的知识文件或 skill
5. 回答问题
```

---

## 🎯 5 个最常见的使用场景

### 场景 1: 我需要诊断性能问题

**快速路由**:
```
问题 → 信号分析？
  ✅ 是 → skill: googleads-audit + knowledge: signal-control-matrix
  ❌ 否 → 继续
```

**使用资源**:
- Skill: `googleads-audit` (落地页审核)
- Knowledge: `/knowledge/googleads/hybrid/signal-analysis-playbook.md`
- Knowledge: `/knowledge/googleads/hybrid/signal-control-matrix.md`

### 场景 2: 我需要创建或优化 Google Ads 活动

**快速路由**:
```
活动问题？
  → skill: googleads-field-operations (Google Ads 优化师总控台)
  → knowledge: /knowledge/googleads/official/field_manual_v3.0.md
  → knowledge: /knowledge/googleads/best-practices/question-framework.md
```

### 场景 3: 我需要关键词分析和优化

**快速路由**:
```
关键词问题？
  → skill: googleads-keyword-expert
  → knowledge: /knowledge/googleads/internal/keyword_expert.md
```

### 场景 4: 我需要编写自动化脚本

**快速路由**:
```
脚本问题？
  → skill: googleads-scripts
  → knowledge: /knowledge/googleads/internal/script_architect.md
```

### 场景 5: 我需要理解 API 或官方文档

**快速路由**:
```
官方文档问题？
  → Load /knowledge/googleads/official/ (4 个文件)
  → 按照 tier loading 规则 (Official tier first)
```

---

## 📚 核心资源快速索引

### 4个活跃的Skills (Active Skills) — 自包含、通用格式

> **核心特性**：每个 Skill 文件都是**完全自包含**的纯 Markdown。  
> 可以直接复制粘贴到任何 AI 工具（ChatGPT / Claude / Gemini / Copilot / Cursor），AI 将立即获得对应能力。  
> 无需额外依赖文件。

| Skill ID | 名称 | 用途 | 入口 |
|----------|------|------|------|
| `googleads-field-operations` | Google Ads 优化师总控台 | 全域运营调度、策略指导 | `skills/googleads-field-operations/SKILL.md` |
| `googleads-audit` | 落地页审计专家 | 合规扫描、质量得分诊断、CTA 优化 | `skills/googleads-audit/SKILL.md` |
| `googleads-keyword-expert` | 关键词意图判官 | 意图分析、红绿灯分类、否定词建议 | `skills/googleads-keyword-expert/SKILL.md` |
| `googleads-scripts` | 脚本专家 | Google Ads 自动化脚本生成 | `skills/googleads-scripts/SKILL.md` |

**跨工具使用方法**：
1. 打开 GitHub 上对应的 SKILL.md 文件
2. 复制全部内容
3. 粘贴到任何 AI 对话中
4. AI 立即具备该技能

### 4层知识库 (Knowledge Layers)

| 层级 | 文件数 | 用途 | 何时加载 |
|------|--------|------|---------|
| **Official** | 4 | Google 官方文档、政策、API | 总是首先加载 |
| **Hybrid** | 5 | 信号工程、策略分析、RCA | 诊断和优化问题 |
| **Internal** | 5 | SOP、工具指南、Navigator | 实施和执行 |
| **Best-Practices** | 4 | 提问框架、路由决策、工程指南 | 改进 AI 响应质量 |

### 2个关键配置文件

| 文件 | 位置 | 用途 |
|------|------|------|
| **TASK_ROUTER** | `/knowledge/googleads/TASK_ROUTER.yaml` | 问题→知识/Skill 路由 |
| **ACTIVE_INDEX** | `/knowledge/googleads/ACTIVE_INDEX.yaml` | 所有知识文件的索引 |

---

## 🔍 如何在新对话中快速加载资源

### 方法 1: 基于问题类型路由 (推荐)

```
用户: "我的转化率很低，怎么优化？"

AI 行动:
1. 识别任务: performance_optimization
2. 查询: /knowledge/googleads/TASK_ROUTER.yaml
3. 找到:
   - Skill: googleads-audit
   - Knowledge: signal-analysis-playbook, signal-control-matrix
4. 加载资源并回答
```

### 方法 2: 基于关键词快速识别

```
关键词识别表:

"转化" "信号" "优化" → signal analysis framework
"脚本" "自动化" → googleads-scripts skill
"关键词" "意图" → googleads-keyword-expert skill
"落地页" "质量分" → googleads-audit skill
"活动" "策略" → googleads-field-operations skill
"政策" "申诉" → official knowledge layer
```

### 方法 3: 直接访问资源

如果你知道你需要什么，直接访问:

```bash
# 访问 Skills
/skills/googleads-{audit|scripts|keyword-expert|field-operations}/SKILL.md

# 访问知识库
/knowledge/googleads/{official|hybrid|internal|best-practices}/{filename}.md

# 查询路由规则
/knowledge/googleads/TASK_ROUTER.yaml

# 查询所有可用文件
/knowledge/googleads/ACTIVE_INDEX.yaml
```

---

## 🚀 在新对话中快速启动的3个步骤

### Step 1: Bootstrap Read (第一件事)
```
我: 我是一个新的AI对话/代理
行动: 
  1. 读取 /registry/repo.yaml (了解项目结构)
  2. 读取 /knowledge/googleads/TASK_ROUTER.yaml (了解路由)
  3. 判断当前任务类型
```

### Step 2: Load Knowledge (加载知识)
```
根据任务类型:
  → Performance Issue? → Load Signal Analysis Framework
  → Campaign Setup? → Load Field Manual + Best-Practices
  → Keyword Work? → Load Keyword Expert SOP
  → 其他? → Load appropriate layer from ACTIVE_INDEX
```

### Step 3: Execute & Document (执行和文档)
```
  → 执行任务
  → 包含 Evidence Map (证据引用)
  → 如果修改项目状态，更新 CURRENT_STATE.md
```

---

## 🔗 快速链接

| 需要 | 位置 | 优先级 |
|------|------|--------|
| 理解项目结构 | `/registry/repo.yaml` | 🔴 高 |
| 了解路由规则 | `/knowledge/googleads/TASK_ROUTER.yaml` | 🔴 高 |
| 查询所有文件 | `/knowledge/googleads/ACTIVE_INDEX.yaml` | 🟡 中 |
| 学习提问最佳实践 | `/knowledge/googleads/best-practices/question-framework.md` | 🟡 中 |
| 理解系统架构 | `/knowledge/googleads/internal/knowledge-retrieval-framework.md` | 🟢 低 |
| 信号分析诊断 | `/knowledge/googleads/hybrid/signal-analysis-playbook.md` | 🔴 高 |
| Google Ads 官方文档 | `/knowledge/googleads/official/field_manual_v3.0.md` | 🔴 高 |

---

## ❓ 常见问题 QA

### Q: 我如何知道某个 skill 是否可用?
**A**: 检查 `/registry/skills.yaml`，查找 `status: active` 的条目。当前有 4 个 active skills。

### Q: 如何加载关于日本市场的信息?
**A**: 
1. 检查是否有专项知识文件 (搜索 "japan" "日本")
2. 如果没有，使用 field_manual.md 并应用到日本市场
3. 在 `/projects/japan-google-ads/` 中查看是否有项目资料
4. 使用 Best-Practices 层的提问框架来构建有效问题

### Q: 如何查询落地页审核和市场调查相关信息?
**A**:
```
1. 落地页审核 → skill: googleads-audit
             → knowledge: /knowledge/googleads/internal/lp_auditor.md
2. 市场调查   → skill: googleads-field-operations (可用于市场分析)
             → knowledge: /knowledge/googleads/official/field_manual_v3.0.md
3. 项目专属   → /projects/japan-google-ads/ (查看项目相关文件)
```

### Q: 我如何确保我的问题得到最准确的回答?
**A**:
1. 先读 `/knowledge/googleads/best-practices/question-framework.md`
2. 使用 question routing 来自动选择正确的知识源
3. 在回答中包含 Evidence Map (指明数据来源)
4. 如果不确定，指联系当前项目所有者 (见 registry)

### Q: 如何参与建设这个知识库?
**A**:
1. 新增知识文件 → 需要在 registry 中注册
2. 新增 Skill → 需要在 `/skills/` 创建并在 `registry/skills.yaml` 中注册
3. 更新 TASK_ROUTER → 配置新的路由规则
4. 更新 ACTIVE_INDEX → 索引新文件

---

## 🎓 学习路径 (Learning Path)

### 对于新 AI 代理 (First-time setup)

**时间**: ~15 分钟 | **优先级**: 🔴 高

```
1️⃣ 读取 AGENT_BOOTSTRAP.md (本仓库治理)
2️⃣ 读取 /registry/repo.yaml (项目结构) 
3️⃣ 读取 /knowledge/googleads/TASK_ROUTER.yaml (路由规则)
4️⃣ 查看 /knowledge/googleads/ACTIVE_INDEX.yaml (可用资源清单)
5️⃣ 根据当前任务，加载相应的 Skill 或 Knowledge
```

### 对于提高回答质量 (Quality improvement)

**时间**: ~10 分钟 | **优先级**: 🟡 中

```
1️⃣ 读取 best-practices/question-framework.md
2️⃣ 读取 best-practices/prompt-engineering-guide.md
3️⃣ 应用到你的回答中
```

### 对于深入理解 (Deep dive)

**时间**: ~30 分钟 | **优先级**: 🟢 低

```
1️⃣ 读取 internal/knowledge-retrieval-framework.md
2️⃣ 研究 hybrid/ 层的所有文件
3️⃣ 理解系统架构和设计原则
```

---

## 📞 获取帮助

如果你：
- 🤔 不知道某个概念 → 查询 ACTIVE_INDEX → 在 official 层查找
- 🎯 需要特定任务的指导 → 查询 TASK_ROUTER → 跳转到相应资源
- 🛠️ 需要工具或 SOP → 在 internal 层查找或使用相应 Skill
- 📊 需要诊断性能 → 使用 Signal Analysis Framework (hybrid 层)
- ❓ 其他问题 → 参考本文档的 QA 部分

---

## 🔄 反馈与改进

如果你发现：
- 这个指南的某个部分不清楚
- 某个资源不可用或已过时
- 需要添加新的快速启动路径

请更新本文件或在 GitHub issues 中报告。

---

**快速启动指南版本**: 1.0  
**最后更新**: 2026-04-08  
**维护者**: AI System  
**适用仓库**: /Users/palu/Google-ads
