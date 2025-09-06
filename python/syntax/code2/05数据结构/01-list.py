"""列表方法
iterable类型的数据结构和列表有类似的方法
"""


# 初始化
list1 = [0] * 5
print(list1) # [0, 0, 0, 0, 0]

"""append(x)
列表末尾追加元素
"""
list1.append(2)
print(list1) # [0, 0, 0, 0, 0, 2]

"""extend(iterable)
通过其他可迭代类型iterable扩展列表
"""
tuple1 = (7, 8)
list1.extend(tuple1)
print(list1) # [0, 0, 0, 0, 0, 2, 7, 8]

"""insert(i, x)
通过下标插入元素
"""
list1.insert(1, 5)
print(list1) # [0, 5, 0, 0, 0, 0, 2, 7, 8]

"""remove(x)
删除第一个找到的元素
"""
list1.remove(0)
print(list1) # [5, 0, 0, 0, 0, 2, 7, 8]

"""pop([i])
通过索引删除元素，返回删除的元素 默认删除最后一个元素
"""
a = list1.pop()
print(list1, a) # [5, 0, 0, 0, 0, 2, 7] 8

"""index(x[, start[, end]])
返回第一个值为x的元素的索引
可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。
返回的索引是相对于整个序列的开始计算的，而不是 start 参数。
"""
# 从索引0开始查找
print(list1.index(0)) # 1
# 从索引3开始查找
print(list1.index(0, 3)) # 3

"""count(x)
返回列表中元素 x 出现的次数
"""
print(list1.count(0)) # 4

"""sort(*, key=None, reverse=False)
就地排序列表中的元素，只能使用关键字参数
False从小到大 True从大到小
sorted()函数和它的功能类似
"""
print(list1) # [5, 0, 0, 0, 0, 2, 7]
list1.sort()
print(list1) # [0, 0, 0, 0, 2, 5, 7]

"""reverse()
翻转列表中的元素
"""
list1.reverse()
print(list1) # [7, 5, 2, 0, 0, 0, 0]

"""copy()
返回列表的浅拷贝。 相当于 list1[:]
"""
print(list1.copy()) # [7, 5, 2, 0, 0, 0, 0]

"""clear()
清空列表 相当于 del list1[:]
"""
list1.clear()
print(list1) # []