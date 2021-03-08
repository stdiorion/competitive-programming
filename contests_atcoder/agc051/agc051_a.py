from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 7)
MOD = 998244353
d = int(input())

@lru_cache(None)
def solve(a, b):
    if a <= 0 or b <= 0:
        return 1
    else:
        return (solve(a - 1, b) + solve(a, b - 1)) % MOD

print(solve(d, d) // 2)