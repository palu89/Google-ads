/**
 * 账户底层健康度扫描器（Account Deep Scanner）
 *
 * 规范与角色：
 * - 遵循 script_architect.md：包含 main()、结构化 JSON 日志、合规安全（不绕政策）
 * - 结合 keyword_expert.md：用于搜索词意图审计的分类启发式（如有扩展）
 *
 * 功能概览：
 * A) 出价透视：扫描 tCPA 系列，输出“学习状态”与“目标 tCPA vs 实际 CPA 偏离度”
 * B) 落地页扫描：检查在线广告 Final URL 的 HTTP 返回码，404/500 高亮预警
 * C) 预算风险：估算在当前消耗速度下，预算预计耗尽的小时
 * D) 实时同步：将审计数据写入 Google Sheets (Bidding_Audit, URL_Alerts)
 *
 * 全局 Dry Run：仅日志输出，不进行任何暂停/修改操作（也不写入表格，除非关闭 Dry Run）
 */
var DRY_RUN = true;
var SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1e6u3IH1TVxGsvx245XH-w1hb39a3gnpN7c6mSEXFx28/edit#gid=0';

/**
 * 结构化日志输出
 * @param {string} level 日志级别（debug|info|warn|error）
 * @param {string} module 模块名称（tcpa|lp_scan|budget_risk 等）
 * @param {string} message 人类可读信息
 * @param {Object=} data 结构化数据对象
 * @returns {void}
 * @throws {Error} 无
 */
function log(level, module, message, data) {
  var entry = {
    time: new Date().toISOString(),
    level: level,
    module: module,
    accountId: AdsApp.currentAccount().getCustomerId(),
    dryRun: DRY_RUN,
    message: message || '',
    data: data || {}
  };
  Logger.log(JSON.stringify(entry));
}

/**
 * 获取账户时区与当前小时信息
 * @returns {{tz:string,hour:number}} 时区与当前小时（0-23）
 * @throws {Error} 获取失败抛出
 */
function getAccountHourInfo() {
  var tz = AdsApp.currentAccount().getTimeZone();
  var hour = parseInt(Utilities.formatDate(new Date(), tz, 'H'), 10);
  return { tz: tz, hour: hour };
}

/**
 * 拉取 BIDDING_STRATEGY_REPORT 中的 tCPA 策略信息
 * @returns {Object} 映射 { bsrId: {type:string, status:string, targetCpa:number, name:string} }
 * @throws {Error} 报表查询失败抛出
 */
function fetchTargetCpaStrategies() {
  var map = {};
  var q = [
    'SELECT BiddingStrategyId, BiddingStrategyName, BiddingStrategyType, BiddingStrategySystemStatus, TargetCpa',
    'FROM BIDDING_STRATEGY_REPORT'
  ].join(' ');
  var rows = AdsApp.report(q).rows();
  while (rows.hasNext()) {
    var r = rows.next();
    var type = String(r['BiddingStrategyType'] || '');
    if (type === 'TARGET_CPA') {
      var id = String(r['BiddingStrategyId'] || '');
      map[id] = {
        type: type,
        status: String(r['BiddingStrategySystemStatus'] || ''),
        targetCpa: parseFloat(r['TargetCpa'] || '0'),
        name: String(r['BiddingStrategyName'] || '')
      };
    }
  }
  return map;
}

/**
 * 扫描 tCPA 系列：将 Campaign 与其 BiddingStrategy 关联，并计算 CPA 偏离度
 * 偏离度计算：actualCPA = Cost / Conversions（近30天）；diff = actualCPA - targetCpa
 * @returns {Array<Object>} 审计结果列表
 * @throws {Error} 报表查询失败抛出
 */
function scanTargetCpaDeviation() {
  var results = [];
  var strategies = fetchTargetCpaStrategies();
  var q = [
    'SELECT CampaignId, CampaignName, BiddingStrategyId, BiddingStrategyType, Cost, Conversions',
    'FROM CAMPAIGN_PERFORMANCE_REPORT',
    'DURING LAST_30_DAYS'
  ].join(' ');
  var rows = AdsApp.report(q).rows();
  while (rows.hasNext()) {
    var r = rows.next();
    var bstType = String(r['BiddingStrategyType'] || '');
    if (bstType !== 'TARGET_CPA') { continue; }
    var bsrId = String(r['BiddingStrategyId'] || '');
    var st = strategies[bsrId] || null;
    var cost = parseFloat(r['Cost'] || '0');
    var conv = parseFloat(r['Conversions'] || '0');
    var actualCpa = conv > 0 ? (cost / conv) : null;
    var targetCpa = st ? st.targetCpa : null;
    var diff = (actualCpa !== null && targetCpa !== null) ? (actualCpa - targetCpa) : null;
    var ratio = (actualCpa !== null && targetCpa !== null && targetCpa > 0) ? (actualCpa / targetCpa - 1) : null;

    var entry = {
      campaignId: parseInt(r['CampaignId'], 10),
      campaignName: String(r['CampaignName'] || ''),
      biddingStrategyId: bsrId || 'standard',
      biddingStrategyType: bstType,
      systemStatus: st ? st.status : 'UNKNOWN',
      targetCpa: targetCpa,
      actualCpa: actualCpa,
      diff: diff,
      deviationRatio: ratio,
      window: 'LAST_30_DAYS'
    };

    log('info', 'tcpa', 'tCPA 学习状态与CPA偏离度', entry);
    results.push(entry);
  }
  return results;
}

/**
 * 取得广告的 Final URLs（兼容不同广告对象接口）
 * @param {Object} ad AdsApp 广告对象
 * @returns {Array<string>} Final URLs 列表
 * @throws {Error} 无
 */
function safeGetFinalUrls(ad) {
  try {
    if (ad.urls && typeof ad.urls === 'function') {
      var u = ad.urls();
      if (u && typeof u.getFinalUrl === 'function') {
        var fu = u.getFinalUrl();
        return fu ? [fu] : [];
      }
      if (typeof u.getFinalUrls === 'function') {
        var arr = u.getFinalUrls();
        return Array.isArray(arr) ? arr : (arr ? [arr] : []);
      }
    }
    if (typeof ad.getFinalUrls === 'function') {
      var arr2 = ad.getFinalUrls();
      return Array.isArray(arr2) ? arr2 : (arr2 ? [arr2] : []);
    }
  } catch (e) {
    // 忽略，返回空
  }
  return [];
}

/**
 * 落地页扫描：请求 Final URL 并记录 HTTP 返回码
 * 限流：最多检查 50 条启用广告，避免过度请求
 * @returns {Array<Object>} URL 检测结果列表
 * @throws {Error} 请求失败抛出
 */
function scanLandingPages() {
  var results = [];
  var it = AdsApp.ads()
    .withCondition('CampaignStatus = ENABLED')
    .withCondition('AdGroupStatus = ENABLED')
    .withCondition('Status = ENABLED')
    .get();
  var checked = 0;
  while (it.hasNext() && checked < 50) {
    var ad = it.next();
    var urls = safeGetFinalUrls(ad);
    var adGroupId = ad.getAdGroup().getId();
    for (var i = 0; i < urls.length && checked < 50; i++) {
      var u = urls[i];
      try {
        var resp = UrlFetchApp.fetch(u, {
          muteHttpExceptions: true,
          followRedirects: true
        });
        var code = resp.getResponseCode();
        var level = (code === 404 || code >= 500) ? 'warn' : 'info';
        
        var entry = {
          adId: ad.getId ? ad.getId() : null,
          adType: ad.getType ? ad.getType() : null,
          adGroupId: adGroupId,
          url: u,
          statusCode: code
        };
        log(level, 'lp_scan', '落地页返回码检测', entry);
        results.push(entry);
      } catch (e) {
        log('error', 'lp_scan', 'URL 检测异常', {
          url: u,
          error: String(e)
        });
      }
      checked++;
    }
  }
  log('info', 'lp_scan', '落地页扫描完成', { checkedCount: checked });
  return results;
}

/**
 * 获取活动今日消耗（CAMPAIGN_PERFORMANCE_REPORT）
 * @returns {Object} 映射 {campaignId:{name:string,cost:number}}
 * @throws {Error} 报表查询失败抛出
 */
function fetchCampaignCostToday() {
  var map = {};
  var q = [
    'SELECT CampaignId, CampaignName, Cost',
    'FROM CAMPAIGN_PERFORMANCE_REPORT',
    'DURING TODAY'
  ].join(' ');
  var rows = AdsApp.report(q).rows();
  while (rows.hasNext()) {
    var r = rows.next();
    var id = parseInt(r['CampaignId'], 10);
    map[id] = {
      name: String(r['CampaignName'] || ''),
      cost: parseFloat(r['Cost'] || '0')
    };
  }
  return map;
}

/**
 * 获取活动日预算（AdsApp）
 * @returns {Object} 映射 {campaignId:{name:string,budget:number}}
 * @throws {Error} 迭代失败抛出
 */
function fetchCampaignBudgets() {
  var it = AdsApp.campaigns().withCondition('Status = ENABLED').get();
  var budgets = {};
  while (it.hasNext()) {
    var c = it.next();
    budgets[c.getId()] = {
      name: c.getName(),
      budget: c.getBudget().getAmount()
    };
  }
  return budgets;
}

/**
 * 预算耗尽小时估算：基于今日已消耗与当前小时的平均每小时消耗
 * @returns {void}
 * @throws {Error} 计算失败抛出
 */
function estimateBudgetDepletionHour() {
  var hourInfo = getAccountHourInfo();
  var costToday = fetchCampaignCostToday();
  var budgets = fetchCampaignBudgets();

  var ids = Object.keys(budgets);
  for (var i = 0; i < ids.length; i++) {
    var cid = parseInt(ids[i], 10);
    var budget = budgets[cid].budget;
    var name = budgets[cid].name;
    var cost = (costToday[cid] && costToday[cid].cost) ? costToday[cid].cost : 0;
    var hoursElapsed = Math.max(1, hourInfo.hour); // 避免除以0
    var avgHourly = cost / hoursElapsed;
    var remaining = Math.max(0, budget - cost);
    var hoursToDeplete = avgHourly > 0 ? (remaining / avgHourly) : null;
    var estHour = (hoursToDeplete !== null) ? ((hourInfo.hour + Math.ceil(hoursToDeplete)) % 24) : null;

    log('info', 'budget_risk', '预算耗尽小时估算', {
      campaignId: cid,
      campaignName: name,
      dailyBudget: budget.toFixed(2),
      spentToday: cost.toFixed(2),
      hourNow: hourInfo.hour,
      avgHourlySpend: avgHourly !== null ? Number(avgHourly.toFixed(2)) : null,
      remainingBudget: Number(remaining.toFixed(2)),
      hoursToDeplete: hoursToDeplete !== null ? Number(hoursToDeplete.toFixed(2)) : null,
      estimatedDepletionHour: estHour
    });
  }
}

/**
 * 将审计数据同步到 Google Sheets
 * @param {Array<Object>} biddingData 出价审计数据
 * @param {Array<Object>} urlData URL 风险数据
 */
function syncToSpreadsheet(biddingData, urlData) {
  if (DRY_RUN) {
    log('info', 'sync', 'Dry Run 模式：跳过表格写入', {
      biddingCount: biddingData.length,
      urlCount: urlData.length
    });
    return;
  }

  try {
    var ss = SpreadsheetApp.openByUrl(SPREADSHEET_URL);
    if (!ss) throw new Error('无法打开表格');

    // 1. Bidding_Audit Sync
    var sheetBid = ss.getSheetByName('Bidding_Audit');
    if (!sheetBid) sheetBid = ss.insertSheet('Bidding_Audit');
    
    // 清空旧数据（保留表头区域，简单起见清空全表后重写表头，或者清除内容）
    // 为了防止表头格式丢失，最好清除第2行之后的数据
    if (sheetBid.getLastRow() > 1) {
      sheetBid.getRange(2, 1, sheetBid.getLastRow() - 1, sheetBid.getLastColumn()).clearContent();
      // 清除背景色和字体颜色（重置）
      sheetBid.getRange(2, 1, sheetBid.getLastRow() - 1, sheetBid.getLastColumn()).setBackground(null).setFontColor(null);
    }
    
    var headersBid = ['Campaign Name', 'Learning Status', 'Target CPA', 'Actual CPA', 'Deviation Ratio'];
    // 检查表头是否一致，不一致则覆盖
    var headerRange = sheetBid.getRange(1, 1, 1, headersBid.length);
    if (sheetBid.getLastRow() === 0 || headerRange.getValues()[0][0] !== headersBid[0]) {
      headerRange.setValues([headersBid]);
      headerRange.setFontWeight('bold');
    }

    if (biddingData.length > 0) {
      var rowsBid = biddingData.map(function(item) {
        return [
          item.campaignName,
          item.systemStatus,
          item.targetCpa,
          item.actualCpa,
          item.deviationRatio
        ];
      });
      
      var writeRange = sheetBid.getRange(2, 1, rowsBid.length, rowsBid[0].length);
      writeRange.setValues(rowsBid);
      
      // 格式化：Deviation Ratio > 0.2 标红
      var backgrounds = [];
      var fontColors = [];
      for (var i = 0; i < biddingData.length; i++) {
        var ratio = biddingData[i].deviationRatio;
        var isAlert = (ratio !== null && ratio > 0.2);
        var rowBg = isAlert ? '#FF0000' : null;
        var rowFont = isAlert ? '#FFFFFF' : null;
        
        var rowBgArr = [];
        var rowFontArr = [];
        for (var j = 0; j < headersBid.length; j++) {
            rowBgArr.push(rowBg);
            rowFontArr.push(rowFont);
        }
        backgrounds.push(rowBgArr);
        fontColors.push(rowFontArr);
      }
      writeRange.setBackgrounds(backgrounds);
      writeRange.setFontColors(fontColors);
    }

    // 2. URL_Alerts Sync
    var sheetUrl = ss.getSheetByName('URL_Alerts');
    if (!sheetUrl) sheetUrl = ss.insertSheet('URL_Alerts');
    
    if (sheetUrl.getLastRow() > 1) {
      sheetUrl.getRange(2, 1, sheetUrl.getLastRow() - 1, sheetUrl.getLastColumn()).clearContent();
    }

    var headersUrl = ['Final URL', 'Status Code', 'Ad Group ID'];
    var headerRangeUrl = sheetUrl.getRange(1, 1, 1, headersUrl.length);
    if (sheetUrl.getLastRow() === 0 || headerRangeUrl.getValues()[0][0] !== headersUrl[0]) {
      headerRangeUrl.setValues([headersUrl]);
      headerRangeUrl.setFontWeight('bold');
    }
    
    var badUrls = urlData.filter(function(item) { return item.statusCode !== 200; });
    
    if (badUrls.length > 0) {
        var rowsUrl = badUrls.map(function(item) {
            return [
                item.url,
                item.statusCode,
                item.adGroupId
            ];
        });
        sheetUrl.getRange(2, 1, rowsUrl.length, rowsUrl[0].length).setValues(rowsUrl);
    }

    log('info', 'sync', '表格同步完成', {
        biddingRows: biddingData.length,
        urlAlerts: badUrls.length
    });

  } catch (e) {
    log('error', 'sync', '表格同步失败', { error: String(e) });
  }
}

/**
 * 主入口：执行三项健康度扫描
 * @returns {void}
 * @throws {Error} 任一步骤失败时抛出
 */
function main() {
  log('info', 'bootstrap', '账户底层健康度扫描启动', { dryRun: DRY_RUN });

  // 0. 检查表格访问（快速失败）
  if (!DRY_RUN) {
    try {
      var ss = SpreadsheetApp.openByUrl(SPREADSHEET_URL);
      if (!ss) throw new Error('Spreadsheet inaccessible');
    } catch (e) {
      log('error', 'bootstrap', '无法访问 Google Sheets，请检查 URL 或权限', { error: String(e) });
      return; // 终止执行
    }
  }

  // 功能 A：tCPA 出价透视
  var biddingData = scanTargetCpaDeviation();

  // 功能 B：落地页返回码扫描
  var urlData = scanLandingPages();

  // 功能 C：预算风险估算
  estimateBudgetDepletionHour();

  // 功能 D：数据同步
  syncToSpreadsheet(biddingData, urlData);

  log('info', 'complete', '账户底层健康度扫描完成', {});
}

