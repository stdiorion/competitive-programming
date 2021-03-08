#include <stdio.h>
int main() {
    int x, y;
    scanf("%d%d", &x, &y);

    if (x > y) {
        x ^= y;
        y = x ^ y;
        x ^= y;
    }

    if (y - x < 3)
        puts("Yes");
    else
        puts("No");
}