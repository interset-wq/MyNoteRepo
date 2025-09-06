# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('PY301-SunSign.csv')
ls = []
ls = f.readlines()
f.close()
while True:
    s = input('请输入星座序号（例如，5）：')
    for i in s.split():
        for line in ls:
            lt = line.strip('\n').split(',')
            if i == lt[0]:
                star = lt[1]
                sid = lt[-1]
                m1 = lt[2][:-2]
                d1 = lt[2][-2:]
                m2 = lt[3][:-2]
                d2 = lt[3][-2:]
                print("{}({})的生日是{}月{}日至{}月{}日之间".format(star,sid,m1,d1,m2,d2))
