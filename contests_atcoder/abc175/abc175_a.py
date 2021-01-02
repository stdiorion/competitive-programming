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

s = input()

ans = 0
cnt = 0

for l in s:
    if l == "R":
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)

print(ans)