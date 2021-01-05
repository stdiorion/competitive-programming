from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

h, n = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) >= h:
    print("Yes")
else:
    print("No")