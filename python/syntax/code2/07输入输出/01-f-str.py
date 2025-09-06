"""格式化字符串（f字符串）
格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，
通过 {expression} 表达式，把 Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。
"""


import math

# 四舍五入 保留三位小数
print(f'The value of pi is approximately {math.pi:.3f}.') # The value of pi is approximately 3.142.

# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    # 10d表示整数最小宽度10 整数默认往左侧添加空白补充长度
    print(f'{name:10} ==> {phone:10d}')
    # Sjoerd     ==>       4127
    # Jack       ==>       4098
    # Dcab       ==>       7678

# 还有一些修饰符可以在格式化前转换值。 
# '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()
animals = 'eels'
print(f'My hovercraft is full of {animals}.') # My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.') # My hovercraft is full of 'eels'.


# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}') # Debugging bugs='roaches' count=13 area='living room'
