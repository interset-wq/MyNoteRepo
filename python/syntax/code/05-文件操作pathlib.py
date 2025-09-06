"""通过pathlib操作文件"""


from pathlib import Path


file_path = r'C:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code\zen.txt'

"""创建Path对象"""
path = Path(file_path)

"""对Path进行操作"""
# 检查路径是否存在
print(path.exists()) # True
# 读取全文
text = path.read_text(encoding='utf-8')
# print(text)
    # Beautiful is better than ugly.
    # Explicit is better than implicit.
    # Simple is better than complex.
# 按行读取 通过splitlines获取的每行内容不会强制以'\n'结尾
for line in text.splitlines():
    print(line)