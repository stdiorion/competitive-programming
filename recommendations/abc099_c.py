n = int(input())

dp = [10**7] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(n + 1):
    if i < n:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    for k in range(1, 8):
        if i + 6 ** k <= n:
            dp[i + 6 ** k] = min(dp[i + 6 ** k], dp[i] + 1)
        else:
            break
    for k in range(1, 8):
        if i + 9 ** k <= n:
            dp[i + 9 ** k] = min(dp[i + 9 ** k], dp[i] + 1)
        else:
            break

print(dp[n])