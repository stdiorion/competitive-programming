from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
a = map(int, input().split())

sum_a = 0

for ai in a:
    sum_a += 1/ai

ans = 1 / sum_a

print(ans)