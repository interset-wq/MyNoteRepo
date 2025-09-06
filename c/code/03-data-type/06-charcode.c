/* 字符对应的ASCII码 */

#include <stdio.h>

int main(void) {
    char ch;
    printf("请输入一个字符： ");
    scanf("%c", &ch);
    printf("字符 %c 对应的ASCII码是 %d", ch, ch);
    return 0;
}

// 请输入一个字符： a
// 字符 a 对应的ASCII码是 97