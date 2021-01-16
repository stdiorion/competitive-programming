import heapq
from math import ceil
from random import randint

for _ in range(10000):
    n, k = randint(1, 10), randint(1, 10)
    K = k
    a = [randint(1, 10) for _ in range(n)]

    if k == 0:
        print(max(a))
        exit()

    #---
    b1 = [(-a[i], a[i], 1) for i in range(n)]

    heapq.heapify(b1)
    for i in range(k):
        now = heapq.heappop(b1)
        new = (-now[1] / (now[2] + 1), now[1], now[2] + 1)
        heapq.heappush(b1, new)

    ans1 = ceil(-heapq.heappop(b1)[0])
    #---

    sa = sum(a)
    a_min = sa / (k + n - 1)

    div = [1] * n

    for i in range(n):
        c = int(a[i] // a_min)
        if c:
            k -= c - 1
            div[i] = c

    b = [(-a[i] / div[i], a[i], div[i]) for i in range(n)]

    heapq.heapify(b)

    for i in range(k):
        now = heapq.heappop(b)
        new = (-now[1] / (now[2] + 1), now[1], now[2] + 1)
        heapq.heappush(b, new)

    ans = ceil(-heapq.heappop(b)[0])
    
    if ans != ans1:
        print(n, K)
        print(*a)
        print(ans, ans1)
