r, c, k = map(int, input().split())
items = [[0] * c for _ in range(r)]

for _ in range(k):
    y, x, v = map(int, input().split())
    items[y-1][x-1] = v

dp0 = [[0] * c for __ in range(r)]
dp1 = [[0] * c for __ in range(r)]
dp2 = [[0] * c for __ in range(r)]
dp3 = [[0] * c for __ in range(r)]

for y in range(r):
    for x in range(c):
        if y != 0:
            dp0[y][x] = max(dp0[y - 1][x], dp1[y - 1][x], dp2[y - 1][x], dp3[y - 1][x])
            dp1[y][x] = max(dp0[y - 1][x], dp1[y - 1][x], dp2[y - 1][x], dp3[y - 1][x]) + items[y][x]
        
        if x != 0:
            dp0[y][x] = max(dp0[y][x], dp0[y][x - 1])
            dp1[y][x] = max(dp0[y][x - 1] + items[y][x], dp1[y][x - 1], dp1[y][x])
            dp2[y][x] = max(dp1[y][x - 1] + items[y][x], dp2[y][x - 1], dp2[y][x])
            dp3[y][x] = max(dp2[y][x - 1] + items[y][x], dp3[y][x - 1], dp3[y][x])
        else:
            dp1[y][x] = dp0[y][x] + items[y][x]

print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))