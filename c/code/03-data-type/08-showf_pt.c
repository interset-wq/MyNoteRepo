/* 浮点数 */

#include <stdio.h>

int main(void) {
    float about = 32000.0;
    double abet = 2.14e9; // 指数计数法
    long double dip = 5.32e-5;
    printf("%f 可以写作 %e\n", about, about);
    printf("%f 可以写作 %e\n", abet, abet);
    printf("%Lf 可以写作 %Le\n", dip, dip);
    return 0;
}


// 32000.000000 可以写作 3.200000e+04
// 2140000000.000000 可以写作 2.140000e+09
// 0.000000 可以写作 3.108171e-317