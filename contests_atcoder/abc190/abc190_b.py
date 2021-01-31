n, s, d = map(int, input().split())
magics = [list(map(int, input().split())) for _ in range(n)]

for m in magics:
    if m[0] < s and m[1] > d:
        print("Yes")
        exit()

print("No")