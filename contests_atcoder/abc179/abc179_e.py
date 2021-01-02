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
INF=float('inf')

n, x, MOD = map(int, input().split())

a = [x]

if n == 1:
    print(x)
    exit()

for i in range(n - 1):
    new_value = a[-1] ** 2 % MOD
    if new_value in a:
        idx = a.index(new_value)
        ans = 0
        ans += sum(a[:idx])
        n -= idx
        ans += sum(a[idx:]) * (n // len(a[idx:]))
        ans += sum(a[idx:idx + n % len(a[idx:])])
        print(ans)
        exit()
    else:
        a.append(new_value)

print(sum(a))