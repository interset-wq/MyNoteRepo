# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

data = input()  # 姓名 年龄 性别
ages = []
genders = []
while data:
    _, gender, age = data.split()
    ages.append(int(age))
    genders.append(gender)
    data = input()
aver_age = sum(ages) / len(ages)
male_num = genders.count('男')
print("平均年龄是{:.2f} 男性人数是{}".format(aver_age, male_num))
