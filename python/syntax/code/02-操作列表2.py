"""操作列表"""


"""zip()同时遍历多个列表
zip()将多个列表合成为 元组列表
这个嵌套了元组的列表的长度等于所有列表中的最短的长度
"""
langs = ['python', 'javascript', 'c++']
extensions = ['py', 'js', 'cpp']
for lang, extension in zip(langs, extensions):
    print(f'{lang}语言的后缀名是{extension}')
    # python语言的后缀名是py
    # javascript语言的后缀名是js
    # c++语言的后缀名是cpp

"""enumerate()同时遍历索引和元素
通过start可以指定索引的起始值，默认是0
"""
langs = ['python', 'javascript', 'c++']
for index, lang in enumerate(langs, start=1):
    print(index, lang)
    # 1 python
    # 2 javascript
    # 3 c++

"""列表推导式"""
# 不使用列表推导式
squires = []
for num in range(1, 10):
    squire = num ** 2
    squires.append(squire)
print(squires) # 输出结果 [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 使用列表推导式
squires = [num**2 for num in range(1, 10)]
print(squires) # 输出结果 [1, 4, 9, 16, 25, 36, 49, 64, 81]

"""判断语句和列表推导式"""
results = [i for i in range(5) if i % 2 == 0]
print(results) # [0, 2, 4]

results = ['偶数' if i % 2 == 0 else '奇数' for i in range(5)]
print(results) # ['偶数', '奇数', '偶数', '奇数', '偶数']