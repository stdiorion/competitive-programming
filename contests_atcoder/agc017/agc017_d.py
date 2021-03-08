from operator import xor
from functools import reduce
import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

g = [[] for _ in range(n)]
for a, b in edges:
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

visited = [False] * n

def dfs(s):
    visited[s] = True
    branches = [dfs(to) for to in g[s] if not visited[to]]
    return reduce(xor, branches, 0) + 1

if dfs(0) - 1:
    print("Alice")
else:
    print("Bob")