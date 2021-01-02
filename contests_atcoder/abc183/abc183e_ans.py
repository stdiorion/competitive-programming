# 以下の解説を参考に作成
# https://drken1215.hatenablog.com/entry/2020/11/16/204900

h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]
MOD = 10 ** 9 + 7

dp = [[0] * (w + 1) for _ in range(h + 1)]
X = [[0] * (w + 1) for _ in range(h + 1)]
Y = [[0] * (w + 1) for _ in range(h + 1)]
Z = [[0] * (w + 1) for _ in range(h + 1)]

dp[1][1] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):

        if field[i - 1][j - 1] == "#":
            continue

        left = X[i][j - 1]
        top = Y[i - 1][j]
        lefttop = Z[i - 1][j - 1]
        current = (dp[i][j] + left + top + lefttop) % MOD

        dp[i][j] = current
        X[i][j] += (left + current) % MOD
        Y[i][j] += (top + current) % MOD
        Z[i][j] += (lefttop + current) % MOD

print(dp[-1][-1])