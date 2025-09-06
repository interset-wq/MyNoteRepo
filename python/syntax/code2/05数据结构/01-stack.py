"""可以使用列表方法
append()和pop()模拟入栈和出栈"""


"""栈的特点是只能从一段增减数据，
即先进后出 后进先出
"""

stack = [3, 4, 5]
"""入栈"""
stack.append(6)
stack.append(7)
print(stack) # [3, 4, 5, 6, 7]

"""出栈"""
stack.pop()
print(stack) # [3, 4, 5, 6]

stack.pop()
print(stack) # [3, 4, 5]

stack.pop() 
print(stack) # [3, 4]