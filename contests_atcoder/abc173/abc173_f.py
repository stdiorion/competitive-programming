n = int(input())
ans = n * (n + 1) // 2

for _ in range(n - 1):
    u, v = map(int, input().split())
    a = abs(u - v) - 1
    ans += a * (a + 1) // 2

print(ans)