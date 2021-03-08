import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from functools import lru_cache
MOD = 10 ** 9 + 7

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

@lru_cache(None)
def search(i, j):
    res = 1
    now = a[i][j]
    if i > 0 and a[i - 1][j] > now:
        res += search(i - 1, j)
    if j > 0 and a[i][j - 1] > now:
        res += search(i, j - 1)
    if i < h - 1 and a[i + 1][j] > now:
        res += search(i + 1, j)
    if j < w - 1 and a[i][j + 1] > now:
        res += search(i, j + 1)
    return res % MOD

print(sum(search(i, j) for i in range(h) for j in range(w)) % MOD)