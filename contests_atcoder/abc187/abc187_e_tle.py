from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# グラフを作る
graph = [[] for _ in range(n)]

for i, e in enumerate(edges):
    graph[e[0]-1].append((e[1]-1, i, False))
    graph[e[1]-1].append((e[0]-1, i, True))

# 逆向きの辺に印をつけるBFS
edges_rev = [False] * (n - 1)
visited = [False] * n

d = deque()
d.append(0)
visited[0] = True

while d:
    now = d.popleft()
    for dst in graph[now]:
        if visited[dst[0]]: continue
        visited[dst[0]] = True
        if dst[2]:
            edges_rev[dst[1]] = True
        d.append(dst[0])

start_val = 0

# クエリ読み込み
edges_val = [0] * (n - 1)

for Q in queries:
    Q[1] -= 1
    if Q[0] == 1:
        if edges_rev[Q[1]]:
            edges_val[Q[1]] += Q[2]
        else:
            edges_val[Q[1]] -= Q[2]
            start_val += Q[2]
    else:
        if not edges_rev[Q[1]]:
            edges_val[Q[1]] += Q[2]
        else:
            edges_val[Q[1]] -= Q[2]
            start_val += Q[2]

# DFS
ans = [0] * n
ans[0] = start_val

visited = [False] * n
visited[0] = True

stack = [0]

while stack:
    now = stack.pop()

    for dst in graph[now]:
        if visited[dst[0]]: continue
        visited[dst[0]] = True

        ans[dst[0]] = ans[now] + edges_val[dst[1]]
        stack.append(dst[0])

# def dfs(now, val, visited):
#     global ans
#     ans[now] = val

#     for dst in graph[now]:
#         if visited[dst[0]]: continue
#         visited[dst[0]] = True

#         dfs(dst[0], val + edges_val[dst[1]], visited)

# dfs(0, start_val, visited)

print(*ans, sep="\n")