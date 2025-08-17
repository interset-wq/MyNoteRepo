/* 随机访问元素 */

function randomAccess(nums) {
    // 在区间 [0, nums.length) 中随机抽取一个数字
    const random_index = Math.floor(Math.random() * nums.length);
    // 获取并返回随机元素
    const random_num = nums[random_index];
    return random_num;
}

// 调用函数
let nums = [1, 3, 2, 5, 4]
console.log(randomAccess(nums))