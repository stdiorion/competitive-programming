from collections import defaultdict
MOD = 998244353
n, s = map(int, input().split())
a = list(map(int, input().split()))

for l in range(n):
    dp = [defaultdict(int) for _ in range(n)]
    dp[l][a[l]] = 1
    for i in range(l + 1, n):
        dp[i][]