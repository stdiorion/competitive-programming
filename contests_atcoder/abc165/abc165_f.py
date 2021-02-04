from bisect import bisect_left
import sys
sys.setrecursionlimit(10 ** 7)
INF = float("inf")

n = int(input())
a = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph = [[] for _ in range(n)]

for u, v in edges:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

d = [0]

dp = [INF] * n
ans = [0] * n
visited = [False] * n
visited[0] = True

def dfs(now):
    global dp, ans, visited
    chg_idx = bisect_left(dp, a[now])
    saved_value = dp[chg_idx]
    dp[chg_idx] = a[now]

    ans[now] = bisect_left(dp, INF)

    for nxt in graph[now]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(nxt)
    
    dp[chg_idx] = saved_value

dfs(0)

print(*ans, sep="\n")