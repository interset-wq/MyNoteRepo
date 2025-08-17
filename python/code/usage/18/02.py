"""生成随机数"""

import random as r
def calpi(c, darts):
    p = 0
    for _ in range(darts):
        p += r.randint(0, darts)
    print("{:2} {:12} {:12}".format(c, darts, p))

n = 4
DART = 3
r.seed(1)
for i in range(n):
    calpi(i+1, DART*(i+1))