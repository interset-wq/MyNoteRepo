"""del语句
通过索引删除元素
"""

a = [-1, 1, 66.25, 333, 333, 1234.5]

# 删除单个元素
del a[0]
print(a) # [1, 66.25, 333, 333, 1234.5]

# 删除某个切片
del a[2:4]
print(a) # [1, 66.25, 1234.5]

# 清空列表
del a[:]
print(a) # []

# 删除变量
del a
print(a) # NameError: name 'a' is not defined