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
bars = list(map(int, input().split()))

ans = 0

for comb in combinations(range(n), 3):
    c = [bars[i] for i in comb]
    c.sort()
    if c[0] == c[1] or c[1] == c[2]:
        continue
    if c[0] + c[1] > c[2]:
        ans += 1

print(ans)