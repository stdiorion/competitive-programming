from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n, d = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for p in points:
    if p[0] ** 2 + p[1] ** 2 <= d ** 2:
        ans += 1

print(ans)