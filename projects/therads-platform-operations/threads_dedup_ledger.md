# Threads 去重台账

用于当前工作区内的 Threads 内容去重执行。

## 执行闸门

每次准备发布新内容前，必须先与最近 `2` 篇 `approved` 内容比较以下 `7` 个维度：

1. 内容链角色
2. 开头钩子
3. 主痛点
4. 论证路径
5. 故事或案例桥段
6. 证据类型
7. 互动问题

判定规则：

- 若有 `3` 项及以上高度相似：判定为 `high_duplicate`，必须重写
- 若有 `2` 项相似：判定为 `medium_duplicate`，必须至少改 `2` 项
- 若仅 `1` 项相似且其余差异明确：判定为 `low_duplicate`

## 模块必备项

- `P4`：必须有盘后结构结论、验证点、次日观察点
- `P5`：必须至少包含以下其中一项：
  - 当天盘面小故事
  - 用户常见误判场景
  - 当天案例拆解
- 同一天第三篇若承担“故事/互动/下一步预告”角色，不能只有方法，没有故事感

## 人设职责分工

- `taiwan-stock-captain`：看风向、资金、大盘结构、趋势航道
- `old-cat-taiwan-stocks`：看盘后数据、洗盘/出货、主力节奏、资金流向
- `laoqiu-88`：看入门知识、技巧拆解、指标与策略入口

## 内容记录

### 2026-03-18-01

- status: approved
- persona_id: taiwan-stock-captain
- stage: P4
- title: 台股老船長 3/18 盤後文案
- chain_role: 盘后基准帖，解释今天市场在交易什么
- hook: 今天盘面看起来不差，但很多人还是看不懂到底算不算强
- pain_point: 看很多盘后资讯还是抓不到主线，容易追高或错过
- argument_path: 先给结论，再拆市场结构，再给次日观察点
- evidence_type: 大盘结构、量能、上涨下跌家数、资金风险偏好
- cta: 你今天最卡的是看指数不敢买，还是看到强股怕追太高
- duplicate_level: baseline
- notes: 作为当天第一篇基准内容，可作为后续比较对象

### 2026-03-18-02

- status: rejected
- persona_id: old-cat-taiwan-stocks
- stage: P5
- title: 老貓看台股 3/18 初稿
- chain_role: 晚间方法帖
- hook: 你今天如果又有这种感觉，我先说，很正常
- pain_point: 追高杀低、把正常震荡脑补成主力洗盘
- argument_path: 情绪共鸣开头 -> 三个判断点 -> 明天继续拆
- evidence_type: 泛化盘面经验，未充分使用分点/尾盘/主力节奏
- cta: 你最常看不懂的是洗盘还是出货
- duplicate_level: high_duplicate
- overlap_with: 2026-03-18-01
- duplicate_reasons:
  - 开头都用“先安抚情绪再切入”的钩子
  - 主痛点都围绕追高、看不懂盘面、怕错过
  - 论证路径相似，都是“共鸣 -> 三点判断 -> 次日预告”
  - CTA 都是二选一式自报困扰
- notes: 不符合多人设并行时必须更换视角、权威来源、互动方式的要求

### 2026-03-18-03

- status: revision_needed
- persona_id: old-cat-taiwan-stocks
- stage: P5
- title: 老貓看台股 3/18 修正版
- chain_role: 晚间方法帖，专讲盘后如何分洗盘与出货
- hook: 今天最容易误判的，不是没追到，而是把尾盘倒货看成主力洗盘
- pain_point: 把所有震荡都解读成洗盘，结果追进最后一棒
- story_case: 缺少具体小故事或当天场景，场景感不足
- argument_path: 先指出误判 -> 给三张盘后检查表 -> 导出次日观察条件
- evidence_type: 尾盘位置、续量、同族群接棒、盘后结构
- cta: 你最近最常死在假洗盤，還是假突破
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-01
- differentiation_points:
  - 改为盘后结构视角，不再用大盘风向开场
  - 痛点从“看不懂强弱”改成“误把出货当洗盘”
  - 证据改成尾盘位置、续量、族群接棒
  - CTA 改成交易误判类型，不再问追高或不敢买
- revision_reason: 符合去重，但未满足 P5 对故事/案例的最低要求

### 2026-03-18-04

- status: approved
- persona_id: old-cat-taiwan-stocks
- stage: P5
- title: 老貓看台股 3/18 故事版
- chain_role: 晚间方法帖，用一个追高误判场景讲洗盘与出货
- hook: 今天尾盤最傷的，不是跌那一下，是很多人把出貨當洗盤
- pain_point: 用自我安慰取代盘后检查，最后接到别人倒出来的货
- story_case: 用一个“早上追進、午后震盪、尾盤轉弱還硬抱”的散戶場景開場
- argument_path: 小故事开场 -> 点破误判 -> 给三张盘后检查表 -> 次日观察条件
- evidence_type: 尾盘位置、续量、同族群接棒、盘后结构
- cta: 你最近比較常輸在假洗盤，還是假突破？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-01
  - 2026-03-18-03
- differentiation_points:
  - 增加具体用户场景，满足 P5 故事感要求
  - 仍保持老貓的人设视角与盘后拆解方法

### 2026-03-18-05

- status: approved
- persona_id: laoqiu-88
- stage: P1
- title: laoqiu.88 3/18 技巧帖
- chain_role: 入口型教学帖，用三步法教新手判断强势股该不该追
- hook: 学了很多指标，真正下单时还是只会看红绿，这就是大多数新手卡住的点
- pain_point: 指标学很多但不会落地，看到强势股还是只剩“能不能追”
- story_case: 用“看到一根长红就心痒”的新手决策场景开场
- argument_path: 点出误区 -> 三步判断框架 -> 一句话记忆点 -> 互动收尾
- evidence_type: 位置、量能、节奏三步法
- cta: 你現在最常卡的是位置、量，還是節奏？記得點關注哦～
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-01
  - 2026-03-18-04
- differentiation_points:
  - 改为入口型知识帖，不做盘后复盘或主力拆解
  - 痛点改成“学很多但不会用”，更符合 laoqiu.88 人设
  - 证据改成简化三步法，降低新手理解门槛

### 2026-03-18-06

- status: approved
- persona_id: amei-exchange-retirement-journal
- persona_mode: temporary_designated_persona
- stage: P5
- title: 阿美 3/18 日誌帖
- chain_role: 日誌型教育帖，用退休日誌口吻拆散戶為何總在情緒最熱時追進去
- hook: 3/18 這種盤，最吵的從來不是市場，是每個人心裡那句「再不買就沒了」
- pain_point: 被熱度推著走，明明想看資金，最後還是先看情緒
- story_case: 用「下午咖啡喝到一半，看見留言區又在問哪檔能追」的退休日常場景開場
- argument_path: 日誌場景 -> 點破情緒陷阱 -> 給一個資金檢查習慣 -> 留下次日預告
- evidence_type: 情緒觀察、資金邏輯、日誌式市場提醒
- cta: 你最近最常輸在太早追，還是太晚才看懂資金方向？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-01
  - 2026-03-18-04
  - 2026-03-18-05
- differentiation_points:
  - 改用退休日誌與生活切片，不走船長的大盤結構，也不走老貓的主力拆盤
  - 主痛點改成「情緒先行，資金後看」
  - 互動問題改成追價時點與資金理解，不重複前文 CTA

### 2026-03-18-07

- status: approved
- persona_id: retired-ajie-taiwan-veteran
- stage: P1
- title: 退休阿傑 3/18 老兵避坑帖
- chain_role: 老兵方法帖，教用户在题材最热时先看筹码是否换手
- hook: 很多人不是看錯題材，是在最熱的時候接到已經換手的籌碼
- pain_point: 明明有做功课，却总在题材最热时追进去，没发现筹码已经开始松动
- story_case: 用“午后看到热门题材继续冲，就以为自己终于跟上主线”的散戶误判场景开场
- argument_path: 点出踩坑 -> 解释为什么热题材最容易收割 -> 给三步筹码检查法 -> 留次日预告
- evidence_type: 题材热度、筹码换手、承接强弱、老兵避坑逻辑
- cta: 你最近最容易踩坑的，是題材追高，還是看不懂籌碼已經在換手？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-04
  - 2026-03-18-05
  - 2026-03-18-06
- differentiation_points:
  - 改成老兵避坑视角，不走老貓的主力洗盘，也不走 laoqiu 的基础三步法
  - 主痛點聚焦“题材热度 + 筹码换手”
  - 互动问题直接贴合阿傑的人设 CTA

### 2026-03-18-08

- status: approved
- persona_id: laozhou-kline-veteran
- stage: P1
- title: 老周｜K線老兵 3/18 紀律帖
- chain_role: K線纪律教学帖，教用户不要把红K当冲锋号
- hook: 今天最容易犯的錯，不是看不懂 K 線，是把每一根紅 K 都當成進攻命令
- pain_point: 手癢亂追、沒耐心等確認、看 K 線卻沒有紀律系統
- story_case: 用“盤中看到一根拉起來的紅 K 就忍不住衝，尾盤才發現上影線很長”的誤判場景開場
- argument_path: 戰場比喻 -> 點破誤讀 -> 給三步 K 線確認法 -> 留下紀律提問
- evidence_type: K 線實體、上影下影、位置與隔日確認
- cta: 你現在最大的問題，是沒耐心等確認，還是明知道逆勢還想硬拗？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-06
  - 2026-03-18-07
- differentiation_points:
  - 改成 K 線紀律視角，不走阿美的日誌感，也不走阿傑的籌碼換手
  - 核心方法改為 K 線三步確認，不與 laoqiu 的位置量節奏重複
  - 語氣更硬朗克制，符合老兵設定

### 2026-03-18-09

- status: approved
- persona_id: master-di-short-swing
- stage: P1
- title: 帝師 3/18 離場紀律帖
- chain_role: 实战节奏帖，教用户短线有赚时怎么离场，不把盈利坐回去
- hook: 很多人不是輸在不會買，是明明有賺，最後卻捨不得走
- pain_point: 進場後不知道何時該走，短線有賺總是坐回去，交易節奏和持有節奏打架
- story_case: 用“早上帳上有賺，下午回吐一半，心裡還在等再拉一根”的短線誤判場景開場
- argument_path: 實戰場景 -> 點破離場拖延 -> 給三個離場判斷 -> 留下節奏提問
- evidence_type: 波段節奏、沖高回落、分批離場、破節奏處理
- cta: 你現在更卡的是進場後不會離場，還是短線和存股的節奏總是抓不準？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-07
  - 2026-03-18-08
- differentiation_points:
  - 改成離場紀律視角，不走阿傑的籌碼，也不走老周的 K 線確認
  - 主痛點從“怎麼買”改成“有賺怎麼走”
  - 方法改為分批離場與節奏管理，符合帝師的人設

### 2026-03-18-10

- status: approved
- persona_id: laowang-taiwan-rebuild
- stage: P1
- title: 台股老汪 3/18 反翻本帖
- chain_role: 交易心理修正帖，提醒用户亏损后最危险的不是赔钱，是急着翻本
- hook: 今天最危險的，不是沒賺到，是一虧就想立刻翻回來
- pain_point: 把股市做成情绪赌局，明知道要停手，还是忍不住冲动加码
- story_case: 用“下午一筆單沒做好，腦中立刻冒出再做一筆把它翻回來”的失控場景開場
- argument_path: 過來人警醒 -> 點破翻本心態 -> 給三個止手檢查點 -> 留下自我提問
- evidence_type: 情緒失控、加碼衝動、停手紀律、反賭式修正
- cta: 你現在最難改掉的，是想翻本的衝動，還是明知道該停手卻停不下來？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-08
  - 2026-03-18-09
- differentiation_points:
  - 改成反翻本心態，不走 K 線紀律或離場紀律
  - 主痛點改成“虧損後想立刻翻回來”
  - 证据和方法聚焦停手纪律与反赌式修正

### 2026-03-18-11

- status: approved
- persona_id: shortline-sniper-temp
- persona_mode: temporary_designated_persona
- stage: P1
- title: 短線狙擊手 3/18 狙擊節奏帖
- chain_role: 短線方法帖，教用户不要抢第一枪，而是等确认后再出手
- hook: 短線最常見的虧法，不是看錯，是太早開槍
- pain_point: 一看到異動就衝，沒等確認，最後買在最容易被震掉的位置
- story_case: 用“開盤看到一檔急拉就追，10 分鐘後回落開始懷疑人生”的短線誤判場景開場
- argument_path: 點破手快迷思 -> 給三個狙擊前確認點 -> 留下次日應用題
- evidence_type: 開盤節奏、第一波異動、回踩確認、量價續航
- cta: 你做短線最常輸在太早出手，還是明明等到了訊號卻不敢打？
- duplicate_level: low_duplicate
- compared_with:
  - 2026-03-18-09
  - 2026-03-18-10
- differentiation_points:
  - 改成“等確認再開槍”的短線節奏，不走帝師的離場紀律
  - 主痛點改成“太早出手”，不走老汪的翻本心態
  - 方法聚焦開盤後第一段節奏與回踩確認
