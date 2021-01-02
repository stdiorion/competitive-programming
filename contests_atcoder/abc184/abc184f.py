import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, T = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (T + 1) for i in range(N + 1)]

for i, t in enumerate(A):
    for j in range(T + 1):
        if j - t >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - t] + t)
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[N][T])