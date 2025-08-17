/* 遍历数组 */

#include <stdio.h>

int main() {
    int nums[4] = {1, 2, 3, 4};
    int length = sizeof(nums) / sizeof(nums[0]);
    int i = 0;

    // 通过索引遍历数组 while循环
    int sum1 = 0;
    while (i < length) {
        sum1 += nums[i];
        i++;
    }
    printf("%d\n", sum1); // 10

    // 通过索引遍历数组 for循环
    int sum2 = 0;
    for (i = 0; i < length; i++) {
        sum2 += nums[i];
    }
    printf("%d\n", sum2); // 10
    return 0;
}