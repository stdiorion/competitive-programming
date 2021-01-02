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
MOD=998244353
INF=float('inf')

n, k = map(int, input().split())

s = []

for _ in range(k):
    l, r = map(int, input().split())
    s += list(range(l, r + 1))


# dp[i] = マスiに行く方法の個数
dp = [0] * (n + 1)
dp[1] = 1

for i in range(n + 1):
    for step in s:
        if i - step > 0:
            dp[i] += dp[i - step]
            dp[i] %= MOD
    

print(dp[n])