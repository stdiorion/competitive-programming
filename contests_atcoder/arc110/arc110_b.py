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
t = input()

s = "110" * (10 ** 5)

if t == "1":
    print(2 * 10 ** 10)
    exit()


for i in range(3):
    if t == s[i : i + n]:
        print(1 + (3 * 10 ** 10 - (i + n)) // 3)
        exit()

print(0)