"""元组
元组是不可变对象immutable，列表是可变对象mutable
元组由多个用逗号隔开的值组成
输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组。
输入时，圆括号可有可无，不过经常是必须的
（如果元组是更大的表达式的一部分）。
不允许为元组中的单个元素赋值，
当然，可以创建含列表等可变对象的元组。
"""

# 空元组
empty = ()
print(empty) # ()

# 单元素元组 逗号必须有
single = 'hello',
print(single) # ('hello',)

t = 12345, 54321, 'hello!'
print(type(t)) # <class 'tuple'>
print(t[0]) # 12345

# 元组可以嵌套：
u = t, (1, 2, 3, 4, 5)
print(u) # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# 元组是不可变对象：
t[0] = 88888 # TypeError: 'tuple' object does not support item assignment