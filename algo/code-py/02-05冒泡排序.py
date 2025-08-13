"""冒泡排序 时间复杂度平方阶
例如 从小到大排序列表 nums = [4, 3, 2, 1] 最坏情况
第一趟 
    3, 4, 2, 1
    3, 2, 4, 1
    3, 2, 1, 4
第二趟
    2, 3, 1, 4
    2, 1, 3, 4
第三趟
    1, 2, 3, 4

趟数 = len(nums) - 1
每趟次数 = len(nums) - 趟号
"""

def bubble(nums: list) -> list:
    times = len(nums) - 1
    # 外层循环控制排序趟数
    for i in range(times):
        # 内层循环控制每趟比较次数，每完成一趟，下一趟就少比较一次
        for j in range(times - i):
            # 比较相邻元素，如果前一个大于后一个则交换
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == '__main__':
    nums = [4, 3, 2, 1]
    print(bubble(nums))  # [1, 2, 3, 4]
    
