from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
S = [input() for _ in range(n)]

exc = []
non_exc = []

for s in S:
    if s[0] == "!":
        exc.append(s[1:])
    else:
        non_exc.append(s)

exc.sort()
non_exc.sort()

i1, i2 = 0, 0

while i1 < len(exc) and i2 < len(non_exc):
    if exc[i1] == non_exc[i2]:
        print(exc[i1])
        exit()
    elif exc[i1] > non_exc[i2]:
        i2 += 1
    else:
        i1 += 1

print("satisfiable")