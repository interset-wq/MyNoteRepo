# 请在...处使用一行或多行代码替换
#
# 注意：请不要修改其他已给出代码

n = eval(input("请输入数量："))
price = 160
percent = 1
if n <= 1:
    percent = 1
elif n <= 4:
    percent = 0.9
elif n <= 9:
    percent = 0.8
elif n >= 10:
    percent = 0.7
cost = n * price * percent
print("总额为:",cost)
