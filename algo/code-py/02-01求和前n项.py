"""计算
1 + 2 + 3 + ... +n
"""

# 通过for循环实现
def sum_n_for(n: int) -> int:
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# 通过while循环实现
def sum_n_while(n: int) -> int:
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

# 递归写法
# f(n) = 1 + 2 + ... + n
# f(n-1) = 1 + 2 + ... + (n-1)
# f(n) = f(n-1) + n
# f(1) = 1
def sum_n_recur(n: int) -> int:
    if n == 1:
        return 1
    else:
        return sum_n_recur(n-1) + n
    
# 尾递归
# f(n) = n + ... + 2 + 1
# 从左到右依次做加法
# res表示已经加好的数的总和，n表示还没有加的数
# res=0时，表明计算还没有开始
def sum_n_tail_recur(n: int, res: int) -> int:
    if n == 0:
        return res
    else:
        return sum_n_tail_recur(n-1, res+n)

if __name__ == '__main__':
    n = 100
    print(sum_n_for(n)) # 5050
    print(sum_n_while(n)) # 5050
    print(sum_n_recur(n)) # 5050
