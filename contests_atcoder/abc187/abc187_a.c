#include <stdio.h>
int digsum(int x) {
    int res = 0;
    do {
        res += x % 10;
        x /= 10;
    } while (x > 0);
    return res;
}
int main() {
    int a, b;
    scanf("%d%d", &a, &b);

    int sa = digsum(a), sb = digsum(b);
    if (sa > sb)
        printf("%d", sa);
    else
        printf("%d", sb);
}