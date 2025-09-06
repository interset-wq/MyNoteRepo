"""处理异常

BaseException 是所有异常的共同基类。
它的一个子类， Exception ，是所有非致命异常的基类。
不是 Exception 的子类的异常通常不被处理，
因为它们被用来指示程序应该终止。
它们包括由 sys.exit() 引发的 SystemExit ，
以及当用户希望中断程序时引发的 KeyboardInterrupt 。

Exception 可以被用作通配符，捕获（几乎）一切。
然而，好的做法是，尽可能具体地说明我们打算处理的异常类型，
并允许任何意外的异常传播下去。

处理 Exception 最常见的模式是打印或记录异常，
然后重新提出（允许调用者也处理异常）
"""

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
