// 预处理语句
// 导入stdio.h头文件I/O库 输入输出相关的库
#include <stdio.h>

// C程序一定要从main()开始执行 并且不需要有main()函数
// void表示main()函数没有参数 有些C编译器可以省略void
// int是main()的返回值类型
int main(void) {
    int num; // 变量声明
    num = 1;
    printf("I am a simple");
    printf("computer.\n");
    printf("My favorite number is %d because it is first.\n", num);
    // 阻止代码运行完毕之后控制台自动关闭
    // 按下回车键结束程序
    getchar();

    // 结束main()函数
    return 0;
}