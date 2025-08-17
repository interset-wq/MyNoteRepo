/* 删除元素 */


function removeElem(nums, index) {
    for (let i = index; i < nums.length - 1; i++) {
        nums[i] = nums[i+1]
    }
    return nums
}

// 调用函数
nums = [1, 3, 2, 5, 4]
console.log(nums) // [1, 3, 2, 5, 4]
console.log(removeElem(nums, 3)) // [1, 3, 2, 4, 4]