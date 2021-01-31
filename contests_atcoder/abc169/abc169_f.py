MOD = 998244353

n, s = map(int, input().split())
A = list(map(int, input().split()))

dp = [1] + [0] * s

for a in A:
    dp_next = [x * 2 for x in dp]
    for i, x in enumerate(dp[:-a]):
        dp_next[i+a] += x
    dp_next = [x % MOD for x in dp_next]
    dp = dp_next[:]
print(dp[s])