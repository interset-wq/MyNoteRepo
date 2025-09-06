"""操作列表"""

list1 = [0] * 5
print(list1) # [0, 0, 0, 0, 0]

"""更改元素"""
list1[2] = 5
print(list1) # [0, 0, 5, 0, 0]

"""查询正向索引"""
print(list1.index(5)) # 2

"""通过索引插入元素"""
list1.insert(1, 7)
print(list1) # [0, 7, 0, 5, 0, 0]

"""追加元素"""
list1.append(6)
print(list1) # [0, 7, 0, 5, 0, 0, 6]

"""批量追加元素"""
list2 = ['a', 'b', 3, 7]
list1.extend(list2)
print(list1) # [0, 7, 0, 5, 0, 0, 6, 'a', 'b', 3, 7]

"""通过元素值删除元素"""
# 删除第一个匹配
list1.remove(0)
print(list1) # [7, 0, 5, 0, 0, 6, 'a', 'b', 3, 7]
# 删除全部匹配
while 0 in list1:
    list1.remove(0)
print(list1) # [7, 5, 6, 'a', 'b', 3, 7]

"""通过索引删除元素 默认删除最后一个元素"""
# pop
popped_elem = list1.pop()
print(popped_elem) # 7
print(list1) # [7, 5, 6, 'a', 'b', 3]

popped_elem2 = list1.pop(-3)
print(popped_elem2) # a
print(list1) # [7, 5, 6, 'b', 3]

# del
del list1[3]
print(list1) # [7, 5, 6, 3]

"""数学"""
# 求和
print(sum(list1)) # 21
# 求最小值
print(min(list1)) # 3
# 求最大值
print(max(list1)) # 7
# 长度
print(len(list1)) # 4
# 统计某元素出现次数
list1.append(5)
print(list1) # [7, 5, 6, 3, 5]
print(list1.count(5)) # 2
# 排序 从小到大正序 传入参数reverse=True时倒序排列
print(sorted(list1)) # [3, 5, 5, 6, 7]
print(sorted(list1, reverse=True)) # [7, 6, 5, 5, 3]
print(list1) # [7, 5, 6, 3, 5]
list1.sort()
print(list1) # [3, 5, 5, 6, 7]
list1.sort(reverse=True)
print(list1) # [7, 6, 5, 5, 3]

"""反转列表"""
print(list1) # [7, 5, 6, 3, 5]
# reverse
list1.reverse() 
print(list1) # [5, 3, 6, 5, 7]
# 切片
print(list1[::-1]) # [7, 5, 6, 3, 5]

"""清空列表"""
list1.clear()
print(list1) # []

"""列表加法运算"""
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]