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
    def group_size(self, x):
        return -self.parents[self.find(x)]
    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)
    def members(self, x):
        root_x = self.find(x)
        return [i for i in range(self.size) if self.find(i) == root_x]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def dict(self):
        ret = defaultdict(list)
        for x in range(self.size):
            ret[self.find(x)].append(x)
        return ret

n, m, k = map(int, input().split())
friend = [tuple(map(int, input().split())) for _ in range(m)]
enemy = [tuple(map(int, input().split())) for _ in range(k)]

follows = [[] for _ in range(n)]
for a, b in friend:
    follows[a - 1].append(b - 1)
    follows[b - 1].append(a - 1)

blocks = [[] for _ in range(n)]
for a, b in enemy:
    blocks[a - 1].append(b - 1)
    blocks[b - 1].append(a - 1)

dsu = UnionFind(n)
ans = [0] * n

for a, b in friend:
    dsu.union(a - 1, b - 1)

for i in range(n):
    ans_ = dsu.group_size(i) - 1
    for j in follows[i]:
        ans_ -= int(dsu.is_same_group(i, j))
    for j in blocks[i]:
        ans_ -= int(dsu.is_same_group(i, j))
    ans[i] = ans_

print(*ans)