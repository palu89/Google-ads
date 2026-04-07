# Threads 多账号运营架构

本文件用于把 Threads 从“单账号内容运营”扩展为“账号矩阵运营”，但仍保持：

- `Codex` 负责方法、结构、规则与组合决策
- `OpenClaw` 负责运行接线、发布、回写与前端交互
- `TG 机器人` 负责日常操作入口

当前以 `2026-03-21` 为基准，已按 Meta 官方 Threads API 能力核对：

- 可程序化发帖
- 可读取与管理 replies
- 可拉取 account / post insights

官方参考：

- [Threads API Collection](https://www.postman.com/meta/threads/collection/dht3nzz/threads-api)
- [Get Account Insights](https://www.postman.com/meta/threads/request/4pbwq2u/get-account-insights)
- [Get Threads Replies](https://www.postman.com/meta/threads/request/n4uyk1y/get-threads-replies)

## 一、目标

当用户要做 `10` 个账户的：

- 发帖
- 下钩子
- 回复运营
- 涨粉
- 复盘

默认不是把 `10` 个号当成 `10` 个相同账号，而是做成一个“组合运营系统”。

## 二、分层架构

### 1. 组合治理层

负责：

- 账号矩阵设计
- 账号角色分工
- 主线 / 副线资源倾斜
- 组合级周报与月报
- 涨粉实验优先级

由 `Codex` 主导。

### 2. 账户治理层

负责：

- 单个账号 persona
- 单个账号栏目
- 单个账号发帖频率
- 单个账号风险边界
- 单个账号基线卡

由 `Codex` 定规则，`OpenClaw` 负责执行和回写。

### 3. 内容工厂层

负责：

- 选题池
- 钩子库
- 草稿
- 审稿
- 队列
- 批次化发布包

多账号情况下，内容工厂仍共用一套审稿与连续性标准，但每个账号必须保留独立 persona 和栏目边界。

### 4. 执行层

负责：

- Threads API 发帖
- 回帖读取和分级
- 高风险回复处理
- 发帖状态回写
- insights 抓取

由 `OpenClaw` 项目层负责。

### 5. 学习层

负责：

- 单账号学习
- 组合级学习
- 钩子表现回写
- 涨粉实验复盘
- 资源倾斜决策

必须区分：

- `账号级学习`
- `组合级学习`

## 三、建议的 10 账户矩阵

建议结构：

- `1` 个主品牌号
- `3` 个垂类号
- `3` 个人设号
- `2` 个快反 / 热点号
- `1` 个实验号

说明：

- 主品牌号负责总定位和信任背书
- 垂类号负责某个细分主题的连续深耕
- 人设号负责情绪温度、故事感和差异表达
- 快反 / 热点号负责事件钩子和流量爆点
- 实验号负责测试新节奏、新钩子和新栏目

## 四、每个账户的最小字段

每个账户至少要有：

- `account_id`
- `account_type`
- `primary_persona`
- `backup_persona`
- `content_pillars`
- `primary_track`
- `secondary_track`
- `post_frequency`
- `reply_policy`
- `growth_goal`
- `risk_boundary`
- `status`

## 五、Codex / OpenClaw / TG 分工

### Codex

- 决定矩阵结构
- 决定账号角色
- 决定钩子策略
- 决定增长实验设计
- 决定哪些项目层 skills 需要新增

### OpenClaw

- 运行发帖
- 运行回帖管理
- 运行 insights 回收
- 运行学习回写
- 对接 TG 入口

### TG 机器人

- 接收运营指令
- 接收内容生成请求
- 接收审稿请求
- 接收周报 / 复盘请求

## 六、Batch 01 约束

多账号链路的第一批不做：

- `10` 账户全自动并发
- 无审稿直发
- 无账号分工的内容铺量
- 无回写的自动增长

第一批只做：

- 矩阵结构
- 账号骨架
- 钩子治理
- 发布规格
- insights 回收规格

## 七、触发条件

只有当用户明确提到以下需求时，才默认进入本架构：

- 多账号
- 账号矩阵
- `10` 个账户
- 统一发帖
- 统一回复
- 组合增长
- 组合周报

否则仍按单账号内容运营主链处理。
