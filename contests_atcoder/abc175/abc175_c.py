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

x, k, d = map(int, input().split())

if abs(x) >= k * d:
    print(abs(x) - k * d)
else:
    n = (k + x / d) // 2
    m = n + 1
    def f(q):
        return abs(x + (k - 2 * q) * d)
    print(int(min(f(n), f(m))))