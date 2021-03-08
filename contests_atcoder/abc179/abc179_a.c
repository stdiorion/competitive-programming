#include <stdio.h>
#include <string.h>
int main() {
    char s[1000];
    scanf("%s", &s);

    if (s[strlen(s) - 1] == 's')
        printf("%s%s", s, "es");
    else
        printf("%s%s", s, "s");
}