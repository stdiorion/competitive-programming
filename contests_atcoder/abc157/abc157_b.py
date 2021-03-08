a = [tuple(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

hit = [[False] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            hit[i][j] = True

for i in range(3):
    judge = True
    for j in range(3):
        judge &= hit[i][j]
    if judge:
        print("Yes")
        exit()


for j in range(3):
    judge = True
    for i in range(3):
        judge &= hit[i][j]
    if judge:
        print("Yes")
        exit()

if hit[0][0] & hit[1][1] & hit[2][2]:
    print("Yes")
    exit()
if hit[2][0] & hit[1][1] & hit[0][2]:
    print("Yes")
    exit()
print("No")