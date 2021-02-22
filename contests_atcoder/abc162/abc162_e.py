MOD = 10 ** 9 + 7
n, k = map(int, input().split())

dp = [0] * (k + 1)
ans = 0

for x in range(k, 0, -1):
    dp[x] = pow(k // x, n, MOD)
    for i in range(2 * x, k + 1, x):
        dp[x] -= dp[i]
    ans += dp[x] * x
    ans %= MOD

print(ans)