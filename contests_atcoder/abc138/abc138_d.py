from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, q = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

vertex = [0] * (n + 1)

for _ in range(q):
    p, q = map(int, input().split())
    vertex[p] += q


d = [1]
visited = [False] * (n + 1)
visited[1] = True

ans = 0

while d:

    now = d.pop()

    for nxt in edges[now]:
        if visited[nxt]:
            continue
        visited[nxt] = True

        vertex[nxt] += vertex[now]

        d.append(nxt)

print(*vertex[1:])