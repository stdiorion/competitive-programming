import sys
input = sys.stdin.readline
from operator import itemgetter

class Fenwick:
    def __init__(self, n, l=[]):
        self.s = n
        self.d = [0] * (n + 1)
        for i, x in enumerate(l, 1):
            self.add(i, x)
    def sum(self, *i):
        if len(i) == 1:
            i = i[0]
            r = 0
            while i >= 1:
                r += self.d[i]
                i -= i & -i
            return r
        elif len(i) == 2:
            return self.sum(i[1]) - self.sum(i[0] - 1)
    def add(self, i, x):
        while i <= self.s:
            self.d[i] += x
            i += i & -i

n, m, Q = map(int, input().split())
trains = [list(map(int, input().split())) + [0, 0] for _ in range(m)]
queries = [list(map(int, input().split())) + [1, i] for i in range(Q)]

que = trains + queries
que.sort(key=itemgetter(1, 2))

bit = Fenwick(n)

ans = [0] * Q

for l, r, type, i in que:
    if type == 0:
        bit.add(l, 1)
    else:
        ans[i] = bit.sum(l, r)

print(*ans, sep="\n")