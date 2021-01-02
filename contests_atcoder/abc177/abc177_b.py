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
t = input()

ans = len(t)

for i in range(len(s) - len(t) + 1):
    count = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            count += 1
    
    ans = min(ans, count)

print(ans)