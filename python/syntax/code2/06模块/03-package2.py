"""从包中导入 *
由于包中有很多模块，模块中又有很多函数，因此不能使用这种写法

唯一的解决办法是提供包的显式索引。import 语句使用如下惯例：
如果包的 __init__.py 代码定义了列表 __all__，
运行 from package import * 时，它就是被导入的模块名列表。
发布包的新版本时，包的作者应更新此列表。
如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表。
例如，sound/effects/__init__.py 文件可以包含以下代码：

__all__ = ["echo", "surround", "reverse"]

这意味着 from sound.effects import * 将导入 sound.effects 包的三个命名子模块
"""