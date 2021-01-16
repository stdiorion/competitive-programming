from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

k = int(input())
sept = 7

for i in range(k):
    if sept % k == 0:
        print(i + 1)
        exit()
    sept = (sept * 10 + 7) % k
else:
    print(-1)