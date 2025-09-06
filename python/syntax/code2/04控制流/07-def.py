"""定义函数
没有返回值的函数默认然后None
"""


def fib(n):    # 打印小于 n 的斐波那契数列
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# 现在调用我们刚定义的函数：
fib(2000)


def fib2(n):  # 返回斐波那契数组直到 n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # 见下
        a, b = b, a+b
    return result

f100 = fib2(100)    # 调用它