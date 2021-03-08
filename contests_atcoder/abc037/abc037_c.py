n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
d = 0
for i in range(n):
    if i <= n - k:
        d += 1
    if i >= k:
        d -= 1
    ans += d * a[i]
print(ans)