# 間違ってた

from random import randint as ri

for t in range(100):
    n = ri(2, 2000)
    m = ri(1, int((n - 1) // 2))

    n -= n % 2

    ans = [(1 + i, n - i) for i in range(m)]

    contestants = [0] * n

    for i in range(n):
        for a, b in ans:
            a = (a - i) % n
            b = (b - i) % n
            contestants[a] += 1
            contestants[b] += 1

    if min(contestants) != max(contestants):
        print(n, m)
        print(contestants)
