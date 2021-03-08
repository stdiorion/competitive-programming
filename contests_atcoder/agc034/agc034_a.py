n, a, b, c, d = [int(x) - 1 for x in input().split()]
s = input()

if c > d:
    x = s[a:c + 1]
    y = s[b - 1:d + 2]
    if "##" in x or "..." not in y:
        print("No")
    else:
        print("Yes")
else:
    x = s[a:d + 1]
    if "##" in x:
        print("No")
    else:
        print("Yes")