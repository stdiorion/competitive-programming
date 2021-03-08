#include <iostream>

int main() {
    int a, b;
    scanf("%d%d", &a, &b);

    float ans = (a - b) * 100. / a;
    printf("%f", ans);
}