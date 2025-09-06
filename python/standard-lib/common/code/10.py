import statistics


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

"""计算均值"""
print(statistics.mean(data)) # 1.6071428571428572

"""计算中位数"""
print(statistics.median(data)) # 1.25

"""计算方差"""
print(statistics.variance(data)) # 1.3720238095238095