# Local-First Deployment

本文件只存在于工作区，不属于 live skill。

目的：
- 先在本地完成 `platform-operations` 的规则与模板调整
- 本地校验通过后，再部署到 Codex live skill
- 最后再部署到 OpenClaw runtime

## 本地 canonical 源

- skill 本地源：
  `/Users/palu/Therads平台运营/.skill-maintenance/platform-operations`
- runtime 本地源：
  `/Users/palu/Therads平台运营/.runtime-fix/platform-operations-bot-high-perf-sync`
- 运行态清理辅助：
  `/Users/palu/Therads平台运营/.runtime-fix/platform-operations-session-reset`

## live 目标

- Codex live skill：
  `/Users/palu/.codex/skills/platform-operations`
- OpenClaw workspace：
  `/Users/palu/.openclaw/workspace-platform-operations-palu`
- OpenClaw agent config：
  `/Users/palu/.openclaw/agents/platform-operations-palu/agent/config.json`
- OpenClaw sessions：
  `/Users/palu/.openclaw/agents/platform-operations-palu/sessions/sessions.json`

## 推荐顺序

1. 先改本地 skill 源
   - 只改 `/Users/palu/Therads平台运营/.skill-maintenance/platform-operations`
   - 若涉及 TG runtime，再改 `/Users/palu/Therads平台运营/.runtime-fix/platform-operations-bot-high-perf-sync`

2. 本地校验
   - 运行：
     `python3 /Users/palu/Therads平台运营/.skill-maintenance/platform-operations/scripts/validate_platform_operations.py /Users/palu/Therads平台运营/.skill-maintenance/platform-operations`

3. 部署到 Codex live skill
   - 运行：
     `rsync -a /Users/palu/Therads平台运营/.skill-maintenance/platform-operations/ /Users/palu/.codex/skills/platform-operations/`

4. 部署到 OpenClaw runtime
   - content output：
     `rsync -a /Users/palu/Therads平台运营/.runtime-fix/platform-operations-bot-high-perf-sync/skills/threads-content-output/SKILL.md /Users/palu/.openclaw/workspace-platform-operations-palu/skills/threads-content-output/`
   - output supervisor：
     `rsync -a /Users/palu/Therads平台运营/.runtime-fix/platform-operations-bot-high-perf-sync/skills/threads-output-supervisor/SKILL.md /Users/palu/.openclaw/workspace-platform-operations-palu/skills/threads-output-supervisor/`
   - agent config：
     `rsync -a /Users/palu/Therads平台运营/.runtime-fix/platform-operations-bot-high-perf-sync/agent/config.json /Users/palu/.openclaw/agents/platform-operations-palu/agent/`
   - 若同时更新 AGENTS / editorial 基线，再额外同步对应文件

5. 清会话并重启
   - 重置 session：
     `rsync -a /Users/palu/Therads平台运营/.runtime-fix/platform-operations-session-reset/sessions.json /Users/palu/.openclaw/agents/platform-operations-palu/sessions/`
   - 重启 gateway：
     `launchctl kickstart -k gui/$UID/ai.openclaw.gateway`

6. 烟雾测试
   - TG 发一条最短测试消息
   - 再发一条真实 `persona / mode / date / module / topic` 指令

## 边界

- 不再直接把 workspace 外的 live 文件当成首改源
- 本地没通过校验，不部署
- 若只改 skill，不强制改 OpenClaw runtime
- 若只改 runtime 包装，不要反向覆盖本地 canonical skill
