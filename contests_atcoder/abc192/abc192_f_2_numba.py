import numpy as np
from numba import njit, i8
readline = lambda: np.fromstring(input(), dtype=np.int64, sep=" ")


@njit((i8, i8, i8[:]), cache=True)
def solve(n, x, A):
    INF = 1 << 60
    res = INF
    for k in range(1, n + 1):
        dp = np.full((n + 1, n), -INF, np.int64)
        dp[0, 0] = 0
        for a in A:
            for i in range(k, 0, -1):
                for j in range(k):
                    dp[i, j] = max(dp[i, j], dp[i - 1, (j - a) % k] + a)
        res = min(res, (x - dp[k, x % k]) // k)
    return res

n, x = readline()
A = readline()
print(solve(n, x, A))