h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0

for i in range(h - 1):
    for j in range(w - 1):
        cnt = 0
        cnt += (s[i][j] == "#")
        cnt += (s[i+1][j] == "#")
        cnt += (s[i][j+1] == "#")
        cnt += (s[i + 1][j + 1] == "#")
        if cnt == 1 or cnt == 3:
            ans += 1

print(ans)