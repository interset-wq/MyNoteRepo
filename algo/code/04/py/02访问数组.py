"""访问数组元素
通过索引（index，下标）可以访问数组元素
数组下标从0开始
这个过程的时间复杂度是O(1)
"""

# python列表除了以上数组的性质外
# 还可以使用负数下标访问元素

from random import randint
# randint是闭区间 返回区间内的随机整数

def random_access(nums: list[int]) -> int:
    """随机访问元素"""
    random_index = randint(0, len(nums) - 1)
    # 获取并返回随机元素
    random_num = nums[random_index]
    return random_num

if __name__ == '__main__':
    nums = [1, 3, 2, 5, 4]
    print(random_access(nums))