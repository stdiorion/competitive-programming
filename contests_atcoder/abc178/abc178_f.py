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
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ca = Counter(a)
cb = Counter(b)

for i in range(1, n + 1):
    if ca[i] + cb[i] > n:
        print("No")
        exit()

print("Yes")

count_max = max(ca.most_common(1)[0][1], cb.most_common(1)[0][1])

for i in range(n):
    ans = b[-((count_max + i - 1) % n + 1):] + b[:-((count_max + i - 1) % n + 1)]

    ok = True
    for j in range(n):
        if a[j] == ans[j]:
            ok = False

    if ok:
        print(*ans)
        exit()