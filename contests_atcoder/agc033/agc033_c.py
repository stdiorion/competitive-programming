INF = float("inf")
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

def tree_diameter_dfs(g):
    d = [0]
    dist = [float("inf")] * n
    dist[0] = 0
    farthest = 0

    while d:
        now = d.pop()
        for to in g[now]:
            if dist[to] == float("inf"):
                d.append(to)
                dist[to] = dist[now] + 1
                if dist[to] > dist[farthest]:
                    farthest = to

    d = [farthest]
    dist = [float("inf")] * n
    dist[farthest] = 0

    while d:
        now = d.pop()
        for to in g[now]:
            if dist[to] == float("inf"):
                d.append(to)
                dist[to] = dist[now] + 1

    return max(dist)

g = [[] for _ in range(n)]
for a, b in edges:
    g[a-1].append(b-1)
    g[b-1].append(a-1)

if tree_diameter_dfs(g) % 3 == 1:
    ans = "Second"
else:
    ans = "First"
print(ans)