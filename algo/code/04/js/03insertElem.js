/* 插入元素 */

function insertElem(nums, index, num) {
    for (let i = nums.length - 1; i > index; i--) {
        nums[i] = nums[i - 1]
    }
    nums[index] = num
    return nums
}

// 调用函数
nums = [1, 3, 2, 5, 4]
console.log(nums) // [1, 3, 2, 5, 4]
console.log(insertElem(nums, 2, 6)) // [1, 3, 6, 2, 5]