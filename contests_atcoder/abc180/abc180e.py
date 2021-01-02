from itertools import permutations
INF = float("inf")

n = int(input())
V = [list(map(int, input().split())) for _ in range(n)]

cost = [[INF] * n for _ in range(n)]

for i in permutations(range(n), 2):
    x1, y1, z1 = V[i[0]]
    x2, y2, z2 = V[i[1]]
    cost[i[0]][i[1]] = abs(x1 - x2) + abs(y1 - y2) + max(z2 - z1, 0)

dp = [[-1] * n for _ in range(1 << n)]

def dfs(S, v):
    global dp
    if dp[S][v] != -1:
        return dp[S][v]
    if S == (1 << n) - 1 and v == 0:
        return 0
    
    res = INF

    for u in range(n):
        if S >> u & 1 == 0:
            res = min(res, dfs(S | 1 << u, u) + cost[v][u])
    
    dp[S][v] = res

    return res

ans = dfs(0, 0)

if ans == INF:
    print(-1)
else:
    print(ans)