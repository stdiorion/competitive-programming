MOD = 998244353

h, w, k = map(int, input().split())

operator = [["N"] * w for _ in range(h)]

for _ in range(k):
    y, x, c = input().split()
    y = int(y) - 1
    x = int(x) - 1
    operator[y][x] = c


dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1

dpp = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(h):
    for j in range(w):
        if operator[i][j] == "N":
            dpp[i+1][j] += dp[i][j] * 2 % MOD
            dpp[i][j+1] += dp[i][j] * 2 % MOD
        else:
            if operator[i][j] == "X":
                r = 1
                d = 1
            elif operator[i][j] == "R":
                r = 1
                d = 0
            elif operator[i][j] == "D":
                r = 0
                d = 1
            dp[i+1][j] += dp[i][j] * d % MOD
            dp[i][j+1] += dp[i][j] * r % MOD

            dpp[i+1][j] += dpp[i][j] * d % MOD
            dpp[i][j+1] += dpp[i][j] * r % MOD

print(dp[-2][-2] % MOD)