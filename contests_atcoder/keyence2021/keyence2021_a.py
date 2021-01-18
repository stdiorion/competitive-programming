n =int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_max = [a[0]]

for x in a[1:]:
    a_max.append(max(a_max[-1], x))

dp = [0] * n
dp[0] = a[0] * b[0]

for i in range(1, n):
    dp[i] = max(dp[i-1], b[i] * a_max[i])

print(*dp, sep="\n")