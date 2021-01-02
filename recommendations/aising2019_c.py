from collections import deque

h, w = map(int, input().split())

field = [list(input().rstrip()) for _ in range(h)]

visited = [[False] * w for _ in range(h)]

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(sy, sx):
    global visited

    d = deque()
    d.append((sy, sx))

    color_count = [0, 0]

    while d:
        y, x = d.popleft()

        color_count[field[y][x] == "."] += 1

        for m in moves:
            if (0 <= x + m[0] < w 
            and 0 <= y + m[1] < h 
            and field[y + m[1]][x + m[0]] != field[y][x] 
            and not visited[y + m[1]][x + m[0]]):
                d.append((y + m[1], x + m[0]))
                visited[y + m[1]][x + m[0]] = True
    
    return color_count[0] * color_count[1]

ans = 0

for i in range(h):
    for j in range(w):
        if not visited[i][j]:
            visited[i][j] = True
            ans += bfs(i, j)

print(ans)