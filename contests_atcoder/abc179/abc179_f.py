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

n, Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

ans = (n - 2) ** 2

T = n
L = n
T_prev, L_prev = T, L

v_count = [n - 2] * (n + 1)
h_count = [n - 2] * (n + 1)

for q in queries:
    if q[0] == 1:
        if q[1] > L:
            ans -= v_count[q[1]]
        else:
            ans -= T - 2
            L_prev = L
            L = q[1]
            for i in range(L, L_prev):
                v_count[i] = T - 2
    else:
        if q[1] > T:
            ans -= h_count[q[1]]
        else:
            ans -= L - 2
            T_prev = T
            T = q[1]
            for i in range(T, T_prev):
                h_count[i] = L - 2

print(ans)