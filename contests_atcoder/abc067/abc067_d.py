from collections import deque
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

g = [[] for _ in range(n)]

for a, b in edges:
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

d = deque([0, n - 1])
color = [""] * n
color[0] = "Fennec"
color[n - 1] = "Snuke"

while d:
    now = d.popleft()

    for to in g[now]:
        if color[to] != "":
            continue
        color[to] = color[now]
        d.append(to)

if color.count("Fennec") > color.count("Snuke"):
    print("Fennec")
else:
    print("Snuke")