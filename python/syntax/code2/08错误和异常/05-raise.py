"""异常链

如果一个未处理的异常发生在 except 部分内，
它将会有被处理的异常附加到它上面，并包括在错误信息中:
"""


"""按照代码的执行顺序抛出异常"""
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 8, in <module>
#     open("database.sqlite")
#     ~~~~^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 10, in <module>
#     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error


"""
为了表明一个异常是另一个异常的直接后果， 
raise 语句允许一个可选的 from 子句:

# exc 必须为异常实例或为 None。
raise RuntimeError from exc

这种方法常用于转换异常
"""

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 42, in <module>
#     func()
#     ~~~~^^
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 39, in func
#     raise ConnectionError
# ConnectionError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 44, in <module>
#     raise RuntimeError('Failed to open database') from exc
# RuntimeError: Failed to open database

"""from None禁用自动异常链"""
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\05-raise.py", line 65, in <module>
#     raise RuntimeError from None
# RuntimeError


"""自定义异常

程序可以通过创建新的异常类命名自己的异常
不论是以直接还是间接的方式，异常都应从 Exception 类派生。

异常类可以被定义成能做其他类所能做的任何事，
但通常应当保持简单，它往往只提供一些属性，
允许相应的异常处理程序提取有关错误的信息。

大多数异常命名都以 “Error” 结尾，类似标准异常的命名。

许多标准模块定义了自己的异常，以报告他们定义的函数中可能出现的错误。
"""