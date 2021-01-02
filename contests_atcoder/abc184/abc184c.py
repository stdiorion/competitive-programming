from sys import stdin
input = stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

def is_movable(p1, q1, p2, q2):
    if p1 + q1 == p2 + q2 or p1 - q1 == p2 - q2 or abs(p1 - p2) + abs(q1 - q2) <= 3:
        return True
    else:
        return False


if x1 == x2 and y1 == y2: print(0)
elif is_movable(x1, y1, x2, y2): print(1)
elif (x1 + x2 + y1 + y2) % 2 == 0: print(2)
else:
    ans = 3
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) <= 3 and is_movable(x1 + i, y1 + j, x2, y2):
                ans = 2
    print(ans)