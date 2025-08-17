// 冒泡排序 时间复杂度 O(n^2)
// 排序 [4, 3, 2, 1]
// 第一趟
    // 3, 4, 2, 1
    // 3, 2, 4, 1
    // 3, 2, 1, 4
// 第二趟
    // 2, 3, 1, 4
    // 2, 1, 3, 4
// 第三趟
    // 1, 2, 3, 4

function bubble(nums){
    let times = nums.length - 1
    for (let i=0; i<times; i++){
        for (let j=0; j<times-i; j++) {
            if (nums[j] > nums[j+1]) {
                [nums[j], nums[j+1]] = [nums[j+1], nums[j]]
            }
        }
    }
    return nums
}

// 调用函数
let nums = [4, 3, 2, 1]
console.log(bubble(nums)) // [ 1, 2, 3, 4 ]