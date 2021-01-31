from functools import reduce, lru_cache
from operator import xor
INF = float("inf")

n = int(input())
a = list(map(int, input().split()))

k = reduce(xor, a[2:]) if len(a) > 2 else 0

@lru_cache(None)
def solve(x, y, k):
    if (x % 2) ^ (y % 2) != k % 2:
        return INF
    if k == 0:
        return (x - y) // 2 if x >= y else INF
    
    return min(2 * solve(x // 2, y // 2, k // 2), 2 * solve((x - 1) // 2, (y + 1) // 2, k // 2) + 1)

ans = solve(a[0], a[1], k)

if ans < a[0]:
    print(ans)
else:
    print(-1)