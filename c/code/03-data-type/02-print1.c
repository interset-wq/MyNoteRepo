/* printf()函数的用法 */

#include <stdio.h>

int main(void) {
    int ten = 10;
    int two = 2;

    printf("正确用法： ");
    printf("%d - %d = %d\n", ten, 2, ten-two);
    // 正确用法： 10 - 2 = 8

    // printf少传入了两个参数，缺失的参数会随机使用内存中的数字
    printf("错误用法： ");
    printf("%d - %d = %d", ten);
    // 错误用法： 10 - -4 = 0

    return 0;
}