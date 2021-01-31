from collections import deque, defaultdict
INF = float("inf")

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

k = int(input())
c = list(map(int, input().split()))

ans = INF

graph2 = defaultdict(dict)

for s in c:
    dist = [0] + [INF] * (n)
    dist[s] = 0

    d = deque()
    d.append(s)

    while d:
        now = d.popleft()
        for dst in graph[now]:
            if dist[dst] != INF: continue
            dist[dst] = dist[now] + 1
            d.append(dst)
    
    graph2[s] = {i: t for i, t in enumerate(dist) if i in c}

# dp[bit][j] = bitが立っている街を訪れ、最後に訪れたのはjであるときの最短路長
dp = [[INF] * k for _ in range(1 << k)]

# 初期状態　
for i in range(k):
    dp[1 << i][i] = 1

for bit in range(1 << k):
    for v in range(k):
        for u in range(k):  # u から v に移動する場合を考える
            # u != v が必要
            if v == u: continue
            # u が訪問済であることが必要
            if bit != 0 and not (bit & (1 << u)): continue
            # v が未訪問であることが必要
            if bit & (1 << v): continue
            # u から v に行ったほうが短ければ更新
            dp[bit | (1 << v)][v] = min(dp[bit | (1 << v)][v], dp[bit][u] + graph2[c[u]][c[v]])

ans = min(dp[-1])

print(-1 if ans == INF else ans)
