# FocusGEO Skills

> 让 AI 大模型在回答中**主动推荐你的品牌**。

FocusGEO Skills 是基于 **GEO（生成式引擎优化）** 方法论的 AI 助手技能集，包含两个互补的 Skill，帮助企业完成 FocusGEO 系统的全流程配置，最终产出一套可直接落地的 GEO 内容策略。

---

## 什么是 GEO？

**GEO = Generative Engine Optimization = AI 搜索推荐优化**

| | 传统 SEO | GEO |
|---|---|---|
| **目标** | 让搜索引擎找到你 | 让 AI 大模型**推荐**你 |
| **优化对象** | 搜索引擎爬虫 | DeepSeek、豆包、文心一言、通义千问等大模型 |
| **核心策略** | 关键词密度、外链权重 | 结构化内容投喂、权威性锚定、多平台覆盖 |

**三条核心法则：**

1. **结构化投喂** — 你在多个平台发布的每一条内容，都是对 AI 的一次"训练"。信息越结构化、越一致，AI 识别越精准。
2. **权威性锚定** — AI 更倾向于引用信息密度高、有具体数据、有明确来源的内容。
3. **多模态覆盖** — 文本 + 图片 + 文档的组合投喂，比单一文本更容易被 AI 多维度识别。

---

## 技能一览

### `focus-geo-config` — 全流程配置向导

通过 **6 阶段深度对话**，引导用户完成 FocusGEO 系统的完整配置，产出可直接执行的《FocusGEO 实操配置手册》。

**配置流程：**

```
企业画像配置 → 关键词策略制定 → 知识库规划
    → GEO 提示词设计 → 多平台改编策略 → 配置手册生成
```

**产出物：** 《FocusGEO 实操配置手册》完整文档

**参考资源：** 内置 6 份参考文档（企业画像模板、关键词策略指南、知识库规划规范、提示词设计模板、平台改编指南、手册生成模板）

---

### `focusgeo-coach` — 实操配置教练

通过 **6 阶段对话式引导**，在教练节奏中完成配置，包含自动脚本辅助，并产出含 48 小时行动清单的可执行手册。

**对话流程：**

```
开场（官网分析）→ 企业画像（自动提取+对话补充）
→ 核心关键词蒸馏（AI 对话式问法）→ 自动组合词库构建
→ 知识库与图片配置 → GEO 内容生成策略 → 多平台改编策略
```

**内置脚本支持：**

| 脚本 | 功能 |
|---|---|
| `analyze_website.py` | 从官网 URL 自动提取企业画像基础信息 |
| `recommend_keywords.py` | 基于产品描述推荐行业核心关键词 |

**产出物：** 《FocusGEO 实操配置手册》+ 48 小时行动清单

---

## 两个 Skill 的区别

| 对比维度 | `focus-geo-config` | `focusgeo-coach` |
|---|---|---|
| **风格** | 结构化操作手册 | 带节奏的教练引导脚本 |
| **对话策略** | 分阶段收集信息 | 一次只问一个问题，追问到底 |
| **脚本支持** | 无 | 有（自动抓取官网、推荐关键词） |
| **关键词策略** | SEO 关键词体系 | AI 对话式完整问句（GEO 关键词） |
| **落地性** | 通用配置模板 | 含 48 小时行动清单，可立刻执行 |
| **参考文档** | 6 份参考文档 | 2 个脚本工具 |

---

## 快速开始

### 方式一：使用 Coach（推荐新手）

```
1. 克隆本仓库
2. 在 AI 助手中加载 focusgeo-coach/SKILL.md
3. 按对话引导完成 6 阶段配置
4. 获得《FocusGEO 实操配置手册》
```

### 方式二：使用 Config（自主配置）

```
1. 克隆本仓库
2. 在 AI 助手中加载 focus-geo-config/SKILL.md
3. 按 6 阶段流程自主填写配置
4. 参考 references/ 目录下的文档完善各阶段产出
```

---

## 目录结构

```
focusgeo-skills/
├── focus-geo-config/                  # 全流程配置向导
│   ├── README.md
│   ├── SKILL.md                      # Skill 定义文件
│   └── references/                   # 参考文档
│       ├── enterprise-profile-template.md    # 企业画像模板
│       ├── geo-prompt-design.md             # GEO 提示词设计
│       ├── keyword-strategy-guide.md        # 关键词策略指南
│       ├── knowledge-base-planning.md      # 知识库规划
│       ├── manual-generation-template.md    # 手册生成模板
│       └── platform-adaptation-guide.md     # 平台改编指南
│
└── focusgeo-coach/                   # 实操配置教练
    ├── README.md
    ├── SKILL.md                     # Skill 定义文件
    └── scripts/                      # 辅助脚本
        ├── analyze_website.py       # 官网分析脚本
        └── recommend_keywords.py    # 关键词推荐脚本
```

---

## 方法论来源

- 《生成式引擎优化(GEO):原理、方法、案例及主流AI搜索引擎策略深度解析》
- FocusGEO v4.0 使用手册

---

## License

MIT
