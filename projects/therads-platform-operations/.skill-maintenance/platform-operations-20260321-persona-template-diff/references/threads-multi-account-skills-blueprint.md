# Threads 多账号项目层 Skills 蓝图

本文件用于定义 Threads 多账号运营需要新增的项目层 skills。

这些 skills 属于：

- `平台账户运营 / Threads` 项目层

不属于：

- `Codex` 系统层
- `OpenClaw` 系统层

## 一、设计原则

- 多账号能力必须挂在项目层
- `Codex` 保留方法与规则主源
- `OpenClaw` 只承担运行 wrapper 与执行接口
- 不复制系统层 skills 本体
- 不把多账号运营误装成通用系统能力

## 二、建议新增的项目层 Skills

### 1. `threads-portfolio-orchestrator`

职责：

- 管账号矩阵
- 管组合级排期
- 管组合级资源倾斜
- 管组合级周报 / 月报

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

### 2. `threads-account-governor`

职责：

- 管单账号基线
- 管 persona 与栏目映射
- 管主线 / 副线
- 管单账号风险边界

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

### 3. `threads-hook-engine`

职责：

- 管钩子库
- 根据账号类型选钩子
- 做钩子去重
- 记录钩子表现

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

### 4. `threads-publisher`

职责：

- 对接 Threads API
- 发帖
- 更新状态
- 回写发布时间、post id 和失败信息

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

### 5. `threads-reply-operator`

职责：

- 拉取 replies
- 分级回复
- 生成建议回复
- 隐藏高风险回复

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

### 6. `threads-insights-collector`

职责：

- 拉账号 insights
- 拉帖子表现
- 回写增长台账
- 形成组合级比较

安装层次：

- `OpenClaw / platform-operations-palu 项目层`

## 三、与系统层 skills 的关系

这些项目层 skills 默认继承：

- `skill-vetter`
- `web-search`
- `summarize`
- `self-improving-agent`

按需启用：

- `serpapi-search`

运行端依赖：

- `playwright`
- `composio-integration`

## 四、Batch 01 的真实目标

`Batch 01` 不是把上述 `6` 个 skills 一次全做完。

`Batch 01` 的目标是：

- 先定蓝图
- 先定字段
- 先定输入输出
- 先定谁在组合层、谁在账户层、谁在执行层

更具体地说：

- `threads-portfolio-orchestrator`
- `threads-account-governor`
- `threads-hook-engine`

优先进入 `Batch 01` 设计。

而：

- `threads-publisher`
- `threads-reply-operator`
- `threads-insights-collector`

优先做接口规格和运行边界，不急着一步做成重自动化。

## 五、交付顺序

推荐顺序：

1. `threads-portfolio-orchestrator`
2. `threads-account-governor`
3. `threads-hook-engine`
4. `threads-publisher`
5. `threads-insights-collector`
6. `threads-reply-operator`

原因：

- 先把“脑子”搭好
- 再把“手脚”接上
- 先有组合治理
- 再做自动执行
