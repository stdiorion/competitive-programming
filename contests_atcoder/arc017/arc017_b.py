n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

if k == 1:
    print(n)
    exit()

ans = 0
streak = 0
for x, y in zip(a, a[1:]):
    if x < y:
        streak += 1
        if streak >= k - 1:
            ans += 1
    else:
        streak = 0

print(ans)