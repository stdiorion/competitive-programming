from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


room_from = [0, 0] + [-1] * (N - 1)

d = deque()
d.append(1)

while d:
    now = d.popleft()
    for dst in graph[now]:
        if room_from[dst] != -1:
            continue
        room_from[dst] = now
        d.append(dst)

print("Yes" if (checked := -1 not in room_from[2:]) else "No")
print(*room_from[2:] if checked else None, sep="\n")