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
p = [list(map(int, input().split())) for _ in range(n)]

f1 = [x[0] - x[1] for x in p]
f2 = [x[0] + x[1] for x in p]

print(max(max(f1) - min(f1), max(f2) - min(f2)))