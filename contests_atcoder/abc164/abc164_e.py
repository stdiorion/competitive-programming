from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10 ** 7)
INF = float("inf")

n, m, s = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
exchange = [0] + [tuple(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(n + 1)]

for u, v, cost, time in edges:
    graph[u].append((v, cost, time))
    graph[v].append((u, cost, time))

ans = [INF] * (n + 1)
ans[1] = 0
visited_prev = [set() for _ in range(n + 1)]
visited_prev[1] = {1}

def dfs(now, money, t, visited):
    global ans, visited_prev

    for to, cost, time in graph[now]:
        if t + time < ans[to] or visited > visited_prev[to]:
            if money < cost:
                excity = sorted([(exchange[city][0] / exchange[city][1], city) for city in visited], reverse=True)[0][1]
                count = -((money - cost) // exchange[excity][0])
                money += exchange[excity][0] * count
                t += exchange[excity][1] * count
            if t + time < ans[to]:
                ans[to] = t + time
            visited_prev[to] = visited | {to}
            dfs(to, money - cost, t + time, visited_prev[to])
        

dfs(1, s, 0, {1})

print(*ans[2:], sep="\n")