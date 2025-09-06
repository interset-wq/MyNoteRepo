"""字符串常用方法"""

str1 = 'heLLo WorLD'

"""大小写"""
# 单词首字母大写
print(str1.title()) # Hello World
# 全小写
print(str1.lower()) # hello world
# 全大写
print(str1.upper()) # HELLO WORLD

"""拆分为列表"""
# 拆分为列表 分割符号默认为空格
print(str1.split()) # ['heLLo', 'WorLD']
str2 = 'hello,world'
print(str2.split(',')) # ['hello', 'world']

"""删除和替换"""
str3 = '   hello   '
str4 = 'https://docs.python.org/zh-cn/3/'
# 删除左右空白
print(str3.strip()) # hello
# 删除右侧空白或字符
print(f'删除右侧空白{str3.rstrip()}') # 删除右侧空白   hello
print(str4.rstrip('/')) # https://docs.python.org/zh-cn/3
# 删除左侧空白或字符 如果传入的是字符串，则会删除最左侧字符串中出现的所有字符
print(f'{str3.lstrip()}删除左侧空白') # hello   删除左侧空白
print(str4.lstrip('th')) # ps://docs.python.org/zh-cn/3/
# 删除前缀
print(str4.removeprefix('https://')) # docs.python.org/zh-cn/3/
# 替换字符
print(str1) # heLLo WorLD
print(str1.replace('o', 'A')) # heLLA WArLD

"""列表方法
字符串可以看作是字符列表，也可以使用列表方法
"""

# - `index(元素)` 方法
# - `count()` 方法
# - `len()` 函数 字符串中的符号和空白也被看做是字符