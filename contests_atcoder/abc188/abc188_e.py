from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, m = map(int, input().split())
price = list(map(int, input().split()))

path_to = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    path_to[y - 1].append(x - 1)

sell_value = [-INF] * n
ans = -INF

for i in range(n - 1, -1, -1):
    for frm in path_to[i]:
        sell_value[frm] = max(price[i], sell_value[frm], sell_value[i])
    ans = max(ans, sell_value[i] - price[i])

print(ans)