/* 分别使用十进制、八进制、十六进制打印十进制数100 */

#include <stdio.h>

int main(void) {
    int num = 100;

    printf("不带前缀： ");
    printf("dec = %d, octal = %o, hex = %x\n", num, num, num);
    // 不带前缀： dec = 100, octal = 144, hex = 64

    printf("带前缀： ");
    printf("dec = %d, octal = %#o, hex = %#x", num, num, num);
    // 带前缀： dec = 100, octal = 0144, hex = 0x64
    
    return 0;
}