n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
ox = [(1, 0, 0)]
oy = [(0, 1, 0)]
for _ in range(m):
    o = tuple(map(int, input().split()))
    ax, bx, cx = ox[-1]
    ay, by, cy = oy[-1]
    if o[0] == 1:
        ox.append((ay, by, cy))
        oy.append((-ax, -bx, -cx))
    elif o[0] == 2:
        ox.append((-ay, -by, -cy))
        oy.append((ax, bx, cx))
    elif o[0] == 3:
        ox.append((-ax, -bx, -cx + 2*o[1]))
        oy.append((ay, by, cy))
    elif o[0] == 4:
        ox.append((ax, bx, cx))
        oy.append((-ay, -by, -cy + 2*o[1]))

Q = int(input())
for _ in range(Q):
    t, p = map(int, input().split())
    x, y = points[p-1]
    ax, bx, cx = ox[t]
    ay, by, cy = oy[t]
    print(ax * x + bx * y + cx, ay * x + by * y + cy)