"""match-case
match 语句接受一个表达式并把它的值
与一个或多个 case 块给出的一系列模式进行比较。
只有第一个匹配的模式会被执行，
并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。
"""


# 将一个主语值与一个或多个字面值进行比较
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # 默认情形
        case _:
            return "Something's wrong with the internet"

# 可以用 | （“或”）将多个字面值组合到一个模式中
def http_error2(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"


if __name__ == '__main__':
    status = 404
    print(http_error2(status))