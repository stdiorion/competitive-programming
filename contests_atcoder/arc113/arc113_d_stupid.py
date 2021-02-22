from itertools import product
from collections import defaultdict
MOD = 998244353
n, m, k = map(int, input().split())

def stupid(n, m, k):
    ret = defaultdict(int)


    for content in product(range(1, k + 1), repeat=n * m):
        a = []
        b = [0] * m
        for i in range(n):
            for j in range(m):
                b[j] = max(b[j], content[i * m + j])
            a.append(min(content[i * m:(i + 1) * m]))
        ret[tuple(a + b)] = 1
    
    return ret.keys()


ret = stupid(n, m, k)
print(*sorted(ret))
print(len(ret))