"""抛出异常raise

raise 语句支持强制触发指定的异常。
"""


"""抛出异常NameError"""
# raise NameError('HiThere')

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\04-raise.py", line 6, in <module>
#     raise NameError('HiThere')
# NameError: HiThere


"""
raise 唯一的参数就是要触发的异常。
这个参数必须是异常实例或异常类（派生自 BaseException 类，
例如 Exception 或其子类）。如果传递的是异常类，
将通过调用没有参数的构造函数来隐式实例化：
"""
# raise ValueError  # 'raise ValueError()' 的简化

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\04-raise.py", line 22, in <module>
#     raise ValueError  # 'raise ValueError()' 的简化
#     ^^^^^^^^^^^^^^^^
# ValueError

"""
如果只想判断是否触发了异常，但并不打算处理该异常，
则可以使用更简单的 raise 语句重新触发异常：
"""
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise # 重新抛出捕获的异常

# An exception flew by!
# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\04-raise.py", line 35, in <module>
#     raise NameError('HiThere')
# NameError: HiThere