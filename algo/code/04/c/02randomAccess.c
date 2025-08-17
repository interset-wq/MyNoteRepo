/* 访问随机元素 */

#include <stdio.h> // printf()函数
#include <stdlib.h> // rand()函数
#include <time.h>  // 用于时间相关函数

/* 随机访问元素 */
int randomAccess(int *nums, int size) {
    // 在区间 [0, size) 中随机抽取一个数字
    int randomIndex = rand() % size;
    // 获取并返回随机元素
    int randomNum = nums[randomIndex];
    return randomNum;
}

int main() {
    // 设置随机数种子，使每次运行产生不同的随机序列
    srand(time(NULL));
    int nums[5] = { 1, 3, 2, 5, 4 };
    int randomValue = randomAccess(nums, 5);
    printf("%d\n", randomValue);
    return 0;
}
