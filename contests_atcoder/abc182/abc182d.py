n = int(input())
a = list(map(int, input().split()))

a_sum = [0]
for elem in a:
    a_sum.append(a_sum[-1] + elem)
del a_sum[0]

# dp_k = (a_k までの移動において一番右端にいるときの相対座標)
dp = [0] * (n + 1)
pos = 0

farthest = 0

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], a_sum[i - 1])
    farthest = max(farthest, dp[i] + pos)
    pos += a_sum[i - 1]


print(farthest)