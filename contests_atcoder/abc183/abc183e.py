h, w = map(int, input().split())
field = [list(input()) for _ in range(h)]

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if field[i][j] == "#":
            continue
        di = 1
        while i + di < h and field[i + di][j] != "#":
            dp[i + di][j] += dp[i][j]
            di += 1
        dj = 1
        while j + dj < w and field[i][j + dj] != "#":
            dp[i][j + dj] += dp[i][j]
            dj += 1
        dl = 1
        while j + dl < w and i + dl < h and field[i + dl][j + dl] != "#":
            dp[i + dl][j + dl] += dp[i][j]
            dl += 1
        
        

print(dp[-2][-2] % (10 ** 9 + 7))