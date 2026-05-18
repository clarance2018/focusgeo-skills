# 企业画像结构化模板

## 概览
本文档提供企业画像的标准结构，用于在FocusGEO配置阶段1中收集和整理企业基础信息。

## 核心内容

### 1. 基础信息
**字段说明**：
- `enterprise_name`：企业/品牌名称
- `industry`：所属行业（具体到细分领域）
- `scale`：企业规模（人数/营收/级别）
- `business_model`：业务模式（B2B/B2C/O2O等）
- `established_year`：成立年份
- `location`：总部/主要服务区域

**示例**：
```yaml
enterprise_name: 智云科技
industry: 企业级SaaS服务/CRM系统
scale: 100-500人/年营收5000万-1亿
business_model: B2B SaaS订阅
established_year: 2018
location: 北京/全国
```

---

### 2. 品牌定位
**字段说明**：
- `brand_tone`：品牌语调（专业/亲切/严谨/活泼等）
- `core_values`：核心价值主张（2-3个）
- `differentiation`：差异化优势（2-3个）
- `brand_mission`：品牌使命
- `brand_vision`：品牌愿景

**示例**：
```yaml
brand_tone: 专业、可靠、高效
core_values:
  - 简单易用
  - 持续创新
  - 客户成功
differentiation:
  - 业界首创的AI智能推荐
  - 7x24小时专属客户成功团队
  - 开放API生态，无缝集成
brand_mission: 让中小企业轻松拥有专业的客户管理系统
brand_vision: 成为中国CRM领域的领导者
```

---

### 3. 目标用户
**字段说明**：
- `primary_audience`：核心用户群体
- `user_personas`：用户画像（3-5个关键特征）
- `pain_points`：用户痛点
- `decision_factors`：决策影响因素
- `user_scenarios`：使用场景

**示例**：
```yaml
primary_audience: 中小企业CEO/销售总监/运营负责人
user_personas:
  - 年龄：25-40岁
  - 行业：互联网/零售/服务业
  - 规模：20-200人
  - 痛点：客户管理混乱、数据分散、效率低下
pain_points:
  - 客户信息分散在各个工具中
  - 销售流程不透明，难以追踪
  - 缺乏数据驱动决策的能力
decision_factors:
  - 易用性（上手难度）
  - 性价比（功能vs价格）
  - 集成能力（与现有系统对接）
  - 售后服务（技术支持质量）
user_scenarios:
  - 新客户录入与分配
  - 销售机会跟进管理
  - 客户数据分析与报表
```

---

### 4. 业务目标
**字段说明**：
- `geo_objectives`：GEO期望效果（可量化）
- `key_metrics`：关键指标（KPI）
- `time_horizon`：时间周期
- `current_challenges`：当前面临的挑战
- `success_criteria`：成功标准

**示例**：
```yaml
geo_objectives:
  - 提升品牌在搜索结果中的可见度
  - 增加自然流量，降低获客成本
  - 建立行业权威形象
key_metrics:
  - 搜索排名：核心关键词Top 3达到50%
  - 自然流量：月均增长20%
  - 内容曝光：月均阅读量10万+
  - 线索获取：每月通过GEO获取有效线索100+
time_horizon: 6个月（短期目标）/12个月（长期目标）
current_challenges:
  - 现有内容质量参差不齐
  - 缺乏系统化的关键词策略
  - 内容分发渠道单一
success_criteria:
  - 6个月内核心关键词排名提升30%
  - 自然流量增长100%
  - GEO贡献的线索占比达到40%
```

---

### 5. 现有资源
**字段说明**：
- `existing_content`：现有内容资产（类型/数量/质量）
- `brand_assets`：品牌资料（Logo/VI/品牌手册等）
- `team_resources`：团队资源（内容团队/技术支持/预算）
- `platforms`：现有平台账号（名称/粉丝量/活跃度）

**示例**：
```yaml
existing_content:
  - 官网博客：50篇，质量中等
  - 产品文档：20篇，质量较高
  - 视频教程：10个，质量一般
brand_assets:
  - Logo：有
  - VI系统：有
  - 品牌手册：有
team_resources:
  - 内容团队：3人（编辑1人/设计1人/视频1人）
  - 技术支持：外包
  - 内容预算：月均2万元
platforms:
  - 微信公众号：企业名称，粉丝2万，周更2次
  - 知乎机构号：企业名称，粉丝5000，月更4次
  - 抖音号：企业名称，粉丝1万，周更3次
```

## 验证规则

### 必填字段
- `enterprise_name`、`industry`、`business_model`
- `brand_tone`、`core_values`（至少2个）
- `primary_audience`、`user_personas`（至少3个特征）
- `geo_objectives`（至少1个可量化目标）
- `key_metrics`（至少2个指标）

### 完整性检查
- [ ] 品牌定位清晰（不超过3个核心价值）
- [ ] 目标用户画像具体（包含3-5个关键特征）
- [ ] 业务目标可量化（包含明确的KPI指标）
- [ ] 差异化优势明确（2-3个独特卖点）
- [ ] 现有资源清单完整（内容/平台/团队）

### 一致性检查
- [ ] 品牌语调与目标用户匹配
- [ ] 业务目标与行业特点相符
- [ ] 现有资源与业务目标匹配

## 常见问题

**Q1：用户提供的品牌定位过于模糊怎么办？**
A：通过追问引导用户具体化，例如：
- "专业"具体体现在哪些方面？（技术实力/服务品质/行业经验等）
- "创新"具体指什么？（产品功能/商业模式/服务方式等）

**Q2：用户对目标用户描述不清晰怎么办？**
A：引导用户从以下维度描述：
- 人群属性（年龄/性别/职业/地域等）
- 需求特征（痛点/需求/期望等）
- 行为习惯（信息获取渠道/决策方式等）

**Q3：业务目标无法量化怎么办？**
A：引导用户将模糊目标转化为可衡量指标：
- "提升品牌影响力"→"搜索曝光量增长X%/品牌词搜索量增长X%"
- "获取更多客户"→"每月通过GEO获取有效线索X个"
- "建立行业权威"→"核心关键词Top 3占比达到X%"

## 示例

### 完整示例（B2B SaaS企业）
```yaml
enterprise_name: 智云科技
industry: 企业级SaaS服务/CRM系统
scale: 100-500人/年营收5000万-1亿
business_model: B2B SaaS订阅
established_year: 2018
location: 北京/全国

brand_tone: 专业、可靠、高效
core_values:
  - 简单易用
  - 持续创新
  - 客户成功
differentiation:
  - 业界首创的AI智能推荐
  - 7x24小时专属客户成功团队
  - 开放API生态，无缝集成
brand_mission: 让中小企业轻松拥有专业的客户管理系统
brand_vision: 成为中国CRM领域的领导者

primary_audience: 中小企业CEO/销售总监/运营负责人
user_personas:
  - 年龄：25-40岁
  - 行业：互联网/零售/服务业
  - 规模：20-200人
  - 痛点：客户管理混乱、数据分散、效率低下
pain_points:
  - 客户信息分散在各个工具中
  - 销售流程不透明，难以追踪
  - 缺乏数据驱动决策的能力
decision_factors:
  - 易用性（上手难度）
  - 性价比（功能vs价格）
  - 集成能力（与现有系统对接）
  - 售后服务（技术支持质量）
user_scenarios:
  - 新客户录入与分配
  - 销售机会跟进管理
  - 客户数据分析与报表

geo_objectives:
  - 提升品牌在搜索结果中的可见度
  - 增加自然流量，降低获客成本
  - 建立行业权威形象
key_metrics:
  - 搜索排名：核心关键词Top 3达到50%
  - 自然流量：月均增长20%
  - 内容曝光：月均阅读量10万+
  - 线索获取：每月通过GEO获取有效线索100+
time_horizon: 6个月（短期目标）/12个月（长期目标）
current_challenges:
  - 现有内容质量参差不齐
  - 缺乏系统化的关键词策略
  - 内容分发渠道单一
success_criteria:
  - 6个月内核心关键词排名提升30%
  - 自然流量增长100%
  - GEO贡献的线索占比达到40%

existing_content:
  - 官网博客：50篇，质量中等
  - 产品文档：20篇，质量较高
  - 视频教程：10个，质量一般
brand_assets:
  - Logo：有
  - VI系统：有
  - 品牌手册：有
team_resources:
  - 内容团队：3人（编辑1人/设计1人/视频1人）
  - 技术支持：外包
  - 内容预算：月均2万元
platforms:
  - 微信公众号：企业名称，粉丝2万，周更2次
  - 知乎机构号：企业名称，粉丝5000，月更4次
  - 抖音号：企业名称，粉丝1万，周更3次
```
