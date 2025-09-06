/* printf()的用法
类型符号使用不当可能造成整数溢出 */

#include <stdio.h>

int main(void) {
    unsigned un = 3000000000;
    short end = 200;
    long big = 65537;
    long long verybig = 12345678908642;

    printf("un = %u, not %d\n", un, un);
    // un = 3000000000, not -1294967296

    printf("end = %hd, not %d\n", end, end);
    // end = 200, not 200

    printf("big = %ld, not %hd\n", big, big);
    // big = 65537, not 1

    printf("verybig = %lld, not %ld\n", verybig, verybig);
    // verybig = 12345678908642, not 1942899938

    return 0;
}