# Threads 提频阶段分栏目升级顺序

本文件用于在内容重启后的提频阶段，明确哪些栏目、哪些 persona 先升级，哪些继续维持，避免全线一起加速。

## 一、适用场景

- 已进入 `threads-content-restart-cadence-escalation-rules.md`
- 准备从当前节奏继续提频
- 需要给不同栏目分先后顺序
- 想避免一提频就全栏目一起抬升

## 二、顺序结论

- `priority-up`
- `hold`
- `late-up`

## 三、最小判断维度

1. 哪些栏目当前最稳定
2. 哪些栏目仍有风险或证据不足
3. 哪些 persona 适合先承担升级节奏
4. 当前主线和副线谁应先升级
5. 若升级失败，哪些栏目要最先回退

## 四、最小模板

```text
Threads 提频阶段分栏目升级顺序：
- 当前节奏级别：
- 当前阶段目标：
- 候选栏目 / persona：
- 第一顺位升级：
- 第二顺位升级：
- 暂缓升级：
- 升级依据：
- 回退优先级：
- 下次复核点：
```

## 五、使用规则

- 分栏目升级顺序要先于正式提频执行
- 同轮提频默认只放大少数稳定栏目，不全线同升
- 主线栏目优先于高波动副线栏目
- 升级顺序应同步 `threads-weekly-content-schedule.md` 与 `threads-stage-goal-tracker.md`
- 若准备进入更长周期提频，应同步 `threads-multiweek-content-cadence-stress-test.md`
