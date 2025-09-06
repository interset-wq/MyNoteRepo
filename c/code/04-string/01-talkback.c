

#include <stdio.h>
#include <string.h> // 提供strlen()函数
#define DENSITY 62.4 // 定义常量 人体密度

int main(void) {
    float weight, volume;
    int size, letters;
    char name[40]; // 字符串，容量是40的字符数组，每个字符1字节
    printf("你的名字是什么？\n");
    scanf("%s", name); // name本来就是地址，不需要使用取地址运算符&
    printf("%s，你的体重是多少磅？\n", name);
    scanf("%f", &weight);
    size = sizeof name;
    letters = strlen(name);
    volume = weight / DENSITY;
    printf("%s，你的体积是%f立方英尺\n", name, volume);
    printf("你的名字有%d个字母\n", letters);
    printf("存储你的名字需要%dbytes", size);
    return 0;
}