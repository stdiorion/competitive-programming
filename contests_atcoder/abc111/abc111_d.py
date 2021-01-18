n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

m = 39
arms = [2 ** i for i in reversed(range(m))]

if sum(points[0]) % 2 == 0:
    m += 1
    arms.append(1)

ans = []

for p in points:

    move = ""

    px, py = p
    x, y = 0, 0

    for i in range(m):
        if abs(px - x) > abs(py - y):
            if px > x:
                move += "R"
                x += arms[i]
            else:
                move += "L"
                x -= arms[i]
        else:
            if py > y:
                move += "U"
                y += arms[i]
            else:
                move += "D"
                y -= arms[i]

    if px == x and py == y:
        ans.append(move)
    else:
        print(-1)
        exit()

print(m)
print(*arms)
print(*ans, sep="\n")