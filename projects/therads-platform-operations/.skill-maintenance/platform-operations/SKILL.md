---
name: platform-operations
description: 台股 Threads 爆款写帖极简 skill。从零重建，只保留单一赚钱爆帖模板。
---

# 台股爆款写帖

这个 skill 只保留一套新写法。

现在只做一件事：

`按核心指令“模版1”写一篇赚钱兑现型爆帖`

## 何时使用
- 用户要直接写 Threads 爆款帖
- 用户明确给出 `模版1`
- 或者给出 `人设：任意标签/模版1/日期`
- 用户在 Codex 中直接要求按 `platform-operations` 进行内容创作

## 默认读取
- `references/content-output-enforcement.md`
- `references/viral-profit-template.md`
- `references/template-01-engine-map.md`
- `references/codex-content-creation-prompt.md`

## 唯一目标
写出一篇：
- 大家先看错
- 主角先看对
- 主角先下手
- 后面真的涨了
- 别人后来回头问

## 核心指令

```text
模版1
```

## 可选补充

```text
人设：<任意标签>
日期：YYYY-MM-DD
事件：<热点事件>
方向：<真正赚钱方向>
```

规则：
- 只要出现 `模版1`，就默认按这个唯一模板起稿
- `人设` 和 `日期` 只作为上下文，不进入输出正文
- 如果用户不给 `事件` 和 `方向`，默认按模板随机替换关键事件和赚钱方向，但必须符合逻辑
- 如果用户补了 `事件` 和 `方向`，就直接按用户给的写
- `模版1` 只允许保留功能位，再做强制槽位替换
- 允许替换外壳槽位，不允许重写发动机、推进顺序、兑现方式和回头来问的闭环
- 每次至少替换 8 项关键槽位，不允许只换几个表层词
- 不允许复用旧样稿的专属句子、专属场景链、专属人物入口和专属回问句型

## 资源
- `references/content-output-enforcement.md`
- `references/viral-profit-template.md`
- `references/template-01-engine-map.md`
- `references/codex-content-creation-prompt.md`
- `references/skill-validation.md`
