/* 整数的值超出int最大范围的情形
整数溢出之后会回到最小值
*/

#include <stdio.h>

int main(void) {
    int i = 2147483647;
    unsigned j = 4294967295;

    printf("%d %d %d\n", i, i+1, i+2);
    // 2147483647 -2147483648 -2147483647

    printf("%u %u %u\n", j, j+1, j+2);
    // 4294967295 0 1

    return 0;
}