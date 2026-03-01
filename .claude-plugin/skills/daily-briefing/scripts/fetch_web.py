#!/usr/bin/env python3
"""
网页内容抓取脚本
从配置文件中的网页URL抓取并提取内容
"""

import json
import logging
import re
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


def fetch_web_content(url: str) -> Dict[str, str]:
    """
    从单个网页抓取内容

    Args:
        url: 网页URL

    Returns:
        包含标题、链接、描述的字典
    """
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        logger.error("依赖库未安装，请运行: pip install requests beautifulsoup4")
        return {}

    logger.info(f"正在抓取网页: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取标题
        title = soup.find('h1')
        if title:
            title = title.get_text(strip=True)
        else:
            title_tag = soup.find('title')
            title = title_tag.get_text(strip=True) if title_tag else '无标题'

        # 提取描述（尝试meta description或第一段）
        description = ''

        # 尝试meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content', '')

        # 如果没有meta description，尝试第一段
        if not description:
            first_p = soup.find('p')
            if first_p:
                description = first_p.get_text(strip=True)

        # 提取页面中的链接（用于相关文章）
        links = []
        for link in soup.find_all('a', href=True)[:10]:
            href = link['href']
            if href.startswith('http'):
                link_text = link.get_text(strip=True)
                if link_text:
                    links.append({'text': link_text, 'url': href})

        result = {
            'title': title,
            'link': url,
            'description': clean_description(description),
            'published': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'source': 'web',
            'source_url': url,
            'related_links': links[:5]  # 最多5个相关链接
        }

        logger.info(f"从 {url} 成功抓取内容")
        return result

    except Exception as e:
        logger.error(f"抓取 {url} 失败: {e}")
        return {}


def clean_description(description: str, max_length: int = 200) -> str:
    """
    清理描述文本

    Args:
        description: 原始描述
        max_length: 最大长度

    Returns:
        清理后的描述
    """
    # 移除多余的空白
    description = re.sub(r'\s+', ' ', description)
    description = description.strip()

    # 截断过长文本
    if len(description) > max_length:
        description = description[:max_length-3] + '...'

    return description


def main():
    parser = argparse.ArgumentParser(description='从网页抓取内容')
    parser.add_argument('--config', default='assets/config.yaml', help='配置文件路径')
    parser.add_argument('--urls', help='额外的网页URL，用逗号分隔')
    parser.add_argument('--output', default='data/web_content.json', help='输出文件路径')
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

        # 抓取配置中的网页
        web_urls = topic.get('web_urls', [])
        for url in web_urls:
            item = fetch_web_content(url)
            if item:
                item['topic'] = topic_name
                all_items.append(item)
                logs.append(f"从 {url} 获取内容成功")

    # 处理额外的URL
    if args.urls:
        logger.info("处理额外的URL")
        extra_urls = args.urls.split(',')
        for url in extra_urls:
            url = url.strip()
            if url:
                item = fetch_web_content(url)
                if item:
                    item['topic'] = '额外'  # 额外URL归为"额外"主题
                    all_items.append(item)
                    logs.append(f"从额外URL {url} 获取内容")

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
