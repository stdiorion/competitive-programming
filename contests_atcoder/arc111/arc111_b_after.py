from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parents = [-1] * n
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return
        if self.parents[x] > self.parents[y]: x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return x, y
    def find(self, x):
        if self.parents[x] < 0: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

n = int(input())
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

uf = UnionFind(400000)

istree = [1] * 400000

for e in edges:
    if uf.is_same_group(e[0], e[1]):
        istree[uf.find(e[0])] = 0
    else:
        x, y = uf.union(e[0], e[1])
        istree[x] = 1 if istree[x] and istree[y] else 0

ans = 400000

for x in uf.roots():
    ans -= istree[x]

print(ans)