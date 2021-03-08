#include <stdio.h>
int main() {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    b -= c;

    if (a > b)
        puts("Takahashi");
    else
        puts("Aoki");
}