"""遍历数组
"""

nums = [1, 2, 3, 4]

# 通过索引遍历数组 while循环
sum0 = 0
i = 0
while i < len(nums):
    sum0 += nums[i]
    i += 1
print(sum0) # 10

# 通过索引遍历列表 for循环
sum1 = 0
for i in range(len(nums)):
    sum1 += nums[i]
print(sum1) # 10

# 直接遍历列表元素 for循环
sum2 = 0
for num in nums:
    sum2 += num
print(sum2) # 10

# 同时遍历索引和元素 for循环
sum3 = 0
sum4 = 0
for i, num in enumerate(nums):
    sum3 += nums[i]
    sum4 += num
print(sum3)
print(sum4)