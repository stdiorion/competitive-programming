INF = float("inf")
n = int(input())
ans = INF

for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        ans = min(ans, p)

if ans == INF:
    ans = -1
print(ans)