# 配置文件格式说明

## 配置文件结构 (config.yaml)

```yaml
# 主题列表
topics:
  # 主题1
  - name: "主题名称"
    # RSS/Atom订阅源列表
    rss_feeds:
      - "https://example.com/rss1"
      - "https://example.com/rss2"
    # 网页URL列表
    web_urls:
      - "https://example.com/page1"
      - "https://example.com/page2"

  # 主题2
  - name: "另一个主题"
    rss_feeds:
      - "https://example.com/feed"
    web_urls: []
```

## 配置项说明

### topics (必需)

主题列表，每个主题包含以下字段：

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| name | string | 是 | 主题名称，用于分类显示 |
| rss_feeds | array | 否 | RSS/Atom订阅源URL列表 |
| web_urls | array | 否 | 网页URL列表 |

### RSS源要求

- 必须是有效的RSS或Atom格式
- URL必须以http://或https://开头
- 建议使用可靠的RSS源

### 网页URL要求

- 必须是有效的HTTP/HTTPS URL
- 网页应可正常访问
- 某些网站可能有反爬虫机制

## 配置示例

### 技术新闻简报

```yaml
topics:
  - name: "前端开发"
    rss_feeds:
      - "https://css-tricks.com/feed/"
      - "https://www.smashingmagazine.com/feed/"
    web_urls:
      - "https://developer.mozilla.org/zh-CN/news/"

  - name: "后端开发"
    rss_feeds:
      - "https://blog.cloudflare.com/rss/"
      - "https://engineering.fb.com/feed/"
    web_urls: []

  - name: "AI/ML"
    rss_feeds:
      - "https://openai.com/blog/rss.xml"
    web_urls:
      - "https://arxiv.org/list/cs.AI/recent"
```

### 综合新闻简报

```yaml
topics:
  - name: "科技"
    rss_feeds:
      - "https://techcrunch.com/feed/"
      - "https://www.theverge.com/rss/index.xml"
    web_urls: []

  - name: "财经"
    rss_feeds:
      - "https://www.bloomberg.com/feed"
    web_urls:
      - "https://finance.yahoo.com/news"

  - name: "设计"
    rss_feeds:
      - "https://www.designboom.com/feed/"
    web_urls: []
```

## 命令行参数

### fetch_rss.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| --config | 配置文件路径 | assets/config.yaml |
| --output | 输出JSON文件路径 | data/rss_content.json |
| --max-items | 每个源最多抓取条目数 | 10 |

### fetch_web.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| --config | 配置文件路径 | assets/config.yaml |
| --urls | 额外的网页URL（逗号分隔） | 无 |
| --output | 输出JSON文件路径 | data/web_content.json |

### generate_report.py

| 参数 | 说明 | 默认值 |
|------|------|--------|
| --config | 配置文件路径 | assets/config.yaml |
| --template | 模板文件路径 | assets/template.md |
| --extra-urls | 额外的网页URL（逗号分隔） | 无 |
| --output | 输出Markdown文件路径 | daily_report.md |
| --data-dir | 数据文件存储目录 | data |
| --skip-fetch | 跳过抓取，使用已有数据 | false |

## 依赖安装

```bash
# RSS抓取依赖
pip install feedparser

# 网页抓取依赖
pip install requests beautifulsoup4

# 配置文件解析依赖
pip install pyyaml
```

或一次性安装所有依赖：

```bash
pip install feedparser requests beautifulsoup4 pyyaml
```
