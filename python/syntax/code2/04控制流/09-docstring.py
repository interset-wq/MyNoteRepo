"""文档字符串
第一行 直接写在三重引号之后，简要介绍函数的功能，这行应该是一个句子，大写字母开头，句点结束
第二行 空白行
第三行开始详细介绍函数的参数等内容
"""


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

# 打印文档字符串
print(my_function.__doc__)