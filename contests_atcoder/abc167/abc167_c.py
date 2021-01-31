n, m, x = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]

ans = float("inf")

for i in range(1 << n):
    a = [0] * m
    cost = 0
    for j in range(n):
        if (i >> j) % 2:
            a = [u + v for u, v in zip(a, books[j][1:])]
            cost += books[j][0]
    if min(a) >= x:
        ans = min(ans, cost)

if ans == float("inf"):
    print(-1)
else:
    print(ans)