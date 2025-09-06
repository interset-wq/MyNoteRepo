"""其他格式化字符串的方法

字符串对象的 str.rjust() 方法通过在左侧填充空格，
对给定宽度字段中的字符串进行右对齐。
同类方法还有 str.ljust() 和 str.center() 。
这些方法不写入任何内容，只返回一个新字符串，
如果输入的字符串太长，它们不会截断字符串，而是原样返回

另一种方法是 str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号
"""


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    print(repr(x*x*x).rjust(4))


print('12'.zfill(5)) # 00012
print('-3.14'.zfill(7)) # -003.14
print('3.14159265359'.zfill(5)) # 3.14159265359

