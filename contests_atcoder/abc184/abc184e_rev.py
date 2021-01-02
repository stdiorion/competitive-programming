from sys import stdin
input = stdin.readline

H, W = map(int, input().split())
field = [list(input().rstrip()) for i in range(H)]

pos_start = (-1, -1)

warp = [[] for _ in range(26)]

for y, line in enumerate(field):
    for x, cell in enumerate(line):
        if cell == "S":
            pos_start = (y, x)
        elif cell.islower():
            warp[ord(cell) - ord("a")].append((y, x))

t = 0
pos_now = [pos_start]

while True:
    if len(pos_now):

        pos_next = []

        for pos in reversed(pos_now):

            cell = field[pos[0]][pos[1]]

            if cell == "G":
                print(t)
                exit()

            del pos_now[-1]

            # 一回踏んだマスは二度と踏まないので埋める
            field[pos[0]][pos[1]] = "#"

            if pos[0] > 0 and field[pos[0] - 1][pos[1]] != "#":
                pos_next.append((pos[0] - 1, pos[1]))

            if pos[1] > 0 and field[pos[0]][pos[1] - 1] != "#":
                pos_next.append((pos[0], pos[1] - 1))

            if pos[0] < H - 1 and field[pos[0] + 1][pos[1]] != "#":
                pos_next.append((pos[0] + 1, pos[1]))

            if pos[1] < W - 1 and field[pos[0]][pos[1] + 1] != "#":
                pos_next.append((pos[0], pos[1] + 1))

            if cell.islower() and warp[ord(cell) - ord("a")] != 0:
                for dst in warp[ord(cell) - ord("a")]:
                    pos_next.append((dst[0], dst[1]))

                # 一回使ったワープは二度と使わない
                warp[ord(cell) - ord("a")] = 0
        
        pos_now = list(set(pos_next)) # 重複のぞく
    
    else:
        print(-1)
        exit()
    
    t += 1