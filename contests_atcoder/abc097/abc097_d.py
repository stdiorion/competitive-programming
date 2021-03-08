n, m = map(int, input().split())
p = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

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

uf = UnionFind(n);
for x, y in edges:
    uf.union(x - 1, y - 1)

ans = 0
for i, k in enumerate(p):
    ans += int(uf.is_same_group(i, k - 1))

print(ans)