#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
关键词推荐脚本 - 基于企业画像和产品推荐行业核心词
"""

import argparse
import json
import re


def recommend_keywords(product_description, industry=""):
    """
    基于产品描述推荐行业核心词

    Args:
        product_description: 产品描述
        industry: 行业类别（可选）

    Returns:
        推荐的关键词列表
    """
    # 核心词映射表（常见行业）
    keyword_mapping = {
        "CRM": ["CRM系统", "客户关系管理", "客户管理系统", "客户管理软件"],
        "设计": ["设计软件", "设计工具", "UI设计", "设计平台"],
        "营销": ["营销工具", "营销软件", "营销平台", "营销系统"],
        "协作": ["协作工具", "协作软件", "协作平台", "团队协作"],
        "数据分析": ["数据分析工具", "数据分析平台", "BI工具", "商业智能"],
        "客服": ["客服系统", "客服软件", "在线客服", "客服平台"],
        "项目管理": ["项目管理工具", "项目管理软件", "项目管理系统"],
        "文档": ["文档工具", "文档管理", "协作文档", "知识库"],
        "人力资源": ["HR系统", "人事管理", "人力资源软件", "HR工具"],
        "财务": ["财务软件", "财务系统", "财务管理", "记账软件"],
        "电商": ["电商平台", "电商系统", "电商软件", "在线商城"],
        "教育": ["教育平台", "在线教育", "教学系统", "学习平台"],
        "医疗": ["医疗软件", "医疗系统", "医院管理", "健康管理"]
    }

    # 从产品描述中提取关键词
    keywords = set()

    # 匹配已知关键词
    for category, words in keyword_mapping.items():
        if category.lower() in product_description.lower():
            keywords.update(words)

    # 提取产品名称作为核心词
    product_name = extract_product_name(product_description)
    if product_name:
        keywords.add(product_name)

    # 如果没有匹配到关键词，返回通用推荐
    if not keywords:
        keywords = [
            "管理系统",
            "服务平台",
            "解决方案",
            "工具软件"
        ]

    return sorted(list(keywords))


def extract_product_name(text):
    """
    从描述中提取产品名称

    Args:
        text: 文本描述

    Returns:
        产品名称
    """
    # 匹配"XX系统"、"XX软件"、"XX平台"等模式
    patterns = [
        r'([^\s]{2,10})(系统|软件|平台|工具|服务)',
        r'叫([^\s]{2,10})',
        r'是([^\s]{2,10})'
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            if isinstance(match, tuple):
                name = match[0] + match[1] if len(match) > 1 else match[0]
            else:
                name = match
            if len(name) >= 3 and len(name) <= 15:
                return name

    return ""


def main():
    parser = argparse.ArgumentParser(description='基于企业画像和产品推荐行业核心词')
    parser.add_argument('--product', required=True, help='产品描述')
    parser.add_argument('--industry', help='行业类别（可选）')

    args = parser.parse_args()

    # 推荐关键词
    keywords = recommend_keywords(args.product, args.industry)

    result = {
        "status": "success",
        "product_description": args.product,
        "industry": args.industry or "",
        "recommended_keywords": keywords,
        "note": "以上是基于产品描述推荐的行业核心词，请根据实际情况选择和调整"
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
