/* 查找元素 */

#include <stdio.h>

int findElem(int *nums, int length, int elem) {
    for (int i = 0; i < length; i++) {
        if (nums[i] == elem) return i;
    }
    return -1;
}

int main() {
    int nums[4] = {1, 3, 6, 4};
    int length = sizeof(nums) / sizeof(nums[0]);
    int index = findElem(nums, length, 6);
    printf("%d\n", index); // 2
    return 0;
}