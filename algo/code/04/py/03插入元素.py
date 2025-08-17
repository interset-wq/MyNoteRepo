"""插入元素
数组元素在内存中是“紧挨着的”，
它们之间没有空间再存放任何数据。
如果想在数组中间插入一个元素，
则需要将该元素之后的所有元素都向后移动一位，
之后再把元素赋值给该索引。
由于数组的长度是固定的，
因此插入一个元素必定会导致数组尾部元素“丢失”。
"""

# python列表的长度不是固定的

def insert_elem(nums: list[int], index: int, num: int):
    """指定下标插入元素
    这是在模拟真正的数组插入元素
    并不是列表插入元素
    """
    # 通过副本防止原列表被修改
    nums = nums[:]
    # 抛弃最后一个元素
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num
    return nums

if __name__ == '__main__':
    nums = [1, 3, 2, 5, 4]
    print(nums) # [1, 3, 2, 5, 4]

    # 数组插入元素 数组长度不变 抛弃最后一个元素
    new_nums = insert_elem(nums, index=2, num=6) 
    print(new_nums) # [1, 3, 2, 5, 4]
    # 列表插入元素 列表长度增加
    nums.insert(2, 6) 
    print(nums) # [1, 3, 6, 2, 5, 4]