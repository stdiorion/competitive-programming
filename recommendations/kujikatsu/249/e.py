from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n + m - 1)]

graph = [[] for _ in range(n + 1)]
count_in = [0] * (n + 1)

# ついでにねをさがす
roots = set(range(1, n + 1))
for u, v in edges:
    graph[u].append(v)
    roots.discard(v)
    count_in[v] += 1
root = roots.pop()

d = deque()
d.append(root)
parent = [0] * (n + 1)

while d:
    now = d.popleft()
    for to in graph[now]:
        if count_in[to] == 1:
            d.appendleft(to)
            parent[to] = now
        else:
            count_in[to] -= 1

print(*parent[1:], sep="\n")