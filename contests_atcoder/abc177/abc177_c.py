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

n = int(input())
a = list(map(int, input().split()))

sa = [0]
for x in a:
    sa.append((sa[-1] + x) % MOD)
del sa[0]

ans = 0
for i in range(1, n):
    ans += sa[i - 1] * a[i]
    ans %= MOD

print(ans)