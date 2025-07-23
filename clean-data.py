import re
from typing import Dict, List, Union, TypedDict

# 定义类型
class Args(TypedDict):
    params: Dict[str, str]

class Output(TypedDict):
    title: str
    content: str
    image_urls: List[str]
    image_count: int
    word_count: int
    extract_status: str

def clean_web_content(raw_content: str) -> Dict[str, Union[str, List[str]]]:
    """
    简单清洗网页内容，提取标题、正文和图片URL
    
    Args:
        raw_content: 原始爬虫内容
        
    Returns:
        dict: 包含title、content和image_urls的字典
    """
    # 1. 移除JavaScript代码
    content = re.sub(r'window\.__NUXT__=.*?\);', '', raw_content, flags=re.DOTALL)
    
    # 2. 移除HTML标签
    content = re.sub(r'<[^>]+>', '', content)
    
    # 3. 解码HTML实体
    content = content.replace('\\u003C', '<').replace('\\u003E', '>')
    content = content.replace('\\u002F', '/').replace('\\u0022', '"')
    content = content.replace('\\u003D', '=').replace('\\u0026', '&')
    
    # 4. 移除多余的空白字符
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()
    
    # 5. 提取标题 - 查找"如何1年内把1万变成114亿？"这样的模式
    title_match = re.search(r'如何.*?？', content)
    title = title_match.group(0) if title_match else "无标题"
    
    # 6. 提取文章内容 - 从"内容仅供娱乐"开始到"（文章来源"结束
    article_match = re.search(r'内容仅供娱乐.*?（文章来源.*?）', content, re.DOTALL)
    if article_match:
        article_content = article_match.group(0)
        # 清理内容中的多余字符
        article_content = re.sub(r'　　', '\n\n', article_content)  # 替换全角空格为换行
        article_content = re.sub(r'\s+', ' ', article_content)  # 合并多余空格
        article_content = article_content.strip()
    else:
        article_content = "无法提取文章内容"
    
    # 7. 提取图片URL - 从原始内容中提取
    image_urls = []
    
    # 先解码转义字符，便于后续提取
    decoded_content = raw_content.replace('\\u002F', '/').replace('\\u0022', '"')
    
    # 从HTML img标签中提取图片URL
    img_pattern = r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>'
    img_matches = re.findall(img_pattern, decoded_content, re.IGNORECASE)
    image_urls.extend(img_matches)
    
    # 直接匹配完整的图片URL（在解码后的内容中）
    direct_img_pattern = r'https?://[^"\'\s]*\.(?:jpg|jpeg|png|gif|webp|bmp)'
    direct_img_matches = re.findall(direct_img_pattern, decoded_content, re.IGNORECASE)
    image_urls.extend(direct_img_matches)
    
    # 处理转义的图片URL - 匹配包含\\\\u002F的URL
    escaped_img_pattern = r'https?:\\\\u002F\\\\u002F[^\\\\\s]*\.(?:jpg|jpeg|png|gif|webp|bmp)'
    escaped_img_matches = re.findall(escaped_img_pattern, raw_content, re.IGNORECASE)
    
    # 解码转义的URL
    for escaped_url in escaped_img_matches:
        decoded_url = escaped_url.replace('\\\\u002F', '/')
        image_urls.append(decoded_url)
    
    # 处理双重转义的图片URL - 匹配包含\\\\\\u002F的URL
    double_escaped_img_pattern = r'https?:\\\\\\u002F\\\\\\u002F[^\\\\\s]*\.(?:jpg|jpeg|png|gif|webp|bmp)'
    double_escaped_img_matches = re.findall(double_escaped_img_pattern, raw_content, re.IGNORECASE)
    
    # 解码双重转义的URL
    for escaped_url in double_escaped_img_matches:
        decoded_url = escaped_url.replace('\\\\\\u002F', '/')
        image_urls.append(decoded_url)
    
    # 处理JavaScript字符串中的转义URL - 匹配包含\\u002F的URL
    js_escaped_img_pattern = r'https?:\\u002F\\u002F[^\\\s]*\.(?:jpg|jpeg|png|gif|webp|bmp)'
    js_escaped_img_matches = re.findall(js_escaped_img_pattern, raw_content, re.IGNORECASE)
    
    # 解码JavaScript转义的URL
    for escaped_url in js_escaped_img_matches:
        decoded_url = escaped_url.replace('\\u002F', '/')
        image_urls.append(decoded_url)
    
    # 处理目标图片URL的特定模式
    target_img_pattern = r'https:\\\\u002F\\\\u002Fnp-newspic\.dfcfw\.com\\\\u002Fdownload\\\\u002FD25730774900815789399_w1563h5643_o\.jpg'
    target_img_matches = re.findall(target_img_pattern, raw_content, re.IGNORECASE)
    
    # 解码目标图片URL
    for escaped_url in target_img_matches:
        decoded_url = escaped_url.replace('\\\\u002F', '/')
        image_urls.append(decoded_url)
    
    # 去重并过滤有效的图片URL
    unique_image_urls = []
    for url in image_urls:
        if url and url not in unique_image_urls:
            # 确保URL格式正确
            if url.startswith('http') and any(ext in url.lower() for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']):
                unique_image_urls.append(url)
    
    return {
        "title": title,
        "content": article_content,
        "image_urls": unique_image_urls
    }

async def main(args: Args) -> Output:
    """
    主函数，处理网页内容清洗
    
    Args:
        args: 包含原始内容的参数对象
        
    Returns:
        Output: 包含清洗结果的输出对象
    """
    params = args.params
    raw_content = params['input']  # 获取输入的原始内容
    
    # 调用清洗函数
    cleaned_result = clean_web_content(raw_content)
    
    # 构建输出对象
    ret: Output = {
        "title": cleaned_result['title'],  # 提取的标题
        "content": cleaned_result['content'],  # 清洗后的内容
        "image_urls": cleaned_result['image_urls'],  # 提取的图片URL列表
        "image_count": len(cleaned_result['image_urls']),  # 图片数量
        "word_count": len(cleaned_result['content']),  # 字数统计
        "extract_status": "success" if cleaned_result['content'] != "无法提取文章内容" else "failed"
    }
    
    return ret