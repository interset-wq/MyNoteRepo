# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

n = 0
m = 0
f = open("univ.txt", "r")

for line in f:  # 此处可多行
    if '大学生' in line:
        continue
    if '大学' in line:
        print(line.strip('\n'))
        n += 1
    if '学院' in line:
        print(line.strip('\n'))
        m += 1

f.close()

print("包含大学的名称数量是{}".format(n))

print("包含学院的名称数量是{}".format(m))
