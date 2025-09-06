"""列表推导式
可以嵌套
"""


# 下面这个 3x4 矩阵，由 3 个长度为 4 的列表组成
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

"""实现矩阵转置"""
# 嵌套的列表推导式
new_matrix = [[row[i] for row in matrix] for i in range(4)]
    # 等价于 new_matrix = list(zip(*matrix))

# 等价于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

# 等价于
transposed = []
for i in range(4):
    # 以下 3 行实现了嵌套的列表组
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
