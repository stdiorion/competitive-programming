""" 
dp[i][j][k] = i頂点n辺グラフ長さ最大値kの組み合わせ数

dp[i][j][k] = dp[i - k][n - usededge][_] for _ in range(k + 1)


よくわからん
 """
import math
from operator import mul
from functools import reduce

def comb(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

MOD = 10 ** 9 + 7

n, m, l = map(int, input().split())

dp = [[[1] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

for i in range(n + 1):
    for j in range(m + 1):
        for k in range(1, l + 1):
            if i - k >= 0 and j - k + 1 >= 0:
                if k > 2:
                    dp[i][j][k] *= (k + 1) * math.factorial(k - 1) / 2 % MOD
                    for _ in range(1, k + 1):
                        dp[i][j][k] *= dp[i - k][j - k + 1][_]
                        dp[i][j][k] %= MOD
                elif k == 1:
                    dp[i][j][k] *= 2
                    for _ in range(1, k + 1):
                        dp[i][j][k] *= dp[i - k][j - k + 1][_] + dp[i - k][j - k][_]
                        dp[i][j][k] %= MOD

                dp[i][j][k] *= comb(i, k) % MOD
                dp[i][j][k] %= MOD

print(dp[n][m][l])