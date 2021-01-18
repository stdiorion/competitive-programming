import scipy.special
MOD = 10 ** 9 + 7
n, m = map(int, input().split())

dp = [0] * (n + 1)
dp[1] = (m - n + 1) * (m - n) % MOD
dp[2] = (m - n + 2) * (m - n + 1) * (1 + max(0, 2 * (m - n)) + max(0, (m - n - 1) * (m - n))) % MOD

for i in range(3, n + 1):
    dp[i] = (i - 1) * ((m - n + i - 1) * dp[i-1] + (m - n + i - 2) * dp[i-2]) % MOD

print(dp[n])