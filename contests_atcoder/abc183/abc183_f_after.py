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

n, Q = map(int, input().split())
C = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

uf = UnionFind(n)

classes = []
for c in C:
    class_count = defaultdict(int)
    class_count[c - 1] = 1
    classes.append(class_count)

def merge_class(cto, cfrom):
    for c in cfrom:
        cto[c] += cfrom[c]
    return cto

for q in queries:
    q[1] -= 1
    q[2] -= 1

    if q[0] == 1 and not uf.is_same_group(q[1], q[2]):
        x, y = uf.union(q[1], q[2])
        classes[x] = merge_class(classes[x], classes[y])
    elif q[0] == 2:
        x = uf.find(q[1])
        print(classes[x][q[2]])