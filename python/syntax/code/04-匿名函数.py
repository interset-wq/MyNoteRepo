"""匿名函数"""


# 把函数作为参数传入
def anonymous(func):
    result = func(2, 5)
    print(result)

def get_sum(x, y):
    return x + y

anonymous(get_sum) # 输出结果 7

# lambda函数
get_sum = lambda x, y : x + y
print(get_sum(2, 5)) # 输出结果 7