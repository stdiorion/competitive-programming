#include <stdio.h>
int main() {
    char c[3];
    scanf("%s", c);

    if (c[0] == c[1] && c[1] == c[2])
        puts("Won");
    else
        puts("Lost");
}