from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import combinations, permutations
from math import gcd, sin, cos, tan, degrees, radians
import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
INF = float("inf")

h, w, k = map(int, input().split())
field = [list(input()) for _ in range(h)]
F = sum(field, [])

ans = 0

for bit in range(1 << (h + w)):
    f = F[:]
    for i in range(h + w):
        if (bit >> i) % 2:
            if i < h:
                for j in range(i * w, (i + 1) * w):
                    f[j] = "."
            else:
                i -= h
                for j in range(i, h * w, w):
                    f[j] = "."
    if f.count("#") == k:
        ans += 1
print(ans)