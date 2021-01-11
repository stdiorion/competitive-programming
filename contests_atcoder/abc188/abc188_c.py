from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

n = int(input())
A = list(map(int, input().split()))
a = A[:]

for i in range(n - 1, 0, -1):
    a = [max(a[2*i], a[2*i+1]) for i in range(2 ** i)]

print(A.index(min(a)) + 1)