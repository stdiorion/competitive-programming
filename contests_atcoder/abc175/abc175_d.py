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

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

unvisited = list(range(n))
g = []

while unvisited:
    start = unvisited.pop(-1)

    g.append({"sC": [c[start]], "len": 0, "loopgain": 0})

    now = start
    head = start

    while True:

        now = p[now] - 1

        if now == head:
            g[-1]["len"] = len(g[-1]["sC"])
            g[-1]["loopgain"] = max(0, g[-1]["sC"][-1])
            g[-1]["sC"] += [x + g[-1]["sC"][-1] for x in g[-1]["sC"]]
            break

        else:
            g[-1]["sC"].append(g[-1]["sC"][-1] + c[now])

            unvisited.remove(now)

ans = -INF

for graph in g:
    cycle, k_mod = divmod(k, graph["len"])
    for i in range(graph["len"]):
        for movedist in range(1, graph["len"] + 1):
            if movedist > k:
                continue

            if movedist > k_mod:
                ans = max(ans, graph["sC"][i + movedist] - graph["sC"][i] + (cycle - 1) * graph["loopgain"])
            else:
                ans = max(ans, graph["sC"][i + movedist] - graph["sC"][i] + cycle * graph["loopgain"])

print(ans)