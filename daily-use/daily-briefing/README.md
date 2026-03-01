# 每日简报技能 (Daily News)

一个自动化生成每日简报的技能，支持从RSS源和网页抓取内容，输出结构化的Markdown格式简报。

## 功能特性

- 支持多个主题分类
- 支持RSS/Atom订阅源和网页内容抓取
- 配置文件预设 + 临时添加额外网址
- 自动提取标题、简介和链接
- 包含操作日志
- 输出Markdown格式简报

## 安装

1. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 配置源

编辑 `assets/config.yaml`，添加你想抓取的RSS源和网页URL：

```yaml
topics:
  - name: "技术"
    rss_feeds:
      - "https://example.com/rss"
    web_urls:
      - "https://example.com/news"
```

### 2. 生成简报

一键生成（推荐）：
```bash
python scripts/generate_report.py --output daily_report.md
```

单独使用各脚本：
```bash
# 只抓取RSS
python scripts/fetch_rss.py --config assets/config.yaml

# 只抓取网页
python scripts/fetch_web.py --config assets/config.yaml

# 生成简报
python scripts/generate_report.py --output daily_report.md
```

### 3. 添加临时URL

```bash
python scripts/generate_report.py --extra-urls "https://example.com/extra1,https://example.com/extra2" --output daily_report.md
```

## 命令行参数

详见 `references/config_schema.md`

## 输出示例

```markdown
# 每日简报 - 2026-03-01

## 操作日志

- [08:00] 开始抓取内容...
- [08:01] 从3个RSS源获取12条内容
- [08:02] 简报生成完成

## 技术

### [新框架发布](https://example.com/article1)
某框架发布了2.0版本，带来了性能提升和新特性。
```

## 目录结构

```
daily-briefing/
├── SKILL.md              # 技能说明文档
├── README.md             # 使用说明
├── requirements.txt      # 依赖列表
├── scripts/              # 脚本目录
│   ├── fetch_rss.py      # RSS抓取脚本
│   ├── fetch_web.py      # 网页抓取脚本
│   └── generate_report.py # 主生成脚本
├── references/           # 参考文档
│   └── config_schema.md  # 配置格式说明
└── assets/               # 资产文件
    ├── config.yaml       # 配置文件模板
    └── template.md       # 简报模板
```
