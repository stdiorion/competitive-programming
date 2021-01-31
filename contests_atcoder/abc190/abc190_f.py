n = int(input())
a = list(map(int, input().split()))

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

cinv = [0] * n

bit = Fenwick(n)

for i in range(n):
    cinv[0] += i - bit.sum(a[i] + 1)
    bit.add(a[i] + 1, 1)

for i, x in enumerate(a[:-1]):
    cinv[i + 1] = cinv[i] + (n - 1 - x) - x

print(*cinv, sep="\n")