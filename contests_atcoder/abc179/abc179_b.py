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
d = [list(map(int, input().split())) for _ in range(n)]

zoro_count = 0

for roll in d:
    if roll[0] == roll[1]:
        zoro_count += 1
        if zoro_count >= 3:
            print("Yes")
            exit()
    else:
        zoro_count = 0

print("No")