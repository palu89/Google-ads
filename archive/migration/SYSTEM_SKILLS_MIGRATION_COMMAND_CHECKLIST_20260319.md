# System Skills 迁移命令清单

## 说明

这是一份执行草案，不代表已经执行。

目标：

- 先迁移 Codex 系统层
- 再迁移 OpenClaw 系统层
- 最后收口 Google Ads 项目层

原则：

- 只做小批次
- 不做破坏性删除
- 优先复制，验证后再冻结旧目录
- 任何带密钥、账号、连接 ID 的内容先脱敏

## 预检查

### 1. 确认目标目录不存在冲突版本

```bash
find /Users/palu/.codex/skills -mindepth 1 -maxdepth 1 -type d | sort
find /Users/palu/.openclaw/skills -mindepth 1 -maxdepth 1 -type d | sort
```

### 2. 只读检查来源 skill

```bash
find /Users/palu/.openclaw/workspace/skills/self-improving-agent -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/workspace/skills/skill-vetter -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/workspace/skills/web-search -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/workspace/skills/skills/summarize -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/workspace/skills/serpapi-search -maxdepth 2 \( -type f -o -type d \) | sort
```

## 批次 A：Codex 系统层迁移

### A1. self-improving-agent

```bash
mkdir -p /Users/palu/.codex/skills/self-improving-agent
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace/skills/self-improving-agent/ \
  /Users/palu/.codex/skills/self-improving-agent/
```

### A2. skill-vetter

```bash
mkdir -p /Users/palu/.codex/skills/skill-vetter
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace/skills/skill-vetter/ \
  /Users/palu/.codex/skills/skill-vetter/
```

### A3. web-search

```bash
mkdir -p /Users/palu/.codex/skills/web-search
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace/skills/web-search/ \
  /Users/palu/.codex/skills/web-search/
```

### A4. summarize

```bash
mkdir -p /Users/palu/.codex/skills/summarize
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace/skills/skills/summarize/ \
  /Users/palu/.codex/skills/summarize/
```

### A5. serpapi-search

```bash
mkdir -p /Users/palu/.codex/skills/serpapi-search
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  --exclude '.env' \
  /Users/palu/.openclaw/workspace/skills/serpapi-search/ \
  /Users/palu/.codex/skills/serpapi-search/
```

### A6. Codex 迁移后检查

```bash
find /Users/palu/.codex/skills/self-improving-agent -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.codex/skills/skill-vetter -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.codex/skills/web-search -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.codex/skills/summarize -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.codex/skills/serpapi-search -maxdepth 2 \( -type f -o -type d \) | sort
```

## 批次 B：OpenClaw 系统层迁移

### B1. proactive-monitor

```bash
mkdir -p /Users/palu/.openclaw/skills/proactive-monitor
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace-googleads-palu/skills/proactive-monitor/ \
  /Users/palu/.openclaw/skills/proactive-monitor/
```

### B2. self-improving-agent

```bash
mkdir -p /Users/palu/.openclaw/skills/self-improving-agent
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace-googleads-palu/skills/self-improving-agent/ \
  /Users/palu/.openclaw/skills/self-improving-agent/
```

### B3. summarize

```bash
mkdir -p /Users/palu/.openclaw/skills/summarize
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  /Users/palu/.openclaw/workspace/skills/skills/summarize/ \
  /Users/palu/.openclaw/skills/summarize/
```

### B4. composio-integration

在执行复制前，先检查并清理：

```bash
sed -n '1,240p' /Users/palu/.openclaw/workspace-googleads-palu/skills/composio-integration/SKILL.md
find /Users/palu/.openclaw/workspace-googleads-palu/skills/composio-integration/scripts -maxdepth 2 -type f | sort
rg -n 'ak_|ca_|gmail|tasks|token|secret|api[_-]?key' /Users/palu/.openclaw/workspace-googleads-palu/skills/composio-integration
```

脱敏后再复制：

```bash
mkdir -p /Users/palu/.openclaw/skills/composio-integration
rsync -a \
  --exclude '.git' \
  --exclude '.clawhub' \
  --exclude '_meta.json' \
  --exclude 'package-lock.json' \
  /Users/palu/.openclaw/workspace-googleads-palu/skills/composio-integration/ \
  /Users/palu/.openclaw/skills/composio-integration/
```

### B5. OpenClaw 迁移后检查

```bash
find /Users/palu/.openclaw/skills/proactive-monitor -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/skills/self-improving-agent -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/skills/summarize -maxdepth 2 \( -type f -o -type d \) | sort
find /Users/palu/.openclaw/skills/composio-integration -maxdepth 2 \( -type f -o -type d \) | sort
```

## 批次 C：Google Ads 项目层收口

### C1. 保留名单核对

```bash
find /Users/palu/.openclaw/workspace-googleads-palu/skills -mindepth 1 -maxdepth 1 -type d | sort
```

保留目标：

- `ads-compliance`
- `ads-compliance-checker`
- `googleads-ai-audit`
- `googleads-knowledge`
- `googleads-orchestrator`
- `googleads-workflow`

待移出项目层：

- `proactive-monitor`
- `self-improving-agent`
- `composio-integration`

待后续整理：

- `docs`
- `verified`

## 批次 D：冻结旧来源

建议先写冻结说明文件，再考虑重命名或归档。

建议标记对象：

- `/Users/palu/.openclaw/workspace/skills`
- `/Users/palu/.openclaw/skills/proactive-agent`
- `/Users/palu/.openclaw/skills/self-improving`
- `/Users/palu/.openclaw/skills/google-ads`
- `/Users/palu/.openclaw/skills/meta-ads-manager`
- `/Users/palu/.openclaw/skills/skill-amazon-ads`
- `/Users/palu/.openclaw/skills/ads-knowledge-indexer`

## 迁移完成后的抽查

### Codex 侧抽查

```bash
find /Users/palu/.codex/skills -mindepth 1 -maxdepth 1 -type d | sort
```

### OpenClaw 侧抽查

```bash
find /Users/palu/.openclaw/skills -mindepth 1 -maxdepth 1 -type d | sort
```

### Google Ads 项目侧抽查

```bash
find /Users/palu/.openclaw/workspace-googleads-palu/skills -mindepth 1 -maxdepth 1 -type d | sort
```

## 执行顺序结论

1. 先迁移 Codex 的 4 个核心系统 skill
2. 再迁移 Codex 的 `serpapi-search`
3. 再把 OpenClaw 的 3 个低风险系统 skill 转正
4. 最后处理 `composio-integration`
5. 等新主源稳定后，再冻结旧来源

