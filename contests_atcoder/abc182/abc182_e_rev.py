h, w, n, m = map(int, input().split())
field = [[0] * w for _ in range(h)]
field_brightness = [[0] * w for _ in range(h)]

for _ in range(n):
    a, b = map(int, input().split())
    field[a - 1][b - 1] = 1

for _ in range(m):
    a, b = map(int, input().split())
    field[a - 1][b - 1] = 2

for i in range(h):
    brightness = 0
    for j in range(w):
        if field[i][j] == 1:
            brightness = 1
        elif field[i][j] == 2:
            brightness = 0
        field_brightness[i][j] |= brightness

for i in range(h):
    brightness = 0
    for j in reversed(range(w)):
        if field[i][j] == 1:
            brightness = 1
        elif field[i][j] == 2:
            brightness = 0
        field_brightness[i][j] |= brightness

for j in range(w):
    brightness = 0
    for i in range(h):
        if field[i][j] == 1:
            brightness = 1
        elif field[i][j] == 2:
            brightness = 0
        field_brightness[i][j] |= brightness

for j in range(w):
    brightness = 0
    for i in reversed(range(h)):
        if field[i][j] == 1:
            brightness = 1
        elif field[i][j] == 2:
            brightness = 0
        field_brightness[i][j] |= brightness

ans = sum([sum(line) for line in field_brightness])
print(ans)