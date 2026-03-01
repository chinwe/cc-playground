#!/usr/bin/env python3
"""
每日简报生成主脚本
协调RSS和网页抓取，生成Markdown格式简报
"""

import json
import logging
import subprocess
import sys
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


def load_template(template_path: str) -> str:
    """加载模板文件"""
    if Path(template_path).exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def generate_markdown_report(items: List[Dict[str, Any]], logs: List[str], date: str) -> str:
    """
    生成Markdown格式的简报

    Args:
        items: 所有抓取的内容项
        logs: 操作日志
        date: 简报日期

    Returns:
        Markdown格式的简报内容
    """
    lines = []

    # 标题
    lines.append(f"# 每日简报 - {date}")
    lines.append("")

    # 操作日志
    lines.append("## 操作日志")
    lines.append("")
    for log in logs:
        lines.append(f"- {log}")
    lines.append("")

    # 按主题分组
    topics = {}
    for item in items:
        topic = item.get('topic', '未分类')
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(item)

    # 生成各主题内容
    for topic_name, topic_items in topics.items():
        lines.append(f"## {topic_name}")
        lines.append("")

        for item in topic_items:
            title = item.get('title', '无标题')
            link = item.get('link', '')
            description = item.get('description', '')

            # Markdown格式: [标题](链接)
            if link:
                lines.append(f"### [{title}]({link})")
            else:
                lines.append(f"### {title}")

            lines.append("")
            lines.append(f"{description}")
            lines.append("")

            # 添加相关链接（如果有）
            if 'related_links' in item and item['related_links']:
                lines.append("**相关链接:**")
                for rel in item['related_links']:
                    lines.append(f"- [{rel['text']}]({rel['url']})")
                lines.append("")

    return '\n'.join(lines)


def run_fetch_rss(config_path: str, output_path: str) -> bool:
    """运行RSS抓取脚本"""
    try:
        script_path = Path(__file__).parent / 'fetch_rss.py'
        result = subprocess.run(
            [sys.executable, str(script_path), '--config', config_path, '--output', output_path],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        logger.error(f"运行RSS抓取脚本失败: {e}")
        return False


def run_fetch_web(config_path: str, output_path: str, extra_urls: str = None) -> bool:
    """运行网页抓取脚本"""
    try:
        script_path = Path(__file__).parent / 'fetch_web.py'
        cmd = [sys.executable, str(script_path), '--config', config_path, '--output', output_path]
        if extra_urls:
            cmd.extend(['--urls', extra_urls])

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception as e:
        logger.error(f"运行网页抓取脚本失败: {e}")
        return False


def merge_results(rss_path: str, web_path: str) -> tuple[List[Dict], List[str]]:
    """合并RSS和网页抓取结果"""
    all_items = []
    all_logs = []

    # 读取RSS结果
    if Path(rss_path).exists():
        with open(rss_path, 'r', encoding='utf-8') as f:
            rss_data = json.load(f)
            all_items.extend(rss_data.get('items', []))
            all_logs.extend(rss_data.get('logs', []))

    # 读取网页结果
    if Path(web_path).exists():
        with open(web_path, 'r', encoding='utf-8') as f:
            web_data = json.load(f)
            all_items.extend(web_data.get('items', []))
            all_logs.extend(web_data.get('logs', []))

    return all_items, all_logs


def main():
    parser = argparse.ArgumentParser(description='生成每日简报')
    parser.add_argument('--config', default='assets/config.yaml', help='配置文件路径')
    parser.add_argument('--template', default='assets/template.md', help='模板文件路径')
    parser.add_argument('--extra-urls', help='额外的网页URL，用逗号分隔')
    parser.add_argument('--output', default='daily_report.md', help='输出文件路径')
    parser.add_argument('--data-dir', default='data', help='数据文件存储目录')
    parser.add_argument('--skip-fetch', action='store_true', help='跳过抓取，使用已有数据')
    args = parser.parse_args()

    # 确保数据目录存在
    data_dir = Path(args.data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)

    logs = []

    # 步骤1: 抓取内容
    if not args.skip_fetch:
        logger.info("开始抓取内容...")
        logs.append(f"[{datetime.now().strftime('%H:%M')}] 开始抓取内容...")

        # 抓取RSS
        rss_output = data_dir / 'rss_content.json'
        if run_fetch_rss(args.config, str(rss_output)):
            logger.info("RSS抓取完成")
        else:
            logger.warning("RSS抓取失败或无RSS源")

        # 抓取网页
        web_output = data_dir / 'web_content.json'
        if run_fetch_web(args.config, str(web_output), args.extra_urls):
            logger.info("网页抓取完成")
        else:
            logger.warning("网页抓取失败或无网页源")

        logs.append(f"[{datetime.now().strftime('%H:%M')}] 内容抓取完成")
    else:
        logger.info("跳过抓取，使用已有数据")

    # 步骤2: 合并结果
    rss_path = data_dir / 'rss_content.json'
    web_path = data_dir / 'web_content.json'

    all_items, fetch_logs = merge_results(str(rss_path), str(web_path))
    logs.extend(fetch_logs)

    if not all_items:
        logger.warning("没有获取到任何内容")
        logs.append(f"[{datetime.now().strftime('%H:%M')}] 警告: 没有获取到任何内容")
    else:
        logs.append(f"[{datetime.now().strftime('%H:%M')}] 共获取 {len(all_items)} 条内容")

    # 步骤3: 生成简报
    logger.info("生成简报...")
    date_str = datetime.now().strftime('%Y-%m-%d')
    markdown_content = generate_markdown_report(all_items, logs, date_str)

    # 步骤4: 保存简报
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    logs.append(f"[{datetime.now().strftime('%H:%M')}] 简报生成完成")

    logger.info(f"简报已保存到 {output_path}")
    logger.info(f"共包含 {len(all_items)} 条内容")


if __name__ == '__main__':
    main()
