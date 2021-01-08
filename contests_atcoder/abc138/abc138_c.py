from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())

v = list(map(int, input().split()))

v.sort()

nabe = v[0]

v = v[1:]

for x in v:
    nabe = (nabe + x) / 2

print(nabe)