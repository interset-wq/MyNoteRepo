/* 转义字符 */

#include <stdio.h>

int main(void) {
    float salary;
    printf("\a请输入你预期的工资： ");
    printf("$______\b\b\b\b\b\b");
    scanf("%f", &salary);
    printf("\n\t月薪$%.2f，或年薪%.2f", salary, salary*12.0);
    printf("\r收到\n");
    return 0;
}