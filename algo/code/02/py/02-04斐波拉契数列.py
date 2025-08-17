"""斐波拉契数列第n项
斐波拉契数列 0, 1, 1, 2, 3, 5, ...
数列中的每一项为前两项之和
f(n) = f(n-1) + f(n-2)
f(1) = 0
f(2) = 1
"""

# 递归树
def fib(n: int) -> int:
    if n == 1 or n == 2:
        return n-1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    n = 5
    print(fib(5)) # 3
