#!/usr/bin/env python3
"""
RSS源抓取脚本
从配置文件中的RSS/Atom订阅源抓取内容
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import argparse

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def load_config(config_path: str) -> Dict[str, Any]:
    """加载配置文件"""
    import yaml
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def fetch_rss_feed(url: str, max_items: int = 10) -> List[Dict[str, str]]:
    """
    从单个RSS源抓取内容

    Args:
        url: RSS源的URL
        max_items: 最多抓取的条目数

    Returns:
        包含标题、链接、描述的字典列表
    """
    try:
        import feedparser
    except ImportError:
        logger.error("feedparser未安装，请运行: pip install feedparser")
        return []

    logger.info(f"正在抓取RSS源: {url}")
    feed = feedparser.parse(url)

    items = []
    for entry in feed.entries[:max_items]:
        # 获取发布时间
        published = entry.get('published', entry.get('updated', ''))

        items.append({
            'title': entry.get('title', '无标题'),
            'link': entry.get('link', ''),
            'description': entry.get('description', entry.get('summary', '')),
            'published': published,
            'source': 'rss',
            'source_url': url
        })

    logger.info(f"从 {url} 获取了 {len(items)} 条内容")
    return items


def clean_description(description: str, max_length: int = 200) -> str:
    """
    清理描述文本，移除HTML标签并截断

    Args:
        description: 原始描述
        max_length: 最大长度

    Returns:
        清理后的描述
    """
    from html.parser import HTMLParser

    class HTMLCleaner(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text = []

        def handle_data(self, data):
            self.text.append(data)

    cleaner = HTMLCleaner()
    cleaner.feed(description)
    text = ''.join(cleaner.text).strip()

    # 截断过长文本
    if len(text) > max_length:
        text = text[:max_length-3] + '...'

    return text


def main():
    parser = argparse.ArgumentParser(description='从RSS源抓取内容')
    parser.add_argument('--config', default='assets/config.yaml', help='配置文件路径')
    parser.add_argument('--output', default='data/rss_content.json', help='输出文件路径')
    parser.add_argument('--max-items', type=int, default=10, help='每个源最多抓取条目数')
    args = parser.parse_args()

    # 加载配置
    config = load_config(args.config)

    # 确保输出目录存在
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    all_items = []
    logs = []

    # 遍历所有主题
    for topic in config.get('topics', []):
        topic_name = topic.get('name', '未分类')
        logger.info(f"处理主题: {topic_name}")

        # 抓取RSS源
        rss_feeds = topic.get('rss_feeds', [])
        for feed_url in rss_feeds:
            items = fetch_rss_feed(feed_url, args.max_items)
            for item in items:
                item['topic'] = topic_name
                item['description'] = clean_description(item['description'])
                all_items.append(item)

            logs.append(f"从 {feed_url} 获取了 {len(items)} 条内容")

    # 保存结果
    result = {
        'fetch_time': datetime.now().isoformat(),
        'total_items': len(all_items),
        'logs': logs,
        'items': all_items
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    logger.info(f"共抓取 {len(all_items)} 条内容，已保存到 {output_path}")


if __name__ == '__main__':
    main()
