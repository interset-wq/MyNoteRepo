import re

# 查找所有f开头的单词
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')) # ['foot', 'fell', 'fastest']

# 删除重复的单词
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')) # cat in the hat

# 使用字符串方法替换
print('tea for too'.replace('too', 'two')) # tea for two