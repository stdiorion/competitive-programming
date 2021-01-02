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
    s.append((l, r + 1))


# dp[i] = マスiに行く方法の個数
dp = [0] * (n + 1)
dp[1] = 1

# sdp[i] = sum(dp[0:i+1])
sdp = [0] * (n + 1)
sdp[1] = 0

for i in range(1, n + 1):
    for step in s:
        if i - step[0] > 0:
            dp[i] += sdp[i - step[0]] - sdp[max(0, i - step[1])]
            dp[i] %= MOD
    sdp[i] += sdp[i - 1] + dp[i]
    sdp[i] %= MOD


print(dp[n])