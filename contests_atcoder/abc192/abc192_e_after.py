from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = float("inf")
n, m, x, y = map(int, input().split())
rails = [tuple(map(int, input().split())) for _ in range(m)]

edges = [[] for _ in range(n)]

for a, b, t, k in rails:
    edges[a - 1].append((b - 1, t, k))
    edges[b - 1].append((a - 1, t, k))

def dijkstra(start, goal):
    q = [(0, start)]
    dist = [INF] * n
    dist[start] = 0

    done = [False] * n

    res = INF

    while q:
        now = heappop(q)[1]
        if done[now]:
            continue
        done[now] = True

        dst_ = dist[now]

        for to, cost, gap in edges[now]:
            dst = (dst_ + gap - 1) // gap * gap
            if to == goal and dst + cost < res:
                res = dst + cost
            if not done[to] and dst + cost < dist[to]:
                dist[to] = dst + cost
                heappush(q, (dist[to], to))
    
    return res if res != INF else - 1

print(dijkstra(x - 1, y - 1))