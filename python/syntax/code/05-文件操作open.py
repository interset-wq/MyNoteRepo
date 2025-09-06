"""文件操作open函数
如果使用with open as就不需要手动关闭文件，操作结束会自动关闭文件
"""

path = r'C:\Users\d111k\Desktop\MyNoteRepo\python\syntax\code\zen.txt'

"""打开文件"""
f = open(path)

"""读写文件
如果文件内容读取完毕之后，再读取会返回空字符串
"""

"""# 读取全文"""
# print(f.read())
    # Beautiful is better than ugly.
    # Explicit is better than implicit.
    # Simple is better than complex.
"""# 每次读取一行 除最后一行外得到的字符串一定以'\n'结尾"""
# print(f.readline()) # Beautiful is better than ugly.
"""# 按行读取 除最后一行外，每行一定以'\n'结尾，
如果是最后一行，是否以'\n'结尾，
取决于读取的文件最后一行是否结束时使用了回车'"""
# 方法一
# for line in f.readlines():
#     print(line)
# 方法二 两种方法没有区别
# for line in f:
#     print(line)
"""关闭文件"""
f.close()