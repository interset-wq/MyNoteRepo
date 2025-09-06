"""处理异常

except 子句 可能会在异常名称后面指定一个变量。 这个变量将被绑定到异常实例，
该实例通常会有一个存储参数的 args 属性。
为了方便起见，内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args。
"""


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # 异常的类型
    print(inst.args)     # 参数保存在 .args 中
    print(inst)          # __str__ 允许 args 被直接打印，
                         # 但可能在异常子类中被覆盖
    x, y = inst.args     # 解包 args
    print('x =', x)
    print('y =', y)

# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs