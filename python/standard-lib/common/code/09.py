import random


# 从传入的选项中随机抽取一个
print(random.choice(['apple', 'pear', 'banana']))

random.sample(range(100), 10)   # 无替代的取样

# [0.0, 1.0) 区间的随机浮点数
print(random.random())   

# 随机抽取0-6的整数，左闭右开
print(random.randrange(6))    # 从 range(6) 中随机选取的整数