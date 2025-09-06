"""双目运算符
双目运算符可以简化if-else语句"""


# if-else
num1 = 9
num2 = 7
num3 = 0
if num1 < num2:
    num3 = num1
else:
    num3 = num2
print(num3) # 输出结果 7

# 双目运算符
num1 = 9
num2 = 7
num3 = num1 if num1 < num2 else num2
print(num3) # 输出结果 7
