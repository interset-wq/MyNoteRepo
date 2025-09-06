/* 一个C文件中有两个函数的情形 */

#include <stdio.h>

void butler(void); // 函数声明（函数原型）

int main(void) {
    printf("I will summon the butler function.\n");
    butler(); // 调用函数
    printf("Yes. Bring me some tea and writable DVDs.\n");
    return 0;
}

// 定义函数
// 无返回值 无参数
void butler(void) {
    printf("You rang, sir?\n");
}