# 斐波那契数列模块

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# 运行这个文件 __name__ 返回字符串 '__main__'
# print(__name__) # __main__

"""以脚本方式执行模块 通过import导入时，if后面的代码不会自动运行"""
if __name__ == "__main__":
    import sys
    # 通过命令行参数通过命令行调用函数
    fib(int(sys.argv[1]))

# 切换到此文件所在目录 在命令行输入
# > python fibo.py 100
# 0 1 1 2 3 5 8 13 21 34 55 89 