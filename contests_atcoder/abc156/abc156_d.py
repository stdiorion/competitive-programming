from functools import reduce

MOD = 10 ** 9 + 7
n, a, b = map(int, input().split())

def comb(n, r):
    numer = reduce(lambda x, y: x * y % MOD, (n - r + k + 1 for k in range(r)))
    denom = reduce(lambda x, y: x * y % MOD, (k + 1 for k in range(r)))
    return numer * pow(denom, MOD - 2, MOD)

print(max(0, (pow(2, n, MOD) - 1 - comb(n, a) - comb(n, b)) % MOD))