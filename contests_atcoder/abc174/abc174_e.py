import heapq
from math import ceil

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 0:
    print(max(a))
    exit()

sa = sum(a)
a_min = sa / (k + n - 1)

div = [1] * n

for i in range(n):
    c = int(a[i] // a_min)
    if c:
        k -= c - 1
        div[i] = c
if k <= 0:
    b = [(-x, x, 1) for x in a]
else:
    b = [(-a[i] / div[i], a[i], div[i]) for i in range(n)]

heapq.heapify(b)

for i in range(k):
    now = heapq.heappop(b)
    new = (-now[1] / (now[2] + 1), now[1], now[2] + 1)
    heapq.heappush(b, new)

ans = heapq.heappop(b)
print(ceil(-ans[0]))