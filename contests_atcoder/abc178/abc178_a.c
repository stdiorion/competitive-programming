#include <stdio.h>
int main() {
    int x;
    if (scanf("%d", &x))
        printf("%d", x ^ 1);
}