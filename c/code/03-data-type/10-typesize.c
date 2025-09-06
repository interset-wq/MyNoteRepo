/* 操作系统中C语言基本数据类型的内存大小 */

#include <stdio.h>

int main(void) {
    printf("int类型的大小是 %zd bytes\n", sizeof(int));
    printf("char类型的大小是 %zd bytes\n", sizeof(char));
    printf("long int类型的大小是 %zd bytes\n", sizeof(long));
    printf("long long int类型的大小是 %zd bytes\n", sizeof(long long));
    printf("double类型的大小是 %zd bytes\n", sizeof(double));
    printf("long double类型的大小是 %zd bytes\n", sizeof(long double));
    printf("float类型的大小是 %zd bytes\n", sizeof(float));
}

// int类型的大小是 4 bytes
// char类型的大小是 1 bytes
// long int类型的大小是 4 bytes
// long long int类型的大小是 8 bytes
// double类型的大小是 8 bytes
// long double类型的大小是 16 bytes
// float类型的大小是 4 bytes