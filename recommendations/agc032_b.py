from itertools import combinations, compress
from operator import mul
from functools import reduce

n = int(input())

# 両端を足してn (n:奇数), n+1 (n:偶数)になる辺は結ばない
illegal = n // 2 * 2 + 1

edges = list(combinations(range(1, n + 1), 2))
ans = ""
count = 0

for e in edges:
    if sum(e) != illegal:
        ans += str(e[0]) + " " + str(e[1]) + "\n"
        count += 1

print(count)
print(ans)

exit()
# 以下はbit全探索によるコード

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

c = combinations_count(n, 2)

for i in range(2 ** c):
    s = -1
    
    edges_flag = [False] * c

    for j in range(c):
        if (i >> j) & 1:
           edges_flag[j] = True
    
    edges_active = list(compress(edges, edges_flag))

    edges_nb = [0] * n

    # 各ノードごとに隣接する頂点を足していく
    for e in edges_active:
        edges_nb[e[0] - 1] += e[1]
        edges_nb[e[1] - 1] += e[0]
    
    if min(edges_nb) == max(edges_nb) != 0:
        print(f"S={min(edges_nb)}")
        print(*edges_active, sep="\n")