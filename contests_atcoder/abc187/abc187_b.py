from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for pair in combinations(points, 2):
    dx = pair[0][0] - pair[1][0]
    dy = pair[0][1] - pair[1][1]
    if dx != 0 and -1 <= dy / dx <= 1:
        ans += 1

print(ans)