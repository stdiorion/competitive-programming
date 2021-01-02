from sys import stdin
input = stdin.readline

N, M, T = map(int, input().split())
a = [list(map(int, input().split())) for i in range(M)]

# 初期残量N
battery = N

ans = "Yes"

# 前回の区切りの時間
prev_time = 0

# cafe[0]:到着時間 cafe[1]:出発時間
for cafe in a:
    battery -= cafe[0] - prev_time
    if battery <= 0:
        ans = "No"
        break
    battery += cafe[1] - cafe[0]
    if battery > N:
        battery = N
    prev_time = cafe[1]

battery -= T - prev_time

if battery <= 0:
    ans = "No"

print(ans)