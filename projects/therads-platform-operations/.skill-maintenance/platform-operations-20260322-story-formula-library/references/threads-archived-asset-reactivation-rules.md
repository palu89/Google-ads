# Threads 归档资产再启用规则

本文件用于处理“旧资产要不要重新启用”，避免把历史内容直接回流到活跃层。

## 一、适用场景

- 旧高表现内容准备重写再发
- 历史栏目准备恢复
- 阶段收口后的参考素材准备重新进入队列
- 想把 `reference` 或 `archive` 层资产重新带回活跃流程

## 二、前置检查

1. 当前为什么要再启用
2. 原归档原因是否已经变化
3. 当前阶段是否仍适配
4. 当前 persona / 栏目是否仍适配
5. 是否需要先重写，而不是直接复用

## 三、处理方式

- `direct-reuse`：允许直接复用
- `revise-first`：先改写后再用
- `reference-only`：仅参考，不重新启用
- `keep-archived`：继续保持归档

## 四、最小模板

```text
Threads 归档资产再启用：
- 资产名称：
- 当前归档层级：
- 再启用理由：
- 原归档原因：
- 当前适配阶段：
- 当前适配 persona / 栏目：
- 处理方式：direct-reuse | revise-first | reference-only | keep-archived
- 风险点：
- 验证步骤：
```

## 五、使用规则

- `blocked` 资产不得无复核直接回流
- `archive` 与 `reference` 资产回流前，应重新走审稿、去重与连续性检查
- 若再启用成功，应同步更新 `threads-content-asset-archiving-rules.md` 与内容队列状态
