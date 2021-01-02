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

from operator import mul
from functools import reduce
MOD=10**9+7
INF=float('inf')

def cmb(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

s = int(input())

ans = 0

for i in range(1, s // 3 + 1):
    ans += cmb(s - 2 * i - 1, i - 1) % MOD
    ans %= MOD

print(ans)