h, w, k = map(int, input().split())
a = [input() for _ in range(h)]

counter = 1
ans = [[0] * w for _ in range(h)]
cop = None

for i, row in enumerate(a):
    first = True
    for j, x in enumerate(row):
        if x == "#":
            if first:
                first = False
            else:
                counter += 1
        ans[i][j] = counter
    if first:
        if counter > 1:
            ans[i] = ans[i - 1]
        else:
            cop = i
    else:
        counter += 1

if cop is not None:
    for i in range(cop + 1):
        ans[i] = ans[cop + 1]

for x in ans:
    print(*x)