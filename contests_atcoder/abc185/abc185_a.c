#include <stdio.h>
int main() {
    int a[4];
    for (int i = 0; i < 4; ++i)
        scanf("%d", &a[i]);

    int ans = 1e9;
    for (int i = 0; i < 4; ++i) {
        if (a[i] < ans)
            ans = a[i];
    }
    printf("%d", ans);
}