#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int ans = 1001001001;
    for (int i = 0; i < n; ++i) {
        int a, p, x;
        scanf("%d%d%d", &a, &p, &x);
        if (a < x && p < ans) {
            ans = p;
        }
    }
    if (ans == 1001001001) ans = -1;
    printf("%d", ans);
}