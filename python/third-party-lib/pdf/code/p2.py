import pdfplumber, string, re

NUMS = string.digits
PARAENDS = ('.', '?', '!', '"', ')', '。', '？', '！', '”', '）')

path = '../example.pdf'

def remove_mul_newlines(text:str) -> str:
    """删除多余空行"""
    return re.sub(r'\n+', '\n', text)

def merge_para(lines: list) -> str:
    """将文章片段合成为通顺的段落"""
    lines = [line.strip() for line in lines]
    text = ''
    for line in lines:
        if not line[-1] in PARAENDS:
            if line[0] in NUMS:
                text += '\n' + line
            else:
                text += line
        else:
            if line[0] in NUMS:
                text += '\n' + line + '\n'
            else:
                text += line + '\n'
    new_text = remove_mul_newlines(text)
    return new_text

# 打开文件创建
with pdfplumber.open(path) as pdf:
    pages = pdf.pages
    line_texts = []
    for page in pages:
        width = page.width
        height = page.height
        cropped_page = page.crop((85, 70, width - 70, height - 65))
        lines = cropped_page.extract_text_lines(strip=False)
        for line in lines:
            line_texts.append(line['text'])
    text = merge_para(line_texts)
    # print(text)
    with open('example.txt', 'w', encoding='utf-8') as f:
        f.write(text)

