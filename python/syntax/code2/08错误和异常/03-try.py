"""处理异常

try 语句的工作原理如下：

首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。

如果没有触发异常，则跳过 except 子句，try 语句执行完毕。

如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 
如果异常的类型与 except 关键字后指定的异常相匹配，
则会执行 except 子句，然后跳到 try/except 代码块之后继续执行。

如果发生的异常与 except 子句 中指定的异常不匹配，
则它会被传递到外层的 try 语句中；如果没有找到处理器，
则它是一个 未处理异常 且执行将停止并输出一条错误消息。

try 语句可以有多个 except 子句 来为不同的异常指定处理程序。 
但最多只有一个处理程序会被执行。 
处理程序只处理对应的 try 子句 中发生的异常，
而不处理同一 try 语句内其他处理程序中的异常。 
except 子句 可以用带圆括号的元组来指定多个异常，例如:

except (RuntimeError, TypeError, NameError):
   pass
"""


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

"""ctrl+c中断程序会触发 KeyboardInterrupt 异常。"""
# Please enter a number: Traceback (most recent call last):
#   File "c:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code2\08错误和异常\03-try.py", line 7, in <module>
#     x = int(input("Please enter a number: "))
#             ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
# KeyboardInterrupt