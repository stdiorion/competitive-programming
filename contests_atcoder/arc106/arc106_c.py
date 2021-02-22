n, m = map(int, input().split())

if n == 1:
    if m == 0:
        print(1, 2)
    else:
        print(-1)
    exit()

if m < 0 or m + 2 > n:
    print(-1)
else:
    print(1, 2 * (m + 2))
    for i in range(1, m + 2):
        print(2 * i, 2 * i + 1)
    for j in range(m + 2, n):
        print(2 * j + 1, 2 * j + 2)