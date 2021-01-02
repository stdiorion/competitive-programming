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

for i in range(1, n + 1):
    child1 = (2 * i) % n if (2 * i) % n else n
    child2 = (2 * i + 1) % n if (2 * i + 1) % n else n
    print(child1, child2)