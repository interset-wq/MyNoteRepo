/* 遍历数组 */

nums = [1, 2, 3, 4];

// 通过索引遍历数组 for循环
let sum1 = 0;
for (let i = 0; i < nums.length; i++) {
    sum1 += nums[i];
}
console.log(sum1); // 10

// 通过索引遍历数组 while循环
let sum3 = 0;
let i = 0;
while (i < nums.length) {
    sum3 += nums[i];
    i++;
}
console.log(sum3); // 10

// 直接遍历数组 for-of循环
let sum2 = 0;
for (const num of nums) {
    sum2 += num;
}
console.log(sum2); // 10