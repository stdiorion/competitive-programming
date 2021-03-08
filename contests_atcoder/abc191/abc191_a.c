#include <stdio.h>
int main() {
    int v, t, s, d;
    scanf("%d%d%d%d", &v, &t, &s, &d);

    if (v * t <= d && d <= v * s)
        printf("No\n");
    else
        printf("Yes\n");
}