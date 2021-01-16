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
                r ^= self.d[i] #
                i -= i & -i
            return r
        elif len(i) == 2:
            return self.sum(i[1]) ^ self.sum(i[0] - 1) #
    def add(self, i, x):
        while i <= self.s:
            self.d[i] ^= x #
            i += i & -i

n, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

bit = Fenwick(n, a)

for q in queries:
    if q[0] == 1:
        bit.add(q[1], q[2])
    else:
        print(bit.sum(q[1], q[2]))