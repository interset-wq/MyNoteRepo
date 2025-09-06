"""dir() 函数
内置函数 dir() 用于查找模块定义的名称。返回结果是经过排序的字符串列表

它列出所有类型的名称：变量，模块，函数，文档字符串等。
dir() 不会列出内置函数和变量的名称，例如python内置函数print，sum等不会被列出。
"""

import fibo

print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fibo']

