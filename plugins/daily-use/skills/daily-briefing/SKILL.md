---
name: daily-briefing
description: 每日简报生成技能。当用户需要生成包含多个主题、从指定网址或RSS源抓取内容的每日简报时使用此技能。支持定时自动生成和按需手动生成，输出Markdown格式简报，包含标题、一句话简介、链接和操作日志。
---

# 每日简报技能 (Daily Briefing)

## 技能目的

此技能用于生成结构化的每日简报，从多个来源（网页和RSS源）抓取内容，并输出为Markdown格式的简报文档。

简报包含以下内容：
- 主题分类
- 每条新闻的标题
- 一句话简介
- 原文链接
- 操作日志（记录抓取过程）

## 何时使用

在以下场景使用此技能：

1. **定时自动生成**：每天自动收集指定主题的最新资讯
2. **按需手动生成**：需要时手动触发生成简报
3. **自定义主题**：用户可以指定任意主题领域（技术、新闻、金融等）
4. **混合来源**：从配置文件预设的网址和临时提供的网址中获取内容

## 如何使用

### 1. 准备配置文件

首先创建或编辑配置文件 `assets/config.yaml`，配置源网址和主题：

```yaml
# 配置文件示例
topics:
  - name: "技术"
    rss_feeds:
      - "https://example.com/tech/rss"
    web_urls:
      - "https://example.com/tech-news"
  - name: "新闻"
    rss_feeds:
      - "https://example.com/news/rss"
```

### 2. 抓取内容

使用提供的脚本抓取内容：

**抓取RSS源：**
```bash
python scripts/fetch_rss.py --config assets/config.yaml
```

**抓取网页内容：**
```bash
python scripts/fetch_web.py --config assets/config.yaml
```

### 3. 生成简报

使用生成脚本创建Markdown简报：

```bash
python scripts/generate_report.py --input data/fetched_content.json --output daily_report.md
```

### 4. 直接生成（一键流程）

也可以使用一键命令完成所有步骤：

```bash
python scripts/generate_report.py --config assets/config.yaml --output daily_report.md
```

### 5. 临时添加额外网址

如果需要临时添加配置文件之外的网址：

```bash
python scripts/generate_report.py --config assets/config.yaml --extra-urls "https://example.com/extra1,https://example.com/extra2" --output daily_report.md
```

## 技能资源

### 脚本 (scripts/)

- **fetch_rss.py**: 从RSS/Atom订阅源抓取内容
- **fetch_web.py**: 从网页抓取并提取内容
- **generate_report.py**: 主生成脚本，协调抓取和简报生成

### 参考文档 (references/)

- **config_schema.md**: 配置文件格式和参数说明

### 资产文件 (assets/)

- **config.yaml**: 配置文件模板
- **template.md**: 简报输出模板

## 输出格式示例

```markdown
# 每日简报 - 2026-03-01

## 操作日志

- [08:00] 开始抓取内容...
- [08:01] 从3个RSS源获取12条内容
- [08:02] 从5个网页获取8条内容
- [08:05] 简报生成完成

## 技术

### [新框架发布](https://example.com/article1)
某框架发布了2.0版本，带来了性能提升和新特性。

### [AI研究突破](https://example.com/article2)
研究人员在机器学习领域取得重要进展。

## 新闻

### [行业动态](https://example.com/article3)
某公司发布新产品，引起市场关注。
```

## 注意事项

1. 确保网络连接正常，脚本需要访问外部网址
2. 某些网站可能有反爬虫机制，请遵守robots.txt
3. RSS源需要是有效的RSS/Atom格式
4. 建议每日定时运行脚本获取最新内容
