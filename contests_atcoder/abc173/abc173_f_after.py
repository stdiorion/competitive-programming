n = int(input())
ans = n * (n + 1) * (n + 2) // 6
for _ in range(n - 1):
    l, r = map(int, input().split())
    if l > r: l, r = r, l
    ans -= l * (n + 1 - r)
print(ans)