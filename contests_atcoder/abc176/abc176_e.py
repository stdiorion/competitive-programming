from itertools import accumulate,chain,combinations,groupby,permutations,product
from collections import deque,Counter
from bisect import bisect_left,bisect_right
from math import gcd,sqrt,sin,cos,tan,degrees,radians
from fractions import Fraction
from decimal import Decimal
import sys
input = lambda: sys.stdin.readline().rstrip()
#from sys import setrecursionlimit
#setrecursionlimit(10**7)
MOD=10**9+7
INF=float('inf')

from bisect import bisect_left, insort
from collections import defaultdict

H, W, m = map(int, input().split())
blocks = [tuple(map(int, input().split())) for _ in range(m)]

bomb_row = [0] * (H + 1)
bomb_col = [0] * (W + 1)
bomb_exists = defaultdict(bool)

for b in blocks:
    bomb_row[b[0]] += 1
    bomb_col[b[1]] += 1
    bomb_exists[(b[0], b[1])] = True


max_count_row = max(bomb_row)
max_count_col = max(bomb_col)

max_rows = [i for i, v in enumerate(bomb_row) if v == max_count_row]
max_cols = [i for i, v in enumerate(bomb_col) if v == max_count_col]

for j in max_rows:
    for k in max_cols:
        if not bomb_exists[(j, k)]:
            print(max_count_row + max_count_col)
            exit()

print(max_count_row + max_count_col - 1)