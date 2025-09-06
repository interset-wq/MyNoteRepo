/* 可移植整数类型
由于整型int的内存大小和操作系统有关
兼容32位系统和64位系统 */

#include <stdio.h>
#include <inttypes.h> // 导入可移植类型

int main(void) {
    int32_t me32; // 32位有符号整型
    me32 = 45933945;
    printf("me32 = %d\n", me32);
    printf("me32 = %" PRId32 "\n", me32); 
    // 上面是固定写法，类似于printf("me32 = %d\n", me32);

    // 拼接字符串
    printf("hello" "world"); // helloworld
    return 0;
}

// me32 = 45933945
// me32 = 45933945