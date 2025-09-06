"""队列
通过列表方法可以模拟队列
先进先出

但是列表作为队列的效率很低。
因为，在列表末尾添加和删除元素非常快，
但在列表开头插入或移除元素却很慢
（因为所有其他元素都必须移动一位）

实现队列最好用 collections.deque，
可以快速从两端添加或删除元素
"""

from collections import deque

queue = deque(["Eric", "John", "Michael"])

"""入队"""
queue.append("Terry")
queue.append("Graham")
print(queue) # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

"""出队"""
queue.popleft()             
print(queue) # deque(['John', 'Michael', 'Terry', 'Graham'])
queue.popleft()  
print(queue) # deque(['Michael', 'Terry', 'Graham'])
