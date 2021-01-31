n, m = map(int, input().split())
cond = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
choice = [tuple(map(int, input().split())) for _ in range(k)]

ans = 0

for i in range(1 << k):
    dish = [0] * n
    for j in range(k):
        dish[choice[j][(i >> j) % 2] - 1] += 1
    ans_ = 0
    for a, b in cond:
        ans_ += int(dish[a - 1] > 0 and dish[b - 1] > 0)
    ans = max(ans, ans_)

print(ans)