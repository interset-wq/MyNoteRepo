"""finally
用于定义在所有情况下都必须要执行的清理操作
"""

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# Goodbye, world!
# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\06-finally.py", line 6, in <module>
#     raise KeyboardInterrupt
# KeyboardInterrupt