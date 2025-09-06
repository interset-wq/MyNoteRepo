"""try-except-else

try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。 
它适用于 try 子句 没有引发异常但又必须要执行的代码。
使用 else 子句比向 try 子句添加额外的代码要好，
可以避免意外捕获非 try ... except 语句保护的代码触发的异常。
"""

import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()