h, w = map(int, input().split())

blocked = []

for i in range(h):
    l, r = map(int, input().split())
    blocked.append((l-1, r-1))

x = 0
y = 0

for i in range(h):
    if blocked[i][0] <= x <= blocked[i][1]:
        x = blocked[i][1] + 1
    if x >= w:
        print(-1)
        continue
    y += 1
    print(x + y)