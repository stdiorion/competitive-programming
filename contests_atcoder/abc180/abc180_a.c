#include <stdio.h>
int main() {
    int n, a, b;
    scanf("%d%d%d", &n, &a, &b);
    int ans = n - a + b;
    printf("%d", ans);
}