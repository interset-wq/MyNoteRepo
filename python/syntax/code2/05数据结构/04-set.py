"""集合
集合是由不重复元素组成的无序容器。
基本用法包括成员检测、消除重复元素。
集合对象支持合集、交集、差集、对称差分等数学运算。

创建集合用花括号或 set() 函数。
注意，创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# 集合中的元素不重复
print(basket) # {'apple', 'pear', 'orange', 'banana'}

# 检查某元素是否在集合内
print('orange' in basket) # True

# 字符串转换为集合
a = set('abracadabra')
b = set('alacazam')
print(a) # {'c', 'd', 'a', 'b', 'r'}
print(b) # {'l', 'c', 'z', 'a', 'm'}

"""集合运算"""
# 差 a有b没有
print(a - b) # {'d', 'b', 'r'}

# 并集
print(a | b) # {'c', 'l', 'z', 'm', 'r', 'a', 'b', 'd'}

# 交集
print(a & b) # {'c', 'a'}

# 并集和交集的差
print(a ^ b) # {'b', 'l', 'm', 'z', 'r', 'd'}

"""集合推导式"""
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # {'r', 'd'}