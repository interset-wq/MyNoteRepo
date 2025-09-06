"""break
跳出当前循环
指的是最近一级的for或while循环
"""


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break


# 4 equals 2 * 2
# 6 equals 2 * 3
# 8 equals 2 * 4
# 9 equals 3 * 3