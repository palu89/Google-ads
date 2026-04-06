---
id: field_manual_v3.0
entity_type: knowledge
domain: googleads
layer: official
task_types: [general_operations, script_deployment, compliance, keyword_audit, landing_page_audit, finance_verification]
priority: 1
status: active
source: /Users/palu/Google ADS/GOOGLE_ADS_FIELD_MANUAL.md
source_checked_at: 2026-04-06T11:09:00Z
content_updated_at: 2026-02-08T04:13:00Z
depends_on: []
summary: Comprehensive field manual for Google Ads operations covering script development, keyword auditing, compliance verification, landing page optimization, and emergency procedures. Serves as the primary operational guide for advanced optimizers.
---

# 📘 Google Ads 总控台 · 深度实战作业指导书 (Field Manual v3.0)

**文档密级**：机密 | **适用人员**：高级优化师 | **核心系统**：Codex Orchestrator

---

## 模块一：自动化脚本开发 (Google Ads Scripts)

### 1.1 作战场景与需求拆解

你不仅是写个脚本，你是要部署一个**7x24小时的账户守卫**。

* **场景 A (止损)**：监控"高花费零转化"的词/组/计划，自动暂停。
* **场景 B (洗词)**：监控"搜索字词"，将点击率 < 0.5% 的词自动拉黑。
* **场景 C (监控)**：监控"账户余额"或"链接 404"，发邮件报警。
* **场景 D (天气)**：下雨天自动提高"雨伞"广告组出价 20%。

### 1.2 核心指令构建 (Copy-Paste Prompts)

**不要**只说"写个脚本"。**必须**按以下格式发送指令：

> **调用总控台：启动 `googleads-scripts` 模块。**
> **【业务逻辑】**：
> 监控过去 **24 小时** (TODAY 还是 YESTERDAY?)，如果 **单次转化成本 (CPA)** 超过 **£50**，且 **转化次数** 大于 **0**，则 **暂停该广告组**。
> **【技术约束】(必须严格执行)**：
> 1. **安全阀**：代码开头必须定义 `var DRY_RUN = true;`。默认只打印日志，不执行修改。
> 2. **货币换算**：注意 `metrics.cost_micros`，输出日志时必须除以 1,000,000 并保留 2 位小数。
> 3. **通知机制**：如果触发暂停，必须发送邮件给 `[你的邮箱]`。
> 4. **迭代器**：使用 `AdsApp.adGroups()` 结合 `.withCondition()` 过滤，不要遍历所有数据。
> 5. **日志规范**：`Logger.log` 必须输出：`[暂停警告] 广告组名: XXX | 花费: £XX | CPA: £XX`。
> 
> 

### 1.3 Google Ads 后台部署 SOP (点击级步骤)

拿到 AI 代码后，请严格按此步骤操作：

1. **进入入口**：
* 登录 Google Ads。
* 点击顶部导航栏 **工具与设置 (Tools and Settings)** 图标（扳手形状）。
* 选择 **批量操作 (Bulk Actions)** > **脚本 (Scripts)**。


2. **创建脚本**：
* 点击蓝色大加号 **[+]**。
* **命名**：顶部"未命名脚本"改为 `Auto_Pause_High_CPA_Script`（一定要命名，否则以后找不到）。


3. **代码注入**：
* **清空**：`function main() {}` 里的所有内容。
* **粘贴**：将 AI 生成的代码完整粘贴进去。
* **修改变量**：找到代码顶部的 `CONFIG` 区域，把 `const EMAIL = '...'` 改成你的真实邮箱。


4. **授权 (Authorize)**：
* 点击编辑器右下角的 **授权 (Authorize)** 黄色/蓝色按钮。
* 弹出窗口选择你的 Google 账号 > 点击 **Allow**。


5. **试运行 (Preview)** —— **生死攸关的一步！**
* 确保代码里 `var DRY_RUN = true;`。
* 点击 **预览 (Preview)** 按钮。
* 盯着底部的 **日志 (Logs)** 窗口。
* *检查点*：日志是否显示 `[Dry Run] Would have paused ad group: Campaign A > Group B`？如果逻辑对，才进行下一步。


6. **实装 (Run)**：
* 将代码里的 `var DRY_RUN = false;`。
* 点击 **运行 (Run)**。


7. **设置排期 (Frequency)**：
* 回到脚本列表页。
* 在 **频率 (Frequency)** 列，将"从不"改为 **每小时 (Hourly)** 或 **每天 (Daily)**。



### 1.4 常见报错与救火指南

* **报错 `ReferenceError: AdsApp is not defined**`
* *原因*：你在浏览器控制台跑代码？
* *解法*：必须在 Google Ads 脚本编辑器里跑。


* **报错 `Cannot read property 'cost_micros' of undefined**`
* *原因*：GAQL 查询语句写错了，或者 API 版本太老。
* *解法*：对 AI 吼："你的 GAQL 查询语句字段不对，请检查最新的 Google Ads API 字段名。"


* **现象：脚本跑了，钱还在花**
* *原因*：`DRY_RUN` 忘了改成 `false`。
* *解法*：改代码，保存，重新运行。



---

## 模块二：关键词清洗与意图审计 (Keyword Auditing)

### 2.1 作战场景

* **新户搭建**：有了 500 个词，不知道选哪 20 个做"Exact Match"。
* **SQR 清洗**：跑了一周，发现 CPA 爆炸，需要从"搜索字词报告"里抓出垃圾词。

### 2.2 核心指令构建

> **调用总控台：启动 `googleads-keyword-expert` 模块。**
> **【背景信息】**：
> 我在推广 **[SaaS 进销存软件]**，目标客户是 **[中小企业老板]**，单价 **[5000元/年]**。
> **【待审列表】**：
> (在此处粘贴 Excel 里的 50-100 个词)
> **【执行动作】**：
> 1. **红绿灯分类**：
> * 🔴 **红色 (剔除)**：C端用户、免费白嫖党、学生党、求职者。
> * 🟢 **绿色 (保留)**：找软件、比价格、找供应商、B端意图。
> 
> 
> 2. **深度否定建议**：
> * 不要只给我词，给我 **匹配模式**。例如：建议否定 `"free"` (Phrase Match)。
> 
> 
> 3. **理由**：
> * 对于剔除的词，告诉我用户搜这个词的时候，脑子里在想什么（Search Intent）。
> 
> 
> 
> 

### 2.3 Google Ads 后台部署 SOP

1. **否定词操作**：
* 点击顶部 **工具 (Tools)** > **共享库 (Shared Library)** > **否定关键词列表 (Negative keyword lists)**。
* 点击 **[+]**，命名为 `General_Negative_List`。
* 将 AI 给出的红色词列表（注意格式：`"phrase match"`, `[exact match]`, `broad match`）粘贴进去。
* 点击 **应用到广告系列 (Apply to campaigns)**，全选所有系列。


2. **新增词操作**：
* 进入具体的 **广告组** > **关键词** > **搜索关键词**。
* 点击 **[+]**，粘贴 AI 给出的绿色词。
* *技巧*：如果不确定，先用 **词组匹配 (Phrase Match, "keyword")**，不要用广泛匹配。



---

## 模块三：金融/敏感行业合规 (Compliance & G2 Verification)

### 3.1 作战场景

* 客户是做外汇 (Forex)、加密货币、股票投顾、甚至减肥药的。
* 广告被拒登，理由是 `Financial Products` 或 `Circumventing Systems`（规避系统）。

### 3.2 核心指令构建

> **调用总控台：启动 `googleads-verify` 和 `googleads-audit` 模块。**
> **【客户画像】**：
> 地区：**[英国 UK]**。业务：**[差价合约 CFD 交易]**。
> **【任务清单】**：
> 1. **资质核查**：在英国推 CFD，需要什么具体的 FCA 牌照号码？Google 的 G2 验证入口链接给我。
> 2. **落地页扫描**：
> * 我的 Footer 写了：`Trading involves risk.`
> * 够不够？不够的话，请根据英国 FCA 规定，帮我重写一段**标准风险免责声明 (Disclaimer)**。
> 
> 
> 3. **申诉预演**：
> * 如果被拒登提示"规避系统"，我该检查网站的哪些技术细节（重定向？Cloaking？弹窗？）
> 
> 
> 
> 

### 3.3 实操落地 SOP

1. **改网站 (Before Appeal)**：
* **Footer 修改**：将 AI 生成的风险声明（如 *"xx% of retail investor accounts lose money..."*）放到网站每一页的最底部，字号不能太小。
* **地址核验**：网站上的公司地址，必须和 Google Ads 账户里的"支付设置"地址、以及 FCA 注册地址**三者完全一致**。


2. **提交 G2 验证**：
* AI 会给你一个链接（通常是 `support.google.com/...` 开头的表单）。
* 填表时，**"Third-party"** 选 NO（除非你是代理商代投），**"License Number"** 填 FCA 监管号。


3. **站内申诉**：
* 在广告账户顶部红条 -> **Fix it** -> **Appeal**。
* **Reason** 选 "Dispute decision" (有异议)。
* **Comments**：复制 AI 帮你写的申诉信（`googleads-appeal` 模块生成的），重点强调："我们是持牌机构（附牌照号），网站合规，请人工复审。"



---

## 模块四：落地页体验优化 (LP Audit)

### 4.1 作战场景

* 质量得分 (Quality Score) 里的"落地页体验"一直是"低于平均值"。
* 移动端转化率极低。

### 4.2 核心指令构建

> **调用总控台：启动 `googleads-audit` 模块。**
> **【页面内容】**：
> (在此处粘贴你的落地页首屏文案，或者 URL)
> **【诊断要求】**：
> 1. **相关性检查**：我的广告语是"低点差外汇开户"，但落地页第一句话是"全球领先的金融科技公司"。请指出文案断层。
> 2. **CTA 优化**：现在的按钮是"提交"。请给三个更具转化诱惑力的 CTA 按钮文案。
> 3. **信任度**：除了牌照，我还应该放什么 Trust Badge (信任徽章)？
> 
> 

---

## ⚠️ 紧急熔断机制 (Emergency Procedures)

**当系统出现以下情况时，请立即停止操作：**

1. **AI 幻觉**：AI 开始编造不存在的 Google Ads 菜单项（比如"点击设置里的高级AI优化按钮"）。
* *动作*：输入指令 **"重置逻辑。引用 `references/agents_backup.md`。告诉我真实的 Google Ads 菜单路径。"**


2. **脚本暴走**：脚本运行后，花费瞬间飙升。
* *动作*：立即在脚本界面点击 **停用 (Disable)**，并去 **更改历史记录 (Change History)** 撤销所有操作。


3. **账户关联封号**：你的 IP 登录了被封的户，导致新户也被封。
* *动作*：**物理隔离**。不要用同一个浏览器指纹登录。使用指纹浏览器或 VPS。



---

**这份文档就是你的作战地图。保存它，打印它，每一次操作前，先查阅它。**