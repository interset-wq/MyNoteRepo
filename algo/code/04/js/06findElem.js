/* 查找元素 */

function findElem(nums, elem) {
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === elem) return i;
    }
    return -1;
}

let nums = [1, 3, 6, 4];
let index = findElem(nums, 6);
console.log(index); // 2