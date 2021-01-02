import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

n = int(input())

nails = [tuple(map(int, input().split())) for _ in range(n)]

# コーナーケース
#nails = [(0, i) for i in range(-99, 100, 1)]
#nails = [(0, i) for i in range(-99, 100, 2)]


r = 100

maxgap = 200

def draw():
    if r % 40 > 1:
        return

    fig = plt.figure()
    ax = plt.axes()
    c = patches.Circle(xy=(bx, by), radius=r, fc='g', ec='r')
    ax.add_patch(c)
    ax.set_aspect('equal')

    plt.scatter([s[0] for s in nails], [s[1] for s in nails])
    plt.show()

def walkalong(x):
    y = 100 - r

    nearest = (200, 0)
    to_nearest = 400

    for n in nails:
        if n[0] > x and n[1] > 100 - 2 * r and n[0] - (r ** 2 - (n[1] - y) ** 2) ** 0.5 < to_nearest:
            nearest = n
            to_nearest = n[0] - (r ** 2 - (n[1] - y) ** 2) ** 0.5
    
    if nearest == (200, 0):
        print(r)
        exit()
    else:
        global maxgap
        global bx
        global by
        maxgap = 100 - nearest[1]
        bx = to_nearest
        by = y
        draw()
        walkaround(nearest, math.atan2(y - nearest[1], to_nearest - nearest[0]))

def walkaround(pivot, start_angle):
    global maxgap
    global bx
    global by

    obstacles = [] # [(relative angle, coordinate, type)]

    if pivot[1] + r * math.sin(start_angle) > 100 or pivot[1] - r <= -100:
        return False


    # collide with the ceiling
    if pivot[1] > 100 - 2 * r:
        obstacles.append(((math.acos((r + pivot[1] - 100) / r) - math.pi / 2 - start_angle) % (2 * math.pi), (pivot[0] + (r ** 2 - (r + pivot[1] - 100) ** 2) ** 0.5, 100), "ceil"))
    # collide with the floor
    if pivot[1] < -100 + 2 * r:
        obstacles.append(((math.acos((r - pivot[1] - 100) / r) + math.pi / 2 - start_angle) % (2 * math.pi), (pivot[0] - (r ** 2 - (r - pivot[1] - 100) ** 2) ** 0.5, -100), "floor"))
        maxgap = max(maxgap, pivot[1] + 100)

    for n in nails:
        # collide with one of the nails
        d = ((n[0] - pivot[0]) ** 2 + (n[1] - pivot[1]) ** 2) ** 0.5
        if 0 < d ** 2 < (2 * r) ** 2:
            angle = 0.5 * math.acos(1 - d ** 2 / (2 * r ** 2)) + math.atan2(n[1] - pivot[1], n[0] - pivot[0]) - math.pi / 2 - start_angle
            # 誤差対策
            if (n[0] - bx) ** 2 + (n[1] - by) ** 2 < r ** 2:
                angle += 0.000001

            obstacles.append((angle % (2 * math.pi), n, "nail"))
            maxgap = max(maxgap, d)

    obstacles.sort()

    if obstacles[0][2] == "ceil":
        walkalong(obstacles[0][1][0])

    elif obstacles[0][2] == "nail":
        d = ((obstacles[0][1][0] - pivot[0]) ** 2 + (obstacles[0][1][1] - pivot[1]) ** 2) ** 0.5
        angle = obstacles[0][0] + start_angle - math.acos(1 - d ** 2 / (2 * r ** 2))

        bx = obstacles[0][1][0] + r * math.cos(angle)
        by = obstacles[0][1][1] + r * math.sin(angle)

        draw()

        walkaround(obstacles[0][1], angle)

while r > 0:
    bx, by = -200, 100 - r
    walkalong(bx)
    r = maxgap / 2

print(r)