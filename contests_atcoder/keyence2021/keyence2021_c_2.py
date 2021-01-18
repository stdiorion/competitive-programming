from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 998244353

h, w, k = map(int, input().split())

operator = [["N"] * min(w - max(i - h + 1, 0), h, i - max(i - h + 1, 0) + 1) for i in range(h+w-1)]

for _ in range(k):
    y, x, c = input().split()
    y = int(y) - 1
    x = int(x) - 1
    i = x + y
    k = x - max(0, i - h + 1)
    operator[i][k] = c

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1

for i in range((h+w-2)):

    n_count = 0

    j = max(i - h + 1, 0)

    operator_l = operator[i]

    n_count = operator_l.count("N")
    
    power_ = pow(3, n_count - 1, MOD) if n_count else 1
    power = power_ * 3 % MOD if n_count else 1

    for k in range(min(w - j, h, i - j + 1)):
        y, x = i-j-k, j+k
        now = dp[y][x]
        if operator_l[k] == "N":
            now = now * power_ % MOD

            dp[y+1][x] += now * 2 % MOD
            dp[y][x+1] += now * 2 % MOD

        else:
            now = now * power % MOD

            if operator_l[k] == "X":
                dp[y][x+1] += now
                dp[y+1][x] += now
            elif operator_l[k] == "R":
                dp[y][x+1] += now
            elif operator_l[k] == "D":
                dp[y+1][x] += now

if operator[-1][-1] == "N":
    dp[-2][-2] *= 3

print(dp[-2][-2] % MOD)