# Threads 内容库存老化规则

本文件用于处理“库存里有很多内容，但越来越不好用”的问题，避免旧选题、旧草稿和旧通过稿长期占位。

## 一、适用场景

- 队列里有很多久拖未发的内容
- 一批旧选题看起来还能用，但已经不确定是否还适配当前阶段
- `approved` 很久却没发的内容开始堆积
- 想判断哪些库存该刷新、回收、归档或淘汰

## 二、老化层级

- `fresh`
- `warm`
- `stale`
- `expired`

## 三、最小判断维度

1. 内容进入库存多久了
2. 当前阶段是否还适配
3. 当前 persona / 栏目是否还适配
4. 信息和论点是否还新鲜
5. 是值得刷新，还是该退出库存

## 四、最小模板

```text
Threads 内容库存老化：
- 内容编号 / 主题：
- 当前状态：
- 入库时间：
- 当前阶段：
- 当前 persona / 栏目：
- 老化层级：fresh | warm | stale | expired
- 当前风险：
- 处理动作：keep | refresh | recycle | archive | retire
- 下次复核点：
```

## 五、使用规则

- `stale` 内容不得继续长期占用核心排期
- `expired` 内容不得直接回到发布队列
- `approved` 但明显过时的内容，必须重新做审稿与时效核验
- 处理结果应同步更新 `threads-content-queue-ledger.md` 与 `threads-content-asset-archiving-rules.md`
- 若判断为值得救的 `refresh`，应继续进入 `threads-content-inventory-regeneration-rules.md`
