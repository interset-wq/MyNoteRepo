"""if-elif-else语句
如果是把一个值与多个常量进行比较，
或者检查特定类型或属性，match 语句更有用。
"""


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')