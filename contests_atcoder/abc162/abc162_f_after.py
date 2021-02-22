INF = float("inf")
n = int(input())
a = list(map(int, input().split())) + [0] * 10

dp = [[-INF] * 3 for _ in range(n + 10)]
dp[0][0] = a[0]
dp[1][1] = a[1]
dp[2][2] = a[2]

for i in range(n):
    dp[i + 2][0] = max(dp[i + 2][0], dp[i][0] + a[i + 2])
    dp[i + 2][1] = max(dp[i + 2][1], dp[i][1] + a[i + 2])
    dp[i + 2][2] = max(dp[i + 2][2], dp[i][2] + a[i + 2])
    dp[i + 3][1] = max(dp[i + 3][1], dp[i][0] + a[i + 3])
    dp[i + 3][2] = max(dp[i + 3][2], dp[i][1] + a[i + 3])
    dp[i + 4][2] = max(dp[i + 4][2], dp[i][0] + a[i + 4])

print(max(dp[n - 1][2], dp[n - 2][1], dp[n - 3][0], dp[n - 1][1], dp[n - 2][0]))