# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


data = input()  # 课程名 考分
d = {}
while data:
    ls = data.split()
    d[ls[0]] = int(ls[1])
    data = input()
lt = list(d.items())
lt.sort(key=lambda x: int(x[-1]),reverse=True)
aver = sum(d.values()) / len(d)
print("最高分课程是{} {}, 最低分课程是{} {}, 平均分是{:.2f}".format(lt[0][0], lt[0][1], lt[-1][0], lt[-1][1],aver))
