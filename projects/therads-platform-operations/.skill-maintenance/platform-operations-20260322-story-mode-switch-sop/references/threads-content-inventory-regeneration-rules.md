# Threads 内容库存再生规则

本文件用于处理“旧内容还值得救，但不能直接再发”的情况，避免把老库存简单改两句就重新推进。

## 一、适用场景

- `stale` 内容仍有价值，但需要重新包装
- 旧角度已过时，但核心方法还可保留
- 某篇旧内容想转成新系列入口
- 想把旧库存重新带回活跃队列

## 二、再生方式

- `light-refresh`
- `angle-reset`
- `series-repack`
- `full-rewrite`
- `abandon`

## 三、最小判断维度

1. 哪些部分还能保留
2. 哪些部分必须重写
3. 当前阶段是否仍适配
4. 当前 persona / 栏目是否仍适配
5. 再生后回到哪个队列入口

## 四、最小模板

```text
Threads 内容库存再生：
- 内容编号 / 主题：
- 当前老化层级：
- 可保留部分：
- 必须重写部分：
- 当前适配阶段：
- 当前适配 persona / 栏目：
- 再生方式：light-refresh | angle-reset | series-repack | full-rewrite | abandon
- 再生后入口：
- 必要复核：
```

## 五、使用规则

- 再生不是跳过审稿的捷径
- 涉及时效和事实的旧内容，必须重新核验
- 再生后应同步更新 `threads-content-queue-ledger.md`
- 若最终不值得救，应回到 `threads-content-asset-archiving-rules.md`
