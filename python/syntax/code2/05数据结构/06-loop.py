"""循环的技巧"""



"""
当对字典执行循环时，
可以使用 items() 方法同时提取键及其对应的值
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

"""在序列中循环时，
用 enumerate() 函数可以同时取出位置索引和对应的值
"""
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

"""同时循环两个或多个序列时，
用 zip() 函数可以将其内的元素一一匹配
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

"""为了逆向对序列进行循环，
可以求出欲循环的正向序列，然后调用 reversed() 函数
"""
for i in reversed(range(1, 10, 2)):
    print(i)

"""按指定顺序循环序列，
可以用 sorted() 函数，
在不改动原序列的基础上，返回一个重新的序列
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

"""使用 set() 去除序列中的重复元素。
使用 sorted() 加 set() 则按排序后的顺序，
循环遍历序列中的唯一元素
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

"""
一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全
"""
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
