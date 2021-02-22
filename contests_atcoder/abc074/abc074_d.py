from heapq import heappop, heappush
from collections import defaultdict

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

edges = defaultdict(int)
for i in range(n):
    for j in range(i + 1, n):
        edges[(i, j)] = dist[i][j]

for k in range(n):
    for i in range(n):
        for j in range(i + 1, n):
            if i == k or j == k:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                exit()
            elif dist[i][j] == dist[i][k] + dist[k][j]:
                edges[(i, j)] = 0

print(sum(edges.values()))

exit()
adj = [[(cost, to) for to, cost in enumerate(l) if cost > 0] for l in dist]

visited = [False] * n
visited[0] = True
d = [(0, 0)]
ans = 0

while d:
    cost, now = heappop(d)

    visited[now] = True
    ans += cost

    for cost, to in adj[now]:
        if not visited[to]:
            heappush(d, (cost, to))

print(ans)