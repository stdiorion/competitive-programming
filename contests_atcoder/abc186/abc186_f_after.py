class Fenwick: # add (max 1)
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

h, w, m = map(int, input().split())
obs = [tuple(map(int, input().split())) for _ in range(m)]

v_bumps = [h + 1] * (w + 1) # 下行ってぶつかる
h_bumps = [w + 1] * (h + 1) # 右行ってぶつかる

v_obs = [[] for _ in range(w + 1)]

for o in obs:
    y, x = o
    v_bumps[x] = min(v_bumps[x], y)
    h_bumps[y] = min(h_bumps[y], x)
    v_obs[x].append(y)

bit = Fenwick(h)

ans = 0
for y in range(1, h + 1):
    if h_bumps[y] == 1:
        break
    ans += h_bumps[y] - 1

if len(v_obs[1]):
    for y in range(min(v_obs[1]), h + 1):
        bit.add(y, 1)

for x in range(2, w + 1):
    for y in v_obs[x]:
        if y == 1:
            print(ans)
            exit()
        if bit.sum(y, y) == 0:
            bit.add(y, 1)
    ans += bit.sum(v_bumps[x] - 1)

print(ans)