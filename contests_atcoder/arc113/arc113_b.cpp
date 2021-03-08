#include <iostream>
int a, b, c, ans;

int main() {
    scanf("%d%d%d", &a, &b, &c);

    b %= 4;

    if (b == 2) {
        if (c == 1) b = 2;
        else b = 0;
    }
    else if (c & 1) b %= 4;
    else b = b * b % 4;

    if (b == 0) b = 4;

    a %= 10;
    ans = 1;
    for (int i = 0;i < b;++i) ans = ans * a % 10;
    
    printf("%d\n", ans);
}