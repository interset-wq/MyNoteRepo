"""查找元素
在数组中查找指定元素需要遍历数组，
每轮判断元素值是否匹配，若匹配则输出对应索引。
因为数组是线性数据结构，所以上述查找操作被称为“线性查找”。
"""

def find_elem(nums: list[int], elem: int) -> int:
    """在列表中查找元素
    Args:
        nums (list[int]): 列表
        elem (int): 被查找的元素
    
    Returns:
        int: 被查找元素在列表中的下标，没找到返回-1
    """
    for i in range(len(nums)):
        if nums[i] == elem:
            return i
    return -1

if __name__ == '__main__':
    nums = [1, 3, 6, 4]
    index = find_elem(nums, 6)
    print(index) # 2
