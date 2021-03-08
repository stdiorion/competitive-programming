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
                r += self.d[i] #
                i -= i & -i
            return r
        elif len(i) == 2:
            return self.sum(i[1]) - self.sum(i[0] - 1) #
    def add(self, i, x):
        while i <= self.s:
            self.d[i] += x #
            i += i & -i

n = int(input())
s = input()
q = int(input())
queries = [tuple(input().split()) for _ in range(q)]

bit = [[] for _ in range(26)]
for i in range(26):
    bit[i] = Fenwick(n)

for i, l in enumerate(s, 1):
    q = ord(l) - ord("a")
    bit[q].add(i, 1)

for tp, i, q in queries:
    if tp == "1":
        i = int(i)
        q = ord(q) - ord("a")
        for let in range(26):
            if bit[let].sum(i, i) and q != let:
                bit[let].add(i, -1)
            elif not bit[let].sum(i, i) and q == let:
                bit[let].add(i, 1)
    else:
        i, q = int(i), int(q)
        print(sum(bit[let].sum(i, q) > 0 for let in range(26)))
