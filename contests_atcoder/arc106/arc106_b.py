n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
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
    def dict(self):
        ret = defaultdict(list)
        for x in range(self.size):
            ret[self.find(x)].append(x)
        return ret

uf = UnionFind(n)

for c, d in edges:
    uf.union(c-1, d-1)

for g in uf.dict().values():
    sum_a = 0
    sum_b = 0
    for i in g:
        sum_a += a[i]
        sum_b += b[i]
    if sum_a != sum_b:
        print("No")
        exit()

print("Yes")