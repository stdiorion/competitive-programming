from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

dot = 0

for i in range(n):
    dot += a[i] * b[i]

if dot == 0:
    print("Yes")
else:
    print("No")