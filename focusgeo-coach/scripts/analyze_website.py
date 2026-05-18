#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网站分析脚本 - 自动从官网提取企业画像基础信息
"""

import argparse
import json
import re
import sys
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


def clean_text(text):
    """清理文本，去除多余空白"""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()


def extract_company_name(soup, url):
    """提取公司名称"""
    # 从页面标题提取
    title = soup.find('title')
    if title:
        title_text = clean_text(title.text)
        # 去除常见的后缀
        name = re.sub(r'\s*[-|]\s*.*$', '', title_text)
        if len(name) > 2 and len(name) < 100:
            return name

    # 从logo的alt文本提取
    logo = soup.find('img', {'class': re.compile(r'logo', re.I)})
    if logo and logo.get('alt'):
        return clean_text(logo['alt'])

    # 从footer提取
    footer = soup.find('footer')
    if footer:
        footer_text = clean_text(footer.text)
        # 尝试匹配公司名称模式
        match = re.search(r'([A-Za-z\u4e00-\u9fa5]{2,20}\s*(科技|网络|信息|软件|系统|智能|数据|咨询|服务)*)', footer_text)
        if match:
            return match.group(1)

    # 从URL提取域名作为后备
    domain = urlparse(url).netloc
    return domain.replace('www.', '').split('.')[0]


def extract_description(soup):
    """提取公司一句话描述"""
    # 从meta description提取
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc and meta_desc.get('content'):
        desc = clean_text(meta_desc['content'])
        if len(desc) > 10:
            return desc

    # 从hero区域提取
    hero = soup.find('section', {'class': re.compile(r'hero', re.I)})
    if not hero:
        hero = soup.find('div', {'class': re.compile(r'hero', re.I)})

    if hero:
        # 查找h1或p标签
        h1 = hero.find('h1')
        if h1:
            return clean_text(h1.text)

        p_tags = hero.find_all('p')
        if p_tags:
            return clean_text(p_tags[0].text)

    # 从第一个段落提取
    first_p = soup.find('p')
    if first_p and len(clean_text(first_p.text)) > 20:
        return clean_text(first_p.text)

    return ""


def extract_location(soup):
    """提取公司地区"""
    # 从footer地址提取
    footer = soup.find('footer')
    if footer:
        footer_text = clean_text(footer.text)
        # 匹配地址模式
        match = re.search(r'([^\s]{2,4}(省|市|区|县|自治区|特别行政区))', footer_text)
        if match:
            return match.group(0)

    # 从联系页面信息提取
    contact_section = soup.find('section', {'id': re.compile(r'contact', re.I)})
    if contact_section:
        text = clean_text(contact_section.text)
        match = re.search(r'([^\s]{2,4}(省|市|区|县))', text)
        if match:
            return match.group(0)

    return ""


def extract_founded_year(soup):
    """提取成立年份"""
    text = soup.get_text()

    # 匹配"成立于YYYY年"模式
    match = re.search(r'(?:成立|创建|创立)(?:于)?(\s)*(?:公元)?(\d{4})', text)
    if match:
        return match.group(2)

    # 匹配"YYYY年成立"模式
    match = re.search(r'(\d{4})\s*年\s*(?:成立|创建|创立)', text)
    if match:
        return match.group(1)

    return ""


def extract_products(soup):
    """提取产品/服务信息"""
    products = []

    # 从产品section提取
    product_sections = soup.find_all('section', {'class': re.compile(r'product|service', re.I)})
    if not product_sections:
        product_sections = soup.find_all('div', {'class': re.compile(r'product|service', re.I)})

    for section in product_sections[:3]:  # 最多取3个section
        h3 = section.find('h3')
        if h3:
            products.append(clean_text(h3.text))
        else:
            h2 = section.find('h2')
            if h2:
                products.append(clean_text(h2.text))

    # 从列表项提取
    if len(products) < 3:
        for li in soup.find_all('li'):
            text = clean_text(li.text)
            if 5 < len(text) < 100:
                products.append(text)
                if len(products) >= 5:
                    break

    return products[:5] if products else []


def extract_partners(soup):
    """提取合作伙伴/客户信息"""
    partners = []

    # 查找客户logo区域
    partner_section = soup.find('section', {'class': re.compile(r'partner|client|customer', re.I)})
    if partner_section:
        for img in partner_section.find_all('img'):
            alt = img.get('alt', '')
            if alt and len(alt) > 2:
                partners.append(clean_text(alt))

    return partners[:5] if partners else []


def analyze_website(url):
    """分析网站，提取企业画像信息"""
    try:
        # 添加协议
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        # 请求网页
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取信息
        result = {
            'status': 'success',
            'url': url,
            'company_name': extract_company_name(soup, url),
            'description': extract_description(soup),
            'location': extract_location(soup),
            'founded_year': extract_founded_year(soup),
            'products': extract_products(soup),
            'partners': extract_partners(soup),
            'note': '以上信息从官网自动提取，请根据实际情况修正和补充'
        }

        return result

    except requests.exceptions.RequestException as e:
        return {
            'status': 'error',
            'error': f'无法访问网站: {str(e)}',
            'note': '请检查网址是否正确，或手动提供企业信息'
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': f'分析失败: {str(e)}',
            'note': '请手动提供企业信息'
        }


def main():
    parser = argparse.ArgumentParser(description='分析官网，提取企业画像基础信息')
    parser.add_argument('--url', required=True, help='官网地址')

    args = parser.parse_args()

    # 分析网站
    result = analyze_website(args.url)

    # 输出JSON结果
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
