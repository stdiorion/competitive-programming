from collections import deque
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

g = [[] for _ in range(n)]
for u, v in edges:
    g[u-1].append(v-1)
    g[v-1].append(u-1)

if n > 1:
    f = [1, 1] + [0] * n
    for i in range(n):
        f[i + 2] = f[i + 1] + f[i]
        if f[i + 2] == n:
            break
        elif f[i + 2] > n:
            print("NO")
            exit()


d = [0]
visited = [0] * n
while d:
    now = d.pop()
    visited[now] = 1
    count = 0
    for to in g[now]:
        if visited[to]:
            continue
        d.append(to)
        count += 1
        if count > 2:
            print("NO")
            exit()

print("YES")