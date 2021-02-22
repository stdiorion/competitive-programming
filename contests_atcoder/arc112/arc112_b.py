b, c = map(int, input().split())

if b == 0:
    ans = c
elif b > 0:
    if c < 3:
        ans = c + 1
    elif 3 <= c <= 2 * b:
        ans = 2 * c - 1
    else:
        ans = 2 * b + c - 1
else:
    b = abs(b)
    if c < 3:
        ans = c + 1
    elif 3 <= c <= 2 * b + 1:
        ans = 2 * c - 1
    else:
        ans = 2 * b + c

print(ans)