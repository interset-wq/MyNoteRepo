"""异常
发生异常有Traceback
而语法错误SyntaxError没有
"""

"""ZeroDivisionError"""
# print(10 * (1/0))

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\02-error.py", line 4, in <module>
#     print(10 * (1/0))
#                 ~^~
# ZeroDivisionError: division by zero


"""NameError"""
# print(4 + spam*3)

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\02-error.py", line 14, in <module>
#     print(4 + spam*3)
#               ^^^^
# NameError: name 'spam' is not defined


"""TypeError"""
print('2' + 2)

# Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\02-error.py", line 23, in <module>
#     print('2' + 2)
#           ~~~~^~~
# TypeError: can only concatenate str (not "int") to str