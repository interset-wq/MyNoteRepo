"""字典
字典是以 键 来索引的，键可以是任何不可变类型；
字符串和数字总是可以作为键。

可以把字典理解为 键值对 的集合，但字典的键必须是唯一的。
花括号 {} 用于创建空字典。
另一种初始化字典的方式是，在花括号里输入逗号分隔的键值对，这也是字典的输出方式。

通过del语句可以删除键值对
"""


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel) # {'jack': 4098, 'sape': 4139, 'guido': 4127}

# 删除键值对
del tel['sape']
print(tel) # {'jack': 4098, 'guido': 4127}

tel['irv'] = 4127
print(tel) # {'jack': 4098, 'guido': 4127, 'irv': 4127}

# 获取键列表
print(list(tel)) # ['jack', 'guido', 'irv']

# 对字典排序实际上是对键列表排序
print(sorted(tel)) # ['guido', 'irv', 'jack']

# 判断键是否在字典中
print('guido' in tel) # True
print('jack' not in tel) # False

# 空字典
empty = {}
print(empty) # {}

"""# 通过dict()初始化字典"""
# 通过序列创建字典
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1) # {'sape': 4139, 'guido': 4127, 'jack': 4098}
# 通过关键字参数创建字典
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict2) # {'sape': 4139, 'guido': 4127, 'jack': 4098}


"""字典推导式"""
dict3 = {x: x**2 for x in (2, 4, 6)}
print(dict3) # {2: 4, 4: 16, 6: 36}