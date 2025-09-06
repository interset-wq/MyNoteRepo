"""for循环和while循环实际上也可以使用else

在 for 或 while 循环中 break 语句可能对应一个 else 子句。 
如果循环在未执行 break 的情况下结束，else 子句将会执行。

这种用法中的else类似于 try-except-else 语句中的else
一个 try 语句的 else 子句会在未发生异常时运行，
而一个循环的 else 子句会在未发生 break 时运行。

在 for 循环中，else 子句会在循环结束其他最后一次迭代之后，
即未执行 break 的情况下被执行。

在 while 循环中，它会在循环条件变为假值后执行。

在这两类循环中，当在循环被 break 终结时 else 子句 不会 被执行。 
当然，其他提前结束循环的方式，如 return 或是引发异常，也会跳过 else 子句的执行。
"""

# 素数
for n in range(2, 10):
    # for-else
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')