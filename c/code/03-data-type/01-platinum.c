/* 计算和体重相等重量的铂金的价值*/

#include <stdio.h>

int main(void) {
    float weight;
    float value;
    printf("你知道自己体重的铂金的价值是多少吗？\n");
    printf("让我们来 计算一下吧。\n");
    printf("请输入你的体重prounds: ");
    scanf("%f", &weight);
    value = 1700.0 * weight * 14.5833; // 计算铂金的价值
    printf("你体重的铂金的价值是 $%.2f", value);

    // 暂停程序，防止控制台自动关闭
    getchar(); // scanf必须使用回车才能完成输入，这个getchar用于接收scanf的回车
    getchar(); // 暂停程序
    return 0;
}