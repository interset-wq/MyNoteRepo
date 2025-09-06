"""修改字典、列表等对象时
为了防止原列表或字典遭到修改，
可以创建副本，然后对副本进行操作"""


# 很难正确地在迭代多项集的同时修改多项集的内容。
# 更简单的方法是迭代多项集的副本或者创建新的多项集

# 创建示例多项集
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# 策略：迭代一个副本
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


# 策略：创建一个新多项集
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status