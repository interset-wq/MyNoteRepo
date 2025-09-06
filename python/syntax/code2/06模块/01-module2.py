"""模块搜索路径

当导入一个名为 spam 的模块时，
解释器首先会搜索具有该名称的内置模块。 
这些模块的名称在 sys.builtin_module_names 中列出。 
如果未找到，它将在变量 sys.path 所给出的目录列表中搜索名为 spam.py 的文件。
sys.path 是从这些位置初始化的:

被命令行直接运行的脚本所在的目录（或未指定文件时的当前目录）。
PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。
依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）。


初始化后，Python 程序可以更改 sys.path。
脚本所在的目录先于标准库所在的路径被搜索。
这意味着，脚本所在的目录如果有和标准库同名的文件，那么加载的是该目录里的，而不是标准库的。
这一般是一个错误，除非这样的替换是你有意为之
"""

""" “已编译的” Python 文件
为了快速加载模块，Python 把模块的编译版本缓存在 __pycache__ 目录中，
文件名为 module.version.pyc，version 对编译文件格式进行编码，
一般是 Python 的版本号。
例如，CPython 的 3.3 发行版中，
spam.py 的编译版本缓存为 __pycache__/spam.cpython-33.pyc。
这种命名惯例让不同 Python 版本编译的模块可以共存。
"""


"""sys
模块 sys，它被内嵌到每一个 Python 解释器中。
sys.ps1 和 sys.ps2 变量定义了一些字符，
它们可以用作主提示符和辅助提示符
对它们重新赋值可以修改python解释器的命令提示符

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '

变量 sys.path 是字符串列表，用于确定解释器的模块搜索路径。
该变量以环境变量 PYTHONPATH 提取的默认路径进行初始化，
如未设置 PYTHONPATH，则使用内置的默认路径。
"""