n = int(input())

# https://qiita.com/takayg1/items/c811bd07c21923d7ec69

#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
ide_ele = -float("inf")
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

d = []
max_valley = 0

for i in range(n):
    s = input()
    delta = len(s) - 2 * s.count(")")
    valley = 0
    y = 0
    for l in s:
        y += 1 if l == ")" else -1
        valley = max(valley, y)
    max_valley = max(max_valley, valley)
    if delta == valley == 0:
        continue
    d.append((delta, valley))

d.sort(key=lambda x:x[1])

pos_depth = [-1] * (max_valley + 1)

idx = 0
for i, x in enumerate(d):
    while idx < x[1]:
        pos_depth[idx] = i
        idx += 1
    if x[1] == max_valley:
        for j in range(idx, max_valley + 1):
            pos_depth[j] = len(d)
        break

D = [x[0] for x in d]

seg = SegTree(D, segfunc, ide_ele)


h = 0

used = set()

while len(used) < len(d):
    delta = seg.query(0, pos_depth[min(h, max_valley)])
    if delta == -float("inf"):
        print("No")
        exit()
    i = D[:pos_depth[min(h, max_valley)]].index(delta)
    h += delta
    if h < 0:
        print("No")
        exit()

    D[i] = -float("inf")
    seg.update(i, -float("inf"))
    used.add(i)

if h:
    print("No")
else:
    print("Yes")