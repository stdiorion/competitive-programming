from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians
from fractions import Fraction
from decimal import Decimal
import sys
input=sys.stdin.readline
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')

h, w = map(int, input().split())

dist = [[-1] * w for _ in range(h)]

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

d = deque()

for i in range(h):
    for j, l in enumerate(list(input().rstrip())):
        if l == "#":
            dist[i][j] = 0
            d.append((i, j))

ans = 0

while d:
    y, x = d.popleft()

    depth = dist[y][x] + 1


    for m in moves:
        if (0 <= x + m[0] < w
        and 0 <= y + m[1] < h
        and dist[y + m[1]][x + m[0]]) == -1:
            d.append((y + m[1], x + m[0]))
            dist[y + m[1]][x + m[0]] = depth
            ans = max(ans, depth)

print(ans)