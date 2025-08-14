import os
import uuid
import re
from urllib.request import urlretrieve
from markdown import markdown
from ebooklib import epub

def download_image(url, img_dir="images"):
    """下载图片并返回本地路径"""
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    # 提取文件名和扩展名
    filename = os.path.basename(url).split('?')[0]  # 去除URL参数
    if not filename:
        filename = f"img_{uuid.uuid4().hex[:8]}.jpg"  # 生成随机文件名
    
    local_path = os.path.join(img_dir, filename)
    
    try:
        urlretrieve(url, local_path)
        return local_path
    except Exception as e:
        print(f"下载图片失败 {url}: {e}")
        return None

def md_to_html(md_path):
    """将Markdown文件转换为HTML"""
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 先处理图片，下载到本地并替换路径
    img_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    def replace_img_tag(match):
        alt = match.group(1)
        url = match.group(2)
        local_path = download_image(url)
        if local_path:
            return f'![{alt}]({local_path})'
        return match.group(0)  # 保留原标签
    
    # 替换图片路径为本地路径
    processed_md = img_pattern.sub(replace_img_tag, md_content)
    
    # 转换为HTML
    html_content = markdown(processed_md, extensions=['extra'])
    return html_content

def html_to_epub(html_content, epub_path, title="未知标题", author="未知作者"):
    """将HTML内容转换为EPUB电子书"""
    # 创建EPUB书籍对象
    book = epub.EpubBook()
    book.set_identifier(str(uuid.uuid4()))
    book.set_title(title)
    book.set_language("zh")
    book.add_author(author)
    
    # 提取并添加图片
    img_pattern = re.compile(r'<img.*?src="(.*?)".*?>')
    img_paths = img_pattern.findall(html_content)
    for img_path in set(img_paths):  # 去重
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                img_content = f.read()
            
            # 获取图片MIME类型
            ext = os.path.splitext(img_path)[1].lower()[1:]  # 去除点
            mime_type = f"image/{ext}" if ext in ['jpg', 'jpeg', 'png', 'gif'] else "image/jpeg"
            
            # 添加图片到EPUB
            img_item = epub.EpubItem(
                uid=f"img_{os.path.basename(img_path)}",
                file_name=img_path,
                media_type=mime_type,
                content=img_content
            )
            book.add_item(img_item)
    
    # 分割HTML为章节（基于h1-h3标题）
    chapters = []
    chapter_id = 1
    
    # 使用正则分割章节
    parts = re.split(r'(<h[1-3].*?>.*?</h[1-3]>)', html_content)
    
    # 处理标题前的内容
    if parts and parts[0].strip():
        intro_html = f"<h2>前言</h2>\n{parts[0]}"
        intro_chapter = epub.EpubHtml(title="前言", file_name="intro.xhtml", lang="zh")
        intro_chapter.content = f"<html><head></head><body>{intro_html}</body></html>"
        book.add_item(intro_chapter)
        chapters.append(intro_chapter)
    
    # 处理每个章节
    for i in range(1, len(parts), 2):
        if i + 1 >= len(parts):
            break
            
        heading = parts[i]
        content = parts[i+1]
        
        # 提取章节标题文本
        title_match = re.search(r'<h[1-3].*?>(.*?)</h[1-3]>', heading)
        chapter_title = title_match.group(1) if title_match else f"章节 {chapter_id}"
        
        # 创建章节
        chapter_file = f"chap_{chapter_id}.xhtml"
        chapter = epub.EpubHtml(title=chapter_title, file_name=chapter_file, lang="zh")
        chapter.content = f"<html><head></head><body>{heading}{content}</body></html>"
        
        book.add_item(chapter)
        chapters.append(chapter)
        chapter_id += 1
    
    # 设置目录和导航
    book.toc = chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # 设置书脊
    book.spine = ['nav'] + chapters
    
    # 写入EPUB文件
    epub.write_epub(epub_path, book, {})
    print(f"EPUB文件已生成: {epub_path}")

def md_to_epub(md_path, epub_path):
    """将Markdown转换为EPUB的主函数"""
    # 从Markdown提取标题作为书名
    with open(md_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
    title = re.sub(r'^#+\s*', '', first_line) if first_line.startswith('#') else "未知标题"
    
    # 转换流程：MD -> HTML -> EPUB
    html_content = md_to_html(md_path)
    html_to_epub(html_content, epub_path, title=title)
    
    # 清理临时图片
    if os.path.exists("images"):
        for file in os.listdir("images"):
            os.remove(os.path.join("images", file))
        os.rmdir("images")

if __name__ == "__main__":
    # 输入输出路径
    md_file = "魔王小姐请再忍耐一下.md"    # 替换为你的Markdown文件路径
    epub_file = "output.epub"  # 输出的EPUB文件路径
    
    # 安装依赖：pip install markdown ebooklib
    md_to_epub(md_file, epub_file)
