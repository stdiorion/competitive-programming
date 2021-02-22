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

h, w = map(int, input().split())
field = [[x == "#" for x in input()] for _ in range(h)]

if h == 2 or w == 2:
    print(0)
    exit()

unreachable_r = set(range(1, h - 1))
unreachable_c = set(range(1, w - 1))

# (i, isrow)
new_reachable = []

for i in range(1, h - 1):
    if field[i][0] or field[i][-1]:
        unreachable_r.discard(i)
        new_reachable.append((i, True))

for i in range(1, w - 1):
    if field[0][i] or field[-1][i]:
        unreachable_c.discard(i)
        new_reachable.append((i, False))

# print(unreachable_r)
# print(unreachable_c)
while new_reachable:
    i, is_row = new_reachable.pop()
    if is_row:
        unreachable_r.discard(i)
        for x in unreachable_c:
            if field[i][x]:
                new_reachable.append((x, False))
    else:
        unreachable_c.discard(i)
        for y in unreachable_r:
            if field[y][i]:
                new_reachable.append((y, True))

ans = min(len(unreachable_r), len(unreachable_c))

dsu_col = UnionFind(w)

for y in unreachable_r:
    flag = True
    parent = None
    for x in unreachable_c:
        if field[y][x]:
            if flag:
                flag = False
                parent = x
            else:
                dsu_col.union(parent, x)

rset = set()
for x in unreachable_c:
    rset.add(dsu_col.find(x))

dsu_row = UnionFind(h)

for x in unreachable_c:
    flag = True
    parent = None
    for y in unreachable_r:
        if field[y][x]:
            if flag:
                flag = False
                parent = y
            else:
                dsu_row.union(parent, y)

cset = set()
for y in unreachable_r:
    cset.add(dsu_row.find(y))

ans = min(ans, len(rset), len(cset))

print(ans)