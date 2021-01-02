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
p = list(map(int, input().split()))

unswapped = [i for i in range(1, n)]
swap_count = 1
swap_order = []

p_dif = [i - p[i-1] for i in range(1, n + 1)]

while swap_count < n:

    swap_count_prev = swap_count

    for i in reversed(unswapped):
        if p_dif[i - 1] < 0 < p_dif[i]:
            p_dif[i - 1], p_dif[i] = p_dif[i] - 1, p_dif[i - 1] + 1
            unswapped.remove(i)
            swap_count += 1
            swap_order.append(i)
    
    if swap_count == swap_count_prev:
        print(-1)
        exit()

print(*swap_order, sep="\n")