n, m, k = map(int, input().split())
a = set(map(int, input().split()))

dp = [0] * n + [0] * (m + 1)

for i in range(n, 0, -1):
    if i - 1 in a:
        continue
    
    dp[i-1] = (m+1)/m * dp[i] - dp[i+m]/m

print(dp[0])