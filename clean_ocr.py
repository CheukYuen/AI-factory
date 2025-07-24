#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR文本清洗工具
将OCR识别的JSON格式文本清洗成大模型容易理解的格式
"""

import json
import re
from typing import List, Dict, Any


def clean_stock_data(text: str) -> str:
    """
    清洗股票数据文本，提取股票名称、涨跌幅和资产信息
    
    Args:
        text: 原始文本，如 "金盾股份 200%25"
    
    Returns:
        清洗后的文本，如 "金盾股份: 涨幅200%, 月末资产25万元"
    """
    # 匹配股票名称 + 涨跌幅 + 资产
    pattern = r'([A-Za-z\u4e00-\u9fff\*]+)\s*([+-]?\d+\.?\d*%)\s*(\d+\.?\d*)'
    match = re.search(pattern, text)
    
    if match:
        stock_name = match.group(1).strip()
        change_rate = match.group(2)
        asset = match.group(3)
        
        # 判断是涨幅还是跌幅
        if change_rate.startswith('-'):
            change_type = "跌幅"
            change_rate = change_rate[1:]  # 去掉负号
        else:
            change_type = "涨幅"
        
        # 根据涨跌幅类型决定单位：涨幅王用万元，跌幅王用元
        asset_value = float(asset)
        if change_type == "涨幅":
            # 涨幅王：原始数据已经是万元单位，直接使用
            return f"{stock_name}: {change_type}{change_rate}, 月末资产{asset_value:.0f}万元"
        else:
            # 跌幅王：保持元为单位
            return f"{stock_name}: {change_type}{change_rate}, 月末资产{asset_value}元"
    
    # 如果没有匹配到，尝试其他模式
    # 处理类似 "深中华A169%2.7" 这样的格式
    pattern2 = r'([A-Za-z\u4e00-\u9fff\*]+)\s*(\d+\.?\d*)%\s*(\d+\.?\d*)'
    match2 = re.search(pattern2, text)
    
    if match2:
        stock_name = match2.group(1).strip()
        change_rate = match2.group(2)
        asset = match2.group(3)
        
        change_type = "涨幅"
        
        # 第二个模式匹配的都是涨幅王，原始数据已经是万元单位
        asset_value = float(asset)
        return f"{stock_name}: {change_type}{change_rate}%, 月末资产{asset_value}万元"
    
    return text


def clean_text_segment(text: str) -> str:
    """
    清洗单个文本片段
    
    Args:
        text: 原始文本
    
    Returns:
        清洗后的文本
    """
    # 去除多余的空格
    text = re.sub(r'\s+', ' ', text.strip())
    
    # 处理股票数据
    if re.search(r'[A-Za-z\u4e00-\u9fff\*]+\s*[+-]?\d+\.?\d*%\s*\d+', text):
        return clean_stock_data(text)
    
    # 处理百分比数据
    text = re.sub(r'(\d+)%(\d+)', r'\1% \2', text)
    
    # 处理特殊字符
    text = text.replace('"', '"').replace('"', '"')
    
    return text


def extract_and_clean_ocr_data(json_data: Dict[str, Any]) -> str:
    """
    从OCR JSON数据中提取并清洗文本
    
    Args:
        json_data: OCR识别的JSON数据
    
    Returns:
        清洗后的文本内容
    """
    try:
        # 提取所有文本片段
        words = json_data.get('data', {}).get('results', [{}])[0].get('words', [])
        text_segments = [word.get('text', '') for word in words]
        
        # 先分类股票数据，再清洗
        gainers_raw = []
        losers_raw = []
        other_segments = []
        
        for segment in text_segments:
            if segment.strip():
                if "%" in segment and re.search(r'[A-Za-z\u4e00-\u9fff\*]+\s*[+-]?\d+\.?\d*%', segment):
                    # 根据涨跌幅判断是涨幅王还是跌幅王
                    if re.search(r'-\d+\.?\d*%', segment):  # 包含负号的为跌幅王
                        losers_raw.append(segment)
                    else:  # 不包含负号的为涨幅王
                        gainers_raw.append(segment)
                else:
                    other_segments.append(segment)
        
        # 清洗股票数据
        gainers_cleaned = [clean_stock_data(segment) for segment in gainers_raw]
        losers_cleaned = [clean_stock_data(segment) for segment in losers_raw]
        
        # 清洗其他文本片段
        cleaned_other = []
        for segment in other_segments:
            cleaned = clean_text_segment(segment)
            if cleaned:
                cleaned_other.append(cleaned)
        
        # 组织成结构化的内容
        return organize_content_improved(cleaned_other, gainers_cleaned, losers_cleaned)
        
    except (KeyError, IndexError) as e:
        print(f"❌ **严重错误** (Critical Error): JSON数据结构解析失败 - {e}")
        return ""


def organize_content_improved(other_segments: List[str], gainers: List[str], losers: List[str]) -> str:
    """
    将清洗后的文本片段组织成结构化的内容（改进版）
    
    Args:
        other_segments: 其他文本片段列表
        gainers: 涨幅王股票列表
        losers: 跌幅王股票列表
    
    Returns:
        结构化的文本内容
    """
    content_parts = []
    
    # 提取标题和主题
    title = ""
    theme = ""
    
    for segment in other_segments:
        if "东方财富" in segment and "权威" in segment:
            title = segment
        elif "2024年A股年度盘点" in segment:
            theme = segment
        elif "年初1万元入市" in segment:
            content_parts.append(f"## 投资假设\n{segment}")
        elif "如何赚到" in segment:
            content_parts.append(f"## 投资目标\n{segment}")
        elif "连续买入月度涨幅王" in segment:
            content_parts.append(f"## 涨幅王投资策略\n{segment}")
        elif "连续买入月度跌幅王" in segment:
            content_parts.append(f"## 跌幅王投资策略\n{segment}")
    
    # 添加涨幅王数据
    if gainers:
        content_parts.append("### 月度涨幅王股票表现:")
        for gainer in gainers:
            content_parts.append(f"- {gainer}")
        content_parts.append("")  # 添加空行分隔
    
    # 添加跌幅王数据
    if losers:
        content_parts.append("### 月度跌幅王股票表现:")
        for loser in losers:
            content_parts.append(f"- {loser}")
        content_parts.append("")  # 添加空行分隔
    
    # 添加数据来源
    for segment in other_segments:
        if "数据来源" in segment or "截至" in segment:
            content_parts.append(f"## 数据说明\n{segment}")
    
    # 组合最终内容
    final_content = f"""# {title}

## 主题
{theme}

{chr(10).join(content_parts)}

## 总结
本报告展示了2024年A股市场的极端投资情况：
1. 如果每月都买入当月涨幅最大的股票，1万元本金最终可达到114亿元
2. 如果每月都买入当月跌幅最大的股票，1万元本金最终仅剩3.61元
3. 这充分说明了股票投资的风险与收益并存，以及选股的重要性
"""
    
    return final_content


def organize_content(segments: List[str]) -> str:
    """
    将清洗后的文本片段组织成结构化的内容
    
    Args:
        segments: 清洗后的文本片段列表
    
    Returns:
        结构化的文本内容
    """
    content_parts = []
    
    # 提取标题和主题
    title = ""
    theme = ""
    
    for segment in segments:
        if "东方财富" in segment and "权威" in segment:
            title = segment
        elif "2024年A股年度盘点" in segment:
            theme = segment
        elif "年初1万元入市" in segment:
            content_parts.append(f"## 投资假设\n{segment}")
        elif "如何赚到" in segment:
            content_parts.append(f"## 投资目标\n{segment}")
    
    # 提取涨幅王数据
    gainers = []
    losers = []
    in_gainers_section = False
    in_losers_section = False
    
    for segment in segments:
        if "连续买入月度涨幅王" in segment:
            in_gainers_section = True
            in_losers_section = False
            content_parts.append(f"## 涨幅王投资策略\n{segment}")
        elif "连续买入月度跌幅王" in segment:
            in_gainers_section = False
            in_losers_section = True
            content_parts.append(f"## 跌幅王投资策略\n{segment}")
        elif in_gainers_section and "%" in segment and any(char.isdigit() for char in segment):
            gainers.append(segment)
        elif in_losers_section and "%" in segment and any(char.isdigit() for char in segment):
            losers.append(segment)
    
    # 添加涨幅王数据
    if gainers:
        content_parts.append("### 月度涨幅王股票表现:")
        for gainer in gainers:
            content_parts.append(f"- {gainer}")
    
    # 添加跌幅王数据
    if losers:
        content_parts.append("### 月度跌幅王股票表现:")
        for loser in losers:
            content_parts.append(f"- {loser}")
    
    # 添加数据来源
    for segment in segments:
        if "数据来源" in segment or "截至" in segment:
            content_parts.append(f"## 数据说明\n{segment}")
    
    # 组合最终内容
    final_content = f"""# {title}

## 主题
{theme}

{chr(10).join(content_parts)}

## 总结
本报告展示了2024年A股市场的极端投资情况：
1. 如果每月都买入当月涨幅最大的股票，1万元本金最终可达到114亿元
2. 如果每月都买入当月跌幅最大的股票，1万元本金最终仅剩3.61元
3. 这充分说明了股票投资的风险与收益并存，以及选股的重要性
"""
    
    return final_content


def main():
    """
    主函数：读取JSON数据并生成清洗后的内容
    """
    # 示例JSON数据（实际使用时可以从文件读取）
    sample_data = {
        "log_id": "202507231641305B1578C3694087D00400",
        "msg": "success",
        "code": 0,
        "data": {
            "results": [
                {
                    "words": [
                        {"text": "东方财富", "lang": "auto"},
                        {"text": "权威·专业·及时·互动", "lang": "auto"},
                        {"text": "2024年A股年度盘点(6)", "lang": "auto"},
                        {"text": "年初1万元入市", "lang": "auto"},
                        {"text": "如何赚到114亿?", "lang": "auto"},
                        {"text": "假设2024初我们拿着1万元入市,每个月都买到最牛/最熊", "lang": "auto"},
                        {"text": "的那只股票,现在手里能有多少钱?", "lang": "auto"},
                        {"text": "连续买入月度\"涨幅王\"1万变114亿", "lang": "auto"},
                        {"text": "深中华A169%2.7", "lang": "auto"},
                        {"text": "克来机电207%8.3", "lang": "auto"},
                        {"text": "金盾股份 200%25", "lang": "auto"},
                        {"text": "正丹股份 362%114", "lang": "auto"},
                        {"text": "英力股份 178% 318", "lang": "auto"},
                        {"text": "逸豪新材 90% 605", "lang": "auto"},
                        {"text": "大众交通 256%2155", "lang": "auto"},
                        {"text": "深圳华强 186% 6157", "lang": "auto"},
                        {"text": "银之杰 285% 23709", "lang": "auto"},
                        {"text": "光智科技 339% 103976", "lang": "auto"},
                        {"text": "日出东方 394% 513513", "lang": "auto"},
                        {"text": "友阿股份 122%1142001", "lang": "auto"},
                        {"text": "连续买入月度\"跌幅王\"1万变3.61元", "lang": "auto"},
                        {"text": "ST天喻-49.91% 5009.21", "lang": "auto"},
                        {"text": "百通能源-30.25% 3494.03", "lang": "auto"},
                        {"text": "华扬联众-26.88% 2554.77", "lang": "auto"},
                        {"text": "*ST 名家 -66.34% 859.92", "lang": "auto"},
                        {"text": "*ST 银江-67.56% 278.93", "lang": "auto"},
                        {"text": "东方集团-56.29% 121.92", "lang": "auto"},
                        {"text": "ST 旭蓝-53.94% 56.15", "lang": "auto"},
                        {"text": "康隆达-36.77% 35.50", "lang": "auto"},
                        {"text": "ST凯文 -25.96% 26.28", "lang": "auto"},
                        {"text": "诺泰生物-29.42%18.55", "lang": "auto"},
                        {"text": "*ST卓朗-65.93%6.32", "lang": "auto"},
                        {"text": "瑞松科技-42.85% 3.61", "lang": "auto"},
                        {"text": "数据来源:东方财富Choice数据", "lang": "auto"},
                        {"text": "(截至12月23日收盘,剔除2024年新股及退市股)", "lang": "auto"}
                    ]
                }
            ]
        }
    }
    
    # 清洗数据并生成结构化内容
    cleaned_content = extract_and_clean_ocr_data(sample_data)
    
    print("🔧 **清洗后的内容** (Cleaned Content):")
    print("=" * 50)
    print(cleaned_content)
    print("=" * 50)
    
    # 保存到文件
    with open('cleaned_ocr_output.txt', 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print("✅ 清洗完成！结果已保存到 cleaned_ocr_output.txt")


if __name__ == "__main__":
    main()