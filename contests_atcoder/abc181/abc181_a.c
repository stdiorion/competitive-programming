#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);

    if (n % 2)
        puts("Black");
    else
        puts("White");
}