from itertools import combinations
INF = float("inf")

n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = INF
for k in range(1, n + 1):
    for comb in combinations(a, k):
        if (x - sum(comb)) % k == 0:
            ans = min(ans, (x - sum(comb)) // k)

print(ans)