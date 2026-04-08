# 18. 竞争情报自动化采集指令集（CI Automation Prompts）

**创建日期**: 2026-04-08  
**用途**: 工程级Prompt模板，用于AI自动化商业情报采集  
**适用工具**: Open Claw / Cursor / ChatGPT / DeepSeek / Google AI

---

## 一、真实广告情报（Competitive Ad Intelligence）

**优化逻辑**: 从"搜索"变为"结构化抓取"

```
Prompt:
"Act as a Google Ads Intelligence Analyst. Visit ads.google.com/transparency 
and extract all active ads for [Brand Name]. 

Output format: 
1. Ad Headline & Description (Original Japanese). 
2. Call-to-Action (CTA) language. 
3. Visual style description (e.g., Manga-style, UI/UX overlay, Trust Badge placement). 
4. Date and Region mapping. 

Constraint: Ignore generic copy; highlight ads that focus on 'NISA', 'No Fee', 
or 'Number 1' claims."
```

---

## 二、LP 结构工程审计（LP Structural Audit）

**优化逻辑**: 从"描述"变为"数字化拆解"

```
Prompt:
"Act as a Conversion Rate Optimizer. Visit [URL] and perform a structural breakdown. 

Required metrics: 
1. Hero 8-Element Order (Trust/H1/Sub/Visual/CTA/SocialProof/Benefit/Legal).
2. CTA attributes: exact text, RGB/Hex color, Sticky status.
3. Section count and functional mapping (How many sections? Goal of each?).
4. Trust Badge audit (Positioning, content, specific牌照 numbers). 
5. FAQ list structure. 

Constraint: Generate a pixel-equivalent layout estimate. If a sticky CTA is present, 
state its display threshold (e.g., mobile-only / persistent)."
```

---

## 三、Wayback Machine 历史溯源（Historical Shift Analysis）

**优化逻辑**: 聚焦"战略重点的迁移"

```
Prompt:
"Use Wayback Machine to compare [URL] versions from 6 months ago vs today. 

Focus: Identify specific changes in:
1. Primary Value Proposition (What did they stop emphasizing? What did they start?). 
2. Section hierarchy (Did they move the NISA content up or down?). 
3. Trust Block evolution (Did they add/remove specific badges?). 
4. Compliance layer visibility (Has the legal disclaimer become more or less prominent?)."
```

---

## 四、SEO 意图图谱（SEO Intent Mapping）

**优化逻辑**: 从"排名前10"变为"意图聚类分析"

```
Prompt:
"Analyze the top-10 organic results on Google.co.jp for '[Keyword]'. 

Task: Classify each URL by: 
1. Intent Category (Informational/Comparison/Conversion/Brand-Direct). 
2. Structure type (Article vs. Comparison Table vs. Account Opening LP vs. Official FAQ). 
3. Trust signals used (Expert writers, official links, citation density). 

Constraint: Identify the 'Winning Pattern' used by competitors to capture the top 3 spots."
```

---

## 五、渠道流量归因（Channel Attribution Spy）

**优化逻辑**: 从"流量数值"变为"获客策略推断"

```
Prompt:
"Use SimilarWeb data to analyze the traffic source mix for [Brand Name]. 

Categorize: Search vs. Display vs. Direct vs. Social vs. Referral. 

Architectural Inference: 
1. If Direct is very high: Is it brand-dominant? 
2. If Display is unusually high: Are they running 'Branding' PMax or aggressive RTB? 
3. If Search/Social mismatch: Are they using 'Influencer-to-Search' strategies? 

Constraint: Clearly mark as 'Estimated Value' based on market trends."
```

---

## 六、校验协议（Verification Protocol）

**在所有上述Prompt末尾强制附加**：

```
VERIFICATION PROTOCOL: 
- If an extracted fact is missing from the page (e.g., license number not visible 
  in footer), mark as [MISSING]. 
- If an element is a visual inference (e.g., CTA color), provided hex values must 
  be approximations based on visual contrast. 
- Categorize the target as either "High-Performance Firm" or "Aggressive Lead-Gen Outlet".
```

---

## 七、任务路由整合方案（TASK_ROUTER）

可通过任务名自动调用对应模板：

| 任务名 | 调用模板 | 用途 |
| :--- | :--- | :--- |
| `audit_competitor_ads` | 模板一（广告情报） | 竞品广告抓取分析 |
| `audit_lp_structure` | 模板二（LP审计） | 落地页结构拆解 |
| `audit_historical_shift` | 模板三（历史溯源） | Wayback Machine对比 |
| `audit_seo_intent` | 模板四（SEO图谱） | 搜索意图聚类 |
| `audit_channel_attribution` | 模板五（流量归因） | 渠道策略推断 |
| `audit_market_trends` | 模板四+五（组合） | 市场趋势综合分析 |

---

## 八、使用注意事项

1. **替换变量**: 所有 `[Brand Name]`、`[URL]`、`[Keyword]` 需替换为实际目标
2. **校验协议必加**: 防止AI基于搜索首条结果就给出结论
3. **输出格式固定**: 要求结构化输出（表格/编号），便于入库
4. **关键提示**: 在prompt中加入 "请不要给我通用最佳实践，我需要你基于XX公司的真实页面/广告进行分析"
