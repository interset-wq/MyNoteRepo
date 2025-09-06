"""包
包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 A.B 表示名为 A 的包中名为 B 的子模块。
"""


"""假设要为统一处理声音文件与声音数据设计一个模块集（“包”）。
声音文件的格式很多（通常以扩展名来识别，例如：.wav，.aiff，.au），
因此，为了不同文件格式之间的转换，需要创建和维护一个不断增长的模块集合。
为了实现对声音数据的不同处理（例如，混声、添加回声、均衡器功能、创造人工立体声效果），还要编写无穷无尽的模块流。
下面这个分级文件树展示了这个包的架构：

sound/                          最高层级的包
      __init__.py               初始化 sound 包
      formats/                  用于文件格式转换的子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  用于音效的子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  用于过滤器的子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""

"""导入包时，Python 搜索 sys.path 里的目录，查找包的子目录。
需要有 __init__.py 文件才能让 Python 将包含该文件的目录当作包来处理
在最简单的情况下，__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码或设置 __all__ 变量
"""