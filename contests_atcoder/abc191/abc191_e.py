from heapq import heappop, heappush
import sys
input = sys.stdin.buffer.readline
INF = 10 ** 9
n, m = map(int, input().split())
road = [tuple(map(int, input().split())) for _ in range(m)]


edges = [[] for _ in range(n)]

for a, b, c in road:
    edges[a - 1].append((b - 1, c))

def dijkstra(start):
    q = [(0, start)]
    dist = [INF] * n
    dist[start] = 0

    done = [False] * n

    res = INF

    while q:
        now = heappop(q)[1]
        done[now] = True

        dst = dist[now]

        for to, cost in edges[now]:
            if to == start and dst + cost < res:
                res = dst + cost
            if not done[to] and dst + cost < dist[to]:
                dist[to] = dst + cost
                heappush(q, (dist[to], to))
    
    return res if res != INF else -1

for i in range(n):
    print(dijkstra(i))