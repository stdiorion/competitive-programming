n, *a = map(int, open(0))

ans = 0

for i in range(n):
    ans += a[i] // 2
    a[i] %= 2
    if i < n - 1:
        ans += min(a[i], a[i + 1])
        a[i + 1] -= min(a[i], a[i + 1])

print(ans)