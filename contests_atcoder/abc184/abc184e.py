import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

H, W = map(int, input().split())
a = [list(input().rstrip()) for i in range(H)]

t = [[100100] * W for _ in range(H)]

goal = (-1, -1)

for i, col in enumerate(a):
    if "S" in col:
        sx, sy = i, col.index("S")
    if "G" in col:
        goal = (i, col.index("G"))
        t[goal[0]][goal[1]] = 0

def findport(st):
    for i, col in enumerate(a):
        if st in col:
            return (i, col.index(st))

def seenext(x, y):
    if x > 0 and a[x-1][y] != "#":
        if t[x-1][y] > t[x][y] + 1:
            t[x-1][y] = t[x][y] + 1
            seenext(x-1, y)
    if y > 0 and a[x][y-1] != "#":
        if t[x][y-1] > t[x][y] + 1:
            t[x][y-1] = t[x][y] + 1
            seenext(x, y-1)
    if x < H-1 and a[x+1][y] != "#":
        if t[x+1][y] > t[x][y] + 1:
            t[x+1][y] = t[x][y] + 1
            seenext(x+1, y)
    if y < W-1 and a[x][y+1] != "#":
        if t[x][y+1] > t[x][y] + 1:
            t[x][y+1] = t[x][y] + 1
            seenext(x, y+1)
    if a[x][y].islower():
        dst = findport(a[x][y])
        if t[dst[0]][dst[1]] > t[x][y] + 1:
            t[dst[0]][dst[1]] = t[x][y] + 1
            seenext(*dst)

seenext(*goal)

print(t[sx][sy] if t[sx][sy] != 100100 else -1)