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

def count_divisors(n):
    i = 1
    cnt = 0
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return cnt


ans = 0

for c in range(n-1, 0, -1):
    ans += count_divisors(n - c)

print(ans)