from collections import deque
import sys
input = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7
INF = float("inf")

h, w, k = map(int, input().split())
x1, y1, x2, y2 = (int(x) - 1 for x in input().split())
field = [input() for _ in range(h)]

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

d = deque()
cost = [[INF] * w for _ in range(h)]

d.append((x1, y1))
cost[x1][y1] = 0

while d:
    x, y = d.popleft()

    if (x, y) == (x2, y2):
        print(cost[x][y])
        exit()

    for dx, dy in directions:
        for i in range(1, k + 1):
            x_to, y_to = x + dx * i, y + dy * i
            if not (0 <= x_to < h and 0 <= y_to < w) or field[x_to][y_to] == 64:
                break

            new_cost = cost[x][y] + 1

            if new_cost < cost[x_to][y_to]:
                cost[x_to][y_to] = new_cost
                d.append((x_to, y_to))
            elif new_cost > cost[x_to][y_to]:
                break

print(-1)